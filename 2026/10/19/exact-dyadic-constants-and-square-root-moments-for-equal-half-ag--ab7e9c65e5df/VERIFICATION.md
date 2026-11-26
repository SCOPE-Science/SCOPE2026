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

Starting with c_n=A_n/n!, the positive recurrence is majorized by H=z+2H², giving radius R≥1/8, and G=G²+2G(z/2). For real 0<z<R the derivative identity gives G<1/2 and z≤G−G²≤1/4. At the finite positive radius R, Pringsheim and the implicit function theorem force G(R−)=1/2: otherwise the implicit derivative 1−2G would not vanish there. The holomorphic half-argument is still inside its convergence disk, and G(R/2)=1/8. Evaluating at consecutive half-arguments yields the stated orbit; the derivative at zero gives lim 2^j a_j=R. Iteration of (1−2G(z))G'(z)=G'(z/2) gives G'(R/2)=1/P. The orbit decreases at least geometrically and the tails of the two products are bounded below by 1 minus the corresponding sum, giving the published brackets and P>0. For z on |z|=R other than R, the arguments of the n=1 and n=2 terms cannot agree, so |G(z/2)|<G(R/2); the discriminant has no competing zeros. Its simple zero at R has linear term (4R/P)(1−z/R). The square-root branch continues to a dented disk, yielding coefficient amplitude sqrt(R/P)/(2 sqrt(pi)) by square-root transfer. Thus the rate R^(-1) refers to A_n/n!; the moments themselves include n!. The displayed digits and stated width bounds were independently certified with rational Machin bounds for pi, dyadic-grid orbit bounds and rational integer-square-root brackets (python3 /workspace/branches/audit_constants.py; widths about 5.4082e−47 and 5.0032e−47). The frozen verifier was read but not executed; its decimal display is not the basis for the rational certification. This is a formal moment-series result, not a proof of a pointwise density tail or of stationary-law existence.

## originality

PASS

The recurrence, dyadic logistic iteration and formal square-root coefficient shape are already in Krapivsky. The supported distinct claim is the identification and certified approximation of the two constants and the rigorous coefficient asymptotic, with the dominant singularity located and competing singularities excluded. The strongest inspected indexed same-model record concerns convex order and a distributional fixed point, not these constants. The judgment does not assign priority for the already known formal shape.

## value

PASS

Equal halves are the canonical deterministic split, and the source explicitly left the normalized moment rate and leading amplitude unknown. The result gives exact computable constants with effective error control and resolves whether the formal moment shape is the actual leading coefficient asymptotic, rather than just providing a fit. This supplies quantitative moment growth usable without assuming a density tail; it is more than a recurrence substitution or a generic invocation of singularity transfer.

The dated certificate retains the supplied scientific assessment, sources and limitations.
