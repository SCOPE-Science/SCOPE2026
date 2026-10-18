# Scientific review

## Correctness

PASS. The unrooted leaf-count chain has transition \(k\mapsto k+1-B\) with conditional success probability \(k/m\), giving \(\mu_m=m/2+1/(m-1)\) and, for \(m\ge3\), \(v_m=m/12-1/(m-1)^2\). Conditioning on the common tree and independent future continuations proves the exact finite covariance and its strict sign and independence boundary. Monotonicity of a shared-uniform coupling gives covariance positivity for all increasing transforms of the two leaf counts. A bounded-noise martingale with explicitly converging quadratic variation gives the bivariate Gaussian and the cubic correlation kernel. Exhaustive exact-rational verification passed 16,932 assertions, independently enumerating full recursive trees through size eight and joint laws through size sixteen.

## Originality

PASS, conditional on the inspected record rather than independent certification. Rácz and Sridhar [1] introduce exactly this common-history uniform-attachment coupling, but their inspected results concern network correlation detection through balancedness and subtree statistics. Bäumler et al. [2] give an independently derived bivariate leaf CLT under a distinct per-step correlation coupling. The marginal random-recursive-tree degree results of Janson [3] do not directly provide a two-tree cross-covariance. Mathematical-record semantic queries for shared-prefix leaf covariance, equivalences and cubic Gaussian memory did not identify a dominating theorem. Historical-priority risk remains, especially inaccessible full text and potentially implicit older joint generating functions.

## Value

PASS. The theorem quantifies how much shared early growth is visible in two canonical graph-invariant counts. Exact independence through the three-vertex prefix, strict positive covariance afterward, universal pairwise positive association, cubic macroscopic memory, and a closed Gaussian quadrant signal jointly distinguish microscopic and macroscopic ancestry in a natural generative model. These are structural dependencies, not isolated small-parameter calculations.

## Boundaries

Only the deterministic two-vertex seed, uniform attachment, undirected degree-one leaves, and shared-prefix/independent-future coupling are treated. Neither full graph independence for small prefixes nor a total-variation detection threshold for arbitrary sublinear shared growth is asserted. Finite enumeration supplements but does not replace the proof of infinitely many cases or the joint CLT. Independent mathematical auditing and historical-priority certification remain outstanding.

Self-review: passed. Independent audit: not yet performed.

## Sources

[1] M. Z. Rácz and A. Sridhar, *Correlated randomly growing graphs*, arXiv:2004.13537v1 (2020).

[2] J. Bäumler, M. Rácz, N. Ross and A. Sridhar, *Correlated uniform attachment trees*, arXiv:2606.02472v1 (2026).

[3] S. Janson, *Asymptotic degree distribution in random recursive trees* (2005), DOI: 10.1002/rsa.20046.
