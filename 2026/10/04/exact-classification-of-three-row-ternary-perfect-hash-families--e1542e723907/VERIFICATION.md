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

The certificate is finite and self-contained. `verify.py` reconstructs all \(27\) ternary columns of length three and checks every candidate directly from the perfect-hash definition. It enumerates all \(296010\) six-subsets and all \(888030\) seven-subsets. It then evaluates the complete equivalence group of order \(1296\) on every maximum family, checks that there is exactly one canonical representative, and regenerates its orbit to obtain exactly \(36\) labeled maxima with stabilizer order \(36\).

Run:

`python verify.py certificate.json`

Expected final line:

`VERIFY_OK p3(3,3)=6 maxima=36 orbits=1 stabilizer=36`

The enumeration of seven-subsets is exhaustive, so the nonexistence assertion is not inferred from a timeout or a partial search. The conclusion for all larger column counts uses only heredity: deleting columns from a perfect hash family preserves the defining property. The computation proves no statement about larger alphabets or different row counts.
