#!/usr/bin/env python3
"""Self-contained exact Paley four-pattern witness census (Python standard library).

The finite census covers every admissible odd prime-power order q<241.
For each q, affine normalization reduces every four-set to {0,1,a,b}.
The program checks every pattern and reports the exact minimum witness count.
"""
import json

IRREDUCIBLES = {
 9:(1,0,1),25:(2,0,1),49:(1,0,1),81:(2,1,0,0,1),
 121:(1,0,1),125:(1,1,0,1),169:(2,0,1),
}

def factors(n):
 d=2; out=[]
 while d*d<=n:
  if n%d==0:
   k=0
   while n%d==0:n//=d;k+=1
   out.append((d,k))
  d+=1
 if n>1:out.append((n,1))
 return out

def decompositions(limit=241):
 return [(p**e,p,e) for q in range(5,limit) if q%4==1
         for p,e in factors(q) if p**e==q]

def digits(n,p,e):
 out=[]
 for _ in range(e):out.append(n%p);n//=p
 return out

def remainder(f,g,p):
 r=list(f)
 while len(r)>=len(g):
  t=r[-1]%p
  if t:
   for i in range(len(g)):
    r[len(r)-len(g)+i]=(r[len(r)-len(g)+i]-t*g[i])%p
  while r and not r[-1]:r.pop()
 return r

def certify_irreducible(f,p):
 e=len(f)-1
 assert f[-1]==1 and e>1
 for degree in range(1,e//2+1):
  for n in range(p**degree):
   g=digits(n,p,degree)+[1]
   if not remainder(f,g,p):return False
 return True

def make_field(p,e):
 q=p**e
 if e==1:
  def mul(a,b):return a*b%p
  def sub(a,b):return (a-b)%p
  return q,mul,sub,None
 f=IRREDUCIBLES[q]
 assert certify_irreducible(f,p),(q,f)
 C=[digits(a,p,e) for a in range(q)]
 def pack(v):
  z=0
  for t in reversed(v):z=z*p+(t%p)
  return z
 MM=[[0]*q for _ in range(q)]
 SS=[[0]*q for _ in range(q)]
 for a in range(q):
  for b in range(q):
   u,v=C[a],C[b]
   SS[a][b]=pack([(u[i]-v[i])%p for i in range(e)])
   conv=[0]*(2*e-1)
   for i in range(e):
    for j in range(e):conv[i+j]=(conv[i+j]+u[i]*v[j])%p
   for k in range(2*e-2,e-1,-1):
    c=conv[k]
    for j in range(e):conv[k-e+j]=(conv[k-e+j]-c*f[j])%p
   MM[a][b]=pack(conv[:e])
 def mul(a,b):return MM[a][b]
 def sub(a,b):return SS[a][b]
 return q,mul,sub,list(f)

def census(q,p,e):
 q,mul,sub,modulus=make_field(p,e)
 S={mul(x,x) for x in range(1,q)}
 assert len(S)==(q-1)//2
 universe=(1<<q)-1
 neighborhoods=[]
 for a in range(q):
  t=0
  for x in range(q):
   if sub(x,a) in S:t|=1<<x
  neighborhoods.append(t)
 assert all((neighborhoods[a]>>a&1)==0 for a in range(q))
 assert all((neighborhoods[a]>>b&1)==(neighborhoods[b]>>a&1) for a in range(q) for b in range(q))
 inverse=[universe^n for n in neighborhoods]
 minimum=q;certificate=None;configurations=0
 for a in range(2,q):
  for b in range(a+1,q):
   vertices=[0,1,a,b]
   allowed=universe ^ sum(1<<v for v in vertices)
   for pattern in range(16):
    hits=allowed
    for i,v in enumerate(vertices):
     hits &= neighborhoods[v] if pattern>>i&1 else inverse[v]
    c=hits.bit_count();configurations+=1
    if c<minimum:
     minimum=c
     certificate={'four_set':vertices,'positive_indices':[i for i in range(4) if pattern>>i&1],
        'pattern_bits':pattern,'witnesses':[x for x in range(q) if hits>>x&1]}
 return {'q':q,'characteristic':p,'degree':e,'irreducible_polynomial':modulus,
         'minimum_witness_count':minimum,'normalized_patterns':configurations,'minimizer':certificate}

def main():
 values=[]
 for q,p,e in decompositions():
  values.append(census(q,p,e))
 assert [o['q'] for o in values if o['minimum_witness_count']>=2]==[89,97,101,109,113,121,137,149,157,169,173,181,193,197,229,233]
 assert [o['q'] for o in values if o['minimum_witness_count']==1]==[125]
 assert all(o['minimum_witness_count']==0 for o in values if o['q']<=81)
 assert values[-1]['q']==233
 print(json.dumps({'algorithm':'exact full normalized four-pattern census',
                   'cutoff_q_exclusive':241,'cases':values},sort_keys=True,separators=(',',':')))
 print('VERIFY_OK: all prime powers q congruent 1 mod 4 with q < 241 exhausted')
if __name__=='__main__':main()
