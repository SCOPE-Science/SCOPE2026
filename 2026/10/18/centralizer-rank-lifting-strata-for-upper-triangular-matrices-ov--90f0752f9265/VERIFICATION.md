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

The commutator has zero diagonal and the three upper coordinates give the stated 3×5 map over R after removing a free scalar diagonal. The residue rank-two cases follow by testing when the third row is in the span of the first two: if both are nonzero this requires a≠0, b=−a and aw+uv=0, while a zero first or second row gives the other two cases. Their closures are the two coordinate 3-flats and V(a+b,aw+uv); the last is an irreducible dimension-three hypersurface in the four-space a+b=0 (primitive linear in w with coprime coefficients). Unit elimination leaves εK and gives field rank 2r+rank(K), with K the map induced by the first-order part from the residue kernel to the cokernel. At the rank-one residue w≠0 the kernel condition is t=−s, and K is the stated two-row matrix; rank one counts 2(q²−1) possibilities with exactly one nonzero row plus (q−1)² with both supported in the third column. At rank two with a=u=0 and b≠0, y12 and s are independently free in the residue kernel and K=0 requires a1=u1=0. When a=b=u=0 and v≠0 the relation y12=−ws/v leaves only one linear condition. Reversing indices and transposing gives the other zero-row stratum. In the nonzero-a stratum the residual row after pivoting on a,b is (a+b,−(aw+uv)/a,(−bw+uv)/b); its differentials impose exactly two independent conditions since the last two numerators differ by (a+b)w and a≠0. All these statements hold in characteristic two. Thus the two rank-two types give 3q²(q−1) and 2q(q−1) residue points, with q³ and q⁴ rank-four lifts per point respectively. Adding all lifts and restoring the scalar factor q² yields the seven coefficients in the Finding, positive for q≥2 and summing to q^12. Weighting by q^(12−r) gives the stated commuting probability.

## originality

PASS

The supported distinct contribution is the elementwise rank census and the explanation of its lift strata in the whole dual-number algebra. The same-ring chain-ring fixed-target formula in Resultary d19c392a0c2b directly covers the commuting-probability consequence for every q (not just the numeric examples), but counts ordered pairs at fixed target and does not give the rank histogram or the stratified lifts on specialization. Do not credit the probability as a distinct result in this comparison. No inspected primary source or indexed record showed the elementwise census by another formulation; the assessment is not a priority guarantee.

## value

PASS

The whole adjoint-rank distribution is a natural exact refinement of the commuting probability: it records how often a typical first argument has each possible number of commuting partners. The simplest nonfield length already has two lift patterns at the same residue rank, explained by the component intersections rather than by interpolation of prime-field counts. The classification and geometric cause of the exceptional lift counts are useful in their own right, independently of the previously covered probability consequence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
