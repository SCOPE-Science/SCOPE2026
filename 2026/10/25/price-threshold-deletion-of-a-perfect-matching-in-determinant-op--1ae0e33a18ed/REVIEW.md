# Scientific review

## Correctness — PASS

For every integer \(n\ge3\), all positive prices and budgets, injectivity of individual edge weights into a reduced simple-graph Laplacian makes log determinant strictly concave on connected supports and forces a unique unrestricted optimum. Joint permutation of matched vertex labels forces exactly two weight classes. The complete four-block spectral factorization gives the exact weighted tree polynomial; the constrained logarithmic derivative has the stated explicitly signed quadratic numerator. Its sign yields the unique positive radical root below the price threshold, and a boundary optimum above. Differentiation of log tree count plus exact crown resistance identities corroborates the same threshold. The standalone exact-rational grounded determinant and resistance tests and floating-point asymmetric comparisons passed; they are not substitutes for proof.

## Originality — PASS (residual risk)

Related primary literature establishes general weighted matrix-tree and convex graph-design principles and, much closer, exact matching-containment tree counts and resistances for matching-deleted complete bipartite graphs. Those prior exact coefficient formulas yield the two-orbit unoptimized weighted count but do not state or globally characterize the unique price-budget allocation over all independent edges, its sharp cutoff or the full cost-dependent optimum. General theory plus simple derivations could make the distinction less independent than a wholly new spectral invariant; this is a real residual risk, not proof of uniqueness of discovery. The closest examined source is Ge and Dong (2019), arXiv:1904.07766, Theorems 1.3, 1.5 and 5.7. Those theorems do give the unoptimized symmetric spanning-tree polynomial and electrical endpoint data; neither this polynomial nor the unoptimized crown case is claimed as new. Khosoussi et al. (2016), arXiv:1604.01116, provide broad log-determinant network design methods, and Ghosh, Boyd and Saberi (2008) address a different resistance-minimization objective. The present supported novelty assessment is limited to the exact unrestricted two-price optimizer and its sharp edge deletion threshold; its derivability using published coefficients remains an explicit risk.

## Mathematical value — PASS

A full closed-form resource-allocation classification for dense bipartite networks with a distinguished perfect matching determines both the unique optimal support and all conductances, including a strict phase transition at a computable resistance-leverage price ratio. The premium for deleting all n matching links tends to zero like 1/n, a nontrivial large-network design effect. This is a natural graph-design optimization, not an arbitrary finite table or isolated parameter computation; it does not rely on any claimed downstream theorem.

## Claim-to-evidence and limitations

The exact parameter domain is all integer \(n\ge3\), real budget \(B>0\), and relative price \(\tau>0\), under independent nonnegative conductances on \(K_{n,n}\). The proof's critical steps are strict concavity, the exact four-eigenspace weighted-Laplacian decomposition, and a quadratic stationary-point sign classification, reinforced by exact resistance ratios at the crown support. `verification.py` provides 24 exact determinant checks, 18 exact resistance and threshold-ratio checks, 4,410 random asymmetric feasible comparisons, and 196 boundary checks; its output is included. These finite tests alone do not establish the theorem. Price heterogeneity within a class, side imbalance, edge upper bounds, and other network criteria remain unproved. Historical specialized coverage remains a material originality risk.

Self-review: passed. Independent audit: not yet performed.
