import math
import random

# K4 incidence matrix, rows indexed by i<j.
D = [
    [1,-1,0,0],
    [1,0,-1,0],
    [1,0,0,-1],
    [0,1,-1,0],
    [0,1,0,-1],
    [0,0,1,-1],
]

# Check D^T D = 4I-J exactly.
G = [[sum(D[r][i]*D[r][j] for r in range(6)) for j in range(4)] for i in range(4)]
target = [[3 if i==j else -1 for j in range(4)] for i in range(4)]
assert G == target

# Infinity operator norm is max absolute row sum.
assert max(sum(abs(v) for v in row) for row in D) == 2

def lp(v,p):
    if math.isinf(p):
        return max(abs(x) for x in v)
    return sum(abs(x)**p for x in v)**(1.0/p)

def apply(a):
    return [sum(row[j]*a[j] for j in range(4)) for row in D]

eq = [1.0,1.0,-1.0,-1.0]
for p in [2.0,2.25,3.0,4.0,6.0,12.0,float("inf")]:
    ratio = lp(apply(eq),p)/lp(eq,p)
    assert abs(ratio-2.0) < 1e-12

# Reproducibility sampling of scalar p-energy inequality.
random.seed(230076)
samples = 0
for p in [2.0,2.25,2.5,3.0,4.0,6.0,10.0]:
    for _ in range(3000):
        a = [random.uniform(-2.0,2.0) for _ in range(4)]
        lhs = sum(abs(z)**p for z in apply(a))
        rhs = (2.0**p)*sum(abs(z)**p for z in a)
        assert lhs <= rhs + 2e-10*max(1.0,rhs)
        samples += 1

# Tetrahedral equality configuration for representative p.
tetra_checks = 0
signs = [
    (1,1,1),
    (1,-1,-1),
    (-1,1,-1),
    (-1,-1,1),
]
for p in [2.0,2.25,3.0,4.0,6.0,12.0,40.0]:
    a = 3.0**(-1.0/p)
    xs = [[a*s for s in row] for row in signs]
    for x in xs:
        assert abs(lp(x,p)-1.0) < 1e-12
    for k in range(3):
        assert abs(sum(x[k] for x in xs)) < 1e-12
    ds = []
    for i in range(4):
        for j in range(i+1,4):
            d = lp([xs[i][k]-xs[j][k] for k in range(3)],p)
            ds.append(d)
    expected_d = 2.0*(2.0/3.0)**(1.0/p)
    assert max(abs(d-expected_d) for d in ds) < 1e-12
    objective = sum(d*d for d in ds)
    expected = 24.0*(2.0/3.0)**(2.0/p)
    assert abs(objective-expected) < 1e-10
    tetra_checks += 1

# Infinity endpoint.
xs = [list(row) for row in signs]
ds = []
for i in range(4):
    for j in range(i+1,4):
        ds.append(lp([xs[i][k]-xs[j][k] for k in range(3)],float("inf")))
assert ds == [2.0]*6
assert sum(d*d for d in ds) == 24.0

# Strict dimension jump for representative finite p>2.
jump_checks = 0
for p in [2.01,2.1,2.5,3.0,4.0,6.0,10.0,50.0,200.0]:
    high = 24.0*(2.0/3.0)**(2.0/p)
    planar = 8.0*(1.0+2.0**(1.0-2.0/p))
    assert high > planar
    jump_checks += 1

print(
    "VERIFY_OK "
    f"scalar_samples={samples} tetra_checks={tetra_checks} "
    f"jump_checks={jump_checks} D2=2 Dinf=2"
)
