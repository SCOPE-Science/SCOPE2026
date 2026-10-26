import sys,sympy as s,time
x,y,z=s.symbols('x y z');vs=(x,y,z)
mon=[(a,b,4-a-b) for a in range(5) for b in range(5-a)]
mon.sort(reverse=True)
expr=[x**a*y**b*z**c for a,b,c in mon]
expected=open('smoothquartic.bin','rb').read()
start=int(sys.argv[1]);end=int(sys.argv[2]);n=0
begin=time.monotonic()
for mask in range(start,end):
 F=sum(expr[i] for i in range(15) if mask>>i&1)
 flag=True
 for i in (0,1,2):
  vv=tuple(vs[j] for j in range(3) if j!=i)
  f=s.Poly(F.subs({vs[i]:1}),*vv,modulus=2).as_expr()
  if list(s.groebner([f,s.diff(f,vv[0]),s.diff(f,vv[1])],*vv,order='grevlex',modulus=2))!=[1]:
   flag=False;break
 if flag!=bool(expected[mask]):raise AssertionError((mask,flag,expected[mask]))
 n+=flag
print('range',start,end,'smooth',n,'elapsed',time.monotonic()-begin)
