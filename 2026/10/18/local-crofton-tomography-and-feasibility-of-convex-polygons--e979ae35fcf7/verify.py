"""Standalone checks for labeled adjacent-edge Crofton tomography of convex polygons.

Only Python's standard library is used. Finite numerical checks corroborate,
but do not replace, the analytic proof in RESULT.md.
"""
import math
import random


def dot(v, u):
    return v[0]*u[0]+v[1]*u[1]


def sub(v, u):
    return (v[0]-u[0], v[1]-u[1])


def dist(v, u):
    return math.hypot(v[0]-u[0], v[1]-u[1])


def data_from_vertices(vertices):
    n = len(vertices)
    s = [dist(vertices[i], vertices[(i+1) % n]) for i in range(n)]
    perimeter = sum(s)
    m = [2*v/perimeter for v in s]
    q = [(s[i]+s[(i+1) % n] - dist(vertices[i], vertices[(i+2) % n]))/perimeter
         for i in range(n)]
    return perimeter, m, q


def reconstruct(m, q):
    n = len(m)
    assert n >= 3 and len(q) == n and abs(sum(m)-2) < 1e-10
    a = [x/2 for x in m]
    d = [a[i] + a[(i+1) % n] - q[i] for i in range(n)]
    theta = []
    for i in range(n):
        b = a[(i+1) % n]
        z = (a[i]*a[i] + b*b - d[i]*d[i])/(2*a[i]*b)
        assert -1 < z < 1, (i,z)
        theta.append(math.acos(z))
    turn = [math.pi-x for x in theta]
    phi = [0.0]
    for j in range(1,n):
        phi.append(phi[-1]+turn[j-1])
    out = [(0.0,0.0)]
    for i in range(n):
        out.append((out[-1][0]+a[i]*math.cos(phi[i]),
                    out[-1][1]+a[i]*math.sin(phi[i])))
    return out, theta, turn


def approximate_marginal(vertices, i, orientations=8192):
    n=len(vertices)
    total=0
    for j in range(orientations):
        t=math.pi*(j+0.3)/orientations
        normal=(math.cos(t),math.sin(t))
        x=dot(vertices[i],normal)
        y=dot(vertices[(i+1)%n],normal)
        total+=abs(x-y)
    return math.pi*total/orientations


def approximate_adjacent(vertices, i, orientations=8192):
    n=len(vertices)
    total=0
    for j in range(orientations):
        t=math.pi*(j+0.3)/orientations
        normal=(math.cos(t),math.sin(t))
        p=[dot(vertices[(i+k)%n],normal) for k in range(3)]
        overlap=max(0.,min(max(p[0],p[1]),max(p[1],p[2]))-
                       max(min(p[0],p[1]),min(p[1],p[2])))
        total+=overlap
    return math.pi*total/orientations


def polygon(n, seed):
    random.seed(seed)
    intervals=[random.uniform(0.6,1.5) for _ in range(n)]
    cum=[0]
    for value in intervals: cum.append(cum[-1]+value)
    angles=[2*math.pi*u/cum[-1] for u in cum[:-1]]
    return [(1.7*math.cos(t)+0.35*math.sin(t),
             0.15*math.cos(t)+0.9*math.sin(t)) for t in angles]


def main():
    comparisons=0
    for n in [3,4,5,6,7,10,13]:
        for seed in [3,11,29]:
            vertices=polygon(n,seed)
            P,m,q=data_from_vertices(vertices)
            assert all(0 < x < 1 for x in m)
            assert all(x>0 for x in q)
            assert abs(sum(m)-2)<1e-12
            out,theta,turn=reconstruct(m,q)
            assert abs(sum(turn)-2*math.pi)<3e-12
            assert dist(out[-1],out[0])<3e-12
            for i in range(n):
                for j in range(i+1,n):
                    assert abs(dist(out[i],out[j])-dist(vertices[i],vertices[j])/P)<4e-12
                    comparisons+=1
            # Independent angular integration of line measures, not a restatement
            # of the analytic edge-length formula.
            for i in range(n):
                marginal=approximate_marginal(vertices,i)/P
                adjacent=approximate_adjacent(vertices,i)/P
                assert abs(marginal-m[i])<1e-6, (n,seed,i,marginal,m[i])
                assert abs(adjacent-q[i])<1e-6, (n,seed,i,adjacent,q[i])
                comparisons+=2
    # Locally valid side pairs need not satisfy global polygonal closure.
    v=polygon(6,41)
    _,m,q=data_from_vertices(v)
    q_bad=list(q)
    q_bad[0]+=1e-4
    out,theta,turn=reconstruct(m,q_bad)
    assert abs(sum(turn)-2*math.pi)>1e-7 or dist(out[0],out[-1])>1e-7
    comparisons+=1
    # Equilateral specialization needs adjacent-pair observations only.
    for n in [3,4,5,8,15]:
        vertices=[(math.cos(2*math.pi*j/n),math.sin(2*math.pi*j/n)) for j in range(n)]
        P,m,q=data_from_vertices(vertices)
        assert max(abs(x-2/n) for x in m)<1e-14
        out,theta,turn=reconstruct([2/n]*n,q)
        for i in range(n):
            for j in range(n):
                assert abs(dist(out[i],out[j])-dist(vertices[i],vertices[j])/P)<2e-12
                comparisons+=1
    print(f"ADJACENT_CROFTON_TOMOGRAPHY_OK polygon_cases=21 regular_cases=5 exact_distance_and_quadrature_checks={comparisons}")


if __name__ == '__main__':
    main()
