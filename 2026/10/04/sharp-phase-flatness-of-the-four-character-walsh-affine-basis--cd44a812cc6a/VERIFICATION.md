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

The proof is analytic and does not depend on computation. The following checks are packaged only to guard the displayed equality case and constants.

1. `verify.py` represents the extremizer \((1,e^{i\pi/4},i,e^{3i\pi/4})\) in exact arithmetic over \(\mathbb Q(\sqrt2)\) and evaluates all eight Walsh samples.
2. It verifies exactly that the squared magnitudes are \(4+2\sqrt2\) four times and \(4-2\sqrt2\) four times.
3. It verifies algebraically that the larger value is \(\csc^2(\pi/8)\).
4. It runs a deterministic numerical phase stress test as a regression check. This finite test is not evidence for the universal lower bound; that bound is proved by the zonogon perimeter argument in `RESULT.md`.

Unproved beyond the stated result: unrestricted coefficient magnitudes, more than four Walsh characters, and any global literature-uniqueness assertion.
