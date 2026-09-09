import numpy as np, math, itertools, random
c1, s1 = math.cos(1.0), math.sin(1.0)
M = np.array([[0.7*c1, -0.7*s1],[0.4*s1, 0.4*c1]])
rho = math.sqrt(0.28)
cphi = (0.7*c1+0.4*c1)/(2*rho); sphi = math.sqrt(1-cphi**2)
m11, m21 = M[0,0], M[1,0]
q = np.array([(rho*cphi-m11)/(rho*sphi), -m21/(rho*sphi)])
Pinv = np.array([[1, -q[0]/q[1]],[0, 1/q[1]]])
t = [np.array([0.,0.]), np.array([1.,0.]), np.array([0.,1.])]
def dst(a, b): return np.linalg.norm(Pinv@(a-b))
C = {}
for w in itertools.product(range(3), repeat=4):
    y = np.zeros(2)
    for i in w: y = M@y + t[i]
    C[w] = y
keys = list(C.keys())
rng = random.Random(0)
best = []
for _ in range(12):
    order = rng.sample(keys, len(keys))
    ch = []
    R = 2.8095495215726323; rad = rho**4*R
    for k in order:
        if all(dst(C[k], C[j]) > 2*rad for j in ch): ch.append(k)
    if len(ch) > len(best): best = ch
print([list(w) for w in best])
