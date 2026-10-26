"""Finite checks for power semigroups of matrix-unit Brandt semigroups.

Run with Python 3.9+ and no third-party libraries.
"""
from itertools import permutations
import random


def model(n):
    # 0 is the zero; 1+i*n+j is matrix unit (i,j).
    z = n * n + 1
    prod = [[0] * z for _ in range(z)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for l in range(n):
                    if j == k:
                        prod[1+i*n+j][1+k*n+l] = 1+i*n+l
    def mul(a, b):
        out = 0
        xa = a
        while xa:
            low = xa & -xa
            i = low.bit_length()-1
            xa ^= low
            yb = b
            while yb:
                low2 = yb & -yb
                j = low2.bit_length()-1
                yb ^= low2
                out |= 1 << prod[i][j]
        return out
    unit = lambda i,j: 1 << (1+i*n+j)
    e = 1
    for i in range(n):
        e |= unit(i,i)
    return z,mul,unit,e


def verify(n):
    z,mul,unit,e = model(n)
    universe = range(1, 1 << z)
    central_idempotents = []
    central_candidates = []
    # Setwise multiplication distributes over unions, so commuting with all
    # singleton subsets is equivalent to commuting with all nonempty subsets.
    for a in universe:
        if all(mul(a, 1<<j) == mul(1<<j, a) for j in range(z)):
            central_candidates.append(a)
            if mul(a,a)==a:
                central_idempotents.append(a)
    assert central_idempotents == [1, e], (n,central_idempotents)
    for a in universe:
        plus = a | 1
        assert mul(e,a)==plus==mul(a,e)
        assert mul(e,plus)==plus
        for j in range(n):
            for k in range(n):
                left = unit(0,j)
                right = unit(k,0)
                sandwich = mul(mul(left,a),right)
                expected_member = bool(a & unit(j,k))
                assert bool(sandwich & unit(0,0)) == expected_member
                assert sandwich in (1, unit(0,0), 1 | unit(0,0))
    # The transformations induced by index permutations are homomorphisms.
    rng = random.Random(20261024+n)
    all_subsets = list(universe)
    for sigma in permutations(range(n)):
        trans = [0] * z
        for i in range(n):
            for j in range(n):
                trans[1+i*n+j] = 1+sigma[i]*n+sigma[j]
        def act(a):
            b = 0
            while a:
                low=a & -a
                x=low.bit_length()-1
                a ^= low
                b |= 1 << trans[x]
            return b
        pairs = ((a,b) for a in all_subsets for b in all_subsets) if n==2 else ((rng.choice(all_subsets),rng.choice(all_subsets)) for _ in range(2500))
        for a,b in pairs:
            assert act(mul(a,b)) == mul(act(a),act(b))
    # n=2: full centrality rather than the singleton necessary condition.
    if n==2:
        actual = [a for a in universe if mul(a,a)==a and all(mul(a,b)==mul(b,a) for b in universe)]
        assert actual == [1,e]
    print('VERIFY_OK', 'n=',n, 'power_elements=',len(all_subsets),
          'central_idempotents=',len(central_idempotents),
          'index_permutations=',__import__('math').factorial(n),
          'singleton_central_candidates=',len(central_candidates))


if __name__ == '__main__':
    verify(2)
    verify(3)


def verify_orbit_formula():
    from math import factorial, gcd
    for n, expected in [(2,19),(3,207),(4,6087),(5,583935),(6,193857983)]:
        sigma_sum=0
        for sigma in permutations(range(n)):
            unseen=set(range(n)); lengths=[]
            while unseen:
                i=next(iter(unseen));j=i;length=0
                while j in unseen:
                    unseen.remove(j);length+=1;j=sigma[j]
                lengths.append(length)
            cycles=sum(gcd(a,b) for a in lengths for b in lengths)
            sigma_sum+=1<<cycles
        assert (2*sigma_sum)//factorial(n)-1==expected
        if n<=3:
            z,_,_,_=model(n)
            todo=set(range(1,1<<z)); actual=0
            while todo:
                x=todo.pop();actual+=1
                orbit=set()
                for sigma in permutations(range(n)):
                    mask=0
                    for i in range(z):
                        if x>>i & 1:
                            j=0 if i==0 else 1+sigma[(i-1)//n]*n+sigma[(i-1)%n]
                            mask |=1<<j
                    orbit.add(mask)
                todo.difference_update(orbit)
            assert actual==expected
        print('ORBIT_OK n=',n,'orbit_count=',expected)

if __name__=='__main__':
    verify_orbit_formula()
