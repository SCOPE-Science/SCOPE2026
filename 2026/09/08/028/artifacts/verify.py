"""Independent verifier: replays (T_i,p_i) table + witness validity + optimality from
matrices alone (no reuse of search code paths: fresh brute-force enumeration and
C(T,p+1) no-(p+1)-family checks), plus isotopy spot-checks of group-based labels.
Stdlib only.
"""
import itertools, json, os
_HERE = os.path.dirname(os.path.abspath(__file__))

MRAW = """012345103254234501325410451032540123
012345103254235410324501451023540132
012345104253235014351420420531543102
012345104523230154325401451032543210
012345104523231054325410450132543201
012345104532235104321450453021540213
012345105234234150340512453021521403
012345105234253410324501431052540123
012345120534234150305412451203543021
012345123450254013305124431502540231
012345130524254130345012403251521403
012345134052201534325401450123543210
012345134520245031351204403152520413
012345135024201453324510450132543201
012345143250254031305124430512521403
012345143502231450350124425031504213
012345143520205413321054450231534102
012345150432245013304521423150531204
012345150432245013304521431250523104
012345153024245130324501401253530412
012345153204231450340521425013504132
012345153420231504340152425013504231""".split()
assert len(MRAW) == 22
SQS = [[[int(s[6*i+j]) for j in range(6)] for i in range(6)] for s in MRAW]
tab = json.load(open(os.path.join(_HERE, "table.json")))
wit = json.load(open(os.path.join(_HERE, "witnesses.json")))
Texp, pexp = tab["T"], tab["p"]
assert len(Texp) == len(pexp) == 22

for i, M in enumerate(SQS):
    # fresh enumeration via column-subset/symbol check in different loop order
    TR = []
    for cols in itertools.permutations(range(6)):
        seen = set()
        ok = True
        for r in range(6):
            v = M[r][cols[r]]
            if v in seen: ok = False; break
            seen.add(v)
        if ok: TR.append(cols)
    assert len(TR) == Texp[i] == int(wit[str(i+1)]["T"]), (i+1, len(TR), Texp[i])
    p = pexp[i]
    assert wit[str(i+1)]["p"] == p
    F = [set((r, t[r]) for r in range(6)) for t in TR]
    # validate witness family
    WF = [tuple(w) for w in wit[str(i+1)]["witness"]]
    assert len(WF) == p
    used = set()
    for t in WF:
        assert tuple(sorted(t)) == (0,1,2,3,4,5), (i+1, t)
        assert len({M[r][t[r]] for r in range(6)}) == 6, (i+1, t)
        assert t in TR, (i+1, t)
        for r in range(6):
            assert (r, t[r]) not in used, (i+1, t)
            used.add((r, t[r]))
    # optimality: no (p+1) pairwise-disjoint transversals
    for combo in itertools.combinations(range(len(TR)), p+1):
        u = set(); ok = True
        for c in combo:
            if not F[c].isdisjoint(u): ok = False; break
            u |= F[c]
        assert not ok, (i+1, combo)
    print(f"type {i+1}: T={len(TR)} p={p} witness+optimality OK")

# Tarry boundary: all p < 6
assert max(pexp) <= 4 and max(pexp) == 4
assert sorted(tab["extremal"]) == sorted([i+1 for i, v in enumerate(pexp) if v == 4])
# group-based spot check: verify stored isotopy witnesses for types 2 (Z6) and 4 (S3)
Z6 = [[(i+j) % 6 for j in range(6)] for i in range(6)]
def check_isotopy(L, G, r, c, s):
    for i in range(6):
        for j in range(6):
            if s[L[r[i]][c[j]]] != G[i][j]:
                return False
    return True
assert check_isotopy(SQS[1], Z6, [0,3,5,1,2,4],[0,3,5,1,2,4],[0,3,4,1,5,2])
elems = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2)]
mp = {e:k for k,e in enumerate(elems)}
def mul(x,y):
    a1,b1=elems[x]; a2,b2=elems[y]
    return mp[((a1+a2)%2,(b1+(b2 if a1==0 else -b2))%3)]
S3 = [[mul(i,j) for j in range(6)] for i in range(6)]
assert check_isotopy(SQS[3], S3, [0,3,4,1,2,5],[0,3,4,1,2,5],[0,3,4,1,2,5])
print("group-label spot checks OK; pmax=4; ALL VERIFY PASS")
