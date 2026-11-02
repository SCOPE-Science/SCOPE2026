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

# Verification record

The primary mathematical evidence is the fully written proof in `RESULT.md`. The reproducibility script `CHECK.py` uses only the Python 3 standard library.

Run `python3 CHECK.py` from a directory containing the script. Actual replay returned: `PASS: 2870 exact and numerical assertions`.

The checker directly enumerates uniform drawn blocks for all \(3\le n\le9\), every allowed \(s,r\), all feasible pair-overlap sizes, and \(k\in\{1,2,3\}\). Exact rational computations verify the two inclusion probabilities and the covariance-sign rule; they also independently test the one-omitted-point formula. The finite example at \((n,r,s)=(100,50,12)\) is checked with exact binomial ratios. The final assertions compare the falling-factorial logarithm against its predicted limit for proportional block sizes and target sizes of order \(\sqrt n\), and independently enumerate the global overlap-sign fraction using exact hypergeometric probabilities.

The program's finite enumerations and numerical convergence tests do not prove the unrestricted finite theorem or the limit. The latter rely on the algebraic and analytic arguments in `RESULT.md`. No independent mathematical audit has been performed.
