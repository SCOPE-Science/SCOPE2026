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

# Reproducibility
The mathematical claim concerns all binary word lengths at least three, not merely the tested finite range. The proof's finite exhaustive support reduction is valid for arbitrarily large edge multiplicities; `derive_gf.py` sums those multiplicities as rational functions and verifies the closed form by exact symbolic cancellation.

Execute `python derive_gf.py` with Python 3 and SymPy installed. Expected exact symbolic check: `EXACT_GF_PASS; valid support/start/end types=136`. Execute `python verify.py` with Python 3 alone. Expected independently constructed finite test: `BRUTE_FORCE_PASS n=3..18`, followed by the documented first thirteen values and a recurrence check through length 112.

The scripts are ordinary mathematical checkers, not formal mechanized proofs or independent external validation. The published statement's first-public-date refers to its 2026 primary literature motivation, not to the creation date of this exact enumeration. Historical literature cannot exclude unknown equivalent formulas.
