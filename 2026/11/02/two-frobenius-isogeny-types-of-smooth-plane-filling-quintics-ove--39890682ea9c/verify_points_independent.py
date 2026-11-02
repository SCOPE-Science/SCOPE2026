"""Independent finite-field point counter using primitive-power multiplication and determinant form.
Run: python verify_points_independent.py (Python standard library only).
"""
from itertools import product

def construct(n):
 q=3**n
 if n==1:
  add=[[ (i+j)%3 for j in range(3)] for i in range(3)]
  mul=[[i*j%3 for j in range(3)] for i in range(3)]
  return q,add,mul,(1,0)
 weights=[3**j for j in range(n)]
 digits=[[ (v//w)%3 for w in weights] for v in range(q)]
 add=[[sum(((u+v)%3)*weights[i] for i,(u,v) in enumerate(zip(digits[a],digits[b]))) for b in range(q)] for a in range(q)]
 def base_mul(a,b,f):
  aa=digits[a];bb=digits[b];h=[0]*(2*n-1)
  for i,u in enumerate(aa):
   for j,v in enumerate(bb):h[i+j]+=u*v
  for k in range(2*n-2,n-1,-1):
   coeff=h[k]%3
   if coeff:
    for j in range(n):h[k-n+j]-=coeff*f[j]
  return sum((h[i]%3)*weights[i] for i in range(n))
 # Construct GF(3^n) through a primitive polynomial rather than the first irreducible.
 f={2:(2,1,1),3:(1,0,2,1),4:(2,0,0,1,1),5:(1,0,0,0,2,1),6:(2,0,0,0,0,1,1)}[n]
 # The primitive-power enumeration exhaustively certifies field cardinality. 
 exp=[1];log=[None]*q
 for k in range(q-1):
  if k:exp.append(base_mul(exp[-1],3,f))
  log[exp[-1]]=k
 assert len(set(exp))==q-1
 mul=[[0 if (a==0 or b==0) else exp[(log[a]+log[b])%(q-1)] for b in range(q)] for a in range(q)]
 for a in range(q):assert mul[a][1]==a
 return q,add,mul,tuple(f)

def count(q,plus,times,a,b,c):
 # Companion matrix from t^3+a*t^2+b*t+c, so F=Y(Y^3Z-YZ^3)+Z(Z^3X-ZX^3)+(-cX-bY-aZ)(X^3Y-XY^3)
 ng=0
 # Frobenius cube computation via repeated multiplication (independent field embedding).
 cubic=[times[times[t][t]][t] for t in range(q)]
 for x in range(q):
  v=plus[x][times[2][cubic[x]]] # x-x^3
  for y in range(q):
   U=plus[cubic[y]][times[2][y]] # y^3-y
   W=plus[times[cubic[x]][y]][times[2][times[x][cubic[y]]]]
   coeff=plus[plus[times[-c%3][x]][times[-b%3][y]]][-a%3]
   F=plus[plus[times[y][U]][v]][times[coeff][W]]
   ng+=(F==0)
 # z=0: [1:y:0] plus [0:1:0].
 for y in range(q):
  W=plus[y][times[2][cubic[y]]]
  coeff=plus[-c%3][times[-b%3][y]]
  ng+=(times[coeff][W]==0)
 ng+=1 # [0:1:0], indeed W=0
 return ng

def main():
 cls={'special_144':(0,2,1),'generic_432':(1,0,2)}
 counts={k:[] for k in cls}
 for n in range(1,7):
  q,plus,times,p=construct(n)
  for name,abc in cls.items():counts[name].append(count(q,plus,times,*abc))
  print(n,p,{k:v[-1] for k,v in counts.items()},flush=True)
 expect={'special_144':[13,13,55,13,208,913],'generic_432':[13,13,16,117,273,640]}
 assert counts==expect,(counts,expect)
 print('INDEPENDENT_POINT_COUNTS_OK')
if __name__=='__main__':main()
