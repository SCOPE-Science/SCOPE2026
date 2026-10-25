"""Regenerate independently checkable finite orientation and collapse data.
Run `python3 make_cert.py`, then `python3 verify.py`.
"""
import json
from collections import defaultdict
from verify import faces,positions,codim_one_cofaces,incidence,check_order_four_classification
from pathlib import Path

f=faces('cyclic');tris=sorted(m for m in f if m.bit_count()==3)
tri2=set(tris);adj=defaultdict(list)
for e in f:
    if e.bit_count()!=2:continue
    a,b=sorted(t for t in tris if e&t==e)
    ratio=-incidence(a,e)*incidence(b,e)
    adj[a].append((b,ratio));adj[b].append((a,ratio))
sgns={tris[0]:1};stack=[tris[0]]
while stack:
    u=stack.pop()
    for v,ratio in adj[u]:
        s=sgns[u]*ratio
        if v in sgns:assert sgns[v]==s
        else:sgns[v]=s;stack.append(v)
assert len(sgns)==32

f=faces('klein'); steps=[]
while True:
    choices=[]
    for low in sorted(f):
        if not low:continue
        co=codim_one_cofaces(low,f)
        if len(co)==1:choices.append((low,co[0]))
    if not choices:break
    low,high=sorted(choices,key=lambda p:(-p[1].bit_count(),p[0],p[1]))[0]
    steps.append([low,high]);f.remove(low);f.remove(high)
assert len(steps)==32
cert={'schema_version':1,'orientation':[[t,sgns[t]] for t in tris], 'collapses':steps,'reduced_isotopies':check_order_four_classification()}
Path(__file__).with_name('certificate.json').write_text(json.dumps(cert,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print('GENERATE_OK',len(steps))
