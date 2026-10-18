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

# Reproducibility and verification

The claim follows from the exact geometric argument in `RESULT.md`: the two perimeter-excess expressions, the unique edge-ray transition equation, and the Green integrals supply the all-parameter proof. No numerical integration is used in the proof.

Run `python3 verify.py` from this directory. The script has no nonstandard package dependencies. It constructs the convex hull of the three triangle vertices and an exterior point directly using the monotone-chain algorithm. For six values \(q=\pi\delta\) it checks the edge-extension transition and independently evaluates the separation-body area by radial bisection and polar quadrature. The recorded run ended with `VERIFY_OK equilateral triangle separation-body all-parameter area`. The largest observed absolute area discrepancy was below \(3\times10^{-6}\) for the six values tested.

The exact small-parameter series is obtained by ordinary Taylor expansion of the displayed closed form with \(q=s^2\). Neither finite sampling nor a formal series truncation is presented as a proof outside its domain; the exact formula covers every \(\delta\ge0\). No independent audit has been performed.
