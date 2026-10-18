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

# Reproduction and scope

Run `python3 checker.py` using the Python standard library. Its successful local replay returned **502 assertions** with no failure. The exact rational tests confirm the finite lattice-return coefficient recurrence, every observer/particle path-trace moment identity for lengths \(1\le n\le6\), the \(96n^2\) uniform third-moment majorant in those cases, and the shared-part Poisson covariance. A separate Simpson quadrature check evaluates the proposed large-\(n\) crossover constant for four choices of the scaled drift and compares it with the exact finite return-probability recurrence.

For \(\lambda=1\), the asymptotic variance-per-\(n^{3/2}\) predictions for \(\kappa=0,1,2,4\) are approximately \(1.50450556,1.43313080,1.25780829,0.87607373\), respectively; their corresponding \(n=5000\) finite values are \(1.49047626,1.41914143,1.24387871,0.86212447\). These finite computations are **not** substitutes for asymptotic proof, do not establish novelty and do not provide independent scientific audit.

The mathematical proof relies on the uniform centered Poisson characteristic expansion, a parity-aware simple-random-walk local central limit theorem, the triangular functional central limit theorem, and the exact Poisson–Charlier bivariate covariance identity. Reconstructing these steps and checking all normalizations, hypotheses and boundary cases are necessary for assessing the infinite claim. No external certification has been performed.
