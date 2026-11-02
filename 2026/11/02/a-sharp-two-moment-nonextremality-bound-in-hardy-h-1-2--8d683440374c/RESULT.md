# A sharp two-moment nonextremality bound in Hardy \(H^{1/2}\)

## Finding

For every inner function \(I\) on the disk and nonzero outer function \(F\in H^{1/2}\), define the probability measure \(d\mu=|F|^{1/2}dm/\int_{\mathbb T}|F|^{1/2}dm\) on the circle, where \(dm=d\theta/(2\pi)\), and its inner moments
\[
\alpha=\int_{\mathbb T}I\,d\mu,\qquad
\beta=\int_{\mathbb T}I^2\,d\mu.
\]
For every real \(t\), set
\[
H_{\pm,t}=\tfrac12e^{it}(1\pm e^{-it}I)^2F,
\qquad
\mathcal E(I,F)=\inf_{t\in\mathbb R}
\frac{\|H_{+,t}\|_{1/2}+\|H_{-,t}\|_{1/2}}{2\|F\|_{1/2}}.
\]
Then
\[
\boxed{\mathcal E(I,F)\le 1-\frac{1-|\alpha|^2+|\beta-\alpha^2|}{8}.}
\]
The coefficient \(1/8\) is the largest universal coefficient in this **decomposition-envelope inequality**. As a consequence, every bounded complex-linear functional \(L\) on \(H^{1/2}\) satisfies
\[
|L(IF)|\le\|L\|\,\|F\|_{1/2}
\left(1-\frac{1-|\alpha|^2+|\beta-\alpha^2|}{8}\right).
\]
For nonconstant \(I\), the parenthesized factor is strictly less than one. Hence any pair obeying \(|L(IF)|\ge(1-\varepsilon)\|L\|\|F\|_{1/2}\), with \(L\ne0\), necessarily has
\[
1-|\alpha|^2+|\beta-\alpha^2|\le 8\varepsilon.
\]
The coefficient is proved optimal for the envelope only, **not** for the functional estimate.

## Assumptions and scope

The Hardy quasi-norm is \(\|f\|_{1/2}=(\int_{\mathbb T}|f|^{1/2}dm)^2\), with standard radial boundary values. The inner function has boundary modulus one almost everywhere; it may be constant. The outer function is nonzero, so \(|F|>0\) almost everywhere and \(\mu\) is a probability with strictly positive density almost everywhere. A bounded functional has its operator quasi-norm \(\|L\|=\sup_{\|h\|_{1/2}\le1}|L(h)|\). No norm attainment is presumed. The result is a phase-optimized inequality for this standard de Leeuw–Rudin two-term decomposition at the specific exponent \(1/2\); it does not give the best constant for the full functional-dual problem.

## Proof

**1. Exact decomposition and the weighted square-root identity.** Write \(U_t=e^{-it}I\) and \(X_t=\operatorname{Re}U_t\) on the circle. Algebra gives \(IF=(H_{+,t}-H_{-,t})/2\). Since \(|U_t|=1\) almost everywhere,
\[
|H_{\pm,t}|=\tfrac12|1\pm U_t|^2|F|=(1\pm X_t)|F|.
\]
Consequently
\[
\frac{\|H_{\pm,t}\|_{1/2}}{\|F\|_{1/2}}
=\left(\int\sqrt{1\pm X_t}\,d\mu\right)^2.
\]
Introduce \(v(x)=(\sqrt{1+x},\sqrt{1-x})\in\mathbb R^2\) for \(-1\le x\le1\). It has \(\|v(x)\|^2=2\), and for the phase-dependent quotient \(P_t=(\|H_{+,t}\|_{1/2}+\|H_{-,t}\|_{1/2})/(2\|F\|_{1/2})\),
\[
P_t=\tfrac12\left\|\int v(X_t)\,d\mu\right\|^2,
\qquad
1-P_t=\tfrac14\iint\|v(X_t(\zeta))-v(X_t(\eta))\|^2d\mu(\zeta)d\mu(\eta).
\]
Both identities are exact, including the cases where \(X_t=\pm1\).

**2. Sharp variance control.** For any \(x,y\in[-1,1]\),
\[
2(x-y)=\langle v(x)-v(y),\, (v_1(x)+v_1(y),-v_2(x)-v_2(y))\rangle.
\]
The norm of the second vector is \(\|v(x)+v(y)\|\le2\sqrt2\). Cauchy–Schwarz yields \(\|v(x)-v(y)\|^2\ge(x-y)^2/2\). Since \(\iint(X_t(\zeta)-X_t(\eta))^2d\mu\,d\mu=2\operatorname{Var}_\mu(X_t)\), the preceding exact identity implies
\[
1-P_t\ge\tfrac14\operatorname{Var}_\mu(X_t).
\]
A direct expansion of \(X_t=(e^{-it}I+e^{it}\overline I)/2\) gives
\[
\operatorname{Var}_\mu(X_t)
=\tfrac12\Big(1-|\alpha|^2+\operatorname{Re}(e^{-2it}(\beta-\alpha^2))\Big).
\]
Its maximum over \(t\) equals \((1-|\alpha|^2+|\beta-\alpha^2|)/2\), proving the asserted envelope bound. The number in parentheses is nonnegative, since it equals twice a maximum of variances. If \(I\) is nonconstant, its unimodular boundary values cannot be constant on a positive-measure set; because the density of \(\mu\) is positive almost everywhere, \(|\alpha|<1\). The inequality for any bounded functional follows from the exact decomposition and \(|L(H)|\le\|L\|\|H\|_{1/2}\), then taking the infimum over \(t\).

**3. Universal sharpness of the envelope coefficient.** Fix \(0<\delta<\pi/2\), let \(I(z)=z\), and first consider the two-point probability \(\mu_\delta=(\delta_{e^{i\delta}}+\delta_{e^{-i\delta}})/2\). It has \(\alpha=\cos\delta\), \(\beta=\cos(2\delta)\), and
\[
S_\delta=1-|\alpha|^2+|\beta-\alpha^2|=2\sin^2\delta.
\]
For any phase, let \(x_{\pm}=\cos(\pm\delta-t)\). The two corresponding vectors \(v(x_\pm)\) lie on the positive-quadrant circle of radius \(\sqrt2\). Writing \(v(\cos\phi)=\sqrt2(|\cos(\phi/2)|,|\sin(\phi/2)|)\), their angular separation in that quadrant is at most \(\delta\); it is exactly \(\delta\) for \(t=\pi/2\). Hence their inner product is at least \(2\cos\delta\), with equality for that phase. By expanding the squared norm of their mean, the phase-optimized envelope is exactly
\[
\mathcal E(\mu_\delta)=\tfrac12(1+\cos\delta).
\]
Thus \((1-\mathcal E(\mu_\delta))/S_\delta=1/[4(1+\cos\delta)]\to1/8\) as \(\delta\downarrow0\).

The two-point measures are legitimate sharpness limits of **actual outer Hardy data**: let \(w_{r,\delta}(e^{i\theta})\) be the average of the normalized Poisson kernels of the boundary points \(e^{\pm i\delta}\), with \(r\uparrow1\). Each is positive, continuous, integrates to one, and has an outer function \(F_{r,\delta}\) with boundary modulus \(|F_{r,\delta}|=w_{r,\delta}^2\). Then \(\|F_{r,\delta}\|_{1/2}=1\), and its associated probability is exactly \(w_{r,\delta}dm\). Weak convergence to the two-point probability, together with joint continuity in phase on the compact circle, implies convergence of both the two moments and the minimum envelope. Taking \(r\uparrow1\) first and \(\delta\downarrow0\) next proves that no coefficient larger than \(1/8\) can hold uniformly.

## Verification

The algebraic decomposition, precise norm normalization, variance identity, phase maximization, and sharpness limit are established in the proof. The standalone \(\texttt{CHECK.py}\) runs independent finite-support numerical diagnostics for the vector inequality, phase-variance identity, and two-point sharpness formula; its finite tests do not establish the continuum result. To reproduce, run \(\texttt{python CHECK.py}\) with Python 3; no packages are needed.

## Relationship to prior work

Brevig and Søvik, *Extremals for linear functionals on \(H^p\) are outer when \(0<p<1\)* (arXiv:2610.21788, publicly released 2026-10-15), prove qualitative strict nonextremality of a nonconstant inner factor for \(0<p<1\) (Theorem 1 and Corollary 2). Their proof uses the same two-term decomposition and an unquantified strict Hölder inequality; it supplies neither the explicit first-two-moment defect nor its sharp phase-optimized constant at \(p=1/2\). De Leeuw and Rudin (1958, Section 2.2) introduced the splitting in a classical \(H^1\) extremal setting, not this quantitative quasi-Banach bound. The present theorem explicitly strengthens the decomposition's quantitative content but does not replace the known qualitative theorem for all exponents.

## Limitations

Only \(H^{1/2}\) is covered; the sharp \(1/8\) pertains to this particular two-term decomposition's phase-optimized envelope, not to all possible decompositions or dual functionals. The sharpness approximation uses smooth strictly positive densities, not atomic outer boundary measures themselves. A stronger unpublished quantitative refinement in the broader reverse-Hölder or Hardy literature may subsume the estimate; the current literature comparison does not prove global novelty. Independent mathematical audit has not been performed.

## References

1. O. F. Brevig and Ø. Søvik, *Extremals for linear functionals on \(H^p\) are outer when \(0<p<1\)*, arXiv:2610.21788, first public 15 October 2026. https://arxiv.org/html/2610.21788v1
2. K. de Leeuw and W. Rudin, *Extreme points and extremum problems in \(H^1\)*, Pacific Journal of Mathematics **8** (1958), 467–485, especially Section 2.2. https://msp.org/pjm/1958/8-3/pjm-v8-n3-p10-p.pdf
3. P. L. Duren, B. W. Romberg and A. L. Shields, *Linear functionals on \(H^p\) spaces with \(0<p<1\)*, Journal für die reine und angewandte Mathematik **238** (1969), 32–60; context for quasi-Banach Hardy duality.
