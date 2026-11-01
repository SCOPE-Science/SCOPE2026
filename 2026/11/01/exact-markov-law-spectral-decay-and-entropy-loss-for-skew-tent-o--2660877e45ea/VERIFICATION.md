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

# Reproduction and proof limits

Execute `python3 verify_ordinal_skew.py` with Python 3 standard library. The script uses exact fractions for seven skew parameters \(c=1/10,1/4,1/3,1/2,2/3,3/4,9/10\). It computes all two-step and three-step ordinal-cylinder measures from inverse affine intervals and checks them against the stationary Markov formula, tests all symbolic words of length at most four for positive measure precisely when graph-admissible, checks matrix row sums and stationary weights, evaluates both characteristic polynomials by exact determinants, and checks the entropy formula numerically. It completed without assertion failures both directly and after assembly. Exact finite checks are corroborative; the manuscript's all-parameter and all-length proof relies on the stated affine full-inverse-branch property, stationarity, and determinant identities. The material does not assert independent external auditing or a computational proof for infinitely many parameters.
