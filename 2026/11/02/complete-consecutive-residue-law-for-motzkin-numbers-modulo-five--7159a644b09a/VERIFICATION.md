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

The included `verify_pairs.py` uses only the Python standard library and outputs `VERIFY_OK` on success. It independently derives the twenty finite push-forward cases using the first five central-trinomial coefficients, checks their eighty-triple frequency matrix, verifies exact Motzkin/central-trinomial identities at finite indices, and checks base-five prefix histograms. Tests are finite verification, not the proof of asymptotic equidistribution. The infinite arguments and the exact nonoccurrence of zero--zero pairs are contained in `RESULT.md`.

The review recorded in `REVIEW.md` is the self-review only; no independent scientific audit has been performed.
