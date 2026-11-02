# Scientific review: five-cycle cluster roundness

## Correctness — PASS

For the exact metric described in `RESULT.md`, the powered-distance matrix factors into a five-cycle circulant tensor and a within-cluster diagonal tensor. Its zero-sum spectrum comprises \(-s^p\) (multiplicity \(5(m-1)\)), \(E_1\) (multiplicity two) and \(E_2\) (multiplicity two). The inequality \(E_1\le-1\) for the entire stipulated domain leaves only \(E_2\), a strictly convex function starting at \(-1\) and tending to infinity. This proves a unique positive critical exponent with an exactly two-dimensional nullspace. The limiting equation and its first two derivatives at zero prove the three distinct branching scales. Exact rational decomposition and independent numerical full-matrix diagonalization replayed successfully; those computations corroborate, rather than substitute for, the analytic proof.

## Originality — PASS, with residual literature risk

The closest primary precedents are Sánchez's full-text Example 2.8 for the ordinary five-cycle, Murugan's general determinant criterion for vertex-transitive metrics, Li–Weston's strict-negative-type inheritance theorem and Weston's universal metric-diameter lower bounds. None of the inspected material states the full \((m,s)\) classification or the three-regime limit with its \(m^{-1/2}\) critical law. General spectral methods are prior art and must not be represented as new. The special \(m=1\) five-cycle exponent is also prior art. Search-index coverage is not exhaustive, and an equivalent differently named clustered-metric result might exist.

## Value — PASS

The class contains both natural five-cycle graph blow-ups as endpoints and a continuous family of nontrivially weighted cluster metrics. The exact equation establishes a meaningful stability threshold for preserving positive Hilbert snowflake exponents under increasing cluster cardinality. The critical distance \(s_c\) separates persistent positive exponents from inverse-linear decay; exactly at the boundary, inverse-square-root decay occurs with an explicit universal constant. The endpoint Euclidean rank loss of two and a sharp \(1\)-negative-type criterion add direct embedding consequences. The finding is an exact infinite-family classification, not a numerical table or isolated parameter computation.

## Closest sources and limitations

Sources examined: A. Weston, arXiv:0807.2705, Theorem 4.1; H. Li and A. Weston, arXiv:0901.0695, Theorem 5.4; S. Sánchez, arXiv:1108.0451, Corollary 2.4 and Example 2.8; M. K. Murugan, arXiv:1112.5657, Theorem 3.1. The result is restricted to five equally sized cyclic clusters and \(0<s\le2\). It does not solve unequal cluster-size or general cyclic cluster problems. There is no claim of independent external validation.

Self-review: passed. Independent audit: not yet performed.
