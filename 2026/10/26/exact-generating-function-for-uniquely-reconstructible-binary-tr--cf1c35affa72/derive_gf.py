import sympy as sp
from supports import trees,E
from functools import lru_cache
z=sp.symbols('z')

def edge_range(mask,forced,i):
 return (0,0) if not(mask>>i&1) else ((1,1) if i in forced else (1,None))
def intersect(A,B):
 lo=max(A[0],B[0]);hi=(min(A[1],B[1]) if A[1]!=None and B[1]!=None else (A[1] if B[1]==None else B[1]))
 return (lo,hi) if hi is None or lo<=hi else None

def R(p,L,U):
 if U is not None:return sum(z**(p*i) for i in range(L,U+1))
 return z**(p*L)/(1-z**p)
@lru_cache(None)
def Above(p,q,K,LC,UC,LD,UD):
 total=R(p,LC,UC)*R(q,LD,UD)
 below=sp.Integer(0)
 for c in range(LC,max(LC,K)):
  if UC is not None and c>UC:break
  for d in range(LD,max(LD,K-c)):
   if UD is not None and d>UD:break
   below+=z**(p*c+q*d)
 return total-below

def gf_case(mask,s,t,forced):
 delta=[int(j==s)-int(j==t) for j in range(4)]
 c=edge_range(mask,forced,2)
 d=intersect(edge_range(mask,forced,3), tuple((v-delta[3] if v is not None else None) for v in edge_range(mask,forced,6)))
 e=intersect(edge_range(mask,forced,4), tuple((v-delta[0] if v is not None else None) for v in edge_range(mask,forced,1)))
 if d is None or e is None:return sp.Integer(0)
 # all raw c,d,e >=0, already implied by own edge ranges; reject shifted negatives through intersection
 LC,UC=c;LD,UD=d;LE,UE=e
 B=delta[0]+delta[1]
 factor=z**(delta[3]-delta[1])
 sf=edge_range(mask,forced,5)
 if sf[1] is None:
  if UE is None:
   T=B+1+LE
   gf=(z**LE*Above(2,3,T,LC,UC,LD,UD)-z**(1-B)*Above(3,4,T,LC,UC,LD,UD))/(1-z)
  else:
   gf=sum(z**i*Above(2,3,B+1+i,LC,UC,LD,UD) for i in range(LE,UE+1))
 else:
  h=sf[0];assert sf[1]==h
  T=B+h+LE
  gf=z**(-B-h)*Above(3,4,T,LC,UC,LD,UD)
  if UE is not None: gf-=z**(-B-h)*Above(3,4,B+h+UE+1,LC,UC,LD,UD)
 for i in (0,7):
  if mask>>i&1:gf*=z/(1-z)
 return factor*gf

def derive():
    terms=[]
    for mask in range(1,256):
        active={v for i,(v,w) in enumerate(E) if mask>>i&1 for v in (v,w)}
        for t in active:
            if sum(bool(mask>>i&1) for i,(v,w) in enumerate(E) if v==t)>1:
                continue
            tr=trees(mask,t,active)
            if len(tr)!=1:
                continue
            forced={i for i in tr[0] if sum(bool(mask>>j&1) for j,(v,w) in enumerate(E) if v==E[i][0])>1}
            for s in active-{t}:
                expr=gf_case(mask,s,t,forced)
                if expr!=0:
                    terms.append(expr)
    assert len(terms)==136, len(terms)
    numerator=2*z*(z**13+2*z**12+z**11-z**10-4*z**9-9*z**8-11*z**7+z**5+8*z**4+6*z**3+6*z**2+2*z+4+z*(1-z)**2*(1+z)*(1+z**2)*(1+z+z**2))
    denominator=(1-z)**3*(1+z)*(1+z**2)*(1+z+z**2)
    target=numerator/denominator
    lhs=2*z/(1-z)+sum(terms)
    assert sp.cancel(lhs-target)==0
    print('EXACT_GF_PASS; valid support/start/end types=136; denominator='+str(sp.factor(denominator)))
    return numerator, denominator
if __name__=='__main__': derive()
