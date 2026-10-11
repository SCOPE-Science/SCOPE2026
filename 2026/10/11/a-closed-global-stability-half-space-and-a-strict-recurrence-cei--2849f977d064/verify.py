from fractions import Fraction

# Sparse exact polynomial arithmetic in variables (x,Y,z,s,b,c).
N=6

def mono(var, power=1, coeff=1):
    e=[0]*N; e[var]=power
    return {tuple(e): Fraction(coeff)}

def const(q):
    return {(0,)*N: Fraction(q)}

def add(*ps):
    out={}
    for p in ps:
        for e,c in p.items():
            out[e]=out.get(e,Fraction(0))+c
            if out[e]==0: del out[e]
    return out

def scale(p,q):
    q=Fraction(q)
    return {e:q*c for e,c in p.items() if q*c}

def mul(p,q):
    out={}
    for e1,c1 in p.items():
        for e2,c2 in q.items():
            e=tuple(a+b for a,b in zip(e1,e2))
            out[e]=out.get(e,Fraction(0))+c1*c2
            if out[e]==0: del out[e]
    return out

x,Y,z,s,b,c=[mono(i) for i in range(N)]
x2=mul(x,x); Y2=mul(Y,Y); z2=mul(z,z)
# Centered system: x'=z+(Y+s)x, Y'=-bY-x^2, z'=-x-cz.
xdot=add(z,mul(Y,x),mul(s,x))
Ydot=add(scale(mul(b,Y),-1),scale(x2,-1))
zdot=add(scale(x,-1),scale(mul(c,z),-1))
Vdot=add(mul(x,xdot),mul(Y,Ydot),mul(z,zdot))
expected=add(mul(s,x2),scale(mul(b,Y2),-1),scale(mul(c,z2),-1))
assert Vdot==expected, (Vdot,expected)

# Aybar special curve: b=c and a=c+1/c, hence s=1/b-a=-c.
# Substitute s -> -c, b -> c at coefficient level.
def specialize_aybar(p):
    out={}
    for e,coef in p.items():
        ex=list(e)
        # s^k -> (-c)^k; b^j -> c^j
        sign=-1 if ex[3]%2 else 1
        cpow=ex[5]+ex[4]+ex[3]
        ne=(ex[0],ex[1],ex[2],0,0,cpow)
        out[ne]=out.get(ne,Fraction(0))+coef*sign
        if out[ne]==0: del out[ne]
    return out
spec=specialize_aybar(Vdot)
expected_spec=scale(mul(c,add(x2,Y2,z2)),-1)
assert spec==expected_spec, (spec,expected_spec)
print('VERIFY_OK')
