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

The piecewise map F has plateau H on the left, affine branch I-2u on J, plateau L on right; the affine branch takes the interior of K bijectively onto itself with inverse slope 1/2. Consequently F_*lambda_K=(1/2)lambda_K+aδ_H+bδ_L, a+b=1/2 and the two atoms swap. Continuous survivor mass after n steps is 2^-n, giving geometric first-cycle-hitting time and mean 2. Solving w=(a/2+b)+w/4 yields w=1/3+2b/3, with explicit a,b piecewise, and after 2n iterations the distribution is 4^-n lambda+(1-4^-n)(wδ_H+(1-w)δ_L), sharp TV 4^-n due to mutually singular continuous and atomic parts. The centered q=I/3 slope -2 causes paired phases h(q-t)+h(q+t)=1 by finite-doubling until plateaus. Independent exact rational checks cover representative parameter ratios including I=2B, I=3B. Universal analytic proof, not finite extrapolation.

## originality

PASS

Earlier analysis explicitly establishes the same map, fixed point and attracting two-cycle, so these are prior facts. Best-of-knowledge original content is exact initial-phase probabilities, every-time uniform-plus-atomic transfer, sharp total variation and mirror balance.

## value

PASS

For a piecewise-affine model with a known attracting two-cycle, the probability of selecting each parity phase is a natural basin statistic absent from the attractor-existence description. The exact parameter-dependent crossover, simple 4^-n total-variation convergence, geometric first-hit law, and unexpected half-half balance on centered neighborhoods give a complete, usable quantitative phase-selection picture, not a routine restatement of a cycle.

The dated certificate retains the supplied scientific assessment, sources and limitations.
