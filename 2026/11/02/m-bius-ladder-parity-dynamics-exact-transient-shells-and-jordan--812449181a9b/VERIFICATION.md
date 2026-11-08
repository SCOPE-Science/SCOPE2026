---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For binary synchronous neighbor XOR on the simple Möbius ladder M_(2n), the update is multiplication by z+z^-1+z^n in GF(2)[z]/(z^(2n)+1). The only zero eigenfactor is z²+z+1, present exactly when 3|n; local valuation yields four length-one zero Jordan blocks for odd n and two length-2e blocks for even n (e=2^v2(n)). Exact kernel growth yields transient shells and polynomial gcd yields all periodic orbit counts. The proof independently derives the untwisted prism comparison. Independent GF(2) matrix ranks for n=3..14 matched predicted kernels and fixed-state trichotomy.

## originality

PASS

Polynomial linear-cellular-automaton methods and ordinary Rule150 divisibility-three facts are established; the explicit twisted Möbius ladder nilpotent Jordan partitions, all transient-shell counts, and sharp comparison with the untwisted prism form the assessed contribution.

## value

PASS

The twist changes Jordan chain lengths while preserving recurrent-state counts, a structurally informative distinction between graph topology and transient linear dynamics; exact all-size finite-dynamics classification is a natural invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
