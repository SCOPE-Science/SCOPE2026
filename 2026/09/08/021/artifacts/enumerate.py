"""Enumerate noble-tail window: words over {1,2,3,4} with q(word)<=200.
alpha(w) = [0; w, 1^infty]. Dedup: strip trailing ones (same infinite expansion).
Exact form alpha = (P + Q*sqrt5)/R with integers, R>0, Q>0.
Derivation: prefix convergents p_k/q_k of [0;w]; theta=phi=(1+s)/2=[1;1,1..];
alpha = (p_k*phi + p_{k-1})/(q_k*phi + q_{k-1})."""
from fractions import Fraction
import json

def prefix_convergents(w):
    # returns (p_prev2? ) compute p_k,q_k and p_{k-1},q_{k-1} for [0;w]
    # standard: p[-2]=0,p[-1]=1? For a0=0: use recurrence
    pm2, pm1 = 0, 1   # p_{-2}, p_{-1} relative? Let's do generic:
    qm2, qm1 = 1, 0
    # iterate a0=0 then w
    pals = [0]+list(w)
    for a in pals:
        p = a*pm1 + pm2
        q = a*qm1 + qm2
        pm2, pm1 = pm1, p
        qm2, qm1 = qm1, q
    # now pm1/qm1 = value; pm2/qm2 = previous convergent
    return pm1, qm1, pm2, qm2

def alpha_PQR(w):
    # alpha = (p_k phi + p_{k-1})/(q_k phi + q_{k-1}), phi=(1+s)/2
    pk, qk, pk1, qk1 = prefix_convergents(w)
    # num = pk*(1+s)/2 + pk1 = (pk+2pk1)/2 + pk*s/2 ; den = (qk+2qk1)/2 + qk*s/2
    U = pk + 2*pk1; V = pk
    W = qk + 2*qk1; X = qk
    # alpha = (U+V s)/(W+X s) = ((U+Vs)(W-Xs))/(W^2-5X^2)
    den = W*W - 5*X*X
    P = U*W - 5*V*X
    Q = V*W - U*X
    R = den
    if R < 0:
        P, Q, R = -P, -Q, -R
    assert R > 0
    return P, Q, R

# enumerate words with q<=200
words = []
stack = [[]]
while stack:
    w = stack.pop()
    for a in (1,2,3,4):
        w2 = w+[a]
        # q of [0;w2]
        _, q, _, _ = prefix_convergents(w2)
        if q <= 200 and q >= 1:
            words.append(tuple(w2))
            stack.append(w2)
print("raw words:", len(words))

# dedup: strip trailing ones -> canonical minimal word; empty = pure noble
canon = {}
for w in words:
    c = list(w)
    while len(c)>0 and c[-1]==1:
        c.pop()
    c = tuple(c)
    # keep representative with smallest? all same alpha; record max word length for q? q of canonical <= q of w? stripping reduces q, still<=200
    canon[c] = True
print("distinct alphas (incl empty):", len(canon))

import math
S5 = math.sqrt(5)
recs = []
for c in canon:
    P,Q,R = alpha_PQR(list(c))
    av = (P+Q*S5)/R
    assert 0 < av < 1, (c, av)
    # sanity: CF starts with w then ones? check convergents denom of w
    _, q, _, _ = prefix_convergents(list(c)) if len(c)>0 else (None,1,None,None)
    recs.append({"w": list(c), "P": P, "Q": Q, "R": R, "q": q, "alpha_float": av})
recs.sort(key=lambda r: r["alpha_float"])
print("Q sign check:", set(r["Q"] for r in recs))
# verify CF reconstruction for a few: expand alpha float CF, check prefix + ones
def cf_expand(x, n=20):
    out=[]
    for _ in range(n):
        a=int(math.floor(x)); out.append(a)
        f=x-a
        if f<1e-12: break
        x=1/f
    return out
for r in recs[:3]+recs[-3:]:
    print(r["w"], r["alpha_float"], cf_expand(r["alpha_float"],12))
json.dump(recs, open("output/artifacts/alpha_table.json","w"))
print("saved", len(recs))
