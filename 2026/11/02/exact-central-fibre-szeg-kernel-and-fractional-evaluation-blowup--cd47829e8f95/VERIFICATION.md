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

# Verification scope
The analytic proof in `RESULT.md` checks every nonnegative integer exponent using orthogonality of torus characters, evaluates all corresponding exact moments with Vandermonde's identity, and sums the resulting series by a beta integral. Its boundary expansion is a Taylor identity in the positive variable \(u=\sqrt{1-t}\). No numerical finite test is used to prove infinitely many moment identities or a global asymptotic.

# Standalone test
Run `python3 verify_axial_kernel.py` using Python's standard library. It independently checks 51 exact rational torus-moment identities (including the recurrence), evaluates the elementary and partial-series kernels at five points, and checks the claimed boundary correction at three points. Reproduction of this output only verifies these finite checks, not the entire theorem.

# Known limits
The underlying Hardy space and bounded evaluation theorem are premises from arXiv:2610.17729v1. The result is for the canonical unweighted norm, with no assertion about other fibres or a full-domain formula. No independent audit was carried out.
