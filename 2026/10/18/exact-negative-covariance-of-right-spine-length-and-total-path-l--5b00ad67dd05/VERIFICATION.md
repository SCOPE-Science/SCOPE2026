---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

Root-rank splitting gives P_n=P_{k-1}+P'_{n-k}+n-1 and R_n=1+R'_{n-k}, not an independent-path approximation. With a_n=2(n+1)H_n-4n and b_n=H_n, the mixed recurrence e_n=a_n+n^{-1}sum_{r=0}^{n-1}[e_r+(a_{n-1-r}+n-1)b_r] yields E(z)=(1-log(1-z))/(1-z)+(2log(1-z)^2-1)/(1-z)^2. Coefficient extraction produces c_n=3n+H_n-2(n+1)H_n^(2) including c_1=c_2=0. The difference c_(n+1)-c_n=3-2H_n^(2)-(n+3)/(n+1)^2 is negative from n=2 by the monotonicity of the complementary positive term; H_n^(2)->pi^2/6 proves the slope, and the established BST path-variance leading term with Var(R_n)=H_n-H_n^(2) proves the correlation scale. Finite partition-function differentiation with theta^{R_n} proves local record-bias sensitivity, not monotonicity for all theta. Independently constructed all BST permutations n=1..7 matched exact rational covariance. No numerical extrapolation was used for any unbounded quantifier.

## originality

PASS

Best-of-knowledge originality: explicit cross-statistic theorem not established by the inspected primary statements; compare four mathematical implications below. No guarantee of absolute historical priority.

## value

PASS

Right-spine length is the upper-record count controlling a natural record-biased insertion model, whereas total path length is insertion/comparison cost. Their cross-moment has a nonobvious negative sign despite nonvanishing O(n) covariance and vanishing normalized correlation; the exact coefficient gives a calculable local sensitivity of search cost to record bias. These two natural tree statistics have different fluctuation scales; deriving their interaction, rather than repeating marginal path-length moments, is a useful finite-n structural statistic.

The dated certificate retains the supplied scientific assessment, sources and limitations.
