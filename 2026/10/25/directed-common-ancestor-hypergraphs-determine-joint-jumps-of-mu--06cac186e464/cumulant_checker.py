"""Exact finite-algebra checks for multitype inverse-Gaussian cumulants.
Requires Python 3 standard library only. The infinite assertions rest on the paper proof.
"""
from fractions import Fraction as F
from itertools import combinations, product
from math import factorial

def inv(A):
    n=len(A); U=[[F(x) for x in row]+[F(int(i==j)) for j in range(n)] for i,row in enumerate(A)]
    for k in range(n):
        p=next(j for j in range(k,n) if U[j][k]);U[k],U[p]=U[p],U[k]
        z=U[k][k];U[k]=[x/z for x in U[k]]
        for j in range(n):
            if j!=k:
                z=U[j][k];U[j]=[a-z*b for a,b in zip(U[j],U[k])]
    return [row[n:] for row in U]

def model(d,edges):
    # Edge parent -> child carries nonnegative weight; B=I-C.
    C=[[F(0) for j in range(d)] for i in range(d)]
    for parent,child,w in edges:C[child][parent]=F(w)
    B=[[F(int(i==j))-C[i][j] for j in range(d)] for i in range(d)]
    R=inv(B)
    J=[[R[j][i] for j in range(d)] for i in range(d)]
    return B,J

def cumulant_vector(J,labels):
    # (signed) derivatives of inverse z: indexed by individual positions.
    d=len(J);r=len(labels);memo={}
    def rec(mask):
        if mask in memo:return memo[mask]
        indices=[j for j in range(r) if (mask>>j)&1]
        if len(indices)==1:
            out=[J[i][labels[indices[0]]] for i in range(d)]
        else:
            out=[F(0) for i in range(d)]
            sub=(mask-1)&mask
            while sub:
                if sub!=mask:
                    a,b=rec(sub),rec(mask^sub)
                    for i in range(d):out[i]+=sum((J[i][l]*a[l]*b[l]/2 for l in range(d)),F(0))
                sub=(sub-1)&mask
        memo[mask]=out;return out
    return rec((1<<r)-1)

def test():
    w=F(1,5)
    # Three independent source classes, each producing a different pair among 4,5,6.
    edges=[(0,3,w),(0,4,w),(1,3,w),(1,5,w),(2,4,w),(2,5,w)]
    B,J=model(6,edges)
    eta=[F(1)]*6
    assert all(sum(B[j][k]*J[i][k] for k in range(6))==F(int(i==j)) for i in range(6) for j in range(6))
    reachable={i:{j for j in range(6) if J[i][j]>0} for i in range(6)}
    checks=0
    for r in range(1,5):
        for labels in product(range(6),repeat=r):
            cv=cumulant_vector(J,labels)
            kappa=sum((eta[i]*cv[i] for i in range(6)),F(0))
            expected=any(all(j in reachable[i] for j in labels) for i in range(6))
            assert (kappa>0)==expected,(r,labels,kappa,expected)
            checks+=1
    for a,b in combinations((3,4,5),2):
        cov=sum(cumulant_vector(J,[a,b]))
        assert cov==F(1,25),(a,b,cov)
    assert sum(cumulant_vector(J,[3,4,5]))==0
    assert sum(cumulant_vector(J,[0,3,4]))>0
    assert sum(cumulant_vector(J,[3,3,4,4]))>0
    # Check low-order Taylor inverse via independent power-series coefficient iteration.
    # Coordinates of u correspond to target labels 3,4,5.
    d=6;orders=4
    inds=[(a,b,c) for m in range(1,orders+1) for a in range(m+1) for b in range(m-a+1) for c in [m-a-b]]
    Q=[{} for i in range(d)]
    for alpha in inds:
        k=sum(alpha)
        for i in range(d):
            val=J[i][3+next(j for j,a in enumerate(alpha) if a)] if k==1 else F(0)
            for l in range(d):
                square=F(0)
                for beta,v in Q[l].items():
                    gamma=tuple(a-b for a,b in zip(alpha,beta))
                    if min(gamma)>=0:square+=v*Q[l].get(gamma,F(0))
                val-=J[i][l]*square/2
            Q[i][alpha]=val
    for alpha in inds:
        labels=[3+i for i,ct in enumerate(alpha) for j in range(ct)]
        order=len(labels)
        signed_psi_der=sum(cumulant_vector(J,labels))
        val=sum(Q[i][alpha] for i in range(d))
        mult=1
        for q in alpha:mult*=factorial(q)
        assert val*mult == (-1)**(order-1)*signed_psi_der,(alpha,val,signed_psi_der)
        checks+=1
    print('PASS exact checks:',checks)
    print('pair covariances (targets 4,5,6):',F(1,25))
    print('third cumulant targets 4,5,6:',sum(cumulant_vector(J,[3,4,5])))
    print('third cumulant targets 1,4,5:',sum(cumulant_vector(J,[0,3,4])))
    print('fourth cumulant targets 4,4,5,5:',sum(cumulant_vector(J,[3,3,4,4])))
    print('source matrix B:',B)

if __name__=='__main__':test()
