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

At size m the retained and deleted root-parent arrivals have exclusive increments and conditional probabilities pC_m/m and (1−p)C_m/m. With alpha=(1−p)/p, D=B−alpha(C−1) is a mean-zero martingale with conditional increment variance alpha C_m/m. Summing telescopes to Var(D_n)=(1−p)(mu_n−1)/p². The cross increment Delta C Delta D contributes −(1−p)mu_m/m, so h=E[CD] divided by mu decreases by (1−p)/(m+p); this gives the negative harmonic correction in the exact covariance. The rising second factorial product C(C+1) is multiplied in expectation by 1+2p/m, giving E[C²]=2Q−mu. Conditional variance for the Bernoulli increment gives v_(m+1)=(1+p/m)²v_m+p mu_m/m−p²(v_m+mu_m²)/m²; substitution gives the claimed difference of the normalized covariances with sign q_m−p/m, where q_m=v_m/mu_m². The latter difference strictly increases by the nonzero increment variance of C/mu and the strict decrease of p/m. Starting with Cov at n=2 equal to −p(1−p), the normalized covariance first decreases (one possible flat step at a negative value), then increases to infinity by gamma ratios. Thus there is exactly one reversal and at most one zero. The same ratios give V_p>0 from q_2>0 and monotonicity. For the correlation check, with the proof's u and w and s=sqrt(1+2u+w), rationalization gives the exact deficit (w−u²)/(s(s+1+u)). The denominator tends to 2 and u²=o(n^−p); inserting Var(D_n) and v_n gives the stated positive limit. Neither variance degenerates for n≥2 with 0<p<1: all-retained and all-deleted configurations already give different C_n and B_n values (for B_n take a star on the all-deleted event).

## originality

PASS

Credit the established root-cluster law, moments and mutation/urn machinery. The distinct October result is the exact fixed-size covariance for the count of immediate daughter components, its unique sign reversal, and the sharp correlation deficit. The strongest indexed comparison is a later-dated joint-law result on exactly the same pair; it determines the covariance and shares exact residual moments, but the catalogue dates do not make it prior coverage of the frozen record. The older inspected primary sources do not supply the relevant boundary-component cross moment or sign/rate theorem.

## value

PASS

At each arrival root growth and daughter-component creation compete, but cumulative fluctuations share the random root growth rate. This natural joint boundary statistic admits a finite-size sign classification rather than just an eventual-limit statement; quantifying the reversal and the residual decorrelation scale distinguishes both effects. The sharply normalized rate measures how well the boundary count tracks root mass, and is not merely the old root marginal.

The dated certificate retains the supplied scientific assessment, sources and limitations.
