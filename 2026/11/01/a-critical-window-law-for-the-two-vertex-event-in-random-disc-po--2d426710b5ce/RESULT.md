# A critical-window law for the two-vertex event in random disc-polygons

## Finding

Let \(B=\{x\in\mathbb R^2:|x|\le1\}\). Sample \(X_1,\dots,X_n\) independently and uniformly from \(B\), with \(n\ge2\). For \(R\ge1\), form their radius-\(R\) ball-convex hull, the intersection of all closed radius-\(R\) discs containing the sample. Let \(N_{n,R}\) be the number of sample points that are ball-extreme (deleting such a point changes the hull), and put \(p_n(R)=\Pr(N_{n,R}=2)\).

**Theorem (three regimes and their crossover).** For fixed \(R>1\), set
\[
q_R=\frac{2R^2\arcsin(1/R)-2\sqrt{R^2-1}}{\pi},\qquad 0<q_R<1.
\]
Then, as \(n\to\infty\),
\[
\boxed{p_n(R)\sim \frac{\pi^2}{4}\sqrt{2q_R}\,(R^2-1)^{5/4}\,n^{-1/2}q_R^n.}
\]
At the critical radius \(R=1\), the decay is polynomial rather than exponential. More precisely,
\[
\boxed{\begin{aligned}
p_n(1)={}&\frac{\pi^4}{8(n+1)(n+2)(n+3)}\\
&+\frac{11\pi^6}{32(n+1)(n+2)(n+3)(n+4)(n+5)}+O(n^{-7}).
\end{aligned}}
\]
In particular, \(\lim_{n\to\infty}n^3p_n(1)=\pi^4/8\).

There is an exact intermediate window. For every fixed \(\kappa\ge0\), choosing \(R_n=1+\kappa/n^2\) gives
\[
\boxed{\lim_{n\to\infty}n^3p_n(R_n)=F(\kappa):=\frac{16}{3\pi}\int_0^\infty t^4\exp\!\left(-\frac4\pi\sqrt{t^2+2\kappa}\right)\,dt.}
\]
The crossover \(F\) is positive, continuous and strictly decreasing, with
\[
F(0)=\frac{\pi^4}{8},\qquad
F(\kappa)\sim\pi^2 2^{-1/4}\kappa^{5/4}
\exp\!\left(-\frac{4\sqrt{2\kappa}}{\pi}\right)
\quad(\kappa\to\infty).
\]

The previously known all-sample-size moment representation for \(p_n(R)\) is explicitly **not** claimed as new. The claim here is the fixed-radius rare-event asymptotics, its second critical term, and the sharp \(n^{-2}\) crossover with explicit scaling function.

## Assumptions and scope

The source body is precisely the Euclidean unit disc, the sample law is independent uniform area measure, and hull discs have the Euclidean radius \(R\ge1\). All \(n\)-limits are through integers. The fixed-radius assertion takes \(R>1\) constant; the critical-window assertion takes \(\kappa\) fixed independently of \(n\). Assertions are not claimed uniformly over all simultaneous choices of \(R\) and \(n\).

For distinct sample points the number of ball-extreme points is unambiguous almost surely. Writing \(\operatorname{sp}_R(x,y)\) for the intersection of all radius-\(R\) discs containing two points \(x,y\), that spindle belongs to \(B\) whenever \(x,y\in B\) and \(R\ge1\). This follows from ball-convexity of \(B\), itself the intersection of suitably shifted radius-\(R\) discs tangent to \(\partial B\).

## Proof

**1. Reduction to a one-dimensional endpoint integral.** Exactly two sample points are ball-extreme if and only if one unordered pair generates the entire hull. Outside the probability-zero coincidence set the pair is unique, so by conditioning on that pair,
\[
p_n(R)=\binom n2\int_0^1 g(\ell)\left(\frac{A_R(\ell)}\pi\right)^{n-2}\,d\ell,
\]
where \(\ell\) is the half-distance between two independent uniform points of \(B\). The explicit classical distance density and spindle area are
\[
g(\ell)=\frac{16\ell}{\pi}\left(\arccos\ell-\ell\sqrt{1-\ell^2}\right),\quad
A_R(\ell)=2R^2\arcsin(\ell/R)-2\ell\sqrt{R^2-\ell^2}.
\]
These formulas, together with the two-extreme-point moment identity, are established in Bakó-Szabó, Besau and Fodor (2026), Equations (3.4), (4.10) and (1.3). Their combination supplies the starting integral, not the new asymptotic theorem. Set \(\ell=\cos\theta\), \(0\le\theta\le\pi/2\). Then
\[
p_n(R)=\binom n2\frac{16}{\pi}
\int_0^{\pi/2}\sin\theta\cos\theta
(\theta-\sin\theta\cos\theta)
\left(\frac{A_R(\cos\theta)}{\pi}\right)^{n-2}d\theta.\tag{1}
\]

**2. Fixed \(R>1\).** The function \(A_R\) is strictly increasing, since
\[A_R'(\ell)=\frac{4\ell^2}{\sqrt{R^2-\ell^2}}.\]
Its normalized endpoint value is \(q_R=A_R(1)/\pi\in(0,1)\). As \(\ell\uparrow1\), direct Taylor expansions give
\[
g(\ell)=\frac{64\sqrt2}{3\pi}(1-\ell)^{3/2}
+O((1-\ell)^{5/2}),
\]
\[
\frac{A_R(\ell)}\pi=q_R-\beta_R(1-\ell)+O_R((1-\ell)^2),\qquad
\beta_R=\frac{4}{\pi\sqrt{R^2-1}}>0.
\]
Endpoint Laplace asymptotics, justified by splitting away a fixed neighbourhood of \(\ell=1\) and scaling \(1-\ell\) as \(n^{-1}\), yields
\[
p_n(R)\sim\frac{n^2}{2}q_R^{n-2}
\frac{64\sqrt2}{3\pi}
\Gamma(5/2)\left(\frac{q_R}{n\beta_R}\right)^{5/2}.
\]
Because \(\Gamma(5/2)=3\sqrt\pi/4\), the coefficient simplifies to the stated \((\pi^2/4)\sqrt{2q_R}(R^2-1)^{5/4}\). The strict endpoint maximum and exponential suppression off it supply the standard domination needed for this calculation.

**3. The critical radius.** For \(R=1\),
\[
\frac{A_1(\cos\theta)}\pi=1-u(\theta),\qquad
u(\theta)=\frac2\pi(\theta+\sin\theta\cos\theta),
\]
where \(u\) increases from zero to one, with \(du/d\theta=4\cos^2\theta/\pi\). Formula (1) becomes
\[
p_n(1)=\binom n2\int_0^1 h(u)(1-u)^{n-2}\,du,
\qquad h(u)=4\tan\theta(u)\left(\theta(u)-\sin\theta(u)\cos\theta(u)\right).
\]
The analytic inverse expansion of \(u(\theta)\) at zero is
\[
\theta(u)=\frac{\pi u}{4}+\frac{\pi^3u^3}{192}+\frac{\pi^5u^5}{3840}+O(u^7),
\]
which gives
\[
h(u)=\frac{\pi^4}{96}u^4+\frac{11\pi^6}{11520}u^6+O(u^8).
\]
Termwise beta integration uses \(\int_0^1u^j(1-u)^{n-2}\,du=j!(n-2)!/(n+j-1)!\). The prefactor \(\binom n2\) changes the first two terms to the displayed rational-denominator expressions. To control the remainder, fix a small positive \(\varepsilon\): on \([0,\varepsilon]\) it is bounded by a constant times \(u^8\), whose beta moment contributes \(O(n^{-7})\), while \([\varepsilon,1]\) is exponentially suppressed. This proves the critical expansion for all sufficiently large integers \(n\).

**4. The critical window.** Put \(R_n=1+\kappa/n^2\) and \(\theta=t/n\) in (1). For each fixed \(t\ge0\), the square-root and inverse-sine expansions, including the endpoint \(\kappa=t=0\) by continuity, yield
\[
\frac{A_{R_n}(\cos(t/n))}{\pi}
=1-\frac{4}{\pi n}\sqrt{t^2+2\kappa}+O_{t,\kappa}(n^{-2}),
\]
so the power \(n-2\) converges to \(\exp(-4\sqrt{t^2+2\kappa}/\pi)\). Moreover,
\[
\sin(t/n)\cos(t/n)\left(t/n-\sin(t/n)\cos(t/n)\right)
=\frac{2t^4}{3n^4}+O_t(n^{-6}).
\]
Dominated convergence is legitimate: monotonicity in \(R\) gives \(A_{R_n}\le A_1\), and
\[
0\le A_1(\cos\theta)/\pi
=1-\frac2\pi(\theta+\sin\theta\cos\theta)
\le e^{-2\theta/\pi}.
\]
For all \(0\le\theta\le\pi/2\), the positive geometric weight in (1) is at most \((2/3)\theta^4\), by integrating \(2\sin^2\theta\le2\theta^2\). After the change \(t=n\theta\), the rescaled integrand is therefore dominated by a constant times \(t^4e^{-t/\pi}\), uniformly for \(n\ge4\), with the domain extended to \([0,\infty)\) by zero. The limit is \(F(\kappa)\) as stated.

The integral is continuous in \(\kappa\) by the same domination, and strictly decreases because its exponential integrand strictly decreases at every \(t\) when \(\kappa\) increases. Direct gamma integration gives \(F(0)=\pi^4/8\). For \(\kappa\to\infty\), write \(s=\sqrt{2\kappa}\) and use
\(\sqrt{t^2+s^2}=s+t^2/(2s)+O(t^4/s^3)\) in the dominant range \(t=O(s^{1/2})\). A Gaussian fourth-moment integral yields
\[
F(\kappa)\sim\frac{16}{3\pi}e^{-4s/\pi}
\int_0^\infty t^4e^{-2t^2/(\pi s)}\,dt
=\pi^2 2^{-1/4}\kappa^{5/4}e^{-4\sqrt{2\kappa}/\pi}.
\]
Standard splitting into \(t\le s^{3/4}\) and its exponentially negligible complement makes the Gaussian approximation rigorous. This finishes the proof.

## Verification

Run `python verify.py` with Python 3, SymPy and mpmath installed. The program independently computes the local inverse series by solving its coefficient equations, checks the exact critical coefficients and gamma-factor normalization, numerically evaluates the original distance integral for multiple fixed radii and sample sizes, checks the two known small-sample identities, and confirms convergence along three critical-window sequences. Its expected output is `VERIFY_OK: 32 symbolic identities / integral checks; fixed-radial and critical-window comparisons`.

For example, at radius one the numerical critical ratio \(n^3p_n(1)/(\pi^4/8)\) is approximately \(0.94477\) at \(n=100\), \(0.98820\) at \(n=500\), and \(0.99701\) at \(n=2000\); the analytic beta expansion explains this convergence. At radius \(R=1.5\), the numerically evaluated fixed-radius asymptotic ratio is approximately \(1.00475\) for \(n=500\). These are finite cross-checks only. Proof for all fixed \(R\) and all \(\kappa\) is analytic above.

## Relationship to prior work

Bakó-Szabó, Besau and Fodor (2026) establish the ball-convex Efron–Buchta identities, and give an exact **all-\(n\)** expression for the two-vertex probability through moments of the area of a random ball-segment: their Corollary 4.4, Proposition 4.3, and Equations (3.4), (4.10)–(4.11). Thus **the integral representation and the special cases \(n=3,4\) are prior work**, not newly claimed here. The inspected article treats exact small-sample Sylvester probabilities and general moment identities, but does not state the large-\(n\) polynomial/exponential transition, the critical width \(R-1\asymp n^{-2}\), or the crossover integral and coefficient. These last statements require joint endpoint asymptotics of both the density and the spindle area, beyond merely invoking the moment identity.

Marynych and Molchanov (2022) establish weak convergence and moment convergence for the face-vector of random \(K\)-hulls; these limit theorems do not directly provide the exact probability's decaying rate or its varying-radius crossover. Fodor and Montenegro Pinzón (2024) and Fodor and Papvári (2025/2026) give expectation and expansion results in smooth-disc models, but do not state the two-vertex rare-event crossover. A historical equivalent under other geometric-probability terminology remains possible.

## Limitations

The leading constant and the two-term critical expansion concern exactly the **two-vertex** event; they do not give the full face-number distribution, rare-event probabilities for three or more vertices, or fluctuations. The crossover holds for fixed nonnegative \(\kappa\) and is not a global uniform approximation for all radii. Nothing is asserted for source bodies other than discs or for higher dimensions. The exact integral and general Efron–Buchta identities are known; novelty is limited to the asymptotic phase law. Historical priority is provisional and independent mathematical review has not been performed.

## References

1. A. Bakó-Szabó, F. Besau and F. Fodor, *Sylvester's four point problem for ball-convex bodies*, arXiv:2608.29975v1 (public 2026-08-30), especially Equations (1.3), (3.4), (4.10)–(4.11) and Corollary 4.4. https://arxiv.org/html/2608.29975v1
2. A. Marynych and I. Molchanov, *Facial structure of strongly convex sets generated by random samples*, Advances in Mathematics **395** (2022), 108086; arXiv:2102.10009. https://arxiv.org/abs/2102.10009
3. F. Fodor and N. A. Montenegro Pinzón, *Series expansions for random disc-polygons in smooth plane convex bodies*, Journal of Applied Probability (2024). https://doi.org/10.1017/jpr.2024.27
4. F. Fodor and D. I. Papvári, *On generalized disc-polygons in plane convex bodies with a higher degree of smoothness*, arXiv:2509.11702 (public 2025-09-15). https://arxiv.org/abs/2509.11702
5. F. Fodor, T. Kevei and V. Vígh, *On random disc-polygons in smooth convex discs*, Advances in Applied Probability **46** (2014), 899–918. https://doi.org/10.1239/aap/1418396236
