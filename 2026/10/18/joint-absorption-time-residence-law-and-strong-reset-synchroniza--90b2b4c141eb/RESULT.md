# Joint absorption-time residence law and strong-reset synchronization of two Brownian regions

## Finding

A Brownian searcher killed on reaching the origin and reset at Poisson times to a point inside the positive half-line has an explicit **joint** law of the total time spent above and below the resetting point before capture. The two disjoint-region residence times have strictly positive covariance at every positive resetting rate. In the frequent-reset limit their respective mean-normalized values converge jointly to the **same** unit exponential random variable, with an exact finite-rate mean-square synchronization defect.

More precisely, let \(D,r,a>0\), let \(X_0=a\), and let \(X\) evolve as Brownian motion with generator \(D\partial_{xx}\) on \((0,\infty)\), reset to \(a\) at the times of an independent rate-\(r\) Poisson process, and be absorbed at \(0\) at time \(\tau\). Define
\[
U=\int_0^\tau\mathbf 1_{\{X_t>a\}}\,dt,
\qquad
L=\int_0^\tau\mathbf 1_{\{0<X_t<a\}}\,dt.
\]
Almost surely \(U+L=\tau\). For all \(p,q\ge0\), put
\[
\mu=\sqrt{\frac{r+q}{D}},\qquad
\nu=\sqrt{\frac{r+p}{D}}.
\]
Then the full joint Laplace transform is
\[
\boxed{\mathbb E[e^{-pU-qL}]=
\left[\frac{r+q\cosh(\mu a)}{r+q}
+\frac{p\nu}{(r+p)\mu}\sinh(\mu a)\right]^{-1}.}
\tag{1}
\]
Write \(z=a\sqrt{r/D}>0\). The exact first and second joint cumulants satisfy
\[
\begin{aligned}
r\mathbb E U&=\sinh z,&
 r\mathbb E L&=\cosh z-1,\\
r^2\operatorname{Var}(U)&=\sinh z(1+\sinh z),&
r^2\operatorname{Var}(L)&=\sinh z(\sinh z-z),\\
r^2\operatorname{Cov}(U,L)&=
 \tfrac12\left[\sinh(2z)-\sinh z-z\cosh z\right]>0.
\end{aligned}
\tag{2}
\]
The exact dimensionless mean-square discrepancy is
\[
\boxed{
\mathbb E\!\left[\left(\frac{U}{\mathbb EU}-\frac{L}{\mathbb EL}\right)^2\right]
=\frac{4e^{2z}(e^z-1-z)}{(e^z-1)^3(e^z+1)}.
}
\tag{3}
\]
As \(z\to\infty\), expression (3) is asymptotic to \(4e^{-z}\), while
\[
\left(\frac U{\mathbb EU},\frac L{\mathbb EL}\right)
\ \Longrightarrow\ (E,E),\qquad E\sim\operatorname{Exp}(1).
\tag{4}
\]
In particular, the fraction \(U/\tau\) converges in probability to \(1/2\), and the Pearson correlation obeys
\[
1-\operatorname{Corr}(U,L)\sim 2e^{-z}.
\tag{5}
\]
The frequent-reset limit here means \(r\to\infty\) with \(D,a\) fixed; the same formulas apply whenever \(z\to\infty\) under the stated model.

## Assumptions and scope

The diffusion coefficient \(D\), reset rate \(r\), and positive initial/resetting point \(a\) are deterministic. Brownian motion has variance \(2Dt\) between resets. Resetting is instantaneous and complete at an independent exponential clock. Absorption ends the experiment; there is no reflecting boundary and no local-time penalty. The process starts at its resetting point. The indicator at \(a\) is immaterial because occupation time at a single point has zero Lebesgue measure almost surely.

A reset-free excursion started at \(a\) hits zero before its next reset with probability \(e^{-z}>0\); hence the number of excursions before absorption is almost surely finite and \(\tau<\infty\). In particular, \(U,L<\infty\) almost surely and the transform in (1) is well defined. The formulas are asserted for **all** \(D,r,a>0\), all \(p,q\ge0\), and all limits explicitly described above; no finite-time numerical result substitutes for these quantifiers.

## Proof

**Backward transform equation.** Let \(f(x)=\mathbb E_x[e^{-pU-qL}]\), with all subsequent resets still to \(a\), and set \(F=f(a)\). Feynman–Kac for the killed jump-diffusion gives
\[
D f''(x)-(r+p\mathbf1_{\{x>a\}}+q\mathbf1_{\{x<a\}})f(x)+rF=0
\quad(x\ne a),
\]
with \(f(0)=1\), boundedness at infinity, and continuity of \(f,f'\) at \(a\). The derivative is continuous because there is no delta killing at the interface. Equivalently, this follows from a first-step calculation and the strong Markov property.

**Solution and matching.** On \(0\le x\le a\), the bounded-at-zero solution can be written
\[
f_<(x)=C_<+(1-C_<)\cosh(\mu x)+B\sinh(\mu x),
\qquad C_<=\frac{rF}{r+q}.
\]
For \(x\ge a\), boundedness at infinity gives
\[
f_>(x)=C_>+(F-C_>)e^{-\nu(x-a)},
\qquad C_>=\frac{rF}{r+p}.
\]
Continuity of the values at \(a\) determines
\[
B=\frac{F-C_<-(1-C_<)\cosh(\mu a)}{\sinh(\mu a)}.
\]
Equating derivatives at \(a\) yields
\[
\mu\left[(F-C_<)\cosh(\mu a)-(1-C_<)\right]
=-\nu(F-C_>)\sinh(\mu a).
\]
Substitution of the two constants gives precisely (1). Uniqueness of the bounded solution follows from the stopped Markov Feynman–Kac representation (or the maximum principle for nonnegative killing). This confirms that matching cannot introduce an extraneous solution.

**Finite-rate joint moments.** Differentiating (1) at \(p=q=0\), justified by the exponential tail of the stopped process, gives the means, variances and covariance in (2). For example, the upper-residence marginal at \(q=0\) reduces exactly to
\[
\mathbb E[e^{-pU}]=
\frac{\sqrt{r(r+p)}}{\sqrt{r(r+p)}+p\sinh z},
\]
while putting \(p=q\) in (1) gives the standard absorption-time transform
\[
\mathbb E[e^{-p\tau}]=\frac{r+p}{r+p\exp(a\sqrt{(r+p)/D})}.
\]
The strict covariance sign is not inferred from numerics: its Taylor series is
\[
r^2\operatorname{Cov}(U,L)
=\sum_{n=1}^\infty\frac{4^n-n-1}{(2n+1)!}z^{2n+1}>0,
\]
since \(4^n>n+1\) for every positive integer \(n\). Elementary substitution of (2) into the squared difference of the two mean-normalized variables gives (3); \(e^z>1+z\) makes it strictly positive.

**Frequent-reset diagonal limit.** Divide the two variables by their means in (1) by substituting
\[
p=\frac{sr}{\sinh z},\qquad q=\frac{tr}{\cosh z-1},\qquad s,t\ge0.
\]
As \(z\to\infty\), both normalized Laplace arguments divided by \(r\) are \(O(e^{-z})\), and \(\mu a=z+O(ze^{-z})\). The two nonconstant denominator terms converge respectively to \(t\) and \(s\). Therefore
\[
\mathbb E\exp\left[-s\frac{U}{\mathbb EU}-t\frac{L}{\mathbb EL}\right]
\longrightarrow \frac1{1+s+t},
\]
which is the bivariate Laplace transform of \((E,E)\) with \(E\) unit exponential. Multivariate Laplace-transform continuity proves (4). Equation (3) gives the stronger quantitative statement that the difference of these normalized variables has mean-square \(4e^{-z}(1+o(1))\). Since both normalized components approach the same almost surely positive limiting variable and \(\mathbb EU/\mathbb EL\to1\), the continuous mapping theorem gives \(U/(U+L)\to1/2\) in probability. Expanding the exact covariance and variances in (2) yields (5).

## Verification

The accompanying `check.py` can be executed with Python, NumPy and SciPy using `python check.py`, with versions described in `requirements.txt`. It numerically checks 1,708 assertions: exact marginal and diagonal reductions, Laplace positivity and monotonicity, independent finite-difference solutions of the nonlocal backward equation, moment differentiation, algebraic synchronization identity, dimensional scaling, and the predicted large-\(z\) limits. For the finite-difference check, the interval is truncated sufficiently far above \(a\), with an explicit right-boundary asymptotic condition. These are consistency checks; the infinite-domain formulas, strict sign, and joint limit are proved above analytically.

## Relationship to prior work

Singh and Pal (2022), *First-passage Brownian functionals with stochastic resetting* (arXiv:2202.02715v1, Secs. 2 and 4), establish the underlying killed/reset Brownian model, the general scalar Feynman–Kac backward equation, and the **single** upper-residence transform and its moments. In particular, our upper marginal at \(q=0\) is their known Eq. (28) after restoring \(D\). Their general scalar equation is a key prior ingredient, **not** claimed novel here. The result isolated here is the evaluated joint two-region transform together with the positive cross-covariance and the exact strong-reset synchronization law.

Li and Zhou (2013), *The Joint Laplace Transforms for Diffusion Occupation Times* (DOI:10.1239/aap/1386857857), study joint occupation transforms for continuous diffusion models, but not the nonlocal Poisson reset-to-point generator considered here. Their general ODE-matching perspective is another prior ingredient. Linn and Lawley (2023), *First passage times under frequent stochastic resetting* (arXiv:2302.05409v1), establish broad scalar exponential first-passage asymptotics, consistent with the diagonal \(p=q\) specialization of (4), but do not state the separate two-region joint law or its finite-rate mean-square defect. Standard renewal-reward ideas also explain why a shared exponential can arise; the exact finite-parameter joint structure and coefficient are the asserted evaluated contribution.

## Limitations

The two-region threshold is exactly the reset position \(a\). This result does not address a different threshold, multiple reset positions, non-Poisson waiting times, diffusions with drift, partial resetting, or diffusive particles in interacting environments. The frequent-reset convergence is a statement about an ideal trajectory experiment, not about finite-sample estimation, and no joint density inversion is claimed. Previously established general scalar Feynman–Kac and frequent-resetting principles substantially motivate the derivation, so the scientific-priority assessment should distinguish the evaluated joint formulas and finite-rate synchronization constant from these known principles. Independent mathematical priority review has not been performed.

## References

1. P. Singh and A. Pal, *First-passage Brownian functionals with stochastic resetting*, arXiv:2202.02715v1 (first posted 2022-02-06), especially Secs. 2 and 4, Eqs. (9), (28)–(30). https://arxiv.org/html/2202.02715v1
2. B. Li and X. Zhou, *The Joint Laplace Transforms for Diffusion Occupation Times*, Advances in Applied Probability 45 (2013), 1049–1067, DOI:10.1239/aap/1386857857. https://doi.org/10.1239/aap/1386857857
3. S. Linn and S. D. Lawley, *First passage times under frequent stochastic resetting*, arXiv:2302.05409v1 (2023), particularly Theorem 1. https://arxiv.org/abs/2302.05409
