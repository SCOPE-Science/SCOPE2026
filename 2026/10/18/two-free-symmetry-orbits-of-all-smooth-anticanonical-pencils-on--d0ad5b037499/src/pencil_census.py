from sympy import symbols, groebner
from itertools import product,combinations
import time,json
from pathlib import Path
X,Y,Z=symbols('X Y Z'); vs=(X,Y,Z)
basis=[Y*Y*Z+2*Y*Z*Z, X*Z*Z+2*Y*Z*Z, X*Y*Z+2*Y*Z*Z, X*Y*Y+2*Y*Z*Z, X*X*Z+2*Y*Z*Z,X*X*Y+2*Y*Z*Z]
def encode(v):return sum(int(a)*3**i for i,a in enumerate(v))
def decode(n):
 r=[]
 for i in range(6):r.append(n%3);n//=3
 return tuple(r)
def norm(v):
 k=next((v[i] for i in range(5,-1,-1) if v[i]),0)
 assert k
 return tuple((a*k)%3 for a in v) # k=2 inverse=2
start=time.monotonic()
allc=sorted({encode(norm(decode(n))) for n in range(1,729)})
assert len(allc)==364
smooth={}
for code in allc:
 coeff=decode(code);f=sum(a*b for a,b in zip(coeff,basis))
 gb=groebner([f]+[f.diff(v) for v in vs],X,Y,Z,modulus=3,order='grevlex')
 lm=[g.LM(order='grevlex').exponents for g in gb.polys]
 iszero=all(any(e[i]>0 and sum(e[j] for j in range(3) if j!=i)==0 for e in lm) for i in range(3))
 if iszero:smooth[code]=str(f)
print('time',time.monotonic()-start,'smooth',len(smooth),flush=True)
S=list(smooth)
pencils={}
for a,b in combinations(S,2):
 v=decode(a);w=decode(b)
 pair=[encode(norm(tuple((u+scale*t)%3 for u,t in zip(v,w)))) for scale in (1,2)]
 if not all(k in smooth for k in pair):continue
 p=tuple(sorted((a,b,*pair)))
 assert len(set(p))==4
 pencils[p]=1
print('elapsed',time.monotonic()-start,'all smooth pencils',len(pencils),flush=True)
print('sample:',list(pencils)[:5])
ref=json.load(open(Path(__file__).resolve().parent.parent/'data/census.json'))
assert ref['smooth_codes']==S
assert {tuple(p) for p in ref['pencils']}==set(pencils)
print('CENSUS VERIFIED')

# No three-dimensional subspace can be all-smooth if it contains a pencil.
for p in pencils:
    u,w=decode(p[0]),decode(p[1])
    for e in smooth.keys()-set(p):
        z=decode(e)
        if all(encode(norm(tuple((z[i]+a*u[i]+b*w[i])%3 for i in range(6)))) in smooth
               for a in range(3) for b in range(3)):
            raise AssertionError('unexpected all-smooth projective net')
print('NO ALL-SMOOTH NET VERIFIED')
