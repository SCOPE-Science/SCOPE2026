"""Independent finite checks for strong odd colorings of clique windmills.
Usage: python verify.py
Only the standard library is required.
"""
from collections import Counter, defaultdict
from itertools import combinations, permutations, product
from math import factorial, comb


def optimal_q(s,m):
    return s if m%2 else 2*((m*s+2*(m-1)-1)//(2*(m-1)))


def parity_dp(s,m,q):
    """Number of row-wise unordered s-subset choices with every column odd."""
    masks=[sum(1<<i for i in x) for x in combinations(range(q),s)]
    states={0:1}
    for _ in range(m):
        new=defaultdict(int)
        for state,count in states.items():
            for mask in masks:
                new[state^mask]+=count
        states=new
    return states.get((1<<q)-1,0)


def fourier(s,m,q):
    val=0
    for j in range(q+1):
        es=sum((-1)**t*comb(j,t)*comb(q-j,s-t)
               for t in range(s+1) if 0<=s-t<=q-j and t<=j)
        val+=comb(q,j)*(-1)**j*es**m
    assert val%2**q==0
    return val//2**q


def brute(s,m,q):
    """Directly inspect proper colorings, rather than subset-parity recurrence."""
    blades=list(permutations(range(q),s))
    answer=0
    for pick in product(blades, repeat=m):
        deg=Counter(x for blade in pick for x in blade)
        if len(deg)==q and all(v%2 for v in deg.values()):
            # Each blade induces a clique, hence leaf colors are distinct.
            # A leaf's neighbor colors comprise the other leaf colors and hub.
            answer+=1
    return answer


def run():
    cases=[(2,1),(2,2),(2,3),(2,4),(3,2),(3,3),(3,4),(4,2),(4,4),(5,2),(6,2)]
    for s,m in cases:
        q=optimal_q(s,m)
        dp=parity_dp(s,m,q)
        ft=fourier(s,m,q)
        assert dp==ft,(s,m,q,dp,ft)
        assert dp>0
        for smaller in range(s,q):
            assert parity_dp(s,m,smaller)==0,(s,m,smaller)
        count=(q+1)*dp*factorial(s)**m
        if s<=3 and m<=4 and not (s==3 and m==4):
            direct=brute(s,m,q)
            assert direct==dp*factorial(s)**m,(s,m,direct,dp)
        print(f's={s} m={m} q={q} chi={q+1} labeled_optimal={count} OK')
    for m in (2,4,6):
        q=optimal_q(2,m)
        count=(q+1)*parity_dp(2,m,q)*factorial(2)**m
        assert count==5*(12**m+3*4**m)//8
    print('VERIFICATION_OK')

if __name__=='__main__':
    run()
