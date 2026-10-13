"""Reproduce exact cherry–Wiener covariance tests for uniform labelled trees."""
from fractions import Fraction
from itertools import product
from math import comb

def numerator_distance(n):
    if n==1:return (0,1)
    p=n**(n-2)
    acc=p
    for k in range(1,n-1):
        p=(p//n)*(n-1-k)
        acc+=p
    return acc,n**(n-2)

def mean_W(n):
    if n==1: return Fraction(0)
    a,b=numerator_distance(n)
    return Fraction(comb(n,2)*a,b)

def mean_C(n):
    if n<=2:return Fraction(0)
    if n==3:return Fraction(1)
    return Fraction(n*comb(n-1,2)*(n-2)**(n-4),n**(n-2))

def conditional_mean_W(n):
    if n<3:return Fraction(0)
    r=n-2
    return Fraction(n+2,n-2)*mean_W(r)+2*(n-1)

def main():
    for n in range(3,627):
        gap=conditional_mean_W(n)-mean_W(n)
        assert (gap==0 if n==3 else gap<0),(n,gap)
        assert mean_C(n)>0
    print('EXACT_N_RANGE_OK',3,626,'n_tests',624)
    for n in (627,628,700,850,1000,2000):
        assert conditional_mean_W(n)<mean_W(n)
    print('TAIL_SPOT_CHECK_OK')
    for n in range(3,8):
        t=0; sW=sC=sCW=0
        for prufer in product(range(n),repeat=n-2):
            deg=[1]*n
            for x in prufer:deg[x]+=1
            adj=[[] for _ in range(n)]
            for x in prufer:
                leaf=next(i for i in range(n) if deg[i]==1)
                adj[leaf].append(x); adj[x].append(leaf)
                deg[leaf]-=1; deg[x]-=1
            a,b=(i for i in range(n) if deg[i]==1)
            adj[a].append(b);adj[b].append(a)
            lv=[sum(1 for u in adj[v] if len(adj[u])==1) for v in range(n)]
            c=sum(z*(z-1)//2 for z in lv)
            w=0
            for a in range(n):
                d=[-1]*n;d[a]=0;q=[a]
                for x in q:
                    for y in adj[x]:
                        if d[y]<0:d[y]=d[x]+1;q.append(y)
                w+=sum(d[a+1:])
            t+=1;sW+=w;sC+=c;sCW+=w*c
        assert t==n**(n-2)
        got=Fraction(sCW*t-sW*sC,t*t)
        exp=mean_C(n)*(conditional_mean_W(n)-mean_W(n))
        assert got==exp,(n,got,exp)
        assert Fraction(sW,t)==mean_W(n)
        assert Fraction(sC,t)==mean_C(n)
        print('CAYLEY_ENUM',n,t, 'cov',str(got))
    print('CHECKER_OK')
if __name__=='__main__':main()
