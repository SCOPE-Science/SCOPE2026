"""Independent locally-surjective adjacency-walk enumeration for finite degree-two domains."""
from itertools import product

def adj(kind,n):
 if kind=='P':return [set(j for j in (i-1,i+1) if 0<=j<n) for i in range(n)]
 return [{(i-1)%n,(i+1)%n} for i in range(n)]

def maps(m,kind,n):
 A=adj(kind,n);out=[]
 for a in range(n):
  for b in A[a]:
   path=[a,b]
   for i in range(1,m-1):
    opts=[z for z in A[path[i]] if A[path[i]]=={path[i-1],z}]
    if len(opts)!=1:raise AssertionError(('local propagation',m,kind,n,path,opts))
    path.append(opts[0])
   if all(A[path[i]]=={path[(i-1)%m],path[(i+1)%m]} for i in range(m)):
    assert set(path)==set(range(n))
    out.append(tuple(path))
 return sorted(set(out))

def target_codes(kind,n):
 return ['P'+str(n) if kind=='P' else 'C'+str(n)]

if __name__=='__main__':
 tested=0
 for m in range(3,19):
  for kind in ('P','C'):
   for n in range(2 if kind=='P' else 3,m+1):
    got=maps(m,kind,n)
    expected=(2*n if m%n==0 else 0) if kind=='C' else (2*(n-1) if m%(2*(n-1))==0 else 0)
    assert len(got)==expected,(m,kind,n,len(got),expected)
    tested+=1
 print('PASS independent adjacency enumeration',tested,'domain/target configurations (m=3..18)')
