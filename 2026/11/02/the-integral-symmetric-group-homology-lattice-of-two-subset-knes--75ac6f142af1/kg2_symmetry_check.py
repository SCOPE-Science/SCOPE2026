"""Exact finite checks of simplicial mod-two boundaries and signed symmetry traces for two-set Kneser independence complexes.

The general theorem requires the separate topological proof; these tests check complete
finite simplicial chain complexes and all group permutations for selected sizes.
"""
import itertools
import math


def faces_and_vertices(n):
    vertices = tuple(itertools.combinations(range(n), 2))
    fac = set()
    for i in range(n):
        star = [edge for edge in vertices if i in edge]
        for k in range(1, len(star) + 1):
            fac.update(itertools.combinations(star, k))
    for a, b, c in itertools.combinations(range(n), 3):
        fac.add(((a, b), (a, c), (b, c)))
    return vertices, tuple(sorted(fac, key=lambda f: (len(f), f)))


def gf2_rank(columns):
    pivots = {}
    for x in columns:
        while x:
            k = x.bit_length() - 1
            if k in pivots:
                x ^= pivots[k]
            else:
                pivots[k] = x
                break
    return len(pivots)


def betti_mod2(faces):
    groups = {}
    for face in faces:
        groups.setdefault(len(face)-1, []).append(face)
    ranks = {-1: 0}
    for k, f in groups.items():
        if k == 0:
            ranks[k] = 0
            continue
        idx = {x: i for i, x in enumerate(groups[k-1])}
        columns = []
        for face in f:
            col = 0
            for i in range(len(face)):
                col ^= 1 << idx[face[:i] + face[i+1:]]
            columns.append(col)
        ranks[k] = gf2_rank(columns)
    maxdim = max(groups)
    return {k:len(v) - ranks[k] - ranks.get(k+1, 0) - (1 if k==0 else 0)
            for k,v in groups.items()}


def action_sign(f, g):
    mapped = [tuple(sorted((g[a], g[b]))) for a,b in f]
    target = tuple(sorted(mapped))
    if target != f:
        return 0
    inv = sum(mapped[i] > mapped[j] for i in range(len(mapped)) for j in range(i+1, len(mapped)))
    return (-1)**inv


def signed_euler_trace(faces, g):
    return sum((-1)**(len(f)-1)*action_sign(f, g) for f in faces) - 1


def char_exterior3_augmentation(g):
    n=len(g)
    visited = set()
    coeff=[1, 0, 0, 0]
    for i in range(n):
        if i in visited:
            continue
        j=i
        l=0
        while j not in visited:
            visited.add(j)
            j=g[j]
            l+=1
        # det(1+t g|V) factor is 1-(-t)^l
        if l <= 3:
            shift = (-1)**(l+1)
            for k in range(3, l-1, -1):
                coeff[k] += shift*coeff[k-l]
    # Divide by 1+t to restrict to the augmentation lattice.
    return coeff[3]-coeff[2]+coeff[1]-coeff[0]


def rotation(n,k):
    return tuple((i+k)%n for i in range(n))


def run():
    for n in range(5,9):
        vertices, faces = faces_and_vertices(n)
        bv = betti_mod2(faces)
        expected = math.comb(n-1,3)
        assert bv == {k:(expected if k==2 else 0) for k in bv}, (n,bv)
        permutation_iterator = (itertools.permutations(range(n)) if n<=7 else
            (tuple(list(range(i,n))+list(range(i))) for i in range(n)))
        tests=0
        for g in permutation_iterator:
            observed=signed_euler_trace(faces,g)
            prediction=char_exterior3_augmentation(g)
            assert observed==prediction, (n,g,observed,prediction)
            tests+=1
        rot_avg=sum(char_exterior3_augmentation(rotation(n,k)) for k in range(n))
        assert rot_avg % n == 0
        q=rot_avg//n
        q_formula=((n-1)*(n-2)+4*(n%3==0))//6 - (n-1)//2
        assert q == q_formula,(n,q,q_formula)
        assert q >= 0
        print('n=%s vertices=%s simplices=%s mod2_betti=%s permutations=%s rotation_quotient_b2=%s OK'
              %(n,len(vertices),len(faces),bv,tests,q))
    print('KG2_FULL_CHAIN_AND_CHARACTER_CHECKS_OK')

if __name__=='__main__':
    run()
