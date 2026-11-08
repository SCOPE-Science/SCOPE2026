---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

PASS: Stationarity, 0<u,v<1, 0<d<=1 and m=pi*d give E(Y_t)=m, adjacent E(Y_iY_{i+1})=m²+m(d-m)r, lag-two E(Y_1Y_3)=m²+m(d-m)r², and triple T=m[m+(d-m)r]². Positivity of d(1-v) fixes the square-root sign, so z=(d-m)r. S=g2+3g3=3m²+mz(2+r), hence for r!=0 recover r, d, pi, u, v exactly; all divisions are legal as d-m>0. At r=0 observations are iid Bernoulli(pi*d), so even ordered arbitrarily long histories are nonidentifying. Two-visit data have only m and adjacent moment; nearby parameter curves retain both. Independently enumerated rational latent/observed paths in positive and negative memory, including d=1, and symbolically checked Jacobian -2 d^5 pi²(1-pi)[pi+(1-pi)r]r². Global identification concerns population counts, not sample-size guarantees.

## originality

PASS

PASS: Best-of-knowledge supported by direct statement/implication comparisons, not claimed absolute priority. Aggregating ordered histories into K discards temporal position; neither model formulation automatically proves the exact three-count inverse of two transition rates and detector sensitivity. A generic ordered-law identification theorem does not imply count-only global identification at every nonzero memory, including negative r; neither states the exact r=0 nonidentifiability fiber. The full law might imply count identifiability only with a separate injectivity proof, provided here via factorial moments. Known Markov-binomial distributions may encode the formula implicitly; check remains a priority risk.

## value

PASS

PASS: Minimum survey replication is a natural statistical design question; the result shows an unusual exact information preservation under discarding visit order, identifies alternating-memory parameters, and characterizes a sharp structural nonidentifiability boundary and its quadratic instability. It is not an elementary consequence of ordered-HMM identifiability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
