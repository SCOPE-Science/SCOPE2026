#!/usr/bin/env python3
from fractions import Fraction as F
m=F(1,2); lam=F(1); lam_e=F(2); p=F(1); muV=F(1)
H1=H2=L1=F(1)
live_generous=(1-m)*F(2)+m*F(2)
assert live_generous==2
actual_live=(1-m)*F(1)+m*F(1)
actual_bracket=actual_live+lam_e*L1
assert actual_bracket==3
for M in (F(0),F(1),F(3,2),F(2)):
    assert p*actual_bracket-muV*M>=1
c=max(F(1),lam)
Bmax=c*((1-m)*H1+m*H2)+lam_e*L1
Vcap=p*Bmax/muV
assert Bmax==3 and Vcap==3
assert p*Bmax-muV*Vcap==0
print("VERIFY_OK")
print("source_live_generous", live_generous)
print("actual_bracket", actual_bracket)
print("corrected_cap", Vcap)
