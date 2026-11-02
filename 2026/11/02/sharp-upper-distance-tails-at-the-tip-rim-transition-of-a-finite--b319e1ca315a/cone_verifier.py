"""Deterministic checks of geodesic pair-distance laws on a circular flat cone.

Standard-library only. Checks are numerical corroboration of separately stated
analytical proofs, not a substitute for the universal limit arguments.
"""
import math

PI = math.pi


def gauss_legendre_01(n):
    """N-point Gauss--Legendre rule on [0,1], computed without dependencies."""
    nodes = [0.0] * n
    weights = [0.0] * n
    m = (n + 1) // 2
    for i in range(m):
        z = math.cos(PI * (i + 0.75) / (n + 0.5))
        for _ in range(20):
            p0, p1 = 1.0, z
            for j in range(2, n + 1):
                p0, p1 = p1, ((2*j-1)*z*p1 - (j-1)*p0)/j
            pn = p1 if n >= 1 else p0
            pprev = p0 if n >= 2 else 1.0
            dp = n * (z * pn - pprev)/(z*z - 1)
            dz = pn / dp
            z -= dz
            if abs(dz) < 2e-15:
                break
        weight = 1.0 / ((1-z*z)*dp*dp)
        nodes[i], nodes[n-1-i] = (1-z)/2, (1+z)/2
        weights[i] = weights[n-1-i] = weight
    return nodes, weights


def prediction(c):
    sn = math.sin(PI*c/2)
    diam = max(1.0, 2*sn)
    if c < 1/3 - 1e-12:
        return diam, 3.0, 4*math.tan(PI*c)/(3*PI*c)
    if abs(c-1/3) <= 1e-12:
        return diam, 3.0, 28/(PI*math.sqrt(3))
    if c < 1 - 1e-12:
        return diam, 3.0, 2/(3*PI*c*math.cos(PI*c/2)*sn*sn)
    return diam, 2.5, 32/(15*PI)


def endpoint_probability(c, eps, n=260):
    """Integrate radial conditional probabilities near all maximal pairs.

    For a fixed first radius and angular separation, solving the quadratic
    distance inequality gives the allowed second-radius interval exactly.
    Only small disjoint neighborhoods of maximizing pairs are required for
    eps <= 0.005 in the tested regimes.
    """
    nodes, weights = gauss_legendre_01(n)
    diam, exponent, coeff = prediction(c)
    result = 0.0
    if c <= 1/3:
        t = 1-eps
        rmax = min(.2, 5*eps/math.cos(PI*c))
        for i,theta0 in enumerate(nodes):
            phi = PI*c*theta0
            cp = math.cos(phi)
            sin2 = 1-cp*cp
            partial = 0.0
            for r0,w in zip(nodes,weights):
                r = rmax*r0
                root = math.sqrt(max(0,t*t-r*r*sin2))
                bound = r*cp + root
                partial += w*r*max(0,1-bound*bound)
            # factor 2 for the two tip--rim orderings
            result += 4*weights[i]*rmax*partial
    if c >= 1/3:
        sn = math.sin(PI*c/2)
        if c < 1:
            delta_max = min(PI, 5*eps/(c*math.cos(PI*c/2)))
        else:
            delta_max = min(PI,5*math.sqrt(eps))
        umax = min(.2,5*eps/max(sn,.5))
        t = diam-eps
        for i,delta0 in enumerate(nodes):
            phi = c*(PI-delta_max*delta0)
            cp,sp = math.cos(phi), math.sin(phi)
            partial = 0.0
            for u0,w in zip(nodes,weights):
                r = 1-umax*u0
                root = math.sqrt(max(0,t*t-r*r*sp*sp))
                bound = r*cp+root
                partial += w*r*max(0,1-bound*bound)
            result += 2/PI*weights[i]*delta_max*umax*partial
    return result


def check():
    nchecks = 0
    for c in [0.12,0.24,1/3,0.40,0.65,0.92,1.0]:
        diam, exp, constant = prediction(c)
        ratios = []
        for eps in [0.005,0.002,0.00075]:
            val = endpoint_probability(c,eps)
            ratio = val / (constant*eps**exp)
            ratios.append(ratio)
            assert abs(ratio-1) < 0.08, (c,eps,ratio)
            nchecks += 1
        assert abs(ratios[-1]-1) < .02, (c,ratios)
        print('c=%.9f diameter=%.9f exponent=%.1f constant=%.9f ratios=%s' %
              (c,diam,exp,constant,[round(z,7) for z in ratios]))
    # Independent tensor quadrature tests the exact second moment.
    nodes,weights = gauss_legendre_01(35)
    for c in [0.12, 1/3, 0.65, 1.0]:
        value = 0.0
        for r,wr in zip(nodes,weights):
            for s,ws in zip(nodes,weights):
                for t,wt in zip(nodes,weights):
                    dsq = r*r+s*s-2*r*s*math.cos(c*PI*t)
                    value += (2*r*wr)*(2*s*ws)*wt*dsq
        exact = 1-8*math.sin(c*PI)/(9*c*PI)
        assert abs(value-exact) < 5e-13,(c,value,exact)
        nchecks += 1
    # The maximum of a convex quadratic over the radial unit square occurs
    # at a corner; direct corner scanning tests the two candidate branches.
    for c in [0.12,0.24,1/3,0.40,0.65,0.92,1.0]:
        diam,_,_ = prediction(c)
        for angle in [0,PI/5,2*PI/5,3*PI/5,4*PI/5,PI]:
            corners = [math.sqrt(r*r+s*s-2*r*s*math.cos(c*angle))
                       for r in (0,1) for s in (0,1)]
            assert max(corners) <= diam+1e-14
            nchecks += 1
    print('PASS: %d independent endpoint, moment and diameter comparisons' % nchecks)

if __name__ == '__main__':
    check()
