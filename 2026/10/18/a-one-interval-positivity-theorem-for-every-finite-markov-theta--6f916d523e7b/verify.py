"""Exact rational checks for the theta-step finite-generator positivity theorem.

The proof for arbitrary finite state spaces is analytic; this script checks
finite-dimensional algebra, derivative ordering at sampled rational parameters,
and illustrative boundary classifications.  Python 3 standard library only.
"""
from fractions import Fraction as F
from random import Random


def inv(a):
    n=len(a)
    b=[[F(a[i][j]) for j in range(n)]+[F(i==j) for j in range(n)] for i in range(n)]
    for k in range(n):
        p=next(j for j in range(k,n) if b[j][k])
        b[p],b[k]=b[k],b[p]
        u=b[k][k]
        b[k]=[z/u for z in b[k]]
        for j in range(n):
            if j==k:continue
            t=b[j][k]
            if t:b[j]=[b[j][u]-t*b[k][u] for u in range(2*n)]
    return [r[n:] for r in b]


def matmul(a,b):
    n=len(a)
    return [[sum((a[i][k]*b[k][j] for k in range(n)),F(0)) for j in range(n)] for i in range(n)]


def gen(edges,n):
    q=[[F(0) for _ in range(n)] for _ in range(n)]
    for i,j,w in edges:q[i][j]+=F(w)
    for i in range(n):q[i][i]=-sum(q[i][j] for j in range(n) if i!=j)
    return q


def res(q,s):
    n=len(q)
    return inv([[F(i==j)-s*q[i][j] for j in range(n)] for i in range(n)])


def theta(q,h,theta):
    n=len(q)
    if theta==0:return [[F(i==j)+h*q[i][j] for j in range(n)] for i in range(n)]
    r=res(q,theta*h)
    a=[[r[i][j]/theta-(1-theta)/theta*F(i==j) for j in range(n)] for i in range(n)]
    b=matmul(r,[[F(i==j)+(1-theta)*h*q[i][j] for j in range(n)] for i in range(n)])
    assert a==b
    return a


def check(q):
    n=len(q)
    ss=[F(1,15),F(1,3),F(1),F(7),F(39)]
    rr=[res(q,s) for s in ss]
    for r in rr:
        assert all(sum(row)==1 for row in r)
        assert all(x>=0 for row in r for x in row)
    for i in range(n):
        if q[i][i]<0:
            assert all(rr[k][i][i]>rr[k+1][i][i] for k in range(len(ss)-1))
        else:
            assert all(r[i][i]==1 for r in rr)
    for t in [F(0),F(1,4),F(1,2),F(3,4),F(9,10),F(1)]:
        for h in [F(0),F(1,9),F(3,5),F(2),F(20)]:
            v=theta(q,h,t)
            assert all(sum(row)==1 for row in v)
            if t>0:
                r=res(q,t*h)
                assert all(v[i][j]>=0 for i in range(n) for j in range(n) if i!=j)
                assert (all(x>=0 for row in v for x in row)==all(r[i][i]>=1-t for i in range(n)))
    return 1


def main():
    count=0
    ex=gen([(0,1,1),(1,2,2)],3)
    for t in [F(0),F(1,4),F(1,2),F(3,4),F(9,10),F(1)]:
        if t<1:
            h=F(1,2)/(1-t)
            assert theta(ex,h,t)[1][1]==0
            assert theta(ex,h-F(1,10)*h,t)[1][1]>0
            assert theta(ex,h+F(1,10)*h,t)[1][1]<0
        else:
            assert all(theta(ex,F(k),t)[1][1]>0 for k in range(1,25))
        count+=1
    Q=gen([(0,1,1),(1,2,2),(2,0,3),(2,3,1),(3,0,1)],4)
    pi=inv([[F(i==j)-F(1,7)*Q[i][j] for j in range(4)] for i in range(4)])
    assert all(sum(row)==1 for row in pi)
    assert all(pi[i][i]<1 for i in range(4))
    count+=check(Q)
    random=Random(360426)
    for n in range(2,7):
        for case in range(38):
            e=[]
            for i in range(n):
                for j in range(n):
                    if i!=j and random.randrange(4):
                        e.append((i,j,F(random.randint(1,5),random.randint(1,4))))
            Q=gen(e,n)
            count+=check(Q)
    # Time reversal for a nonequilibrium irreducible four-state generator:
    q=gen([(0,1,1),(1,2,2),(2,0,3),(2,3,4),(3,0,5)],4)
    # Stationary row via Q^T and row-sum normalization.
    w=[[q[j][i] for j in range(4)] for i in range(4)]
    w[0]=[F(1) for _ in range(4)]
    z=inv(w)
    pi=[z[i][0] for i in range(4)]
    assert all(x>0 for x in pi) and sum(pi)==1
    qrev=[[pi[j]*q[j][i]/pi[i] for j in range(4)] for i in range(4)]
    for s in [F(1,3),F(1),F(4),F(40)]:
        r=res(q,s); rr=res(qrev,s)
        assert [r[i][i] for i in range(4)]==[rr[i][i] for i in range(4)]
    print('PASS: %d generators tested; all exact rational inverse checks pass.'%count)
    print('PASS: reducible pure-birth finite horizons; irreversible time reversal invariance.')

if __name__=='__main__':main()
