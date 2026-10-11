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

# Verification notes

The exact standalone checker is `verify.py`. Running `python verify.py` prints all tested rational parameters and ends with `ALL_EXACT_CHECKS_PASS 9 parameter values, 6 alternative ellipsoid scales each`. It uses `fractions.Fraction` and exhaustive intersections of triples chosen from the twelve defining half-space boundaries; all fourteen vertices are recovered at every tested parameter. It checks the advertised rational expression, explicit quadratic contact vectors on the boundary, and comparisons against six alternative invariant positive quadratic forms at each test point.

The actual mathematical proof additionally verifies the symmetry averaging for **all** real Euclidean pullbacks, complete vertex and facet extremization for **every** positive parameter, and global optimization over the remaining real variable. No numerical experiment establishes those universal quantifiers, and no claim is made for metrics outside the stated family.

This is same-model scientific review, not independent audit.
