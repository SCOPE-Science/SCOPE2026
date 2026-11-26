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

The expectation is of the Jaccard ratio on detected species, not individual overlap or a ratio of expectations. Inclusion–exclusion counts exactly those size-m subsets whose support is S, and independence multiplies two support counts. A separate replay generated every composition via cuts among N−1 gaps, sorted to exhaust the abundance partitions, and averaged the rational similarity over every ordered pair of labeled size-m samples. It agrees with the frozen CSV on all 135 cells of all 29 profiles through N=6. Its only strict drop is (1,5) from 7/9 to 3/4, at m=2 to 3. For general (1,N−1), both m≥2 samples always include the dominant species, so a similarity loss of 1/2 occurs precisely on singleton detection disagreement. Under independence the disagreement probability is 2(m/N)(1−m/N); under disjoint sampling the singleton cannot appear twice, giving 2m/N. At m=1 the ratio is exactly the species-match indicator. The initial increase is 2/N² and the forward difference thereafter is (2m+1−N)/N², which also gives the asserted integer minimizers on the stated domain (including the odd-N tie when both nearest integers are in it). Analytic arguments, not extrapolation, support the arbitrary-N results.

## originality

PASS

Best-of-knowledge pass for the exact finite-census minimality and uniqueness together with the sampling-design gap. Sample-size dependence and Jaccard undersampling bias are established prior phenomena. The closest exact indexed analogue has different sampling assumptions; the Cao body could not be checked.

## value

PASS

The sharp obstruction answers whether expected within-community Jaccard can serve as a monotone diagnostic of greater sampling effort under a standard finite sampling design. Smallest-census uniqueness is a natural endpoint, not an selected profile after the fact. The two protocols preserve equal marginal effort but differ in how singleton detections pair, reaching a 1/4 expectation gap at half the census; this gives the phenomenon quantitative and design relevance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
