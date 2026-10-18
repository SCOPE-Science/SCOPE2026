import numpy as np

def allmul(q,G):
 M=(np.array([[0,0],[0,1]],dtype=np.uint8) if q==2 else np.array([[0,0,0,0],[0,1,2,3],[0,2,3,1],[0,3,1,2]],dtype=np.uint8))
 N=q**8
 ids=np.arange(N,dtype=np.uint32)
 A=np.column_stack([(ids//(q**i))%q for i in range(8)]).astype(np.uint8)
 def times(x,y):
  z=np.zeros_like(x)
  for i in range(8):
   for j in range(8):z[:,G[i,j]] ^= M[x[:,i],y[:,j]]
  return z
 e=np.bitwise_xor.reduce(A,axis=1)==0
 x2=times(A,A)
 x3=times(x2,A)
 x4=times(x3,A)
 zero=lambda v:np.all(v==0,axis=1)
 return [int(np.count_nonzero(e & zero(a))) for a in (x2,x3,x4)]
Gs={}
Gs['C8']=np.fromfunction(lambda a,b:(a+b)%8,(8,8),dtype=int).astype(int)
Gs['C4xC2']=np.array([[((i%4+j%4)%4)+4*((i//4+j//4)%2) for j in range(8)]for i in range(8)],dtype=int)
Gs['C2^3']=np.array([[i^j for j in range(8)]for i in range(8)],dtype=int)
Gs['D8']=np.array([[((i%4+(-1)**(i//4)*(j%4))%4)+4*((i//4+j//4)%2)for j in range(8)]for i in range(8)],dtype=int)
# Q8 different encoding a=sign bit and b=quaternion unit 1,i,j,k
U={}
for a in range(4):
 for b in range(4):
  if a==0:U[a,b]=(0,b)
  elif b==0:U[a,b]=(0,a)
  elif a==b:U[a,b]=(1,0)
  else:
   for x,y,z in ((1,2,3),(2,3,1),(3,1,2)):
    if (a,b)==(x,y):U[a,b]=(0,z)
    elif (a,b)==(y,x):U[a,b]=(1,z)
Gs['Q8']=np.array([[4*((i//4+j//4+U[i%4,j%4][0])%2)+U[i%4,j%4][1]for j in range(8)]for i in range(8)],dtype=int)
for q in (2,4):
 for name,G in Gs.items():
  obs=allmul(q,G)
  formulas={
   'C8':[q**4,q**5,q**6],
   'C4xC2':[q**6,q**6,q**7],
   'C2^3':[q**7,q**7,q**7],
   'D8':[(2*q-1)*q**4,(2*q-1)*q**5,q**7],
   'Q8':[q**4,q**5,q**7],
  }
  assert obs==formulas[name],(q,name,obs,formulas[name]);print(f'GF({q}) {name}: {obs} verified')
print('ALL_ORDER_EIGHT_OK')
