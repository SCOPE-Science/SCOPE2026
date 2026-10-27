"""An independent, standard-library-only rational Jacobian screening.

Input is the exactly enumerated normal-form indices with at least four hyperflex flags.
The homogeneous degree is four and the field is F3, so Euler gives
F = sum Xi*dF/dXi (mod 3). A simultaneous zero of all partials
is therefore a singular point on the hypersurface.
"""
import itertools, json
from pathlib import Path

M = [tuple(x) for x in json.loads(Path('hyperflex_flags.json').read_text())['monomials']]
assert len(M) == 15
points = set()
for v in itertools.product(range(3), repeat=3):
    if not any(v): continue
    s=next(x for x in v if x)
    points.add(tuple((a*s)%3 for a in v))
assert len(points)==13
jac=[]
for p in sorted(points):
    matrix=[]
    for k in range(3):
        matrix.append([m[k]*__import__('math').prod(p[i]**(m[i]-(i==k)) for i in range(3))%3 if m[k] else 0 for m in M])
    jac.append(matrix)

def smooth_at_rational_points(n):
    c=[(n//3**i)%3 for i in range(15)]
    for mat in jac:
        if all(sum(x*y for x,y in zip(c,row))%3==0 for row in mat):
            return False
    return True

sizes={}
for k in range(4,13):
    fn=Path(f'hyperflex_count_{k}.txt')
    if not fn.exists():continue
    a=[int(x) for x in fn.read_text().split()]
    good=[x for x in a if smooth_at_rational_points(x)]
    sizes[k]=(len(a),len(good))
    if k==4:
        expected=[int(x) for x in Path('hyperflex_rsmooth_4.txt').read_text().split()]
        assert expected==good, (len(expected),len(good))
    else:
        assert not good, k
assert sizes[4]==(87750,52884)
assert sum(sizes[k][0] for k in sizes if k>=5)==9997
print('Independent Jacobian screening, counts (candidate, rationally smooth):',sizes)
print('Exactly matched all 52,884 rationally smooth four-contact candidates')
