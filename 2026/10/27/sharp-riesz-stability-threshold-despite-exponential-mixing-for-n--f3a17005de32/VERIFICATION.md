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

The exact analysis uses Haar preservation of each centered inner function, a first-Taylor-coefficient identity, and Gram factorization \(LC^{(N)}L^*=D\). These establish the entire general theorem for every \(N\), not merely a finite sample. Weighted bidiagonal norm bounds yield the universal Riesz constants and adjacent innovations prove necessity at derivative supremum one. Toeplitz trial vectors prove simultaneous optimality. The exact sparse-spike example satisfies the assumptions of Evdoridou et al.'s 2026 Theorems A and C(a), while principal-minor interlacing proves its severe Gram conditioning.

The executable file `CHECKER.py` independently computes four exact symbolic Gram inverses, nine symbolic derivative products, a 65,536-point Haar quadrature test for four observable times, three large finite Toeplitz sharpness trials, and six exact power-of-two near-rotation eigenvalue identities. The stored output `CHECKER_OUTPUT.txt` is the output from running `python CHECKER.py` with Python, SymPy, and NumPy. The numerical quadrature bound is not a formal interval certificate. Neither the infinite Riesz characterization nor the entropy/mixing results can be established by these finite checks; see the analytical proof and primary citations.

Independent audit and independent scientific validation have not been performed.
