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

PASS: Multiplication gives gh=hg iff A_gB_h-A_hB_g=0, exactly XY=0 for independent uniform 2m-square matrices. The count of rank-r X is q^{r(4m-r)} Phi_{2m}^2/(Phi_r Phi_{2m-r}^2); each has q^{2m(2m-r)} compatible Y. The normalized formula has exponent -3m^2-t^2 and the group order is q^{8m^2}; hence k(G)=q^{8m^2} cp. The uniform tail product Q_j=1-q^{-j}/(q-1)+O_q(q^{-2j}) yields the two-term summed expansion with domination q^{-t^2+2|t|}; it also holds after multiplying by |t|, giving total variation and mean. Under t->1-t the first odd-weight moment is Xi(q)/2, proving negative bias; nonzero mean is not claimed at finite m. Independently enumerated all q=2,m=1 matrix pairs: rank-stratum counts (16,36,6), total 58, matching actual class number. Independently evaluated q=2,m=3,5,8,12 Euler-product series at 70-decimal precision; q^{2m}-scaled two-term residual remains bounded and signed mean agrees with coefficient. The infinite result rests on the analytic uniform error, not finite data.

## originality

PASS

Best-of-knowledge PASS for the specific fixed-q growing-m conjugacy-class two-term expansion and the conditional one-sided annihilation rank law with strictly negative first bias. Standard rank enumeration and general polynomiality/theta phenomena are not presented as new. Similar prior group/matrix work does not exhibit a stronger statement directly covering this pair of conditional statistics.

## value

PASS

PASS: Beyond the standard rank formula, this computes a natural group-theoretic conjugacy-class invariant in a growing-dimensional family to two orders and reveals a discrete-theta conditional rank distribution with an intrinsic first-order negative bias. Fixed-field polynomiality does not quantify this; the signed finite-size correction is meaningful as a refinement of a natural random commuting-pair statistic. Worth does not depend on solving all parabolic groups.

The dated certificate retains the supplied scientific assessment, sources and limitations.
