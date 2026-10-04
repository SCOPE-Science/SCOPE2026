# Review

## Correctness

PASS. After scaling the PAGE estimator by \(\mu\), the refresh branch sets the estimator equal to the new position, while the recursive branch multiplies it by \(1-\alpha(1+\sigma h)\). Exact branch averaging closes the three second moments \(\mathbb E[x^2]\), \(\mathbb E[xy]\), and \(\mathbb E[y^2]\). The characteristic cubic satisfies
\[
P(1)=\frac{\alpha}{9}\left[2+3\alpha-2(1+2h^2)\alpha^2\right].
\]
The proof checks the complete cubic Jury criterion and shows all other inequalities stay strict until this factor vanishes. Equality gives eigenvalue \(1\), and larger positive steps violate a necessary Schur condition.

Risk: the result is specific to the stated PAGE branch order and \(p=1/3\).

## Originality

PASS. Loopless SARAH is an algorithmic alias of the full-gradient-refresh PAGE specialization and was therefore inspected directly. Its primary analysis gives mean-square-error and convergence bounds under sufficient stepsize conditions, not an exact two-component lifted spectral boundary. The PAGE source supplies the \(p=b'/(b+b')\) formula and general sufficient average-smoothness theorem, but not this exact frontier. A 2026 PAGE Lyapunov analysis improves sufficient convex/weakly-convex bounds without giving a scalar second-moment phase diagram.

Focused semantic searches over PAGE and Loopless-SARAH aliases, scalar quadratics, mean-square stability, second moments, Schur/Jury criteria, and the radical formula found no covering statement. The main residual risk is an equivalent calculation in older stochastic-approximation or jump-linear-system literature.

## Value

PASS. The smallest heterogeneous PAGE finite sum already retains the method's defining competition between occasional exact refreshes and cheap recursive corrections. The source probability formula selects \(p=1/3\) for \(b=2\), \(b'=1\), making the model canonical rather than an arbitrary slice. The exact radical boundary quantifies how curvature heterogeneity erodes the stable stepsize and shows that affine noninterpolation noise cancels from this mechanism. It also measures the conservatism of general sufficient PAGE/L2S stepsize rules on a fully solvable benchmark.

Same-model review: passed. Independent audit: not yet performed.
