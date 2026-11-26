---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Independently reproduced the exact census with `python /workspace/review-work/cubic_census.py` (SymPy 1.14.0 for the base ideals). The smoothness test here uses F4 and F8 with an exhaustive geometric argument, not the frozen finite-field check as a certificate: an absolutely irreducible cubic cannot have two distinct singular points by intersecting with their joining line, so if singular its unique point is rational. A reducible cubic with a rational line has a singular point at an intersection with the residual quadratic, rational or defined over F4 (or a repeated line). If geometrically reducible with no rational line, the factors must be three Frobenius-conjugate lines defined over F8, which meet pairwise over F8. In degree three and characteristic two, the vanishing partials imply the equation by Euler. Testing the partials at all projective points of these two fields gave 336 smooth forms. Enumerating subspaces by their sorted nonzero element sets gave 5544 pencils and 864 nets; explicit invertible coordinate actions gave disjoint orbits of the eight listed representatives covering precisely that set. Independent projective-chart elimination gave the unit ideal for six reps and no points at X=0 for any rep. For (522,395,101) and (579,271,229), the X=1 ideals have Y+Z^4+Z^3+Z² and Y+Z^5+Z² respectively, each with Z^6+Z^4+1. The latter is (Z³+Z²+1)², with no rational root in its cubic factor. The local doubling is curvilinear, of length two at each of the three geometric points, not the square of a point's two-generator plane ideal. Orbit sizes give 16 versus 848. The three cubics of a basepoint-free net define a projective morphism, and every curve in a fiber would have zero degree against its pulled-back line bundle O(3), impossible. Proper quasi-finite implies finite; the image has dimension two and the intersection pullback gives degree 9. This tests only the seven rational members per net. The submitted checkers were inspected, not executed.

## originality

PASS

Pass only the geometric-base refinement, which is the stated new assertion. The earlier exact census supplies the 864 nets, orbit partition and rational-point information, and explicitly stops at rational base points. A prior general construction already gives geometrically basepoint-free examples (hence degree-nine maps in this case); the new result is which nets are geometrically basepoint-free and the length and structure of the two exceptional orbits.

## value

PASS

An intrinsic scheme-theoretic invariant distinguishes nets that agree on simple rational data and explains exactly which maximal smooth systems induce finite morphisms by their defining cubic forms. The extra information is the number, placement in orbits and curvilinear multiplicity of the otherwise invisible base points, not a re-count of the ambient nets or a standalone degree computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
