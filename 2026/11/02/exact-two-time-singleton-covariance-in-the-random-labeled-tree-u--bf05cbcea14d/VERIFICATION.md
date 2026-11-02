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

The exact finite covariance follows analytically from a weighted Matrix–Tree cofactor, an explicit rank-two determinant calculation, and a three-case enumeration of ordered vertex pairs. The limiting two-time covariance follows by uniform first-order expansions in reciprocal tree size on compact interior time sets.

Reproduce local checks using `python checker.py` with Python 3 and no third-party packages. It constructs all labeled trees through Prüfer codes for sizes 4 through 7 and checks exact rational time-pair cross moments; it checks selected additional finite covariance signs and a numerical approach to the limiting kernel. It returns 79,130 assertions passed. Finite checks cannot certify the asymptotic claim, which rests on the proof; no finite-order covariance positivity theorem is claimed. Historical priority and independent validation remain unperformed.
