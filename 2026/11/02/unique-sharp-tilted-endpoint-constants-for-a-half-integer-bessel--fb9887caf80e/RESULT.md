# Unique sharp tilted endpoint constants for a half-integer Bessel moment

## Finding
Let \(0<\gamma<1\), and define, for every \(x>0\),
\[
R_\gamma(x)=\frac{\displaystyle\int_0^x e^{-\gamma t}t^{1/2}I_{1/2}(t)\,dt}{e^{-\gamma x}x^{1/2}I_{3/2}(x)}
=\frac{e^{\gamma x}\displaystyle\int_0^x e^{-\gamma t}\sinh t\,dt}{\cosh x-\sinh x/x}.
\]
Here \(I_\nu\) is the modified Bessel function of the first kind, with its standard series normalization. The sharp upper constant \(M_\gamma=\sup_{x>0}R_\gamma(x)\) is attained at **exactly one** finite point \(x_\gamma>0\). It is strictly larger than both endpoint ratios,
\[
M_\gamma>\max\left\{\frac32,\frac{1}{1-\gamma}\right\}.
\]

Set \(L(x)=\coth x-1/x\), and
\[
D_\gamma(x)=1-\frac{L(x)}x-\gamma L(x).
\]
The point \(x_\gamma\) is the **unique positive solution** of the explicit scalar equation
\[
\left(\int_0^x e^{-\gamma t}\sinh t\,dt\right)D_\gamma(x)
=e^{-\gamma x}\left(\cosh x-\frac{\sinh x}{x}\right).
\]
Consequently \(M_\gamma=1/D_\gamma(x_\gamma)\), or, without numerical integration,
\[
M_\gamma=\frac{x_\gamma\big[(1+\gamma)+(1-\gamma)e^{-2x_\gamma}-2e^{-(1-\gamma)x_\gamma}\big]}{(1-\gamma^2)\big[(x_\gamma-1)+(x_\gamma+1)e^{-2x_\gamma}\big]}.
\]
Equality in the sharp Bessel integral inequality occurs if and only if \(x=x_\gamma\).

The optimizers and optimal constants obey two different endpoint scaling laws. As \(\gamma\downarrow0\),
\[
x_\gamma=10\gamma+O(\gamma^3),\qquad M_\gamma=\frac32+\frac52\gamma^2+O(\gamma^4).
\]
As \(\gamma\uparrow1\), put \(\delta=1-\gamma\) and \(\Lambda=\log(1/\delta)\). Then
\[
\delta x_\gamma=\Lambda+2\log\Lambda+o(1),\qquad
M_\gamma=\frac1\delta+\frac{1+o(1)}{\Lambda}.
\]
The second formula quantifies a logarithmically small **additive** surplus beyond the large-\(x\) endpoint constant.

## Assumptions and scope
All statements hold for every real \(\gamma\in(0,1)\), with \(x>0\). The window corresponds exactly to power parameter \(q=1\) and Bessel order \(\mu=1/2\) in the sharp power-weighted quotient \(R_{\mu,q,\gamma}\). The factor \(x^{1/2}\) is essential in both numerator and denominator. No claim is made for arbitrary orders or powers, and the asymptotic remainder statements are one-sided at the indicated ends of the tilt interval.

## Proof
**1. Elementary representation and endpoints.** The half-integer identities are
\[
I_{1/2}(x)=\sqrt{\frac{2}{\pi x}}\sinh x,\qquad
I_{3/2}(x)=\sqrt{\frac{2}{\pi x}}\left(\cosh x-\frac{\sinh x}{x}\right).
\]
Define \(F_\gamma(x)=\int_0^x e^{-\gamma t}\sinh t\,dt\) and \(G_\gamma(x)=e^{-\gamma x}(\cosh x-\sinh x/x)\). Both vanish at the origin and are strictly positive on \((0,\infty)\), while \(F_\gamma'(x)=e^{-\gamma x}\sinh x>0\). Then \(R_\gamma=F_\gamma/G_\gamma\). Direct integration yields
\[
R_\gamma(x)=\frac{x\big[(1+\gamma)+(1-\gamma)e^{-2x}-2e^{-(1-\gamma)x}\big]}{(1-\gamma^2)\big[(x-1)+(x+1)e^{-2x}\big]}.
\]
Series at zero and exponential asymptotics at infinity give
\[
\lim_{x\downarrow0}R_\gamma(x)=\frac32,\qquad
R_\gamma(x)=\frac1{1-\gamma}+\frac1{(1-\gamma)x}+O_\gamma(x^{-2})\quad(x\to\infty).
\]

**2. A strict one-turn derivative ratio.** Write \(H_\gamma=G_\gamma/F_\gamma=1/R_\gamma\). The quotient of derivatives is
\[
\frac{G_\gamma'(x)}{F_\gamma'(x)}=D_\gamma(x)=1-\frac{L(x)}x-\gamma L(x),\qquad L(x)=\coth x-\frac1x.
\]
We have \(L'(x)=x^{-2}-\sinh^{-2}x>0\). Let
\[
q(x)=-\frac{(L(x)/x)'}{L'(x)}.
\]
An exact logarithmic-derivative identity gives
\[
q(x)=\frac12\frac{d}{dx}\log\left(\frac{\sinh^2x-x^2}{x^4}\right).
\]
The function inside the logarithm is a **strictly log-convex moment-generating function**: Taylor's integral remainder gives
\[
\frac{\sinh^2x-x^2}{x^4}=\frac43\int_0^1(1-s)^3\cosh(2sx)\,ds.
\]
This is the Laplace transform of a positive, nondegenerate symmetric measure. Its logarithmic second derivative is the strictly positive variance of the tilted measure. Thus \(q'(x)>0\) for all \(x>0\). Its endpoint limits, directly from the hyperbolic expansions, are \(q(0+)=0\) and \(q(\infty)=1\). Therefore
\[
D_\gamma'(x)=L'(x)\big(q(x)-\gamma\big)
\]
is strictly negative before a single point and strictly positive thereafter.

**3. Passing the one turn from derivatives to the quotient.** Define \(P_\gamma(x)=F_\gamma(x)D_\gamma(x)-G_\gamma(x)\). Since \(G_\gamma'=F_\gamma'D_\gamma\),
\[
P_\gamma'(x)=F_\gamma(x)D_\gamma'(x).
\]
Moreover, \(P_\gamma(0+)=0\), so \(P_\gamma\) strictly decreases until the unique minimum of \(D_\gamma\) and then strictly increases. At infinity, using \(L(x)=1-x^{-1}+O(e^{-2x})\),
\[
D_\gamma(x)-\frac{G_\gamma(x)}{F_\gamma(x)}=x^{-2}+O_\gamma(x^{-3})+O_\gamma(e^{-(1-\gamma)x})>0
\]
for all sufficiently large \(x\). Thus \(P_\gamma\) crosses zero exactly once on \((0,\infty)\). Since
\[
H_\gamma'(x)=\frac{F_\gamma'(x)}{F_\gamma(x)}\big(D_\gamma(x)-H_\gamma(x)\big),
\]
\(H_\gamma\) strictly decreases and then strictly increases, and \(R_\gamma=1/H_\gamma\) strictly increases and then strictly decreases. The unique critical point is \(x_\gamma\), with the stated defining equation. Strict endpoint inequalities follow from these monotonicity statements and the asymptotic at infinity.

**4. Small tilt.** The explicit hyperbolic formula admits a real-analytic extension near \((x,\gamma)=(0,0)\), with expansion
\[
R_\gamma(x)=\frac32+\frac{\gamma x}{2}+\left(\frac{\gamma^2}{8}-\frac1{40}\right)x^2+\frac{\gamma(\gamma^2-1)}{40}x^3+O(x^4).
\]
The stationary equation has derivative \(-1/20\) with respect to \(x\) and derivative \(1/2\) with respect to \(\gamma\) at the origin. The analytic implicit-function theorem gives \(x_\gamma=10\gamma+O(\gamma^3)\). The cubic remainder order follows from the symmetry \(R_{-\gamma}(-x)=R_\gamma(x)\) of the analytic continuation and uniqueness of the local branch. Substitution yields \(M_\gamma=3/2+5\gamma^2/2+O(\gamma^4)\).

**5. Critical tilt.** Put \(\delta=1-\gamma\), \(\Lambda=\log(1/\delta)\), \(y_\gamma=\delta x_\gamma\). Because \(M_\gamma\ge\delta^{-1}\) whereas \(R_\gamma\) is bounded on compact \(x\)-intervals uniformly as \(\delta\downarrow0\), we first have \(x_\gamma\to\infty\). If \(y_\gamma\) stayed bounded, the elementary formula in Step 1 would imply \(\delta R_\gamma(x_\gamma)=1-e^{-y_\gamma}+o(1)<1\), uniformly on bounded ranges of \(y_\gamma\), contradicting \(\delta M_\gamma\ge1\). Hence \(y_\gamma\to\infty\).

At the maximizing point, differentiating the closed formula of Step 1 and grouping the terms with \(e^{-2x_\gamma}\) gives
\[
2e^{-y_\gamma}\big(1+\delta x_\gamma(x_\gamma-1)\big)
=2-\delta+O(x_\gamma^2e^{-2x_\gamma}).
\]
Since \(y_\gamma\to\infty\), logarithms imply
\[
y_\gamma=\Lambda+2\log y_\gamma+o(1).
\]
As the large solution of this equation has \(y_\gamma/\Lambda\to1\), it follows that \(y_\gamma=\Lambda+2\log\Lambda+o(1)\). The same stationary equation shows
\[
\frac{2e^{-y_\gamma}}{2-\delta}=\frac{\delta}{y_\gamma^2}(1+o(1)).
\]
Substituting into the exact ratio and using \(x_\gamma=y_\gamma/\delta\) yields
\[
M_\gamma-\frac1\delta=\frac1{y_\gamma}+o(y_\gamma^{-1})=\frac{1+o(1)}\Lambda.
\]
This completes the proof of the entire stated claim.

## Verification
`CHECK.py` reproduces the half-integer Bessel normalization by independent quadrature, verifies the closed primitive and the exact logarithmic derivative identity at high precision, brackets unique critical points for representative tilts, and compares both asymptotic regimes. It uses `mpmath` and prints an explicit assertion count on success. These finite checks are supplementary: the proof of uniqueness and the asymptotics for every admissible tilt is analytic in Steps 2–5.

## Relationship to prior work
Yang and Zhang (arXiv:2605.20983, first public 2026-05-20), Section 6, give a general sharp-constant supremum and a stationary-value representation for \(R_{\mu,q,\gamma}\), together with endpoint expansions. That characterization alone leaves open the number of critical points, the unique optimizing parameter, and the matched critical-tilt law proved above. In particular, the general bound supplied in their Theorem 3.3 is explicitly not sharp. Gaunt (arXiv:2501.12197, 2025) investigates precisely the positive-power Bessel integral, but his Theorem 2.1 supplies parameter-dependent upper inequalities rather than the globally sharp constant for this half-integer order. Gaunt (arXiv:1806.00524, 2018) develops earlier related integral inequalities, not this one-turn optimization theorem. The structural key here is strict log-convexity of an integral representation for \((\sinh^2x-x^2)/x^4\), combined with a one-turn quotient argument.

## Limitations
The result is confined to the natural half-integer power-weighted case \((\mu,q)=(1/2,1)\) and \(0<\gamma<1\); it does not assert a comparable uniqueness statement for all Bessel orders or weight exponents. The maximizing point is specified by a unique transcendental root, not an elementary expression. The work is not an independently audited classification of all previous special-function identities, and an unindexed equivalent optimization remains possible.

## References
- Y. Yang and Y. Zhang, *Weighted Uniform Endpoint Majorants for Integrals Involving Modified Bessel Functions*, arXiv:2605.20983, first submitted 2026-05-20. https://arxiv.org/abs/2605.20983
- R. E. Gaunt, *Inequalities for an integral involving the modified Bessel function of the first kind*, arXiv:2501.12197, first submitted 2025-01-21. https://arxiv.org/html/2501.12197v1
- R. E. Gaunt, *Inequalities for some integrals involving modified Bessel functions*, arXiv:1806.00524, first submitted 2018-06-01. https://arxiv.org/abs/1806.00524
