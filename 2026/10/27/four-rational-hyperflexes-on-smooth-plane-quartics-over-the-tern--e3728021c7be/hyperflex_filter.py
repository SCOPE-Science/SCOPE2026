import json,numpy as np
x=json.load(open('hyperflex_flags.json'));M=x['monomials']
vs=[]
for v in __import__('itertools').product(range(3),repeat=3):
 if any(v):
  lead=next(a for a in v if a)
  w=tuple(a*pow(lead,-1,3)%3 for a in v)
  if w not in vs:vs.append(w)
P=np.array(vs)
forms=np.array([[np.prod([pow(int(pt[j]),m[j],3) for j in range(3)])%3 for m in M] for pt in P],dtype=np.int32)
der=np.array([[[ (m[k]*np.prod([pow(int(pt[j]),m[j]-(j==k),3) for j in range(3)]) )%3 if m[k]>0 else 0 for m in M] for k in range(3)]for pt in P],dtype=np.int32)
for c in range(12,3,-1):
 try:raw=np.loadtxt('hyperflex_count_'+str(c)+'.txt',dtype=np.int32,ndmin=1)
 except OSError:continue
 if len(raw)==0:continue
 v=(raw[:,None] // (3**np.arange(15))[None,:])%3
 vals=v@forms.T %3
 gra=np.einsum('nm,pkm->npk',v,der)%3
 smooth=np.all((vals!=0)|np.any(gra!=0,axis=2),axis=1)
 a=raw[smooth]
 np.savetxt('hyperflex_rsmooth_'+str(c)+'.txt',a,fmt='%d')
 print('hyperflex',c,'candidate',len(raw),'rational smooth',len(a),'sample',a[:20])
