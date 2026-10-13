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

Run `python3 verify.py` in the extracted package directory (Python 3 standard library only). The script constructs 84 fully specified simple graph matrices for \(2\le r\le7\) and \(1\le m\le14\) using exact fractions, confirms the vertex-level annihilating polynomial and eigenspaces, compares the *exact* projector onto eigenvalue zero with cellwise mean subtraction, and tests odd-time phase solvability with integer arithmetic. Expected output: `VERIFY_OK exact_fraction_graphs=84 transfer_cases=12 first_irregular=K_2_2_2_6 time=5pi`.

No floating-point diagonalization is needed. These are limited corroborating examples, not proof of the universal result. For all integer parameters, the analytic proof in RESULT.md derives the full invariant decomposition, forced phases, arithmetic equivalence, and block unitary. The independent audit status in the front matter has not been independently assessed here.
