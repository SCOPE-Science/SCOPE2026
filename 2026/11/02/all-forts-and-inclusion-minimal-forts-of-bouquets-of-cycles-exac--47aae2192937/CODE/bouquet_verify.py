from itertools import combinations, product
from collections import Counter
from functools import lru_cache


def maximal_independent_path(n):
    if n < 0: raise ValueError(n)
    masks=[]
    for b in range(1<<n):
        if b & (b<<1): continue
        if any(not ((b>>i)&1) and not ((i>0 and (b>>(i-1))&1) or (i+1<n and (b>>(i+1))&1)) for i in range(n)):
            continue
        masks.append(b)
    return masks


def proposed_minimal_fort_polynomial(lengths):
    result=Counter()
    for ell in lengths:
        for mask in maximal_independent_path(ell-3):
            result[ell-1-mask.bit_count()]+=1
    # Each petal contributes maximal independent sets of its non-hub path containing at least one endpoint.
    p=Counter({0:1})
    for ell in lengths:
        r=ell-1
        q=Counter()
        for mask in maximal_independent_path(r):
            if not (mask&1 or mask&(1<<(r-1))): continue
            q[r-mask.bit_count()]+=1
        pp=Counter()
        for a,x in p.items():
            for b,y in q.items(): pp[a+b]+=x*y
        p=pp
    for d,num in p.items(): result[1+d]+=num
    return result

def full_fort_polynomial(lengths):
    z=Counter({0:1})
    for ell in lengths:
        p=Counter()
        for mask in range(1<<(ell-1)):
            if not mask&(mask<<1):p[ell-1-mask.bit_count()]+=1
        zz=Counter()
        for a,x in z.items():
            for b,y in p.items():zz[a+b]+=x*y
        z=zz
    d=Counter({0:1})
    for ell in lengths:
        p=Counter({0:1})
        for mask in range(1<<(ell-3)):
            if not mask&(mask<<1):p[ell-1-mask.bit_count()]+=1
        dd=Counter()
        for a,x in d.items():
            for b,y in p.items():dd[a+b]+=x*y
        d=dd
    out=Counter({a+1:x for a,x in z.items()})
    out.update()  # no-op
    for a,x in d.items():out[a]+=x
    out[0]-=1
    if not out[0]:del out[0]
    return out

def graph_neighborhood(lengths):
    adj=[0]
    for ell in lengths:
        inds=list(range(len(adj),len(adj)+ell-1))
        adj.extend([0]*(ell-1))
        edges=[(0,inds[0]),(0,inds[-1])]+list(zip(inds,inds[1:]))
        for u,v in edges:
            adj[u] |=1<<v;adj[v] |=1<<u
    return adj

def is_fort(adj, white):
    if white==0:return False
    n=len(adj)
    for v in range(n):
        if white&(1<<v):continue
        if (adj[v]&white).bit_count()==1:return False
    return True

def direct_minimal_fort_polynomial(lengths):
    adj=graph_neighborhood(lengths)
    n=len(adj)
    good=set()
    allcount=Counter()
    for mask in range(1,1<<n):
        if is_fort(adj,mask):
            good.add(mask)
            allcount[mask.bit_count()]+=1
    mins=Counter()
    for mask in good:
        if not any(other!=mask and other&mask==other for other in good):
            mins[mask.bit_count()]+=1
    return mins,allcount

def validate():
    tests=[]
    for n in range(3,11):tests.append((n,))
    for a in range(3,8):
        for b in range(a,9):
            if 1+(a-1)+(b-1)<=15:tests.append((a,b))
    for a in range(3,6):
        for b in range(a,7):
            for c in range(b,7):
                if 1+(a-1)+(b-1)+(c-1)<=15:tests.append((a,b,c))
    for L in tests:
        p0,a0=direct_minimal_fort_polynomial(L)
        p1=proposed_minimal_fort_polynomial(L)
        a1=full_fort_polynomial(L)
        if p0!=p1 or a0!=a1:
            print('FAIL',L,p0,p1,a0,a1)
            return False
    print('VERIFY_OK',len(tests),'graph instances',sum((1<<(1+sum(x-1 for x in L)))-1 for L in tests),'nonempty subsets')
    for L in [(3,3),(4,5),(3,4,6),(6,6),(3,3,3),(8,8,8)]:
        p=proposed_minimal_fort_polynomial(L)
        print('SPECTRUM',L, sorted(p.items()))
    return True

if __name__=='__main__':assert validate()


def direct_zero_forcing(adj, blue):
    n=len(adj)
    target=(1<<n)-1
    while blue!=target:
        additions=0
        for i in range(n):
            if (blue>>i)&1:
                remaining=adj[i]&~blue&target
                if remaining and not remaining & (remaining-1):
                    additions |=remaining
        if not additions:
            return False
        blue|=additions
    return True


def standalone_second_checks():
    # Independently compute the weighted recurrences and boundary-restricted families.
    H=[Counter({0:1}),Counter({0:1,1:1})]
    Q=[Counter({0:1}),Counter({0:1}),Counter({1:2})]
    for r in range(2,17):
        h=Counter()
        for e,c in H[r-1].items():h[e+1]+=c
        for e,c in H[r-2].items():h[e+1]+=c
        H.append(h)
        if r>=3:
            q=Counter()
            for e,c in Q[r-2].items():q[e+1]+=c
            for e,c in Q[r-3].items():q[e+2]+=c
            Q.append(q)
        explicitH=Counter()
        for bits in range(1<<r):
            if not bits&(bits<<1): explicitH[r-bits.bit_count()]+=1
        assert H[r]==explicitH,(r,H[r],explicitH)
        if r>=2:
            direct=Counter(r-bits.bit_count() for bits in maximal_independent_path(r))
            assert Q[r]==direct,(r,Q[r],direct)
            restricted=Counter(r-bits.bit_count() for bits in maximal_independent_path(r) if not (bits&1 or bits&(1<<(r-1))))
            if r==2:reference=Counter()
            elif r==3:reference=Counter({2:1})
            elif r==4:reference=Counter()
            elif r==5:reference=Counter({3:1})
            else:reference=Counter({j+4:c for j,c in Q[r-6].items()})
            assert restricted==reference,(r,restricted,reference)
    direct_tests=[(3,3),(3,4),(4,5),(3,3,3),(3,4,5),(4,4,4),(6,6),(3,5,7)]
    exact=0
    for L in direct_tests:
        adj=graph_neighborhood(L)
        n=len(adj)
        if n>13:continue
        p=proposed_minimal_fort_polynomial(L)
        zf=Counter()
        for mask in range(1<<n):
            if direct_zero_forcing(adj,mask):continue
            if all(direct_zero_forcing(adj,mask|(1<<i)) for i in range(n) if not (mask>>i)&1):
                zf[mask.bit_count()]+=1
            exact+=1
        predicted=Counter({n-size:c for size,c in p.items()})
        assert zf==predicted,(L,zf,predicted)
        shortest=min(L)
        maxfailed=n-(shortest+1)//2
        multiplicity=sum((1 if ell%2==0 else (ell-1)//2) for ell in L if (ell+1)//2 == (shortest+1)//2)
        assert max(zf)==maxfailed,(L,max(zf),maxfailed)
        assert zf[maxfailed]==multiplicity,(L,zf[maxfailed],multiplicity)
    print('SECOND_CHECKS_OK weighted H/Q/E recurrences through 16; zero forcing on',len(direct_tests),'graphs')

if __name__=='__main__':standalone_second_checks()
