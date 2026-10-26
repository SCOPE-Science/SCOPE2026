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

The analytic derivation in `RESULT.md` is the proof. Its critical nonstandard ingredient is the phase-uniform factorization of the full three-step return: the cubic Taylor term is explicit, its remainder is controlled in the angular derivative, and six exact inverse cancellations eliminate the near-grid small-denominator problem.

The reproducible `verify.py` implements the positive-root squared-speed formula from the implicit recurrence. It checks the cubic return coefficient with 65-digit decimal arithmetic and two signs of the forcing, checks exactly cancelling three-force arrangements, and runs one long orbit in the escape regime. `VERIFY_RUN.txt` records the actual terminal output, ending in `CHECKS_PASS`.

Finite numerical agreement is not a proof for every phase, arbitrarily high squared speed, or infinite time. In particular, the 500000-cycle growth diagnostic still has an initial-state offset and is not expected to equal the limiting coefficient to high precision. The source is the publicly accessible full-text arXiv:2412.15002v1. Originality is an evidence-based comparison, not independently certified priority.
