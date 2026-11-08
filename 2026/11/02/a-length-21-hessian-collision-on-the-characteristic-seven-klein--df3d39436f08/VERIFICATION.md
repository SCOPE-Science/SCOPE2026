---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For F=X^3Y+Y^3Z+Z^3X and G=X^5Z-5X^2Y^2Z^2+XY^5+YZ^5 over Z_(7), direct differentiation gives det Hess(F)=-54G. On Z=1 modulo 7, resultant_y(f,g)=-x(x-2)^21; translating u=x-2,v=y-4 gives affine Groebner leading monomials u^2,uv^7,v^15. Adjoining v^14 isolates the fat point, where leading monomials u^2,uv^7,v^14 give length 14+7=21. Independently recomputed maximal-ideal filtration ranks 21,20,18,16,14,12,10,8,6,5,4,3,2,1,0 and Hilbert-Samuel sequence (1,2,2,2,2,2,2,2,1,1,1,1,1,1). The other affine vertex [0:0:1] and two infinity vertices are transverse, so special length 24; relative projective zero-dimensional CI is finite torsion-free over DVR, hence flat degree 24; fat local CI is Artin Gorenstein. Original verify.py inspected; independent SymPy algebra emits FOUR_HESSIAN_EXACT_PASS. This is coefficientwise plane model, not smooth good reduction.

## originality

PASS

The inspected prior primary mathematics supplies the classical framework, but none of the materially compared statements implies the full claimed specialization; best-of-knowledge priority, with explicit risks. Rephrasing as naive coefficientwise specialization of a 24-point Hessian flex scheme is essential: it is distinct from the smooth good-reduction Weierstrass-point scheme. The local algebra and its 21-dimensional filtration are not the already-known generic flex orbit. The classical global results identify the object but not the local Groebner algebra in inspected relevant sections. An earlier specific reduction computation could dominate; residual priority risk noted.

## value

PASS

The classical Klein quartic has 24 flex intersections and a distinguished prime of bad plane reduction. The exact 21-point collision, local Hilbert–Samuel function and finite-flat specialization give concrete scheme-theoretic degeneration data that global point counting or identifying the singular point alone does not supply.

The dated certificate retains the supplied scientific assessment, sources and limitations.
