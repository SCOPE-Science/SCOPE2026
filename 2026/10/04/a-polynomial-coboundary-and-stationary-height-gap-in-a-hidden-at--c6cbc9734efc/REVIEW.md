# Review

## Correctness
PASS. The exact polynomial
\[
G=z+\frac12(x+y)^2+\frac{11}{10}x+\frac{1}{10}y+\frac{3}{20}x^2
\]
satisfies \(LG=a+5y-x^2\) for the published vector field. Together with the elementary generator identities for \(x\), \(y\), \(x^2/2\), \((x+y)^2/2\), and \(xy\), this gives the stated stationary mean and covariance laws. The variance inequality is exactly \(\operatorname{Var}(x+y)\ge0\). Equality forces the invariant support onto the equilibrium, so the strict non-equilibrium statements are justified. A packaged exact-arithmetic checker replays the algebra.

## Originality
PASS. The primary 2018 open-access article was inspected directly. It studies equilibria, numerical bifurcations, Lyapunov exponents, entropy, parameter estimation, and circuit implementation, but does not state the coboundary or all-invariant-measures laws. Targeted exact-equation and exact-source searches, together with semantic searches for stationary-balance analogues, located no equivalent result. The closest results concern different ODEs and do not imply this claim. A residual risk remains for unindexed work or an equivalent identity written under substantially different coordinates.

## Value
PASS. The article's central qualitative feature is coexistence of a stable equilibrium with hidden non-equilibrium dynamics. The theorem gives an exact statistical separation: every non-equilibrium compact stationary state has mean \(y\) strictly above the equilibrium ordinate and a strict variance floor tied to \(\langle x^2\rangle\). It also yields a nontrivial amplitude constraint for every periodic orbit. These exact constraints can be used to validate long numerical runs or circuit realizations and sharpen the source's predominantly numerical dynamical description.

The result does not claim to prove the existence or hiddenness of the source's numerical attractor, nor does it determine its basin or physical measure.

Same-model review: passed. Independent audit: not yet performed.
