import math, random
EPS=1e-7
def norm(v): return math.sqrt(sum(x*x for x in v))
def pure(gs,u):
    A=sum(g for g in gs if g>0); B=-sum(g for g in gs if g<0); S=A+B
    if S==0: return 0.0
    return A if u < A/S else -B
def rescale(original, transformed, eps=EPS):
    nt=norm(transformed); no=norm(original)
    return [x*no/(nt+eps) for x in transformed]

for a in (0.1,1.0,7.5,100.0):
    assert pure([a,-a],0.25)==a
    assert pure([a,-a],0.75)==-a
    assert rescale([0.0],[a])==[0.0]
    assert rescale([0.0],[-a])==[0.0]

random.seed(350073)
for _ in range(2000):
    d=random.randint(1,12)
    v=[random.uniform(-10,10) for _ in range(d)]
    original=[0.0]*d
    transformed=[random.uniform(-20,20) for _ in range(d)]
    assert norm(rescale(original,transformed))==0.0

for _ in range(5000):
    d=random.randint(1,12)
    original=[random.uniform(-100,100) for _ in range(d)]
    transformed=[random.uniform(-100,100) for _ in range(d)]
    out=rescale(original,transformed)
    assert norm(out) <= norm(original)+1e-12
    if norm(transformed)>0 and norm(original)>0:
        assert norm(out) < norm(original)

a=3.0
for delta in (1e-1,1e-3,1e-6,1e-9):
    original=[delta]
    for u in (0.1,0.9):
        raw=pure([a,-a+delta],u)
        assert abs(raw)>2.0
        out=rescale(original,[raw])
        assert abs(out[0]) <= abs(original[0])+1e-15

print("verification passed")
