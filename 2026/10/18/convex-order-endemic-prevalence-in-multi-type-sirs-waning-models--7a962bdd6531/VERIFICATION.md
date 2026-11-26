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

At I>0, summing the infectious balances gives sum s_j=1/R0. With x=R0 I, the other balances give i_j=xs_j and r_j=gamma h_j xs_j/(1+mu h_j), so conservation gives s_j=p_j g_x(h_j). Conversely these fractions have sum i_j=x/R0 when E g_x(H)=1/R0, and the susceptible equation follows from mass balance plus the other two equations. The scalar left side is continuous and strictly decreasing from 1 to 0, ensuring exactly one positive root for R0>1. The kernel has g''_x(h)=2 gamma x [mu+(mu+gamma)x]/[1+x+(mu+(mu+gamma)x)h]^3>0 for x,h>0. Convex order at fixed x and then strict decrease in x put the two roots in the asserted order; Jensen is strict for a nondegenerate spread of a point mass. For the stated two-point family, the sigma derivative at fixed x is m sqrt(p(1-p)) times g'_x(h_2)-g'_x(h_1), which is positive for every allowed sigma>0 regardless of p. At zero, using E Z=0 and E Z^2=1, F_sigma=0 and F_sigmasigma=m^2 g''_x(m); F_x=-C_0/R0^2 at x_0. The implicit-function formula for I=x/R0, with the factor 1/2 from Taylor expansion, gives the positive displayed coefficient. The denominator identity at x_0 is (1+mu m)R0, and no split p remains in the quadratic term. Independent replay: python3 /workspace/review_replay.py 5 uses the positive root of the two-class quadratic (not the supplied bisection checker), reproduces the three example values, and checks the leading coefficient at five p values by 65-digit arithmetic. This is a finite diagnostic; the derivative and equilibrium arguments establish the full claim. No uploaded scripts executed. The conclusion concerns the intrinsic reciprocals of type-specific waning rates and the stated homogeneous-mixing equilibrium, not realized lifetimes under turnover, empirical predictions, stability or transient effects.

## originality

PASS

The accessible primary preprint proves the same two-type monotonicity (including positive derivative for positive variation) on p>=1/2 and only reports simulations for p<1/2. It supplies the equivalent two-type equilibrium expression, not the proof of the missing range, finite-type convex-order theorem or quantified split-independent onset. The latter are the distinct supported contributions. The exact journal text was not verified; this is not a historical priority ruling.

## value

PASS

The analysis resolves a precise missing regime in an existing two-type prevalence comparison and makes the mechanism explicit through a strictly convex equilibrium kernel. It replaces an ad hoc comparison of two splits with a distribution-level ordering in the homogeneous-mixing setting, and quantifies the near-homogeneity change with a coefficient independent of the split. It makes no claims for other mixing mechanisms or epidemic dynamics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
