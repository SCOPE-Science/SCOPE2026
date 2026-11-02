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

Run the accompanying `verify.py` with a standard Python interpreter. It uses no nonstandard package or downloaded data. It builds each finite unit group from the diagonal units and arrow coordinates and implements multiplication and inversion from the square-zero algebra formula, rather than identifying conjugacy classes from character data. It then independently counts conjugacy classes by generating conjugation orbits; a different calculation enumerates diagonal-torus orbits on additive-radical dual vectors. Both are checked against the theorem's predicted degree multiplicities. The degree-square sum is tested against the actual group order, and every conjugacy class cardinality is accounted for.

The program evaluates 19 fully exhaustive finite-field graph-pattern cases with \(q\in\{2,3,4,5\}\), up to four vertices and four arrows, including directed cycles, opposite arrows, repeated arrows and loops. Observed final line: `VERIFY_OK 19 direct conjugacy censuses, diagonal-dual orbit censuses, degree-sum checks`. These finite computations corroborate and stress-test the universal proof but do not certify an arbitrary quiver or all field sizes. No independent mathematical audit has been performed. No publication-priority certification is asserted.
