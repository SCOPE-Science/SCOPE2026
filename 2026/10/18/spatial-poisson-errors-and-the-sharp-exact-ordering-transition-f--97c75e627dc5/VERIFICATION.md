---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

Reconstructed the n-dependent exponential clock model with strictly positive rates, unique continuous sample ordering and uniform neighboring ratios n*r_{n,i}→a(i/n) where a is bounded continuous and may vanish. For i<j the exact two-clock race probability is lambda_j/(lambda_i+lambda_j)≤(C/n)^(j-i), so the expected number of inversions at gaps≥2 is at most n(C/n)^2/(1-C/n)=O(n^-1). Excluding them, adjacent inversions cannot touch (else transitivity makes a gap-two inversion) and inversion sets determine the full permutation. The exact chronological race probability for a length-k decreasing run is ≤R_n^k; disjoint clock blocks factor, giving domination of each size-k Laplace inclusion-exclusion term by C^k/k!. Neighbor-free subsets factor, neighboring subsets count O_k(n^(k-1)); Riemann summation of (1-exp(-f(i/n)))r_i gives ∫a(1-exp(-f)). Dominated summation yields the spatial Poisson Laplace functional. Full inversion and parity limits follow with O(n^-1) rare long-inversion error. For geometric r, sequential race selection gives exactly product_{k=2}^n[(1-r)/(1-r^k)]; nr→∞ case follows by n/2 independent odd-index adjacent comparisons. Independently recomputed exact identity and pair probabilities n=2..7 from independent enumeration. All-size convergence is analytical, not inferred from enumeration.

## originality

PASS

Published ranking laws for independent continuous variables and finite heterogeneous exponential record indicators do not imply this n→∞ spatial Poisson permutation limit; classic exponential race and Poisson rare-event tools are background, not new. Best-of-knowledge priority remains subject to equivalent high-signal Plackett–Luce ranking analyses outside indexed papers.

## value

PASS

A natural complete asymptotic description of a noisy sorting regime: not merely convergence of a count, but the marked error locations, exact permutation support, parity, zero-error probability and sharp geometric recovery transition. This identifies precisely when exponential-race rankings become reliable and how sparse errors arise. The spatial point process and full permutation refinement are mathematically useful even though their constituent race identities are standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
