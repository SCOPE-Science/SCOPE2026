---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

Counting ones among the 2k-1 other vertices yields exact three-case global map: if r=a+b<k then F(X,Y)=(0,1), if r=k then F(X,Y)=(complement X,Y), if r>k then F(X,Y)=(1,0). The four special states form one 4-cycle; only configurations a=b=k/2 (even k) form primitive 2-cycles; no other period or fixed point. Counts T0=4+B_k, T1=4^k-C(2k,k)-2, T2=C(2k,k)-2-B_k follow by separating r=k and four-cycle states; bound T<=2 sharp k>=3. Independent direct per-vertex graph updates verified all 5460 states for k<=6. Product Bernoulli measure gives B_k[p(1-p)]^k; Stirling yields fixed-s critical window (2/pi k)e^(-4s^2). Quantifiers and k=1,2 handled analytically.

## originality

PASS

Best-of-knowledge scoped originality after explicit implication comparisons, with real residual priority risk: Cannings (2009) is same-model, full text unavailable and may contain closed labelled count formulas or equivalent central-layer calculation. Model requires equal k/k split, no self-neighbors, synchronous updates.

## value

PASS

Complete microscopic attractor basins, two-step entrance census and parity-selective Gaussian critical window for a canonical balanced majority/minority network. Distinct from earlier mere qualitative period restrictions; yields precise prevalence of coexistence rhythms.

The dated certificate retains the supplied scientific assessment, sources and limitations.
