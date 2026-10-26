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
# Reproducibility and limits

Run `python verify.py` in a standard Python 3 installation (no dependencies). A successful execution prints `2LI_EXACT 2 6 / 16`, `2LI_EXACT 3 210 / 512`, `ODD_FIELD_DIM_TWO 3 two_LI 48 unique 56 out_of 81`, `ODD_FIELD_DIM_TWO 5 two_LI 480 unique 480 out_of 625`, `SINGULAR_RIGID_CRITERION_WITNESS 5 rank 4 rows [25, 4, 17, 27, 10]`, and `VERIFY_OK`. Exhaustive binary enumeration checks all \(n=2,3\) structure matrices and every corresponding invertible change of basis. The prime-field two-dimensional enumeration corroborates the stated restriction on the necessity of 2LI: a field of three elements has more unique-natural-basis algebras than 2LI algebras, whereas the counts agree at field size five.

The five-dimensional binary witness has singular structure matrix, nonzero pairwise distinct square rows, and a strongly connected asymmetric directed support containing a loop. It is a witness to the deterministic criterion, not a proof of genericity.

The general argument uses exact ranks, the multiplicative automorphism identity, independent random support bits, the bound on Bernoulli orbit invariance, and elementary finite-field matrix rank probabilities. Code cannot verify the asymptotic bounds for all dimensions; no independent audit, formal proof certification, or external validation is claimed.
