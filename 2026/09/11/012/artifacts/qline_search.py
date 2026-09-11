"""Recovery test 2: search for ANY Q-line on X: 2x0^4+7x1^4+8x2^4-17x3^4=0.
A line spanned by independent p,q in Q^4 lies on X iff the 5 coeff-forms vanish:
sum ai*pi^4=0, sum ai*pi^3*qi=0, sum ai*pi^2*qi^2=0, sum ai*pi*qi^3=0, sum ai*qi^4=0.
Bounded search over small integer p (normalize), solving conics is overkill;
instead brute force pairs with coords in [-6,6]. Exact integer arithmetic."""
from itertools import product
a=[2,7,8,-17]
R=range(-6,7)
pts=[p for p in product(R,repeat=4) if any(p) and sum(a[i]*p[i]**4 for i in range(4))==0]
print("Q-pts with coords in [-6,6]:", len(pts))
# normalize projective: keep one rep per scalar multiple (positive-first-nonzero)
def norm(p):
    for v in p:
        if v!=0:
            return tuple(x//v if all(x%v==0 for x in p) else x for x in p) if False else None
    return None
reps={}
for p in pts:
    # primitive + sign normalize
    import math
    g=0
    for v in p: g=math.gcd(g,v)
    q=tuple(v//g for v in p)
    for v in q:
        if v!=0:
            if v<0: q=tuple(-x for x in q)
            break
    reps[q]=True
print("projective Q-points:", len(reps), sorted(reps)[:10])
lines=[]
reps=list(reps)
for i in range(len(reps)):
    for j in range(i+1,len(reps)):
        p,q=reps[i],reps[j]
        ok=all(sum(a[k]*(p[k]**(3-e))*(q[k]**e) if False else 0 for k in range(4))==0 for e in [])  # placeholder
        # exact conditions e=0..4 mixed
        def mix(e):
            return sum(a[k]*p[k]**(4-e)*q[k]**e for k in range(4))
        if all(mix(e)==0 for e in range(5)):
            lines.append((p,q))
print("Q-lines found in box:", lines)
print("QLINE_RESULT:", "FOUND" if lines else "NONE in [-6,6]^4 box")
