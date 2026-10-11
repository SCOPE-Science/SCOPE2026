"""Exact rational tests for products of binary conditional expectations.

Run with Python 3 standard library. Finite tests check algebraic identities;
the all-probability-space norm theorem requires the accompanying proof.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import isclose


def matmul(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def subtract(A, B):
    return [[x-y for x,y in zip(row_a,row_b)]
            for row_a,row_b in zip(A,B)]


def matrix_for_event(weights, event):
    n=len(weights)
    a=sum(weights[i] for i in event)
    assert 0<a<1
    u=[int(i in event)-a for i in range(n)]
    alpha=a*(1-a)
    E=[[weights[j] for j in range(n)] for i in range(n)]
    P=[[E[i][j]+u[i]*u[j]*weights[j]/alpha for j in range(n)]
       for i in range(n)]
    return a,alpha,u,P


def verify(weights, event_sequence):
    n=len(weights)
    E=[[weights[j] for j in range(n)] for i in range(n)]
    rec=[matrix_for_event(weights,e) for e in event_sequence]
    W=rec[0][3]
    # P_m ... P_1, not opposite order.
    for _,_,_,P in rec[1:]:
        W=matmul(P,W)
    covariance=[]
    for left,right in zip(rec,rec[1:]):
        cov=sum(weights[i]*left[2][i]*right[2][i] for i in range(n))
        covariance.append(cov)
    c=F(1)
    for cov in covariance:c*=cov
    for _,alpha,_,_ in rec:c/=alpha
    expected=[[c*rec[-1][2][i]*rec[0][2][j]*weights[j] for j in range(n)]
              for i in range(n)]
    assert subtract(W,E)==expected
    # Exact scalar for every power, including nilpotent cases.
    cyclic_cov=sum(weights[i]*rec[-1][2][i]*rec[0][2][i]
                   for i in range(n))
    lam=c*cyclic_cov
    W2=matmul(W,W)
    assert subtract(W2,E)==[[lam*v for v in row] for row in expected]
    return rec,c,expected


def H(a,p):
    return float(a*(1-a)**p+(1-a)*a**p)**(1/p)


def test_norm(weights, seq, p):
    rec,c,_=verify(weights,seq)
    q=p/(p-1)
    up=[float(z) for z in rec[0][2]]
    f=[(1 if z>0 else -1)*abs(z)**(q-1) for z in up]
    fnorm=sum(float(w)*abs(z)**p for w,z in zip(weights,f))**(1/p)
    f=[z/fnorm for z in f]
    weighted_input=sum(float(w)*float(u)*fi for w,u,fi
                       in zip(weights,rec[0][2],f))
    output=[float(c)*float(u)*weighted_input for u in rec[-1][2]]
    observed=sum(float(w)*abs(v)**p for w,v in zip(weights,output))**(1/p)
    predicted=abs(float(c))*H(rec[-1][0],p)*H(rec[0][0],q)
    assert isclose(observed,predicted,rel_tol=1e-11,abs_tol=1e-13)


def main():
    weights=[F(1,12),F(2,12),F(3,12),F(6,12)]
    events=[frozenset(e) for r in range(1,len(weights))
            for e in combinations(range(len(weights)),r)]
    tests=0
    # 14 ordered binary projections, repeated-event and complementary cases.
    for a in events:
        for b in events:
            for c in events:
                tests+=1
                seq=[a,b,c]
                verify(weights,seq)
                if tests%11==0:
                    test_norm(weights,seq,1.5)
                    test_norm(weights,seq,4)
    assert tests==14**3
    for k in [10,100,1000]:
        eps=F(1,2*k)
        pw=[eps,F(1,2)-eps,F(1,2)]
        A=frozenset([0]); B=frozenset([0,1])
        rr=[]
        for seq in ([B,A],[A,B]):
            test_norm(pw,seq,4)
            rec,c,_=verify(pw,seq)
            rr.append(abs(float(c))*H(rec[-1][0],4)*H(rec[0][0],4/3))
        assert rr[0]/rr[1]>1
    # The two endpoint events are independent; both adjacent pairs correlate.
    fair=[F(1,4)]*4
    first=frozenset((0,1))
    middle=frozenset((0,1,2))
    last=frozenset((0,2))
    rec,c,T=verify(fair,[first,middle,last])
    assert c==F(4,3) and any(x for row in T for x in row)
    assert sum(fair[i]*rec[0][2][i]*rec[-1][2][i]
               for i in range(4))==0
    print('BINARY_EXPECTATION_EXACT_IDENTITIES_OK',tests)

if __name__=='__main__':
    main()
