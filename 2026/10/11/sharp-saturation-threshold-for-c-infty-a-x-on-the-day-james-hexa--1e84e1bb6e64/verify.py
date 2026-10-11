from fractions import Fraction as F
from itertools import combinations

def N(p):
    x,y=p
    return max(abs(x),abs(y),abs(x-y))

# Endpoint approximants for a=1: x=(1,1), y=(0,1-e), z=(-(1-e),0).
for k in range(2,13):
    e=F(1,k)
    x=(F(1),F(1)); y=(F(0),F(1)-e); z=(-(F(1)-e),F(0))
    sep=N((y[0]-z[0],y[1]-z[1]))
    assert sep < 1
    D=2*N(x)**2+N(y)**2+N(z)**2
    q1=N((x[0]+y[0],x[1]+y[1]))**2/D
    q2=N((x[0]-z[0],x[1]-z[1]))**2/D
    assert q1==q2 and q1 < 1
assert q1 > F(99,100)

# Exact LP check of the face lemma. Unit ball: |u|,|v|,|u-v| <= 1.
verts=[(F(1),F(1)),(F(1),F(0)),(F(0),F(-1)),(F(-1),F(-1)),(F(-1),F(0)),(F(0),F(1))]
faces=[(verts[i],verts[(i+1)%6]) for i in range(6)]

def incident(v):
    return [i for i,(a,b) in enumerate(faces) if v==a or v==b]

def lincomb(p,q,a):
    return (p[0]+a*(q[0]-p[0]), p[1]+a*(q[1]-p[1]))

def min_pair(fi,fj):
    # variables a,b,t; constraints A*a+B*b+C*t <= d
    f1=faces[fi]; f2=faces[fj]
    p=f1[0]; dp=(f1[1][0]-p[0],f1[1][1]-p[1])
    q=f2[0]; dq=(f2[1][0]-q[0],f2[1][1]-q[1])
    cons=[]
    # 0<=a,b<=1
    cons += [(F(-1),F(0),F(0),F(0)),(F(1),F(0),F(0),F(1)),(F(0),F(-1),F(0),F(0)),(F(0),F(1),F(0),F(1))]
    # |u|,|v|,|u-v| <= t for u=y+w
    base=(p[0]+q[0],p[1]+q[1]); da=(dp[0],dp[1]); db=(dq[0],dq[1])
    forms=[(base[0],da[0],db[0]),(base[1],da[1],db[1]),(base[0]-base[1],da[0]-da[1],db[0]-db[1])]
    for c0,ca,cb in forms:
        cons.append((ca,cb,F(-1),-c0))
        cons.append((-ca,-cb,F(-1),c0))
    best=None
    for idxs in combinations(range(len(cons)),3):
        M=[]; rhs=[]
        for i in idxs:
            A,B,C,d=cons[i]; M.append([A,B,C]); rhs.append(d)
        # Gaussian elimination exact
        aug=[M[i]+[rhs[i]] for i in range(3)]
        ok=True
        for col in range(3):
            piv=next((r for r in range(col,3) if aug[r][col]),None)
            if piv is None: ok=False; break
            aug[col],aug[piv]=aug[piv],aug[col]
            z=aug[col][col]; aug[col]=[v/z for v in aug[col]]
            for r in range(3):
                if r!=col and aug[r][col]:
                    z=aug[r][col]; aug[r]=[aug[r][j]-z*aug[col][j] for j in range(4)]
        if not ok: continue
        a,b,t=[aug[i][3] for i in range(3)]
        if all(A*a+B*b+C*t <= d for A,B,C,d in cons):
            if best is None or t<best: best=t
    return best

mins=[]
for v in verts:
    inc=incident(v)
    assert len(inc)==2
    for fi in inc:
        for fj in inc:
            m=min_pair(fi,fj); mins.append(m)
            assert m is not None and m>=1
assert min(mins)==1
print('VERIFY_OK endpoint_approximants=11 face_pairs=%d min_separation=%s'%(len(mins),min(mins)))
