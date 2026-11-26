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

With positive finite masses and strict upper records, conditioning on the last value at time r yields q_r=Σ_b p_b F_{b−1}^{r−1}. Conditioning on the two distinct record values a<b gives the joint formula: all observations before s are below a and all t−s−1 intervening observations are below b. In particular this includes adjacent times with a zero exponent. Independently, given the prefix maximum M_s=k, a record at s means the maximum occurs just once and at position s, giving p_k F_{k−1}^{s−1}/(F_k^s−F_{k−1}^s). Factoring the denominator shows this probability is increasing as F_k/F_{k−1} decreases (k≥1); the reverse hazard is 1−F_{k−1}/F_k. At k=0 the probability is zero. The conditional probability of a record at t uses only M_s and the independent suffix; increasing the maximum drops a strictly positive term from the admissible record-value sum. Thus the covariance is that of the nondecreasing and strictly decreasing conditional functions of M_s, and the usual independent-copy identity is strictly negative on the levels 0 and 1. Binary strict post-initial records are mutually exclusive and each has positive probability. For ternary masses (ε,ε,1−2ε), the sole possible two-record pair of values is (1,2); its probability is of order ε^(t−1) with positive coefficient, whereas the product of marginals is of order ε^(s+t−2). This proves the fixed-pair sign and exact minimum support size. For example at s=2,t=3 and ε=.01, q_2=.0197, q_3=.000393 and the joint is .000098, strictly above the product. Time 1 is deterministic and the proof does not claim negative association of the full vector.

## originality

PASS

The inspected antecedents cover marginal record rates, count asymptotics, or changes of sign from nonidentical continuous laws. They do not give either the finite iid reverse-hazard criterion for arbitrary pairs or the arbitrary-fixed-pair ternary witness with exact support threshold. Some older titles remain unresolved; the pass is bounded to the evidenced comparisons.

## value

PASS

Ties remove the familiar iid continuous independence property. A distributional shape criterion guaranteeing a strict sign for every pair gives a usable replacement in one regime. A sharp finite-support boundary showing why the opposite sign becomes possible is meaningful, and the pairwise conditional-maxima mechanism explains the dependence rather than just furnishing a numerical counterexample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
