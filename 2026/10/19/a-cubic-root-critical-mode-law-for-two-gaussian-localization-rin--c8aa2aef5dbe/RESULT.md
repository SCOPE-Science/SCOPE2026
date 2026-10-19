# A cubic-root critical mode law for two Gaussian localization rings

## Finding
Fix \(w>0\), \(d>0\), and let \(a\to\infty\). In Gaussian-window time-frequency localization, take two equal-area concentric annuli whose area-coordinate intervals are
\[
I_{a,d,w}^{\pm}=[a\pm d\sqrt a-w/2,\ a\pm d\sqrt a+w/2].
\]
They are positive and disjoint for sufficiently large \(a\). For each \(n\ge0\), the normalized Hermite eigenvalue is
\[
\lambda_n(a;d,w)=\frac1{n!}\sum_{\sigma\in\{-1,1\}}\int_{I_{a,d,w}^{\sigma}}e^{-t}t^n\,dt.
\]
For any maximizing nonnegative integer \(n_a\), the following three regimes hold:
\[
\begin{array}{ll}
0<d<1:&n_a=a+O_{d,w}(1);\\
d=1:&n_a=a-2^{1/3}a^{1/3}+o_w(a^{1/3});\\
d>1:&n_a=a-x_d\sqrt a+o_{d,w}(\sqrt a),
\end{array}
\]
where \(x_d\in(0,d)\) is the unique positive solution of \(x_d=d\tanh(d x_d)\). When \(d>1\), the spectrum has two macroscopically separated local peaks near \(a\pm x_d\sqrt a\), but the lower-index peak uniquely dominates at leading nonvanishing order. In the critical case, the global maximizer moves by the non-Gaussian scale \(a^{1/3}\), despite the two rings being symmetric about \(a\).

## Assumptions and scope
The Gaussian window has unit \(L^2\) norm and the area coordinate is \(t=\pi(x^2+\xi^2)\). The symbol is the indicator of the two annuli. The degree \(n\) ranges over all nonnegative integers. Constants in asymptotic estimates can depend on fixed \(d,w\), never on \(a\) or \(n\). Any maximizer is covered; uniqueness for all finite \(a\) is not asserted. At \(d=1\) the coefficient is independent of the fixed positive width \(w\).

## Proof
Daubechies' radial diagonalization gives the displayed Hermite eigenvalues. Put \(R=\sqrt a\), \(x=(n-a)/R\), and \(u\in\{-d,d\}\). Stirling's formula, uniformly for bounded real \(x,u\), gives
\[
\frac{e^{-(a+uR)}(a+uR)^n}{\Gamma(n+1)}
=\frac{e^{-(x-u)^2/2}}{\sqrt{2\pi}R}
\left[1+\frac{Q(x,u)}R+O(R^{-2})\right],
\quad Q(x,u)=\frac{u^3}{3}-\frac{xu^2}{2}+\frac{x^3}{6}-\frac x2.
\]
The expansion and its first two \(x\)-derivatives are uniform on compact sets. Integrating each term over a width-\(w\) interval centered at \(a+uR\), its odd displacement cancels. Accordingly, uniformly for \(x\) in compact sets,
\[
\lambda_n(a;d,w)=\frac{w}{\sqrt{2\pi}R}
\left[F_d(x)+R^{-1}H_d(x)+O_{d,w}(R^{-2})\right],
\]
where
\[
F_d(x)=e^{-(x-d)^2/2}+e^{-(x+d)^2/2},\quad
H_d(x)=\sum_{u=\pm d}e^{-(x-u)^2/2}Q(x,u).
\]
The remainder also admits bounded \(x\)-derivatives. Standard uniform Poisson large-deviation bounds for \(e^{-t}t^n/n!\), together with the positive lower bound obtained by taking \(n\) nearest \(a\), show that all maximizing indices satisfy \(|n-a|\le C_{d,w}R\). Hence all maximizers arise from the displayed compact-uniform expansion.

The stationary equation for \(F_d\) is \(x=d\tanh(dx)\). For \(d<1\) this has only \(x=0\), with strictly negative second derivative; the differentiated expansion and a lattice spacing of \(R^{-1}\) imply \(n_a=a+O_{d,w}(1)\). For \(d>1\), there are exactly three solutions \(0,\pm x_d\); the outer two are nondegenerate equal global maxima. At \(x=x_d\), using the stationary equation in the correction gives
\[
H_d(x_d)=\frac{x_d(x_d^2-d^2-3)}6 F_d(x_d)<0,
\qquad H_d(-x_d)=-H_d(x_d)>0.
\]
Consequently the lower peak exceeds the upper by a positive multiple of \(R^{-1}\) inside the brackets. Lattice discretization changes each peak by only \(O(R^{-2})\); hence every global maximizing index satisfies \((n_a-a)/R\to-x_d\). The same nondegenerate second derivative gives two separated local peaks.

At \(d=1\), \(F_1\) has a unique quartically flat maximum at zero. Taylor expansion gives
\[
F_1(x)=2e^{-1/2}-\frac{e^{-1/2}}6x^4+O(x^6),\quad
H_1(x)=-\frac{4e^{-1/2}}3x+O(x^3).
\]
The global comparison with \(x=0\) first implies every maximizing \(x=O(R^{-1/3})\), by the negative quartic and the linear perturbation (the \(O(R^{-2})\) remainder is smaller than \(R^{-4/3}\)). Substituting \(x=yR^{-1/3}\), the normalized difference from the central value, multiplied by \(R^{4/3}\), tends uniformly on bounded \(y\) to
\[
e^{-1/2}\left(-\frac{y^4}{6}-\frac{4y}{3}\right).
\]
This polynomial tends to negative infinity and has the unique maximizer \(y=-2^{1/3}\). The compactness argument and mesh spacing \(R^{-2/3}\) in \(y\) imply \((n_a-a)/a^{1/3}\to-2^{1/3}\), as claimed.

## Verification
The companion `verify.py` evaluates the actual incomplete-gamma integrals by Gauss–Legendre quadrature with logarithmically stabilized Poisson masses; it compares the selected mode with the three asymptotic predictions over several large \(a\), and independently checks the cubic-root coefficient extracted from the local polynomial. The analytic proof, not numerical fitting, establishes the limits.

## Relationship to prior work
Daubechies' classical theorem provides radial Gaussian localization diagonalization. Abreu–Dörfler (2012) discuss inverse geometry and radial annular symbols; Knutsen (2020) studies single-annulus norms and radial Cantor sets. The two equal rings here are separated by the natural Poisson fluctuation scale and produce a pitchfork threshold at \(d=1\). The leading equal-Gaussian-mixture bifurcation is standard; the additional spectral conclusion is its explicit symmetry-breaking correction and, critically, the \(a^{1/3}\) displacement with coefficient \(2^{1/3}\). No novelty is asserted for radial diagonalization or the Gaussian-mixture stationary equation.

## Limitations
The theorem covers fixed \(w,d>0\) and the Gaussian window only; it makes no uniform claim as \(d\to1\) jointly with \(a\), and does not establish finite-\(a\) uniqueness of maximizing integer indices. The precise second-order error or a full crossover function for varying \(d\) is not claimed. Possible implicit equivalents in asymptotic Poisson-mixture mode literature remain a publication-priority risk.

## References
1. I. Daubechies, *Time-frequency localization operators: a geometric phase space approach*, IEEE Trans. Inform. Theory **34** (1988), 605–612.
2. L. D. Abreu and M. Dörfler, *An Inverse Problem for Localization Operators*, arXiv:1202.5841, first submitted 2012-02-27.
3. H. Knutsen, *Daubechies’ Time–Frequency Localization Operator on Cantor Type Sets I*, J. Fourier Anal. Appl. **26** (2020), 47, DOI:10.1007/s00041-020-09751-9.
