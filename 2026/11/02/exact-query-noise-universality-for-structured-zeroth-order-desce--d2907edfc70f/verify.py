#!/usr/bin/env python3
"""Exact finite-branch checks for structured finite-difference noisy quadratics.

Independent checks supplement, but do not replace, the quantified algebraic proof
in RESULT.md. No external data or other package paths are required.
"""
from itertools import combinations, product
from sympy import Matrix, Rational, sqrt, simplify


def frames(d, ell):
    c = Rational(d, ell)
    for indices in combinations(range(d), ell):
        for signs in product((-1, 1), repeat=ell):
            p = Matrix.zeros(d, ell)
            for j, i in enumerate(indices):
                p[i, j] = signs[j] * sqrt(c)
            yield p


def gradient(x, p, lam, h, errors):
    d, ell = p.shape
    base = errors[0]
    f0 = lam * (x.dot(x)) / 2 + base
    out = Matrix.zeros(d, 1)
    for j in range(ell):
        z = x + h*p[:, j]
        fj = lam * z.dot(z) / 2 + errors[j+1]
        out += ((fj-f0)/h)*p[:, j]
    return out


def all_one_step(x, d, ell, lam, eta, h, sigma):
    total_g = Matrix.zeros(d, 1)
    total_g_sq = 0
    total_next_sq = 0
    count = 0
    for p in frames(d, ell):
        for bits in product((-1, 1), repeat=ell+1):
            noise = [sigma*bit for bit in bits]
            g = gradient(x, p, lam, h, noise)
            y = x - eta*g
            total_g += g
            total_g_sq += g.dot(g)
            total_next_sq += y.dot(y)
            count += 1
    return [simplify(a/Rational(count)) for a in total_g], simplify(total_g_sq/count), simplify(total_next_sq/count), count


def factor(d, ell, lam, eta):
    return 1-2*eta*lam+eta*eta*lam*lam*Rational(d,ell)


def innovation(d, ell, lam, eta, h, sigma):
    return eta*eta*(lam*lam*h*h*Rational(d**3,4*ell**2)+2*Rational(d)*sigma*sigma/(h*h))



def gradient_separate_baselines(x, p, lam, h, errors):
    # Each directional difference has its own fresh baseline measurement.
    d, ell = p.shape
    out = Matrix.zeros(d, 1)
    for j in range(ell):
        z = x + h*p[:, j]
        delta = (lam*(z.dot(z)-x.dot(x))/2 + errors[2*j+1]-errors[2*j])/h
        out += delta*p[:, j]
    return out


def test_separate_baselines(d, ell, x_values, lam, eta, h, sigma):
    x=Matrix([Rational(v) for v in x_values]); count=0
    total=0
    for p in frames(d,ell):
        for bits in product((-1,1),repeat=2*ell):
            g=gradient_separate_baselines(x,p,lam,h,[sigma*bit for bit in bits])
            y=x-eta*g
            total+=y.dot(y)
            count+=1
    expected=factor(d,ell,lam,eta)*x.dot(x)+innovation(d,ell,lam,eta,h,sigma)
    assert simplify(total/Rational(count)-expected)==0
    return count


def test_one_step(d, ell, x_values, lam, eta, h, sigma):
    x = Matrix([Rational(z) for z in x_values]); assert len(x)==d
    e_g, e_g_sq, e_x_sq, count = all_one_step(x, d, ell, lam, eta, h, sigma)
    predicted_g = lam*x
    predicted_g_sq = lam**2*Rational(d,ell)*x.dot(x) + lam**2*h*h*Rational(d**3,4*ell**2)+2*d*sigma**2/h**2
    predicted_x = factor(d,ell,lam,eta)*x.dot(x)+innovation(d,ell,lam,eta,h,sigma)
    assert all(simplify(e_g[i]-predicted_g[i])==0 for i in range(d)), ('mean',d,ell)
    assert simplify(e_g_sq-predicted_g_sq)==0, ('gradient sq',d,ell)
    assert simplify(e_x_sq-predicted_x)==0, ('update sq',d,ell)
    return count


def two_step(d, ell, x, lam, eta, h, sigma):
    assert (d,ell)==(2,1)
    paths = []
    for p in frames(d,ell):
        for bits in product((-1,1), repeat=ell+1):
            paths.append(x-eta*gradient(x,p,lam,h,[sigma*v for v in bits]))
    assert len(paths)==16
    total = 0
    for y in paths:
        for p in frames(d,ell):
            for bits in product((-1,1), repeat=ell+1):
                z = y-eta*gradient(y,p,lam,h,[sigma*v for v in bits])
                total += z.dot(z)
    return simplify(total/Rational(16**2))


def run():
    checks = 0
    choices = [
        (2,1,[Rational(2,3),Rational(-1,2)],Rational(3,2),Rational(1,4),Rational(3,5),Rational(2,3)),
        (3,1,[1,2,-3],Rational(2),Rational(1,5),Rational(1,2),Rational(3,4)),
        (3,2,[1,0,-2],Rational(5,3),Rational(1,4),Rational(2,3),Rational(1)),
        (3,3,[2,-1,4],Rational(1),Rational(3,4),Rational(4,5),Rational(1,3)),
        (4,2,[0,1,2,-3],Rational(7,4),Rational(1,4),Rational(5,6),Rational(2,3)),
    ]
    for d,ell,x,lam,eta,h,sigma in choices:
        count = test_one_step(d,ell,x,lam,eta,h,sigma)
        checks += 3
        print(f'one-step: d={d}, ell={ell}, {count} branches, exact first and second moments PASS')
    d,ell,x,lam,eta,h,sigma=choices[0]
    x=Matrix(x)
    r=factor(d,ell,lam,eta)
    b=innovation(d,ell,lam,eta,h,sigma)
    assert simplify(two_step(d,ell,x,lam,eta,h,sigma)-(r*r*x.dot(x)+(1+r)*b))==0
    checks += 1
    print('two-step: 256 independent branches, exact recursion PASS')
    count = test_separate_baselines(3,2,[1,0,-2],Rational(5,3),Rational(1,4),Rational(2,3),Rational(1))
    checks += 1
    print(f'separate baselines: {count} independent branches, same squared risk PASS')
    # Formula for the all-horizon minimizing radius and minimum innovation.
    for d in [2,3,5,8]:
        for ell in range(1,d+1):
            lam=Rational(5,3); sigma=Rational(2,7)
            h4=8*sigma**2*ell**2/(lam**2*d**2)
            A=lam**2*Rational(d**3,4*ell**2)
            B=2*d*sigma**2
            assert simplify(h4-B/A)==0
            assert simplify(2*sqrt(A*B)-sqrt(2)*lam*sigma*d**2/ell)==0
            eta=Rational(ell,d)/lam
            r=factor(d,ell,lam,eta)
            assert simplify(r-(1-Rational(ell,d)))==0
            assert simplify(eta**2*(2*sqrt(A*B))/(1-r)-sqrt(2)*sigma*d/lam)==0
            checks += 4
    print(f'optimal radius and dimension-cancellation identities: {checks} assertions PASS')
    print('All finite-branch and exact symbolic tests passed. These are not substitutes for the proof.')

if __name__=='__main__':
    run()
