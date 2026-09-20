# Same-model review

Same-model review: passed. Independent audit: not yet performed.

## Correctness

**PASS.** The proof separates the untruncated and boundary Cauchy regimes. In the
untruncated regime, the exact trust-region decrease is bounded above by the full
Newton decrease, giving the fixed-gradient factor immediately. In the boundary
regime, every feasible step is written as \(-\Delta v\); the desired domination
reduces to an affine function of the normalized radius. Its two endpoint
inequalities follow from ordinary Cauchy--Schwarz, weighted Cauchy--Schwarz and
AM--GM. This proves the same factor for every radius. Kantorovich then yields the
condition-number envelope, with its standard two-extreme-eigenspace equality case.

The sharpness statement was checked carefully: when the trust region contains the
Newton and unconstrained Cauchy steps, the ratio is exactly
\(1/[(u^TBu)(u^TB^{-1}u)]\). The two-dimensional matrix
\(\operatorname{diag}(\mu,L)\) with equal gradient energy in the extreme
eigendirections attains the Kantorovich equality. The fraction-of-Cauchy conversion
is sharp because any prescribed fraction \(\gamma\in(0,1]\) can be attained on the
Cauchy segment in the same equality family. A simple negative-curvature example
confirms that positive definiteness is essential.

Deterministic numerical checks independently solve the SPD trust-region subproblem
by a secular-parameter bisection, reproduce the sharp family for several condition
numbers, and test the fixed-gradient inequality over multiple non-diagonal matrices
and trust radii.

## Originality

**PASS, to the best of our knowledge.** The checked classical sources establish the
Cauchy point, fraction-of-Cauchy decrease, and the exact trust-region model minimizer
as standard objects. Conn--Scheinberg--Vicente explicitly note that a
fraction-of-optimal-decrease condition is stronger than the usual Cauchy/eigenstep
conditions in the general trust-region setting. The classical Kantorovich inequality
supplies the full-space steepest-descent versus Newton condition-number factor.

Searches were carried out under Cauchy point/step, fraction of optimal decrease,
trust-region approximation ratio, SPD/positive-definite trust-region models,
condition number, Kantorovich inequality, gradient direction, and equivalent
formulations. They did not locate the statement that the full-space Kantorovich
fraction remains valid for every trust radius, nor the resulting sharp implication
from fraction-of-Cauchy to fraction-of-optimal decrease for uniformly SPD quadratic
models.

The main residual originality risk is historical equivalence in broad classical
sources. The theorem-level contents of all relevant portions of Conn--Gould--Toint,
Nocedal--Wright, Dennis--Schnabel, and older Powell trust-region papers were not all
available for complete line-by-line checking. Those sources could contain an
equivalent inequality under different terminology. This uncertainty is material and
is retained explicitly.

## Value

**PASS.** The result gives a sharp, radius-independent quality certificate against
the exact trust-region optimum using only the gradient-direction curvature and an
inverse quadratic form, and a sharp condition-number-only form depending on no
radius. More directly, it bridges two standard trust-region sufficient-decrease
notions: on uniformly SPD models, any fraction-of-Cauchy guarantee automatically is
a quantitatively explicit fraction-of-optimal guarantee. The metric version gives
the corresponding preconditioned statement.

## Scientific limitations

The theorem concerns exact arithmetic and predicted decrease for real SPD quadratic
models. It does not cover indefinite or singular Hessian models, actual reduction of
a nonquadratic objective, step-distance approximation, finite-precision stability,
or runtime complexity. Exact trust-region, dogleg, Steihaug-CG, Lanczos and related
subproblem solvers may produce substantially better steps; the result is a sharp
quality floor for the Cauchy benchmark, not an optimality claim for using Cauchy
steps in practice. Broad historical trust-region literature leaves residual
prior-coverage risk. Independent audit has not been performed.
