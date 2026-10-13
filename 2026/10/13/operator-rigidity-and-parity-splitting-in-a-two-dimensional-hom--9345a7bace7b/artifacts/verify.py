from itertools import product

def mul(x,y,p):
    a,b=x
    c,d=y
    return ((-a*c + b*d) % p, (a*d + b*c) % p)

def alpha(x,p):
    return (x[0] % p, (-x[1]) % p)

def alpha_pow(x,parity,p):
    return x if parity == 0 else alpha(x,p)

def op(t,x,p):
    a,b=t
    return (a*x[0] % p, b*x[1] % p)

def add(*xs,p):
    return tuple(sum(z[i] for z in xs) % p for i in range(2))

def neg(x,p):
    return ((-x[0])%p,(-x[1])%p)

basis=[(1,0),(0,1)]

def hom_assoc_ok(p):
    for x,y,z in product(basis, repeat=3):
        lhs=mul(alpha(x,p), mul(y,z,p), p)
        rhs=mul(mul(x,y,p), alpha(z,p), p)
        if lhs != rhs:
            return False
    return True

def rb_ok(t,lam,p):
    for x,y in product(basis,repeat=2):
        rx,ry=op(t,x,p),op(t,y,p)
        lhs=mul(rx,ry,p)
        inside=add(mul(rx,y,p),mul(x,ry,p),
                   tuple((lam*v)%p for v in mul(x,y,p)),p=p)
        rhs=op(t,inside,p)
        if lhs != rhs:
            return False
    return True

def nij_ok(t,p):
    for x,y in product(basis,repeat=2):
        nx,ny=op(t,x,p),op(t,y,p)
        lhs=mul(nx,ny,p)
        nxy=op(t,mul(x,y,p),p)
        inside=add(mul(nx,y,p),mul(x,ny,p),neg(nxy,p),p=p)
        rhs=op(t,inside,p)
        if lhs != rhs:
            return False
    return True

def centroid_ok(t,parity,p):
    for x,y in product(basis,repeat=2):
        bxy=op(t,mul(x,y,p),p)
        lhs2=mul(op(t,x,p),alpha_pow(y,parity,p),p)
        lhs3=mul(alpha_pow(x,parity,p),op(t,y,p),p)
        if not (bxy==lhs2==lhs3):
            return False
    return True

def averaging_ok(t,parity,p):
    for x,y in product(basis,repeat=2):
        bx,by=op(t,x,p),op(t,y,p)
        lhs=mul(bx,by,p)
        rhs1=op(t,mul(bx,alpha_pow(y,parity,p),p),p)
        rhs2=op(t,mul(alpha_pow(x,parity,p),by,p),p)
        if not (lhs==rhs1==rhs2):
            return False
    return True

for p in (3,5,7,11):
    assert hom_assoc_ok(p)
    ops=list(product(range(p),repeat=2))

    for lam in range(p):
        got={t for t in ops if rb_ok(t,lam,p)}
        expected={(0,0)}
        if lam != 0:
            expected.add(((-lam)%p,(-lam)%p))
        assert got == expected, ("RB",p,lam,got,expected)

    got_nij={t for t in ops if nij_ok(t,p)}
    exp_nij={(a,a) for a in range(p)}
    assert got_nij == exp_nij, ("Nij",p,got_nij,exp_nij)

    got_cent_even={t for t in ops if centroid_ok(t,0,p)}
    exp_cent_even={(a,a) for a in range(p)}
    assert got_cent_even == exp_cent_even

    got_cent_odd={t for t in ops if centroid_ok(t,1,p)}
    exp_cent_odd={(a,(-a)%p) for a in range(p)}
    assert got_cent_odd == exp_cent_odd

    got_avg_even={t for t in ops if averaging_ok(t,0,p)}
    exp_avg_even={(a,0) for a in range(p)} | {(a,a) for a in range(p)}
    assert got_avg_even == exp_avg_even

    got_avg_odd={t for t in ops if averaging_ok(t,1,p)}
    exp_avg_odd={(a,0) for a in range(p)}
    assert got_avg_odd == exp_avg_odd

    print({
        "q":p,
        "RB_weight_0":1,
        "RB_nonzero_weight":2,
        "Nijenhuis":len(got_nij),
        "centroid_even":len(got_cent_even),
        "centroid_odd":len(got_cent_odd),
        "averaging_even":len(got_avg_even),
        "averaging_odd":len(got_avg_odd)
    })

print("VERIFY_OK")
