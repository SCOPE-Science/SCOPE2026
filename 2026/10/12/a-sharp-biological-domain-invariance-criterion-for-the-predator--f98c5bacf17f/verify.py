#!/usr/bin/env python3
import sympy as sp
from fractions import Fraction as F

delta,r2,e,K,q2,E = sp.symbols("delta r2 e K q2 E", positive=True)
Ptop=1/delta
Pdot=sp.simplify(Ptop*(r2*(1-e*Ptop/K)-q2*E*Ptop))
target=(delta*r2-r2*e/K-q2*E)/delta**2
assert sp.simplify(Pdot-target)==0

# Exact counterexample.
dw=F(1,5)
r2w=F(1)
ew=F(1,10)
Kw=F(2)
q2w=F(1,10)
Ew=F(1,10)
threshold_w=ew/Kw+q2w*Ew/r2w
assert threshold_w==F(3,50)
assert dw>threshold_w
Pw=1/dw
Pdot_w=Pw*(r2w*(1-ew*Pw/Kw)-q2w*Ew*Pw)
assert Pw==5
assert Pdot_w==F(7,2)

# Source Dataset (24).
ds=F(1,20)
r2s=F(1)
es=F(1,5)
Ks=F(2)
q2s=F(1,5)
Es=F(3,4)
threshold_s=es/Ks+q2s*Es/r2s
assert threshold_s==F(1,4)
assert ds<threshold_s
Ps=1/ds
Pdot_s=Ps*(r2s*(1-es*Ps/Ks)-q2s*Es*Ps)
assert Pdot_s==F(-80)

# Positive singular curves outside the biological strip for the witness.
Psing=F(10)
c=F(2)
N_pred=Kw/(dw*Psing-1)
N_prey=(c+ew*Psing)/(dw*Psing-1)
assert N_pred==2
assert N_prey==3
assert Kw+N_pred*(1-dw*Psing)==0
assert c+N_prey*(1-dw*Psing)+ew*Psing==0

print("VERIFY_OK")
print("boundary_formula", sp.factor(Pdot))
print("witness_threshold", threshold_w)
print("witness_Ptop", Pw)
print("witness_Pdot_top", Pdot_w)
print("source_threshold", threshold_s)
print("source_Pdot_top", Pdot_s)
print("singular_predator_point", (N_pred,Psing))
print("singular_prey_point", (N_prey,Psing))
