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

The included standard-library script `verify_noncrossing.py` exhaustively generates the noncrossing partitions of \([n]\) for \(5\le n\le9\) (a total of \(6{,}895\) partitions). It compares the conditional profile probabilities to those of positive uniform compositions; it computes all \(50\) eligible conditional singleton/size-\(s\) covariance triples as exact rational numbers and compares them to the theorem. It separately checks the size-biased algebra for all eligible triples with \(5\le n\le200\), and explicitly verifies \(\operatorname{Cov}(X_1,X_6\mid K=3)=0\) at \(n=10\).

To reproduce: run `python3 verify_noncrossing.py` in any Python 3 environment using only the standard library. The expected final line starts with `VERIFY_OK 6895 noncrossing partitions; 50 conditional covariance cases`.

These checks are finite; the all-parameter theorem is established by the Lagrange-inversion and marked-composition argument in `RESULT.md`. They do not certify historical originality or supply an independent scientific audit.
