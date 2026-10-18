# Flooding on a scalar quadratic: log-radius rotations, ergodic calibration, and an exact-solve collapse

## Finding

Let \(a,b>0\), \(f(x)=ax^2/2\), \(r=\sqrt{2b/a}\), and let the deterministic Flooding update minimize \(\widetilde f(x)=|f(x)-b|+b\) with fixed stepsize \(\eta>0\). Put \(h=\eta a\). At the nonsmooth boundary we use the explicit selection \(\operatorname{sign}(0)=0\). Thus
\[
 x^+=\begin{cases}(1-h)x,&|x|>r,\\ x,&|x|=r,\\(1+h)x,&0<|x|<r,\\0,&x=0.\end{cases}
\]

**Rotation regime.** Fix \(0<h<1\) and a **nonzero** initial point whose orbit never reaches \(|x|=r\). (The excluded nonzero boundary-preimage set is countable.) The sign of \(x\) is invariant. Define
\[
 A=\log(1+h),\qquad B=-\log(1-h),\qquad L=A+B,\qquad\rho=A/L\in(0,1/2).
\]
After finitely many iterates, \(u_t=\log(|x_t|/r)\) belongs to \((-B,A)\) and obeys
\[
 u_{t+1}=\begin{cases}u_t+A,&u_t<0,\\u_t-B,&u_t>0.\end{cases}
\]
Equivalently \(s_t=u_t+B\in(0,L)\) is a rotation \(s_{t+1}=s_t+A\pmod L\). Coordinates at the endpoints are identified on the circle; the no-boundary-hit assumption prevents the singular \(u=0\) trajectory. If \(\rho=p/q\) in lowest terms, every such post-transient orbit consists of exactly \(q\) distinct log radii. If \(\rho\) is irrational, each post-transient orbit is dense in \([-B,A]\) and is equidistributed with respect to normalized Lebesgue measure.

For every non-boundary orbit, rational or irrational, the asymptotic fraction of iterates with raw loss \(f(x_t)>b\) is \(\rho\). **For irrational \(\rho\) only**, unique ergodicity gives the phase-independent statistics
\[
 \boxed{\lim_{T\to\infty}\frac1T\sum_{t<T}f(x_t)=\frac{bh}{\operatorname{artanh}(h)}<b},
 \qquad
 \boxed{\exp\!\left(\lim_{T\to\infty}\frac1T\sum_{t<T}\log f(x_t)\right)=b(1-h^2)}.
\]
For such irrational rotations, the **closure of the set of post-transient raw loss values** is exactly
\[
 \boxed{[b(1-h)^2,b(1+h)^2]}.
\]
For **rational \(\rho=p/q\)**, the closure is instead the \(q\)-point orbit \(\{b\exp(2u_t):0\le t<q\}\), which is contained in that interval and depends on the initial phase. Its arithmetic and geometric time means are the corresponding finite averages, not in general the irrational-rotation formulas. The asymptotic frequency above \(b\) nevertheless remains \(p/q\), since each boundary-avoiding \(q\)-cycle has precisely \(p\) iterates in the arc \((0,A)\).

A simple exact resonance is \(h=(\sqrt5-1)/2\). Then \(B=2A\), \(\rho=1/3\), and every non-boundary post-transient orbit has period exactly three. In particular, this resonance gives an explicit **counterexample** to the unqualified claim that every post-transient orbit has the full loss band as its closure.

**Exact-solve endpoint.** At \(h=1\), any iterate with \(|x|>r\) maps directly to zero; a nonzero iterate strictly below \(r\) doubles in magnitude. Hence every nonzero initial point outside the discrete family
\[
 \boxed{|x_0|=r2^{-n},\qquad n\in\{0,1,2,\ldots\}}
\]
reaches \(x=0\) after finitely many steps and remains there. Each exceptional initialization reaches \(|x|=r\) exactly and remains fixed under the stated kink convention. Zero is itself fixed. Thus the underlying quadratic's exact-solve step can make Flooding terminate at **zero raw loss**, despite the motivation for flooding.

## Assumptions and scope

The model is deterministic full-batch gradient descent on the exact nonsmooth objective, in one real variable, with a fixed \(a,b>0\) and no momentum, minibatch noise, adaptivity, or other coupling. The rotation conclusions require \(0<h<1\), \(x_0\ne0\), and non-contact with the threshold. For the rational-rotation regime, asymptotic averages generally depend on phase and **must not** be identified with unique-ergodic integrals. The separate \(h=1\) statement uses \(\operatorname{sign}(0)=0\) as the subgradient choice at \(|x|=r\). The proofs address optimization dynamics and do not infer generalization performance from mean training loss.

## Proof

Away from \(|x|=r\), \(\nabla f(x)=ax\) and the gradient of the flooded objective is \(\operatorname{sign}(f(x)-b)ax\). Thus the displayed multiplicative update is exact, with multipliers \(1+h\) on the interior and \(1-h\) on the exterior. For \(0<h<1\) both multipliers are positive, preserving the sign and nonzeroness of an initial nonzero state.

Taking \(u=\log(|x|/r)\) yields the two translations \(+A\) for \(u<0\) and \(-B\) for \(u>0\). Any negative \(u\) advances in finite increments of \(A\) until it first crosses zero, at which point it is below \(A\); any positive \(u\) decreases by \(B\) until it first crosses zero, at which point it lies above \(-B\). Boundary-contact trajectories are excluded. This establishes finite entry into the invariant interval \((-B,A)\). Setting \(s=u+B\) makes the two branches a common displacement by \(A\) modulo \(L=A+B\). Standard circle-rotation theory now gives exact periods for rational \(\rho\) and dense equidistribution for irrational \(\rho\). Since \(0<A<B\), \(\rho\in(0,1/2)\).

The set of above-threshold iterates corresponds to \(u\in(0,A)\), an arc of normalized length \(A/L=\rho\). For irrational rotations equidistribution yields this frequency. If \(\rho=p/q\) is rational, equally spaced \(q\)-point orbits partition the circle into \(q\) equal arcs; because the orbit does not touch the arc endpoints, exactly \(p\) orbit points lie in the interval of length \(pL/q=A\), so the frequency is again \(p/q\). Boundary hits cannot be included in this argument, as the specified update stops there.

For irrational \(\rho\), the raw loss is \(f=be^{2u}\). Its circle-integral mean is
\[
 \frac{b}{L}\int_{-B}^{A}e^{2u}\,du
 =\frac{b(e^{2A}-e^{-2B})}{2L}
 =\frac{b((1+h)^2-(1-h)^2)}{2L}
 =\frac{2bh}{L}
 =\frac{bh}{\operatorname{artanh}(h)}.
\]
The inequality follows from \(\operatorname{artanh}(h)>h\) for \(0<h<1\). The mean logarithm of the raw loss equals \(\log b+2(-B+A)/2\), giving the geometric mean \(b e^{A-B}=b(1-h^2)\). Density of irrational log radii and continuity of \(u\mapsto be^{2u}\) yield the **closed** loss band as the closure of the orbit. Conversely, rational rotations have only \(q\) distinct log radii, hence a finite loss-set closure and initial-phase-dependent raw-loss mean; a finite orbit is not dense in an interval. These distinctions are essential to the exact statements.

For \(h=(\sqrt5-1)/2\), the identity \(1-h=(1+h)^{-2}\) gives \(B=2A\) and \(\rho=1/3\). The no-contact orbit has exact period three. For \(h=1\), the exterior descent multiplier is zero and the interior ascent multiplier is two. A nonzero interior initial magnitude reaches the boundary exactly iff \(2^n|x_0|=r\) for some \(n\ge0\); otherwise it crosses in finitely many doublings and the following exterior update reaches zero. An initially exterior state reaches zero in one step, and both zero and the boundary are fixed under the stated convention. This proves the endpoint classification.

## Verification

A separate mathematical check verifies the exact three-cycle, explicitly demonstrate variation of the three-cycle's arithmetic loss mean with initial phase (and therefore the falsehood of a universal loss-band closure at rational rotation), and test the \(h=1\) collapse on representative nonexceptional starts. These finite checks are corroboration of the analytic proof above, not a replacement for the unrestricted rotation and doubling arguments. The global full-band assertion must be restricted to irrational rotations, and the zero initialization is explicitly excluded from logarithmic coordinates.

## Relationship to prior work

Ishida, Yamane, Sakai, Niu and Sugiyama, *Do We Need Zero Training Loss After Achieving Zero Training Error?* (ICML 2020, arXiv:2002.08709), introduce the Flooding objective and describe the alternating ascent/descent mechanism. Their defining article does not in the inspected material give this deterministic scalar rigid-rotation conjugacy, rational phase distinction, ergodic raw-loss calibration, or exact-solve collapse. Karakida, Takase, Hayase and Osawa, *Understanding Gradient Regularization in Deep Learning* (arXiv:2210.02720), discuss local two-step Flooding-related regularization. Holland and Nakatani, *Soft ascent-descent as a stable and flexible alternative to flooding* (arXiv:2310.10006), analyze stabilization and numerical examples. A separate known Fromage-optimizer calculation also exhibits a shifted-quadratic log-coordinate rotation, but its update and threshold mechanism are different; it does not imply these Flooding-specific raw-loss averages and exact-solve behavior. The rigid-rotation theorem itself is standard; novelty, if any, is its exact specialization and consequences for this optimizer. An unnoticed equivalent one-dimensional analysis remains a publication-priority risk.

## Limitations

This is a scalar deterministic model, not a stochastic training theorem. It neither bounds generalization error nor asserts convergence to the minimizer for \(0<h<1\). At rational rotation numbers finite orbits need not exhibit the irrational time-integral means and do not fill the loss band. The boundary subgradient convention controls a countable family of exceptional trajectories. The endpoint collapse is specific to \(h=1\) and is not a generic small-step behavior. Independent literature-priority assessment remains qualified by the inspected-source coverage.

## References

1. T. Ishida, I. Yamane, T. Sakai, G. Niu and M. Sugiyama, *Do We Need Zero Training Loss After Achieving Zero Training Error?*, ICML 2020, PMLR 119; https://proceedings.mlr.press/v119/ishida20a/ishida20a.pdf (arXiv:2002.08709).
2. R. Karakida, T. Takase, T. Hayase and K. Osawa, *Understanding Gradient Regularization in Deep Learning: Efficient Finite-Difference Computation and Implicit Bias*, arXiv:2210.02720.
3. M. J. Holland and K. Nakatani, *Soft ascent-descent as a stable and flexible alternative to flooding*, arXiv:2310.10006.
