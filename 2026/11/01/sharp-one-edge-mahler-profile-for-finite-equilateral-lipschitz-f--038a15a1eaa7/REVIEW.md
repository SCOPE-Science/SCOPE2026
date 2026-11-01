# Scientific review: one-edge Mahler profile

## Correctness — PASS

For every integer \(N\ge3\) and \(0<r\le1\), the object is the real Lipschitz-free unit ball dual to the finite-distance Lipschitz ball, with one exceptional distance and all remaining distances one. The proof reconstructs both polar bodies. The order-chamber Jacobian is unimodular; the beta-binomial identity integrates the \(N!\) simplex chambers exactly to \(r(2(N-1)-(N-2)r)\). The type-A root-polytope facet cones admit spanning-tree unimodular triangulations and their two stretched antipodal cap volumes add without overlap. The rational identities and the unique critical parameter follow directly. Numeric convex-hull evaluations independently reproduce both volumes through dimension six, while exact rational identities were checked through \(N=40\). The finite tests are corroboration, not the all-parameter proof.

## Originality — PASS, with residual priority risk

The closest full primary text is Alexander–Fradelizi–García-Lirola–Zvavitch, arXiv:1911.10642: its §5.2 computes only the undeformed equilateral value, while §5.1 proves abstract nonmaximality for nonsimplicial free-space balls and gives a general local facet-cap volume principle (Lemma 5.4), which is not claimed here as a new method. The present one-short-edge **two-volume identity**, the unique optimizer inside the shortening interval and the limiting amplification \(9/8\) are not covered or directly implied as numerical conclusions. Gordon–Petrov, arXiv:1608.06848, studies root-polytope face combinatorics and unimodular triangulations, not the varying Mahler product. Çelik et al., arXiv:2003.06725, treats Wasserstein polytopes for discrete and product metrics, not this one-parameter weighted metric. A publicly available claim about independently shortened disjoint pairs counts facets and classifies extreme potentials, but does not yield volume formulas. The remaining risk is an equivalent earlier stretched-root-polytope volume calculation under different terminology; absence from searched records is not exhaustive priority certification.

## Mathematical value — PASS

Finite Lipschitz-free space Mahler products are a motivated quantitative problem, specifically raised by the 2019 reference. The formula yields a **complete infinite-dimensional-parameter optimization for a canonical perturbation family**, not only another computation at the undeformed point. In every cardinality \(N\ge4\), the equilateral metric loses optimality under a single shortened distance and a unique interior distortion length restores optimality. The sharp relative improvement tends to \(9/8\), giving a dimension-independent quantitative answer to the nonmaximality phenomenon. The result does not claim a global metric-space maximum or settle higher-dimensional Mahler conjectures.

## Limitations and literature comparison

The full theorem is limited to real spaces with exactly one shortened metric pair and \(0<r\le1\). The \(N=3\) boundary is included, and the degenerate limit at \(r=0\) is excluded. Earlier results on arbitrary polyhedral deformations or single-root radial variations may express an equivalent fact; a historical-priority search cannot exclude every formulation. The checker needs Python, NumPy and SciPy for its independent hull mode; the proof uses none of those packages.

Self-review: passed. Independent audit: not yet performed.
