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

Run `python verification/check_drum.py` with the listed dependencies. It independently expands the *exact source expressions* for surface area and edge-inclusive total mean curvature to sixth order, checks the exact fixed-area coefficients using the spherical derivative, verifies the critical sixth-order sign and optimizing coefficient algebraically, and tests the implicit fixed-area solution at 75-digit precision. The tests use areas both below and above \(2\pi\) and compare several supercritical test surfaces with both classical competitors. The program was run successfully on the embedded saved version.

The universal sign for every fixed positive area, the existence and uniqueness of the local critical branch, and the strict all-area interval conclusion follow from the analytic proof; the finite numerical examples do not by themselves prove these claims. The exact two-parameter input identities are due to Hong, arxiv:2606.01771v4. A separate independent audit has not been performed. Scope is the symmetric two-plane truncated-ball family, not global minimization over all convex bodies.
