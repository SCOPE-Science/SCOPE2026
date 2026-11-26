---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The season generators implement exactly the conservative uniform clockwise cycle and the isolated-patch averages are (-1/2,-5,-1/2,-9/2). Each exponential is strictly positive for T>0 by the directed paths in powers of the nonnegative shifted generator. Shifting by 16I gives H(T)=exp(16T)M(T). For each scaled generator the max row sum is at most 144/5; the k=81 scalar Taylor term divided by 1-r/82 therefore bounds each entry of the omitted tail. Positivity permits ordered multiplication of the entrywise bounds. A fresh exact Fraction replay at /workspace/branches/03d20474-ccd7-4f85-a58b-b7be5e0da5f1/independent_certificate.py confirmed the componentwise Perron certificates: rho(H(2/5))<263, 7.5e9<rho(H(8/5))<8e9, and rho(H(16/5))<5.5e19. Since 263^4<7.5e9 and (7.5e9)^2>5.5e19, the period ratios 4 and 2 give the stated strict interior high value. Independent scalar Taylor lower bounds on exp(16T) exceed the corresponding Perron upper thresholds, proving negativity at those three periods only. One constant season has exponent equal to the generator's spectral abscissa independently of T; no patch-minimality claim is tested. The frozen checker and notes were inspected, not executed.

## originality

PASS

Pass the simultaneous uniform-cycle, two equal seasons, isolated-sinks witness with both directions certified at three periods, not generic failure of monotonicity or the rational Perron technique. A closely matching catalogued two-season failure of nondecreasingness uses nonuniform rates, is not all isolated sinks as stated, and its displayed comparison is in one direction only. Calendar order is not used as a coverage test.

## value

PASS

This is a witness at a natural control boundary: minimal number of seasonal states even when the migration rates are forced equal, while all isolated patches are sinks. The exact interior increase and decrease at negative exponents show that period can change the rate of extinction nonmonotonically without any of the three comparisons being a persistence switch. That constrained counterexample is useful independently of a classification or a minimal patch count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
