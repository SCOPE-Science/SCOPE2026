"""Lane-441 target stress-test certificate (stdlib + numpy only).
Rebuilds SL(2,7), checks C_7 membership, BFS connectedness of Cayley and
bipartite double cover, and spectra. Refutes both conjuncts of target_claim at q=7.
Usage: python3 output/artifacts/verify.py  -> prints VERIFY_OK on success."""
import collections
import numpy as np

q = 7
M = [(a,b,c,d) for a in range(q) for b in range(q) for c in range(q) for d in range(q) if (a*d-b*c) % q == 1]
n = len(M)
assert n == 336, n
idx = {m:i for i,m in enumerate(M)}

def mul(X,Y):
    a,b,c,d = X; e,f,g,h = Y
    return ((a*e+b*g)%q,(a*f+b*h)%q,(c*e+d*g)%q,(c*f+d*h)%q)
def inv(X):
    a,b,c,d = X
    return (d%q,(-b)%q,(-c)%q,a%q)
def mat(a,b,c,d): return (a%q,b%q,c%q,d%q)

I = (1,0,0,1); z = mat(-1,0,0,-1)
def is_unip(g): return (g[0]+g[3])%q == 2 and g != I
def in_C7(S):
    if len(set(S)) != 7 or z not in S: return False
    rest = [g for g in S if g != z]
    if any(inv(g) not in rest or inv(g)==g for g in rest): return False
    reps = []
    for g in rest:
        if g in reps or inv(g) in reps: continue
        reps.append(g)
    return len(reps)==3 and all(is_unip(g) for g in reps)

def cay_comp(S):
    seen={0}; dq=collections.deque([0])
    while dq:
        x=dq.popleft()
        for g in S:
            y=idx[mul(M[x],g)]
            if y not in seen: seen.add(y); dq.append(y)
    return len(seen)

def double_comp(S):
    seen={(0,0)}; dq=collections.deque([(0,0)])
    while dq:
        x,s=dq.popleft()
        for g in S:
            y=(idx[mul(M[x],g)],1-s)
            if y not in seen: seen.add(y); dq.append(y)
    return len(seen)

def adj(S):
    A=np.zeros((n,n))
    for i,x in enumerate(M):
        for g in S: A[i,idx[mul(x,g)]]+=1
    return A

u = lambda a: mat(1,a,0,1)
SB = [z,u(1),u(2),u(3),inv(u(1)),inv(u(2)),inv(u(3))]
# Ramanujan witness: z + 3 inverse-paired R-class unipotents (pair-reps verified unipotent below)
SR = [(6,0,0,6),(4,2,6,5),(2,4,5,0),(1,4,0,1),(5,5,1,4),(0,3,2,2),(1,3,0,1)]

RB = 2*np.sqrt(6)
print("Ramanujan bound 2*sqrt(6) =", RB)

# --- Witness 1: connectivity killer ---
assert in_C7(SB), "SB must lie in C_7"
csb, dsb = cay_comp(SB), double_comp(SB)
print(f"SB in C7: True; Cayley comp={csb}/336; double-cover comp={dsb}/672")
assert csb == 14 and dsb == 28, (csb,dsb)
print("SB verdict: X(SB) DISCONNECTED -> target 'connected for every S' FALSE")

# --- Witness 2: Ramanujan killer ---
assert in_C7(SR), "SR must lie in C_7"
csr, dsr = cay_comp(SR), double_comp(SR)
print(f"SR in C7: True; Cayley comp={csr}/336; double-cover comp={dsr}/672")
assert csr == 336 and dsr == 672
A = adj(SR)
assert (A==A.T).all() and (A.sum(axis=1)==7).all()
ev, V = np.linalg.eigh(A)
o = np.argsort(ev); ev=ev[o]; V=V[:,o]
lam2G, lammin = float(ev[-2]), float(ev[0])
lam2X = max(lam2G,-lammin)
print(f"SR lam2(G)={lam2G:.8f} lammin={lammin:.8f} lam2(X)={lam2X:.8f}")
assert lam2X < RB, "SR must be Ramanujan"
print(f"SR margin 2sqrt6-lam2(X)={RB-lam2X:.8f} > 0 -> universal '>' FALSE")
# cross-checks
B = A.astype(np.int64)
tr2 = int(np.linalg.matrix_power(B,2).trace()); tr4 = int(np.linalg.matrix_power(B,4).trace())
print(f"exact traces: trA^2={tr2} (336*7), trA^4={tr4}; spectral moments {float((ev**2).sum()):.3f},{float((ev**4).sum()):.1f}")
assert tr2 == 2352 and abs(float((ev**2).sum())-tr2)<1e-6 and abs(float((ev**4).sum())-tr4)<1e-3
ev2 = np.linalg.eigvals(A)
assert abs(sorted(ev2.real)[-2]-lam2G)<1e-9, "second eigensolver must agree"
# residual + rounded-Rayleigh replayable bounds
r = A.dot(V[:,n-2])-ev[n-2]*V[:,n-2]
print(f"eigenpair residual_inf={float(np.abs(r).max()):.2e}")
assert float(np.abs(r).max())<1e-10
w = np.round(V[:,n-2],6); w=w-w.mean(); w=w/np.linalg.norm(w)
rq = float(w.dot(A.dot(w)))
print(f"rounded-vector Rayleigh quotient={rq:.8f} (replayable lower bound on lam2(G))")
print("VERIFY_OK")
