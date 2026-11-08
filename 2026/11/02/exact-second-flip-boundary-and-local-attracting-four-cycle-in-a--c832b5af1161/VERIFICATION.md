---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For K_mu(x)=mu*x*(1-x)/(1+x), 0<mu<=3+2sqrt(2), verified K^2-x rational factorization with quadratic primitive-cycle factor Q, discriminant (mu^2-1)(mu^2-4mu-1), unique two-cycle for mu>2+sqrt(5), and multiplier 1-(mu^2-1)(mu^2-4mu-1)/(2mu^2). The strictly decreasing multiplier crosses -1 uniquely at mu_f=1+sqrt(2)+sqrt(4+2sqrt(2)). The exact negative Schwarzian of K gives positive cubic normal coefficient of K^2 and transverse flip, yielding exactly one local attracting 4-cycle for mu>mu_f near threshold with two explicit distinct square-root amplitudes. Independently recalculated symbolic identities, quartic radical and numerical amplitude values.

## originality

PASS

Best-of-knowledge exact claim-vs-prior comparison after this run’s independent Resultary search and primary-source checks. The exact multiplier and negative Schwarzian + transverse unfolding complete the missing family-specific steps that are not entailed by prior numerical observations; generic flip theory alone is insufficient to calculate these numbers. Priority qualified: An unindexed appendix to earlier rational-map bifurcation studies could have derived the same algebra; no claim of globally exhaustive priority.

## value

PASS

It converts a numerical published second period-doubling threshold of a particular rational unimodal map to a closed radical, proves exact two-cycle stability phases and computes local normal-form amplitudes and return multiplier; the supercritical classification is an analytically useful sharpening, not a mere rounded numerical table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
