---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The arcsine change of variable gives a uniform full-branch zigzag with g_q^n=g_(q^n). Each of the j whole branches contributes p/Q to the joint event. The partial branch contributes min(theta,p)/Q if increasing, and max(0,theta-(1-p))/Q if decreasing. Subtracting p^2 gives the claimed sign and minimum, with zeros exactly at integer Qp and maximum magnitude bounded by p(1-p)/Q. At a one-step grid threshold the two label indicators transfer to constants, so iteration factors all word probabilities. The full branch cylinders shrink and have equal weights q^(-m), giving entropy log q and the claimed strict information loss at q>=3. The q=2,p=1/4 counterexample gives lag one 1/16, lag two zero. Endpoints are null. Independent exact backward-branch checks (210 cases, replay: python3 /workspace/check_frozen_math.py) corroborate the covariance, not the infinite proof. Frozen verification notes and checker inspected, not executed.

## originality

PASS

Credit the existing two-branch threshold-symbol probability analysis and the known generating tent partition; credit also general Chebyshev correlations for other observables. The distinct supported contribution is the all-integer-degree, all-lag explicit threshold covariance with exact zeros, combined with the lag-one rigidity classification for this threshold family. The closest inspected indexed divisibility criteria concern materially different systems, partitions and orders of independence. This is a best-of-knowledge verdict with named unresolved tent-map sources, not a historical priority claim.

## value

PASS

The threshold family is a natural observation of a full-branch chaotic map. The signed covariance with exact arithmetic zeros is a usable diagnostic: one adjacent-time covariance determines whether the entire observed process is Bernoulli, while isolated more distant zeros can be spurious. The all-lag formula and factor criterion add information beyond the known binary tent coding, exponential mixing bounds, or pairwise numerical tests.

The dated certificate retains the supplied scientific assessment, sources and limitations.
