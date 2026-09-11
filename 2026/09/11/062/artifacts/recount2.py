"""Independent recount (self-contained, no import from enumerate.py).
Method differs: brute-force compact-edge weights in 1..4 (no linear solver),
attachment-outer loop order, independent thickening check. Same rule set:
F0 (k_surf=0), phi=(-2,-2,1,3), n=4, one k=1, sum s=3, tree+balance+thick counts,
s=0-primary 2-flag rule. Reports per-psi-position counts and total D(1), D(q)."""
import itertools
from collections import defaultdict

ENDS = [("L1",-2),("L2",-2),("R1",1),("R2",3)]
N = 4
WMAX = 4

def trees(n):
    out = []
    for seq in itertools.product(range(n), repeat=n-2):
        deg = [1]*n
        for s in seq:
            deg[s] += 1
        import bisect
        leaves = sorted(i for i in range(n) if deg[i] == 1)
        d = list(deg); edges = []
        for s in seq:
            leaf = leaves.pop(0)
            edges.append((min(leaf,s), max(leaf,s)))
            d[leaf] -= 1; d[s] -= 1
            if d[s] == 1:
                bisect.insort(leaves, s)
        l1, l2 = leaves
        edges.append((min(l1,l2), max(l1,l2)))
        out.append(tuple(sorted(edges)))
    return sorted(set(out))

def run():
    ts = trees(N)
    per = {}
    D = defaultdict(int)
    for p in range(N):
        kvec = [0]*N; kvec[p] = 1
        ndiag = 0; d1 = 0
        for z in range(N):  # size pattern: unique s=0 at z
            sizes = tuple(1 if i != z else 0 for i in range(N))
            t = [kvec[i]+2-2*sizes[i] for i in range(N)]
            if any(x < 0 for x in t) or sum(t) != 3:
                continue
            for attach in itertools.product(range(N), repeat=4):  # attachments OUTER
                for edges in ts:  # trees INNER (opposite order vs enumerate.py)
                    inc = {v: [] for v in range(N)}
                    for ei,(a,b) in enumerate(edges):
                        inc[a].append(ei); inc[b].append(ei)
                    ok = True
                    for v in range(N):
                        if sizes[v] == 0 and kvec[v] == 0:
                            if len(inc[v])+[attach[j]==v for j in range(4)].count(True) != 2:
                                ok = False; break
                    if not ok:
                        continue
                    for w in itertools.product(range(1,WMAX+1), repeat=3):
                        # vertex balance: signed compact sum + end imbalance = 0
                        bal = True
                        for v in range(N):
                            imb = sum(ew for j,(nm,ew) in enumerate(ENDS) if attach[j]==v)
                            s = sum((1 if v==a else -1 if v==b else 0)*w[ei] for ei,(a,b) in enumerate(edges))
                            if s+imb != 0:
                                bal = False; break
                        if not bal:
                            continue
                        for bits in itertools.product([0,1], repeat=3):
                            cnt = [0]*N
                            for ei,(a,b) in enumerate(edges):
                                cnt[a if bits[ei]==0 else b] += 1
                            if cnt != t:
                                continue
                            good = True
                            for v in range(N):
                                if sizes[v]==0 and kvec[v]==0:
                                    fl = []
                                    for ei in inc[v]:
                                        a,b = edges[ei]
                                        th = (v==a and bits[ei]==0) or (v==b and bits[ei]==1)
                                        other = b if v==a else a
                                        dr = +1 if other>v else -1
                                        fl.append((th,dr,w[ei]))
                                    for j,(nm,ew) in enumerate(ENDS):
                                        if attach[j]==v:
                                            fl.append((False,+1 if ew>0 else -1,abs(ew)))
                                    if len(fl)!=2 or not all(f[0] for f in fl):
                                        good=False; break
                                    if fl[0][1]==fl[1][1] or fl[0][2]!=fl[1][2]:
                                        good=False; break
                            if not good:
                                continue
                            m = w[0]*w[1]*w[2]
                            ndiag += 1; d1 += m
                            poly = {0:1}
                            for ww in w:
                                br = {ww-1-2*i:1 for i in range(ww)}
                                np = defaultdict(int)
                                for e1,c1 in poly.items():
                                    for e2,c2 in br.items():
                                        np[e1+e2]+=c1*c2
                                poly = dict(np)
                            for e,c in poly.items():
                                D[e]+=c
        per[p]=(ndiag,d1)
    tot_n = sum(v[0] for v in per.values()); tot_d = sum(v[1] for v in per.values())
    print("per-psi (n,D1):", per)
    print("TOTAL n=",tot_n,"D(1)=",tot_d,"Dq(1)=",sum(D.values()))
    print("symmetric:", all(D[e]==D[-e] for e in list(D)))
    for e in sorted(D):
        print(e,D[e])
    assert tot_n==168 and tot_d==1464, (tot_n,tot_d)
    assert sum(D.values())==1464
    print("RECOUNT2_OK")

if __name__=="__main__":
    run()
