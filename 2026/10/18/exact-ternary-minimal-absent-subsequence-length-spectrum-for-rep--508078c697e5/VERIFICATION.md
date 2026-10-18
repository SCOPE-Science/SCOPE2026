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

# Reproducing the checks

Run `python3 verify_mas.py` using Python 3 with no third-party dependencies. It compares independently computed direct scattered-subsequence membership with the local characterization over complete finite layers, and checks coefficient tables. Expected last line: `VERIFY_OK`.

Run `python3 verify_rational.py` in an environment with SymPy installed. It verifies the exact multivariate polynomial determinant and adjugate identity of the nine-state transfer matrix. Expected marker: `SYMBOLIC_OK 9state_determinant_and_numerator bivariate_and_univariate`.

The complete mathematical proof is in `RESULT.md`; these finite checks and symbolic algebra confirm calculations but do not replace the proof for all positive integer repetition counts. No independent audit has been performed.
