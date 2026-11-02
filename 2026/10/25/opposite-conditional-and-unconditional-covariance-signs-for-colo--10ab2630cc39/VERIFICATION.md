---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For fixed-composition sampling, any prescribed p ones and q zeros at disjoint positions has hypergeometric probability (a)_p(b)_q/(a+b)_{p+q}. Partition the simultaneous singleton indicators by endpoint/interior and separation; prescribed local bit patterns give E X, E Y and E XY, with factoring Cov=2ab(a-1)(b-1)[ab(2n-3)-2n]/[n²(n-1)²(n-2)(n-3)]>0 using ab>=2(n-2). Given run counts and starting bit, one- and zero-run lengths are independent uniform compositions; expected singleton count in r parts summing to a is r(r-1)/(a-1). Even R fixes both run numbers and yields conditional independence. Odd R mixes two opposing endpoint orientations with weights C(a-1,t)C(b-1,t-1) and C(a-1,t-1)C(b-1,t), producing the negative covariance; t=1 simplifies to -4/(n-2)^2. The n=4,5 boundary cases are separately checked. Independent exact rational enumeration for all 2<=a,b<=7 agrees with both marginal and conditioned formulas.

## originality

PASS

The classical Wald–Wolfowitz/Smeeton–Cox run-count distribution and Doğanaksoy et al. length-one run tests establish ingredients, and the previously published Resultary dependence-phases paper is on **transition indicators** rather than opposite-color singleton *run counts*. Neither inspected same-sample claim implies the universal conditional-vs-unconditional sign reversal, but Barton & David (1957) Multiple Runs and Barton (1967) completed runs may contain broader multivariate generating-function machinery. That historical risk is explicit; best-of-knowledge PASS is not a universal priority certificate.

## value

PASS

In fixed-composition testing the per-color singleton-run counts are natural measures of isolated local symbols, and the total run count is the standard statistic used for conditioning. A uniform positive-to-nonpositive covariance reversal at every fixed run count, with strict sign at R=3, is an interpretable nontrivial dependence phenomenon. The exact algebra matters to run-stratified interpretation, without claiming a new downstream test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
