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

The exact source equations for the period-dependent probability-generating functions, the unit-premium root matrix, and the last normalization row were compared against the original 2022 preprint and the 2024 OA extension. The matrix in the theorem agrees with their unit-premium equations after cyclic column indexing.

The proof reconstructs formal series using the nonvanishing constant term of the kernel. It explicitly cancels all simple zeros in the closed unit disk, including any on the unit circle, and proves sufficient analytic radius for summability of all phase coefficients. The phase transition at zero is checked by direct coefficient comparison; the finite signed-measure implication is then reduced to the standard unique-ergodic-class criterion using an explicit one-period negative drift and zero-claim accessibility.

To reproduce the standalone example, use Python 3 to run `python check_example.py` from the package directory. The expected output is `VERIFY_OK kernel_factorization=exact root=-1 determinant=1`. The example is finite evidence only; the mathematical proof covers all allowed periods and light-tailed law choices. Stronger general-premium and heavy-tailed assertions remain unproved here.
