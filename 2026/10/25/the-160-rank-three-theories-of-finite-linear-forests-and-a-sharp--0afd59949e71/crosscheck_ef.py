"""Direct three-round EF-game cross-check on small path forests."""
import importlib.util, functools, random
from pathlib import Path
s=importlib.util.spec_from_file_location('forest', str(Path(__file__).resolve().parent/'verify_rank3.py'));m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
def ef(G,H,r=3):
 n,a=G;v,b=H
 @functools.lru_cache(None)
 def win(aa,bb,left):
  for i in range(len(aa)):
   for j in range(len(aa)):
    if (aa[i]==aa[j])!=(bb[i]==bb[j]):return False
    if bool(a[aa[i]]&(1<<aa[j]))!=bool(b[bb[i]]&(1<<bb[j])):return False
  if left==0:return True
  return all(any(win(aa+(x,),bb+(y,),left-1) for y in range(v)) for x in range(n)) and all(any(win(aa+(x,),bb+(y,),left-1) for x in range(n)) for y in range(v))
 return win((),(),r)
small=[]
for code in range(1,4**7):
 n,a=m.graph(code)
 if n<=8:small.append((code,(n,a),m.rank3_type(n,a)))
print('small_forests',len(small))
r=random.Random(4417)
checks=set()
for i in range(len(small)):
 for j in range(i+1,len(small)):
  if i<22 or j<22 or r.random()<.035:checks.add((i,j))
for i,j in checks:
 A=small[i];B=small[j]
 if ef(A[1],B[1],3)!=(A[2]==B[2]):raise AssertionError((A[0],B[0]))
print('EF_game_agreement_pairs',len(checks))
