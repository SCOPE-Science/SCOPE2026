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

Inspected 1D exact UTR-Adaptive Strategy 4.1 update on f_p(x)=|x|^p/p with p>=3 and rho floor>0. Gradient magnitude a^(p-1), Hessian (p-1)a^(p-2), and ratio H/sqrt(|g|)=(p-1)a^((p-3)/2) drive branch selection. For p=3, the two branch radii and constrained Newton solutions yield q3(rho)=1/2 (rho<=1), 1-1/(2rho) (1<rho<=2), and 1-1/(4rho) (rho>2). At p>3 branch H/sqrt|g| ->0, radius a^((p-1)/2)/(4rho) is eventually active, and descent acceptance tends to 1/4>eta; accepted updates lower rho to rho_min. Exact recurrence a_{k+1}=a_k-a_k^((p-1)/2)/(4rho_min) gives a_k ~ [8rho_min/((p-3)k)]^(2/(p-3)) by inverse-power telescoping. Formula describes local infinite zero-tolerance update, not a fixed positive-stopping-tolerance run. Independently checked branch thresholds and recurrence algebra and inspected provided verification.py; finite checks alone do not establish asymptotics.

## originality

PASS

The algorithm and quadratic local rate at nondegenerate optima are prior Jiang et al. material. This claim investigates exact degenerate power minima with f_p''(0)=0, outside positive-definite Hessian theorem assumptions. The cubic-versus-higher flatness branch boundary, rho-floor dependent contraction and polynomial leading constant are not implied by that theorem as stated. Related Bregman/regularized Newton papers use different updates.

## value

PASS

A sharp, explicit degeneracy threshold for a standard adaptive trust-region algorithm is useful for diagnosing its limits at flat minima: cubic flatness contracts linearly but higher powers show quantified polynomial stall, with exact dependence on parameter floor. The test family is natural and the asymptotic rate is nontrivial beyond mere substitution, despite the one-dimensional and pre-termination restriction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
