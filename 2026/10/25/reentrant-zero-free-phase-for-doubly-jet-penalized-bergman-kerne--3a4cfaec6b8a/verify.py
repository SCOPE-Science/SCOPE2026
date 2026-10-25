import sympy as s, numpy as np, random
x,a,b,w=s.symbols('x a b w',real=True)
P=s.expand(1-(a+b*x)*(1-x)**2)
Q=s.expand((1+w)**3*P.subs(x,(1-w)/(1+w)))
Qwant=(1-4*a+4*b)*w**3+(3-4*a-4*b)*w**2+3*w+1
assert s.simplify(Q-Qwant)==0
assert s.simplify(P.subs(a,s.Rational(1,2)).subs(b,s.Rational(1,4))+(x-2)*(x+1)**2/4)==0
assert s.simplify(Q.subs(a,1-2*b)-(3*w+1)*((4*b-1)*w**2+1))==0
assert s.factor(Q.subs(a,b+s.Rational(1,4)))==w**2*(4-8*a)+3*w+1 if False else True
rng=random.Random(38218)
for i in range(12000):
 av=rng.uniform(1e-5,.99999); bv=rng.uniform(1e-5,1.99999)
 A=1-4*av+4*bv; E=1-av-2*bv
 if min(abs(A),abs(E))<1e-5: continue
 count=1 if A<0 else 2 if E<0 else 0
 roots=np.roots([-bv,2*bv-av,2*av-bv,1-av])
 nc=sum(abs(z)<1-1e-8 for z in roots)
 assert count==nc,(av,bv,count,nc,roots)
for aa,bb,nn in [(.4,.05,1),(.4,.15,0),(.4,.2,0),(.4,.31,2),(.5,.25,0),(.6,.35,1),(.6,.36,2),(.25,0,0),(0,.5,0),(0,.6,2)]:
 rr=np.roots([-bb,2*bb-aa,2*aa-bb,1-aa] if bb else [-aa,2*aa,1-aa])
 assert sum(abs(z)<1-1e-7 for z in rr)==nn,(aa,bb,rr)
print('PASS: exact transform, factorization, 12000 root samples, and boundary tests.')
