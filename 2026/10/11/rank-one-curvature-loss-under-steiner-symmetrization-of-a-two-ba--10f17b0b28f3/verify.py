"""Numerical cross-checks for the curvature-index theorem.

The universal result is proved analytically; these checks sample only finite cases.
Run with Python 3.9 or newer: python verify.py
"""
import math
import random


def curvature_data(p, q):
    """First form G, averaged spherical curvature form II, and deficit B."""
    av = [(p[i] + q[i]) / 2 for i in range(len(p))]
    wp = math.sqrt(1 + sum(x*x for x in p))
    wq = math.sqrt(1 + sum(x*x for x in q))
    w = math.sqrt(1 + sum(x*x for x in av))
    dim = len(av)
    g = [[float(i == j) + av[i]*av[j] for j in range(dim)] for i in range(dim)]
    b = [[.5*(wp*(float(i == j)+p[i]*p[j]) + wq*(float(i == j)+q[i]*q[j]))-w*g[i][j]
          for j in range(dim)] for i in range(dim)]
    ii = [[(b[i][j]+w*g[i][j])/w for j in range(dim)] for i in range(dim)]
    return g, ii, b


def quad(mat, v):
    return sum(v[i]*mat[i][j]*v[j] for i in range(len(v)) for j in range(len(v)))


def lower_generalized_eigenvalue(g, ii):
    a = g[0][0]*g[1][1]-g[0][1]*g[0][1]
    b = ii[0][0]*g[1][1]+ii[1][1]*g[0][0]-2*ii[0][1]*g[0][1]
    c = ii[0][0]*ii[1][1]-ii[0][1]*ii[0][1]
    disc = max(0., b*b - 4*a*c)
    return (b-math.sqrt(disc))/(2*a)

rng = random.Random(260214090)
count = 0
for dim in (2, 3, 5, 9):
    for _ in range(1000):
        p = [rng.uniform(-15,15) for i in range(dim)]
        q = [rng.uniform(-15,15) for i in range(dim)]
        g, ii, b = curvature_data(p, q)
        diff = [p[i]-q[i] for i in range(dim)]
        dd = sum(x*x for x in diff)
        j = max(range(dim), key=lambda i: abs(diff[i]))
        for i in range(dim):
            if i == j:
                continue
            tangent = [0.] * dim
            tangent[i] = 1.
            tangent[j] = -diff[i]/diff[j]
            assert abs(sum(diff[k]*tangent[k] for k in range(dim))) < 1e-8
            assert quad(b, tangent) > -1e-8 * sum(t*t for t in tangent)
            count += 1
        if dim == 2:
            # Two negative deficit eigenvalues are impossible, so det(B) >= 0
            # need NOT hold: one may be negative. The larger eigenvalue is
            # nonnegative, and this is checked via its trace/discriminant.
            tr = b[0][0]+b[1][1]
            det = b[0][0]*b[1][1]-b[0][1]*b[0][1]
            high=(tr+math.sqrt(max(0,tr*tr-4*det)))/2
            assert high > -1e-9
            count += 1

# Explicit lens used in the primary literature, with the mixed-fiber geometry.
c0=(-.2794,.2451,.36)
x=(.4154,.7262)
ps=[]
for sg in (1,-1):
    d=[x[i]-sg*c0[i] for i in range(2)]
    f=math.sqrt(1-sum(t*t for t in d))
    ps.append([-z/f for z in d])
f_plus=math.sqrt(1-sum((x[i]-c0[i])**2 for i in range(2)))
f_minus=math.sqrt(1-sum((x[i]+c0[i])**2 for i in range(2)))
assert abs(f_plus-f_minus)<2*abs(c0[2])<f_plus+f_minus
G, II, B=curvature_data(*ps)
kmin=lower_generalized_eigenvalue(G,II)
assert 0.965<kmin<0.975, kmin
print('VERIFY_OK',count,'transverse tests; source-lens minimum curvature',round(kmin,9))
