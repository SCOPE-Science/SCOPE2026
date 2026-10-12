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

The supplied `verify.py` is a standard-library exact checker. It embeds the second \(12\times25\) generator matrix from the cited `25-12-9.txt` file and performs the following checks over \(\mathbb F_3\):

1. exact row rank \(12\) and self-orthogonality \(GG^T=0\);
2. exhaustive enumeration of all \(3^{12}\) words of \(C\), recovering the stated complete weight enumerator and minimum distance \(9\);
3. exhaustive search of all normalized dual relations supported on at most four coordinates, recovering no weights \(1,2,3\) and exactly one projective weight-\(4\) relation on \(\{1,19,20,21\}\);
4. the exact ternary MacWilliams transform, recovering every stated coefficient of \(W_{C^\perp}\) and total size \(3^{13}\).

`verification_output.txt` records a successful replay ending in `VERIFY_OK`.

The check is finite and exhaustive for the stated code and the complete primal enumerator, and exact for the complete dual enumerator via the MacWilliams identity. It does not enumerate or classify the other 25 extremal equivalence classes. Independent audit has not been performed.
