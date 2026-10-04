from fractions import Fraction as F

# Primitive parameters from the article's autonomous parametrization.
NA = NH = NF = NC = F(1)
b = F(4)
pi_VH = F(1)
pi_HV = F(1, 2)
k = F(1, 2)
p = F(1, 2)
muV = F(1)
gammaA = gammaH = F(1, 4)
muA = F(3, 4)
muH = F(11, 4)

denom = k*NA + (1-p)*NH
a = k*NA/denom
h = (1-p)*NH/denom
assert a == h == F(1, 2)

beta_FA = b*pi_VH*a
beta_FH = b*pi_VH*h
beta_CH = b*pi_VH
beta_AF = b*pi_HV*a
beta_HF = b*pi_HV*h
beta_HC = b*pi_HV
assert (beta_FA,beta_FH,beta_CH,beta_AF,beta_HF,beta_HC) == (F(2),F(2),F(4),F(1),F(1),F(2))

dA = muA + gammaA
dH = muH + gammaH
assert dA == 1 and dH == 3

RFA = (beta_AF/muV)*(beta_FA/dA)*(NF/NA)
RFH = (beta_HF/muV)*(beta_FH/dH)*(NF/NH)
RCH = (beta_CH/dH)*(beta_HC/muV)*(NC/NH)
assert (RFA, RFH, RCH) == (F(2), F(2,3), F(8,3))
S = RFA + RFH + RCH
P = RFA * RCH
assert S == P == F(16,3)
D = S*S - 4*P
rootD = F(8,3)
assert D == rootD*rootD == F(64,9)
q = (S + rootD)/2
assert q == 4
assert S - P - 1 == -1
assert not (S > P + 1)

IA = IF = IH = IC = F(1,2)
r1 = beta_FA*IF*(NA-IA)/NA - dA*IA
r2 = (beta_AF*IA/NA + beta_HF*IH/NH)*(NF-IF) - muV*IF
r3 = (beta_FH*IF + beta_CH*IC)*(NH-IH)/NH - dH*IH
r4 = beta_HC*IH/NH*(NC-IC) - muV*IC
assert (r1,r2,r3,r4) == (0,0,0,0)
print("VERIFY_OK")
