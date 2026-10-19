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

Execute `python3 check.py` using standard Python 3. The checker independently enumerates every field-linear \(3\times 3\) candidate endomorphism matrix for three finite fields and checks composition-idempotence and the original multiplication table directly. It also performs reduced-row-echelon subspace enumeration over the binary field and a separate direct quotient-projection enumeration in dimension four, without using the Goursat classification to construct those objects.

The saved execution reported `ALL_EXACT_CHECKS_PASSED`, with direct map rank profiles \([(0,1),(1,8),(3,1)]\) over \(\mathbb F_2\), \([(0,1),(1,18),(3,1)]\) over \(\mathbb F_3\), and \([(0,1),(1,32),(3,1)]\) over \(\mathbb F_4\). For the five-dimensional algebra over \(\mathbb F_2\), the direct quotient-projection calculation returned \([(0,1),(1,144),(2,320),(5,1)]\). The ordered zero-product subspace dimensions in \(\mathbb F_2^6\) were counted as \([(0,1),(1,35),(2,77),(3,16)]\).

These bounded checks do not certify the universal theorem; correctness for every \(n\) and \(q\) rests on the proof in `RESULT.md`. Originality searches do not establish exhaustive prior-art absence. Independent mathematical audit: not performed.
