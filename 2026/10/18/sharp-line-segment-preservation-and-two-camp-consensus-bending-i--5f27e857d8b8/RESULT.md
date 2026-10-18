# Sharp line-segment preservation and two-camp consensus bending in multidimensional opinion formation

## Finding

Consider the two-topic continuum opinion model with initial law consisting of two fixed-importance camps. For the affine influence response \(\phi(s)=1-s/2\), the two opinion vectors converge to one common vector in the *interior of their original coordinate rectangle*. Nevertheless, the common vector need not lie on the line segment joining the two initial opinion vectors.

Let \(0<p<1\), \(x^0,y^0\in[-1,1]^2\), and \(0<a=y^0_1-x^0_1<2\), \(0<b=y^0_2-x^0_2<2\). The first camp has mass \(p\) and importance vector \(\alpha=(\alpha_1,1-\alpha_1)\), the other has mass \(1-p\) and importance vector \(\eta=(\eta_1,1-\eta_1)\), with \(\alpha_1,\eta_1\in[0,1]\). Fix the topicwise-locality parameter \(\beta\in[0,1]\). If \(z\) is the common limiting opinion, define \(\theta_j=(z_j-x^0_j)/(y^0_j-x^0_j)\).

**Sharp classification.** The limit \(z\) belongs to the original segment \([x^0,y^0]\) if and only if at least one of
\[
\beta=0,\qquad \beta=1,\qquad a=b,\qquad \alpha_1=\eta_1
\]
holds. If all four equalities fail, the two segment parameters are different, and
\[
\operatorname{sgn}(\theta_2-\theta_1)=\operatorname{sgn}(\alpha_1-\eta_1).
\]
In particular, the transverse direction is independent of which topic has the greater initial opinion gap.

**Sharp weak-locality onset.** Hold the other parameters fixed, put \(\bar\alpha=(1-p)\alpha+p\eta\) and \(c=(\bar\alpha_1a+\bar\alpha_2b)/2\in(0,1)\). As \(\beta\downarrow0\),
\[
\theta_2-\theta_1=\frac{\beta p(1-p)(\alpha_1-\eta_1)(a-b)^2}{4}J(c)+O(\beta^2),\qquad
J(c)=\frac{c+\log(1-c)+\tfrac12\log^2(1-c)}{c^3}>0.
\]
These assertions concern the two-atomic mean-field system, not random finite-population realization or arbitrary multi-camp distributions.

## Assumptions and scope

For any topic \(j\in\{1,2\}\), source-camp importance \(w\in\{\alpha,\eta\}\), and nonnegative gap vector \(d=(d_1,d_2)\), use the original model's topicwise perceived disagreement
\[
s_j(d;w)=\beta d_j+(1-\beta)(w_1d_1+w_2d_2),\qquad \Phi_j^w(d)=\phi(s_j(d;w)),\quad \phi(s)=1-s/2.
\]
The source defines importance vectors in the simplex and a nonincreasing Lipschitz influence function on \([0,2]\). The strict initial gaps make all subsequent perceived distances strictly below \(2\), hence every \(\Phi_j^w\) remains uniformly positive. The two-atomic solution consists of camp positions \(x(t),y(t)\) carrying fixed weights \(p,1-p\) and fixed importance vectors \(\alpha,\eta\). We study the original nonlocal first-order opinion dynamics in its mean-field characteristic form. Here \(z\in[x^0,y^0]\) means membership in the Euclidean straight line segment, not merely the coordinate rectangle.

## Proof

**1. Exact two-atomic characteristics and contraction.** With \(d_j(t)=y_j(t)-x_j(t)\), the model's Vlasov characteristic velocities restrict to
\[
\dot x_j=(1-p)\Phi_j^\alpha(d)d_j,\qquad
\dot y_j=-p\Phi_j^\eta(d)d_j.
\]
Define \(\bar\alpha=(1-p)\alpha+p\eta\). Subtraction yields
\[
\dot d_j=-H_j(d)d_j,\qquad
H_j(d)=1-\tfrac12\bigl(\beta d_j+(1-\beta)\bar\alpha\cdot d\bigr).
\]
Initially \(d_1=a\), \(d_2=b\). Both gaps remain strictly positive at every finite time and decrease monotonically, with \(H_j\ge1-\max(a,b)/2>0\). They therefore decay exponentially. Each \(x_j\) increases and each \(y_j\) decreases; since \(d_j\to0\), their limits agree at a point \(z\), and \(x_j^0<z_j<y_j^0\).

**2. Persistent ordered splitting.** Set \(q_1=d_1/a\), \(q_2=d_2/b\); they are positive and start at \(1\). The exact difference of contraction rates gives
\[
\frac{d}{dt}\log\frac{q_1}{q_2}=H_2-H_1=\frac\beta2(d_1-d_2).
\]
For \(\beta>0\), \(d_1-d_2\) cannot change sign: if it vanished, uniqueness for the autonomous ODE would preserve equality from that instant, contradicting strict inequality earlier. Equivalently, the displayed logarithmic-ratio equation shows a gap ratio above \(1\) increases and one below \(1\) decreases. Thus, whenever \(\beta>0\) and \(a\ne b\), both \(d_1-d_2\) and \(q_1-q_2\) have the constant nonzero sign of \(a-b\) for all \(t>0\). For \(\beta=0\), the normalized gaps agree at all times.

**3. Exact bending identity.** The weighted topicwise average \(m_j=px_j+(1-p)y_j\) satisfies
\[
\dot m_j=p(1-p)(\Phi_j^\alpha-\Phi_j^\eta)d_j
=-\frac{p(1-p)(1-\beta)(\alpha_1-\eta_1)}2(d_1-d_2)d_j.
\]
Since \(m_j(0)=x_j^0+(1-p)(y_j^0-x_j^0)\) and \(m_j(\infty)=z_j\), dividing its integrated change by each initial topic gap and subtracting yields the convergent exact identity
\[
\boxed{\displaystyle
\theta_2-\theta_1=\frac{p(1-p)(1-\beta)(\alpha_1-\eta_1)}2
\int_0^\infty(d_1-d_2)(q_1-q_2)\,dt.}
\]
When \(0<\beta<1\) and \(a\ne b\), the integrand is strictly positive for every \(t>0\). Hence the sign and all the stated necessary-and-sufficient zero-bending conditions follow. Both \(\theta_j\in(0,1)\); therefore \(z\) lies on the original segment exactly when \(\theta_1=\theta_2\).

**4. First-order response at \(\beta=0\).** With all other inputs fixed and \(\beta=0\), the gap vector retains its initial direction: \(d_1=aq\), \(d_2=bq\), where
\[
q'=-q(1-cq),\qquad q(0)=1,\qquad q(t)=\frac{e^{-t}}{1-c+ce^{-t}}.
\]
Differentiating the logarithmic-ratio identity at \(\beta=0\) and using \(q_1=q_2=q\) there gives
\[
\left.\frac{\partial}{\partial\beta}(q_1-q_2)\right|_{\beta=0}
=\frac{a-b}{2}\,q(t)\int_0^tq(s)\,ds.
\]
Smooth dependence on \(\beta\), together with a contraction rate uniformly bounded away from zero, permits differentiation under the convergent bending integral; the same uniform exponential variational bounds give the stated \(O(\beta^2)\) remainder. Its positive integral coefficient is
\[
J(c)=\int_0^\infty q(t)^2\int_0^tq(s)\,ds\,dt
=\frac{c+\log(1-c)+\frac12\log^2(1-c)}{c^3}.
\]
The change of variable \(u=e^{-t}\) proves the last expression. The integral representation proves \(J(c)>0\). Substituting the first variation into the exact identity proves the asserted weak-locality onset and completes the proof.

## Verification

The standalone script `check_two_camp_geometry.py` uses exact rational arithmetic to check the two fundamental velocity and mean-drift identities for \(81\) parameter combinations. A fourth-order Runge–Kutta calculation independently checks a strict bending example, all four degeneracies, both importance orderings, both gap orderings, and small-\(\beta\) scaling. These computations are diagnostics, not the proof of convergence, positivity of the time integral, or the all-parameter classification.

For \(p=1/2\), \(\alpha=(1,0)\), \(\eta=(0,1)\), \(\beta=1/2\), \(x^0=(-0.9,-0.1)\), and \(y^0=(0.9,0.1)\), the script returns \(\theta_1\approx0.3951023218\), \(\theta_2\approx0.4176439920\), a strict off-segment consensus. Running `python3 check_two_camp_geometry.py` requires only the standard library.

## Relationship to prior work

Bartel, Burger and Wolfram introduce the multi-topic, heterogeneous-importance model. Their analysis establishes the characteristic dynamics, conditions for agreement, componentwise confinement, and possible nonconservation of the mean. These findings motivate, but do not by themselves decide, whether the limit of exactly two initially different camp vectors lies on the *straight segment* between them. The present result is a sharp statement for the positive affine influence kernel and the two-atomic characteristic subsystem; it does not claim the source's broader convergence results as new.

Li, Luo and Chu study multidimensional, topic-weighted bounded confidence using symmetric pairwise opinion updates. The present two-camp velocities generally are nonreciprocal because each camp assigns a different topic importance, and their disagreement-dependent relative motion creates the transverse effect. Thus the geometric preservation of symmetric convex averaging does not directly imply the claimed classification.

## Limitations

The theorem requires two camps, two topics with both initial topic gaps strictly between \(0\) and \(2\), a fixed importance vector per camp, and \(\phi(s)=1-s/2\). The exact transverse formula and weak-locality coefficient need not persist for another nonlinear response, more camps, or time-varying importance. The result does not address finite-agent random fluctuations, empirical identification, or a global two-dimensional convex-hull theorem for arbitrary distributions. Broader historical priority requires independent scrutiny.

## References

1. H. Bartel, M. Burger and M.-T. Wolfram, *Multi-Dimensional Opinion Formation*, arXiv:2601.04074, initially posted 2026-01-07; model, mean-field equations, moment behavior, convergence analysis, and appendix. Full text: https://arxiv.org/html/2601.04074v4 .
2. G. J. Li, J. Luo and W. Chu, *Bounded-Confidence Models of Multidimensional Opinions with Topic-Weighted Discordance*, arXiv:2502.00284, full text: https://arxiv.org/html/2502.00284v2 .
