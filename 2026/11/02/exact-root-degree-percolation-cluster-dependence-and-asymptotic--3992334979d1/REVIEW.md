# Review of exact root-degree and percolation-cluster dependence

## Correctness — PASS

The increasing-tree decomposition supplies the bivariate joint generating series, and the one-step conditional increment identities yield the closed covariance by telescoping. A second-moment recursion proves square-integrable martingale convergence for the normalized root component; original root attachment indicators split at a subpolynomial logarithmic scale into an asymptotically independent Gaussian tail. This proves the joint limit without confusing finite positive covariance with limiting independence. The standalone checker passed 345 independently generated exact-rational comparisons, including exhaustive original-parent/retention enumeration through six vertices. Finite checks corroborate rather than replace the all-size proofs.

## Originality — PASS, historically qualified

Desmarais, Holmgren and Wagner (arXiv:2110.15050; DOI 10.1002/rsa.21142) give a marginal generating function for the percolated root-cluster size and its limiting law. The present extra mark counts the original root children, regardless of edge retention; their marginal theorem does not determine a joint covariance or distribution. Kürsten (arXiv:1512.05275; DOI 10.1103/PhysRevE.93.032111), in Section IV and Appendix B, studies first-generation descendant-cluster sizes under percolation; that count differs from original root degree and has no identified implication covering the claimed joint formula. Targeted searches compared equivalent formulations, stronger literature and potential exact tables; no covering result was identified. Historical priority is not guaranteed by negative searches.

## Value — PASS

The exact transform gives all finite mixed moments of a natural local-versus-global pair in the same random tree. The positive covariance of order \(n^p\) and asymptotic Gaussian/Mittag–Leffler independence show precisely how local root attachment dependence survives in finite size but disappears at the central-limit scale, a distinction not obtainable from the two marginals. This is a structural dependence statement, not a routine parameter substitution.

## Scientific limitations

Uniform random recursive trees, independent fixed-parameter percolation \(0<p<1\), and original rather than retained root degree are essential. No finite convergence rate, variable-parameter uniformity, or general preferential-attachment extension is established. Independent assessment of mathematical validity and priority is still required.

Self-review: passed. Independent audit: not yet performed.
