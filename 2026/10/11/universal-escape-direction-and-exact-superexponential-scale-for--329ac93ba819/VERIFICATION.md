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

# Verification and scope

The analytical proof includes a global monotone-sequence exhaustion, exact recurrences for the sum and difference on the escaping tail, explicit relative-error bounds, a convergent telescoping series for the escape height, and a tail estimate proving an additive \(o(1)\) in the logarithm. It separately verifies the even-degree sign-conjugacy and excludes all unproved bounded-trajectory alternatives.

The standalone `verify_escape.py` checks exact integer coordinate recurrences and signed conjugacy and tests numerical convergence of the limit for finitely many seeds and even degrees. It does not certify the general theorem; the general proof is contained in `RESULT.md`.

The origin and its basin-boundary topology are established in the cited primary literature. The present theorem is restricted to the exact polynomial model and does not claim transfer to the genuine secant iteration. Publication priority and independent mathematical validation remain open.
