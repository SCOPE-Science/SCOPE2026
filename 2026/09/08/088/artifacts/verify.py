"""Replay verifier: A5 symmetric-normal Cayley census from committed character table.
Requires: numpy only. Exits VERIFY_OK on exact agreement, else nonzero."""
import itertools
import numpy as np
from math import sqrt
# Committed data
SIZES = {"1":1,"2A":15,"3A":20,"5A":12,"5B":12}
phi=(1+sqrt(5))/2; psi=(1-sqrt(5))/2
CH = {"t":[1,1,1,1,1],"3a":[3,-1,0,phi,psi],"3b":[3,-1,0,psi,phi],
      "4":[4,0,1,-1,-1],"5":[5,1,-1,0,0]}
# 1. character-table orthogonality
names=["1","2A","3A","5A","5B"]; rows=[CH["t"],CH["3a"],CH["3b"],CH["4"],CH["5"]]
for i in range(5):
    for j in range(5):
        s=sum(SIZES[n]*rows[i][k]*rows[j][k] for k,n in enumerate(names))
        assert abs(s-(60 if i==j else 0))<1e-9, ("orth",i,j,s)
# 2. permutation model: class sizes + inverse-closedness of each class
perms=[p for p in itertools.permutations(range(5)) if sum(1 for i in range(5) for j in range(i+1,5) if p[i]>p[j])%2==0]
assert len(perms)==60
def comp(a,b): return tuple(a[b[i]] for i in range(5))
def inv(a):
    r=[0]*5
    for i,v in enumerate(a): r[v]=i
    return tuple(r)
def conj(g,x): return comp(g,comp(x,inv(g)))
IDENT=tuple(range(5)); idx={p:i for i,p in enumerate(perms)}
seen=set(); cls=[]
for x in perms:
    if x in seen: continue
    cl={conj(g,x) for g in perms}; seen|=cl; cls.append(sorted(cl))
assert sorted(len(c) for c in cls)==[1,12,12,15,20], sorted(len(c) for c in cls)
for c in cls: assert {inv(p) for p in c}==set(c), "class not inverse-closed"
assert sum(len(c) for c in cls)==60 and IDENT in [c for c in cls if len(c)==1][0]
C15=[c for c in cls if len(c)==15][0]; C20=[c for c in cls if len(c)==20][0]
C12=[c for c in cls if len(c)==12]
g0=(1,2,3,4,0); c5A=C12[0] if g0 in C12[0] else C12[1]; c5B=C12[1] if g0 in C12[0] else C12[0]
AT={"2A":C15,"3A":C20,"5A":c5A,"5B":c5B}
# 3. all 15 nonempty symmetric normal sets: spectrum, matrix cross-check, verdict
nram=0; ntriv_ok=0; exc=[]
for r in range(1,16):
    keys=[k for b,k in zip([(r>>j)&1 for j in range(4)],["2A","3A","5A","5B"]) if b]
    S=set().union(*[set(AT[k]) for k in keys]); d=len(S)
    assert IDENT not in S and all(inv(s) in S for s in S)
    sp={}
    for cn in ["t","3a","3b","4","5"]:
        t=0.0
        if "2A" in keys: t+=15*CH[cn][1]
        if "3A" in keys: t+=20*CH[cn][2]
        if "5A" in keys: t+=12*CH[cn][3]
        if "5B" in keys: t+=12*CH[cn][4]
        sp[cn]=t/CH[cn][0]
    Am=np.zeros((60,60)); SI={idx[s] for s in S}
    for i,p in enumerate(perms):
        for s in SI: Am[i,idx[comp(perms[s],p)]]=1
    assert bool((Am==Am.T).all())
    ev=np.sort(np.linalg.eigvalsh(Am))
    ex=np.sort(np.array(sum([[round(sp[c],9)]*int(CH[c][0]**2) for c in ["t","3a","3b","4","5"]],[])))
    ag=float(np.max(np.abs(ex-ev))); assert ag<1e-9, (keys,ag)
    lam=max(abs(round(sp[c],9)) for c in ["3a","3b","4","5"]); RB=2*sqrt(d-1)
    assert lam<=RB+1e-9, ("NOT RAMANUJAN",keys,lam,RB)
    nram+=1
    tm=max(((15*abs(CH[c][1]) if "2A" in keys else 0)+(20*abs(CH[c][2]) if "3A" in keys else 0)+(12*abs(CH[c][3]) if "5A" in keys else 0)+(12*abs(CH[c][4]) if "5B" in keys else 0))/CH[c][0] for c in ["3a","3b","4","5"])
    if tm<=RB+1e-9: ntriv_ok+=1
    else: exc.append(("+".join(keys),d))
    # BFS generation (connectedness)
    sn={IDENT}; st=[IDENT]
    while st:
        x=st.pop()
        for s in S:
            y=comp(s,x)
            if y not in sn: sn.add(y); st.append(y)
    assert len(sn)==60, ("disconnected",keys)
assert nram==15 and ntriv_ok==12, (nram,ntriv_ok)
assert sorted(e[0] for e in exc)==["2A+5A","2A+5A+5B","2A+5B"], exc
print(f"VERIFY_OK: 15/15 Ramanujan, matrix agreement <1e-9, 12/15 trivial-certified, exceptions {[e[0] for e in exc]}")
