# Zero-probe curvature: convex sufficiency and an unbounded nonconvex SQP–SQCQP gap

## Finding
Consider two optimization subproblems that share the same strongly convex quadratic objective but differ in their inequality constraints: the SQP model keeps the affine part, whereas the SQCQP model adds the quadratic constraint-curvature correction. An indicator that tests only the *value* of the correction at the SQP direction has a precise safe case and a sharp structural limitation.

**Convex sufficiency.** For a common strictly convex objective and positive-semidefinite quadratic corrections, an SQP minimizer with zero correction for every constraint is also the unique SQCQP minimizer.

**Unbounded nonconvex blind spot.** In two dimensions, a smooth indefinite quadratic inequality with bounded Hessian admits an entire family in which this correction is exactly zero at the SQP direction, yet the SQCQP optimum is arbitrarily far away and arbitrarily better. The SQP direction fails even the KKT stationarity condition of the quadratic model. Hence zero scalar probe curvature is not an objective-gap or direction-gap certificate without further structural assumptions.

## Assumptions and scope
Fix a symmetric positive-definite matrix \(B\in\mathbb R^{n\times n}\), vector \(g\in\mathbb R^n\), and finitely many affine functions \(\ell_j(d)=a_j^{\mathsf T}d+b_j\). Define
\[
Q(d)=g^{\mathsf T}d+\tfrac12d^{\mathsf T}Bd,\qquad
q_j(d)=\tfrac12d^{\mathsf T}H_jd.
\]
Assume the affine system is feasible and the SQP minimum is attained. Strict convexity then gives its unique minimizer \(d_L\). The SQCQP subproblem minimizes exactly the **same** \(Q\), subject to \(\ell_j(d)+q_j(d)\le0\). The positive statement below assumes all \(H_j\succeq0\) and all \(q_j(d_L)=0\). It concerns inequalities only; nonlinear equality constraints need a separate argument.

For the negative statement fix any real \(r>1\) and \(m>0\). At the base point \(x^0=(0,0)\), use the analytic constraint
\[
c(x,y)=y-xy\le0
\]
and the positive-definite exact quadratic objective
\[
F_{r,m}(x,y)=\tfrac12(x-r)^2+\tfrac12(y-m)^2.
\]
The two local objective matrices are both \(I_2\), and the stochastic gradient estimator is set equal to the exact gradient at this point. We compare **global minima of the two precisely specified local subproblems**; no claim is made that an actual nonconvex SQCQP implementation will find its global minimum.

The relative constraint-curvature indicator in Tiwari and Ansary (2026) computes the absolute quadratic correction at the SQP probe divided by a strictly positive normalization; its smoothing initializes at zero and its low switching threshold is positive. Only those properties are needed for the example, so the outcome does not depend on the normalization constants.

## Proof
**1. Positive-semidefinite sufficiency.** If \(H_j\succeq0\), then \(q_j(d)\ge0\) for every \(d\). Thus every quadratically feasible point satisfies \(\ell_j(d)\le -q_j(d)\le0\). Consequently the SQCQP feasible set is contained in the SQP feasible set. The assumed \(q_j(d_L)=0\) and \(\ell_j(d_L)\le0\) show that \(d_L\) lies in both sets. Since it minimizes \(Q\) on the larger SQP set, it also minimizes \(Q\) on the smaller SQCQP set. Strict convexity gives uniqueness. The argument does not require any numerical tolerance or an assumption about the active set.

**2. The nonconvex quadratic-model geometry.** At \((0,0)\), the constraint value is zero, its gradient is \((0,1)\), and its constant Hessian is
\[
H=\begin{pmatrix}0&-1\\-1&0\end{pmatrix}.
\]
Its eigenvalues are \(1,-1\), hence \(\|H\|_2=1\); the base constraint gradient also has norm one, so LICQ holds there. Taylor expansion is exact and gives the SQP and SQCQP constraints
\[
\ell(x,y)=y\le0,\qquad \ell(x,y)+q(x,y)=y-xy=y(1-x)\le0,
\qquad q(x,y)=-xy.
\]
For \(r>1\), \(m>0\), the strictly convex objective \(F_{r,m}\) is minimized on the affine half-space \(y\le0\) uniquely at \(d_L=(r,0)\). Thus \(q(d_L)=0\), regardless of \(r,m\). The source's normalized raw indicator is therefore \(\eta_0=0\) for every strictly positive scale denominator. With initial smoothed indicator zero, its switching rule selects SQP at this initial model comparison for any positive lower threshold.

**3. Quadratic-model optimum and unbounded gap.** The unconstrained minimizer of \(F_{r,m}\) is \(d_Q=(r,m)\). It is strictly feasible in the quadratic subproblem because \(m(1-r)<0\). It is therefore the unique global SQCQP minimizer. Direct evaluation yields
\[
F_{r,m}(d_L)=\frac{m^2}{2},\quad F_{r,m}(d_Q)=0,\quad
\|d_Q-d_L\|_2=m.
\]
Letting \(m\) grow proves that neither gap is bounded by any finite function of the raw indicator value zero, with objective matrices and constraint Hessian kept fixed.

**4. First-order failure at the probe.** The model-objective gradient at \(d_L\) is \((0,-m)\). The quadratic constraint gradient there is \((0,1-r)\), pointing in the *opposite* vertical direction from its affine approximation. Stationarity with the required multiplier \(\mu\ge0\) would impose
\[
-m+\mu(1-r)=0,
\qquad\mu=\frac{m}{1-r}<0,
\]
a contradiction. More directly, \((r,t)\) is quadratically feasible for every \(t>0\), and the objective decreases from \(d_L\) whenever \(0<t<2m\). Hence the SQP point is not even a local solution of the quadratic subproblem. This occurs because \(d_L^{\mathsf T}Hd_L=0\) does *not* imply \(Hd_L=0\) for an indefinite Hessian. In contrast, for \(H\succeq0\) it does imply \(Hd_L=0\), consistent with the positive statement.

## Verification
Run the included standalone `verify.py` with Python 3 (standard library only). It reconstructs exact rational model values and constraint inequalities over 16,269 parameter instances and separately checks nine positive-semidefinite control instances. Its output is `PASS: 16269 nonconvex exact-rational witness cases; 9 convex control cases`. The program confirms the sign and algebra checks but cannot certify universal quantifiers. The argument above proves those conclusions for every stated \(r,m\) and every valid positive-semidefinite family.

## Relationship to prior work
Tiwari and Ansary, *Adaptive Variance-Reduced Stochastic Sequential (Quadratic Constrained) Quadratic Programming* (arXiv:2610.18428, publicly submitted 2026-10-13), introduce a normalized SQP-probe curvature magnitude and a hysteretic SQP/SQCQP selection rule. Equations (4)–(5) define the competing subproblems, and Section 3.1 defines the indicator and switching. Their local direction-comparison result (Section 4.2) imposes a small-step, strongly regular local regime; the present nonlocal family does not contradict that local theorem. This result concerns a question not settled by their vanishing-indicator property: whether a zero correction *at the probe* certifies that the two local optimization problems have similar minimizers.

Solodov's 2004 SQCQP framework uses positive-semidefinite quadratic constraint surrogates and slack variables, and earlier convex SQCQP work by Fukushima, Luo and Tseng (2003) concerns convex inequality models. Those methods clarify the importance of convexity, but their documented assumptions do not imply a zero-indicator discrepancy bound for the indefinite 2026 source formulation. The elementary positive-semidefinite implication is recorded as a comparison boundary, not asserted to be a standalone historical discovery.

## Limitations
The negative result addresses an exact single-step model-selection diagnostic and exact subproblem global optima, not full algorithm convergence, Armijo step acceptance, or stochastic sample complexity. The counterexample uses an indefinite, thus nonconvex, quadratic inequality and is outside the small-step local regime of the source's stability theorem. Its objective gap grows with the target parameter \(m\); a bound additionally incorporating problem-scale quantities may remain possible. This document does not claim novelty of the elementary convex inclusion argument, and broader historical priority of the nonconvex probe-blindness construction has not been independently certified.

## References
1. G. Tiwari and M. A. T. Ansary, *Adaptive Variance-Reduced Stochastic Sequential (Quadratic Constrained) Quadratic Programming*, arXiv:2610.18428v1 (2026), Sections 2.1, 3.1, 4.2; https://arxiv.org/abs/2610.18428.
2. M. V. Solodov, *On the Sequential Quadratically Constrained Quadratic Programming Methods*, Mathematics of Operations Research 29 (2004), 64–79, doi:10.1287/moor.1030.0069; https://pages.cs.wisc.edu/~solodov/mvs04sqcqp.pdf.
3. M. Fukushima, Z.-Q. Luo and P. Tseng, *A Sequential Quadratically Constrained Quadratic Programming Method for Differentiable Convex Minimization*, SIAM Journal on Optimization 13 (2003), 1098–1119, doi:10.1137/S1052623401398120.
