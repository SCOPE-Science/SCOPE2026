"""Independent finite-group enumeration of invariable tuples, plus finite-field rank formula.
Uses only the Python standard library. Run: python check_invariable.py
"""
from itertools import product
from math import comb

def mobius(d):
    u=0; t=d; x=2
    while x*x<=t:
        if t%x==0:
            t//=x; u+=1
            if t%x==0:return 0
            while t%x==0:t//=x
        x+=1
    return (-1)**(u+(t>1))

def exact_count(p,n,m,r,k):
    # r has multiplicative order m modulo p.
    N=p**n
    def F(j):
        if j<n:return 0
        z=1
        for i in range(n):z*=p**j-p**i
        return z
    T=lambda a:sum(mobius(m//d)*(d-1)**a for d in range(1,m+1) if m%d==0)
    return sum(comb(k,j)*F(j)*N**(k-j)*T(k-j) for j in range(k+1))

def make_group(p,n,m,r):
    vs=list(product(range(p),repeat=n)); vecid={v:i for i,v in enumerate(vs)}
    N=len(vs); zero=vecid[(0,)*n]
    elems=[(v,a) for a in range(m) for v in range(N)]
    def mul(x,y):
        v,a=elems[x]; w,b=elems[y]
        z=tuple((vs[v][i]+pow(r,a,p)*vs[w][i])%p for i in range(n))
        return (a+b)%m*N+vecid[z]
    e=zero
    size=m*N
    inv=[next(t for t in range(size) if mul(g,t)==e and mul(t,g)==e) for g in range(size)]
    def closure(gs):
        steps=set(gs)|{inv[g] for g in gs}
        S={e}; frontier=[e]
        while frontier:
            g=frontier.pop()
            for s in steps:
                v=mul(g,s)
                if v not in S:S.add(v);frontier.append(v)
        return frozenset(S)
    subs={frozenset([e])}; pending=[frozenset([e])]
    while pending:
        H=pending.pop()
        for g in range(size):
            if g in H:continue
            K=closure(set(H)|{g})
            if K not in subs:subs.add(K);pending.append(K)
    maximals=[H for H in subs if len(H)<size and not any(H<K and len(K)<size for K in subs)]
    classes=[]; unseen=set(range(size))
    while unseen:
        g=next(iter(unseen))
        C={mul(mul(t,g),inv[t]) for t in range(size)}
        unseen.difference_update(C);classes.append(C)
    masks=[]
    for g in range(size):
        masks.append(sum((1<<i) for i,H in enumerate(maximals) if any(z in H for C in classes if g in C for z in C)))
    def brute(k):
        return sum(not any(all((masks[g]>>i)&1 for g in tup) for i in range(len(maximals))) for tup in product(range(size),repeat=k))
    return size,len(subs),len(maximals),len(classes),brute

def check():
    cases=[(3,1,2,2,(2,3,4)),(5,1,4,2,(2,3)),(3,2,2,2,(2,3)),(7,1,3,2,(2,3))]
    for p,n,m,r,ks in cases:
        size,ss,mm,cc,brute=make_group(p,n,m,r)
        for k in ks:
            a=brute(k);b=exact_count(p,n,m,r,k)
            assert a==b,(p,n,m,k,a,b)
            print('OK',p,n,m,k,'count',a,'total',size**k,'subgroups',ss,'maximal',mm,'classes',cc)
    print('ALL_INVARIABLE_CHECKS_PASSED')
if __name__=='__main__':check()
