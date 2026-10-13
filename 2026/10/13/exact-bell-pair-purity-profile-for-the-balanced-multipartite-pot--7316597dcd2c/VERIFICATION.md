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

The exact identity is checked in two independent ways within the package: the proof counts subset types analytically, and `verify.py` directly enumerates all subsets for \(1\le K\le8\) using exact rational arithmetic and compares those averages with coefficients of \((1+x+x^2)^K\).

The balanced cases are additionally checked against the central-trinomial coefficients. The checker verifies the first exact values \(H(B_2)=1/2\), \(H(B_3)=7/20\), and \(H(B_4)=19/70\).

The asymptotic statements are not certified by finite sampling. They follow from the displayed integral/Laplace argument for the central trinomial coefficient and Stirling's formula. No claim is made about finite-size optimality of Bell-pair products or about the full minimizers of the balanced potential.
