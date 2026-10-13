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

Run `python3 verify.py` in the same directory. The verifier uses only the Python standard library and exact integer/finite-field arithmetic.

It checks:

1. reconstruction of \(f_8\) from its defining sum and the centered identity \(f_8(z+4)=h(z^2)\);
2. the irreducible degree-\(4\) factor modulo \(17\) and the \(1+3\) factorization modulo \(11\) for \(h\);
3. the squarefree \(4+2+1+1\) factorization modulo \(7\) for the centered degree-eight polynomial;
4. the order \(192\) of the even signed permutation group and the exact count \(75\) of elements fixing a signed root;
5. the group-theoretic model of the modulo-\(7\) cycle type whose square is a weight-\(2\) sign flip.

Recorded output:

`VERIFY_OK centered_f8=yes h17=irreducible4 h11=1+3 g7=4+2+1+1 group_order=192 fixed=75 density=25/64`

The verifier does not prove Chebotarev's density theorem and does not infer an infinite density from a finite prime sample. The density conclusion uses the exact Galois-group proof plus the standard theorem.
