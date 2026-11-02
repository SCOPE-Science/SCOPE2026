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

# Reproducibility and verification

Run `python3 verify_klein_k3.py` from this directory. The checker has no third-party dependencies; it uses bit-polynomial arithmetic for all finite fields \(\mathbb F_{2^n}\) with \(1\le n\le6\), checks the defining quartic by full projective-point enumeration, and evaluates the partial derivatives at every point on the quartic. It checks the seven-root singular locus formula and that the two tangent directions occur exactly over even-degree extensions. It then independently compares the predicted two-blowup rational-point correction against the closed-form expression. The exact success marker is `KLEIN_SEVEN_A3_FROBENIUS_ZETA_CHECKS_PASS`.

Expected numerical check for \(n=1,2,3,4,5,6\): singular quartic counts \(7,21,73,273,1057,4161\); singular rational point counts \(1,1,7,1,1,7\); smooth-resolution counts \(9,33,129,321,1089,5505\). This finite test is corroborative. Universal validity follows separately from the seven singularity parameters, formal local \(A_3\) normal form, arithmetic tangent-cone splitting, the two-step resolution, and the all-field radicial projection described in `RESULT.md`.

No independent audit or independent external validation has been performed.
