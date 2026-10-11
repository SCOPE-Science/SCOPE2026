from fractions import Fraction as F

# Polynomial arithmetic for variables (x,y,z,g).
def add(a,b):
    c=dict(a)
    for m,v in b.items():
        c[m]=c.get(m,F(0))+v
        if c[m]==0: del c[m]
    return c

def mul(a,b):
    c={}
    for ma,va in a.items():
        for mb,vb in b.items():
            m=tuple(u+v for u,v in zip(ma,mb))
            c[m]=c.get(m,F(0))+va*vb
    return {m:v for m,v in c.items() if v}

def neg(a): return {m:-v for m,v in a.items()}
def scale(a,k): return {m:k*v for m,v in a.items() if k*v}
def var(i,n=4):
    e=[0]*n; e[i]=1
    return {tuple(e):F(1)}

one={(0,0,0,0):F(1)}
x,y,z,g=[var(i) for i in range(4)]
f1=add(neg(x),mul(y,z))
f2=add(add(neg(y),neg(mul(x,z))),mul(g,z))
two_minus_g=add(scale(one,F(2)),neg(g))
# V_z*z_dot contributes (2-g) z (y-z), since sigma cancels exactly.
deriv=add(add(mul(x,f1),mul(y,f2)),mul(mul(two_minus_g,z),add(y,neg(z))))
target=add(add(neg(mul(x,x)),neg(mul(add(y,neg(z)),add(y,neg(z))))),neg(mul(add(one,neg(g)),mul(z,z))))
assert deriv==target, (deriv,target)

# Exact equilibrium check in Q[g,r] modulo r^2-(g-1).
# A polynomial is a dict (power_g,power_r) -> coefficient.
def add2(a,b):
    c=dict(a)
    for m,v in b.items():
        c[m]=c.get(m,F(0))+v
        if c[m]==0: del c[m]
    return c

def mul2(a,b):
    c={}
    for (ag,ar),va in a.items():
        for (bg,br),vb in b.items():
            m=(ag+bg,ar+br)
            c[m]=c.get(m,F(0))+va*vb
    return {m:v for m,v in c.items() if v}

def neg2(a): return {m:-v for m,v in a.items()}
def reduce_relation(p):
    p=dict(p)
    while True:
        key=next((m for m in p if m[1]>=2),None)
        if key is None: break
        coeff=p.pop(key); ag,ar=key
        # g^ag r^ar = g^(ag+1) r^(ar-2) - g^ag r^(ar-2)
        for m,v in [((ag+1,ar-2),coeff),((ag,ar-2),-coeff)]:
            p[m]=p.get(m,F(0))+v
            if p[m]==0: del p[m]
    return p

G={(1,0):F(1)}; R={(0,1):F(1)}; O={(0,0):F(1)}
X=add2(G,neg2(O))  # g-1
# y=z=r; signs cancel identically, so checking +r suffices and -r follows by substitution r -> -r.
f1e=add2(neg2(X),mul2(R,R))
f2e=add2(add2(neg2(R),neg2(mul2(X,R))),mul2(G,R))
f3e=add2(R,neg2(R))
assert reduce_relation(f1e)=={}
assert reduce_relation(f2e)=={}
assert reduce_relation(f3e)=={}
print('VERIFY_OK')
