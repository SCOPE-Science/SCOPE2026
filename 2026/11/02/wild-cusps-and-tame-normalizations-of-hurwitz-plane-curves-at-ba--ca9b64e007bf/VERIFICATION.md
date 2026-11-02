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

# Verification record
The standalone `verify.py` uses only Python standard-library integer and finite-field arithmetic. It verifies sample singularity counts, delta/genus arithmetic, the simple critical point coefficient, and equality of direct plane point counts with counts from the tame Kummer normalization over prime and quadratic extension fields. Execute `python3 verify.py` from the same directory. A successful run prints `VERIFY_OK` and matches `verify_output.txt`.

The proof of the universal theorem is in `RESULT.md`; the finite experiments only test specific parameters and do not claim to enumerate all parameters or characteristics. The 1997 original paper's whole-document contents were not accessible and are not represented as inspected.
