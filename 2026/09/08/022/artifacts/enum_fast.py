"""Fast Enumerator A2: left-to-right DFS.
Key lemma: all three forbidden patterns start with 1, so for a<b? with a=min check:
for quadruple values (a,b,c,d), forbidden iff a==min and type(b,c,d) in {132,213,321}.
Check only quadruples ending at new last element."""
import sys, json

def enumerate_n(n, kmax_keep=None):
    maxk = n*(n-1)//2
    dist = [0]*(maxk+1)
    perm = [0]*n
    total = 0
    # iterative stack: (pos, next_candidate_v, used_mask, inv)
    # recursive DFS with closure for speed
    sys.setrecursionlimit(10000)
    def dfs(m, used, inv):
        nonlocal total
        if m == n:
            dist[inv] += 1
            total += 1
            return
        P = perm
        for v in range(1, n+1):
            bit = 1 << v
            if used & bit: continue
            # added inversions = # previous > v
            add = 0
            for i in range(m):
                if P[i] > v: add += 1
            P[m] = v
            # check quadruples (i<j<k<m) with new d=v: need P[i]<v,P[i]<P[j],P[i]<P[k] then classify
            ok = True
            # only if m>=3
            if m >= 3:
                for i in range(m):
                    a = P[i]
                    if a > v: continue
                    for j in range(i+1, m):
                        b = P[j]
                        if a > b: continue
                        for k in range(j+1, m):
                            c = P[k]
                            if a > c: continue
                            # a is min; classify (b,c,v): need type in {132,213,321}
                            # comparisons: bc=(b<c), bv=(b<v), cv=(c<v)
                            if b < c:
                                if c < v:
                                    pass  # 123 ok
                                elif b < v:
                                    ok = False  # b<v<c : 132
                                    break
                                else:
                                    pass  # v<b<c : 123 ok
                            else:  # b>c
                                if b < v:
                                    ok = False  # c<b<v : 213
                                    break
                                elif c < v:
                                    pass  # c<v<b : 231? ranks of (b,c,v): b largest,c smallest -> (3,1,2)=312 ok
                                else:
                                    ok = False  # v<c<b : 321
                                    break
                            # NOTE: cases b==c etc impossible (distinct)
                        if not ok: break
                    if not ok: break
            if ok:
                dfs(m+1, used | bit, inv + add)
        P[m] = 0
    dfs(0, 0, 0)
    return total, dist

if __name__ == "__main__":
    n = int(sys.argv[1])
    total, dist = enumerate_n(n)
    print(f"n={n} total={total}", flush=True)
    out = {str(k): dist[k] for k in range(len(dist)) if dist[k]}
    import os
    os.makedirs("biv", exist_ok=True)
    json.dump(out, open(f"biv/distA2_n{n}.json","w"))
