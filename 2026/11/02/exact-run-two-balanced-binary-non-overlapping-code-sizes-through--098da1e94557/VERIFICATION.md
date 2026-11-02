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

# Finite-certificate verification

Place `verify.py` and `certificates.json` in the same directory and run `python3 verify.py` under Python 3. The verifier requires only the standard library and reconstructs every balanced, cyclic-run-two, unbordered word at the specified lengths by exhaustive iteration over all binary words. It independently checks every same-color pair has an overlap, every pair of witness codewords has no overlap, the witness words are eligible, and all expected lengths/counts agree. It also reconstructs the restricted Dyck counts from their original Dyck-path restrictions.

The extracted package was replayed and returned `VERIFY_OK` with six length-specific lines matching the claimed table. An accepted independent audit or other external certification is **not** asserted. The upper bound is a finite combinatorial certificate; no extrapolation to higher even lengths follows from it. Historical novelty is limited to the inspected literature, and a later unindexed table may require a fresh priority comparison.
