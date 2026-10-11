"""Exact rational illustrations for a universal analytic norm-attainment theorem.

All examples follow the same coordinate sign-flip construction. These checks do
not replace the proof for arbitrary Banach sequence lattices.
"""
from fractions import Fraction as Q

def check(name, a, f, primal_norm, dual_norm, defect):
    assert primal_norm(a) == 1, (name, 'primal norm')
    assert dual_norm(f) == 1, (name, 'dual norm')
    assert sum(a[j]*f[j] for j in range(len(a))) == 1
    assert all(z >= 0 for z in a+f)
    i = next(j for j in range(len(a)) if a[j]>0 and f[j]<1)
    x = [a[j] if j==i else -a[j] for j in range(len(a))]
    F = [f[j] if j==i else -f[j] for j in range(len(f))]
    # X=E direct-sum-one R and X*=E* direct-sum-infinity R.
    assert primal_norm([abs(z) for z in x]) == 1
    assert max(dual_norm([abs(z) for z in F]), Q(1)) == 1
    assert sum(x[j]*F[j] for j in range(len(x))) == 1
    xplus = [max(z,Q(0)) for z in x]
    Fplus = [max(z,Q(0)) for z in F]
    assert primal_norm(xplus) == a[i]
    assert max(dual_norm(Fplus), Q(1)) == 1
    gap = a[i] - sum(xplus[j]*Fplus[j] for j in range(len(x)))
    assert gap == defect and gap>0, (name,gap,defect)
    print(name, 'exact positive-part defect', gap)

def square(z): return max(abs(t) for t in z)
def square_dual(z): return sum(abs(t) for t in z)
check('square', [Q(1),Q(1)], [Q(1,2),Q(1,2)], square, square_dual, Q(1,2))

# Euclidean case: prove both the primal and dual rational unit norms by squaring.
def euc(z):
    v=sum(t*t for t in z)
    assert v==1 or v==Q(9,25) or v==Q(16,25) or v==0
    if v==1: return Q(1)
    if v==Q(9,25): return Q(3,5)
    if v==Q(16,25): return Q(4,5)
    return Q(0)
check('Euclidean rational unit pair',[Q(3,5),Q(4,5)],[Q(3,5),Q(4,5)],euc,euc,Q(6,25))

def octagon(z): return max(abs(z[0]),abs(z[1]),Q(2,3)*(abs(z[0])+abs(z[1])))
# f=(2/3,2/3) is a positive norm-one support because its action is
# bounded by the third defining facet; equality holds at a=(3/4,3/4).
def octagon_dual(z):
    # Dual norm is max of vertex pairings; positive unit ball vertices:
    # (1,1/2), (1/2,1), (3/4,3/4), plus their signed/reflected images.
    import itertools
    vertices=[(Q(1),Q(1,2)),(Q(1,2),Q(1)),(Q(3,4),Q(3,4))]
    return max(abs(sum(z[j]*Q(sgn[j])*v[j] for j in range(2)))
               for v in vertices for sgn in itertools.product((-1,1),repeat=2))
check('source-style octagon',[Q(3,4),Q(3,4)],[Q(2,3),Q(2,3)],octagon,octagon_dual,Q(1,4))

def top2(z): return sum(sorted([abs(t) for t in z],reverse=True)[:2])
def top2_dual(z): return max(max(abs(t) for t in z),sum(abs(t) for t in z)/Q(2))
check('top-two-three-dimensional',[Q(1,2)]*3,[Q(2,3)]*3,top2,top2_dual,Q(1,6))

# Finite coordinatewise ell_1: normalized support pairs split their norm
# into positive and negative parts exactly, including zero components.
from itertools import product
count=0
for n in (2,3,4):
    for c in product(range(-2,3),repeat=n):
        if not any(c):continue
        mass=sum(abs(z) for z in c)
        for d in product((-1,0,1),repeat=n):
            if any((z>0 and d[j]!=1) or (z<0 and d[j]!=-1) for j,z in enumerate(c)):
                continue
            if not any(abs(z)==1 for z in d):continue
            positive=sum(max(z,0) for z in c)
            negative=sum(max(-z,0) for z in c)
            fpos=max(max(z,0) for z in d)
            fneg=max(max(-z,0) for z in d)
            assert sum(max(c[j],0)*max(d[j],0) for j in range(n))==positive*fpos
            assert sum(max(-c[j],0)*max(-d[j],0) for j in range(n))==negative*fneg
            assert positive+negative==mass
            count+=1
print('VERIFY_OK exact_witness_families=4 ell1_normalized_pairs=',count)
