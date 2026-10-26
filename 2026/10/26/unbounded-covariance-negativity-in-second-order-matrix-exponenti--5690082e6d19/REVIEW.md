# Scientific review

## Correctness — PASS

The conclusion follows by specializing the exact printed METD1, METD2, and METD2RK formulas to the two-dimensional Lyapunov equation with zero initial matrix and constant rank-one forcing. The exact covariance is a Gram matrix of distinct exponential functions and is strictly positive definite. For METD1, the symmetrized determinant is exactly \(-[f(a)-f(b)]^2/4\), so it is negative for distinct decay rates. For the second-order schemes, the full entrywise formula is explicit, and its symmetrized matrix divided by \(a\) converges to a symmetric two-by-two matrix with eigenvalues \(\pm g(b)/2\). The rational upper bound for the determinant at the finite witness \((a,b)=(10,1)\) avoids relying on floating point. The accompanying standard-library verifier passes 55 numerical/integral and rational checks; the infinite assertions follow from the proof rather than those tests.

## Originality — PASS (self-review)

The closest primary source is Shkeir and Grafke, arXiv:2406.13761, whose Section 2 supplies the exact schemes and whose Section 6.1 studies Lyapunov test problems. It does not present the universal METD1 rank-one indefiniteness or the linear-in-stiffness negative-eigenvalue limit for METD2/METD2RK. The low-rank Lie--Trotter construction of Ostermann, Piazzola, and Walach (arXiv:1803.10473) is a different update. Li’s Sylvester-superoperator exponential formula (arXiv:1907.12971, Section 2) uses an exact two-sided forcing integral instead of the source’s truncated commutator and does not imply its quantified failure. The symmetry- and positivity-preserving integrating-factor SSP methods of Zhang, Lan, and Jing (arXiv:2606.15703) are also different methods, and their general preservation results do not imply the quantitative negative-eigenvalue rate for the published METD algorithms. Specific source sections and claim-vs-prior comparisons are recorded in `AUDIT.json`. General geometric-integrator results and unlocated equivalent treatments remain a residual priority risk; absence from a search does not prove absolute novelty.

## Mathematical value — PASS

This is more than a symmetry or type-mismatch observation. On a uniformly bounded, strictly positive exact covariance problem with rank-one forcing, the **symmetric part** of the second-order approximation develops an arbitrarily large negative eigenvalue as one damped mode becomes stiff. Even post-step symmetrization cannot restore covariance validity. The exact coefficient \(g(b)/2\) quantifies the severity, and a rationally certified two-mode witness makes the boundary operationally detectable. The result separates fixed-operator convergence order from structure preservation and identifies a motivation for two-sided covariance-preserving quadratures.

## Limits and residual risks

Only the published full-matrix formulas with constant forcing, real negative diagonal generators, exact arithmetic, and one unit-length step are proved to have this behavior. Nothing here establishes divergence when the step tends to zero with the generator fixed, nor does it rule out alternative positivity-preserving exponential integrators. A covering statement may exist in other matrix-positivity literature; there has been no independent literature-priority adjudication or independent proof audit.

Self-review: passed. Independent audit: not yet performed.
