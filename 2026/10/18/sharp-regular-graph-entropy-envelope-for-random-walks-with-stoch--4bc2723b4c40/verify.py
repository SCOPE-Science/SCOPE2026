"""Finite checks for entropy of resetting walks and the regular-tree limit.

Only standard Python modules are required. The infinite theorems are proved in RESULT.md;
finite computations here test definitions, normalization, and independent formulations.
"""
from fractions import Fraction
from math import log, sqrt, isclose


def cycle(n):
    return [sorted({(i-1)%n, (i+1)%n}) for i in range(n)]

def complete(n):
    return [[j for j in range(n) if j != i] for i in range(n)]

def cube(d):
    return [[i^(1<<j) for j in range(d)] for i in range(1<<d)]

def complete_bipartite(k):
    return [list(range(k,2*k)) for _ in range(k)]+[list(range(k)) for _ in range(k)]

def solve(A,b):
    n=len(b)
    a=[list(A[i])+[b[i]] for i in range(n)]
    for j in range(n):
        h=next(i for i in range(j,n) if a[i][j])
        a[j],a[h]=a[h],a[j]
        f=a[j][j]
        a[j]=[v/f for v in a[j]]
        for i in range(n):
            if i!=j:
                t=a[i][j]
                if t:
                    a[i]=[x-t*y for x,y in zip(a[i],a[j])]
    return [a[i][-1] for i in range(n)]

def entropy(a):
    return -sum(float(x)*log(float(x)) for x in a if x>0)

def exact_pi(adj,r,root):
    n=len(adj);k=len(adj[0]);q=1-r
    Q=[[r*(j==root) + (q/Fraction(k) if j in adj[i] else 0)
         for j in range(n)] for i in range(n)]
    A=[[ (Fraction(i==j)-Q[j][i]) for j in range(n)] for i in range(n)]
    A[-1]=[Fraction(1)]*n
    b=[Fraction(0)]*(n-1)+[Fraction(1)]
    pi=solve(A,b)
    return Q,pi

def tree_limit(k,r):
    r=float(r);q=1-r
    if r==0:return log(k)
    if r==1:return 0.0
    a=q/k
    D=(r+a)*log(r+a)-r*log(r)-a*log(a)
    H=-r*log(r)-q*log(q/k)
    G=2*(k-1)/(k-2+sqrt(k*k-4*(k-1)*q*q))
    rho=k*r/q*(G-1)
    return H-rho*D

def check_case(adj,root,r):
    n=len(adj);k=len(adj[0]);q=1-r
    assert 2<=k<n
    assert all(len(nbr)==k and i not in nbr and len(nbr)==len(set(nbr)) for i,nbr in enumerate(adj))
    assert all(i in adj[j] for i,nbr in enumerate(adj) for j in nbr)
    Q,pi=exact_pi(adj,r,root)
    assert sum(pi)==1 and all(v>0 for v in pi)
    assert all(sum(row)==1 for row in Q)
    assert all(sum(pi[i]*Q[i][j] for i in range(n))==pi[j] for j in range(n))
    rho=sum(pi[i] for i in adj[root]); a=q/Fraction(k)
    D=(float(r+a)*log(float(r+a))-float(r)*log(float(r))-float(a)*log(float(a)))
    H=-float(q)*log(float(a))-float(r)*log(float(r))
    h_direct=sum(float(pi[i])*entropy(Q[i]) for i in range(n))
    h_formula=H-float(rho)*D
    assert isclose(h_direct,h_formula,abs_tol=2e-12,rel_tol=2e-12)
    assert h_direct<log(k+1)
    assert float(rho)>=float(r*q)-1e-12
    return h_direct,rho

def run():
    ct=0
    families=[]
    families += [(f'C{n}',cycle(n)) for n in range(3,18)]
    families += [(f'K{n}',complete(n)) for n in range(3,10)]
    families += [(f'K{k},{k}',complete_bipartite(k)) for k in range(2,7)]
    families += [(f'Q{d}',cube(d)) for d in range(2,5)]
    for name,adj in families:
        for root in sorted({0,len(adj)//3}):
            for r in [Fraction(1,7),Fraction(1,4),Fraction(2,5),Fraction(3,4)]:
                check_case(adj,root,r)
                ct+=1
    print('PASS exact rational stationary distributions and direct vs collision entropy:',ct,'cases')
    for k in range(2,9):
        for r in [0.01,0.05,0.2,0.5,0.8]:
            v=tree_limit(k,r)
            assert log(k)<v+2 or v>=0 # sanity
            assert 0<=v<log(k+1)
    print('PASS regular-tree closed form: 35 interior parameter checks')
    for n in [12,24,40,80,120]:
        adj=cycle(n)
        for r in [Fraction(1,7),Fraction(1,4),Fraction(2,5)]:
            # Efficient discounted Green iteration, with rigorous geometric tail
            q=float(1-r);v=[0.0]*n;v[0]=1.0
            rho=0.0
            for t in range(180):
                rho+=float(r)*(q**t)*(v[1]+v[-1])
                v=[(v[(i-1)%n]+v[(i+1)%n])/2 for i in range(n)]
            a=q/2
            D=(float(r)+a)*log(float(r)+a)-float(r)*log(float(r))-a*log(a)
            H=-q*log(a)-float(r)*log(float(r))
            h=H-rho*D
            err=abs(h-tree_limit(2,r))
            m=(n-1)//2
            assert err <= D*(q**(m+1)) + 1e-10,(n,r,err)
    print('PASS high-girth cycle comparison with rigorous truncation envelope: 15 cases')
    print('NUMERICAL ILLUSTRATION: regular-tree entropy at k=2, r=0.3:',format(tree_limit(2,0.3),'.12f'))

if __name__=='__main__':run()
