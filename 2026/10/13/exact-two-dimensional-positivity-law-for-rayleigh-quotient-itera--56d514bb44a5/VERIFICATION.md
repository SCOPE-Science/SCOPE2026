---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For normalized eigenbasis x∼v1+t v2, exact Rayleigh quotient μ=(λ1+λ2t²)/(1+t²) and inverse iteration give t+ = −t³. Starting cone is −tanθ<t<cotθ, mapped-positive condition is −cuberoot(cotθ)<t<cuberoot(tanθ), giving the intersection. Universal positive-ray invariance implies tanθ=cotθ=1, equivalent to a=d. Independent rational elimination for A=[[1,−1],[−1,2]], x=(1,4) gives μ=25/17 and y=(−1309/361,255/361), and satisfies basin condition. This covers eigenvector termination, sign orientation, and equal-diagonal cubic convergence.

## originality

PASS

Parlett classical RQI gives t→−t³ and Jia–Lin–Liu motivate positive eigensolver variants. Neither inspected work states the sharp safe-start intersection or iff equal-diagonal invariant positive cone for all 2×2 SPD Stieltjes matrices, including basin counterexample. Independent Resultary searches found related CG/MINRES/SOR positivity results on different methods, not an implication for ordinary RQI.

## value

PASS

The complete 2×2 exact cone-safety region and equal-diagonal iff criterion give a sharp natural boundary for positivity loss in a classical eigenvalue algorithm, directly motivating positive-preserving alternatives. More substantive than just a negative numerical witness.

The dated certificate retains the supplied scientific assessment, sources and limitations.
