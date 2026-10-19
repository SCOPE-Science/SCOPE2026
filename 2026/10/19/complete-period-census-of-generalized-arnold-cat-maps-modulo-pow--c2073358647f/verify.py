from collections import Counter

def mm(A,B,N):
 return ((A[0]*B[0]+A[1]*B[2])%N,(A[0]*B[1]+A[1]*B[3])%N,(A[2]*B[0]+A[3]*B[2])%N,(A[2]*B[1]+A[3]*B[3])%N)
def order(A,N):
 X=(1,0,0,1)
 for k in range(1,2*N+1):
  X=mm(X,A,N)
  if X==(1,0,0,1):return k
 raise RuntimeError('order exceeds bound')
def val(x,N,e):
 x%=N
 if x==0:return e
 s=0
 while x%3==0:s+=1;x//=3
 return s
def calc(p,q,N,e):
 x=p*q%N
 if p%3==0 and q%3==0:
  s=min(val(p,N,e),val(q,N,e));r=1
 elif x%3==0:
  s=val(x+3,N,e);r=3
 elif x%3==1:
  s=val(x+2,N,e);r=4
 else:
  s=val(x+1,N,e);r=6
 return r*3**max(0,e-s),(r,s)

def theoretical(e):
 out=Counter()
 out[(1,e)]+=1
 for s in range(1,e):
  out[(1,s)]+=8*3**(2*(e-s-1))
  out[(3,s)]+=8*3**(2*e-s-2)
  out[(4,s)]+=4*3**(2*e-s-2)
  out[(6,s)]+=4*3**(2*e-s-2)
 out[(3,e)]+=4*3**(e-1)
 out[(4,e)]+=2*3**(e-1)
 out[(6,e)]+=2*3**(e-1)
 return out
for e in range(1,5):
 N=3**e
 obs,actual,predict=Counter(),Counter(),Counter()
 for p in range(N):
  for q in range(N):
   P,(r,s)=calc(p,q,N,e)
   act=order((1,p,q,(1+p*q)%N),N)
   if act!=P:raise AssertionError((e,p,q,P,act,r,s))
   obs[(r,s)]+=1;actual[act]+=1;predict[P]+=1
 expected=theoretical(e)
 assert obs==expected,(e,obs,expected)
 assert sum(obs.values())==N*N
 print('e',e,'N',N,'counts',sorted(actual.items()),'sum',sum(actual.values()),'all_verified',True)
print('VERIFY_OK')
