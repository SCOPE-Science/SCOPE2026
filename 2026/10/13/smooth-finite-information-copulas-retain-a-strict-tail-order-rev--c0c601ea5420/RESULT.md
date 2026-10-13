# Smooth finite-information copulas retain a strict tail-order reversal

## Finding
There is one absolutely continuous bivariate copula \(C_*\), with an everywhere strictly positive \(C^\infty\) density on \((0,1)^2\) and finite relative entropy from independence, such that for **every** Clayton copula \(C_\theta\), \(\theta>0\),
\[
\Lambda_{C_*}(x,y)=0<\Lambda_{C_\theta}(x,y)=(x^{-\theta}+y^{-\theta})^{-1/\theta}\qquad(x,y>0),
\]
yet \(C_*\not\le_{\mathrm{loc}} C_\theta\). Indeed, for each fixed \(\theta>0\),
\[
C_*(t,\sqrt t)>C_\theta(t,\sqrt t)
\]
for every sufficiently small \(t>0\). Thus strict lower-tail dependence ordering does not imply local lower-orthant stochastic ordering even within strictly positive interior-smooth finite-information densities. The same constructed \(C_*\) works for all \(\theta>0\); the threshold in \(t\) may depend on \(\theta\).

## Assumptions and scope
A bivariate copula is a distribution function on \([0,1]^2\) with uniform marginals. Its lower-tail dependence function is \(\Lambda_C(x,y)=\lim_{s\downarrow0}C(sx,sy)/s\). The strict tail order requires a strict inequality for every \(x,y>0\). The notation \(C\le_{\mathrm{loc}}D\) means that \(C(u,v)\le D(u,v)\) in some entire neighborhood of \((0,0)\). Smooth means \(C^\infty\) on the *open* unit square, not bounded or smoothly extendible at its boundary. Finite information means \(\int_{(0,1)^2}c_*\log c_*<\infty\), with natural logarithms.

Put \(\delta=2^{-14}\). Define the standard bump
\[
r(z)=\begin{cases}\exp[-1/(z(1-z))],&0<z<1,\\0,&\text{otherwise},\end{cases}\quad
I=\int_0^1 r(z)\,dz,\qquad h(z)=r(z)/I.
\]
Thus \(h\) is a nonnegative, unit-mass, smooth bump supported in \([0,1]\), with \(H=\|h\|_\infty<8\). In fact \(r(z)\le e^{-4}\), while integrating on \([1/4,3/4]\) shows \(I\ge\tfrac12e^{-16/3}\), giving \(H\le2e^{4/3}<8\).

Set \(\eta(z)=e^{-1/z}\) for \(z>0\), and zero otherwise. Choose a smooth cutoff \(\chi:[0,1]\to[0,1]\) that is one for \(u\le\delta/2\), zero for \(u\ge\delta\), and in between is
\[
\chi(u)=\frac{\eta(1-z)}{\eta(z)+\eta(1-z)},\qquad z=2u/\delta-1.
\]
The cutoff satisfies \(\chi(u)+\chi(3\delta/2-u)=1\) in the transition region, so \(\int_0^1\chi(u)\,du=3\delta/4\). Put \(\varepsilon(u)=e^{-1/u^2}\) for \(u>0\), and
\[
a(u,v)=(1-\varepsilon(u))u^{-1/2}h(v/\sqrt u)+\varepsilon(u),\qquad 0<u<\delta,\ 0<v<1.
\]
Let
\[
m(v)=\int_0^\delta\chi(u)a(u,v)\,du,\quad J=1-3\delta/4,
\quad g(v)=\frac{1-m(v)}J,\quad
c_*(u,v)=\chi(u)a(u,v)+(1-\chi(u))g(v),
\]
where the final formula uses the \(a\)-term only on the support of \(\chi\); outside this support the density equals \(g(v)\).

## Proof
**Normalization and regularity.** For \(0<u<\delta\), \(\sqrt u<1\), hence \(\int_0^1u^{-1/2}h(v/\sqrt u)\,dv=1\); consequently \(a(u,\cdot)\) is a probability density. For every \(v\),
\[
0\le m(v)\le 2H\sqrt\delta+\delta<\tfrac14.
\]
Indeed, the first contribution is at most \(H\int_0^\delta u^{-1/2}du\), and the leakage term at most \(\delta\). Thus \(g(v)>0\), and \(\int_0^1g(v)dv=(1-\int\chi)/J=1\). Integration first in \(v\) gives every row sum of \(c_*\) equal to one; integration first in \(u\) gives every column sum \(m(v)+Jg(v)=1\). Hence \(c_*\) is a genuine doubly stochastic density. It is strictly positive because \(a(u,v)\ge\varepsilon(u)>0\) and \(g(v)>0\). Smoothness on the open square follows from the flatness of \(h,\chi\) and from differentiating \(m(v)\) on compact interior intervals: for fixed \(v>0\), the bump term vanishes whenever \(u\le v^2\), so the apparent singularity at \(u=0\) is absent locally in \(v\).

**Vanishing lower tail.** If \(sx<\delta/2\), then \(c_*(u,v)=a(u,v)\) for \(0<u<sx\). For fixed \(x,y>0\),
\[
0\le C_*(sx,sy)\le 2H\sqrt x\,y\,s^{3/2}+xy\,s^2.
\]
Dividing by \(s\) and letting \(s\downarrow0\) proves \(\Lambda_{C_*}(x,y)=0\). On the axes the tail dependence function is also zero by grounding. Clayton's known formula, obtainable directly from its definition by scaling, is
\(\Lambda_{C_\theta}(x,y)=(x^{-\theta}+y^{-\theta})^{-1/\theta}>0\) for \(x,y>0\).

**Curved reversal.** If \(0<t<\delta/2\), every first-coordinate value \(0<u<t\) has \(\sqrt u\le\sqrt t\), so the entire bump component of \(a(u,\cdot)\) lies below \(\sqrt t\). Exact integration yields
\[
C_*(t,\sqrt t)=\int_0^t\bigl[(1-\varepsilon(u))+\sqrt t\,\varepsilon(u)\bigr]du
=t-(1-\sqrt t)\int_0^te^{-1/u^2}\,du.
\]
Therefore \(0\le t-C_*(t,\sqrt t)\le t e^{-1/t^2}\). In contrast,
\[
C_\theta(t,\sqrt t)=\frac{t}{(1+t^{\theta/2}-t^\theta)^{1/\theta}},\qquad
\lim_{t\downarrow0}\frac{t-C_\theta(t,\sqrt t)}{t^{1+\theta/2}}=\frac1\theta.
\]
Since \(e^{-1/t^2}=o(t^a)\) for every \(a>0\), the Clayton deficit eventually exceeds the \(C_*\) deficit for each \(\theta>0\). The reversal occurs at points tending to \((0,0)\); hence no neighborhood supports \(C_*\le C_\theta\).

**Finite mutual information.** The convexity of \(z\mapsto z\log z\) gives, row by row,
\[
\int c_*\log c_*\,dv\le\chi(u)\int a(u,\cdot)\log a(u,\cdot)\,dv +(1-\chi(u))\int g\log g\,dv.
\]
A second application to the mixture defining \(a\), using the uniform density as the second component, bounds the first integral by \((1-\varepsilon(u))[-\tfrac12\log u+\int_0^1h(z)\log h(z)\,dz]\). This is integrable for \(0<u<\delta\). The density \(g\) is bounded both above and away from zero because \(0\le m<1/4\), so \(\int g\log g\) is finite. Moreover \(z\log z\ge-e^{-1}\), avoiding negative-divergence issues. Therefore \(\int c_*\log c_*\) is finite.

## Verification
The standalone `check.py` evaluates the bump normalization, exact cutoff integral, analytic positivity bound and representative column-balancing values, then checks the curved inequality at several Clayton parameters using high precision. It is a diagnostic rather than proof of the continuum theorem. The proof above verifies the exact marginal constraints, all \(\theta>0\), all strictly positive directions, positivity and interior smoothness without relying on finite sampling. Running requires Python, SciPy and mpmath.

## Relationship to prior work
Siburg and Strothmann, *Multivariate tail dependence and local stochastic dominance*, arXiv:2210.06842 (first public 2022-10-13), Example 3, give a Marshall–Olkin versus Clayton curved-path reversal; their Marshall–Olkin copula has a **singular** component supported on the curve. Their Theorem 2 establishes ordering on fixed interior cones; this theorem respects it because the reversing path approaches an axis. Their Section 5 gives positive local-order implications within specific structured families, not within all smooth copulas. The present construction proves that removing singular mass, imposing interior \(C^\infty\) strict density positivity, and even requiring finite information do not rescue the unrestricted implication, and does so for all positive Clayton parameters using the *same* copula. Siburg, Strothmann and Weiß, *Comparing and quantifying tail dependence*, arXiv:2208.10319, develops dependence-order context but does not supply this smooth regularity boundary in the inspected full text. This is a scientific distinction, not a claim of established publication priority.

## Limitations
Smoothness and positivity are asserted on \((0,1)^2\), not continuously through the boundary. The density need not be bounded near \(u=0\), and may be asymmetric. For each Clayton parameter the sufficiently-small threshold can depend on that parameter; no uniform threshold over \(\theta\in(0,\infty)\) is claimed. No comparison is made with all possible copulas possessing positive tail dependence, nor is any claim made about a sharp optimal defect or minimum information. No independent mathematical or bibliographic audit has been performed.

## References
1. K. F. Siburg and C. Strothmann, *Multivariate tail dependence and local stochastic dominance*, arXiv:2210.06842, submitted 2022-10-13, https://arxiv.org/html/2210.06842v2 (Sections 3–5; Example 3).
2. K. F. Siburg, C. Strothmann and G. Weiß, *Comparing and quantifying tail dependence*, arXiv:2208.10319, submitted 2022-08-22, https://arxiv.org/abs/2208.10319.
