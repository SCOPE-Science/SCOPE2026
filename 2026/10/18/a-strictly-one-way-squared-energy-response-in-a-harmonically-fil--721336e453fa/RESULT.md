# A strictly one-way squared-energy response in a harmonically filtered resetting Brownian drive

## Finding

For every \(\beta>0\), the stationary active particle driven by reset Brownian forcing has a strictly positive temporal asymmetry between the squared particle displacement and squared driving signal. This is a statement about the *two distinct temporal orderings*, not about unequal one-time variances.

Write \(U_\beta(t)=\operatorname{Cov}(X_t^2,Y_0^2)\), \(V_\beta(t)=\operatorname{Cov}(Y_t^2,X_0^2)\), and \(\Delta_\beta(t)=U_\beta(t)-V_\beta(t)\). For \(a>0\), let \(k_a(t)=e^{-at}\mathbf 1_{\{t\geq0\}}\), with \(*\) denoting causal convolution. The exact all-parameter law is

\[
\Delta_\beta(t)=\frac{8\beta}{(\beta+1)^2(\beta+2)}\left[(16\beta+10)(k_\beta*k_2)(t)+(5\beta^2+12\beta+4)(k_\beta*k_2*k_{\beta+1})(t)\right].
\]

Every coefficient and every nontrivial convolution factor is positive. Consequently \(\Delta_\beta(t)>0\) for all \(\beta,t>0\), including coincident decay rates \(\beta=1,2\). Let \(A_\beta=\operatorname{Cov}(X_0^2,Y_0^2)\). The dimensionless normalized integrated directionality is exactly

\[
\mathcal R(\beta)=\frac{\int_0^\infty\Delta_\beta(t)\,dt}{A_\beta}=\frac{21\beta^2+38\beta+14}{2(\beta+1)(8\beta+5)}.
\]

It has a *unique* global maximizer on \((0,\infty)\), and its optimal value is

\[
\beta_* = \frac{-7+3\sqrt{33}}{31},\qquad
\mathcal R(\beta_*)=\frac{10-\sqrt{33}}3.
\]

This dimensionless area concerns lag measured in inverse trap-relaxation units. In physical time the normalized area is divided by the relaxation rate.

## Assumptions and scope

Take a real two-coordinate stationary Markov process satisfying, between independently occurring rate-\(\beta\) Poisson events,

\[
dX_t=(-X_t+\beta Y_t)\,dt,\qquad dY_t=\sqrt 2\,dW_t.
\]

At each Poisson event, only the driving coordinate is reset: \(Y_t\mapsto0\), while \(X_t\) stays continuous. Here \(\beta>0\) is arbitrary, \(W\) is independent Brownian motion, and the two-sided process is initialized in its unique stationary distribution. This is a nondimensionalized harmonic particle driven by Brownian resetting noise, as in Gueneau--Majumdar--Schehr. All moments displayed below are finite. The statement does not require a Gaussian joint stationary law (which generally fails).

One stationary construction is to run the Poisson-resetting Brownian drive from the infinite past and set \(X_t=\beta\int_0^\infty e^{-s}Y_{t-s}\,ds\). The reset drive has moments of all orders, and exponential filtering makes the position well defined with finite moments. The construction also ensures uniqueness of the stationary coupled law.

## Proof

The generator on polynomial observables is

\[
\mathcal L f=(-x+\beta y)\partial_x f+\partial_{yy}f+\beta[f(x,0)-f(x,y)].
\]

More particularly, for nonnegative integers \(a,c\),

\[
\mathcal L(x^ay^c)=-a x^ay^c+a\beta x^{a-1}y^{c+1}+c(c-1)x^ay^{c-2}-\beta\mathbf1_{\{c>0\}}x^ay^c,
\]

with terms containing zero prefactors omitted. Applying \(\mathbb E\mathcal Lf=0\) in the stationary law to monomials through total degree four gives

\[
\begin{gathered}
\mathbb EX^2=\frac{2\beta}{\beta+1},\quad
\mathbb E(XY)=\frac2{\beta+1},\quad
\mathbb EY^2=\frac2\beta,\\
\mathbb EY^4=\frac{24}{\beta^2},\quad
\mathbb E(XY^3)=\frac{12(3\beta+2)}{\beta(\beta+1)^2},\\
\mathbb E(X^2Y^2)=\frac{4(\beta^2+19\beta+12)}{(\beta+1)^2(\beta+2)}.
\end{gathered}
\]

It follows that three initial centered covariances are

\[
A_\beta=\frac{8(8\beta+5)}{(\beta+1)^2(\beta+2)},\qquad
B_\beta=\operatorname{Cov}(X_0Y_0,Y_0^2)=\frac{4(8\beta+5)}{\beta(\beta+1)^2},\qquad
C_\beta=\operatorname{Var}(Y_0^2)=\frac{20}{\beta^2}.
\]

For \(t\geq0\), put \(u(t)=\operatorname{Cov}(X_t^2,Y_0^2)\), \(v(t)=\operatorname{Cov}(X_tY_t,Y_0^2)\), \(w(t)=\operatorname{Cov}(Y_t^2,Y_0^2)\). The generator's exact quadratic closure gives

\[
u'=-2u+2\beta v,\quad v'=-(\beta+1)v+\beta w,\quad w'=-\beta w,
\qquad (u(0),v(0),w(0))=(A_\beta,B_\beta,C_\beta).
\]

The driving coordinate evolves autonomously. Since its conditional squared mean is \(\mathbb E(Y_t^2\mid X_0,Y_0)=e^{-\beta t}Y_0^2+(2/\beta)(1-e^{-\beta t})\), the reversed ordering satisfies \(V_\beta(t)=A_\beta e^{-\beta t}\). Taking Laplace transforms of the triangular system, subtracting this reversed contribution, and simplifying gives, for \(p\geq0\),

\[
\int_0^\infty e^{-pt}\Delta_\beta(t)\,dt=
\frac{8\beta\left[(16\beta+10)(p+\beta+1)+(5\beta^2+12\beta+4)\right]}
{(\beta+1)^2(\beta+2)(p+\beta)(p+2)(p+\beta+1)}.
\]

Inverting each product of resolvents by elementary causal convolution proves the displayed positive-kernel formula. The integrals of two- and three-factor kernels are the reciprocals of the respective products of their positive rates. At \(p=0\), division by \(A_\beta\) yields the rational formula for \(\mathcal R\).

Finally, direct differentiation gives

\[
\mathcal R'(\beta)=-\frac{31\beta^2+14\beta-8}{2(\beta+1)^2(8\beta+5)^2}.
\]

The numerator has precisely one positive zero \(\beta_*\), with positive derivative before and negative derivative after. Hence it is the unique global maximizer. Substitution simplifies to \((10-\sqrt{33})/3\), completing the proof.

## Verification

The standalone `check.py`, requiring the packages in `requirements.txt`, independently builds the polynomial generator matrix through degree four, solves its stationary linear equations, evaluates the quadratic semigroup by matrix exponentiation, checks the positive convolution by quadrature, and checks the Laplace-transform and optimization formulas. Running `python check.py` yielded `PASS: 622 independent numerical assertions`. These finite numerical checks independently corroborate the formulas but are **not** the proof of positivity for every continuous parameter or the global optimization; those statements follow from the displayed algebra and strictly positive convolutions.

## Relationship to prior work

Gueneau, Majumdar, and Schehr (first public preprint June 15, 2023) develop the same harmonic particle with resetting Brownian drive, stationary position moments and the ordinary position autocorrelation, including the two-time analysis in Appendix G. They do **not** state the ordered \(X^2\)-versus-\(Y^2\) cross-covariances or their strictly positive all-lag difference and globally optimized normalized area. Their results supply the model and several lower-dimensional ingredients, not the evaluated claim here. Gu's 2023 thermodynamic cross-correlation inequalities motivate the relevance of temporal asymmetry but concern different bounds, not this model-specific formula or optimum. Broader polynomial-semigroup methods could reproduce parts of the derivation; neither the generator nor its general moment-closure principle is claimed as new.

## Limitations

Only the precise complete-resetting Brownian drive and linear harmonic filter above are treated. The result is a stationary, *two-time squared-observable* statement, not entropy-production quantification, linear-covariance irreversibility, a finite-sample inferential guarantee, or a theorem for other reset laws. In particular, the exact numerical optimum depends on the stated choice of squared observables, normalization, and Poisson reset law. Scientific priority remains subject to independent review; equivalent specializations of more general prior stochastic-calculus frameworks cannot be wholly ruled out by finite literature searches.

## References

1. M. Gueneau, S. N. Majumdar, and G. Schehr, *Active particle in a harmonic trap driven by a resetting noise: an approach via Kesten variables*, arXiv:2306.09453v1 (first publicly submitted 2023-06-15), full HTML of v2: https://arxiv.org/html/2306.09453v2. Sections 4.2 and 5 and Appendix G were inspected.
2. J. Gu, *Thermodynamic bounds on the asymmetry of cross-correlations with dynamical activity and entropy production*, arXiv:2312.00354v1 (2023-12-01), https://arxiv.org/html/2312.00354v2.
3. K. S. Olsen and H. Löwen, *Dynamics of inertial particles under velocity resetting*, arXiv:2401.12685v1 (2024-01-23), https://arxiv.org/abs/2401.12685 (abstract screened for alternate resetting-transport methods).
