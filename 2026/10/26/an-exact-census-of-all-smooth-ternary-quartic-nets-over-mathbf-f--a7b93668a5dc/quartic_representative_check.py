import json,sympy as s,time
x,y,z=s.symbols('x y z'); v=(x,y,z)
exp=sorted([(a,b,4-a-b) for a in range(5) for b in range(5-a)],reverse=True)
terms=[x**a*y**b*z**c for a,b,c in exp]
data=json.load(open('smoothquartic_orbits.json'))
# sample all form-orbit reps to verify smoothness independently with grevlex
# all representatives regenerate from orbit enumeration without using precomputed group-orbit assignment
# use direct supplied group data, checking both smooth and nonsmooth reps
rows=[]
# regenerate reps via 3 substitution maps
import struct
maps=struct.unpack('<98304H',open('quartic_gentable.bin','rb').read())
seen=bytearray(32768)
for f in range(1,32768):
 if seen[f]:continue
 seen[f]=1; queue=[f]
 for a in queue:
  for k in range(3):
   b=maps[k*32768+a]
   if not seen[b]:seen[b]=1;queue.append(b)
 rows.append((f,len(queue)))
print('all_orbits',len(rows))
T=time.monotonic();ok=open('smoothquartic.bin','rb').read()
assert len(rows)==279 and sum(sz for _,sz in rows)==32767
for f,sz in rows:
 F=sum(terms[i] for i in range(15) if f>>i&1)
 good=True
 for i in range(3):
  w=[v[j] for j in range(3) if j!=i]
  p=s.Poly(F.subs({v[i]:1}),*w,modulus=2).as_expr()
  if list(s.groebner([p,s.diff(p,w[0]),s.diff(p,w[1])],*w,order='grevlex',modulus=2))!=[1]:good=False;break
 if good!=bool(ok[f]):raise Exception((f,sz,good,ok[f]))
print('smooth_orbits',sum(ok[f] for f,_ in rows),'smooth_forms',sum(sz for f,sz in rows if ok[f]),'time',round(time.monotonic()-T,3))
