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

The proof-critical finite lemma is reproduced by:

`python3 artifacts/verify.py`

The checker uses only exact arithmetic over \(\mathbb F_2\) and \(\mathbb F_3\). For each canonical residue-and-boundary signature it constructs:

- the target exact coefficient space;
- every valid exact predecessor coefficient space;
- the quadratic anchor kernel \(K_r=\ker((1,1,1)+e_r)\);
- every bracket coefficient \(\lambda_w(a)b-\lambda_w(b)a\);
- the rank of their span.

It exhausts \(50\) signatures in characteristic \(2\) and \(108\) in characteristic \(3\). Every target rank matches the bracket-image rank. The recorded output is in `artifacts/VERIFY.txt` and ends with `CHECK_OK`.

The checker certifies the finite linear-algebra lemma after the mathematical reduction; it does not by itself prove that the reduction covers all degrees. That coverage is supplied in `RESULT.md` by showing that the matrices depend only on zero-versus-positive status and coordinate residues modulo the characteristic, with the impossible low-sum signatures excluded for \(d\ge3\).
