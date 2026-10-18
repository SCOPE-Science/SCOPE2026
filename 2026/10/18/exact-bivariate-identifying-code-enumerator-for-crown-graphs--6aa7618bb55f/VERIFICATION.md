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

# Verification scope

Run `python3 verify.py` with Python 3 and its standard library. The script constructs every graph \(H_n\) for \(4\le n\le10\), constructs full closed-neighborhood signatures directly from adjacency, tests all \(2^{2n}\) selected sets, and compares both the classification and all coefficients of the bivariate polynomial. It verifies \(1,398,016\) subsets in seven graphs. Separate finite symbolic checks for \(11\le n\le50\) verify coefficient positivity, exchange symmetry and total counts. The complete stdout is preserved verbatim in `verification_output.txt` and ends in `VERIFICATION_OK`.

The source `verify.py` and the recorded output accompany this document. Finite exhaustive checks through \(n=10\) are not an infinite proof; the arbitrary-\(n\) proof is in `RESULT.md`. No other hidden dependencies or computational certificates are required. The reported literature comparisons are scientific best-knowledge checks, not a formal noncoverage certificate.
