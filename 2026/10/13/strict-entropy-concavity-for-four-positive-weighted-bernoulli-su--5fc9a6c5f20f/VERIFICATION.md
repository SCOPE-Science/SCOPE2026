---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For all four positive real weights and common p in (0,1), normalize/order weights. Every subset-sum collision is a dot product with one of 40 normals in {-1,0,1}^4 modulo sign. Intersections of up to three normals and ordered-simplex boundary planes yield 12 distinct exact-rational vertices and exactly 23 attainable positive collision coefficient patterns. Independently executed classify4.py and verified 40 normals, 12 vertices, 3327 subspaces, 23 patterns, all with representatives <=8. Every resulting probability q_s(p) is a four-term Bernstein polynomial; H″=-Σ_s (q″log q+(q′)^2/q). For 0<p<=1e-4, q_s>=p^4, Σ|q″|<=192, and Fisher-information lower bound 4(1-p)^2/p imply strict negative curvature. On [1e-4,1/2] the supplied complete outward-rounded mpmath.iv interval checker rigorously encloses H″ for each pattern, bisecting undecided boxes until strict negative upper bounds; independently ran full code with mpmath 1.3.0 and reproduced 1,129 visited interval nodes across 23 patterns, maximum depth five. Symmetry H(p)=H(1-p) gives (1/2,1), endpoint continuity strict concavity on [0,1]. Computational continuum certificates are substantive proof ingredients, not finite sample extrapolation.

## originality

PASS

The 2026 Neunhäuserer preprint states the full positive-weight Bernoulli concavity conjecture and proves certain extremal weight regimes; MathOverflow answer updated September 15 counts the same 23 four-weight collision patterns but proves only seven analytically and numerically tests the rest. The current work supplies reproducible rigorous interval certifications of all 23, strengthening prior numerical experiments. Shepp–Olkin equal-weight result does not imply arbitrary unequal weights with collisions. Best-of-knowledge risk: subsequently updated preprints or unindexed discussions may supply proof.

## value

PASS

A concrete open conjecture stage (four weights), naturally motivated collision-pattern boundary, rigorously resolves all positive weights with uniform strictness. The 23-pattern exact combinatorial exhaustiveness and outward-rounded interval certificate are nontrivial; not merely numerical sampling or classical unweighted entropy concavity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
