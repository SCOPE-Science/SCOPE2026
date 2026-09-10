"""Independent replay: recompute Tr4/Tr6/N6 from filed matrix; check enclosure + verdict."""
import json, csv, math
import numpy as np
A=list(csv.reader(open(__import__("os").path.join(__import__("os").path.dirname(__file__),"A_eps_star.csv"))))
A=[[int(x) for x in row] for row in A]
n=len(A)
assert n==60 and all(len(r)==60 for r in A)
assert all(A[i][j]==A[j][i] for i in range(n) for j in range(n))
assert set(x for r in A for x in r)<={-1,0,1}
deg=[sum(abs(x) for x in r) for r in A]; assert set(deg)=={4}, set(deg)
def mm(X,Y):
    # exact integer product; entries of powers beyond A are general ints
    Z=[[0]*n for _ in range(n)]
    for i in range(n):
        Zi=Z[i]; Xi=X[i]
        for k in range(n):
            x=Xi[k]
            if x:
                Yk=Y[k]
                for j in range(n): Zi[j]+=x*Yk[j]
    return Z
def tr(X): return sum(X[i][i] for i in range(n))
A2=mm(A,A); T2=tr(A2); A4=mm(A2,A2); T4=tr(A4); A6=mm(A4,A2); T6=tr(A6)
print("Tr2,Tr4,Tr6 =",T2,T4,T6)
assert (T2,T4,T6)==(240,1920,18000), "moment mismatch"
nbrs=[[j for j in range(n) if A[i][j]!=0] for i in range(n)]
def NB(k):
    tot=0
    for v0 in range(n):
        st=[(v0,-1,1,0)]
        while st:
            v,p,s,l=st.pop()
            if l==k:
                if v==v0: tot+=s
                continue
            for w in nbrs[v]:
                if w==p: continue
                st.append((w,v,s*A[v][w],l+1))
    return tot
N6=NB(6); print("N6 =",N6); assert N6==240
v=json.load(open(__import__("os").path.join(__import__("os").path.dirname(__file__),"rayleigh_vector.json")))
Av=[sum(A[i][j]*v[j] for j in range(n)) for i in range(n)]
num=sum(a*b for a,b in zip(Av,v)); den=sum(x*x for x in v)
A2v=[sum(A[i][j]*Av[j] for j in range(n)) for i in range(n)]
num2=sum(a*b for a,b in zip(A2v,v))
print(f"Rayleigh: vTAv={num} vTv={den} q={num/den:.9f}; vTA2v={num2} q2sqrt={math.sqrt(num2/den):.9f}")
lo=num/den
assert lo>=3.40, "lower bound too weak"
Af=np.array(A,float); w=np.linalg.eigvalsh(Af); rho=float(max(abs(w.max()),abs(w.min())))
print(f"float rho={rho:.9f} max={w.max():.9f} min={w.min():.9f}")
R=2*math.sqrt(3)
# certified-style enclosure: [lo_exact, U] with U=3.44 validated by float LDL + margin note
U=3.44
for sgn,name in [(1,"U-A"),(-1,"U+A")]:
    M=U*np.eye(n)-sgn*Af
    np.linalg.cholesky(M); print(name,"Cholesky OK")
assert U-lo<=0.05, f"width {U-lo} too big"
assert U<=R, "not Ramanujan?!"
print(f"ENCLOSURE [{lo:.6f},{U}] width={U-lo:.6f} R={R:.6f} -> two-sided Ramanujan. VERIFY_OK")

# exact upper-bound cross-check note: run output/artifacts/certify_upper.py
# (Bareiss integer LDL, CERTIFY_UPPER_OK) for the proof-grade rho<3.44 bound.
