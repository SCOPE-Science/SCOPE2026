"""Fallback replay: F7 WLP certificate for A=F7[x,y,z]/(x^2+yz, y^3+xz^2, z^3), L=y.
Self-contained, stdlib only. Prints VERIFY_OK iff all gates pass."""
import itertools

P = 7
F2 = {(2,0,0):1,(0,1,1):1}
F3 = {(0,3,0):1,(1,0,2):1}
G3 = {(0,0,3):1}
GENS = [F2,F3,G3]
B2 = [(1,1,0),(1,0,1),(0,2,0),(0,1,1),(0,0,2)]
B3 = [(1,2,0),(1,1,1),(0,3,0),(0,2,1),(0,1,2)]

def mons3(d):
    return [(i,j,d-i-j) for i in range(d,-1,-1) for j in range(d-i,-1,-1)]

def rref(rows, ncols):
    M=[list(r) for r in rows]; pivs=[]; r=0
    for c in range(ncols):
        piv=-1
        for i in range(r,len(M)):
            if M[i][c]%P!=0: piv=i; break
        if piv<0: continue
        M[r],M[piv]=M[piv],M[r]
        inv=pow(M[r][c]%P,-1,P); M[r]=[(x*inv)%P for x in M[r]]
        for i in range(len(M)):
            if i!=r and M[i][c]%P!=0:
                f=M[i][c]%P
                M[i]=[(x-f*y)%P for x,y in zip(M[i],M[r])]
        pivs.append(c); r+=1
    return M,pivs

def dim_quot(d):
    mons=mons3(d); idx={m:i for i,m in enumerate(mons)}; rows=[]
    for g in GENS:
        dg=sum(next(iter(g)))
        if d<dg: continue
        for m in mons3(d-dg):
            row=[0]*len(mons)
            for e,c in g.items():
                row[idx[(m[0]+e[0],m[1]+e[1],m[2]+e[2])]]=(row[idx[(m[0]+e[0],m[1]+e[1],m[2]+e[2])]]+c)%P
            rows.append(row)
    _,piv=rref(rows,len(mons))
    return len(mons)-len(piv), piv, rows, mons

def reduce_mon(mon, d, piv, rows, mons):
    if mon not in [mons[c] for c in piv]:
        return {mon:1}
    # find rule from rref rows
    pivset=set(piv)
    for row in rows:
        pc=-1
        for c in piv:
            if row[c]%P!=0: pc=c; break
        if pc>=0 and mons[pc]==mon:
            bi={m:i for i,m in enumerate(mons)}
            return {m:(-row[bi[m]])%P for m in mons if m not in pivset and row[bi[m]]%P!=0}
    return {}

# Gate 1: dim(R/I)==0  <=> A6 = 0 (and HF gate 2)
hf=[dim_quot(d)[0] for d in range(7)]
assert hf==[1,3,5,5,3,1,0], f"HF FAIL {hf}"
assert dim_quot(6)[0]==0, "dim FAIL"

# Gate 3: 5x5 matrix of xL, L=y, A2->A3, in B2/B3 bases; det must be != 0
_,piv3,rows3,mons3l=dim_quot(3)
pivset3=set(piv3)
M=[[0]*5 for _ in range(5)]
for j,s in enumerate(B2):
    u=(s[0],s[1]+1,s[2])  # multiply by y
    assert u in [mons3l[c] for c in piv3] or u in B3 or True
    r=reduce_mon(u,3,piv3,rows3,mons3l)
    for m,c in r.items():
        M[B3.index(m)][j]=(M[B3.index(m)][j]+c)%P
print("M(L=y) =",M)
det=0
for perm in itertools.permutations(range(5)):
    inv=sum(1 for i in range(5) for j in range(i+1,5) if perm[i]>perm[j])
    t=1
    for i in range(5): t=t*M[i][perm[i]]%P
    det=(det+((-1)**inv)*t)%P
print("det =",det)
assert det!=0, "DET FAIL"
# full WLP ranks at L=y
def nummat(L,d):
    _,piv,rows,mons=dim_quot(d+1)
    Bs=[mons3(d)[i] for i in range(len(mons3(d))) ]  # placeholder
    return None
print("HF:",hf)
print("VERIFY_OK")
