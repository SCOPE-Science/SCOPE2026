# Sharp extreme lower tails of the two- and three-dimensional torus matching limits
## Finding
For \(d\in\{2,3\}\), let
\[
L_d=\sum_{[k]\in\mathcal P_d}\frac{2}{\lambda_k}(\zeta_{[k]}-1),
\qquad
\lambda_k=4\pi^2|k|^2,
\]
where \(\mathcal P_d=(\mathbb Z^d\setminus\{0\})/\{k\sim-k\}\) and the \(\zeta_{[k]}\) are independent \(\operatorname{Exp}(1)\) random variables. Then
\[
\lim_{x\to\infty}\frac1x\log\log\frac1{\Pr(L_2\le -x)}=4\pi,
\]
whereas
\[
\lim_{x\to\infty}\frac{-\log\Pr(L_3\le -x)}{x^3}
=\frac{8\pi^2}3.
\]
Thus the two-dimensional lower tail is double-exponential on the logarithmic scale, while the three-dimensional lower tail is stretched exponential with cubic exponent.

If
\[
q_d(\alpha)=\inf\{y:\Pr(L_d\le y)\ge\alpha\},
\]
then, as \(\alpha\downarrow0\),
\[
q_2(\alpha)\sim-\frac1{4\pi}\log\log\frac1\alpha,
\qquad
q_3(\alpha)\sim-
\left(\frac3{8\pi^2}\log\frac1\alpha\right)^{1/3}.
\]

## Assumptions and scope
The random variables \(L_2\) and \(L_3\) are exactly the limiting laws defined by Feng and Mordant for the centered quadratic matching cost on the flat torus. Their series converges almost surely and in \(L^2\). All logarithms here are natural logarithms.

The finding is a theorem about the limiting random variables. Weak convergence of a finite-sample statistic to \(L_d\) does not by itself justify replacing extreme finite-sample tail probabilities by these formulas. No uniform-in-tail finite-sample approximation is claimed.

## Proof
Set \(Y_d=-L_d\) and
\[
a_k=\frac2{\lambda_k}=\frac1{2\pi^2|k|^2}.
\]
For \(s>0\), independence gives
\[
K_d(s):=\log\mathbb E e^{sY_d}
=\sum_{[k]\in\mathcal P_d}
\left(sa_k-\log(1+sa_k)\right).
\]
Writing \(g(u)=u-\log(1+u)\), this is finite because \(g(u)\sim u^2/2\) at the origin and \(\sum |k|^{-4}<\infty\) for \(d=2,3\).

For \(d=3\), put \(c=1/(2\pi^2)\) and \(R=\sqrt{cs}\). Pairing \(k\) and \(-k\) yields
\[
K_3(s)=\frac12\sum_{k\in\mathbb Z^3\setminus\{0\}}
g\left(\frac{R^2}{|k|^2}\right).
\]
A lattice Riemann-sum limit gives
\[
K_3(s)\sim
\frac12R^3\int_{\mathbb R^3}g(|y|^{-2})\,dy.
\]
The integral is finite at both zero and infinity. To evaluate it, define
\[
J(a)=\int_0^\infty r^2
\left(\frac a{r^2}-\log\left(1+\frac a{r^2}\right)\right)dr.
\]
Differentiation under the integral gives
\[
J'(a)=\int_0^\infty\frac a{r^2+a}dr
=\frac\pi2\sqrt a,
\]
so \(J(a)=\pi a^{3/2}/3\). Hence
\[
\int_{\mathbb R^3}g(|y|^{-2})\,dy=\frac{4\pi^2}3
\]
and therefore
\[
K_3(s)\sim A_3s^{3/2},
\qquad
A_3=\frac1{3\sqrt2\,\pi}.
\]
Convexity and regular variation imply
\[
K_3'(s)\sim\frac32A_3s^{1/2},
\]
while direct differentiation gives
\[
K_3''(s)=
\sum_{[k]}\frac{a_k^2}{(1+sa_k)^2}
=O(s^{-1/2}).
\]
Optimizing the Chernoff bound gives
\[
\inf_{s>0}\bigl(K_3(s)-sx\bigr)
\sim-\frac4{27A_3^2}x^3
=-\frac{8\pi^2}3x^3.
\]
For the matching lower bound, tilt by
\[
\frac{d\mathbb P_s}{d\mathbb P}
=e^{sY_3-K_3(s)}.
\]
Choose \(s\) so that \(K_3'(s)\) is slightly larger than \(x\). Under \(\mathbb P_s\), the variance is \(K_3''(s)=o(x^2)\), so \(Y_3\) concentrates in a relative-width window above \(x\). Undoing the tilt and then shrinking that relative width yields the same cubic constant.

For \(d=2\),
\[
K_2'(s)
=\frac c2\sum_{k\in\mathbb Z^2\setminus\{0\}}
\frac{R^2}{|k|^2(|k|^2+R^2)}.
\]
The elementary lattice count
\[
N(r)=\#\{k\in\mathbb Z^2:0<|k|\le r\}
=\pi r^2+O(r)
\]
and Abel summation give
\[
\sum_{k\ne0}
\frac{R^2}{|k|^2(|k|^2+R^2)}
\sim2\pi\log R.
\]
Since \(R^2=cs\),
\[
K_2'(s)\sim\frac1{4\pi}\log s,
\qquad
K_2(s)\sim\frac1{4\pi}s\log s.
\]
Also
\[
K_2''(s)
=\frac{c^2}2
\sum_{k\ne0}\frac1{(|k|^2+cs)^2}
=O(s^{-1}).
\]
For any fixed \(\varepsilon\in(0,1)\), choosing
\[
s=\exp\left((1-\varepsilon)4\pi x\right)
\]
in the Chernoff bound yields
\[
\liminf_{x\to\infty}
\frac1x\log\bigl[-\log\Pr(Y_2\ge x)\bigr]
\ge4\pi(1-\varepsilon).
\]
For the reverse inequality, choose
\[
s=\exp\left((1+\varepsilon)4\pi x\right).
\]
Then \(K_2'(s)\sim(1+\varepsilon)x\) and \(K_2''(s)\to0\), so under the same exponential tilt \(Y_2\) concentrates just above \(x\). Undoing the tilt gives
\[
\limsup_{x\to\infty}
\frac1x\log\bigl[-\log\Pr(Y_2\ge x)\bigr]
\le4\pi(1+\varepsilon).
\]
Letting \(\varepsilon\downarrow0\) proves the two-dimensional limit. The quantile formulas follow by monotone inversion of the two tail asymptotics.

## Verification
The constant in the three-dimensional Legendre transform was checked algebraically:
\[
\frac4{27A_3^2}=\frac{8\pi^2}3
\quad\text{for}\quad
A_3=\frac1{3\sqrt2\,\pi}.
\]
The dimension-two coefficient was independently recovered from the continuum radial integral for \(K_2'(s)\), with the quotient by \(k\sim-k\) contributing the required factor \(1/2\). The proof uses analytic asymptotics rather than finite enumeration.

## Relationship to prior work
Feng and Mordant identify the exact non-Gaussian limits \(L_2\) and \(L_3\), including the weighted centered-exponential representation, but do not state their extreme lower-tail or lower-quantile asymptotics.

Wang and Zhao give a broader determinant/Laplace-transform framework for second-Wiener-chaos quadratic energies and obtain growth orders of the logarithmic Laplace transform in logarithmic and Riesz regimes. Those results cover the qualitative growth orders underlying this calculation, but the inspected theorem does not give the flat-torus spectral constants \(1/(4\pi)\) and \(1/(3\sqrt2\,\pi)\), nor the resulting sharp probability constants \(4\pi\) and \(8\pi^2/3\).

Classical small-deviation results for positive quadratic Gaussian norms address trace-class-type nonnegative sums. Here \(\sum a_k=\infty\) while \(\sum a_k^2<\infty\), so the object is a centered, renormalized quadratic series rather than a finite positive quadratic norm.

## Limitations
The theorem does not provide finite-sample moderate- or large-deviation bounds for the empirical matching cost. In particular, it cannot be used by itself to assign extreme finite-sample significance levels from the weak convergence theorem. The proof also treats only the explicit limiting laws in dimensions two and three.

A residual literature risk remains that a sufficiently general sharp Tauberian theorem for non-trace-class second-chaos series may imply the same constants after insertion of the torus spectrum; targeted searches did not locate such a statement specialized to these laws.

## References
1. Shi Feng and Gilles Mordant, *Fluctuations of the quadratic matching cost on the flat torus: dimensions two, three and four*, arXiv:2609.26597v1, 2026.
2. Zhenfu Wang and Xianliang Zhao, *Uniform Partition-Function Estimates for Coulomb Modulated Energy at All Positive Temperatures*, arXiv:2609.00867v1, 2026.
3. M. A. Lifshits and A. I. Nazarov, *\(L_2\)-Small Deviations for Weighted Stationary Processes*, arXiv:1705.00422, 2017.
