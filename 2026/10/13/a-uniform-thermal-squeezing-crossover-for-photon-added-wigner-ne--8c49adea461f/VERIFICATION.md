---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

PASS: Inspected pinned RESULT.md (blob 92af740b...) and reconstructed the normalized photon-added squeezed-thermal Wigner polynomial with gamma=cosh(2r), purity t=(1-q)/(1+q), and negative ellipse. Gaussian normalization and positive denominator (gamma+t) were checked. Ellipse rescaling with s=t exp(2r), z=t exp(-2r), sz=t^2 leads to the exact angular integral J(s,z) and path-uniform relative bound 12(exp(-4r)+t exp(-2r)+t^2); the positive lower bound for J(s,0) prevents division by a vanishing profile. Dominated convergence yields G(s)~1/s and G(infty)=kappa, a separate fixed-r argument gives N~t^2/(2cosh(2r)), and the pointwise monotone positive disk integral proves F(t)/t^3 decreases strictly. Independently evaluated the Gaussian ellipse integral (not the repository checker): kappa=0.23096817781411702; F(1)=0.21306131942526688; for (t,r)=(0.05,3), exact N=3.3218096750e-5 vs profile 3.3238050558e-5; at (0.01,4), N=2.5447933854e-7 vs profile 2.5448418359e-7; errors fall below stated bound. Numerical cases corroborate, do not prove infinite uniformity. The continuum proof's endpoint/large-s restrictions and exact normalization were inspected.

## originality

PASS

PASS best-of-knowledge: Hertz–De Bièvre already give the same model's finite-temperature Wigner polynomial and a fixed-temperature strong-squeezing negativity integral, and earlier Xu–Hu–Fan/Hu–Zhang study photon-added squeezed thermal states. These are not new. The assessed point is the uniform two-parameter singular crossover with explicit global relative estimate, a Bessel limiting profile, precise cubic coefficient and monotone envelope. The inspected primary full-text relevant sections/appendix do not state this joint path-uniform result. Named-source and Resultary searches found no theorem implying it; risk of an alternative derivation from the published fixed-temperature integral remains.

## value

PASS

PASS: Wigner negative volume measures a quantitative nonclassical optical resource, unlike binary Wigner-negativity existence. The sharp uniform crossover distinguishes quadratic purity decay for bounded squeeze from cubic decay when squeeze outpaces log(1/t), resolves order-of-limits ambiguity, and supplies a reusable uniform error rather than selected simulations. Restriction to ideal one-mode single-photon-addition states is stated; no multimode or loss claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
