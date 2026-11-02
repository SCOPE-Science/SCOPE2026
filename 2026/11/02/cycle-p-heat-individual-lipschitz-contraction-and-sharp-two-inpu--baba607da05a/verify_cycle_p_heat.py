"""Reproducible checks for p-heat edge-gradient instability on finite cycles.

Requires Python 3.9 or newer; no third-party packages. This script does not
replace the universal proof in RESULT.md.
"""
from fractions import Fraction


def flux(x, exponent):
    return (1 if x >= 0 else -1) * abs(x) ** (exponent - 1)


def rhs(u, exponent):
    n = len(u)
    return [flux(u[(i + 1) % n] - u[i], exponent)
            + flux(u[(i - 1) % n] - u[i], exponent) for i in range(n)]


def edges(u):
    return [u[(i + 1) % len(u)] - u[i] for i in range(len(u))]


def base(n, exponent):
    r = 4 ** (1 / (exponent - 2))
    a = [1.0, r, -(r + n - 2)] + [1.0] * (n - 3)
    d = [0.0] * n
    d[0] = d[1] = 1.0
    d[2] = d[n - 1] = -1.0
    assert abs(sum(a)) < 1e-10 and abs(sum(d)) < 1e-10
    u, v = [0.0], [0.0]
    for k in range(n - 1):
        u.append(u[-1] + a[k])
        v.append(v[-1] + d[k])
    assert max(abs(x - y) for x,y in zip(edges(u),a)) < 1e-10
    assert max(abs(x - y) for x,y in zip(edges(v),d)) < 1e-10
    return u, v, r


def witness(n, exponent):
    u, v, r = base(n, exponent)
    eps = min(.001, r / 5)
    up = [ui + eps * vi / 2 for ui,vi in zip(u,v)]
    um = [ui - eps * vi / 2 for ui,vi in zip(u,v)]
    diff_f = [fi - gi for fi,gi in zip(rhs(up,exponent),rhs(um,exponent))]
    first_rate = (diff_f[1] - diff_f[0]) / eps
    predicted = exponent - 1
    assert first_rate > 0 and abs(first_rate - predicted) < .02 * predicted, (n,exponent,first_rate)
    return up,um,eps,first_rate


def rk4(u,exponent,step):
    n=len(u)
    a=rhs(u,exponent)
    b=rhs([u[i]+step*a[i]/2 for i in range(n)],exponent)
    c=rhs([u[i]+step*b[i]/2 for i in range(n)],exponent)
    d=rhs([u[i]+step*c[i] for i in range(n)],exponent)
    return [u[i]+step*(a[i]+2*b[i]+2*c[i]+d[i])/6 for i in range(n)]


def check():
    for n in range(3,13):
        u=[Fraction(j*j-5*j+1) for j in range(n)]
        a=edges(u)
        e=[t*abs(t) for t in a]
        f=[e[i]-e[(i-1)%n] for i in range(n)]
        lhs=edges(f)
        rhs2=[e[(i+1)%n]+e[(i-1)%n]-2*e[i] for i in range(n)]
        assert lhs==rhs2
    print('EXACT_EDGE_FLOW_IDENTITY_OK n=3..12 at p=3')
    count=0
    for n in [4,5,6,8,12]:
        for exponent in [1.25,1.5,1.75,2.5,3,4]:
            witness(n,exponent)
            count+=1
    print('TWO_INPUT_INSTANTANEOUS_GROWTH_OK cases=',count)
    for n,exponent in [(4,1.5),(4,3),(8,1.5),(8,3)]:
        up,um,eps,rate=witness(n,exponent)
        t_final = 1e-5 if exponent <2 else 1e-4
        steps=500
        dt=t_final/steps
        for _ in range(steps):
            up=rk4(up,exponent,dt)
            um=rk4(um,exponent,dt)
        diff=[x-y for x,y in zip(up,um)]
        gain=max(abs(x) for x in edges(diff))/eps
        assert gain>1+.05*rate*t_final, (n,exponent,gain)
        print('INTEGRATED_GROWTH',n,exponent,'gain=',f'{gain:.12f}')
    print('ALL_CYCLE_P_HEAT_CHECKS_OK')

if __name__=='__main__':
    check()
