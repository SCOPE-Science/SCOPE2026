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

The conditional mean given equilibrium age is zero, the conditional variance is q+(v-q)Z, and the conditional fourth cumulant is kappa_R Z^2 because independent Gaussian noise contributes zero fourth cumulant. Thus the mixture contributes three times the variance of the conditional variance, yielding exactly kappa_R L_2+3(v-q)^2(L_2-L_1^2), including D=0. Uniform and exponential ages give the displayed F functions. For tau>0, sinh(tau)>tau and the positive polynomial difference tau^2(24tau+7) establish the strict gap. The derivatives are positive and endpoints 0 and 1 are unattained at finite positive period, so the stated equality and threshold cases are exhaustive. An independent replay gave the no-diffusion binary roots 2.224744871391589 and 2.984704585357887. At tau=5/2, the Poisson value is a^4/132, while the deterministic value is negative since tanh(5/2)>5/6. Ordering refers to normalized cumulants; positive attenuation preserves each sign but not the numerical ordering of the original values.

## originality

PASS

Pass for the strict equal-mean comparison of the two normalized fourth cumulants, the resulting exact crossing classification including the deterministic protocol, and the opposite-sign example. The renewal-age framework and Poisson harmonic moment formulas are existing machinery, not distinct findings here.

## value

PASS

The renewal-reset literature motivates evaluating protocol sensitivity at equal mean; the reset law and mean waiting time alone do not determine even the sign of the stationary fourth cumulant. The strict comparison and a simple opposite-sign example give a mathematically precise distinction between two standard protocols, with exact thresholds rather than an isolated numerical case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
