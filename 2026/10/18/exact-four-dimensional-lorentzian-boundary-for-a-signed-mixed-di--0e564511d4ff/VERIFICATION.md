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

Run `python3 verify.py` with SymPy installed (a standalone Python 3 script; no source repository or network access needed). The program exactly expands the generic determinant of a symbolic \(4\times4\) symmetric matrix to certify the normalization factor \(12\) for the coefficient of the term containing two copies of \(A\), one copy of \(Z\), and one of \(I_4\). It verifies the generic algebraic identity \(\det W=-4(e_1e_3-4e_4)\) for all symbolic eigenvalues and evaluates each rational boundary witness and the precise negative reverse-CS deficit.

The universal inertia proof is the three-step analytic block-decomposition, trace-zero, and Perron–Frobenius argument in `RESULT.md`. Symbolic identity verification is exact over the polynomial ring, but it does not separately prove the Perron–Frobenius lemma or literature originality. This is a self-review; no independent audit has been performed.
