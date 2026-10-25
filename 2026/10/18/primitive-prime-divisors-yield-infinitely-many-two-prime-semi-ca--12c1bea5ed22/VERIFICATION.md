---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

For n=pq (p<q distinct primes), checking all four positive divisors reduces exactly, by CRT and Fermat, to q|p^(p−1)−1 and p|q^(q−1)−1. Bang–Zsigmondy for (p,1,h=p−1) has no exceptional case for p≥5, so a primitive q has ord_q(p)=p−1, p−1|(q−1), q>p; Fermat supplies the second condition. Taking one q per p gives distinct products because p is always the smaller factor; pq<p^p. For Y=floor(log X/loglog X), Y log Y<log X and the prime number theorem yield S₂(X)≥π(Y)−2 and stated liminf at least one. Two-prime Korselt divisibility excludes every constructed n from ordinary Carmichael numbers. Independent code checked all 5,047 distinct semiprimes <=20,000 (25 satisfying) by the original and reduced criteria and several order witnesses. The finite checks do not certify Zsigmondy, the PNT, or the infinite conclusion.

## originality

PASS

Best-of-knowledge comparison against genuinely read primary material and identified published mathematical records. Earlier definitions, known subcases and broad general results are credited. Inaccessible plausible full text is a material priority risk, not an automatic failure; unsuccessful database search is not a novelty proof.

## value

PASS

Answers an explicitly recorded infinitude question for the mathematically natural class of divisor-base semiprimes, supplies a uniform construction with any prescribed smaller p≥5 and an explicit lower-order counting bound. The known semiprime test and Zsigmondy are credited as premises; the value is their nontrivial bridge yielding a new infinite family and quantitative consequence. The lower bound is weak and is not a global asymptotic or effective least q algorithm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
