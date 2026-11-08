---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

PASS. For K_{n,n} with exactly n red+n blue agents and both agents strictly improving across a swap, same-color or within-shore swaps cannot make both better. Every available opposite-color cross-shore swap changes x by ±1. Closed-neighborhood own-color fractions are complementary x/(n+1) and 1−x/(n+1) (or the analogous (x+1)/(n+1)); admissible utility is strictly monotone transform of q_Λ(s)=min{s/Λ,(1−s)/(1−Λ)}. Therefore preference comparison sign is (1/2−Λ)(1/2−s); low peak drifts from midpoint toward x∈{0,n}, high peak toward midpoint, Λ=1/2 gives complete indifference, and every profitable move decreases explicit T_nΛ(x) by one, proving every maximal strict path same length. Stable-coloring counts 2, binomial C(2n,n), and sum_{j=floor n/2}^{ceil n/2} C(n,j)^2 follow. Direct Vandermonde hypergeometric X and telescoping x² C(n,x)² yield exact D_n expected |X−n/2| and Stirling sqrt(n/(4π)). Independently checked actual swaps and T clocks on all colorings n=2..5 at three rational peaks, including odd/even boundary, and exact D_n for n 2..15. Assumes full occupancy, two equal parts and common peak, not asynchronous attempts.

## originality

PASS

PASS at best knowledge for the balanced complete-bipartite all-peaks equilibrium spectrum, choice-independent exact strict-swap clock and random-initialization expectation; the Schelling game model and generic equilibrium existence/FIP theorems are acknowledged prior work.

## value

PASS

PASS. A natural concrete Schelling game achieves a complete equilibrium census plus strong path-length invariance under arbitrary improvement choices and exact expected convergence counts; the critical all-coloring degeneracy and Θ(sqrt n) vs Θ(n) clock scales give useful, interpretable finite-to-asymptotic dynamics beyond existence theorems.

The dated certificate retains the supplied scientific assessment, sources and limitations.
