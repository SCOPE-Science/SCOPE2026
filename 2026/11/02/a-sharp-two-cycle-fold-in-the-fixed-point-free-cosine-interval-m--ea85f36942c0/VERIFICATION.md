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

For 1/4<=a<1/2, 0<c<1/2, switch b=1/2, the left branch exceeds the diagonal by at least a-1/[8(1-a)]>=1/12 and the right branch is strictly below it. Increasing branches prohibit a primitive cycle wholly inside one branch. Every primitive 2-cycle is equivalent to x=c C_a(x), x in (theta_a,1/2), C_a(x)=cos(pi(1-a)cos(pi*x)). For t=cos(pi*x), sign(C_a second derivative)=sign(t tan(k*t)-k(1-t^2)); its derivative is positive on (0,pi/(2k)), so exactly one sign change. H=C-xCprime first decreases then increases, H(theta+)<0, H(1/2)=1; hence Q=x/C has exactly one nondegenerate minimum c*<1/2. At the two roots lambda=c Cprime is >1 on the lower and in (0,1) on upper. Taylor expansion of c C-x gives sqrt(c-c*) splitting and correct multiplier coefficients. Inspected verify_cosine.py checks five parameter slices but no sampled scan is used to justify all-parameter uniqueness.

## originality

PASS

Exact global primitive-two-cycle count, analytic threshold and attracting/repelling fold on this fixed-point-free cosine subfamily are not implied by the numerical phase plots in the source cosine example. The generic local saddle-node normal form does not give the unique global turning point. The related 2024 family-construction paper was not fully read, so assessment is priority-qualified.

## value

PASS

The cosine no-equilibrium map is a concrete dynamical model with numerical bifurcation charts but lacked an exact 2-cycle count. Locating the unique fold and its universal square-root scaling and stability regions is a motivated structural classification, not just a renamed saddle-node lemma.

The dated certificate retains the supplied scientific assessment, sources and limitations.
