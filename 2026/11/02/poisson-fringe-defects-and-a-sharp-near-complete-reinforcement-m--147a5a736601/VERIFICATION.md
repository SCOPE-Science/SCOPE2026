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

For uniform recursive-tree parent choices the non-root original fringe count satisfies EB_{N,k}=N/[k(k+1)] and fixed-k concentration. At Nq_N→lambda, independent edge marks yield independent Poisson intensities lambda/[k(k+1)]; the expected count of marked sizes>K is ≤Nq_N/(K+1). Two marked edges are ancestrally nested with expected count O(q_N²N log N)=o(1), so with high probability the actual non-root components coincide exactly with distinct uncut marked fringes. This proves ℓ¹ tightness in number of components, compound-Poisson root deficit W with jump probabilities 1/[k(k+1)], infinite E[W] for lambda>0, tail lambda/m, and ED_N~lambda log N for exact q_N=lambda/N. Binary reinforced-step conditioning supplies a uniform independent bit per percolated component, whose parity Fourier character is the indicator all components have even size. Odd N makes it identically zero; even N makes it asymptotically exp(-lambda sum_{k odd}1/[k(k+1)])=2^{-lambda}, hence TV 2^{-lambda-1}. Independently exhaustive n=2..6 parent-tree/edge-cut enumerations confirm both exact fringe means and parity character; they do not prove convergence.

## originality

PASS

Peres–Qin arXiv:2604.07207 and 2604.07227 establish the walk/recursive-forest correspondence and exact odd-time parity uniformity, while Corollary 1.6 of the companion gives exponential two-sided even-time bounds at fixed reinforcement rather than the sharp N(1-alpha)→lambda crossover. The classical random-recursive-tree fringe law is prior work, not novel by itself. Baur’s high-retention percolation theorems concern diverging cut counts, unlike this bounded-intensity regime. The joint marked-component spectrum and resulting exact parity mixing coefficient are not implied by the compared specific theorems. General Poisson thinning literature remains a genuine priority risk.

## value

PASS

The nontrivial near-perfect-reinforcement mixing window has a closed critical profile and an explicit even-time TV constant, linking random recursive trees, a heavy-tailed compound Poisson root deficit, and a natural finite-group walk. The infinite-mean/distributional convergence contrast and parity phenomenon are substantive, not a cosmetic parameter change.

The dated certificate retains the supplied scientific assessment, sources and limitations.
