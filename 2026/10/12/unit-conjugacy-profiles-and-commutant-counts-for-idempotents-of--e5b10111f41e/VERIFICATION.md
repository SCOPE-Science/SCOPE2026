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

# Verification of unit-conjugacy profiles and centralizer formulas

Run `python3 verify.py` using a standard Python 3 interpreter. No external packages or external files are required.

Observed output from the extracted standalone source:
```
n 2 magma_monoid_order 16 idempotents 7 unit_orbits 4 unit_group 4 centralizer_samples 7 VERIFY_OK
n 3 magma_monoid_order 19683 idempotents 706 unit_orbits 31 unit_group 288 centralizer_samples 31 VERIFY_OK
```
The program enumerates all equivariant endomaps and literally composes them. For \(n=2\) it checks the centralizer formula on every idempotent. For \(n=3\) it checks it for one idempotent from each of all 31 unit-conjugacy classes; centralizer cardinality is conjugacy-invariant, so this checks all classes. It also constructs every unit conjugate and compares the resulting orbits to the profile partition, and verifies predicted orbit sizes and that the orbit partition exhausts all idempotents.

Separate direct enumeration of all binary-operation multiplication tables and the literal product defining the magma monoid returned 7 and 706 idempotents at \(n=2\) and \(n=3\) respectively. The finite enumerations are not an all-n proof. The all-n proof in RESULT.md establishes the retraction classification, signed-permutation stabilizer count and fiberwise commuting-map construction.

No external or independent audit has been performed. Historical novelty cannot be certified by database or literature searches.
