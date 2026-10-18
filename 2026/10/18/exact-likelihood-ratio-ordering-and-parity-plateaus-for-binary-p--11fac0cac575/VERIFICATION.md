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

The analytic proof is in `RESULT.md`. Execute `python verify.py` with the Python standard library. It performs exhaustive binary-word enumeration for every length from 2 through 9, verifies all conditional composition coefficients and every 2-by-2 minor of the folded transition kernel, and independently computes the binary urn law using exact rational rising-factorial weights for five positive concentrations. It then checks each required parity plateau, strict likelihood-ratio jump, and strict upper-tail inequality for every ordered parameter pair. The reported result is 1,882 exact-rational assertions passed.

These are **finite computations**, not exhaustive verification over arbitrary lengths and positive real parameters. The proof of the infinite quantified result is the positive-minor and likelihood-ratio argument; the finite tests protect against indexing and normalization mistakes only. The full text of two close historical sources was unavailable; this limits historical priority review but not the direct mathematical proof. Independent audit has not been performed.
