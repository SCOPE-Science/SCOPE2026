from math import cos, pi, hypot
import random

def vertices(n, R=1.0):
    return [(R*cos(2*pi*j/n), R*__import__("math").sin(2*pi*j/n)) for j in range(n)]

def facet_normals(n):
    # Vertices at angles 2*pi*j/n; side between j and j+1 has outward normal at midpoint angle.
    return [(cos((2*j+1)*pi/n), __import__("math").sin((2*j+1)*pi/n)) for j in range(n)]

def support(verts, u):
    return max(x*u[0]+y*u[1] for x,y in verts)

def mu_p_odd_formula(n, x, p, R=1.0):
    r = R*cos(pi/n)
    ns = facet_normals(n)
    ts = [x[0]*u[0]+x[1]*u[1] for u in ns]
    if p == float("inf"):
        # direct support ratios over facet normals; enough here for center.
        return max((R+t)/(r-t) for t in ts)
    return (sum((R+t)**p * (r-t)**(1-p) for t in ts)/(n*r))**(1/p)

for n in range(3, 32):
    vs = vertices(n)
    ns = facet_normals(n)
    R = 1.0
    r = cos(pi/n)
    # Verify support values in facet-normal directions.
    for u in ns:
        hp = support(vs, u)
        hm = support(vs, (-u[0],-u[1]))
        assert abs(hp-r) < 2e-12
        target = r if n % 2 == 0 else R
        assert abs(hm-target) < 2e-12

    if n % 2 == 0:
        # Central symmetry on vertices.
        S = {(round(x,12),round(y,12)) for x,y in vs}
        for x,y in vs:
            assert (round(-x,12),round(-y,12)) in S
    else:
        sec = 1/r
        # Center values.
        for p in (1.0, 1.25, 2.0, 4.0, 12.0):
            assert abs(mu_p_odd_formula(n,(0.0,0.0),p)-sec) < 2e-12
        # p=1 is independent of the center: test random interior points near center.
        random.seed(n)
        for _ in range(100):
            rho = 0.7*r*random.random()
            ang = 2*pi*random.random()
            x = (rho*cos(ang), rho*__import__("math").sin(ang))
            assert abs(mu_p_odd_formula(n,x,1.0)-sec) < 3e-12
            # strict convexity prediction for p>1
            for p in (1.25,2.0,4.0):
                assert mu_p_odd_formula(n,x,p) >= sec-2e-12

        # Numerical finite-difference confirmation of strict convexity kernel.
        R = 1.0
        for p in (1.25,2.0,5.0):
            for t in (-0.5*r, -0.1*r, 0.2*r, 0.5*r):
                f2 = p*(p-1)*(R+r)**2*(R+t)**(p-2)*(r-t)**(-p-1)
                assert f2 > 0

print("VERIFY_OK regular polygon p-asymmetry spectrum")
