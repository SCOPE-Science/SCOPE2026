# A unique least-dispersed spherical lune for random squared chords

## Finding

For each opening angle \(0<\alpha\le\pi\), let \(L_\alpha\subset S^2\) be the closed spherical lune swept between two north-to-south great semicircles at longitude separation \(\alpha\). Let \(X,Y\) be independent surface-area-uniform points of \(L_\alpha\), and define their **squared ambient Euclidean chord length** as \(S_\alpha=\|X-Y\|^2\). Then

\[
\mathbb E S_\alpha=2-\frac{\pi^2\sin^2(\alpha/2)}{2\alpha^2},\qquad
V(\alpha):=\operatorname{Var}(S_\alpha)=\frac43+\frac89\left(\frac{\sin\alpha}{\alpha}\right)^2-\frac{\pi^4\sin^4(\alpha/2)}{4\alpha^4}.
\]

The mean is **strictly increasing** in \(\alpha\). In contrast, the variance first strictly decreases and then strictly increases. Precisely, define \(t_*\in(0,\pi/2)\) as the unique root of

\[
\left(t\cot t\right)^2+\frac{t^3}{\tan t-t}=\frac{9\pi^4}{256}.
\]

Then \(\alpha_*=2t_*\) is the **unique global variance-minimizing opening**, and the complete sharp bound is

\[
V(\alpha_*)\le V(\alpha)\le\frac{13}{12},\quad 0<\alpha\le\pi.
\]

Equality on the left holds exactly at \(\alpha=\alpha_*\), and equality on the right holds exactly at the hemisphere \(\alpha=\pi\). Numerically, \(\alpha_*=1.1164752259454760\ldots\) radians (about \(63.9693^\circ\)) and \(V(\alpha_*)=0.6753158386946393\ldots\). The collapsed-lune endpoint instead has the larger limiting variance

\[
\lim_{\alpha\downarrow0}V(\alpha)=\frac{20}{9}-\frac{\pi^4}{64}=0.7002051748159341\ldots.
\]

The interior minimum is nondegenerate: \(V(\alpha)-V(\alpha_*)=c_*(\alpha-\alpha_*)^2+O(|\alpha-\alpha_*|^3)\), where \(c_*>0\) and \(c_*=0.06977992640516\ldots\).

## Assumptions and scope

The sphere has unit radius. The chosen surface-area measure is normalized to a probability separately for each lune. The opening is restricted to \(0<\alpha\le\pi\), including a hemisphere at \(\pi\). A spherical lune has two antipodal pole vertices; it should not be confused with a *pointed* spherical convex body (an intersection of the sphere with a line-free cone). The distance is the Euclidean chord in \(\mathbb R^3\), **squared**. Neither intrinsic geodesic distance nor unsquared chord distance is optimized here. No claim is made about arbitrary spherical polygons or higher-dimensional wedges.

## Proof

**1. Exact one-point moments.** Use coordinates

\[
U=(\sin\theta\cos\phi,\sin\theta\sin\phi,\cos\theta),\quad 0\le\theta\le\pi,\quad -\alpha/2\le\phi\le\alpha/2.
\]

The normalized area element is \((2\alpha)^{-1}\sin\theta\,d\theta\,d\phi\). Therefore \(\phi\) is uniform on its interval and independent of \(\theta\), whose density is \(\sin\theta/2\). The relevant one-dimensional moments are

\[
\mathbb E\sin\theta=\frac\pi4,\quad \mathbb E\cos\theta=0,\quad
\mathbb E\sin^2\theta=\frac23,\quad\mathbb E\cos^2\theta=\frac13,
\]

and

\[
\mathbb E\cos\phi=\frac{2\sin(\alpha/2)}\alpha,\quad
\mathbb E\sin\phi=0,\quad
\mathbb E\cos^2\phi=\frac12\left(1+\frac{\sin\alpha}\alpha\right).
\]

Hence, writing \(m=\mathbb E U\) and \(M=\mathbb E UU^\top\),

\[
m=\left(\frac{\pi\sin(\alpha/2)}{2\alpha},0,0\right),\quad
M=\frac13\operatorname{diag}\left(1+\frac{\sin\alpha}\alpha,1-\frac{\sin\alpha}\alpha,1\right).
\]

**2. Two-point moments.** For independent copies \(X,Y\), \(S_\alpha=2-2X\cdot Y\). Independence and the trace identity give

\[
\mathbb E(X\cdot Y)=\|m\|^2,\qquad
\mathbb E(X\cdot Y)^2=\sum_{i,j}M_{ij}^2=\operatorname{tr}(M^2).
\]

Consequently \(\mathbb E S_\alpha=2-2\|m\|^2\) and \(\operatorname{Var}(S_\alpha)=4(\operatorname{tr}(M^2)-\|m\|^4)\), yielding the two formulas in the finding. Since \(\sin t/t\) strictly decreases for \(0<t\le\pi/2\), the mean strictly increases with \(\alpha\).

**3. Exact global variance derivative.** Set \(t=\alpha/2\) and \(q(t)=(\sin t/t)^2\). Rewriting the variance gives

\[
V(2t)=\frac43+\frac89q(t)\cos^2t-\frac{\pi^4}{64}q(t)^2.
\]

With

\[
H(t)=(t\cot t)^2+\frac{t^3}{\tan t-t},
\]

a direct differentiation, using \(q'(t)<0\), gives the exact factorization

\[
\frac{d}{dt}V(2t)
=q(t)q'(t)\left(\frac89H(t)-\frac{\pi^4}{32}\right).
\]

Both positive summands of \(H\) strictly decrease on \((0,\pi/2)\). For the first, \(t\cot t\) decreases because its derivative has numerator \(\sin t\cos t-t<0\). For the second, observe that \((\tan t-t)/t^3\) is strictly increasing. Indeed, its derivative has the sign of \(G(t)=t\tan^2t-3(\tan t-t)\), with

\[
G'(t)=2\tan t\,[t\sec^2t-\tan t]>0;
\]

here \(t\sec^2t-\tan t\) has derivative \(2t\sec^2t\tan t>0\) and vanishes at zero. Thus \(G(t)>0\) for positive \(t\). Finally \(H(t)\to4\) as \(t\downarrow0\), and \(H(t)\to0\) as \(t\uparrow\pi/2\). Since \(0<9\pi^4/256<4\), the defining equation has exactly one root. The derivative factorization now proves strict decrease before \(t_*\), strict increase afterward, and unique global minimization at \(\alpha_*\).

**4. Global maximum and rigidity.** As \(\alpha\downarrow0\), the variance approaches \(20/9-\pi^4/64\). At \(\alpha=\pi\) it equals \(13/12\), which is strictly larger than the collapsed-lune limit (for example \(\pi>3\) proves the required numerical inequality). Since the variance decreases then increases, \(13/12\) is the strict global maximum except at \(\pi\), where it is attained. Differentiating the factorized expression again at \(t_*\) gives

\[
\left.\frac{d^2}{dt^2}V(2t)\right|_{t_*}
=\frac89q(t_*)q'(t_*)H'(t_*)>0.
\]

Taylor's theorem then proves the stated nondegenerate quadratic local stability, with \(c_*=q(t_*)q'(t_*)H'(t_*)/9\) (the factor \(1/8\) accounts for the change from \(t\) to \(\alpha=2t\)). All differentiations are over the open interval; endpoint comparisons use continuous limits.

## Verification

The accompanying standalone Python checker verifies the stationary-point equation, exact hemisphere and collapsed-limit values, and independent area-uniform Monte Carlo estimates of both moments at four opening angles. It additionally tests the analytic profile on a finite grid. Reproduce with `python3 verification/checker.py`; the only dependency is the Python standard library. Its final output is `ALL_CHECKS_PASSED`. The infinitely many angles and the uniqueness assertion are justified by the derivative proof, **not** by sampling or finite-grid tests.

## Relationship to prior work

Moseeva, Tarasov and Zaporozhets (2020) derive a random-distance versus random-chord relation for spherical **pointed-cone** convex bodies and an explicit distribution for spherical caps. Their definition requires a line-free cone (Section 2), whereas the complete longitude lune here contains the two antipodal poles. Moreover, their stated cap results do not optimize squared Euclidean chord variance as a function of lune opening. The present calculation uses elementary surface moments and supplies a global shape classification absent from that work. General spherical integral-geometric moment identities are classical mathematical background, not claimed as new. A comprehensive historical priority determination is not asserted.

## Limitations

This establishes only the first two moments of **squared ambient chord distance** and their sharp optimization over \(0<\alpha\le\pi\). It does not determine the full chord-length distribution or any geodesic-distance variance. The optimum is expressed by a unique transcendental root, not a closed elementary angle. All numerical approximations and simulations are supplementary to the analytic proof. Older or unindexed spherical-wedge calculations could affect historical priority.

## References

1. T. Moseeva, A. Tarasov and D. Zaporozhets, *Random sections of spherical convex bodies*, arXiv:2007.07297 (first public version 2020-07-14), especially Sections 1–3. DOI: 10.1007/s10958-022-06236-6.
2. *Mathematics Subject Classification 2020*, code 52A55 (spherical and hyperbolic convexity), American Mathematical Society / zbMATH.
