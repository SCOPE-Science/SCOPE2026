# Self-review

## Correctness
PASS. Each diagonal mode has an exact two-state error matrix with determinant \(0\) and trace
\[
\zeta_i=1-\frac{\alpha\rho(a_i+b_i)}{(\rho+a_i)(\rho+b_i)}.
\]
Cayley--Hamilton gives \(M_i^2=\zeta_iM_i\), so finite termination for every initialization is equivalent to \(\zeta_i=0\) in every mode. Solving those equations gives the line criterion and \(0<\tau\le\rho\). The rational witness is replayed by `verify.py`.

## Originality
PASS. Ghadimi--Teixeira--Shames--Johansson prove the zero-factor result for an isotropic second quadratic with Hessian \(\delta I\), and their general-Hessian change of variables alters the augmented metric in the original coordinates. This finding instead fixes one scalar Euclidean penalty and gives a necessary-and-sufficient heterogeneous curvature-line criterion. Giselsson--Boyd provide broader metric-selection theory but do not state this scalar-penalty classification. Targeted statement-level literature searches found no implication-equivalent result.

Residual risk remains that older quadratic Douglas--Rachford literature may contain an equivalent simultaneous-diagonalization formula from which the line condition follows implicitly.

## Value
PASS. Exact finite termination is a natural endpoint of ADMM tuning. The line geometry answers when a single scalar penalty and one standard relaxation can annihilate all modes despite two heterogeneous diagonal Hessians, and distinguishes that scalar possibility from matrix-valued preconditioning.

## Closest literature and limitations
The closest direct source is Ghadimi et al. (first public posting 2013-06-10), which contains the isotropic \(\delta I\) zero-factor formula. Giselsson--Boyd supplies the closest broader metric-selection framework. The theorem is limited to positive diagonal Hessians in the Euclidean coordinates of the scalar penalty, exact arithmetic, and constant parameters.

Self-review: passed. Independent audit: not yet performed.
