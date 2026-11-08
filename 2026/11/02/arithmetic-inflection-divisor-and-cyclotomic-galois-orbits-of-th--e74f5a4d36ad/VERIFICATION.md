---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Read actual RESULT.md and verify_c48_flex.py. Smoothness from simultaneous first derivatives; Hessian det=108Y^2 Z(8X^3-Z^3) over Z[1/6]. Intersections: Y=0 gives four simple-in-Y curve points with Hessian order 2 and line contact 4; Z=0 gives four simple intersections with contact 3; 8X^3=Z^3 gives 12 simple intersections with Y^4=-9 zeta3^j/16. Total Hessian degree 4*6=24 accounts for all points. Hyperflex and infinity labels generate Q(zeta3) and Q(zeta8), respectively, whose compositum is Q(zeta24). Unit-group action on explicitly listed cyclotomic coordinates has orbit sizes 1,1,2,4,4,8; Frobenius acts by q mod24, and p^2=1 mod24 for p>3. Independent exact symbolic Hessian, Galois action and direct prime-field counts p=5,7,11,13,17,19,23 passed. Finite primes corroborate, not justify the all-prime formula.

## originality

PASS

Janasz 2024 already proves the four hyperosculating lines and 16 ordinary dual cusps for exactly this complex quartic; geometric counts are prior coverage and excluded from claimed independent novelty. The new assessed arithmetic claim is the full coordinate-level Q(zeta24) splitting field, explicit Galois permutation orbits, uniform Frobenius fixed-point counts over all F_q and quadratic splitting. The inspected original Section 3 does not give these arithmetic invariants. A classical inflection-field computation could be unindexed.

## value

PASS

An inflection divisor is a canonical genus-three curve invariant; its splitting field and Frobenius action distinguish arithmetic geometry absent from bare complex flex support counts. The exact field-of-definition and all-extension point-count table provide useful direct data for rational tangents and reductions of a distinguished high-symmetry quartic, not a recomputation of known four hyperflexes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
