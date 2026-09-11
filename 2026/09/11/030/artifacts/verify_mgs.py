"""Independent verifier for the MGS word w=(2,4,3,1,2,4) on B_T.

Uses a separately written mutation routine (flat-list representation) to
cross-check the BFS search code. Checks:
  (a) each mutated vertex is green (sign-coherent column >= 0) at mutation time,
  (b) per-step B/C replay via the FZ extended-matrix rule,
  (c) sign coherence of every C-matrix,
  (d) terminal C is all-red (every column <= 0, nonzero).
Prints VERIFY_OK plus the full per-step log on success.
"""
n = 4
B0 = [0,3,0,-1, -3,0,1,0, 0,-1,0,2, 1,0,-2,0]  # row-major
C0 = [1,0,0,0, 0,1,0,0, 0,0,1,0, 0,0,0,1]
w = [2,4,3,1,2,4]  # 1-indexed

def mut(B, C, k):
    k -= 1
    Bn = [0]*(n*n)
    for i in range(n):
        for j in range(n):
            if i == k or j == k:
                Bn[i*n+j] = -B[i*n+j]
            else:
                Bn[i*n+j] = (B[i*n+j]
                             + max(B[i*n+k],0)*max(B[k*n+j],0)
                             - max(-B[i*n+k],0)*max(-B[k*n+j],0))
    Cn = [0]*(n*n)
    for i in range(n):
        for j in range(n):
            if j == k:
                Cn[i*n+j] = -C[i*n+j]
            else:
                Cn[i*n+j] = (C[i*n+j]
                             + max(C[i*n+k],0)*max(B[k*n+j],0)
                             - max(-C[i*n+k],0)*max(-B[k*n+j],0))
    return Bn, Cn

def col(C, j):
    return [C[i*n+j] for i in range(n)]

def status(C):
    out = []
    for j in range(n):
        c = col(C, j)
        if all(v >= 0 for v in c) and any(v != 0 for v in c):
            out.append('G')
        elif all(v <= 0 for v in c) and any(v != 0 for v in c):
            out.append('R')
        else:
            out.append('?')
    return out

def mat(B):
    return [[B[i*n+j] for j in range(n)] for i in range(n)]

B, C = list(B0), list(C0)
print("t=0 B=", mat(B))
print("t=0 C=", mat(C), "status=", status(C))
assert status(C) == ['G','G','G','G']
for t, k in enumerate(w):
    st = status(C)
    assert '?' not in st, "sign-coherence failure at step %d" % t
    assert st[k-1] == 'G', "mutated vertex %d not green at step %d (status %s)" % (k, t, st)
    B, C = mut(B, C, k)
    print("t=%d mutate %d B=" % (t+1, k), mat(B))
    print("t=%d mutate %d C=" % (t+1, k), mat(C), "status=", status(C))
assert status(C) == ['R','R','R','R'], status(C)
assert len(w) <= 10
print("LENGTH", len(w), "<= 10 OK")
print("TERMINAL all-red OK")
print("VERIFY_OK")
