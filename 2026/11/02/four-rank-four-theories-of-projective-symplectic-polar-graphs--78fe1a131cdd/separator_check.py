from verify_polar import points,form
for q,d in [(2,2),(2,3),(3,2),(3,3),(4,2)]:
 v=list(points(q,d)); n=len(v);adj=[]
 for u in v:adj.append(sum(1<<j for j,w in enumerate(v) if u!=w and form(u,w,q,d)==0))
 universe=(1<<n)-1
 qsep=dsep=False
 x=0
 for y in range(1,n):
  both=adj[x]&adj[y]
  for z in range(1,n):
   if z==y:continue
   if (adj[x]>>y)&1:
    if (adj[x]>>z)&1 and (adj[y]>>z)&1 and (both & (universe^adj[z]) & ~(1|(1<<y)|(1<<z))):
     dsep=True
   else:
    if not (adj[x]>>z)&1 and not (adj[y]>>z)&1:
     if not (both & (universe^adj[z])) and (universe^adj[x]) & (universe^adj[y]) & (universe^adj[z]) & ~(1|(1<<y)|(1<<z)):
      qsep=True
 assert qsep==(q>2) and dsep==(d>2),(q,d,qsep,dsep)
 print(f'SEPARATORS_OK q={q} d={d} field_gt_two={qsep} witt_gt_two={dsep}')
print('SEPARATOR_VERIFY_OK')
