from math import comb

def K_bound(q, rho, t, r):
    a = rho - 2*r + t - 2
    b = rho - 2*r - 1
    vals = []
    for h in range(a+1, rho+1):
        num = (q**h - q**(h-a))*h - b*(q**h - 1)
        den = q**(h-a) - 1
        vals.append((h, num // den))
    return min(v for _, v in vals)

def V(Q, n, r):
    return sum(comb(n, i)*(Q-1)**i for i in range(r+1))

def residual_binary_rho15():
    q, rho = 2, 15
    exceptional_aux = {(3,4),(3,5),(4,5),(4,6)}
    survivors = []
    for t in range(1, rho+1):
        for r in range(t, rho+1):
            if t <= 2: continue
            if r == t: continue
            if t >= rho - 4: continue
            if 2*r + 3 > rho + t: continue
            if 3*r >= 2*rho: continue
            if (t,r) in exceptional_aux: continue
            if q >= r: continue
            K = K_bound(q, rho, t, r)
            if K <= 5*t - 2: continue
            N = rho + K
            if comb(N, r) < q**(t*(rho-r)): continue
            survivors.append((t, r, K, N))
    return survivors

survivors = residual_binary_rho15()
assert survivors == [(3, 6, 78, 93)]
Nmax=64; kmax=58; nmax=73
lhs=V(8,nmax,6); rhs=2**45
assert lhs < rhs

points=list(range(1,64))
mult={x:1 for x in points}
mult[1]+=1
lines=set()
for a in points:
    for b in points:
        if a < b:
            line=tuple(sorted((a,b,a^b)))
            if len(set(line))==3:
                lines.add(line)

assert len(lines)==651
assert max(sum(mult[x] for x in L) for L in lines)==4
assert sum(mult.values())==64
print('ALL EXACT CHECKS PASSED')
