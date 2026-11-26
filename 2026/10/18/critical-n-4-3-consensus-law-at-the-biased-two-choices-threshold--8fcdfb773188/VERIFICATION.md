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

The explicit assumptions and transition probabilities specify two independent draws from the n−1 other agents, with repeats allowed; the Finding's phrase 'distinct-index neighbors' should not be read as excluding repeats. At bias 1/9 the exact up/down ratio gives r=8k(n−k)/[(n−1)²+8k²]. The first-step differences satisfy λ_k d_k−μ_k d_(k−1)=1 and the initial equation at k=0, with absorption and finite mean guaranteed by the finite positive upward path. Iteration and summation give exactly the two nested sums. For x=k/n, 1−f(x)=(4x−1)²/(1+8x²), and the log perturbation from excluding the updater is O(1/n). At width h=n^(2/3), λ→1/8 and summing log r produces −(32/9)(u³−v³); the O(h/n) perturbation disappears. Globally the product is bounded by a constant times exp[−c n^(−2)Σ(ℓ−n/4)²]. The block of m successive indices has sum of squares at least (m³−m)/12. When the right endpoint is far from n/4, the terms with m≤|k−n/4|/2 have the extra decay exp[−c m(k−n/4)²/n²], and the rest have the cubic tail. With λ bounded below for k≤n/2 these give the integrable O(h/[1+((k−n/4)/h)²]) bound on d_k. The last half is O(n log n) by a fixed ratio gap starting at 3n/8, with earlier-index products suppressed. These estimates justify the inner and outer limits, including all fixed starts below 1/4, and the Gaussian midpoint integration gives the stated Gamma(1/6) coefficient. At p>1/4 one can start the ratio gap at a fixed p0 strictly between 1/4 and p, not at p itself. For k≥(1−δ)n, terms beginning below (1−2δ)n are exponentially suppressed, the remaining ratios are O(δ), and 1/λ_k=(n/(n−k))[1+O(δ+1/n)]. Hence the final states give coefficient 1 in front of n log n as δ→0, and the earlier states are O_δ(n). The scale counts individual updates throughout.

## originality

PASS

The distinct contribution is the controlled discrete consensus asymptotic for the original neighbor-only chain: critical-window start profile, below-window matching and above-window n log n matching at the precise bias omitted in the same-model prior theorem. The cubic diffusion kernel and its full-passage constant in saddle-node units are classical; only their rigorously derived realization and normalization in this chain, plus matching to actual consensus, are credited. Neither the same-model off-critical bounds nor the diffusion calculation implies the required uniform integrability or the remote absorbing-end estimate.

## value

PASS

The exact threshold is a natural gap between fast and exponentially slow regimes. The result identifies a different scale, quantifies the dependence on starts across the bottleneck, and separates it from a distinct coupon-collector endpoint even at the same bias. This is useful discrete finite-size information about a standard model beyond the known continuous normal form.

The dated certificate retains the supplied scientific assessment, sources and limitations.
