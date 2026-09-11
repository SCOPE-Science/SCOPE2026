"""Extend Q-line/Q-point box search to [-12,12]^4. Exact integer arithmetic."""
from itertools import product
import math
a=[2,7,8,-17]
R=range(-12,13)
reps={}
n=0
for p in product(R,repeat=4):
    if not any(p): continue
    if sum(a[i]*p[i]**4 for i in range(4))!=0: continue
    n+=1
    g=0
    for v in p: g=math.gcd(g,v)
    q=tuple(v//g for v in p)
    for v in q:
        if v!=0:
            if v<0: q=tuple(-x for x in q)
            break
    reps[q]=True
print("raw pts:",n,"projective Q-points:",len(reps),sorted(reps))
reps=list(reps)
def mix(p,q,e): return sum(a[k]*p[k]**(4-e)*q[k]**e for k in range(4))
lines=[(p,q) for i,p in enumerate(reps) for q in reps[i+1:] if all(mix(p,q,e)==0 for e in range(5))]
print("Q-lines in [-12,12] box:",lines)
print("DONE")
