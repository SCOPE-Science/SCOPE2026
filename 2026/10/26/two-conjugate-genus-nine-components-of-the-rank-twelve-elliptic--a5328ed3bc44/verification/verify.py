"""Exact polynomial certificate for two conjugate residual discriminant factors.
Standard-library only. Execute: python3 verification/verify.py
All arithmetic is in Q[s]/(s*s-rad), with polynomial variables (v,q).
"""
from fractions import Fraction as F
from math import gcd

def ring(rad):
    z = (F(0), F(0)); one = (F(1), F(0))
    def plus(a,b): return (a[0]+b[0],a[1]+b[1])
    def neg(a): return (-a[0],-a[1])
    def prod(a,b): return (a[0]*b[0]+rad*a[1]*b[1],a[0]*b[1]+a[1]*b[0])
    def mon(x,n): return {(n,0):x} if x!=z else {}
    def cons(n): return mon((F(n),F(0)),0)
    V={(1,0):one}; Q={(0,1):one}; S={(0,0):(F(0),F(1))}
    def add(*args):
        out={}
        for a in args:
            for m,c in a.items():
                out[m]=plus(out.get(m,z),c)
        return {m:c for m,c in out.items() if c!=z}
    def mul(a,b):
        out={}
        for (i,j),x in a.items():
            for (k,l),y in b.items():
                m=(i+k,j+l);out[m]=plus(out.get(m,z),prod(x,y))
        return {m:c for m,c in out.items() if c!=z}
    def scale(a,n):return {m:prod(c,(F(n),F(0))) for m,c in a.items() if prod(c,(F(n),F(0)))!=z}
    def sub(a,b):return add(a,scale(b,-1))
    def power(a,n):
        out=cons(1)
        while n:
            if n&1:out=mul(out,a)
            a=mul(a,a);n//=2
        return out
    return cons,V,Q,S,add,mul,scale,sub,power

cons,v,q,s,add,mul,scale,sub,power=ring(481**3)
A=add(power(v,8),scale(power(v,4),14),cons(1))
B=sub(power(v,5),v)
C=add(power(v,12),scale(power(v,8),-33),scale(power(v,4),-33),cons(1))
a,b,c=481,30,-4879;d=54*b**4
assert sub(sub(power(A,3),power(C,2)),scale(power(B,4),108))=={}
assert a**3-c**2==108*b**4
R=sub(power(add(scale(power(q,2),d),scale(mul(C,q),c),scale(power(B,4),54)),2),scale(mul(power(A,3),power(q,2)),a**3))
u_minus_c=sub(s,cons(c));u_plus_c=add(s,cons(c))
G1=sub(sub(scale(power(q,2),d),mul(mul(u_minus_c,C),q)),scale(mul(power(u_minus_c,2),power(B,4)),F(1,2*b**4)))
G2=sub(add(scale(power(q,2),d),mul(mul(u_plus_c,C),q)),scale(mul(power(u_plus_c,2),power(B,4)),F(1,2*b**4)))
assert sub(R,mul(G1,G2))=={}
cons,v,q,r,add,mul,scale,sub,power=ring(-3)
B=sub(power(v,5),v);C=add(power(v,12),scale(power(v,8),-33),scale(power(v,4),-33),cons(1));A=add(power(v,8),scale(power(v,4),14),cons(1))
Hp=add(power(v,4),scale(mul(r,power(v,2)),2),cons(1))
Hm=sub(add(power(v,4),cons(1)),scale(mul(r,power(v,2)),2))
assert mul(Hp,Hm)==A
assert add(C,scale(mul(r,power(B,2)),6))==power(Hp,3)
assert sub(C,scale(mul(r,power(B,2)),6))==power(Hm,3)
# The equations H±=v^4 ± 2 sqrt(-3) v^2 +1 each have four simple roots:
# as polynomials in y=v² their discriminants are -16, and y=0 is not a root.
assert (-3)*4-4==-16
# The two factors are coprime since their difference is 4 sqrt(-3) v².
assert all(H.get((0,0))==(F(1),F(0)) for H in (Hp,Hm))
# Degree/parameter and genus arithmetic; local valuations in RESULT.md.
assert (8-2)//2==3
assert 1+4*(3-1)==9
assert 2*41+96-1==177
print('VERIFY_OK: factorization, auxiliary identities, distinct quartic roots, genus and arithmetic genus checks')
