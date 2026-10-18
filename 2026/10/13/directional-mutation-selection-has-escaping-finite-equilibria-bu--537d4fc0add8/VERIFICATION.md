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

For the stated bilateral positive Laplace kernel and bounded mortality with 0<mu_inf<mu_i and mu_i→mu_inf as i→+infinity, a nonzero l1 equilibrium would require a=lambda(1-m)>mu_inf from summation. The exact kernel Green identity (1+r^2)p_k-r(p_{k-1}+p_{k+1})=(1-r)^2 1_{k=0} forces y=Px to be eventually strictly concave because 1-a/mu_i<0; a positive summable sequence cannot be concave on a tail while tending to zero. Finite L_I=D_I^{-1}P_I is positive and similar to symmetric H_I; Rayleigh norm bounds give rho_I<1/mu_inf. Nested principal sections give monotonicity and trials on long right-hand blocks where mu_i≈mu_inf give convergence. Summed Perron eigen-equations yield the claimed quantitative escape bound. Perron simplicity and normalization establish uniqueness of finite positive equilibria exactly when lambda*rho_I>1. The lambda<=mu_inf boundary, no renormalization of truncated convolution, and nonmonotone rates (only finite-F bound, not one-sided) are correctly handled.

## originality

PASS

The exact theorem is not merely the existing confining-mortality Krein-Rutman threshold: here bounded mortality approaches an unattained infimum, and the right-tail concavity argument proves every lambda lacks a nonzero l1 equilibrium, while normalized finite Perron eigenvectors escape with an explicit finite-set bound. The motivating Pollett work introduces precisely this system and reports bounded-mortality drift without, in its available abstract, giving these quantified conclusions. Its full Section 6 was not accessible; novelty remains best-of-knowledge and this primary overlap is a material risk, not a false full-text noncoverage conclusion.

## value

PASS

The distinction between a positive limiting finite-section Perron radius and nonexistence of an l1 eigenvector addresses a genuine infinite-trait modeling problem: finite cutoffs give persistent positive mass but no stationary infinite profile. The sharp limiting birth-rate threshold for spurious finite equilibria and explicit mass-leakage inequality are separately useful when interpreting numerical simulations and spectral approximations, even without a trajectory-drift-rate theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
