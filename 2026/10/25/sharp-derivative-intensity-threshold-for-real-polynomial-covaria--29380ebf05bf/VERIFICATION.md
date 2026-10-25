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
# Reproducibility and limits

Run `python checker.py` in the extracted directory with Python 3 and SymPy. The script checks exact rational matrix ranks and nullities for all \(N=1,\ldots,12\), all derivative orders from \(0\) through \(\min(N,7)\), annihilation of the explicit \((X-Y)^{2K+2}\) witness, and strict positive definiteness of two distinct counterexample matrices. Observed result: `PASS: 111 exact assertions, degrees n=1..12, derivative ranges up to 7`.

The infinite statement is proved algebraically in RESULT.md; this finite experiment does not serve as an infinite proof. No independent audit or certification has been conducted. The formula recovers real symmetric covariances, not arbitrary complex Hermitian covariance matrices, and the claimed minimality is for all-rank covariance reconstruction rather than recovery of a single complex signal.
