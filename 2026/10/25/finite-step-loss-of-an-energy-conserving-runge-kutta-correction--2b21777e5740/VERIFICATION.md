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

# Reproducibility and scope

Run `python verify.py` with Python 3.10 or newer. No additional packages are required.

The verifier checks the exact-rational two-frequency witness, the one-step energy conservation identity, the signed second-step discriminant, the sharp initial energy share, rational modal identities, and 20,000 seeded random finite-mode instances of the quadratic conservation equation. It prints `VERIFY_OK` on success.

The finite-time obstruction for every positive-energy high-frequency mode is an analytical consequence of the strictly increasing highest-frequency energy and bounded conserved total energy. Random tests or finite symbolic grids do not establish the infinite-iteration theorem independently; the proof is in `RESULT.md`.

The scientific assessment is a self-review; no independent audit has been performed.
