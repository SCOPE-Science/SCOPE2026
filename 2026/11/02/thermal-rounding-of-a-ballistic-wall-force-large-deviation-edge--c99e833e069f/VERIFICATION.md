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

On a fixed interval the reflection term gives S_T=A_T-(X_T-X_0), with error at most L pathwise. This proves speed-T exponential equivalence and equality of the SCGFs without any assumption about individual-wall independence. The tilted sign matrix has top eigenvalue -lambda+sqrt(lambda^2+v^2 q^2) with positive stationary overlap; independent Brownian motion adds Dq^2. For D>0 the derivative is onto and its derivative is strictly positive; for D=0 the Legendre formula holds, and the no-flip events supply the endpoint lower bounds separately. For the positive edge, let Q=(lambda^2/(vD))^(1/3), eta=lambda/(vQ), q=Qz. The exact scaled Legendre objective after subtracting lambda is sz-z^2-1/(sqrt(z^2+eta^2)+z). For each bounded s-interval choose fixed positive z_- and z_+ whose limiting scaled derivative F(z)=2z-1/(2z^2) lies strictly outside that s-interval. The exact scaled optimizer equation converges at both brackets, then uniformly between them, and is strictly monotone. This justifies uniform optimizer localization and convergence, not just a fixed-z expansion. Evaluating at s=0 gives z=4^(-1/3) and -3/2^(4/3). Symmetry, mobility scaling and the fixed-N rate by independent products follow. Independent golden-section maximization of the exact scaled objective at v=lambda=1, s=-3,0,3 and D=10^-3,10^-6,10^-9 corroborated convergence; for s=0 the scaled errors were 0.00498425, 0.0000499984, and 0.000000500000.

## originality

PASS

Credit the free telegraph SCGF, the Brownian addition, the zero-temperature wall-contact setting, and general reflected-process LDP methods as preexisting ingredients. The distinct claim supported by this comparison is the exact singular thermal crossover for the signed wall difference, including its compact-uniform profile and edge constant. Neither a contact-time transform at D=0 nor a free-current or mean-pressure formula states that limit. No verified equivalent or dominating result for the crossover was found.

## value

PASS

A reflecting RTP's net wall impulse is a natural force observable, and width-independence alone does not quantify how its ballistic support disappears. The two distinct scaling exponents, full profile and edge amplitude quantify precisely the nonuniform breakdown of the zero-noise approximation where Gaussian central fluctuations are not predictive. The result gives more than the standard SCGF or a simulation fit.

The dated certificate retains the supplied scientific assessment, sources and limitations.
