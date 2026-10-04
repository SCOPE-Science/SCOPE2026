#!/usr/bin/env python3
import math, random
q=math.sqrt(3.0)
V=[(1/q,1/q,1/q),(1/q,-1/q,-1/q),(-1/q,1/q,-1/q),(-1/q,-1/q,1/q)]
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def norm(a): return math.sqrt(dot(a,a))
def mul(c,a): return tuple(c*x for x in a)
def add(a,b): return tuple(x+y for x,y in zip(a,b))
def unit(a):
 n=norm(a); return tuple(x/n for x in a)
def ends(r): return abs(1-r)+3*math.sqrt(1+r*r+2*r/3), 1+r+3*math.sqrt(1+r*r-2*r/3)
def S(r,w): return sum(norm(add(mul(r,w),mul(-1,v))) for v in V)
frame=0.0
for i in range(4):
 frame=max(frame,abs(dot(V[i],V[i])-1))
 for j in range(4):
  if i!=j: frame=max(frame,abs(dot(V[i],V[j])+1/3))
for a in range(3):
 for b in range(3): frame=max(frame,abs(sum(v[a]*v[b] for v in V)-(4/3 if a==b else 0)))
rng=random.Random(21031); recon=viol=enderr=0.0; n=0
for r in [0,1e-6,1e-4,.01,.1,.25,.5,.9,1,1.1,2,10,100]:
 lo,hi=ends(r)
 if r==0: enderr=max(enderr,abs(lo-4),abs(hi-4))
 else:
  for v in V:
   enderr=max(enderr,abs(S(r,v)-lo),abs(S(r,mul(-1,v))-hi)); n+=2
 for _ in range(1800):
  w=unit((rng.gauss(0,1),rng.gauss(0,1),rng.gauss(0,1)))
  t=[dot(w,v) for v in V]
  wr=tuple(.75*sum(t[i]*V[i][j] for i in range(4)) for j in range(3))
  recon=max(recon,norm(add(wr,mul(-1,w))),abs(sum(t)),abs(sum(z*z for z in t)-4/3))
  s=S(r,w); viol=max(viol,lo-s,s-hi,0); n+=1
limit=5e-11
print('VERIFY_OK' if max(frame,recon,viol,enderr)<=limit else 'VERIFY_FAIL')
print(f'checks={n}')
print(f'frame_error={frame:.3e}')
print(f'reconstruction_error={recon:.3e}')
print(f'max_bound_violation={viol:.3e}')
print(f'endpoint_error={enderr:.3e}')
if max(frame,recon,viol,enderr)>limit: raise SystemExit(1)
