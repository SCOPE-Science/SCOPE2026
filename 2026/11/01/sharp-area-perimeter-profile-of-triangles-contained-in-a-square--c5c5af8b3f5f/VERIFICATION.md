---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

For each A in (0,1/2], compactness yields a maximizing triangle. Fixing ordinate coordinates and signed double area gives a 2-dimensional affine kernel of horizontal perturbations; moving a triangle with horizontal span <1 wholly into the square leaves a nontranslation feasible direction along which the perimeter is strictly convex, contradicting interior maximality. The same holds vertically. Thus normalized vertex coordinate extrema are 0 and 1. Coordinate orders reduce exactly to diagonal-edge Case I and the no-opposite-corner Case II. In I strict convexity along |s-t|=2A forces side endpoints, giving M(A). In II write q=st=1-2A and p=s+t in [2sqrt q,1+q]. The closed expression U(p)+V(p) is strictly increasing for q>=1/4 (p>=1) and strictly convex for q<1/4 (U second derivative positive since c=1-q>3/4, V second derivative positive); hence extrema at endpoints. Direct comparison shows p=1+q wins for 0<q<1/4; at q=0 endpoints represent identical three-corner equality orbits. Derivatives Mprime>0 and Mdoubleprime>0 and dihedral orbit counting yield 8 maximizers for 0<A<1/2, 4 at A=1/2. Independently checked rational equality witnesses and several Case-II inequalities; finite tests corroborate the continuum argument.

## originality

PASS

Best-of-knowledge mathematical implication comparison of actual primary material and published records. Novelty is provisional, with explicit unresolved historical-source risks. 

## value

PASS

The complete sharp all-area reverse-isoperimetric profile for Euclidean triangles inside a square is a naturally motivated tractable restriction of the active inclusion-constrained perimeter problem. The forced diagonal edge, strict convexity, endpoint orbit collapse and equality count are structural exact information, not an arbitrary finite gain.

The dated certificate retains the supplied scientific assessment, sources and limitations.
