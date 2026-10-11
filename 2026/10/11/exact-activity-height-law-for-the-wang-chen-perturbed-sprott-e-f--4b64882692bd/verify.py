from fractions import Fraction as F

# Minimal polynomial algebra in variables (x,y,z,a).
def add(p, q):
    out = dict(p)
    for m, c in q.items():
        out[m] = out.get(m, F(0)) + c
        if out[m] == 0:
            del out[m]
    return out

def scale(p, c):
    return {m: c*v for m, v in p.items() if c*v}

def mul(p, q):
    out = {}
    for m, c in p.items():
        for n, d in q.items():
            k = tuple(m[i] + n[i] for i in range(4))
            out[k] = out.get(k, F(0)) + c*d
    return {m:c for m,c in out.items() if c}

def deriv(p, i):
    out = {}
    for m, c in p.items():
        if m[i]:
            k = list(m); k[i] -= 1; k = tuple(k)
            out[k] = out.get(k, F(0)) + c*m[i]
    return out

def lie(p, field):
    out = {}
    for i in range(3):
        out = add(out, mul(deriv(p, i), field[i]))
    return out

one={(0,0,0,0):F(1)}
x={(1,0,0,0):F(1)}
y={(0,1,0,0):F(1)}
z={(0,0,1,0):F(1)}
a={(0,0,0,1):F(1)}
fx=add(mul(y,z),a)
fy=add(mul(x,x),scale(y,F(-1)))
fz=add(one,scale(x,F(-4)))
field=[fx,fy,fz]

assert lie(x,field)==fx
assert lie(y,field)==fy
assert lie(z,field)==fz

# Exact equilibrium Q=(1/4,1/16,-16a): substitute symbolically in components.
# fx=(1/16)(-16a)+a=0, fy=(1/4)^2-1/16=0, fz=1-4(1/4)=0.
assert F(1,16)*F(-16,1)+1 == 0
assert F(1,4)**2-F(1,16) == 0
assert 1-4*F(1,4) == 0

# Stationary moment conversion: mx=1/4, my=mx2, A=16(mx2-1/16).
for A in [F(0), F(1,7), F(3,2), F(25,4)]:
    mx2 = F(1,16) + A/F(16)
    my = mx2
    assert my == (1+A)/16
    for aval in [F(-3,10), F(0), F(1,100), F(2,3)]:
        yz = -aval
        weighted_height = yz/my
        assert weighted_height == -16*aval/(1+A)

print('VERIFY_OK')
