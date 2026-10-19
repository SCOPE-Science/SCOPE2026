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
# Reproducibility checks and limits

The exact proof uses matrix-space linear algebra over an arbitrary finite field. The crucial steps to check directly are (i) the inequality \(\dim J\leq\dim(JM)\dim(M/\operatorname{Ann}_M(J))\), (ii) the fact that any matrix hyperplane contains an invertible matrix, (iii) the pointwise stabilizer of such a hyperplane under the left/right general linear action, and (iv) the resulting block commutation equations.

The standalone script `verification/check.py` enumerates all \(2520\) frames of \(2\times2\) matrix hyperplanes over \(\mathbb F_2\) and their complete group orbits; it finds orbit size \(36\), class counts \(42,28\), and adds two rectangular classes. Over \(\mathbb F_3\) it enumerates all \(40\) projective hyperplane normals and directly checks every corresponding pointwise stabilizer, obtaining size \(2\); its rank-stratum totals are \(156,234\). It additionally evaluates the closed formulas as integers for \(s=2,3,4\) and \(q=2,3,4,5\). Those arithmetic checks are not exhaustive enumeration over extension fields or larger modules.

Execute with `python3 verification/check.py` using Python 3.8 or later. The script has no third-party imports. The mathematically infinite part of the claim is justified in `RESULT.md`, not inferred from test coverage. No external mathematical audit or proof-assistant verification has been performed.
