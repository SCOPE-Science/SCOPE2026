from fractions import Fraction

def dnum(a,m):
    a%=m
    return min(a,m-a)

def tmin(N,mask):
    M=2*N
    best=None
    for k in range(N):
        w=max(dnum(2*j*k-bit*N,M) for j,bit in enumerate(mask,1))
        v=Fraction(w,M)
        if best is None or v<best: best=v
    return best

MASKS=[tuple((m>>j)&1 for j in range(3)) for m in range(8)]

def beta(N):
    if N%4==0: return Fraction(1,4)
    if N%4==2: return Fraction(N+2,4*N)
    return Fraction(N+3,4*N)

def f010(N): return Fraction(N+(0,3,2,1)[N%4],4*N)
def f111(N): return Fraction(N+(0,1,2,3)[N%4],4*N)

tests=0
for N in range(5,201):
    vals=[tmin(N,m) for m in MASKS]
    assert max(vals)==beta(N),(N,vals,beta(N))
    assert vals[2]==f010(N),(N,vals[2],f010(N))
    assert vals[7]==f111(N),(N,vals[7],f111(N))
    tests += 8*N
for N in range(5,30):
    assert max(tmin(N,m) for m in MASKS)==beta(N)
    tests += 8*N
print("finite_remainder=5..29")
print("corroborative_range=5..200")
print("exact_grid_target_tests=%d"%tests)
print("VERIFY_OK")
