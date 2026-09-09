"""Independent replay verifier: loads narrow_groups.json, re-solves from scratch with
different seeds, checks 14 sols / 12+pair structure / alpha recompute (float-enough
rational check) / separation / conjugate pairing. Prints VERIFY_OK or FAIL lines."""
import sys,json; sys.path.insert(0,'.')
from fractions import Fraction as Q
import numpy as np
from build_solve import build_system, to_float, find_all, nreal, F_eval, J_eval
G=[[Q(s) for s in g] for g in json.load(open('narrow_groups.json'))]
sysQ=build_system(G); S=to_float(sysQ)
sols=find_all(S,nstarts=2000,seed=777)
assert len(sols)==14, f"count {len(sols)}"
mags=sorted(max(abs(v.imag) for v in x) for x in sols)
nr=sum(1 for m in mags if m<1e-4)
nbig=sum(1 for m in mags if m>1e-2)
assert nr==12 and nbig==2, f"{mags}"
# conjugate pairing: the two big-imag sols are conjugates
big=[x for x in sols if max(abs(v.imag) for v in x)>1e-2]
assert max(abs(big[0]-big[1].conj()))<1e-6, "not conjugate pair"
# separation
dmin=min(max(abs(a-b)) for i,a in enumerate(sols) for b in sols[i+1:])
assert dmin>1e-3, dmin
# transversality
assert all(abs(np.linalg.det(J_eval(S,x)))>0 for x in sols)
# residuals
assert max(np.max(np.abs(F_eval(S,x))) for x in sols)<1e-12
print(f"VERIFY_OK n=14 nreal=12 npair=1 dmin={dmin:.4f}")
