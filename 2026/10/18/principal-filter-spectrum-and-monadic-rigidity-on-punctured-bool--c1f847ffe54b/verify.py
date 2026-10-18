from itertools import product
from math import factorial

def relation(K,n):
 top=(1<<n)-1
 return tuple(sum(1<<y for y,k in enumerate(K) if k & ~a) for a in range(1,top+1))

def is_necessity(V,n):
 # principal filter corresponds to complement K under Fi(N_n)->B_n; top bitmask is nonprincipal
 return all(v != (1<<n)-1 for v in V)

def is_qmo(V,n):
 top=(1<<n)-1
 if V[-1]!=0: return False
 return all(V[(a&b)-1] == (V[a-1] | V[b-1]) for a in range(1,top+1) for b in range(1,top+1) if a&b)

def is_monadic(K,n):
 # QMO induced on B_n: D(S) has y if K_y intersects S.
 top=(1<<n)-1
 D=[sum(1<<y for y,k in enumerate(K) if k&s) for s in range(top+1)]
 return all((a & D[a])==a and D[a&D[b]] == (D[a] & D[b]) for a in range(top+1) for b in range(top+1))

for n in (2,3):
 qmo=necess=monad=monadnecess=0
 for K in product(range(1<<n), repeat=n):
  V=relation(K,n); assert is_qmo(V,n)
  qmo+=1; p=is_necessity(V,n);necess+=p
  if is_monadic(K,n):monad+=1;monadnecess+=p
 pred=(2**n)**n-(2**n-1)**n+factorial(n)
 print(f'n={n} QMO={qmo} necessity={necess} prediction={pred} monadic={monad} monadic_necessity={monadnecess}')
 assert necess==pred and monadnecess==1
print('VERIFY_OK')
# Independently replay the original R,T,M axioms via the explicit Boolean-filter isomorphism.
for n in (2,3):
 top=(1<<n)-1; monadic_direct=0; principal_direct=0
 for K in product(range(1<<n),repeat=n):
  D=lambda s:sum(1<<y for y,k in enumerate(K) if s&k)
  V=lambda a:D(top^a)
  R=all((top^a) & ~V(a)==0 for a in range(1,top+1))
  T=all(D(V(a)) & ~V(a)==0 for a in range(1,top+1))
  M=all((V(a)&V(b)) & ~D((top^a)&V(b))==0 for a in range(1,top+1) for b in range(1,top+1))
  monad=(R and T and M)
  assert monad==is_monadic(K,n)
  monadic_direct+=monad; principal_direct+=monad and all(V(a)!=top for a in range(1,top+1))
 print('ORIGINAL_RTM',n,'monadic',monadic_direct,'principal',principal_direct)
 assert principal_direct==1
print('ORIGINAL_RTM_OK')
