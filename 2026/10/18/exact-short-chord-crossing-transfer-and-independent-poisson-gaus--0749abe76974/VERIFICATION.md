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

Execute `python verify_chord_joint.py` from the same package. The standard-library implementation independently generates every perfect matching on the fixed boundary labels for sizes \(n=2,3,4,5,6,7\), and computes both the local simple-chord count and unordered crossing-pair count directly. It checks for each \(0\le k\le n\) equality of the entire exact-rational crossing histogram weighted by the falling factorial, rather than checking only moments. The comparison histogram comes independently from size \(n-k\). It also checks the exact means, covariance, variances, squared correlation, matching counts, and coefficient bounds.

Observed output: `PASS: 487 exact-rational/equality assertions; all perfect matchings through n=7 checked.`

Limit of computation: all-size transfer and asymptotic independence are established analytically in RESULT.md. Finite enumeration alone cannot certify them. The normal crossing marginal invoked in the limit is from Flajolet–Noy (2000). No independent external audit or certification has been performed.
