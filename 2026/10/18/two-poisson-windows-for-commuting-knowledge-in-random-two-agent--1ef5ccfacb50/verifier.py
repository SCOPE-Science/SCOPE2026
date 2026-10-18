"""Standalone finite verification for commuting two-agent knowledge relations.
Runs an independent full powerset modal-operator test against a P4 test."""
from itertools import product, combinations
from math import comb

def incidence_P4(cells,k):
    taken=set(cells)
    for a,a2 in combinations(range(k),2):
        for b,b2 in combinations(range(k),2):
            n=sum((x,y) in taken for x in (a,a2) for y in (b,b2))
            if n==3:
                return True
    return False

def actual_commute(cells):
    n=len(cells)
    ar=[sum(1<<j for j,(a2,b2) in enumerate(cells) if a==a2) for a,b in cells]
    br=[sum(1<<j for j,(a2,b2) in enumerate(cells) if b==b2) for a,b in cells]
    allmask=(1<<n)-1
    def box(S,relation):
        return sum(1<<i for i,mask in enumerate(relation) if S&mask==mask)
    return all(box(box(S,ar),br)==box(box(S,br),ar) for S in range(allmask+1))

def test():
    tests=0
    for k,maxn in ((2,6),(3,4)):
        for n in range(0,maxn+1):
            for sample in product(range(k*k), repeat=n):
                cells=tuple(divmod(x,k) for x in sample)
                via_graph=not incidence_P4(cells,k)
                via_modal=actual_commute(cells)
                assert via_graph == via_modal,(k,n,cells,via_graph,via_modal)
                tests+=1
    # Check triple probability by counting all ordered triples of sampled cell types.
    for k in range(2,7):
        count=0
        for e in product(range(k*k),repeat=3):
            cells=[divmod(x,k) for x in e]
            R={a for a,b in cells}; C={b for a,b in cells}
            if len(R)==2 and len(C)==2 and len(set(cells))==3:
                count+=1
        assert count==6*k*k*(k-1)**2,(k,count)
    print('VERIFY_OK exhaustive two-agent modal truth sets:',tests,
          'samples; six exact triple probabilities')
if __name__=='__main__': test()

# Exact independent combinatorial enumeration of all biclique-component graphs.
from functools import lru_cache
@lru_cache(None)
def biclique_count(l,r,e):
    if e<0:return 0
    if l==0:return int(e==0)
    total=biclique_count(l-1,r,e)
    for a in range(1,l+1):
        for b in range(1,r+1):
            total+=comb(l-1,a-1)*comb(r,b)*biclique_count(l-a,r-b,e-a*b)
    return total

def onto(n,e):
    if e==0:return int(n==0)
    return sum((-1)**(e-j)*comb(e,j)*j**n for j in range(e+1))

def verify_exact():
    cases=0
    for k,maxn in ((2,6),(3,4)):
        for n in range(maxn+1):
            from_structure=sum(biclique_count(k,k,e)*onto(n,e) for e in range(k*k+1))
            from_modal=sum(actual_commute(tuple(divmod(x,k) for x in sample))
                           for sample in product(range(k*k),repeat=n))
            assert from_structure==from_modal, (k,n,from_structure,from_modal)
            cases+=1
    print('EXACT_COUNT_OK',cases,'sample-size and alphabet-size cases')
if __name__=='__main__':verify_exact()
