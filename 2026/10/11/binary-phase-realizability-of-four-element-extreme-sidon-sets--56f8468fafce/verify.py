from itertools import product
import cmath


def autocorr_cyclic(n, support, coeffs):
    dct = dict(zip(support, coeffs))
    out=[]
    for d in range(n):
        s=0
        for x,a in dct.items():
            y=(x-d)%n
            if y in dct:
                s += a*dct[y]
        out.append(s)
    return out

# Z7 binary witness.
assert autocorr_cyclic(7,[0,1,2,4],[1,-1,-1,-1]) == [4,0,0,0,0,0,0]

# No binary witness for the Z5 prototype.
z5=[]
for eps in product((1,-1), repeat=4):
    if autocorr_cyclic(5,[0,1,2,3],eps) == [4,0,0,0,0]:
        z5.append(eps)
assert not z5

# Exceptional Z4 x Z2 prototype: no binary witness.
F=[(0,0),(1,0),(3,1),(0,1)]
def sub(u,v): return ((u[0]-v[0])%4,(u[1]-v[1])%2)
exceptional=[]
for eps in product((1,-1), repeat=4):
    C={(a,b):0 for a in range(4) for b in range(2)}
    for i,x in enumerate(F):
        for j,y in enumerate(F):
            C[sub(x,y)] += eps[i]*eps[j]
    if C[(0,0)]==4 and all(v==0 for k,v in C.items() if k!=(0,0)):
        exceptional.append(eps)
assert not exceptional

# Rectangle witnesses in cyclic test groups.  x=N/2 has order two.
rectangle_cases=0
max_err=0.0
for N in range(4,81,2):
    x=N//2
    for y in range(1,N):
        E=[0,x,y,(x+y)%N]
        if len(set(E))<4:
            continue
        coeff={0:1,x:1,y:1,(x+y)%N:-1}
        for k in range(N):
            z=sum(a*cmath.exp(2j*cmath.pi*k*t/N) for t,a in coeff.items())
            max_err=max(max_err,abs(abs(z)-2.0))
        rectangle_cases += 1
assert max_err < 1e-11
print(f"VERIFY_OK rectangle_cases={rectangle_cases} z7=1 z5_binary_solutions={len(z5)} exceptional_binary_solutions={len(exceptional)} max_rectangle_err={max_err:.3e}")
