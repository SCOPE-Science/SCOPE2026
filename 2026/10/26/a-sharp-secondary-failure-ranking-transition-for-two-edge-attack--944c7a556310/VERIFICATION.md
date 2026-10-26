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

# Reproducibility and verification

The standalone file `crown_verify.py` depends on `sympy`, as declared in `requirements.txt`. Execute `python crown_verify.py`. A completed execution returned `VERIFY_OK` following exhaustive exact checks for \(n=4\), \(5\), \(6\), and \(7\). A transcript of the program's standard output is saved in `VERIFY_OUTPUT.txt`.

The checker reconstructs the spectral kernel from its Kronecker-delta formula, asserts symbolic equality of each of the four two-edge damage rational functions, and tests coefficient positivity certificates of the necessary comparison polynomials upon shifting \(n=t+4\). It checks the complete sign change of \(n^3-14n^2+34n-12\) using finite exact values for integers \(4\) through \(11\) and a positive-coefficient expression at \(n=12+t\). To avoid relying only on Woodbury, it also directly constructs every pairwise edge-deleted Laplacian at the four tested orders, grounds a vertex, inverts the grounded matrix over exact rational numbers, computes the Kirchhoff index, and matches the symbolic orbit formula. The total number of direct inversions is 1,552.

Connectivity for every \(n\ge4\), all possible pairs, and the strict universal comparisons are established by the positivity calculations in the written proof. Finite verification is not claimed as an infinite theorem, formal certification, or independent audit.
