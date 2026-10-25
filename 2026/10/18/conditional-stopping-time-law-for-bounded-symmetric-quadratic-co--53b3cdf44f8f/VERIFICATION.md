---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

The map is even-halving and odd (n^2-1)/4; Ye 2026 Theorem 3 provides a complete classification of eventually zero-reaching positive odd parts as 2^m-1, 2^m+1 and exceptions 11,23,181. Direct recursions give T(2^ell(2^m-1))=ell+m(m+1)/2, plus-family adds 2; 3 is counted twice with matching time, and exceptional times are 12,20,80. Counting bounded powers up to 2^L gives L^2+2L-12, and arithmetic progression sums give the displayed quartic first moment. Uniform cutoff 2^L<=X<2^(L+1) changes lattice-triangle counts by O(L), proving the limiting CDF F(z)=2sqrt(2z)-2z on [0,1/2] and moment 1/(2^r(r+1)(2r+1)). Horizontal time rounding O(1/L) combined with the square-root singularity gives Kolmogorov O(L^-1/2). Since T(n)>=log2(n), all T<=L seeds lie below 2^L, and the two triangular C_m cutoff sums yield H_L=(4sqrt2/3)L^(3/2)+O(L), giving the positive 2sqrt2/3 lower coefficient at z=1/L. Fresh exact-integer tests for L=7..18 verified counts, sums and H_L; numerical asymptotic-gap checks at L=100,1000,10000 approach 2sqrt2/3. This is conditional on Ye classification; finite arithmetic does not prove it.

## originality

PASS

Best-of-knowledge original structural or statistical addition survives direct statement/implication comparison with published primary results. Established premises, included special cases and residual priority risks are identified rather than represented as discoveries. Unsuccessful search is not treated as proof of novelty.

## value

PASS

A full conditional limit law, all polynomial moments, exact dyadic census and sharp slow distributional rate quantify a natural sparse set of terminating seeds for a specific quadratic dynamical system. Those are mathematically meaningful statistical refinements of the bounded-orbit classification and separate rigorous density-zero sampling from ordinary random integers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
