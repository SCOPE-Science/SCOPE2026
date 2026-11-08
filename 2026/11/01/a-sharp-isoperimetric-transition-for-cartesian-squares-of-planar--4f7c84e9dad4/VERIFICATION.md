---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

For any nonempty-interior planar convex B with area A and perimeter P, the Euclidean R^4 product parallel volume splits by zero, one and two exterior factors. Quadrant disk integration gives S_{B×B}(t)=A²+2APt+(2pi A+pi P²/4)t²+(4pi P/3)t³+(pi²/2)t⁴. Independent symbolic normalization yields F_q(z)=z⁴/2+(8/3)z³+(pi+2q)z²+4qz+q² with q=4pi A/P². Independent SymPy discriminant computation recovers disc(F_q)=(8/27)q²G(q) with the source quartic G, and high-precision root q*=0.8766744290496891255567354... . An independent exact rational Bernstein computation over [0,1/2],[1/2,3/4],[3/4,7/8],[7/8,1] plus a rigorous pi interval checks G'<0 globally, not merely at sampled points; endpoint and rational bracketing give a single simple critical q. At q→0 the quartic splits into two distinct negative O(1) roots and two distinct negative O(q) roots, so four real roots on q<q*. At q>q*, discriminant negative gives two real roots and one conjugate pair; at the simple discriminant crossing exactly one double negative root. Positive coefficients preclude nonnegative real roots. Polygon quotient q_m=pi/[m tan(pi/m)] strictly increases; q5<.87<q*<.9<q6 proves cutoff between pentagon and hexagon. Source algebra and critical bounds were independently examined; all-convex-body conclusion is from analytic normalization, not numerical sampling.

## originality

PASS

Katsnelson, On H. Weyl and J. Steiner Polynomials (arXiv:0803.2346), Section12 Theorem12.4, already proves the Cartesian-product Steiner M-product and hence the quartic coefficients; these are credited as known. Henk–Hernández Cifre (2007) studies general root location and Henk–Hernández Cifre–Saorín (2011) determines the general possible-root cone, not the one-parameter real-root count for all equal planar Cartesian squares. Resultary searches for quartic equal-factor, regular-polygon root cutoffs and isoperimetric thresholds found no dominating published mathematical record. The root-type transition remains plausibly original as a natural specialization not explicitly implied by a prior root-count theorem; an unindexed computation is a residual risk.

## value

PASS

A natural four-dimensional convex-geometric construction reduces real Steiner-root topology of all equal planar products to a single geometric isoperimetric quotient. Its rigorously unique four-to-two real-root transition and exact regular-pentagon/hexagon boundary provide a nontrivial, independently useful classification beyond the classical product coefficient identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
