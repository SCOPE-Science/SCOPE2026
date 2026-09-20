# Sharp one-step objective frontier for scaled Polyak steps on SPD quadratics

## Setting

Let
\[
f(x)=f_*+\frac12 (x-x_*)^T A(x-x_*),
\qquad A=A^T\succ0,
\]
with spectrum contained in \([\mu,L]\), \(0<\mu\le L\), and condition number
\(\kappa=L/\mu\). Work in exact real arithmetic with the Euclidean gradient and
assume that the exact optimal value \(f_*\) is known.

For a scale parameter \(\gamma>0\), consider the scaled Polyak update
\[
x_+=x-\alpha\nabla f(x),\qquad
\alpha=\gamma\frac{f(x)-f_*}{\|\nabla f(x)\|_2^2}.
\]
Thus \(\gamma=1\) is the classical Polyak step, while \(\gamma=2\) is the
frequently studied doubled variant that is distance-optimal within this family on
SPD quadratics.

## Main theorem: exact worst one-step objective factor

For every nonoptimal \(x\),
\[
\boxed{
\frac{f(x_+)-f_*}{f(x)-f_*}
\le
Q_\gamma(\kappa)
:=1-\gamma+\frac{\gamma^2(\kappa+1)^2}{16\kappa}.
}
\]
The constant is sharp for every \(\kappa\ge1\) and every \(\gamma>0\): equality
is attained already in dimension two. Consequently the update is guaranteed to be
objective-nonincreasing for every SPD quadratic of condition number at most
\(\kappa\) if and only if
\[
\boxed{0<\gamma\le \Gamma(\kappa):=
\frac{16\kappa}{(\kappa+1)^2}.}
\]
For fixed \(0<\gamma\le4\), the equivalent sharp condition-number frontier is
\[
\boxed{
\kappa\le
\kappa_+(\gamma):=
\frac{8-\gamma+4\sqrt{4-\gamma}}{\gamma}.
}
\]
For \(\gamma>4\), universal one-step objective monotonicity fails even when
\(\kappa=1\).

Two notable special cases are
\[
\boxed{\gamma=1:\quad \kappa\le7+4\sqrt3\approx13.9282032303,}
\]
for the classical Polyak step, and
\[
\boxed{\gamma=2:\quad \kappa\le3+2\sqrt2\approx5.82842712475,}
\]
for the doubled Polyak step.

## Proof

Write \(e=x-x_*\) and
\[
S_j=e^T A^j e\qquad(j=1,2,3).
\]
Since \(f(x)-f_*=S_1/2\), \(\nabla f(x)=Ae\), and
\(\alpha=(\gamma/2)S_1/S_2\), direct expansion gives
\[
\frac{f(x_+)-f_*}{f(x)-f_*}
=1-\gamma+\frac{\gamma^2}{4}\frac{S_1S_3}{S_2^2}. \tag{1}
\]
It remains to solve the spectral-moment extremum in the last factor.

Diagonalize \(A\), write its eigenvalues as \(\lambda_i\in[\mu,L]\), and define
probabilities
\[
p_i=\frac{\lambda_i e_i^2}{S_1}.
\]
If \(\Lambda\) is the random variable taking value \(\lambda_i\) with
probability \(p_i\), then
\[
\frac{S_1S_3}{S_2^2}
=\frac{\mathbb E[\Lambda^2]}{\mathbb E[\Lambda]^2}.
\]
For every \(\lambda\in[\mu,L]\),
\[
\lambda^2\le(\mu+L)\lambda-\mu L.
\]
Putting \(m=\mathbb E[\Lambda]\) therefore yields
\[
\frac{\mathbb E[\Lambda^2]}{m^2}
\le \frac{(\mu+L)m-\mu L}{m^2}
\le \frac{(\mu+L)^2}{4\mu L}
=\frac{(\kappa+1)^2}{4\kappa}, \tag{2}
\]
where the scalar maximum occurs at \(m=2\mu L/(\mu+L)\). Combining (1) and
(2) proves the upper bound.

Both inequalities in (2) are simultaneously sharp on the two-point spectrum
\(\{\mu,L\}\): use probabilities
\[
p_\mu=\frac{L}{\mu+L},\qquad
p_L=\frac{\mu}{\mu+L}.
\]
Equivalently, after scaling \(\mu=1\), take
\[
A=\operatorname{diag}(1,\kappa),\qquad e=(\kappa,1)^T.
\]
Then equality holds in the theorem for every \(\gamma>0\). The monotonicity
frontiers follow by solving \(Q_\gamma(\kappa)\le1\).

## A minimax calibration

For a known condition number, minimizing the sharp one-step envelope over the scale
parameter gives
\[
\boxed{
\gamma_{\rm obj}^*(\kappa)=\frac{8\kappa}{(\kappa+1)^2},
\qquad
\min_{\gamma>0} Q_\gamma(\kappa)
=\left(\frac{\kappa-1}{\kappa+1}\right)^2.
}
\]
Thus the best condition-number-calibrated scaling of the Polyak formula has the
same sharp worst-case one-step objective factor as exact-line-search steepest
descent and optimal fixed-step gradient descent on the SPD quadratic class. This
is an equality of worst-case factors, not an assertion that the step choices agree
state by state.

## Objective increase despite distance decrease

The result separates Fejer-type distance behavior from objective monotonicity.
For the classical step \(\gamma=1\), take
\[
A=\operatorname{diag}(1,20),\qquad e=(20,1)^T.
\]
Then \(\alpha=21/80\) and
\[
\frac{f(x_+)-f_*}{f(x)-f_*}=1.378125>1,
\]
while
\[
\frac{\|e_+\|_2^2}{\|e\|_2^2}
=\frac{235.625}{401}<1.
\]
Hence a genuine objective spike can occur while the iterate moves substantially
closer to the minimizer in Euclidean distance. Moreover
\(Q_1(\kappa)\sim\kappa/16\), so the one-step objective amplification of the
classical Polyak rule is unbounded as the condition number grows.

## Relation to prior work

Polyak's 1969 target-value step is the classical origin of the rule. Barré,
Taylor and d'Aspremont (2020) distinguish the classical step, a doubled variant
optimized for distance control, and a separate descent-oriented variant. Huang
and Qi (2024) give a sharp analytic Euclidean-distance contraction for the Polyak
family on SPD quadratics; under their notation the classical and doubled rules
correspond to their parameters \(1/2\) and \(1\), respectively. Their theorem
controls Euclidean distance, whereas the result above determines the exact
objective-gap envelope and its monotonicity frontier.

Recent analyses by Orabona and D'Orazio (2025/2026) and by He, Gao, Jiang, Udell
and Zhang (2025/2026) substantially sharpen the general convergence picture and
identify worst-case functions or trajectories for PolyakGD, but the checked
statements do not give this all-state SPD quadratic one-step objective envelope or
the thresholds \(7+4\sqrt3\) and \(3+2\sqrt2\). The 2026 work of Wang et al. on
adaptive quadratic stepsizes instead targets convergence toward the optimal
constant step. Exact-line-search steepest descent has the classical sharp
objective factor \(((\kappa-1)/(\kappa+1))^2\), which supplies the comparison in
the minimax calibration above.

To the best of our knowledge, the closed-form envelope \(Q_\gamma(\kappa)\), its
sharp objective-monotonicity frontier, and the minimax calibration above were not
located in the checked literature. The historical literature on target-value and
subgradient steps is broad, however, and an equivalent two-moment inequality may
exist under different terminology.

## Reproducibility

`artifacts/verify.py` deterministically checks the equality family, the two sharp
thresholds, the minimax calibration, and random SPD instances against the proved
bound using NumPy. `artifacts/verification.txt` records the verified output.
Numerical checks support but do not replace the proof.

## Limitations

The theorem concerns exact arithmetic, unconstrained real SPD quadratics, the
Euclidean gradient, and exact knowledge of \(f_*\). It is a one-step worst-case
statement and does not by itself characterize long-run trajectories, finite-
precision behavior, stochastic gradients, inaccurate target values, constraints,
or nonquadratic objectives. The condition number is spectral in the Euclidean
metric. Historical-equivalence risk remains because the complete theorem-level
contents of some older Polyak/subgradient sources were not fully inspected.

## References

1. B. T. Polyak, *Minimization of Unsmooth Functionals*, USSR Computational Mathematics and Mathematical Physics 9(3), 14-29 (1969). https://doi.org/10.1016/0041-5553(69)90061-5
2. M. Barré, A. Taylor, A. d'Aspremont, *Complexity Guarantees for Polyak Steps with Momentum*, PMLR 125, 452-478 (2020). https://proceedings.mlr.press/v125/barre20a.html
3. Y.-K. Huang, H.-D. Qi, *Analytic analysis of the worst-case complexity of the gradient method with exact line search and the Polyak stepsize* (2024). https://arxiv.org/abs/2407.04914
4. F. Orabona, R. D'Orazio, *New Perspectives on the Polyak Stepsize: Surrogate Functions and Negative Results* (2025/2026). https://arxiv.org/abs/2505.20219
5. C. He, W. Gao, B. Jiang, M. Udell, S. Zhang, *New Results on the Polyak Stepsize: Tight Convergence Analysis and Universal Function Classes* (2025/2026). https://arxiv.org/abs/2512.06231
6. Y. Wang, L. Ballotta, R. Carli, X. Cao, L. Schenato, *Pursuing Optimal Stepsize in Adaptive Gradient-Based Quadratic Optimization* (2026). https://arxiv.org/abs/2608.03546
7. E. de Klerk, F. Glineur, A. Taylor, *On the worst-case complexity of the gradient method with exact line search for smooth strongly convex functions*, Optimization Letters 11, 1185-1199 (2017). https://doi.org/10.1007/s11590-016-1087-4
