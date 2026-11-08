---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-01.md",
      "INDEPENDENT_AUDIT_2026-11-01.json"
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

PASS: For any finite support lambda_1<...<lambda_r spanning spec(T), N=sum_j(lambda_j I-T)P_j(lambda_j I-T) is positive without assuming effects commute. For each adjacent pair, q(x)=(x-lambda_i)(x-lambda_i+1) is nonnegative on every support atom; sum q(lambda_j)P_j>=0 implies N>=(T-lambda_i I)(lambda_i+1 I-T), so norm at least max of piecewise quadratic g_lambda on the spectrum. Continuous functional calculus cardinal hat effects P_j=w_j(T) attain exactly g_lambda(T), proving the fixed-support optimum even against arbitrary noncommuting POVMs. Because spec(T) reaches -1 and +1 and outcomes lie inside [-1,1], both extreme outcomes are forced; adding nodes cannot increase error. At four nodes -1,-s,s,1, solving s^2-a^2=(1-s)^2/4 yields s=(2 sqrt(1+3a^2)-1)/3 and E=(2-sqrt(1+3a^2))^2/9. Any support with error<=E has inner nodes -u<-a,v>a, each outer midpoint forces u,v>=s; endpoint -a then forces (u-a)(v+a)>=s^2-a^2=E, with equality only u=v=s. This proves optimality and uniqueness of outcome values, not POVM effects. Independently checked symbolic identity (1-s)^2/4=s^2-a^2.

## originality

PASS

Best-of-knowledge noncoverage after actual subject/statement/implication comparisons. Relevant known special cases and technical mechanisms credited; no proof of universal publication priority is claimed.

## value

PASS

PASS: The exact minimal intrinsic noise of a fixed small-outcome unbiased measurement with disconnected continuum spectral support is a naturally motivated quantitative replacement for the known infinite-spectrum exact-second-moment obstruction. The explicit nonzero gap law, unique optimal codebook and universal no-noncommuting-improvement theorem are mathematically meaningful rather than a rescaled numerical table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
