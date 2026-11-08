# Scientific review

## Correctness

PASS. Each \(0/1\) stable-set vector is a vertex; exact counting gives \(2^p+2^q-1\) distinct vertices. Explicit first and second moments give the block covariance, and its invariant contrast spaces and two-dimensional axial space exhaust the ambient coordinates. In the balanced case axial diagonalization yields a strictly smaller least eigenvalue than either contrast value. In the unbalanced case the exactly expanded determinant \(\det(L-(b/2)I_2)\), together with its positive leading principal minor, strictly separates both axial eigenvalues from the smaller-part contrast eigenvalue. A standalone exact rational checker enumerates 36 low-dimensional parameter pairs (2,988 sampled vertices across profiles), matching every covariance entry and the predicted eigenvalues. Numerical eigenvalues are used only as checks; the all-dimensional statements use the analytical inequalities.

## Originality

PASS with historical-priority risk. Primary full-text material for Aliniaeifard et al. (arXiv:1804.00360) concerns edge characterization, combinatorial skeleta, and graph-theoretic diameter. Aprile et al. (arXiv:1702.08741) address extended formulations; only its public abstract was available for direct comparison. Closest indexed records on two-layer order polytopes concern John ellipsoids (volume-maximizing inscribed ellipsoids), while other multipartite stable-set records concern minimum enclosing spheres: these invariants do not imply vertex-uniform covariance or its balancing transition without additional results. Search by synonyms for vertex sampling, inertia, second moments, and covariance returned no corresponding prior complete eigenvalue classification. This is a qualified self-review, not a guarantee of historical uniqueness.

## Mathematical value

PASS. The result is a natural complete spectral classification for every biclique stable-set polytope, rather than a special numerical slice. It exposes a discontinuous change in the minimizing eigenspace when a bipartition ceases to be balanced; in particular the dimension changes from one to \(q-1\) for unequal parts with smaller part size \(q\). It also separates linear balanced spectral condition growth from exponential fixed-minority growth. These qualitative changes inform geometry of vertex sampling and covariance-conditioned algorithms and are not provided by edge counts or facet descriptions alone.

## Limitations and risks

The proof uses standard Euclidean indicator coordinates and the uniform measure on **vertices**, not uniform interior volume. No independent audit has been performed. A Bernoulli-mixture or design-theoretic equivalent not surfaced by the searches could predate this classification. A publicly visible John-ellipsoid article on the isometric two-level order-polytope family was compared at statement level; its complete full text was not accessible in this review. This limitation does not establish absence of incidental second-moment formulae there.

Self-review: passed. Independent audit: not yet performed.
