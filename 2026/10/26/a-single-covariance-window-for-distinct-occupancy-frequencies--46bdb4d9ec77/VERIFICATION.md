---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Exact multinomial one-box and ordered two-box probabilities give E[N_r], E[N_s], E[N_rN_s] and normalized cross moment T_n. Algebraic cancellation yields T_(n+1)/T_n=m(m−2)/(m−1)²·[1+rs/((n+1)(n+1−r−s))], which strictly decreases for n≥r+s, m≥3, r≠s≥1. Hence T_n is positive strictly log-concave and tends to zero, so {n:T_n>1} is a single finite interval, exactly the positive-covariance indices. Exact rational checks confirm signs at (m,r,s;n)=(10,1,8;9,20,70) are −,+,−. Expanding log T_n at n/m→λ yields m(T_n−1)→r+s−1−λ−rs/λ, and E N_j/m→e^(−λ)λ^j/j!, giving asserted limiting covariance sign diagram. Independent exact multinomial enumeration/ratio tests passed; finite checks do not prove all parameters.

## originality

PASS

The assessed new statement, not its model/semantic/occupancy/antipower/divisor premises, survives direct implication comparison to the inspected primary literature. The full text of Sevastyanov–Chistyakov (1964) and Harris–Park’s companion 1971 linear-combination paper was inaccessible: exact finite log-concavity might occur there. Best-of-knowledge priority is qualified, not certified by unsuccessful searching.

## value

PASS

Frequency-of-frequency covariance is a core statistic in occupancy and sampling. A sharp upper bound of two sign reversals, unique positive interval, explicit attaining example, and large-box phase interpretation are intrinsic structural statistics rather than a routine moment table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
