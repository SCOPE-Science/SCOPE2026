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

Exact finite-field verification: running `python3 verify_bring5.py` reproduces `verify_output.txt`, with six rational transverse conic--cubic directions, affine-group coset count six, evaluation ranks \((1,3,5,6,6,6,6)\), delta \(9\), seminormalization defect \(4\), and point counts \((31,151,751,3751)\) over the first four extension fields. The script was run on the actual embedded source before final assembly.

The proof of reducedness uses the Jacobian criterion away from the common point and Cohen--Macaulayness of a pure complete intersection. The normalization sequence and truncated logarithm prove the group-scheme isomorphism over \(\mathbb F_5\); finite experiments alone do not certify such an isomorphism. No assertion about a semistable model, Néron model, or characteristic-zero specialization of Picard schemes is made. The singularity is nonnodal and the normalized special fiber has six connected components. Independence or external expert validation has not been performed.
