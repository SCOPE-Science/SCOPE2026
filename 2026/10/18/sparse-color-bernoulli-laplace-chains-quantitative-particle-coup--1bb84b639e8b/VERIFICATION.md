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

The exact comparison holds on the full finite parameter domain. After j decisions in an urn of size M, the discrepancy of selection probabilities is |jk/M-a|/(M-j) ≤ j/(M-j). Couple the whole marked-location vectors while they agree, then sum over urns and times. The stationary law is obtained by uniform placement of red labels, even for periodic swaps; applying the same sampling argument once with M=N and subset size m gives the stationary term. Projection to counts and the reverse triangle inequality give (1). The two-state recursion has signed eigenvalue ρ; the independent proxy has mean shift (x-rh)ρ^t. For finite z, the Bernoulli variances are uniformly rh(1-h)(1+o(1)). In the local limit argument the characteristic-function modulus is bounded by exp(-2σ² sin²(θ/2)) and the centered expansion at θ=w/σ is exp(-w²/2+O(|w|³/√r)); inversion gives uniform local Gaussian error o(r^-1/2), then truncation to O(√r) cells gives an ℓ¹ approximation. The equal-variance Gaussian comparison and whole-number discretization give the stated limit uniformly in x. For z=0 one can apply this at min(t,ceil(2a_N)) and contract, avoiding any use of (1) at arbitrarily late times. For infinite z and u≠h₀, the proxy means are separated by much more than √r, so midpoint Chebyshev and (1) apply; endpoint starts suffice for the worst-start lower bound. The lattice window is bounded, without replacing actual integer-time z by a continuous profile. The packaged exact-rational checker was inspected, not rerun; the proof does not depend on it.

## originality

PASS

The distinct contribution supported by the comparison is the count-chain error bound for simultaneous swaps and the logarithmic-time Gaussian TV profile for sparse colors with interior capacity and noncritical limiting |ρ|. Sampling couplings, Gaussian profiles in other urn regimes, and negative single-step eigenvalues are not new individually.

## value

PASS

The count chain is natural and previously compared positive-density cutoffs do not describe it. The explicit finite-time error is useful in its own right, and the sharp lattice-aware profile locates and quantifies mixing on the minority scale log r, not log N. The sufficient sparsity condition and exclusions (including the zero limiting eigenvalue) are material and are stated, not silently extrapolated.

The dated certificate retains the supplied scientific assessment, sources and limitations.
