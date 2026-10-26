# Scientific review: Eventual exact Hilbert norms of maximal averages on unbalanced bicliques

## Correctness — PASS
The proof identifies the exact three ball averages at each graph vertex, computes the two-class singular-value benchmark, and establishes a uniform large-class estimate that forces every maximizing input into its strict active branch for the explicit sufficient threshold. Compactness justifies choosing a maximizer and the top singular value is simple. The analytic proof, not small finite tests, establishes the universal quantified result. The separately replayed `check.py` reports 2,658 finite checks.

## Originality — PASS within inspected evidence
Soria and Tradacete (2014, arXiv:1410.6204v1) studied finite-graph maximal operators and derived general sharp small-exponent bounds. González-Riquelme and Madrid (2020, arXiv:2005.03146; 2020 follow-up arXiv:2011.02630) give exact Hilbert norms on stars and complete graphs; those are distinct from nonstar bicliques. The star case \(a=1\) is excluded. Searches for equivalent formulations, broader results, exact tables and implications of nearby theorem statements found no decisive nonstar coverage. Historical priority is provisional and is not certified by an unsuccessful search.

## Mathematical value — PASS
The result identifies a natural regime in which an otherwise nonlinear maximal-averaging optimization admits an exact closed radical, proves the unique type of maximizing modulus, and establishes an explicit asymptotic with its inverse-size correction. It solves an infinite family of nonstar cases, rather than merely computing sample graph values.

## Limits and residual risks
Only integers \(a\ge2\), \(b\ge102400(a+1)^6\), counting measure, centered averages and the strong \(\ell^2\) norm are covered. The explicit threshold may be very far from sharp and the balanced regime is open under the present proof. External literature may contain equivalent nonstar results under different terminology. Numerics do not certify the general theorem.

Self-review: passed. Independent audit: not yet performed.
