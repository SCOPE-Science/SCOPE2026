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

For a fixed real invertible symmetric indefinite A, Gaussian radial cancellation gives the uniform spherical direction and the core norm v/|q|, where v=||Au||² and q=uᵀAu. Indefiniteness gives a nonempty zero set; invertibility makes its tangential gradient 2Au nonvanishing there. The zero set is compact and regular (counting measure when n=2), with a regular neighborhood by compactness. For h=q/v the absolute reciprocal tail is the mass of |h|<1/t; its smooth level density at zero is C(A)/2 because |grad h|=2/||Au|| there. Integrating on both sides and sandwiching the residual by the core norm plus or minus ||A|| gives the stated coefficient. Integrating the tail gives exactly 0<p<1; definite q is separated from zero. In the specified hard-rejection rule, weighted coarea for q gives F(0)=C(A)/2 and F(±s)=F(0)+O_A(s); integrating the accepted pole down to ε||A|| gives C(A) log(1/ε)+O_A(1), and the pointwise bounded residual/core difference preserves it. The two-dimensional trace and determinant give E=ab/|q|; the arcsine law and the two spherical latitudes give the displayed special cases. The analytical checks replay at RESULT.md lines 36–74; VERIFICATION.md and the inspected verify.py cover finite examples, not the universal theorem, and were not executed. No conclusion for singular A, higher sketch rank or other stabilization follows.

## originality

PASS

Known indefinite-core instability, the divergent-mean phenomenon, and special-case reciprocal-form laws are not credited as new. The supported distinction is the explicit geometric residual-tail coefficient for every fixed nonsingular indefinite real symmetric A with one isotropic probe and the matching risk law for normalized hard rejection of the scalar core. The strongest inspected overlapping statements do not give this combination or the general rank-one coefficient by specialization. This is a bounded literature finding, not a priority certification.

## value

PASS

The instability is a practical issue for indefinite low-rank sketches. The geometric coefficient determines the rate of rare large residuals and quantifies the deterioration of expected error as the specific safeguard is removed, with the same scale in both observables. This goes beyond a tiny failure example or the fact of an infinite mean, without implying advice for other algorithms or sketch ranks.

The dated certificate retains the supplied scientific assessment, sources and limitations.
