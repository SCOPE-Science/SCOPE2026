---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The successor rule computes both neighbor influences from the pre-spread state, then ignites exactly one remaining vertex unless terminal. Burned sets strictly increase, so exhaustive closure gives all and only legal terminal words. An independently written two-mask round search plus a multisource hypercube BFS reproduces all counts, run types, and distance histograms at orders 3–10. It confirms that the 8 nonconstant order-four words are exactly the singleton-minority words, and compares all two-boundary words at orders 5–10. At order ten the two alternating targets alone attain radius four; the independently enumerated path has radius three. For n≥10 fire from any given ignition cannot reach farther than its number of completed spreads: vertices 2, 4 and 6 evade all previous sources when ignited, in particular d(0,6)≥4 at round four. Their permanent alternating signs force a boundary on each of the four disjoint arcs in any completion. Balanced signatures form the positive switching class; switching carries the code by coordinate sign flips, giving the stated n minus radius plurality corollary.

## originality

PASS

The dynamics, switching-distance theorem and positive-path radius are prior results. A distinct complete-multipartite record covers the C3 base case; it has no bearing on cycles of order 4 or greater. No compared source covers the new cycle-specific codes, the order-ten threshold with a uniform witness, or the new cycle radii.

## value

PASS

For the first cyclic graph family the theorem identifies precisely when two-colour competition first permits four alternating domains, and separates a finite obstruction from a uniform larger-order construction. The exact onset code and its distinct radius quantify a genuine difference from paths; the radius is independently useful for determining worst balanced-signature plurality, not merely an arbitrary table of small instances.

The dated certificate retains the supplied scientific assessment, sources and limitations.
