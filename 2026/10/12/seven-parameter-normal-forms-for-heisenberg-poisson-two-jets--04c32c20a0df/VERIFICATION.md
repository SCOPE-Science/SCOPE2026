---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

On A=K[x,y,z]/(x,y,z)^3 with fixed first-order {x,y}=z, every degree-two correction P,Q,R lies in M=Sym²(K³), yielding 18 coefficients. Jacobi is equivalent to three independent constraints 2q1+r2=0, q2+2r4=0, q3+r5=0 (each has a unit coefficient even in characteristics 2 and 3), hence a 15-dimensional affine solution space. Tangent-identity substitutions x_i→x_i+H_i act by P→P+DxHy−DyHx−Hz, Q→Q+DxHz,R→R+DyHz, with Dx=z∂y,Dy=−z∂x; P image has rank6, while fixing P=0 leaves two independent z² corrections, total rank8. Choosing P=0 and Q,R z²-free gives the advertised unique seven coordinates (a,b,c,d,e,f,g), so Fq has q^15 brackets and q^7 framed orbits each q^8. Independent Jacobi/gauge matrix computation over primes 2,3,5,7,11 found ranks (3,8) and each normal form has zero Jacobi obstruction. The proof uses exact polynomial identities with unit pivots, not finite-characteristic extrapolation; char2 alternation is essential. Includes explicit fixed first-order assumption, not classification by full Aut(A).

## originality

PASS

Best-of-knowledge priority judgment based on direct statement/implication comparisons with specified inspected sources, published semantic search and alias checks; neither the source names nor negative searches by themselves demonstrate novelty. The claim was compared as both a Poisson jet/gauge section and the Lie-algebra cohomology H²(h3,Sym²h3), not merely by title. No retrieved source supplied same numeric ranks or concrete normal forms.

## value

PASS

The exact framed deformation fiber and seven-dimensional gauge quotient for a natural ten-dimensional cube-zero algebra are natural local Poisson invariants. The explicit normal form, uniform behavior in every characteristic and cohomological dimension H²(h3,Sym² h3)=7 fill a concrete gap beyond general orbit-method frameworks; the result is not a relabeling of a dimension-three Poisson classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
