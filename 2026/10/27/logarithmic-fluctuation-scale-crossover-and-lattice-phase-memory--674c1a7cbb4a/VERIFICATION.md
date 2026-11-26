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

For the repaired vector statement in repairs/5/RESULT.md, take windows of lengths u≤v with u+v<N; there are v−u+1 containing shifts and two shifts at each overlap u−r for 1≤r<u. Common signs cancel, giving the stated finite covariance after subtracting the product of means at each overlapping shift. The geometric tail gives C with d=|h_i−h_j|, and the last term (u+v−1)mu^(u+v) vanishes. For each linear combination, the absolute covariance sum is uniformly bounded by the same overlap count and a convergent geometric series. Keeping blocks of size floor(N^(1/3)) separated by gaps of length O(log N) (including at wraparound) retains independent block sums with maximum size o(sqrt N). The o(N) omitted terms have o(N) variance; the retained variance converges to the asserted quadratic form after normalization. Lindeberg–Feller and Cramér–Wold apply, with zero limiting variance handled by Chebyshev. The exact mean gives the phase-dependent vector shift, and the positive marginal variances ensure Gaussian orthants have null boundary. The original scalar assertions are mathematically sound but were already covered. Frozen VERIFICATION.md and verify_kac.py were inspected, not rerun; finite checks do not establish this CLT.

## originality

PASS

Original originality FAIL for the unqualified scalar growing-time CLT and one-time sign/noise crossover: the earlier revival record proves this same early-time scalar CLT with the same parameters, range of times, and variance, and its critical-window calculation yields the same sign limit. This is exact coverage in its proof even though its main theorem is at revival. The repaired claim expressly credits and does not claim those one-time conclusions. It retains only the joint distinct-offset limit and the resulting joint phase law, which neither the identified scalar result nor the fixed-horizon covariance implies. This is a best-of-knowledge assessment of the narrowed claim.

## value

PASS

The repaired claim identifies correlations between different nearby times at the relaxation scale in one static environment. Those correlations determine simultaneous sign probabilities and give information unavailable from the known scalar CLT or the signal-to-noise timescale alone. The uniform growing-window proof is needed to justify using the explicit kernel as a joint Gaussian law.

The dated certificate retains the supplied scientific assessment, sources and limitations.
