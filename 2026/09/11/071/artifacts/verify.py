"""Self-contained verifier for the PG(2,13) size-24 minimal non-Redei blocking set.
Stdlib only. Rebuilds the 183-point/183-line normalized model of PG(2,13)
(first nonzero homogeneous coordinate = 1) and checks the witness B.
"""
q = 13
B = [(0,1,8),(0,1,11),(1,0,0),(1,1,1),(1,1,2),(1,1,7),(1,2,2),(1,3,3),
     (1,3,5),(1,4,2),(1,4,4),(1,4,8),(1,5,9),(1,6,1),(1,7,3),(1,8,7),
     (1,8,8),(1,9,12),(1,10,10),(1,11,8),(1,11,11),(1,12,4),(1,12,6),(1,12,12)]

def norm(t):
    for v in t:
        if v % q != 0:
            inv = pow(v, q-2, q)
            return tuple((x*inv) % q for x in t)
    raise ValueError("zero vector")

pts, seen = [], {}
for a in range(q):
    for b in range(q):
        for c in range(q):
            if a == b == c == 0:
                continue
            n = norm((a,b,c))
            if n not in seen:
                seen[n] = len(pts)
                pts.append(n)
assert len(pts) == 183

lines, seenL = [], {}
for a in range(q):
    for b in range(q):
        for c in range(q):
            if a == b == c == 0:
                continue
            n = norm((a,b,c))
            if n not in seenL:
                seenL[n] = len(lines)
                lines.append(n)
assert len(lines) == 183

S = set(B)
assert len(S) == 24
import collections
sec = []
for (A,Bb,C) in lines:
    sec.append(sum(1 for (x,y,z) in S if (A*x+Bb*y+C*z) % q == 0))
hist = dict(collections.Counter(sec))
uncovered = sum(1 for k in sec if k == 0)
has14 = sum(1 for k in sec if k == 14)
n11 = hist.get(11, 0)
print("npts=183 nlines=183")
print("uncovered:", uncovered)
print("has14:", has14)
print("hist:", hist, "sum:", sum(hist.values()))
print("n11:", n11, "max:", max(sec))
noness = []
tangents = {}
for p in B:
    x,y,z = p
    tg = [L for L in lines
          if (L[0]*x+L[1]*y+L[2]*z) % q == 0
          and sum(1 for (a,b,c) in S if (L[0]*a+L[1]*b+L[2]*c) % q == 0) == 1]
    if tg:
        tangents[p] = tg[0]
    else:
        noness.append(p)
print("nonessential:", noness)
for p in B:
    print(p, "tangent:", tangents.get(p))
# deletion test: every point essential
for p in B:
    rest = S - {p}
    if not any(all((L[0]*x+L[1]*y+L[2]*z) % q != 0 for (x,y,z) in rest) for L in lines):
        print("NOT ESSENTIAL:", p)
        raise SystemExit(1)
assert uncovered == 0 and has14 == 0 and not noness and n11 == 0 and max(sec) == 9
print("VERIFY_OK")
