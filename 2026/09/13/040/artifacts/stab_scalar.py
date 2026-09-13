from math import perm as P
# Orbit-size scaling for stabilization on coinvariants:
# invariant orbit-sum class of support type t maps with scalar P(k,t)/P(k+1,t) = (k+1-t)/(k+1) != 0.
print("support-type scaling k -> k+1:")
for t in [2,3,4,5,6,8]:
    for k in [3,4,5,10]:
        print(f" t={t} k={k}->{k+1}: scalar=(k+1-t)/(k+1)={(k+1-t)/(k+1):.4f} nonzero={(k+1-t)!=0}")
    print("---")
# Crude support bound: supp(H^q \otimes W) <= q+4 (G: 2 per 3 deg; H2/H4: <=1 per 2/4 deg; W: <=4).
# Check q+4 <= 2q+3 (range) and <= 2q+2 (boundary) for relevant q.
print("q : q+4 <= 2q+3? <= 2q+2?")
for q in range(0,13):
    print(f" {q:2d} : {q+4} <= {2*q+3}? {q+4<=2*q+3} ; <= {2*q+2}? {q+4<=2*q+2}")
# Tighter bound floor(2q/3)+4 check
print("tighter floor(2q/3)+4 vs boundary:")
for q in range(0,13):
    b=(2*q)//3+4
    print(f" q={q:2d} bound={b:2d} 2q+2={2*q+2:2d} ok={b<=2*q+2}")
