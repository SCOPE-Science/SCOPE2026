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

The proof is a full combinatorial derivation using unique greedy-arch decompositions, the symmetric-midpoint lemma, and exact support enumeration. The generating-function identity is formal and valid for all integers \(f,d\ge1\), all word lengths, and all universality indices.

To repeat finite tests, run `python3 verify_mixed_gf.py` and `python3 verify_symmetry.py` from the directory containing these files. Both scripts use only Python's standard library and print `VERIFY_OK` on successful completion. The former checks six mixed involution types, comparing exact convolution coefficients with exhaustive self-symmetric words through specified small lengths; the latter checks shortest-length statements and counts with exhaustive smaller-alphabet enumeration, including absence of shorter universal symmetric words.

These finite tests are consistency checks, not proofs of an unrestricted infinite identity. The infinite result is justified by the six proof steps in `RESULT.md`. Prior published formulas cover the pure identity and fixed-point-free involution cases; the mixed type is the new domain assessed here. Independent external verification has not been performed.
