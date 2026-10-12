import math, cmath
from collections import defaultdict

rt=math.sqrt
U=[
 [0.5,0.5,0.5,0.5],
 [1/(2*rt(3)),1/(2*rt(3)),1/(2*rt(3)),-rt(3)/2],
 [1/rt(2),-1/rt(2),0.0,0.0],
 [1/rt(6),1/rt(6),-2/rt(6),0.0],
]

def dot(x,y): return sum(a*b for a,b in zip(x,y))
for i in range(4):
  for j in range(4):
    target=1.0 if i==j else 0.0
    assert abs(dot(U[i],U[j])-target)<1e-13

# state dictionary in normalized output Fock basis; index = 2*l+q.
vac={(0,)*8:1+0j}
def create_superposition(state,row,q):
  out=defaultdict(complex)
  for occ,amp in state.items():
    for l,u in enumerate(U[row]):
      if u==0: continue
      idx=2*l+q
      oo=list(occ); fac=math.sqrt(oo[idx]+1); oo[idx]+=1
      out[tuple(oo)] += amp*u*fac
  return dict(out)
def create_seq(ops):
  s=vac
  for row,q in ops: s=create_superposition(s,row,q)
  return s
def add_scaled(dst,src,c):
  for k,v in src.items(): dst[k]+=c*v

def target_prob(state):
  p=0.0
  amps=[]
  for occ,amp in state.items():
    spatial=[occ[2*l]+occ[2*l+1] for l in range(4)]
    if spatial==[1,1,1,0]:
      p+=abs(amp)**2; amps.append((occ,amp))
  return p,amps

def family(phi):
  out=defaultdict(complex)
  A=create_seq([(0,0),(0,0),(1,1)])
  B=create_seq([(0,0),(0,1),(1,0)])
  add_scaled(out,A,math.sqrt(2/3)/math.sqrt(2))
  add_scaled(out,B,cmath.exp(1j*phi)/math.sqrt(3))
  return dict(out)

for phi in [0.0, math.pi/3, math.pi]:
  p,amps=target_prob(family(phi))
  expected=(1+math.cos(phi))/24
  assert abs(p-expected)<2e-14,(phi,p,expected)
  if abs(phi-math.pi)<1e-12: assert p<1e-28

# Fully indistinguishable three-photon input on same spatial occupation.
allid=create_seq([(0,0),(0,0),(1,0)])
allid={k:v/math.sqrt(2) for k,v in allid.items()}
pid,amps=target_prob(allid)
assert abs(pid-3/32)<1e-14, pid
# normalized amplitude is sqrt(6)/8 for the sole internal pattern
assert len(amps)==1 and abs(abs(amps[0][1])-math.sqrt(6)/8)<1e-14

# Every relevant two-photon spatial amplitude to two distinct outputs among 1,2,3 is nonzero.
for j in range(3):
  for k in range(j+1,3):
    same=math.sqrt(2)*U[0][j]*U[0][k]
    mixed=U[0][j]*U[1][k]+U[0][k]*U[1][j]
    assert abs(same)>1e-14 and abs(mixed)>1e-14
    assert abs(mixed-1/(2*math.sqrt(3)))<1e-14
print('VERIFY_OK phase_zero=passed coherence_dependence=passed no_subset_suppression=passed')
