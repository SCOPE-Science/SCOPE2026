---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For every fixed fully supported nonuniform q-ary law, exact cell increments u=q^(-n),v=product(p_digit) give D_n=2-L_n=E_U phi(exp(S_n)). Since M’(0)=-D(U||P)<0 and M’(1)=D(P||U)>0, strict convexity fixes unique s* in (0,1), rho<1 and centered positive-variance tilted increments. The precise change of measure D_n=rho^n E_pi g(S_n) and per-step gain G_n=rho^n E_pi psi(S_n) follow from the finite formula. Strict concavity of phi and nonuniform weights makes psi positive. g and psi have exponential tails, allowing classical Stone/local lattice LLTs and positive uniformly summable periodic profiles. Explicit integration by parts evaluates int(g)=2^(s*-1) B((s*+1)/2,1-s*)/s*; int(psi)=(1-rho)int(g), and the arithmetic shifts give H(theta)=A(theta)-rho A(theta+a). Thus both D_n and G_n have the asserted sharp rho^n/sqrt(n) laws. Independently recomputed 7-file tree and verified finite levels with direct and multinomial methods, Chernoff tilts, beta quadrature and periodic gains. Uniform p and zero digit weights are correctly excluded; finite numerics are not a proof of the infinite theorem.

## originality

PASS

The motivating 2023 article already proves the exact finite polygonal arclength and its limit 2, but asks for a quantitative step gain in Section 5.1. The assessed result adds the all-positive-biased-law sharp Chernoff exponent, n^-1/2 correction, evaluated beta factor and indispensable arithmetic-phase coefficient. Real Resultary searches and primary-source mathematical comparisons did not identify equivalent or stronger published coverage; standard LLT/Chernoff theory supplies inputs, not the assembled geometric asymptotic. Best-of-knowledge only, with residual risks explicitly recorded.

## value

PASS

It resolves the natural explicitly posed quantitative refinement question for biased-digit CDF polygonal arclength, throughout the full fixed fully supported nonuniform q-ary family, rather than merely computing finite instances. The sharp rate identifies the Chernoff affinity and has a nontrivial square-root penalty; a positive periodic correction is essential in arithmetic cases. The result offers a mathematically reusable leading law and distinguishes effects of digit bias from finite numerical tables.

The dated certificate retains the supplied scientific assessment, sources and limitations.
