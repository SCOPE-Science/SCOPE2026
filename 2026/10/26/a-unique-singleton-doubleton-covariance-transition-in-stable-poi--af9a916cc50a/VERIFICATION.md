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

For prescribed blocks of total size s and count k, once seated the marked blocks stay unchanged at step m with probability (m-s+kα)/m. Applying this to (s,k)=(1,1),(2,1),(3,2) and multiplying by the number of disjoint placements gives all three moments and the stated sign ratio. For n≥4 the factors (j+2α)/(j+α)^2 decrease strictly for j≥1, with decreasing leftover reciprocal factors; at n=3 the ratio is 2/[3α(1+α)]. The endpoint ratios straddle one. The sample-size quotient increases with α because n−3+2α is smaller than both denominator arguments n−2+α and n−1+α. Its numerator after subtracting 1 at α=2/5 has a positive factor 13n²−43n+24=(n−3)(13n−4)+12, so induction from α₃>2/5 gives strict ordering. Gamma-ratio cancellation gives αB(α,α)>1 at fixed α<1, implying αₙ→1. The log-ratio slope at α=1 telescopes to −1−1/(n−1), its second derivative is uniformly bounded by reciprocal-square sums near 1, and its value at 1 is log(1−2/n). The mean value theorem gives the stated scaling. Independent EPPF enumeration reproduced the moments for 35 exact parameter pairs and a symbolic check reproduced the quotient positivity identity; replay: python /workspace/branches/replay_three.py. Read but did not execute the frozen verifier; its numerical n-values up to 1000 are selected samples, not the proof of ordering.

## originality

PASS

Credit the known frequency-count law and its specialization to mixed block moments. The supported distinct contribution is the global one-zero sign theorem, strict nesting in sample size and near-one moving-discount scale, not the discovery of the joint law or of the three moments.

## value

PASS

Singletons and doubletons are the first two frequency-of-frequencies counts. The theorem tells precisely when the direction of their dependence reverses without changing the sampling model, establishes that the negative-covariance window strictly shrinks, and fixes its scale where fixed-discount asymptotics do not decide the sign. This is a natural all-n comparison, not a numerical root at a selected n.

The dated certificate retains the supplied scientific assessment, sources and limitations.
