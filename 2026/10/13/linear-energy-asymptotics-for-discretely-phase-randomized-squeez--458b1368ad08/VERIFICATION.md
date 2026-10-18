---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For even j=2k, the exact squeezed photon law is (1+nbar)^(-1/2) binom(2k,k)4^(-k) [nbar/(1+nbar)]^k. With nbar=cM and j=xM>0, central-binomial Stirling gives M p_j→g_c(x)=sqrt[2/(pi c x)]e^(−x/(2c)). In 4 sum_even j<M of harmonic p_j,p_(j+M), even mesh 2/M yields 2 integral_0^1 g(x)g(x+1)/(g(x)+g(x+1)) dx. Near j=0, use harmonic≤p_(j+M) and uniform density x in [1,1+epsilon], then endpoint is O(epsilon). Integrand is positive and finite, so source squeezed bound proportional to B_M^(-1) stays constant. For classical source lower bound proportional to (1−c−c/M)e^(cM) M!/(cM)^M, Stirling gives sqrt(2pi M)(1−c) exp(M[c−1−ln c]); c−1−ln c>0. Numerical independent loggamma sums converge to integral for c=.25 and .6. Source finite-sample premise was taken from the quoted source formulas and could NOT be independently checked against its full primary paper; this is a material correctness/priority verification limitation on the source-level implication, not a fabricated independent validation of that premise.

## originality

PASS

Best-of-knowledge PASS as a *conditional fixed-c asymptotic deduction* in the explicit source model: Conlon et al develop the general bounds and an nbar=M/log M example; the new analysis evaluates a genuinely distinct linear-energy regime 0<c<1 and derives a positive visibility limit and classical large-deviation exponent. The originating paper full text was inaccessible; equivalence in an uninspected appendix is a live risk, explicitly not dismissed.

## value

PASS

The concrete scaling crossover (constant squeezed samples vs exponential lower bound for the specified classical family) at every subcritical linear coefficient substantially refines the source energy/sample-complexity phase portrait, while explicitly excluding c=1 and all protocols outside its model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
