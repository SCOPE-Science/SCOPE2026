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

# Reproducible checks and mathematical scope

Run `python artifacts/verify.py` with Python 3, SymPy, and NumPy available. The program constructs the orthogonal centered-activity/label-contrast basis over the whole alphabet and evaluates the exact Bernoulli shell Gram matrix independently of the closed spectrum formula. SymPy compares full rational characteristic polynomials for parameters \((q,n,k,d)=(3,4,2,2),(3,5,2,2),(4,4,2,2)\). The matrix dimensions are \(33,51,67\), and the predicted positive ranks are \(24,40,54\) respectively.

The program also diagonalizes an independently assembled full Gram matrix for \((q,n,k,d)=(3,6,3,3)\), of matrix dimension \(233\), and compares the entire eigenvalue multiset with the formula, including \(73\) zeros and \(160\) positive eigenvalues. The numerical comparison uses tolerance \(10^{-11}\), so it is not an exact certificate.

The all-parameter proof is the tensor contrast decomposition, the Boolean harmonic incidence norm formula, the slice generating-function restriction identity, and the independent injectivity argument for multiplication by the shell equation in `RESULT.md`. Small computations cannot certify that proof universally. No independent audit or formal proof certification is claimed.
