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

The proof in `RESULT.md` establishes the filtered PL homeomorphism using barycentric coordinates and the exact cyclic-orbit diameter identity. This checker is finite supporting evidence, not a substitute for the universal proof.

Run with `python3 check_cycle_fixed.py` from this directory. It uses the standard Python library, checks exact integer arithmetic, and contains no external dependencies.

Observed successful output:

```
ODD_ROTATION_ORBIT_DIAMETER_FORMULA 407813 VERIFIED
FIXED_SIMPLEX_FILTRATION_EQUIVALENCE 49472 VERIFIED
SIGNED_LEFSCHETZ_FIXED_EULER 202 VERIFIED
```

The first test verifies odd-order orbit diameter identities for all divisors of sizes three through one hundred. The second test compares all nonempty subsets of quotient orbit classes with their lifted original vertex sets for all thresholds up to the graph diameter when the quotient has at most eight vertices. The third compares signed reduced simplicial Lefschetz traces for rotation actions on small cycle powers to the reduced Euler characteristic of the predicted geometric fixed complex. The tests include the identity subgroup, singleton quotient orbits, even-order subgroups, odd-order subgroups, and threshold endpoints.

No independently performed audit or validation is asserted. Any future claim of priority would require external expert literature review.
