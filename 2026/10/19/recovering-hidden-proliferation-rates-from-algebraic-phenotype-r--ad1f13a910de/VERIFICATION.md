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

The nonnegative off-diagonal terms preserve strict positivity, and U'=U z^p a(t), where a(t)=r^T y(t) lies between the positive minimum and maximum rates. The upper bound on U' prevents a finite-time hit of U=1, and the lower bound forces U to tend to 1. Normalizing gives w'=Qw+z^p H(y), with w=y-pi and H(y)=diag(r)y-(r^T y)y zero-sum and bounded on the simplex. An irreducible finite generator has exponential semigroup decay on the zero-sum space, without reversibility; convolution with the vanishing bounded forcing gives w to zero. Thus (z^{1-p})'=(p-1)(1-z)a(t) converges to (p-1)rbar and integration gives z^p asymptotic to a positive constant times t^{-p/(p-1)}. In the Duhamel integral divided by z(t)^p, the ratio z(t-v)^p/z(t)^p tends to 1 at fixed v and is bounded for 0<=v<=t/2 by the power asymptotic. For v>=t/2, the contribution is O(exp(-gamma t/2)/z(t)^p), hence vanishes. The limit is L=integral of exp(Qv)H(pi) from zero to infinity; multiplying by Q shows QL=-H(pi) and the zero-sum normalization gives uniqueness. Rearrangement with pi_i>0 yields the claimed inverse for known Q. It also handles equal rates, when L=0 and the mass signal alone supplies the common rate. The asymptotic for z gives the log slope. The sample has L_1=1/4 and z~1/(2t), so the t^2-composition coefficient is 1/16. The frozen checker was read, not executed; it uses numerical tolerances for linear residuals and prints rather than asserts an asymptotic-error tolerance. The limits rest on the analytic proof.

## originality

PASS

The inspected predecessors cover the uniform-modulation model, stationary-profile convergence and switching memory, not a first-order forced response at an algebraically approached capacity together with an inverse based only on leading asymptotic measurements. The credible distinction is that combined result for the flat brake, not the equilibrium, the normalized model, the abstract Poisson equation, or identifiability from a full differentiable trajectory. The comparison supports provisional distinctness, not priority certification.

## value

PASS

The stationary composition erases rate differences, but the first forced correction recovers the contrasts and the scalar clock recovers the missing common component. This is a useful distinction between what equilibrium and leading relaxation reveal in a natural population model, including nonreversible switching. It is not a claim that differentiating an entire observed trajectory is hard or that estimating the vanishing signal is stable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
