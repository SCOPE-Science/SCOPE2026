"""Lane-515 consolidated target audit (replaces v1 ansatz script).
Checks the three verified components + the closed-form obstruction lemma.
Run: python3 output/artifacts/verify_target.py  (exit 0 <-> all PASS)
"""
import json

# 1. setup: D*B1 skew-symmetric
B1=[[0,2,-1],[-1,0,1],[1,-2,0]]; D=[1,2,1]
DB=[[D[i]*B1[i][j] for j in range(3)] for i in range(3)]
assert all(DB[i][j]==-DB[j][i] for i in range(3) for j in range(3))
print("PASS setup: D*B1 skew-symmetric")

# 2. closed-form obstruction: q(a,b,0)=(a-b)^2+b^2>=1 for nonzero integers
S=[[2,-2,-1],[-2,4,-2],[-1,-2,2]]
for a in range(-50,51):
    for b in range(-50,51):
        if (a,b)==(0,0): continue
        q=(S[0][0]*a*a+2*S[0][1]*a*b+S[1][1]*b*b)//2
        assert q==(a-b)**2+b**2>=1, (a,b,q)
print("PASS obstruction: all n3=0 normals real-root side (box +-50 + closed form)")

# 3. component artifacts exist and agree
b2=json.load(open("output/artifacts/b2_slice.json"))
cv=json.load(open("output/artifacts/cvec_bfs.json"))
assert b2["period6"] is True
assert cv["slice0"]==[[-2,-1,0],[-1,-1,0],[-1,0,0],[0,-1,0],[0,1,0],[1,0,0],[1,1,0],[2,1,0]]
assert set(map(tuple,cv["slice0"]))==set(tuple(v[:2])+(0,) for v in b2["b2_cvecs"])
assert all(v=="1" or v=="2" for v in cv["q_slice0"].values())
print("PASS components agree: J*-slice = complete finite B2 root system, all q in {1,2}")
print("CONSOLIDATED AUDIT: VERIFY_OK")
