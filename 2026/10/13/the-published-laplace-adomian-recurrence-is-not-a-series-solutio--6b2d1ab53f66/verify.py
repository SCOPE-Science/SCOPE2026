#!/usr/bin/env python3
import sympy as sp

q,beta,betap,lam,phis,rhoh = sp.symbols("q beta betap lam phis rhoh")
delta,sigma,a,rhoa,lams,tauh = sp.symbols("delta sigma a rhoa lams tauh")
K1,K2,K3,K4,K5,K6,K7 = sp.symbols("K1 K2 K3 K4 K5 K6 K7")

AS = delta-q*beta*K1*K3-q*betap*K1*K4-lam*K1
AE = q*beta*K1*K3+q*betap*K1*K4-(sigma+lam)*K2
AIs = (1-a)*sigma*K2+rhoa*K4-(lams+lam+phis)*K3
AR = rhoh*K6+tauh*K5-lam*K7

AIs_59 = (1-a)*sigma*K2+rhoa*K4-(lams+lam)*K3-phis*K4
AR_59 = rhoh*K5+tauh*K5-lam*K7

AS_510 = delta-q*beta*K1*K4-q*betap*K1*K3-lam*K2
AE_510 = q*beta*K1*K4+q*betap*K1*K3-(sigma+lam)*K2
AIs_510 = (1-a)*sigma*K2+rhoa*K4-(lams+lam)*K3-phis*K4

assert sp.simplify((AIs_59-AIs)-phis*(K3-K4)) == 0
assert sp.simplify((AR_59-AR)-rhoh*(K5-K6)) == 0
assert sp.simplify((AS_510-AS)-(q*(beta-betap)*K1*(K3-K4)+lam*(K1-K2))) == 0
assert sp.simplify((AE_510-AE)+q*(beta-betap)*K1*(K3-K4)) == 0
assert sp.simplify((AIs_510-AIs)-phis*(K3-K4)) == 0

infection_S = -q*beta*K1*K3-q*betap*K1*K4
infection_E = q*beta*K1*K3+q*betap*K1*K4
assert sp.simplify(infection_S+infection_E) == 0

w = {
    q:sp.Rational(1,2), K1:1, K2:2, K3:3, K4:4, K5:5, K6:6, K7:7,
    beta:2, betap:1, lam:1, phis:1, rhoh:1,
}
dS = sp.simplify((AS_510-AS).subs(w))
dIs = sp.simplify((AIs_59-AIs).subs(w))
dR = sp.simplify((AR_59-AR).subs(w))
assert dS == -sp.Rational(3,2)
assert dIs == -1
assert dR == -1

print("VERIFY_OK")
print("S_5_10_minus_model", dS)
print("Is_5_9_minus_model", dIs)
print("R_5_9_minus_model", dR)
