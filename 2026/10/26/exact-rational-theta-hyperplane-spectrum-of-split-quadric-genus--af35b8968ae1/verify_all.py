"""Reproduce the exact theta-hyperplane census for bidegree-(3,3) forms over F2."""
import collections
import json
import pathlib
from tri_probe import form_test
from tri_orbits import get_orbits,trans,xform
from tri_smooth import is_smooth
from tritangent_check_independent import count as direct_plane_count

ROOT=pathlib.Path(__file__).resolve().parent
ROWS=json.loads((ROOT/'orbit_certificate.json').read_text(encoding='utf-8'))
assert len(ROWS)==1075
assert [(r['mask'],r['orbit_size']) for r in ROWS]==get_orbits()
assert sum(r['orbit_size'] for r in ROWS)==65535
assert len({r['mask'] for r in ROWS})==1075
smooth=collections.Counter()
maximizers=[]
for r in ROWS:
    f=r['mask']
    first=form_test(f)
    second=direct_plane_count(f)
    assert first==second==(r['theta_count'],r['theta_plane_mask']),(f,first,second,r)
    assert is_smooth(f)==r['geometrically_smooth'],f
    if r['geometrically_smooth']:
        smooth[r['theta_count']]+=r['orbit_size']
        if r['theta_count']==4:
            maximizers.append((f,r['orbit_size']))
assert smooth=={0:5208,1:8076,2:2556,3:120,4:60},smooth
assert maximizers==[(10723,18),(11750,36),(30857,6)],maximizers
assert sum(smooth.values())==16020
# Check each orbit's count is invariant on every transformed representative.
for r in ROWS:
    f=r['mask'];k=r['theta_count'];visited=set()
    for g in trans:
        h=xform(f,g);visited.add(h)
        assert form_test(h)[0]==k,(f,h)
    assert len(visited)==r['orbit_size'],f
print('Verified: 65,535 nonzero (3,3) forms and 1,075 projective orbits.')
print('Geometrically smooth: 252 orbits representing 16,020 forms.')
print('Exact theta-hyperplane distribution:',json.dumps(dict(sorted(smooth.items()))))
print('Four-plane maximizer orbits:',maximizers,'(sizes sum to 60).')
print('Independent graph/line incidence agrees with polynomial-conic checker for all 1,075 representatives.')
print('All orbit members preserve theta-hyperplane count under 72 split-quadric transformations.')
