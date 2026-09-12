"""Consolidated verification for Triple Milnor-Redei vanishing over Q(zeta_8).
Requires cypari (PARI 2.15). Run: python3 output/artifacts/verify_all.py"""
import sys
sys.path.insert(0, '/var/lib/scoperesearch/.local/lib/python3.12/site-packages')
from cypari import pari

K = "nfinit(t^4+1)"
print("== class number of Q(zeta8):", pari("bnfinit(t^4+1).no"))
# 1. Pairwise vanishing: Hilbert grids identically 1 for (pi2,pi3a,pi17a)
pari("K=nfinit(t^4+1)")
triples = {"pi2": "1+t", "pi3a": "-1-t^2-t^3", "pi17a": "2-t^3"}
places = ["idealprimedec(K,2)[1]", "idealprimedec(K,3)[1]", "idealprimedec(K,3)[2]",
          "idealprimedec(K,5)[1]", "idealprimedec(K,5)[2]", "idealprimedec(K,17)[1]",
          "idealprimedec(K,17)[2]", "idealprimedec(K,17)[3]", "idealprimedec(K,17)[4]"]
import itertools
for an, bn in itertools.combinations(triples, 2):
    row = [str(pari("nfhilbert(K,Mod(%s,t^4+1),Mod(%s,t^4+1),%s)" % (triples[an], triples[bn], P))) for P in places]
    print("hilbert(%s,%s) =" % (an, bn), row, "VANISH" if row == ['1'] * 9 else "NONZERO")
# 2. Redei norm solution: a=-(1+t+t^2), b=-(1+t-t^3), N/pi3a = square
print("N/pi3a =", pari("K=nfinit(t^4+1); a=Mod(-1-t-t^2,t^4+1); b=Mod(-1-t+t^3,t^4+1); N=a^2-Mod(1+t,t^4+1)*b^2; N/Mod(-1-t^2-t^3,t^4+1)"))
print("is square (2 factors):", pari("K=nfinit(t^4+1); matsize(nffactor(K,x^2-Mod(-2*t^3-3*t^2-2*t,t^4+1)))[1]"))
print("sqrt check z^2:", pari("K=nfinit(t^4+1); Mod(t^3+t^2-1,t^4+1)^2"))
# 3. alpha non-square in K1 => [M:K1]=2
print("alpha nonsquare (1 factor):", pari("K1=nfinit(y^8-4*y^6+6*y^4-4*y^2+2); matsize(nffactor(K1,x^2-(y^7-3*y^5-y^4+2*y^3+y^2-y-1)))[1]"))
# 4. Q splits completely in M: both K1-primes above Q17a split in M/K1
pari("K1=bnfinit(y^8-4*y^6+6*y^4-4*y^2+2)")
pari("M=rnfinit(K1,x^2-(y^7-3*y^5-y^4+2*y^3+y^2-y-1))")
print("K1 primes above Q17a split in M as:",
      pari("P17=idealprimedec(K1,17); [#rnfidealprimedec(M,P17[2]),#rnfidealprimedec(M,P17[3])]"),
      "ef:",
      pari("P17=idealprimedec(K1,17); [vector(#rnfidealprimedec(M,P17[2]),i,rnfidealprimedec(M,P17[2])[i][3..4]),vector(#rnfidealprimedec(M,P17[3]),i,rnfidealprimedec(M,P17[3])[i][3..4])]"))
# 5. Second defining system agrees
print("second system splits as:",
      pari("M2=rnfinit(K1,x^2-((-(y^4-y^2+1)+(y^2-1)^3)+(-(y^2)+(y^2-1)^2+(y^2-1)^3)*y)); P17=idealprimedec(K1,17); [#rnfidealprimedec(M2,P17[2]),#rnfidealprimedec(M2,P17[3])]"))
print("ALL CHECKS DONE")
