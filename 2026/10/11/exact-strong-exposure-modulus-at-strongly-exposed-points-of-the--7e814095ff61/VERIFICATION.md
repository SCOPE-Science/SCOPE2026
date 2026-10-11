---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The checked domain is the real binary tree space \(X_T\) of arXiv:2603.12947v1 and the canonical exposing functional attached in Proposition 3.2 to a strongly exposed point.

The upper bound was verified from three exact facts: a finite maximal antichain meets every branch once; the source norm bounds absolute mass on each branch by \(1\); and the slice deficit equals the average of the coordinate deficits on the antichain. For a branch meeting \(\alpha\) at \(s\), the distance contribution is at most twice the deficit at \(s\).

Sharpness was verified by moving an amount \(\varepsilon\) of mass from one antichain node to a strict descendant. The resulting vector remains on the unit sphere, loses exactly \(\varepsilon/N\) in the exposing functional, and moves exactly \(2\varepsilon\) in norm. Passing \(\varepsilon\) to \(N\delta\) or to \(1\) gives the two branches of the exact formula.

No computation, finite enumeration, external certificate, or unproved asymptotic limit is part of the proof. The result does not optimize over all exposing functionals and does not compute the diameter of the entire slice.
