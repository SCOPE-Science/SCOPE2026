"""Exact combinatorial checks for complementary-subset sphere actions.

The mathematical proof covers every integer n >= 2. This finite program
independently reconstructs signed coordinate permutations and their fixed
subspaces for small n; it is not a substitute for the general proof.
"""
import itertools
from math import comb


def model(n):
    universe = set(range(2*n))
    subsets = list(itertools.combinations(range(2*n), n))
    pairs = sorted({min(s, tuple(sorted(universe.difference(s)))) for s in subsets})
    return universe, pairs, {p:i for i,p in enumerate(pairs)}


def action(n, model_data, perm):
    universe, pairs, index = model_data
    targets = []
    signs = []
    for a in pairs:
        b = tuple(sorted(perm[x] for x in a))
        c = tuple(sorted(universe.difference(b)))
        target = min(b,c)
        targets.append(index[target])
        signs.append(1 if b == target else -1)
    return targets, signs


def perm_sign(perm):
    inv = 0
    for i,x in enumerate(perm):
        for y in perm[i+1:]:
            inv ^= (x > y)
    return -1 if inv else 1


def signed_determinant(targets, signs):
    return perm_sign(targets) * (1 if signs.count(-1)%2==0 else -1)


def s2(n):
    return n.bit_count()


def orbit_fixed_dimension(model_data,n, generators):
    transforms = [action(n,model_data,g) for g in generators]
    N=len(model_data[1]); unseen=set(range(N)); good=0
    while unseen:
        seed=min(unseen)
        stack=[(seed,1)]
        assigned={seed:1}; consistent=True
        while stack:
            i, s=stack.pop()
            for target,sgn in transforms:
                j=target[i]; z=s*sgn[i]
                if j not in assigned:
                    assigned[j]=z;stack.append((j,z))
                elif assigned[j]!=z:
                    consistent=False
        unseen.difference_update(assigned)
        good+=int(consistent)
    return good


def cyclic_dimension_from_traces(model_data,n,perm):
    identity=tuple(range(2*n)); cur=identity; d=0; order=0
    while True:
        targets,signs=action(n,model_data,cur)
        d+=sum(s for i,s in enumerate(signs) if targets[i]==i)
        order+=1
        cur=tuple(perm[x] for x in cur)
        if cur==identity:break
    assert d%order==0
    return d//order


def verify():
    checks=0
    # All permutations up to eight labels: the integral determinant is
    # the predicted trivial/sign character, not merely the transposition.
    for n in (2,3,4):
        data=model(n); expected=-1 if s2(n-1)==1 else 1
        for p in itertools.permutations(range(2*n)):
            a,b=action(n,data,p)
            assert signed_determinant(a,b)==(1 if expected==1 else perm_sign(p))
            checks+=1
    # Direct signed permutation on complementary pairs verifies the
    # fixed-sphere dimension without using the counting identity.
    samples=0
    for n in range(2,9):
        data=model(n)
        p=list(range(2*n));p[0],p[1]=p[1],p[0]
        targets,signs=action(n,data,p)
        assert signed_determinant(targets,signs)==(-1 if (n-1).bit_count()==1 else 1)
        trace=sum(s for i,s in enumerate(signs) if targets[i]==i)
        fixed_dim=orbit_fixed_dimension(data,n,[p])
        assert fixed_dim==(len(targets)+trace)//2
        assert fixed_dim==comb(2*n,n)//2-comb(2*n-2,n-1)//2
        samples+=1
        checks+=1
    # Arbitrary cyclic permutation actions: orbit-sign consistency agrees
    # with averaging the actual trace on the signed coordinate module.
    for n in range(2,7):
        data=model(n)
        pp=[tuple((j+i)%(2*n) for j in range(2*n)) for i in range(1,2*n)]
        pp += [tuple((0 if j==i else i if j==0 else j) for j in range(2*n)) for i in range(1,2*n)]
        for p in pp:
            d1=orbit_fixed_dimension(data,n,[p])
            d2=cyclic_dimension_from_traces(data,n,p)
            assert d1==d2
            checks+=1
    print('ALL_VERIFY_OK')
    print('complete_group_actions=41064')
    print('transposition_dimensions=7')
    print('cyclic_subgroups=70')
    print('total_exact_checks=',checks)
    print('samples=',samples)


if __name__=='__main__':
    verify()
