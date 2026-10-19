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

Execute `python3 verify.py` with Python 3.8 or newer. The program uses only standard-library modular arithmetic. It enumerates **all** pairs of independent two-component vectors over each of the prime fields with three, five and seven elements. For every pair, it forms both common-image and common-kernel coefficient normal forms in split-octonion coordinates, implements both parenthesized octonion products directly, and checks that the constructed first-variable slice has rank exactly six with the stated zero-coordinate restrictions.

Expected counts for **each** of the two incidence types are 48, 480 and 2016 ordered pairs. Successful replay ends with `VERIFY_OK`.

The infinite-field proof does not rely on the finite enumerations: it rests on the displayed determinant and rank identities in `RESULT.md`. These tests do not inspect coefficient pairs outside quaternion composition subalgebras, characteristic two, or every finite extension field. No independent mathematical audit is claimed.
