# Sharp condition-number frontier for objective monotonicity of two-step cyclic steepest descent

## Finding

Let \(A\) be real symmetric positive definite on \(\mathbb R^n\), with \(n\ge1\) and spectral condition number \(\kappa=\lambda_{\max}(A)/\lambda_{\min}(A)\). For the quadratic energy
\[
q(x)=\frac12(x-x_*)^\top A(x-x_*),\qquad g=A(x-x_*),
\]
consider **one complete two-step cyclic steepest-descent cycle**: at its beginning compute
\[
\alpha=\frac{g^\top g}{g^\top A g},\qquad
x^+=x-\alpha g,\qquad
x^{++}=x^+-\alpha A(x^+-x_*).
\]
Both updates use the original \(\alpha\). Define
\[
T=\frac{5+3\sqrt3}{2},\qquad
\kappa_* = \frac{T+\sqrt{T^2-4}}2=4.893733238138796\ldots.
\]
Then **all complete cycles are objective-nonincreasing for every initialization and every real finite dimension if and only if \(\kappa\le\kappa_*\)**. At \(\kappa<\kappa_*\), the decrease is strict when \(g\neq0\). At the endpoint \(\kappa=\kappa_*\), a nonoptimal two-dimensional initialization attains equality. For each \(\kappa>\kappa_*\), a diagonal two-dimensional problem with condition number exactly \(\kappa\) has a nonempty open family of initializations with \(q(x^{++})>q(x)\).

This sharp boundary is a **cycle-boundary** assertion; the second individual step need not be descending.

## Assumptions and scope

All assertions use exact arithmetic. No restriction is placed on dimension, eigenvalue multiplicities, or initial spectral support; the initial point may be any \(x\in\mathbb R^n\). With \(g=0\), the algorithm is at its unique minimizer and a cycle is unnecessary. Positive rescaling of \(A\) leaves the cycle behavior invariant after simultaneously rescaling \(\alpha\), so normalize \(\lambda_{\min}(A)=1\), \(\lambda_{\max}(A)=\kappa\). If \(\kappa=1\), a single update reaches the minimizer; below assume \(\kappa>1\). All statements concern quadratic objective gaps, not gradient norms or Euclidean iterate norms.

## Proof

**1. A moment identity.** Let \(P_i\) be the orthogonal spectral projectors, with distinct eigenvalues \(\lambda_i\in[1,\kappa]\), and introduce normalized nonnegative weights \(p_i=\|P_i g\|^2/\|g\|^2\), summing to one. Write
\[
a=\sum_i p_i\lambda_i,\qquad m_2=\sum_i p_i\lambda_i^2,
\qquad m_3=\sum_i p_i\lambda_i^3.
\]
Here \(a\in[1,\kappa]\) and \(\alpha=1/a\). The spectral expression for the energy before and after two repeated updates is
\[
q(x)=\frac{\|g\|^2}{2}\sum_i\frac{p_i}{\lambda_i},\qquad
q(x^{++})=\frac{\|g\|^2}{2}\sum_i\frac{p_i}{\lambda_i}
\left(1-\frac{\lambda_i}{a}\right)^4.
\]
Expansion yields the exact, dimension-independent formula
\[
q(x^{++})-q(x)=\frac{\|g\|^2}{2a^4}\,S,\qquad
S=2a^3-4am_2+m_3. \tag{1}
\]

**2. Reduction to spectral endpoints or an unconditionally negative case.** The elementary pointwise bounds \((\lambda-1)(\kappa-\lambda)\ge0\) and \(\lambda(\lambda-1)(\kappa-\lambda)\ge0\), averaged over \(p_i\), give
\[
m_2\le(\kappa+1)a-\kappa,\qquad
m_3\le(\kappa+1)m_2-\kappa a.
\]
Thus
\[
S\le 2a^3+(\kappa+1-4a)m_2-\kappa a. \tag{2}
\]
If \(a\le(\kappa+1)/4\), the coefficient of \(m_2\) is nonnegative. Use the first bound to obtain
\[
S\le E_\kappa(a):=2a^3+(\kappa+1-4a)((\kappa+1)a-\kappa)-\kappa a. \tag{3}
\]
Both moment bounds are equalities when all nonzero spectral weights lie at the two endpoints \(1\) and \(\kappa\), with fixed mean \(a\). Hence it suffices to analyze two endpoints in this case.

If instead \(a>(\kappa+1)/4\), the coefficient in (2) is negative, and Jensen's inequality \(m_2\ge a^2\) yields
\[
S\le-a\{2a^2-(\kappa+1)a+\kappa\}. \tag{4}
\]
For \(1\le\kappa\le\kappa_*<3+2\sqrt2\), the quadratic in braces is strictly positive for every real \(a\): its leading coefficient is positive and its discriminant \(\kappa^2-6\kappa+1\) is negative. Therefore (4) is strictly negative throughout this case.

**3. Exact two-endpoint inequality.** Set \(A=\operatorname{diag}(1,\kappa)\), with a nonzero initial gradient proportional to \((1,\sqrt r)^\top\), \(r>0\). The first mean curvature is \(a=(1+\kappa r)/(1+r)\). The ratio of postcycle to initial energies is exactly
\[
R_\kappa(r)=\frac{(\kappa-1)^4(\kappa r^4+r)}{(1+\kappa r)^4(\kappa+r)}. \tag{5}
\]
Its denominator is positive. The difference between the denominator and numerator factors as
\[
(1+\kappa r)^4(\kappa+r)-(\kappa-1)^4(\kappa r^4+r)
=\kappa(1+r)^2Q_\kappa(r), \tag{6}
\]
where
\[
Q_\kappa(r)=\kappa^3r^3+(2\kappa^3-2\kappa^2+4\kappa-1)r^2
+(-\kappa^3+4\kappa^2-2\kappa+2)r+1. \tag{7}
\]
Consequently, \(R_\kappa(r)\le1\) is equivalent to \(Q_\kappa(r)\ge0\). The discriminant of this cubic with respect to \(r\) is
\[
4(\kappa-1)^6(\kappa^2+1)
(2\kappa^4-10\kappa^3+3\kappa^2-10\kappa+2). \tag{8}
\]
Dividing the last quartic by \(\kappa^2\) and setting \(z=\kappa+1/\kappa\) transforms it into \(2z^2-10z-1\). As \(\kappa\) runs over \([1,\infty)\), \(z\) increases from \(2\) to infinity; the unique zero in this range is \(T=(5+3\sqrt3)/2\). Hence (8) is negative for \(1<\kappa<\kappa_*\), zero at \(\kappa_*\), and positive above it.

For \(1<\kappa<\kappa_*\), a cubic with negative discriminant has exactly one real root. Since \(Q_\kappa(0)=1\) and \(Q_\kappa(r)\to-\infty\) as \(r\to-\infty\), that unique root is negative. Thus \(Q_\kappa(r)>0\) for all \(r\ge0\), including the limiting single-endpoint weights. At \(\kappa=\kappa_*\), continuity in \(\kappa\) gives \(Q_{\kappa_*}(r)\ge0\). Its discriminant vanishes; its derivative at zero is negative, since \(-\kappa_*^3+4\kappa_*^2-2\kappa_*+2<0\), so the cubic has a positive local minimum. A repeated root must occur there, and nonnegativity forces that minimum to equal zero. Thus equality is attained at a positive \(r\).

Combining the endpoint inequality with (3) proves nonincrease for all dimensions and all \(\kappa\le\kappa_*\). When \(\kappa<\kappa_*\), (3) is strictly negative for any nonzero endpoint mix or any single-endpoint gradient, and (4) is strictly negative otherwise; hence strict decrease. The case \(\kappa=1\) was already settled.

For \(\kappa>\kappa_*\), the cubic has three distinct real roots by (8). Its coefficient of \(r^2\) is positive, while its coefficient of \(r\) is negative. The polynomial \(Q_\kappa(-r)\) has one sign change, so Descartes' rule and \(Q_\kappa(-\infty)<0<Q_\kappa(0)\) give exactly one negative real root of \(Q_\kappa\). The remaining two roots are positive. Between them \(Q_\kappa(r)<0\), hence (5) exceeds one. Strictness and continuity in the initial gradient give an open set of ascent-producing initial points.

**4. Explicit rational witness.** For \(A=\operatorname{diag}(1,5)\), \(x_*=(0,0)^\top\), and initial gradient \(g=(4,1)^\top\), the initial point is \(x=(4,1/5)^\top\). The cycle uses \(\alpha=17/21\) twice; exact arithmetic gives
\[
q(x)=\frac{81}{10},\qquad
q(x^{++})=\frac{2799616}{324135},\qquad
\frac{q(x^{++})}{q(x)}=\frac{5599232}{5250987}>1.
\]
This also demonstrates that objective increases may occur even though the first step is an exact line-search step.

## Verification

The included `csd2_cycle_verify.py` checks identities (6) and (8), the endpoint moment reduction, the algebraic characterization of \(\kappa_*\), and the explicit rational witness. Invoke `python3 csd2_cycle_verify.py` with Python 3 and SymPy installed; the script returns `VERIFY_OK` when its checks pass. The proof above covers all positive dimensions and all real spectral parameters; neither finite numerical sampling nor the checker substitutes for the moment and polynomial-sign arguments.

## Relationship to prior work

Ran Gu, arXiv:2609.25800v1, defines cyclic steepest descent and proves almost-everywhere doubly exponential *asymptotic* convergence for certain eigenvalue-count/cycle-length regimes. The present assertion instead classifies *one-cycle objective monotonicity for all dimensions and all initial points*, with a sharp condition-number boundary; it does not follow from asymptotic decay.

Li and Wang, arXiv:2610.00939v1 (earlier Zenodo DOI:10.5281/zenodo.22209278), construct exact exceptional non-superlinear CSD orbits, including a two-spectral balanced example and a three-spectral projective period-two orbit. Their existence and contraction calculations do not establish a uniform objective monotonicity threshold. Shen, Li, and Dai, arXiv:2501.16731v2, analyze CSD and a distinct triangle steepest-descent algorithm; those rate results are not objective-cycle inequalities. Friedlander, Martínez, Molina, and Raydan (1999) prove global convergence for delayed gradient schemes. The earlier Dai–Fletcher (2005) work addresses asymptotic behavior; full-text comparison of the latter remains a specifically noted access limitation.

## Limitations

The theorem concerns only exactly computed, reused steepest-descent steps on **positive-definite quadratics**, for **two updates per cycle**. It does not establish descent at each inner update, global rates, generic-orbit behavior, robustness to inexact gradients, or analogous thresholds for longer cycles, nonquadratic objectives, or indefinite matrices. A relevant older paper by Dai and Fletcher was not available in complete text despite attempted accessible-source and institutional retrieval; an unindexed equivalent result remains a residual originality risk. Same-model proof and literature review are not independent validation.

## References

1. R. Gu, *Doubly exponential convergence of the cyclic steepest descent method for strictly convex quadratics in arbitrary dimensions*, arXiv:2609.25800v1 (first posted 2026-09-22), https://arxiv.org/abs/2609.25800.
2. Y. Li and Q. Wang, *Exact counterexamples to R-superlinear convergence of cyclic steepest descent*, arXiv:2610.00939v1 (2026), https://arxiv.org/abs/2610.00939; earlier version DOI:10.5281/zenodo.22209278.
3. Y. Shen, Q.-N. Li, and Y.-H. Dai, *Triangle Steepest Descent: A Geometry-Based Gradient Algorithm with Guaranteed R-Linear Convergence*, arXiv:2501.16731v2 (2025), https://arxiv.org/abs/2501.16731.
4. A. Friedlander, J. M. Martínez, B. Molina, and M. Raydan, *Gradient method with retards and generalizations*, SIAM J. Numer. Anal. 36 (1999), 275–289, DOI:10.1137/S003614299427315X.
5. Y.-H. Dai and R. Fletcher, *On the asymptotic behaviour of some new gradient methods*, Math. Program. 103 (2005), 541–559, DOI:10.1007/s10107-004-0516-9.
