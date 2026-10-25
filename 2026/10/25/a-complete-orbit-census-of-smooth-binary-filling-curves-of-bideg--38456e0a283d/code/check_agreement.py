"""Compare the two full coefficient-level classifications and orbit certificate."""
import json
from collections import Counter
a=json.load(open('biquartic_census_output.json',encoding='utf8'))
b=json.load(open('biquartic_independent_output.json',encoding='utf8'))
c=json.load(open('data/ORBIT_REPRESENTATIVES.json',encoding='utf8'))
assert a['rank']==9 and a['rational_count']==3648
assert a['geometric_count']==len(a['smooth_masks'])==2328
assert b['smooth']==len(b['smooth_masks'])==2328
assert a['smooth_masks']==b['smooth_masks']
assert Counter({int(k):v for k,v in a['orbit_counts'].items()})==Counter({72:31,36:2,24:1})
assert Counter({int(k):v for k,v in b['orbit_sizes'].items()})==Counter({72:31,36:2,24:1})
assert len(c['orbits'])==34 and sum(o['orbit_size'] for o in c['orbits'])==2328
assert sorted((r['coefficient_mask'],r['orbit_size']) for r in c['orbits'])==sorted(tuple(v) for v in b['orbit_reps'])
print('PASS: 2,328 identical smooth coefficient masks in 34 orbits (31x72,2x36,1x24)')
