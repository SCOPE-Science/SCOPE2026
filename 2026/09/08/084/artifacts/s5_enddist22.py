import json
from s4_enum22 import indecomp, dec, enc
D=json.load(open('/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-251/output/artifacts/s4_enum22.json'))
import sys; sys.path.insert(0,'/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-251/output/artifacts')
from s2_bricks import enddim
nb=0; dist={}
for k,v in D['reps'].items():
    a,b=2,2
    M=[[[r for r in row] for row in [v['rep'][kk][0:2],v['rep'][kk][2:4]]] for kk in range(3)]
    # M_k as bxa matrix: rep flat [m0..m3] row-major 2x2
    Mk=[[[v['rep'][kk][i*2+j] for j in range(2)] for i in range(2)] for kk in range(3)]
    d=enddim(2,2,Mk); dist[d]=dist.get(d,0)+1
    if v['indec'] and d==1: nb+=1
print('enddim dist (all classes):',dist,'brick_indec:',nb)
json.dump({'dist':dist,'nbrick':nb},open('/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-251/output/artifacts/s5_enddist22.json','w'))
