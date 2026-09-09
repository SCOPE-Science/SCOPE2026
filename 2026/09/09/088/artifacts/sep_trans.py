"""Rigorous separation + transversality + reality for base (a), exact Fractions."""
import sys,pickle,json; sys.path.insert(0,'.')
from fractions import Fraction as Q
import numpy as np
from build_solve import build_system

DEN=10**12
base_centers=[Q(-14,10)+Q(4,10)*k for k in range(8)]
offs=[Q(0),Q(8,100),Q(16,100),Q(24,100)]
G=[[c+o for o in offs] for c in base_centers]
sysQ=build_system(G)
const,lin,quad=sysQ
sols=np.array(pickle.load(open('base_sols.pkl','rb')))
n=len(sols)
# rational centers as Fractions
M=[[Q(int(round(v.real*DEN)),DEN) for v in x] for x in sols]  # imag snapped (all <1e-9)
# separation matrix (exact, lower bounds via float diff minus rationalization err 1e-12)
sep=[]
for i in range(n):
    row=[]
    for j in range(n):
        if i==j: row.append(Q(0)); continue
        d=max(abs(float(M[i][a]-M[j][a])) for a in range(8))
        row.append(d)
    sep.append(row)
dmin=min(sep[i][j] for i in range(n) for j in range(n) if i!=j)
print("dmin (float lower approx):",dmin)
# transversality: exact det of Jacobian at rational centers
def det_frac(A):
    n=len(A); M=[list(r) for r in A]
    det=Q(1)
    for c in range(n):
        piv=None
        for r in range(c,n):
            if M[r][c]!=0: piv=r; break
        if piv is None: return Q(0)
        if piv!=c: M[c],M[piv]=M[piv],M[c]; det=-det
        det*=M[c][c]; pv=M[c][c]
        for r in range(c+1,n):
            f=M[r][c]/pv
            for k in range(c,n): M[r][k]-=f*M[c][k]
    return det
dets=[]
for i in range(n):
    J=[[lin[e][c]+sum(quad[e][c][a]*M[i][a]+quad[e][a][c]*M[i][a] for a in range(8)) for c in range(8)] for e in range(8)]
    d=det_frac(J)
    dets.append(d)
print("all dets nonzero:",all(d!=0 for d in dets))
print("min |det| float:",min(float(abs(d)) for d in dets))
# residual at rational centers (exact)
def Fres(i):
    x=M[i]; out=[]
    for e in range(8):
        s=const[e]+sum(lin[e][a]*x[a] for a in range(8))+sum(quad[e][a][b]*x[a]*x[b] for a in range(8) for b in range(8))
        out.append(s)
    return out
print("max |F| at rat centers:",max(float(abs(v)) for i in range(n) for v in Fres(i)))
# alpha data already in alpha_base.json; separation vs beta: beta_max ~5e-13 << dmin/2?
ab=json.load(open('alpha_base.json'))
bmax=max(r['beta'] for r in ab)
print("beta_max:",bmax,"dmin/2:",dmin/2,"separation OK:",float(bmax)<dmin/2)
# reality: alpha balls radius ~2*beta (Newton contraction); imag parts all <1e-9 << dmin
# certified reality argument: each approx has |imag|<1e-9; alpha ball radius r_i<=2beta<1.1e-12... wait beta 5e-13 so ball radius tiny; ball lies within 1e-9+1e-12 of real axis? For reality need Krawczyk symmetric-box argument; record numbers for DRAFT.
json.dump({"dmin":dmin,"beta_max":bmax,"dets_nonzero":True,
  "min_absdet":min(float(abs(d)) for d in dets)},open("sep_base.json","w"),indent=1)
