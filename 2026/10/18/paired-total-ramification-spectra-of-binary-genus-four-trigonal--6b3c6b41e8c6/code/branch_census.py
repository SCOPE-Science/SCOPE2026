"""Exact ramification census from cube-fibre tests and 72 automorphisms."""
from pathlib import Path
from collections import Counter
import json
from group_orbits import smooth_orbits, profile, total
smooth=Path('data/smooth_bitset.bin').read_bytes()
assert len(smooth)==65536 and smooth[0]
orbits=smooth_orbits(smooth)
orbit_hist=Counter(); weighted=Counter()
for rep,size,p in orbits:
    orbit_hist[p]+=1
    weighted[p]+=size
hist=Counter(profile(m) for m in range(1,65536) if not smooth[m])
assert hist==weighted
expected={(0,0):(5856,103),(0,1):(6912,96),
          (0,2):(1224,19),(0,3):(48,2),
          (1,1):(1620,27),(1,2):(360,5)}
assert {p:(weighted[p],orbit_hist[p]) for p in hist}==expected
report={
    'field':'F2','bidegree':[3,3],
    'total_coefficients_nonzero':65535,
    'geometrically_smooth_equations':16020,
    'projective_isomorphism_classes':252,
    'automorphism_group_order':72,
    'rows':[{'total_ramification_pair':list(p), 'equations':weighted[p],
             'isomorphism_classes':orbit_hist[p]} for p in sorted(hist)],
    'orbit_representatives':[{'mask':m,'orbit_size':size,
                              'total_ramification_pair':list(p)}
                             for m,size,p in orbits]
}
Path('data/census.json').write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')
print('census: 16020 smooth forms; 252 orbits; 6 unordered total-ramification pairs')
for p in sorted(hist):print(p,weighted[p],orbit_hist[p])
