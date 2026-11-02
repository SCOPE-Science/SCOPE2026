from collections import Counter, defaultdict
from fractions import Fraction
from itertools import combinations, permutations
from math import factorial, comb

def comp_positive(n,k):
    if k==1:
        yield (n,)
        return
    for v in range(1,n-k+2):
        for rem in comp_positive(n-v,k-1):
            yield (v,)+rem

def type_by_runs(run_gap,p):
    types=[]
    for r,g in run_gap:
        if r==1: typ=('s',1)
        elif r%2==0: typ=('e',r)
        else: typ=('o',r,p)
        types.append(typ)
        p=(p+r+g)%2
    return tuple(sorted(types))

def inventory(n):
    N=2*n
    c=defaultdict(Fraction)
    c[()]+=1
    for t in range(1,n+1):
        for positive in comp_positive(N,2*t):
            rg=list(zip(positive[::2],positive[1::2]))
            for p in range(2):
                c[type_by_runs(rg,p)]+=Fraction(n,t)
    for k,v in c.items():
        assert v.denominator==1,(n,k,v)
    return {k:int(v) for k,v in c.items()}

def actual_type(n,mask):
    N=2*n
    if not mask:return ()
    if mask==(1<<N)-1:return ('full',)
    terms=[]
    for i in range(N):
        if (mask>>i)&1 and not ((mask>>((i-1)%N))&1):
            r=0
            while (mask>>((i+r)%N))&1:r+=1
            if r==1:typ=('s',1)
            elif r%2==0:typ=('e',r)
            else:typ=('o',r,i%2)
            terms.append(typ)
    return tuple(sorted(terms))

def aut(t):
    a=1
    for typ,k in Counter(t).items():
        a*=factorial(k)
        if typ[0]=='o': a*=2**k
    return a

def rank_poly(n,inventory):
    r=defaultdict(int)
    for t,c in inventory.items():
        rank=sum(z[1] for z in t)
        r[rank]+=c*c*aut(t)
    r[2*n]+=2*n
    return dict(sorted(r.items()))

def direct_mappings(n):
    N=2*n
    # Compare relation for any two domain elements: i<j iff i even and j odd and neighbors cyclic.
    def leq(i,j):
        return i%2==0 and j%2==1 and ((i-j)%N in (1,N-1))
    rank=Counter()
    sets=[tuple(i for i in range(N) if mask>>i&1) for mask in range(1<<N)]
    grouped=defaultdict(list)
    for s in sets:grouped[len(s)].append(s)
    for k in range(N+1):
        for domain in grouped[k]:
            rel={(i,j) for i in range(k) for j in range(k) if leq(domain[i],domain[j])}
            for image in grouped[k]:
                for v in permutations(image):
                    if all(leq(v[i],v[j])==((i,j) in rel) for i in range(k) for j in range(k)):
                        rank[k]+=1
    return dict(sorted(rank.items()))

if __name__=='__main__':
 for n in range(2,9):
    inv=inventory(n)
    counted=Counter(actual_type(n,mask) for mask in range((1<<(2*n))-1))
    assert counted==inv,(n,[(k,v,counted[k]) for k,v in inv.items() if v!=counted[k]])
    rp=rank_poly(n,inv)
    assert rp[2*n-1]==4*n*n
    if n>=3:assert rp[2*n-2]==n*n*(6*n-8)
    if n<=4:
        exact=direct_mappings(n)
        assert rp==exact,(n,rp,exact)
    print('CROWN_OK',n,len(inv),sum(rp.values()),rp[2*n-2],rp[2*n-1],rp[2*n])
 print('VERIFY_OK')
