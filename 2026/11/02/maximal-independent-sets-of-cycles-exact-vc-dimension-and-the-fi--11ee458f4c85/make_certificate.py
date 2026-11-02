import json
from cycle_exact import maximal_independent_cycle, dimension_vc,dimension_ld,construct_tree,trace_spectrum
rows=[]
for n in range(3,14):
 cs=maximal_independent_cycle(n)
 vc,_=dimension_vc(cs,n)
 ld,_=dimension_ld(cs,n)
 rows.append([n,len(cs),vc,ld])
cs=maximal_independent_cycle(13)
ld,rank=dimension_ld(cs,13)
assert ld==5
c={'graph':'C_13','n':13,'small_cycle_table':rows,'vc_witness':list(dimension_vc(cs,13)[1]), 'trace_spectra':{str(k):{str(a):b for a,b in trace_spectrum(cs,13,k).items()} for k in [4,5]},'depth_five_tree':construct_tree(cs,13,rank,5)}
with open('certificate.json','w') as f:json.dump(c,f,ensure_ascii=False,separators=(',',':'),indent=2);f.write('\n')
print('certificate generated',rows,'size',len(open('certificate.json').read()))
