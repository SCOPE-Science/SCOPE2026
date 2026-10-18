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

# Verification of the Gaussian AR(1) finite-window covariance theorem

`verify_gaussian.py` needs Python 3 and SymPy and can run without network or external datasets. The verifier recomputes the centered-matrix covariance numerator independently of the geometric-sum expression, checks their equality over integer sample sizes \(2\) through \(10\) at several exact rational correlations, checks the closed half-correlation formula and the independent-case boundary, and differentiates the numerator to verify the near-perfect-correlation coefficient. It also reconstructs the low-dimension factorizations and positive Bernstein coefficients, and tests the midparameter sign for a further finite range of sample sizes. On the packaged scientific inputs, the script completed **204 exact assertions**.

The finite verifier is supplementary, not a certificate for infinitely many integers or for the entire correlation continuum. The written proof establishes the all-\(n\) signs with a symbolic geometric formula, and the low-dimensional positive Bernstein polynomials appear explicitly in the manuscript. The claim has no Lean proof and has not received independent scientific review or priority verification. An inaccessible relevant Gaussian crossing-covariance article is listed among historical risks.
