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

The file `verify_rectband.py` contains an independent multiplication checker based on explicit four-index semigroup multiplication, rather than relying on the row-sum/column-sum proof shortcut. It enumerates all ordered pairs in eight selected finite algebras at field orders two and four, reduces each commutator by finite-field Gaussian elimination, and asserts exact equality with the formula's three rank counts. Executing `python3 verify_rectband.py` prints `RECTANGULAR_BAND_COMMUTATOR_OK 8 complete enumerations` on success. This code's finite cases do not prove the unbounded finite-field theorem; the general proof is included in `RESULT.md`. The claimed lack of complete prior coverage is subject to the identified historical publication-priority limitations. No independent audit has been performed.
