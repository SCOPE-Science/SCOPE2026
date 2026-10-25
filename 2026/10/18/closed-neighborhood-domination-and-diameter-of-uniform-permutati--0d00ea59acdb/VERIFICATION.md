---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

On the encoded caterpillar, all leaf-support spine vertices may be simultaneously selected in a minimum closed-neighborhood dominating set; k consecutive unsupported internal spine vertices between forced supports cost floor(k/3). Verified directly by constructing permutation inversion trees and minimizing closed-neighborhood coverage for all fair-bit words with 3<=n<=9. Geometric run cycles have E(M,R,C)=(4,8/7,2), centered covariance E(U^2)=72/343, E(UV)=12/49, E(V^2)=1. Independent exact rational arithmetic yields slopes (18/343,3/49,1/4), determinant 45/4802. Regenerative CLT with exponential tails and bounded boundary moments justifies the joint distribution and covariance limits; finite checks alone do not.

## originality

PASS

Best-of-knowledge PASS for the standard closed-neighborhood domination number jointly with diameter, with new explicit constants. The 2014/2016 Acan-Hitczenko paper unfortunately calls its edge-incidence vertex-cover statistic domination; direct full-text inspection of §3.4 proves its recurrence floor(k/2) and linear mean n/3, not the present floor(k/3), 2n/7 closed-neighborhood statistic.

## value

PASS

A basic random graph model has a natural and previously conflated parameter: ordinary vertex domination versus edge-incidence coverage. The exact finite-word formula and explicit joint Gaussian covariance with diameter quantify a nontrivial dependence in a canonical model, so this is more than a simple renaming.

The dated certificate retains the supplied scientific assessment, sources and limitations.
