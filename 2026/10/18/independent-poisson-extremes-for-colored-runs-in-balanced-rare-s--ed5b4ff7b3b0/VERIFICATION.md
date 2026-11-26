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

For m=N/2 and odds u=q/(1-q), at fixed switch count and first sign the two ordered run lists are independent uniform positive compositions of m. Their counts give the stated odd/even weights. In the Bessel comparison, writing a=j-1 and x=mu, the relative clipped-product deficits in the odd and even summands are bounded by a(a+1)/m and (a+1)^2/m, respectively. Summed against the two Bessel series, their combined bound is x(x+1)/m times I_0(2x)+I_1(2x), before the common 2x factor. Thus the relative error vanishes uniformly for odds tilted by s in a compact interval around 1. The resulting log conditional PGF is 2x(s-1)+(log s)/2+o(1), with 2x=T+o(1). Chernoff tilts s=exp(±c/log^2 T) give |K-T|<=T/log^2 T with probability tending to one since T/log^4 T diverges. For a color with r parts, discretizing r-1 iid cuts by ceil((m-1)U) moves each cut by at most one in m-scale. Conditional on distinct cuts the sorted set is uniform; resampling a uniform set only on collision gives an exact composition coupling, and the collision probability is O(r^2/m). Uniformly over concentrated switch counts, the largest error when replacing all (K/N)-scaled parts by iid exponentials is o_P(1): the cut error is O(K/N), and the sample-mean error times the largest exponential is O_P(log r/sqrt(r)), with K/(2r)=1+O(1/K). Independent exponential arrays give the product Laplace functional; log(r/K) tends to -log 2. The normalization transfer to T has uniform maximum displacement o_P(1) by the sharper switch concentration. Compact-window counts of the coupled exponentials are tight, so this displacement does not change the Laplace limit. Their maxima centered by log r are tight from the explicit exponential maximum law. That last fact, and the absence of limit atoms at z, justify the unbounded upper-tail counts and the longest-run law beyond vague convergence alone.

## originality

PASS

The supported contribution is joint, color-resolved extreme-run convergence for the balanced, rare-switch Markov word. Neither the previous endpoint crossing, nor a fixed-threshold Markov run law, nor a maximum of uniform spacings establishes the random-switch-count triangular-array joint limit.

## value

PASS

Exact balance strongly constrains the lengths and couples the run colors through the random number of switches. Showing that the colors nevertheless separate in the upper-tail limit answers more than the usual longest-run question, and applies on the independently motivated crossover scale. The full PPP identifies the joint law of counts in multiple extreme windows, not just the Gumbel marginal.

The dated certificate retains the supplied scientific assessment, sources and limitations.
