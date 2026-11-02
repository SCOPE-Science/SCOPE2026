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
# Reproducibility

Run `python verify.py` with Python 3.10 or later, NumPy and SciPy. The checker constructs the convex hull of the canonical selected vertices for every doubled-pair count \(1\le K\le d\) in dimensions \(2\le d\le5\), collects all supporting-facet vertex sets, closes those sets under intersection to reconstruct all faces, and compares the resulting face counts to the polynomial in `RESULT.md`. It also compares volumes against the orthogonal-pyramid formula. Independently, it evaluates the exact finite probability law and both conditional moment identities with rational arithmetic for dimensions \(2\le d\le8\) and retention probabilities \(1/5,1/2,4/5\). It tests strict annealed–typical inequalities at four numerical parameters.

The program was executed with all tests passing and printed `ALL_CHECKS_PASSED`. Its finite checks do not validate the infinite-dimensional limits or replace the analytic proof, and they do not assess historical priority. The logarithmic asymptotics depend on the classical binomial law of large numbers, central limit theorem, bounded-remainder argument, and strict concavity shown in `RESULT.md`. Independent mathematical audit was not performed.
