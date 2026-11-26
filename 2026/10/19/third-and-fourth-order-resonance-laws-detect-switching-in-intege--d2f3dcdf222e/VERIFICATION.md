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

Lebesgue integration selects signed frequency sums equal to zero, with weight 2^(-k) for k cosine factors. Growth by integer factors at least two implies that a unique largest term in a cancellation with at most four factors must be the sum of all the smaller terms with the same sign: even the two largest smaller frequencies together are at most the largest, and any subtraction makes the inequality strict. With three factors this gives two equal half-frequencies, necessarily an adjacent doubling. With four factors, three equal smaller frequencies give an adjacent tripling, with four permutations and weight 1/8 per product. Exactly two equal smaller ones require the repeated smaller frequency to be half the larger smaller frequency, and that one half the largest: for u<v<w one needs w=2u+v, since w=u+2v would contradict integer divisibility. With four distinct frequencies the three smaller sum to at most 7/4 times the second largest, never the largest. If the largest repeats, only pair cancellations survive except the all-equal case already counted. The single-frequency and two-pair baselines give 3n²/4−3n/8, and consecutive doublings contribute twelve permutations at weight 1/8. Third and fourth cumulants then give the switch counts as stated. At fixed m>0 and L=n−1, A=m−r for r nonempty runs, and every r from 1 to min(m,L−m+1) is realized by separating runs with tripling switches and placing surplus symbols arbitrarily. The case m=0, including n=1, is the singleton range. The annealed cumulant averages the conditional one here because both the conditional mean and variance are constant. No full word reconstruction or noisy estimability follows.

## originality

PASS

Exact constant-base cases are prior: Aistleitner–Gantert–Kabluchko–Prochno–Ramanan give the same finite dyadic third and fourth cumulants outright, the tripling fourth-cumulant correction in the proof of Theorem B(iv), and independent-arcsine moments through order q at fixed base q. Do not credit those coefficients or the Fourier zero-sum method as new. The surviving distinct claim is the full finite classification under arbitrary integer-product switching, including isolation of which adjacent doubling pairs contribute and exact inference and attainability for nonconstant binary schedules. The inspected literature or catalogue entries do not resolve that classification for arbitrary prescribed mixed products.

## value

PASS

The natural first Fourier observable has a variance blind to all schedules; this calculation quantifies exactly which first non-Gaussian statistics detect local switch order, and which values are attainable at a fixed slope count. For example the schedules (2,2,3) and (2,3,2) have equal mean, variance and third moment, but their fourth cumulants differ by 3/2. A fixed-base table cannot answer that comparison. The inference is explicitly limited to two exact aggregate statistics, not full reconstruction or sample-efficient detection.

The dated certificate retains the supplied scientific assessment, sources and limitations.
