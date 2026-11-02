---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

The cycle Laplacian eigenvalues are 4sin^2(pi k/N) on the mean-zero subspace. Cauchy–Schwarz for L+tI yields the diagonal Green upper bound; at a scalar stationary maximum the resolvent column has E(u)/||u||²=t, so the mixed-product upper bound is attained with exactly the asserted equality class. Periodizing the infinite-line resolvent and subtracting the zero mode gives g_N=coth(Ny)/sqrt(t(t+4))-1/(Nt), y=asinh(sqrt(t)/2). The inequality coth x<1+1/x plus tanh y<=y establishes C_N<1. The proof localizes all global maxima to t=sN^-2/3 with s in a fixed positive compact interval, then uniform derivative expansions and F(s)=s/8+2/sqrt(s) with F"(4)=3/64 give unique t_N and the stated coefficients. Independent optimization of the independently coded Fourier/Green formulas at N=3,5,8,20,100,1000,10000 confirms sharpness, including C_3=2/(3sqrt(3)) at t=3. The numerical checks do not establish uniform asymptotics.

## originality

PASS

PASS, qualified. Nagai et al. 2008 give the homogeneous gradient constant on the same mean-zero finite cycle, Yamagishi et al. 2012 prove fixed mass-parameter additive Green inequalities, and Ilyin–Laptev–Zelik 2014/15 prove the infinite Z multiplicative constant 1. None of their inspected results explicitly optimizes the finite mean-zero mixed product or derives its N^-2/3 three-term defect. The 2009 Nagai–Kametaka–Watanabe discrete Sobolev article could contain a dominating equivalent formula but full text was inaccessible even using authorized access; this is a material priority risk, not automatic failure.

## value

PASS

The finite mean-zero mixed embedding norm is an intrinsic sharp stability constant for periodic discrete gradients. The nonintegral 2/3 correction and three explicit coefficients explain zero-mode removal against lattice dispersion and locate exact Green extremizers; neither a textbook bound nor an arbitrary small numerical improvement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
