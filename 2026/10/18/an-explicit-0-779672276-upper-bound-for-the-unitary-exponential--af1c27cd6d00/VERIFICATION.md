---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
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

Local factors rho_p(v_p(n))=(1+p^a)/sum_{d|a}p^d multiply exactly, with exponent0 factor1; a=1 gives 1+1/p and a>=2 gives <1. Take p<=5003 with specified caps, b=1001/1000 and exact integer ceil scores k_p(a). The weighted CRT DP over 670 primes counts E={all capped, sum scores<=−2}; independently recomputed 4216 nonzero states and exact G/M>11023/50000 with mass 0.220466626902605. On E, local product<=b^−2. Tail positive log is at most X=sum_{p>5003,p|n}1/p; CRT and sum p^−2 converge, giving independent limiting Bernoulli tail μ<31e−6, V<23e−10. Independently reproduced exact prime sieve ceiling sums 20243665461,2200010 for p<=100000 (8922 tail primes), variance Chebyshev risk <0.000594454<3/5000 above threshold 2ln b>2/1001. Thus E∩{X<2ln b} has lower density > (11023/50000)(1−3/5000)=55081931/250000000, where full divisor ratio<1. Complement upper density of strict excess <194918069/250000000. This is a genuine infinite tail domination argument, not extrapolation from 30,000 cases; exact DP reimplemented independently, not just source VERIFY_OK.

## originality

PASS

Trudgian poses the density comparison and gives squarefree lower bound and numerics. A relevant earlier published Resultary result gives a rigorous 0.753659844... LOWER density bound, not an upper bound. The present certified positive-density deficient-cylinder construction plus bounded all-prime compensation gives the different-sided strict upper bound. No stronger relevant upper theorem found in actual searches; unseen estimates remain risk.

## value

PASS

The density of the inequality between two natural divisor sums was explicitly posed and had a large uncertainty between rigorous lower bound and empirical frequency near 0.7783. A certified quantitative upper bound 0.779672276, close to the observed regime, is a substantive mathematical tightening, not mere rounding of a finite numerical table. The finite cylinder and analytic tail split is a reusable method.

The dated certificate retains the supplied scientific assessment, sources and limitations.
