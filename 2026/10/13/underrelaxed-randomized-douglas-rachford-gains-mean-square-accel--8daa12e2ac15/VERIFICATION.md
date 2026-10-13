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
The reproducibility program `verify.py` is standalone Python using only the standard library.

It enumerates the four possible ordered pairs of two row reflections for the homogeneous identity system, verifies the resulting scalar Bernoulli law, reconstructs exact first and mixed second moments with rational arithmetic, and checks them against the claimed finite-dimensional moment operator through several steps.

It independently constructs the rational witness’s characteristic coefficients and certifies all three real-root brackets by exact sign changes. It checks the sufficient source bound and the published upper-bound factor, and algebraically replays the zero-momentum slope and the critical midpoint expansion.

The finite enumeration and decimal approximations are reproducibility checks, not substitutes for the exact recurrence, root-isolation argument, or analytic eigenvalue proof.
