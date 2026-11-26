---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The separate unitary input dilation and output reflection/dilation cancel the prefactor α, giving kα(s)=(1−s/α)_+^(α−1) at s=u+v. The twice-differentiated kernel is continuous through s=α for real α>3. Reconstruct h by integrating h'' against (t−s)_+; the triangle kernel equals the reflected J_t², a product of two zero-extended Hilbert–Schmidt kernels each with squared norm t²/2. They vary continuously in t in Hilbert–Schmidt norm, so the resulting weighted integral is well defined in trace class and bounded by half the weighted L¹ second derivative. For s≤α^(1/5), expanding the logarithm of the differentiated power gives −s+(3s−s²/2)/α+O((s²+s³)/α²); the prefactor adds −3/α. The exponential Taylor bound integrates against s² uniformly. Beyond the cutoff kα'' is bounded by e^(−s/2) for sufficiently large α, and the subtrahends are exponentially bounded as well. Thus the full nuclear remainder is O(α⁻²). Independently replayed the finite compression in the orthonormal basis √2 e^(−u) times [1,1−2u,1−4u+2u²]: the K₁ matrix is [[1,1,−1],[1,−1,0],[−1,0,0]]/8. Replay by expanding (u+v)−(u+v)²/2 and integrating each monomial via ∫u^m e^(−2u)du=m!/2^(m+1). The kernel is supported on this finite-dimensional operator block; a first-order skew-adjoint conjugation across the 1/2 spectral gap removes the off-diagonal block, leaving 1/2+ε/8, −ε/8, 0, up to O(ε²) in trace norm. Here support means the range and co-range of K₀+εK₁, not the spatial support. Ordered extremal eigenvalues and the best rank-two approximation bound transfer this to the infinite Hankel operator, including the O(ε²) total remaining singular mass. Rank-one singular-value interlacing and leading-mode truncation yield the exact best rank-one tail identity, hence both constants. No finite Nyström samples certify the real-order limit or trace tail; the listed checker orders are integer samples, although the proof is for real orders.

## originality

PASS

Pass for the sharp trace-class correction and the optimal nuclear tail, not for the leading trace constant or the first two singular coefficients in isolation. The same-day related record gives the latter coefficients and an ℓ² tail, not a nuclear tail. Its chronology within the day is undetermined. Eveson gives the leading trace norm and asks about a specified rank-one approximation; RESULT.md:78 should not describe that question as explicitly about the optimizer. This attribution qualification does not change the actual new trace-class conclusion.

## value

PASS

Quantifies the optimal nuclear error for a classical family where even the first two singular values and a small Hilbert–Schmidt tail do not determine that error. Eveson's question about a particular model motivates this operator-ideal scale, but the value does not rely on claiming that his literal question concerned the optimum or that the result computes the error for his chosen approximant. The weighted Hankel decomposition yields genuine uniform nuclear control beyond the same-day spectral subclaims.

The dated certificate retains the supplied scientific assessment, sources and limitations.
