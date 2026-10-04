from fractions import Fraction as F
from math import exp

T=F(2); c=F(2); r=F(1); q=F(4); G=F(1); ell=F(1); E=F(2)
printed_barT=(q-c*r)/q
true_barT=T*(q-c*r)/q
barT=F(3,4)
digamma=r*T-(q/c)*(T-barT)
correct_rstar=(T-barT)*q/(c*T)
printed_rstar=(T-barT)*q/T
cycle_bound=barT*F(1)+(T-barT)*F(-1)
assert printed_barT == F(1,2)
assert true_barT == F(1)
assert digamma == F(-1,2)
assert correct_rstar == F(5,4)
assert printed_rstar == F(5,2)
assert E >= G*ell/c
assert q >= c*r
assert E > q*ell*G/(r*c*c)
assert cycle_bound == F(-1,2)
assert exp(float(cycle_bound)) < 1
print('VERIFY_OK')
