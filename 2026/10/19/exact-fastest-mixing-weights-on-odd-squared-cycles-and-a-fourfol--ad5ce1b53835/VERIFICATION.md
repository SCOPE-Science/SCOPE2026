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

# Verification and reproducibility

Run `python verify.py` with Python 3, NumPy, and SciPy. This reproduces independent Fourier and full-matrix eigenvalue checks, finite-dimensional linear-program optimizations, random noncirculant feasible competitors, and large-order asymptotics. The reviewed execution printed `PASS 1651 checks`.

The decisive infinite-family argument is analytical: dihedral averaging, location of the discrete maximum of a concave quadratic, exact positivity of holding probability, and an affine three-contact lower-bound argument. Numeric tests cannot establish global optimality for all orders or exclude equivalent prior literature. Independent external audit has not been performed.
