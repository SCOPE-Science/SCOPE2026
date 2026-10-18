"""Exact finite-graph checks for covariance of component-size counts.

Run: python verify.py
Only Python's standard library is required.
"""
from itertools import combinations
from fractions import Fraction
from math import comb, factorial

def stats_from_mask(n, edges, mask):
    root=list(range(n)); deg=[0]*n
    def find(x):
        while root[x]!=x:
            x=root[x]
        return x
    for i,(u,v) in enumerate(edges):
        if (mask>>i)&1:
            ru,rv=find(u),find(v)
            root[ru]=rv
            deg[u]+=1;deg[v]+=1
    groups={}
    for v in range(n):
        groups.setdefault(find(v),[]).append(v)
    sizes=[len(x) for x in groups.values()]
    C={k:sizes.count(k) for k in range(1,n+1)}
    # Typed component counts: tree components of size 2..n and cliques of size 2..n
    tree={k:0 for k in range(1,n+1)}
    clique={k:0 for k in range(1,n+1)}
    for vertices in groups.values():
        k=len(vertices)
        e=sum(deg[v] for v in vertices)//2
        tree[k]+=int(e==k-1)
        clique[k]+=int(e==k*(k-1)//2)
    return C, tree, clique

def exact_test(n,p):
    edges=list(combinations(range(n),2))
    m=len(edges)
    num,den=p.numerator,p.denominator
    denpow=den**m
    weight=[(num**k)*((den-num)**(m-k)) for k in range(m+1)]
    totals={name:[0]*(n+1) for name in ('all','tree','clique')}
    moments={}
    pairs=[]
    for a in ('all','tree','clique'):
        for b in ('all','tree','clique'):
            for r in range(1,n+1):
                for s in range(1,n+1):
                    if r!=s:
                        pairs.append((a,b,r,s))
                        moments[a,b,r,s]=0
    for mask in range(1<<m):
        w=weight[mask.bit_count()]
        C,T,Q=stats_from_mask(n,edges,mask)
        d={'all':C,'tree':T,'clique':Q}
        for a in d:
            for r in range(1,n+1): totals[a][r]+=w*d[a][r]
        for a,b,r,s in pairs:
            moments[a,b,r,s]+=w*d[a][r]*d[b][s]
    checks=0
    for a,b,r,s in pairs:
        if totals[a][r]==0 or totals[b][s]==0:
            continue
        ratio=Fraction(factorial(n-r)*factorial(n-s),factorial(n)*factorial(n-r-s)) if r+s<=n else Fraction(0)
        q=1-p
        joint=Fraction(moments[a,b,r,s],denpow)
        expected=Fraction(totals[a][r]*totals[b][s],denpow**2)
        assert joint == expected*ratio/q**(r*s), (n,p,a,b,r,s,joint,expected*ratio/q**(r*s))
        assert (joint>expected)-(joint<expected)==(ratio>q**(r*s))-(ratio<q**(r*s))
        checks+=2
    return checks

def threshold_checks():
    checks=0
    for n in range(3,30):
      for r in range(1,n):
       for s in range(r+1,n):
        if r+s>n:continue
        R=Fraction(factorial(n-r)*factorial(n-s),factorial(n)*factorial(n-r-s))
        # Every off-diagonal threshold exceeds the classical critical value 1/n.
        assert R < Fraction(n-1,n)**(r*s)
        # Ratio formula agrees with the telescoping product.
        lhs=Fraction(1,R)
        rhs=Fraction(1)
        for i in range(r):
         for j in range(s): rhs*=Fraction(n-i-j,n-i-j-1)
        assert lhs==rhs
        checks+=2
    return checks

if __name__=='__main__':
    tests=0
    for n in range(3,6):
      for p in (Fraction(1,5),Fraction(1,2),Fraction(4,5)):
        c=exact_test(n,p)
        print('all graph configurations',n,p,'assertions',c)
        tests+=c
    for p in (Fraction(1,5),Fraction(1,2)):
       c=exact_test(6,p)
       print('all graph configurations',6,p,'assertions',c)
       tests+=c
    tests+=threshold_checks()
    print('VERIFY_OK',tests)
