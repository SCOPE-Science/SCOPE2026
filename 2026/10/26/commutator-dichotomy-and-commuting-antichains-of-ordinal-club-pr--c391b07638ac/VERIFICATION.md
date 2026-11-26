---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For a club D, the ceiling map is an increasing idempotent above the identity. It is continuous at limits in D by monotonicity and the bounds t ≤ π_D(t) ≤ α for t ≤ α in D; at a limit outside D it is constant on a left neighborhood by closedness, and successor ordinals and zero are isolated. Pullback therefore preserves continuity and eventual vanishing, and is a norm-one projection. Pullback reverses composition order. Distinct composite point maps are separated at any distinct output ordinals x < y by the difference of the indicators of the compact clopen sets [0,x] and [x+1,y], yielding exactly 2 by contractivity. If d = π_D(α) < e = π_E(α), then π_E(d) = e and the two compositions agree there exactly when e is in D; the symmetric case is identical after interchanging D and E. Testing at d in D\E and e in E\D gives necessity. In the construction all limit ordinals and all even tails belong to every club; each exclusive odd-tail member has a common even-tail successor. Choosing one from each pair of optional odd tails gives incomparable clubs in both directions. All checks are exact, over either scalar field; no numerical certificate is needed.

## originality

PASS

The canonical projections are known, the norm dichotomy is a direct point-evaluation fact, and the membership criterion is a simple instance of compatible ceiling maps. Credit the distinct club-specific classification together with the explicit incomparable commuting family, not a new norm phenomenon for composition operators or a new general theorem on idempotents.

## value

PASS

The norm argument alone is routine. The club-level criterion and simultaneous construction give a usable description of commuting pairs in a named Banach-space projection family and show that nesting is far from necessary, even for a continuum of mutually compatible distinct projections. This is a structural boundary, not a result about arbitrary commutators or a maximal cardinality assertion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
