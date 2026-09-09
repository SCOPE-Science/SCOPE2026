"""Run full exact certification on disjoint base (a) and best 12-real candidate (b).

(b) candidate choice: lam-grid showed 12-real at lam=0.55 with 10 overlaps — not minimal.
Better: use fresh random search restricted to SINGLE-pair overlap with reality!=14.
First: certify (a) fully now (alpha+Krawczyk+separation+reality); hunt (b) minimal next.
"""
import sys, json; sys.path.insert(0,'.')
from fractions import Fraction as Q
import numpy as np, pickle
from build_solve import build_system, to_float, F_eval, find_all
from certify import alpha_cert, krawczyk, mat_inv, ALPHA_TH

base_centers=[Q(-14,10)+Q(4,10)*k for k in range(8)]
offs=[Q(0),Q(8,100),Q(16,100),Q(24,100)]
G=[[c+o for o in offs] for c in base_centers]
sysQ=build_system(G)
S=to_float(sysQ)
sols=np.array(pickle.load(open('base_sols.pkl','rb')))
print("n:",len(sols))

# rationalize solutions to Fractions (denominator 10^12, snap tiny imag to 0 if <1e-9)
DEN=10**12
M=[]
for x in sols:
    m=[]
    for v in x:
        if abs(v.imag)<1e-9: v=complex(v.real,0.0)
        m.append(complex(v))
    M.append(m)

from fractions import Fraction as Q
def toQ(z):
    return Q(int(round(z.real*DEN)),DEN)+Q(int(round(z.imag*DEN)),DEN)*1j if False else (Q(int(round(z.real*DEN)),DEN), Q(int(round(z.imag*DEN)),DEN))

# alpha cert needs real or complex? Do real split: represent complex system as 16 real eqs? Simpler:
# certify with complex arithmetic in Fractions via pairs. Implement complex alpha with complex Fractions:
class CQ:
    __slots__=("r","i")
    def __init__(s,r,i): s.r=r; s.i=i
    def __add__(s,o): return CQ(s.r+o.r,s.i+o.i)
    def __sub__(s,o): return CQ(s.r-o.r,s.i-o.i)
    def __mul__(s,o): return CQ(s.r*o.r-s.i*o.i, s.r*o.i+s.i*o.r)
    def __neg__(s): return CQ(-s.r,-s.i)
    def __truediv__(s,o):
        d=o.r*o.r+o.i*o.i; return CQ((s.r*o.r+s.i*o.i)/d,(s.i*o.r-s.r*o.i)/d)
    def __abs__(s): return float(s.r*s.r+s.i*s.i)**0.5
    def conj(s): return CQ(s.r,-s.i)

def csolve(A,b):
    n=len(A); M=[[A[i][j] for j in range(n)]+[b[i]] for i in range(n)]
    for c in range(n):
        piv=None
        for r in range(c,n):
            if M[r][c].r!=0 or M[r][c].i!=0: piv=r; break
        if piv is None: raise ValueError("singular")
        M[c],M[piv]=M[piv],M[c]; pv=M[c][c]
        for r in range(n):
            if r!=c and (M[r][c].r!=0 or M[r][c].i!=0):
                f=M[r][c]/pv
                for k in range(c,n+1): M[r][k]=M[r][k]-f*M[c][k]
    return [M[i][n]/M[i][i] for i in range(n)]

def cinv(A):
    n=len(A)
    I=[[CQ(Q(1),Q(0)) if i==j else CQ(Q(0),Q(0)) for j in range(n)] for i in range(n)]
    M=[list(A[i])+list(I[i]) for i in range(n)]
    for c in range(n):
        piv=None
        for r in range(c,n):
            if M[r][c].r!=0 or M[r][c].i!=0: piv=r; break
        if piv is None: raise ValueError("singular")
        M[c],M[piv]=M[piv],M[c]; pv=M[c][c]
        for k in range(2*n): M[c][k]=M[c][k]/pv
        for r in range(n):
            if r!=c and (M[r][c].r!=0 or M[r][c].i!=0):
                f=M[r][c]
                for k in range(2*n): M[r][k]=M[r][k]-f*M[c][k]
    return [row[n:] for row in M]

def F_cq(sys,m):
    const,lin,quad=sys; n=len(const); out=[]
    for e in range(n):
        s=CQ(const[e],Q(0))
        for a in range(n):
            s=s+CQ(lin[e][a],Q(0))*m[a]
            for b in range(n):
                s=s+CQ(quad[e][a][b],Q(0))*m[a]*m[b]
        out.append(s)
    return out
def J_cq(sys,m):
    const,lin,quad=sys; n=len(const); J=[[None]*n for _ in range(n)]
    for e in range(n):
        for c_ in range(n):
            s=CQ(lin[e][c_],Q(0))
            for a in range(n):
                s=s+CQ(quad[e][c_][a]+quad[e][a][c_],Q(0))*m[a]
            J[e][c_]=s
    return J

def cnorm_v(v): return max(abs(z) for z in v)
def cnorm_m(A): return max(sum(abs(z) for z in row) for row in A)

const,lin,quad=sysQ
Sbound=max(sum(abs(quad[e][a][b]+quad[e][b][a])/2 for a in range(8) for b in range(8)) for e in range(8))
print("Sbound:",float(Sbound),Sbound)

results=[]
for idx,x in enumerate(sols):
    m=[CQ(Q(int(round(v.real*DEN)),DEN),Q(int(round(v.imag*DEN)),DEN)) for v in x]
    F=F_cq(sysQ,m); J=J_cq(sysQ,m)
    Ji=cinv(J)
    dx=csolve(J,[CQ(-f.r,-f.i) for f in F])
    beta=cnorm_v(dx); g=cnorm_m(Ji)*float(Sbound); alpha=beta*g
    # separation vs others
    print(f"sol{idx}: beta={beta:.3e} gamma<={g:.3e} alpha<={alpha:.3e} cert={alpha<ALPHA_TH} imagmax={max(abs(v.imag) for v in x):.1e}")
    results.append({"beta":beta,"gamma":g,"alpha":alpha})
print("all alpha cert:",all(r["alpha"]<ALPHA_TH for r in results))
json.dump([{"beta":r["beta"],"gamma":r["gamma"],"alpha":r["alpha"]} for r in results],open("alpha_base.json","w"),indent=1)
