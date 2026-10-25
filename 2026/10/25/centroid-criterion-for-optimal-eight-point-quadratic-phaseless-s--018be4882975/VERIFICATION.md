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

Analytic checks: the Hermitian form's restriction to both lines has the same leading coefficients \(c\) and \(2w\); the cubic-coefficient discrepancy is \(c(\sum r_j-\sum s_j)\). With unequal sums, a nonzero kernel matrix is a scalar multiple of \(H_h\), whose determinant is exactly \(2\). With equal sums, an independent kernel direction with \(c=1\) exists and \(\det(K_1+tH_h)\) has a real root as an odd-degree real polynomial with leading coefficient \(2\). Vandermonde injectivity excludes nonzero semidefinite kernel elements.

Executable supplementary check: run `python checker.py` using Python 3 and SymPy. It validates the quartic leading terms, the full-rank line-vanishing direction, and six rational/integer coordinate examples on both sides of the centroid boundary. Expected output is in `checker_output.txt`. Finite checks are not a proof of universal injectivity; the full symbolic proof is in `RESULT.md`.

No external or independent scientific audit or numerical conditioning certificate has been supplied.
