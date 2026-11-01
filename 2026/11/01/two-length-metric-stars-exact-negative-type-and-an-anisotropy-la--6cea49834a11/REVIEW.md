# Scientific review

## Correctness — PASS

For every integer \(m,n\ge2\) and every positive length pair \(a,b\), the leaf-mean and internal-fluctuation decomposition gives identity (3) in `RESULT.md`. The two fluctuation blocks are strictly negative; the sole remaining radial block has determinant (4). The normalized cross term is strictly increasing in exponent above \(1\), while both diagonal factors decrease to their first zeros, proving existence and uniqueness of the threshold and precise sign changes. Strict \(1\)-negative type holds by an exact edge-cut identity; the standard downward-inheritance result extends strictness to smaller exponents. The critical block has nullity exactly one. The length-ratio monotonicity is proved independently using the strict concavity of the log-hyperbolic-sine function, and the limit uses a fixed-exponent asymptotic with exponent below \(2\). Gram ranks follow from the centered quadratic form. Exact rational and independent eigensolver tests on the package verifier corroborate, but cannot establish, infinite-parameter claims.

## Originality — PASS, qualified

Doust and Weston, arXiv:0705.0411 (first posted 2007-05-03), give weighted-tree strict negative-type bounds and evaluate the *equal-length* star exponent in their Theorem 38. This equals the uniform-length endpoint here. Li and Weston, arXiv:0901.0695, give the downward-inheritance theorem, not the present two-length evaluation. Sánchez, arXiv:1108.0451, gives a general distance-matrix method and an explicit **unweighted complete-bipartite** classification, but neither the exact two-length star threshold nor its monotonic contrast law is stated in the inspected text. The numerical and analytic contrast laws are not implied by those evaluated equal-length or unweighted classifications without an additional computation and inequality.

The relevant mathematical research-record searches and accessible earlier claim statements did not identify the same claim. A record about bounded-Lipschitz Dudley norms on equiradial stars concerns a different functional; a spider-tree curvature-distortion calculation concerns a different invariant; the earlier balanced double-star finding concerns two adjacent hubs with unit lengths, not a single hub with unequal arm lengths. A later full-text comparison with Doust and Weston, arXiv:2404.06684, also distinguishes their weighted-Hamming-cube strict \(1\)-negative-type equivalences and four-point-star illustration from the present all-exponent two-length-star evaluation. A 1990 metric-transform article by Deza and Maehara may contain related general embedding techniques, but its full text could not be inspected; bibliographic uniqueness is not certified.

## Mathematical value — PASS

The parameter family is the first natural heterogeneous refinement of the classical uniform star appearing in enhanced negative-type theory. It admits a **complete** real-exponent classification, a one-dimensional critical equality-space description, and a genuine structural anisotropy law: heterogeneity strictly raises the generalized-roundness exponent, despite keeping the underlying tree combinatorics fixed. Swapping the long- and short-arm assignments does not change the exponent even with unequal class sizes. A four-leaf example approaches exponent \(2\) without ever attaining it at finite length ratio. This goes beyond a numerical lookup or an isolated finite case and can inform the stability of Hilbert snowflake embeddings under edge-length perturbations.

## Risks and limitations

Only the stated two-class stars are covered. The limit is not achieved for any positive finite ratio. Source comparison is best knowledge rather than exhaustive: an equivalent result might occur in the inaccessible Deza--Maehara article or other unindexed literature. The supplied verifier does not independently certify the full proof. No independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
