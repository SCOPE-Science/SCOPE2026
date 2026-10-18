---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

PASS. At the exact RESULT.md snapshot, with a=x1,b=x4,p=x2+i*x3,q=x2-i*x3, the partials of F=(a²+b²+pq)²−4(a²b²+pq) give exhaustive alternatives p=q=0,b=±a or a²=b²=1,pq=0. The former are 2 main lines, latter 8 isotropic lines. The origin change P=p(4−2(a²+b²)−pq),Q=q,u=a−b,v=a+b has invertible Jacobian and yields PQ−u²v²: Jacobian (P,Q,u²v,uv²), radical (P,Q,uv), an embedded square-zero length-one uv class. Vertex substitutions reduce to U²+Vpq with radical squarefree Jacobian (U,pq,Vp,Vq), 3 components. Nonzero Hessian 3x3 minors −128t²(t²−1)² and −512t² prove ordinary transverse A1 at every other point. Reconstructed identities using independent SymPy checks, not only saved VERIFY_OK; global exhaustiveness is the algebraic case split, not finite sampling.

## originality

PASS

PASS (best of knowledge). Primary Example 8.1 prints the precise 4-dimensional quartic and its four real multi-exposure points, but no ten-line complex Jacobian stratification, formal triple branches or embedded length-one origin. Distinct Example 3.2 classifies a different 3-variable surface. Resultary searches found the target and other different quartics, no dominating explicit scheme classification. An undiscovered classical coordinate-equivalent quartic remains a risk.

## value

PASS

PASS. Singular-scheme support versus embedded nilpotent structure is a nontrivial intrinsic algebraic invariant of a natural geometric test example at the boundary of known discotope results. The exact normal forms at ten generic lines, four triple points and one embedded origin have use for resolution, deformation, and boundary singularity comparisons; this is not merely transcribing the input polynomial.

The dated certificate retains the supplied scientific assessment, sources and limitations.
