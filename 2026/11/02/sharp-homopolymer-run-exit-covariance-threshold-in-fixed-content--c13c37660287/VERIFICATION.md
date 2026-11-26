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

For a linear word with b ones, the b+1 lengths L_j of zero gaps are a uniform weak composition of a. The probability of prescribed lower bounds totaling s on distinct gaps is R_s=binom(n−s,b)/binom(n,b), or zero if s>a. Write S_s=sum_{t=s}^a R_t; by the hockey-stick identity this equals binom(n−s+1,b+1)/binom(n,b) (zero for s>a). Since X=sum_j (L_j−2)_+ and Y=sum_{j≤b}1_{L_j≥2}, EX=(b+1)S_3 and EY=bR_2. Each same-gap term of EXY gives S_3, each distinct-gap term S_5, hence EXY=bS_3+b²S_5. Therefore Cov=bS_3[1−(b+1)R_2]+b²S_5. Substitution and a+b=n give the frozen formula, including n=4,5 with impossible gap events counted as zero. The source's separate ordered window proof also has the stated counts of n−3, n−4 and (n−4)(n−5) for +1, +2 and disjoint pairs at n≥6. The remaining factors are strictly positive, so the sign is that of τ_n−a. In the zero equation t=2n−3 divides (n+6)(n−1); four times the product is 15 mod t. With t≥5 only 5 and 15 are possible, giving exactly (4,3,1) and (9,4,5), and the leading powers yield the normalized limit. Independent exact enumeration agreed on all 88 compositions at lengths 4–14 (including smaller a with X identically zero); output /workspace/branches/ae960dac-a50f-4325-ba26-2e2c660dd19e/enumeration-check.txt. This finite check does not prove the general sign law. The frozen verification notes and script were read, not rerun.

## originality

PASS

The supported distinct result is the fixed-count linear 000/001 covariance sign threshold and exact nondegenerate equality classification, including the finite-size shift. The closest inspected result concerns different overlapping trigrams; it cannot be transformed into this one by relabeling or reversing the word. Broad pattern-count methods motivate the calculation but no inspected theorem gave a direct fixed-count sign law or equality classification for these observables. This is best-of-knowledge, not a historical priority assertion.

## value

PASS

Both observables are natural complementary summaries of long zero runs: excess length and the number of exits into a one. Their covariance under the exact fixed-content null changes sign and is neither generically absent nor fixed by independent-bit intuition. The exact crossover and two finite exceptional zeros can be used to calibrate contrasts even near the asymptotic threshold. This is useful without implying independence or greater statistical power.

The dated certificate retains the supplied scientific assessment, sources and limitations.
