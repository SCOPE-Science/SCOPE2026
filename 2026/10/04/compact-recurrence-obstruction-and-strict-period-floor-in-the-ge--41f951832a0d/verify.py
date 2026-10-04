from fractions import Fraction as F
# sparse polynomials in (x,y,z,a,b)
N=5
def C(q): return {(0,0,0,0,0):F(q)}
def V(i):
 e=[0]*N;e[i]=1;return {tuple(e):F(1)}
def add(p,q):
 r=p.copy()
 for m,c in q.items():
  r[m]=r.get(m,F(0))+c
  if not r[m]: del r[m]
 return r
def neg(p): return {m:-c for m,c in p.items()}
def sub(p,q): return add(p,neg(q))
def mul(p,q):
 r={}
 for m,c in p.items():
  for n,d in q.items():
   k=tuple(m[i]+n[i] for i in range(N));r[k]=r.get(k,F(0))+c*d
 return {m:c for m,c in r.items() if c}
def sc(c,p): return {m:F(c)*v for m,v in p.items() if F(c)*v}
def powp(p,n):
 r=C(1)
 for _ in range(n): r=mul(r,p)
 return r
def der(p,i):
 r={}
 for m,c in p.items():
  if m[i]:
   e=list(m); k=e[i]; e[i]-=1; r[tuple(e)]=r.get(tuple(e),F(0))+c*k
 return r
def eq(p,q): return sub(p,q)=={}
def subab(p,av,bv):
 r={}
 for m,c in p.items():
  cc=c*(av**m[3])*(bv**m[4]); e=(m[0],m[1],m[2],0,0); r[e]=r.get(e,F(0))+cc
 return {m:c for m,c in r.items() if c}

x,y,z,a,b=[V(i) for i in range(5)]
Fx=neg(z)
Fy=sub(neg(powp(x,2)),y)
Fz=add(add(a,mul(b,x)),y)
fields=[Fx,Fy,Fz]
def L(p):
 r={}
 for i,fi in enumerate(fields): r=add(r,mul(der(p,i),fi))
 return r
p=sub(sub(powp(x,2),mul(b,x)),a)
w=Fz
H=add(add(sc(F(1,3),powp(x,3)),sc(F(-1,2),mul(b,powp(x,2)))),neg(mul(a,x)))
assert eq(L(H),neg(mul(z,p)))
assert eq(L(sc(F(1,2),powp(z,2))),mul(z,w))
rhs=add(add(add(powp(w,2),neg(mul(b,powp(z,2)))),neg(mul(z,p))),neg(mul(z,w)))
assert eq(L(mul(z,w)),rhs)
# jerk: x''' + x'' + b x' = p(x)
x1=L(x); x2=L(x1); x3=L(x2)
assert eq(add(add(x3,x2),mul(b,x1)),p)
pc=subab(p,F(17,10),F(17,10))
pcan=add(add(sc(10,powp(x,2)),sc(-17,x)),C(-17))
assert eq(sc(10,pc),pcan)
print('VERIFY_OK')
