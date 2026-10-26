from math import factorial
T=((2,1),(1,0))
def mul(A,B):return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
def power(A,n):
 R=((1,0),(0,1))
 while n:
  if n&1:R=mul(R,A)
  A=mul(A,A);n//=2
 return R
def tr(A):return A[0][0]+A[1][1]
def q(n):return tr(power(T,n))//2
B=((7,3),(3,1));D=((123,51),(51,21))

for r,step,base,mat in ((1,4,8,B),(3,4,8,B),(2,8,32,D),(6,8,32,D)):
 assert (q(r+step)-q(r))%base==0
 lead=(q(r+step)-q(r))//base
 second=(q(r+2*step)-2*q(r+step)+q(r))//base
 print(r,step,base,'Qr',q(r),'lead',lead,'coeff2',second)
 assert lead%2==1 and second%4==0
 for j in range(2,30):
  a=(step**j*tr(mul(power(T,r),power(mat,j))))//(2*base)
  assert step**j*tr(mul(power(T,r),power(mat,j)))%(2*base)==0
  target=2**(1+sum(j//(2**e) for e in range(1,j.bit_length()+1)))
  assert a%target==0,(r,j,a,target)
for k in range(1,16):
 mod=1<<k
 x,y=2%mod,2%mod;seen=set();states=set()
 while (x,y) not in states:
  states.add((x,y));seen.add(x)
  x,y=y,(2*y+x)%mod
 expected={z for z in range(mod) if z%16 in (2,14) or z%64==6} if k>=6 else None
 if k>=6: assert seen==expected,(k,len(seen),len(expected))
 print(k,len(seen),len(states))
print('PASS')
