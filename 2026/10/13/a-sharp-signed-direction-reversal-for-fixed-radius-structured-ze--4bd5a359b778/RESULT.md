# A sharp signed-direction reversal for fixed-radius structured zeroth-order descent

## Finding

Consider the forward-difference structured stochastic zeroth-order descent (S-SZD) update on the isotropic quadratic \(f(x)=\lambda\|x\|_2^2/2\). With a fixed step size and fixed, positive finite-difference radius, the limiting expected squared distance to the minimizer is controlled by a *single* statistic of the random direction frame: the squared norm of its mean summed direction. Across **every** isotropic law of orthogonal frames allowed by the algorithm, a sharp transition at normalized step \(\alpha\lambda d/\ell=1\) reverses which orientation law minimizes the asymptotic risk.

Let \(r=d/\ell\), \(\beta=\alpha\lambda\), \(u=P\mathbf 1_\ell\), and \(q=\|\mathbb E u\|_2^2\). For \(0<\beta r<2\),

\[
\boxed{\lim_{k\to\infty}\mathbb E\|x_k\|_2^2
 =\frac{h^2r^2}{4}\,\frac{\beta d+2(1-\beta r)q}{2-\beta r}.}
\]

Every admissible direction law satisfies \(0\le q\le\ell\), and every value in this interval is attainable by an admissible law. Consequently, for \(\beta r<1\), a symmetric signed-coordinate frame minimizes the limiting risk and an all-positive coordinate frame maximizes it. At \(\beta r=1\), all admissible laws tie. For \(1<\beta r<2\), the ordering reverses: all-positive coordinate frames minimize the limiting risk and symmetrically signed frames maximize it. The sharp endpoint values are

\[
\boxed{V_{\mathrm{signed}}=\frac{h^2r^2\beta d}{4(2-\beta r)},\qquad
V_{\mathrm{unsigned}}=\frac{h^2d^2}{4\ell}.}
\]

The signed value is zero only in the limiting zero-step or zero-radius regimes, not at any positive parameters in the stated domain; the unsigned value does not depend on the step size within the stable interval. Moreover, as \(\beta r\uparrow 2\), the signed limiting squared error diverges while the unsigned limiting squared error remains \(h^2d^2/(4\ell)\): this is a genuine risk-preference reversal, not only a small change in numerical constants.

## Assumptions and scope

Fix integers \(d\ge1\), \(1\le\ell\le d\), a curvature \(\lambda>0\), a finite-difference radius \(h>0\), and a fixed step size \(\alpha>0\) with \(0<\alpha\lambda d/\ell<2\). Start from any deterministic \(x_0\in\mathbb R^d\). Independently at each iteration draw \(P_k\in\mathbb R^{d\times\ell}\) with identical distribution satisfying

\[
P_k^\top P_k=\frac d\ell I_\ell\quad\text{almost surely},\qquad
\mathbb E[P_kP_k^\top]=I_d.
\]

The columns \(p_{k,i}\) form the directions, with each \(\|p_{k,i}\|_2^2=d/\ell\). The update is precisely the forward-difference version of S-SZD (Algorithm 1 in Rando et al.):

\[
x_{k+1}=x_k-\alpha\sum_{i=1}^\ell
\frac{f(x_k+h p_{k,i})-f(x_k)}h\,p_{k,i},
\qquad f(x)=\tfrac\lambda2\|x\|_2^2.
\]

This is the deterministic-objective special case of the stochastic algorithm: there is no additional function-evaluation noise. Independence over iterations, fixed parameters, and the isotropic quadratic curvature are material hypotheses. In particular, the statement is about **limiting expected squared error**, not an assertion that iterates converge almost surely to a point or that one frame law dominates at every finite step.

## Proof

Write \(R=PP^\top\), \(u=P\mathbf1_\ell\), \(r=d/\ell\), \(\beta=\alpha\lambda\), and \(a=\beta hr/2\). The quadratic identity

\[
\frac{f(x+hp_i)-f(x)}h=\lambda p_i^\top x+\tfrac12\lambda h\|p_i\|_2^2
\]

makes the iteration **exactly**

\[
x_{k+1}=(I-\beta R_k)x_k-a u_k.
\]

Orthonormality yields \(R^2=rR\), \(Ru=ru\), and \(\|u\|_2^2=\ell r=d\), almost surely; isotropy gives \(\mathbb E R=I\). Let \(m=\mathbb E u\), \(b_k=\mathbb E x_k\), and \(S_k=\mathbb E\|x_k\|_2^2\). Since each new frame is independent of \(x_k\),

\[
b_{k+1}=(1-\beta)b_k-a m.
\]

Because \(r\ge1\) and \(0<\beta r<2\), one has \(0<\beta<2\) and thus \(|1-\beta|<1\). Therefore

\[
b_k\longrightarrow -\frac a\beta m=-\frac{hr}{2}m.
\]

Expanding the squared update and applying the three frame identities gives the exact scalar recurrence

\[
S_{k+1}=\rho S_k+a^2d-2a(1-\beta r)\langle b_k,m\rangle,
\qquad\rho=1-2\beta+\beta^2r.
\]

The assumed step interval implies \(0\le\rho<1\): indeed \(\rho=1-\beta(2-\beta r)\), and \(\rho\ge(1-\beta)^2\) because \(r\ge1\). The convergent linear recurrence thus has limit

\[
\frac{a^2d+2a^2(1-\beta r)\|m\|_2^2/\beta}
{\beta(2-\beta r)}
=\frac{h^2r^2}{4}\frac{\beta d+2(1-\beta r)q}{2-\beta r}.
\]

The bound on \(q\) is stronger than the immediate Jensen estimate. For every unit vector \(v\), Cauchy--Schwarz and isotropy imply

\[
(v^\top m)^2\le\mathbb E(v^\top P\mathbf1_\ell)^2
\le\ell\,\mathbb E\|P^\top v\|_2^2=\ell.
\]

Taking \(v=m/\|m\|\) when \(m\ne0\) proves \(q\le\ell\); nonnegativity is automatic.

For attainability choose a uniformly random \(\ell\)-subset of the coordinate axes, scaling each selected axis by \(\sqrt r\). With independent equally likely signs on its columns, \(m=0\), so \(q=0\). With all signs positive,

\[
m=\sqrt r\,\frac\ell d\mathbf1_d=\frac1{\sqrt r}\mathbf1_d,
\quad q=\frac d r=\ell.
\]

Both laws have \(P^\top P=rI\) and \(\mathbb E PP^\top=I\). For an intermediate \(q\), independently multiply the unsigned frame by a global sign whose expectation is \(\sqrt{q/\ell}\); this changes \(m\) by that factor without changing either structural frame condition. Thus the full interval is realized. The limiting-risk formula is affine in \(q\) with slope having the sign of \(1-\beta r\), proving all three sharp regimes and both endpoint formulas. The proof holds for every admissible frame law, not just coordinate frames.

For example, at \(d=4\), \(\ell=2\), \(\lambda=h=1\), the two endpoint risks are \(2/3\) (signed) and \(2\) (unsigned) for \(\alpha=1/4\), while they are \(6\) (signed) and \(2\) (unsigned) for \(\alpha=3/4\). These two choices lie on opposite sides of the exact crossover \(\alpha=1/2\).

## Verification

The standalone file `verify.py` uses `fractions.Fraction` and enumerates coordinate-subset and sign distributions; it represents the state in units \(2/(h\sqrt r)\), so the direction scale cancels and all transitions are rational. The script checks the conditional mean and squared-error recurrences against independently enumerated exact finite-step distributions, the extrema \(q=0,\ell\), an intermediate sign mixture, and the sharp transition across small integer dimensions. Running `python verify.py` produced:

`PASS: 1305 exact-rational transition, moment and endpoint checks`

The script also reproduces the two exact examples above. The universal frame-law conclusion is proved algebraically; this finite enumeration checks representative cases but is **not** an exhaustive enumeration of all possible frame laws.

## Relationship to prior work

Rando, Molinari, Villa, and Rosasco, *Stochastic Zeroth Order Descent with Structured Directions* (arXiv:2206.05124, first version 2022-06-10), provide exactly this forward-difference update and these isotropic orthogonal-frame conditions in their Assumption 2 and Algorithm 1, with convergence bounds under prescribed step/radius schedules and PL hypotheses. Their results do not state the exact fixed-radius asymptotic mean-square functional or optimize it over direction laws. In particular, their Theorem 2 is an inequality, not an equality law for \(\lim\mathbb E\|x_k\|^2\).

Kozak, Molinari, Rosasco, Tenorio, and Villa, *Zeroth order optimization with orthogonal random directions* (arXiv:2107.03941, 2021), provide related fixed-discretization convergence bounds. Their Remark 4.2 explains first-order bias cancellation for symmetric sampling on quadratics and explicitly leaves a tailored quadratic convergence analysis for future work. This is consistent with the signed endpoint here but does not determine the precise variance floor or the reversal for large admissible step sizes. Earlier work *A stochastic subspace approach to gradient-free optimization in high dimensions* (arXiv:2003.02684) studies related subspace-gradient techniques, without the same exact finite-difference asymptotic result.

Relevant published-finding corpus records on exact Haar stochastic subspace-descent moments and inverse-positive coordinate sampling concern, respectively, derivative/subspace descent and sampling for first-order coordinate optimization. The finite-radius affine forcing and the step-dependent *reversal* between signed and unsigned orientations are absent from their available scientific summaries; their full texts were not established as read in this comparison. No claim of exhaustive priority or independence is made.

## Limitations

The theorem requires an exactly isotropic scalar Hessian, independent and identically distributed frames, zero function-evaluation noise, and constant parameters satisfying the strict stable-step inequality. It gives the limiting **second moment**, not a complete limiting distribution, an almost-sure convergence theorem, or a risk ordering for arbitrary nonisotropic Hessians. At the excluded boundary \(\alpha\lambda d/\ell=2\), the second-moment recurrence ceases to be contractive; no stability conclusion is asserted there. The available literature inspection is not a proof of global priority; in particular, specialized unindexed analyses of constant-radius zeroth-order schemes may exist.

## References

1. M. Rando, C. Molinari, S. Villa, L. Rosasco, *Stochastic Zeroth Order Descent with Structured Directions*, arXiv:2206.05124 (first version 2022-06-10), Assumption 2, Algorithm 1, Theorem 2, Appendix D.4.
2. D. Kozak, C. Molinari, L. Rosasco, L. Tenorio, S. Villa, *Zeroth order optimization with orthogonal random directions*, arXiv:2107.03941 (first version 2021-07-08), Algorithm 1, Theorem 3.7, Remark 4.2.
3. D. Kozak et al., *A stochastic subspace approach to gradient-free optimization in high dimensions*, arXiv:2003.02684 (2020).
4. Y. Feng and T. Wang, *Stochastic Zeroth Order Gradient and Hessian Estimators: Variance Reduction and Refined Bias Bounds*, arXiv:2205.14737 (2022); abstract-level comparison only.
