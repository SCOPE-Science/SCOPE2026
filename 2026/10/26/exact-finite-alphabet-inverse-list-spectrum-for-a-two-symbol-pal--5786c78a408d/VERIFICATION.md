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

Two inverse windows starting at i<j delete positions i+2,i+3 and j+2,j+3 in zero-based coordinates. Identical resulting words force y_k=y_(k+2) for i+2≤k≤j+1, making y_(i+2)…y_(j+3) 2-periodic. The equal middle pair of the last palindrome lies within this segment and makes it constant. The first palindrome then forces the entire interval to be constant. Thus each long constant run contributes once, and each nonconstant window corresponds bijectively to an interior length-two run with matching flanks. With R=(z+(t−1)z^4)/(1−z), summing weights of runs gives qR plus q(q−1)R²/[1−(q−1)R−(t−1)z²]: only appending after an interior two-run offers one weighted return color and q−2 other choices. This yields the rational function including words with zero parents. The mean independently follows from N−3 nonconstant-window terms of probability (q−1)/q³, a possible first long-run start of probability 1/q³, and N−4 other long-run starts of probability (q−1)/q⁴. For the limit law, choose a fixed circle in z enclosing 1/q at t=1; by continuity and Rouché the denominator has exactly one simple zero ρ(t) inside for complex t near 1. Its analytic leading coefficient is nonzero, and removing its pole gives a uniformly exponentially smaller coefficient term. With D=z²−z³+(q−1)z⁴ evaluated at 1/q, the first two derivatives of log(ρ(1)/ρ(e^s)) at zero are D and D(1+D−2D′/q), giving the claimed μ_q and positive ν_q. The uniform analytic expansion yields linear variance and the Gaussian limit. Odd-coordinate complementation exchanges precisely the parity of each of the two reversed copies and commutes with the even shift of the suffix. Independent window-deletion enumeration deduplicated parents as tuples and matched the generating function coefficient recurrence and run weights at (q,N)=(2,6),(3,8),(4,8); replay with python3 replay/1.py. These finite checks do not establish the limit law. The supplied verification package was inspected, not executed.

## originality

PASS

The complete nonbinary receiver spectrum and explicit fixed-q fluctuation law are the supported distinct content. The binary census, cited conjugacy, extremal observations and incidence count do not receive new-result credit. Distinct same-day and later overlapping statements were compared on their actual counting direction and parameter ranges, not assumed to be the original or to establish priority.

## value

PASS

Receiver ambiguity is a natural error-channel statistic; its full-population spectrum answers questions that code-size bounds, worst cases and forward-degree censuses cannot. The nonbinary return-color effect is structurally different from the binary model, and the nondegenerate variance rate quantifies typical fluctuations as well as providing exact finite coefficients. The claim does not promise a new encoder or a law for source-sampled channel outputs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
