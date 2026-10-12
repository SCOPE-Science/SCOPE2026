"""Exact finite-field checks of the projective stabilizer formula.

This checker enumerates all normalized projectivities preserving the unique
rational point and its tangent in the cases s=2,3. The all-s proof is symbolic.
"""
from itertools import product


def run_case(p, a0, a1, eta):
    # F_(p^2) = F_p[t]/(t^2 - a1*t - a0).
    Q = p * p
    el = range(Q)

    def add(x, y):
        return ((x % p + y % p) % p) + p * ((x // p + y // p) % p)

    def neg(x):
        return ((-x % p) % p) + p * ((-(x // p) % p) % p)

    def mul(x, y):
        a, b = x % p, x // p
        c, d = y % p, y // p
        return ((a*c + a0*b*d) % p) + p * ((a*d + b*c + a1*b*d) % p)

    def power(x, e):
        y = 1
        while e:
            if e & 1:
                y = mul(y, x)
            x = mul(x, x)
            e //= 2
        return y

    def eq(x,y):
        return x == y

    if power(eta, p) == eta:
        raise AssertionError('eta must be outside prime subfield')
    positives = []
    predicted = set()
    # Each rational stabilizer has unique representative
    # [[a,b,0],[0,1,0],[u,v,w]] with a,w != 0.
    for a in range(1,Q):
        for b in el:
            for u in el:
                for v in el:
                    for w in range(1,Q):
                        lam = power(a,p+1)
                        # Compare the five independent monomial coefficients:
                        # X^(p+1), X^p Y, XY^p, Y^(p+1), Y^pZ and Y Z^p.
                        if add(mul(power(a,p),b),power(u,p)) != 0:
                            continue
                        if add(mul(a,power(b,p)),u) != 0:
                            continue
                        yy = add(add(add(power(b,p+1),eta),v),power(v,p))
                        if yy != mul(lam,eta):
                            continue
                        if w != lam or power(w,p) != lam:
                            continue
                        positives.append((a,b,u,v,w))
    for a in range(1,Q):
        if power(a,p+1) != 1:
            continue
        for b in el:
            for v in el:
                if add(add(v,power(v,p)),power(b,p+1)) == 0:
                    predicted.add((a,b,neg(mul(a,power(b,p))),v,1))
    found = set(positives)
    assert found == predicted, (p, len(found),len(predicted))
    assert len(found) == p**3*(p+1), (p,len(found))
    print(f'FIELD F_{p*p}: {len(found)} stabilizers; exact exhaustive normalized-matrix match')
    # Invariance checked independently on every affine F_(p^2) point of the curve.
    for a,b,u,v,w in positives:
        for X,Y in product(el, repeat=2):
            Z=1
            old = add(add(power(X,p+1),mul(eta,power(Y,p+1))),add(mul(power(Y,p),Z),mul(Y,power(Z,p))))
            X1=add(mul(a,X),mul(b,Y))
            Y1=Y
            Z1=add(add(mul(u,X),mul(v,Y)),mul(w,Z))
            new = add(add(power(X1,p+1),mul(eta,power(Y1,p+1))),add(mul(power(Y1,p),Z1),mul(Y1,power(Z1,p))))
            if old != 0 or new != 0:
                assert old == new == 0 or (old != 0 and new != 0), (p,a,b,X,Y)
    # The unipotent subgroup has order p^3, and p=2 case has one
    # involution and six elements of order four.
    H = [(b,v) for b in el for v in el if add(add(v,power(v,p)),power(b,p+1)) == 0]
    assert len(H) == p**3
    def prod(g,h):
        b,v=g; c,w=h
        return (add(b,c), add(add(v,w),neg(mul(power(b,p),c))))
    assert all(prod(g,h) in H for g in H for h in H)
    if p == 2:
        identity=(0,0)
        nontrivial_involutions=[]
        fours=[]
        for g in H:
            if g == identity:
                continue
            g2 = prod(g,g)
            if g2 == identity:
                nontrivial_involutions.append(g)
            elif prod(g2,g2) == identity:
                fours.append(g)
            else:
                raise AssertionError('unexpected element order')
        assert len(nontrivial_involutions) == 1 and len(fours) == 6
        print('FIELD F_4: unipotent subgroup is quaternion Q_8')


if __name__ == '__main__':
    run_case(2,1,1,2) # t^2=t+1, eta=t
    run_case(3,2,0,3) # t^2=-1, eta=t
    print('HERMITIAN_STABILIZER_EXACT_OK')
