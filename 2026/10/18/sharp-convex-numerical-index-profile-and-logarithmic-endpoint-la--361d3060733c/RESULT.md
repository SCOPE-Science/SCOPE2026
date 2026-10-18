# Sharp convex numerical-index profile and logarithmic endpoint layers for real \(\ell_p^2\)

## Finding
For the real Banach plane \(X_p=(\mathbb R^2,\|\cdot\|_p)\), with \(1<p<\infty\), put
\[
\alpha=|1-2/p|,\qquad \mathcal N(\alpha)=n(X_p),
\]
where \(n(X)\) is the numerical index: the infimum of the numerical radius \(v(T)\) over all norm-one real-linear operators \(T:X\to X\). The value depends only on \(\alpha\), and its continuous endpoint values are \(\mathcal N(0)=0\), \(\mathcal N(1)=1\).

**Theorem.** The function \(\mathcal N\) is strictly increasing, strictly convex, and real analytic for \(0<\alpha<1\). Let \(z_*>0\) be the unique solution of
\[
z_*\tanh z_*=1,
\]
and define
\[
c_*:=\frac{z_*}{\cosh z_*}=0.662743419349\ldots,\qquad
 d_*:=\frac{z_*^3}{6\cosh z_*}=0.158973240429\ldots.
\]
Then for all \(0<\alpha<1\),
\[
\boxed{c_*\alpha<\mathcal N(\alpha)<\alpha.}
\]
Both constants are globally optimal. At the Hilbert point,
\[
\boxed{\mathcal N(\alpha)=c_*\alpha+d_*\alpha^3+O(\alpha^5)}\qquad(\alpha\downarrow0).
\]
At the opposite boundary, writing \(\delta=1-\alpha\),
\[
\boxed{\mathcal N(1-\delta)=1-\frac\delta2\left[\log\frac4\delta+1\right]+o(\delta)}\qquad(\delta\downarrow0).
\]
The derivative exists for \(0<\alpha<1\) and satisfies
\[
\boxed{\mathcal N'(1-\delta)=\frac12\log\frac4\delta+o(1)}.
\]
Thus the approach to numerical index one is logarithmically non-Lipschitz in the natural duality-invariant parameter.

In the original exponent, the two extreme-end expansions are
\[
\begin{aligned}
1-n(X_p)&=\frac{p-1}{p}\left[\log\frac{2p}{p-1}+1\right]+o(p-1),&&p\downarrow1,\\
1-n(X_p)&=\frac1p[\log(2p)+1]+o(1/p),&&p\to\infty.
\end{aligned}
\]
For \(p\ne2\), the unique maximizing scalar \(t_p\in(0,1)\) in the inherited exact scalar numerical-index formula obeys
\[
\boxed{t_p\sim\frac{p-1}{2}\quad(p\downarrow1),\qquad
 t_p=1-\frac{\log(2p)}p+o(1/p)\quad(p\to\infty).}
\]
The last two formulas quantify the migration of the rotation's extremizing norming vectors near the two nonsmooth endpoints.

## Assumptions and scope
All scalars, duals, and operators are **real**. The space is precisely two dimensional. The norm \(\|(x,y)\|_p=(|x|^p+|y|^p)^{1/p}\) is used for \(1<p<\infty\), with the standard \(\ell_1\) and \(\ell_\infty\) endpoint norms. The numerical radius is
\[
v(T)=\sup\{|x^*(Tx)|:\|x\|=\|x^*\|=x^*(x)=1\}.
\]
The external theorem needed here is Chiclana's 2026 identity
\[
n(X_p)=M_p=\max_{0\le t\le1}\frac{|t^{p-1}-t|}{1+t^p}.
\]
That identity, its scalar maximizer and its hyperbolic rewriting are **known prior results**; the present finding consists only of the global profile properties, sharp constants, asymptotics, derivative divergence, and sharp extremizer migration proved below. No assertion is made for higher-dimensional \(\ell_p\), complex scalars, or infinite-dimensional \(L_p\).

## Proof
**1. Exact inherited reduction and maximizer.** Put \(t=e^{-2z/p}\), \(z\ge0\). A direct rearrangement of the cited identity, using \(\alpha=|1-2/p|\), gives
\[
\mathcal N(\alpha)=\max_{z\ge0}F_\alpha(z),\qquad F_\alpha(z)=\frac{\sinh(\alpha z)}{\cosh z}.
\]
For \(0<\alpha<1\), this function vanishes at zero and at infinity and is positive in between. Its logarithmic derivative is
\[
\partial_z\log F_\alpha(z)=\alpha\coth(\alpha z)-\tanh z,
\]
whose derivative equals \(-\alpha^2\operatorname{csch}^2(\alpha z)-\operatorname{sech}^2z<0\). Hence the maximum is achieved at one finite positive point \(z_\alpha\), characterized equivalently by the **previously known** equation
\[
\tanh(\alpha z_\alpha)\tanh z_\alpha=\alpha.
\]
The product on the left grows continuously from zero to one, proving uniqueness as well. The implicit-function theorem, together with the positivity of the derivative of that product, makes \(z_\alpha\) and \(\mathcal N(\alpha)=F_\alpha(z_\alpha)\) real analytic on \((0,1)\).

**2. Strict convexity and sharp global bounds.** For each fixed \(z>0\), the function \(\alpha\mapsto\sinh(\alpha z)/\cosh z\) is strictly increasing and strictly convex on \((0,1)\). Taking its value at the optimizer of a convex combination proves strict convexity of its attained supremum (and also strict increase). More precisely, for \(0<\alpha_1<\alpha_2<1\), \(0<\theta<1\), put \(\beta=\theta\alpha_1+(1-\theta)\alpha_2\) and choose \(z=z_\beta>0\). Then
\[
\mathcal N(\beta)=F_\beta(z)<\theta F_{\alpha_1}(z)+(1-\theta)F_{\alpha_2}(z)
\le\theta\mathcal N(\alpha_1)+(1-\theta)\mathcal N(\alpha_2).
\]
Since \(\sinh(\alpha z)<\alpha\sinh z\) for \(0<\alpha<1\), at the unique optimizer
\[
\mathcal N(\alpha)<\alpha\tanh z_\alpha<\alpha.
\]
The unique positive maximum of \(z/\cosh z\) occurs at \(z=z_*\), because the derivative has the sign of \(1-z\tanh z\). Evaluating at this fixed point gives
\[
\mathcal N(\alpha)\ge\frac{\sinh(\alpha z_*)}{\cosh z_*}>\frac{\alpha z_*}{\cosh z_*}=c_*\alpha.
\]
The endpoint expansions established below give \(\mathcal N(\alpha)/\alpha\to c_*\) as \(\alpha\downarrow0\), and \(\mathcal N(\alpha)/\alpha\to1\) as \(\alpha\uparrow1\), proving both constants best possible.

**3. Hilbert-point expansion.** The stationary equation and \(\tanh(\alpha z)\le\alpha z\) imply \(z_\alpha\tanh z_\alpha\ge1\), hence \(z_\alpha\ge z_*\). Moreover
\[
\tanh(\alpha z_\alpha)=\frac\alpha{\tanh z_\alpha}\le\frac\alpha{\tanh z_*}.
\]
For small \(\alpha\), this bounds \(z_\alpha\) uniformly; expanding the stationary equation then yields \(z_\alpha\tanh z_\alpha=1+O(\alpha^2)\), whence \(z_\alpha=z_*+O(\alpha^2)\) by its nonzero derivative at \(z_*\). Uniformly for bounded \(z\),
\[
F_\alpha(z)=\alpha\frac z{\cosh z}+\frac{\alpha^3}6\frac{z^3}{\cosh z}+O(\alpha^5).
\]
At the stationary maximum of the leading coefficient, the shift \(z_\alpha-z_*=O(\alpha^2)\) changes that leading coefficient by only \(O(\alpha^4)\), and changes the cubic coefficient by \(O(\alpha^2)\). Substitution proves the two displayed sharp coefficients and the \(O(\alpha^5)\) remainder.

**4. Logarithmic boundary layer.** Let \(\delta=1-\alpha\downarrow0\) and \(u=e^{-2z_\alpha}\). The stationary equation is **exactly**
\[
\delta=\frac{2(u^\alpha+u)}{(1+u^\alpha)(1+u)}.
\]
Since \(\alpha\uparrow1\) forces \(z_\alpha\to\infty\), we have \(u\to0\). The inequalities
\[
\delta\ge1-\tanh z_\alpha=\frac{2u}{1+u},\qquad
\delta\le(1-\tanh(\alpha z_\alpha))+(1-\tanh z_\alpha)\le4u^\alpha
\]
show \(u\le\delta\) and \(z_\alpha\le\log(4/\delta)/(2\alpha)\); consequently \(\delta z_\alpha\to0\). Therefore \(u^\alpha=u\exp(2\delta z_\alpha)=u(1+o(1))\), and the exact equation yields
\[
u=\frac\delta4(1+o(1)),\qquad z_\alpha=\frac12\log\frac4\delta+o(1).
\]
At the optimizer,
\[
\mathcal N(1-\delta)=\exp(-\delta z_\alpha)\frac{1-u^\alpha}{1+u}.
\]
Here \(\delta z_\alpha=O(\delta\log(1/\delta))\) and \(u^\alpha+u=\delta/2+o(\delta)\). Expansion of the factors proves
\[
1-\mathcal N(1-\delta)=\delta z_\alpha+u^\alpha+u+o(\delta)
=\frac\delta2\left(\log\frac4\delta+1\right)+o(\delta).
\]
The envelope theorem (or ordinary differentiation at the unique stationary optimizer) gives
\[
\mathcal N'(\alpha)=\frac{z_\alpha\cosh(\alpha z_\alpha)}{\cosh z_\alpha}.
\]
Because the cosh ratio at \(\alpha=1-\delta\) is \(1+O(\delta\log(1/\delta))\), and \(z_\alpha=O(\log(1/\delta))\), this yields the derivative expansion. Finally, \(\delta=2(p-1)/p\) for \(1<p<2\) and \(\delta=2/p\) for \(p>2\), yielding both stated exponent-endpoint laws. The maximizing original coordinate parameter is \(t_p=e^{-2z_\alpha/p}=u^{1/p}\): using \(u\sim\delta/4\) gives the two sharp migration formulas.

## Verification
The self-contained Python 3 program `check.py` performs 137 finite diagnostics. It independently solves both stationary equations by bisection, checks strict inequalities at 99 parameter values, strict midpoint convexity at 18 triples, five small-parameter cubic approximations, five large-parameter logarithmic and derivative checks, and nine duality checks. It prints the constant values. All finite tests passed. The universal assertions follow from the analytic proof, not the finite diagnostics.

## Relationship to prior work
Chiclana, *The Numerical Index of Two-Dimensional Real \(\ell_p\) Spaces* (arXiv:2606.01675v1, first posted 2026-06-01), proves the exact global identity for the numerical index; Sections 2 and 7 also contain its hyperbolic change of variables and the maximizing equation. Those results are prerequisites, not novel parts of this finding. Martín and Merí, *A Note on the Numerical Index of the \(L_p\) Space of Dimension Two* (2007 preprint; 2009 publication), and Merí–Quero, *On the Numerical Index of the Real Two-Dimensional \(L_p\) Space* (arXiv:2205.08807), provide older bounds or equality on partial exponent intervals. The retrieved full versions do not contain the sharp global convex profile, the four exact endpoint coefficients, the derivative blow-up, or the matching maximizer migration. In particular, the 2022 work establishes equality only on a bounded range of exponents, so it cannot itself imply the extreme-exponent endpoint limits. Mathematical equivalents under another notation remain a priority risk.

## Limitations
The global exact numerical-index formula and stationary hyperbolic equation are taken from published prior research, not reproved here from first principles. The new conclusions concern real two-dimensional \(\ell_p\) planes only; no higher-dimensional, infinite-dimensional, or complex-space extension is established. Asymptotics are pointwise in the stated limits, not uniform over additional families. Finite numerical diagnostics are illustrative and do not certify infinite quantifiers. No independent scientific review has been performed, and an equivalent earlier asymptotic statement under other terminology cannot be absolutely excluded.

## References
1. R. Chiclana, *The Numerical Index of Two-Dimensional Real \(\ell_p\) Spaces*, arXiv:2606.01675v1 (first publicly posted 2026-06-01), https://arxiv.org/abs/2606.01675.
2. M. Martín and J. Merí, *A Note on the Numerical Index of the \(L_p\) Space of Dimension Two*, 2007 preprint; *Linear and Multilinear Algebra* (2009), https://www.ugr.es/~mmartins/Curriculum/Papers/2009-MartinMeri-Lp.pdf.
3. J. Merí and A. Quero, *On the Numerical Index of the Real Two-Dimensional \(L_p\) Space*, arXiv:2205.08807v1 (2022-05-18), https://arxiv.org/abs/2205.08807.
