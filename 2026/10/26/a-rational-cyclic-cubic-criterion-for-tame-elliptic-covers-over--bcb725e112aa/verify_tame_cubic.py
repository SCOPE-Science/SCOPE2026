"""Exact finite-field corroboration for rational cyclic-cubic elliptic covers.

The proof is mathematical; this script verifies the finite automorphism
and Frobenius calculations in GF(16). No external dependencies required.
"""
MOD=0b10011

def mul(a,b):
    out=0
    while b:
        if b&1:out^=a
        b>>=1
        a<<=1
        if a&16:a^=MOD
    return out

def power(a,n):
    out=1
    while n:
        if n&1:out=mul(out,a)
        a=mul(a,a)
        n>>=1
    return out

def compose(f,g):
    # f after g, for (x,y) -> (u^2*x+r, y+u^2*s*x+t).
    u,r,s,t=f
    v,R,S,T=g
    return (mul(u,v), mul(power(u,2),R)^r,
            mul(power(u,13),S)^s, T^mul(power(u,2),mul(s,R))^t)

def frobenius(f):
    return tuple(power(x,2) for x in f)

ONE=(1,0,0,0)

def automorphisms(a,b):
    # E_{a,b}: y^2+y=x^3+a*x+b; b cancels in automorphism equations.
    out=[]
    for u in range(1,16):
        if power(u,3)!=1:continue
        for r in range(16):
            s=power(r,2)^mul(a,1^u)
            if power(s,2)!=r:continue
            for t in range(16):
                if power(t,2)^t == power(r,3)^mul(a,r):
                    out.append((u,r,s,t))
    assert len(out)==24
    return out

def stable_groups(a,b):
    autos=automorphisms(a,b)
    generators=[f for f in autos if f!=ONE and compose(compose(f,f),f)==ONE]
    assert len(generators)==8
    stable=[]
    for f in generators:
        if frobenius(f)==compose(f,f):
            key=tuple(sorted([f,compose(f,f)]))
            if key not in stable:stable.append(key)
    return len(generators),len(stable)

def points(a,b):
    n=1
    for x in (0,1):
        for y in (0,1):
            if (y^y)==(x^mul(a,x)^b): # y^2=y in F2, so y^2+y=0.
                n+=1
    return n

def supersingular_points(a,b):
    return 1+sum(1 for x in (0,1) for y in (0,1)
                 if (y*y^y)==(x*x*x^a*x^b))

def main():
    for a,b,expected_n,expected_groups in [(0,0,3,2),(1,0,5,0),(1,1,1,0)]:
        # In F2 y^2+y=0, x^3=x; rhs=x+a*x+b.
        n=1+sum(1 for x in (0,1) for y in (0,1)
                if ((y*y)^y)==((x*x*x)^(a*x)^b))
        generators,stable=stable_groups(a,b)
        assert (n,generators,stable)==(expected_n,8,expected_groups)
        print(f'E_a,b=({a},{b}) rational_points={n} order3_generators={generators} frobenius_stable_C3={stable}')
    print('ALL GF16 AUTOMORPHISM CHECKS PASSED')
if __name__=='__main__':main()
