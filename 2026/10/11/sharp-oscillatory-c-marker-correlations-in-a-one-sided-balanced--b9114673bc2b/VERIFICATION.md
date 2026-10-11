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

# Mathematical verification

Run `python checker.py` using Python 3 and its standard library. It independently counts first-return words through length \(90\), constructs conditional renewal probabilities as exact rational numbers, checks all \(91\) rational covariance coefficients through degree \(90\), and confirms return-weight normalization at \(1/2\). A successful run prints `PASS`.

These finite calculations do not certify the entropy uniqueness claim or the infinite covariance limit. The proof instead uses a uniquely decodable first-return presentation, entropy/relative-entropy inequalities with the inducing formula, an exact renewal transform, and a complete cubic pole comparison. Errors outside tested lengths remain possible if those mathematical steps were wrong; the independent audit is not yet performed.
