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

The standalone `verification/check_joint_three.py` uses only Python 3 standard-library facilities. Invoke `python3 verification/check_joint_three.py` from the package root. It reconstructs the real three-by-three matrix inequality as squared integer comparisons \(9D^2\le25W^2\), where \(D^2=\sum_j\|a_j\|_1^2\) and \(W^2=\max_s\|A^{\mathsf T}s\|_2^2\).

The script exhausts every matrix with nine entries from \(\{-1,0,1\}\), giving exactly \(19{,}683\) cases; it also checks \(50{,}000\) pseudorandom integer matrices with a fixed seed. It verifies each of four omitted-projective-sign-line relations, the explicit integral witness Gram matrix \(AA^{\mathsf T}=9I_3\), and exact witness squares \(D^2=75\) and \(W^2=27\). An observed invocation returned `VERIFY_OK exhaustive_ternary_matrices=19683 random_integer_matrices=50000 witness_D2=75 witness_W2=27 sign_class_relations=4`.

The decisive universal statement does not follow from enumeration. It is proved in `RESULT.md` by exact coordinate reduction, four sign classes, a dual-vector identity, and Cauchy--Schwarz. No external independent audit or complete bibliographic certification has been performed.
