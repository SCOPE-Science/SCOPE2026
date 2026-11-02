"""Exact finite-characteristic checks for the Klein cubic's characteristic-eleven fiber."""
import sympy as s
v=s.symbols('v')
z=s.symbols('z1:5')
F=z[0]+z[0]**2*z[1]+z[1]**2*z[2]+z[2]**2*z[3]+z[3]**2
D=[s.diff(F,a) for a in z]
P={z[0]:3,z[1]:9,z[2]:5,z[3]:4}
assert int(F.subs(P))%11==0
assert all(int(d.subs(P))%11==0 for d in D)
H=s.hessian(F,z).subs(P)
def mrank(A,p):
 M=[[int(x)%p for x in row] for row in A.tolist()]
 n=len(M); m=len(M[0]); row=0
 for col in range(m):
  pivot=next((j for j in range(row,n) if M[j][col]),None)
  if pivot is None:continue
  M[row],M[pivot]=M[pivot],M[row]
  inv=pow(M[row][col],-1,p);M[row]=[(t*inv)%p for t in M[row]]
  for j in range(n):
   if j!=row and M[j][col]:
    a=M[j][col];M[j]=[(M[j][k]-a*M[row][k])%p for k in range(m)]
  row+=1
 return row
assert mrank(H,11)==3
assert int(H.extract([1,2,3],[1,2,3]).det())%11==8
section={z[0]:3*v**5,z[1]:9*v**6,z[2]:5*v**4,z[3]:4*v**8}
assert all(s.Poly(s.expand(d.subs(section)),v,modulus=11).is_zero for d in D[1:])
h=s.expand(F.subs(section))
assert s.Poly(h+3*v**5*(v-1)**11,v,modulus=11).is_zero
assert s.Poly(h,v,modulus=11)==s.Poly(3*v**5+8*v**16,v,modulus=11)
assert s.Poly(s.diff(h,v)+15*v**4*(v-1)**11,v,modulus=11).is_zero
# For odd p with 2^5=-1, c=-1/2 and c^5=1: critical points are parametrized by t^11=c^2.
for p in (3,11):
 c=(-pow(2,-1,p))%p
 assert (c**5)%p==1
 assert (2+c**4)%p==0
 f=(1+c+c*c+c**3+c**4)%p
 print(f'CHARACTERISTIC_{p}_C={c};CRITICAL_ON_CUBIC={f==0};F_COEFFICIENT={f}')
assert sum(pow(i,11,11)==3 for i in range(11))==1
print('CHAR_11_UNIQUE_GEOMETRIC_CRITICAL_POINT=(1:3:9:5:4)')
print(f'HESSIAN_RANK_MOD11={mrank(H,11)};TRANSVERSE_DETERMINANT={int(H.extract([1,2,3],[1,2,3]).det())%11}')
print('TRANSVERSE_CRITICAL_SECTION=(3v^5,9v^6,5v^4,4v^8)')
print('RESTRICTED_FUNCTION=-3v^5(v-1)^11;TJURINA_LENGTH=11')
print('VERIFY_OK')
