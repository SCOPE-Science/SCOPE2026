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

For each n≥3 circular prism P_n=C_n□K2, encode an independent set by ternary word (0,+,−), at most one chosen vertex per rung. The unchosen rung-partner of a selected + rung sees 1 plus the number t∈{0,1,2} of adjacent − rungs; odd parity forces t∈{0,2}. The analogous − case implies any consecutive selected rungs propagate two alternating full choices around the ring, possible only for even n (coefficient a_{n,n}=2). Otherwise selected rungs are isolated and those separated by a single zero must have opposite signs; every other gap has no constraint. For 1≤k<n/2 put L=n−2k>0, r long gaps; choose their positions C(k,r), distribute L extra zeros C(L−1,r−1), assign 2^r signs to r path components; cyclic pointing yields factor n/k, exactly the displayed integer coefficient. For L=0 the two parity classes give 4 configurations iff 4|n and zero otherwise, with all other coefficients 0. Odd n maximum size (n−1)/2 has 2n witnesses; even n has exactly two full-row alternators. Independent newly written direct-neighbourhood enumeration of all 3^n ternary configurations for n=3..10 reproduced every coefficient including n=3, n≡2 mod4, and n≡0 mod4 boundaries. Initially a private test used incorrect layer encoding (-1,0,1) and was fixed BEFORE evaluation to correct states (0,1,2); rerun matched all coefficients. All-size proof is the sign-propagation and cyclic-gap argument, not finite enumeration.

## originality

PASS

The general notion and bipartite cubic even-n maximum are already known in Caro et al (2025). The new candidate contribution is the entire coefficient array of odd independent sets of the natural width-two cylindrical grid and the odd-n extremal count; neither source Paper I nor II provides these in inspected statements. The natural graph-product motivation is explicit in Paper II, which poses general Cartesian-grid determination as Problem 27. No global novelty guarantee is possible for unindexed transfer enumerations.

## value

PASS

C_n□K2 is the canonical first nontrivial cylindrical grid, precisely in the product-graph direction of the 2025 papers. A full coefficient formula determines the entire size distribution, including sharp odd/even density jump and n mod4 absence of halfway-size sets; this reveals structure invisible from the already known even-n maximum. Such exact enumerators are usable for other counting and parity-constrained coloring questions; no downstream theorem requirement is assumed. The combinatorial decomposition itself is independently informative.

The dated certificate retains the supplied scientific assessment, sources and limitations.
