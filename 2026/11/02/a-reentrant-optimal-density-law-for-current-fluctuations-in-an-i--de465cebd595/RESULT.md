# A reentrant optimal-density law for current fluctuations in an interacting active lattice gas

## Finding

The homogeneous interacting active lattice gas of Jose, Dandekar and Ramola has a **unique density maximizing its long-time integrated-current variance coefficient at every subcritical activity**. This maximizing density first moves below half filling, reaches an explicit minimum, then moves above half filling and approaches the motility-induced phase-separation spinodal.

More precisely, write \(p=\mathrm{Pe}^{2}\) for squared Péclet number and let \(\rho\in(0,1)\) be the uniform initial particle density. For \(0\le p<16\), define
\[
V(\rho,p)=\frac{\rho(1-\rho)[2+p(1-\rho)]}{\sqrt{\pi}\sqrt{2-p(1-\rho)(2\rho-1)}}.
\]
Under the homogeneous, zero-magnetization and quenched-initial-profile limit specified below, the published macroscopic-fluctuation theory gives \(\operatorname{Var}Q(T)=V(\rho,p)\sqrt T+O(1)\) as \(T\to\infty\), in its dimensionless units [1, Eq. (101)].

**Theorem.** For every \(p\in[0,16)\), the function \(\rho\mapsto V(\rho,p)\) has exactly one maximizer \(\rho_*(p)\in(0,1)\), and this is its only stationary point. The map \(p\mapsto\rho_*(p)\) is smooth, with:

1. \(\rho_*(0)=1/2\). It initially decreases, reaches its **unique global minimum**
\[
\rho_{\min}=\sqrt3-\frac54,\qquad
p_{\min}=\frac{64+48\sqrt3}{99},
\]
and thereafter increases strictly throughout \((p_{\min},16)\).
2. The exact half-filling crossover is
\[
\rho_*(p)<\frac12\quad(0<p<4),\qquad
\rho_*(4)=\frac12,\qquad
\frac12<\rho_*(p)<\frac34\quad(4<p<16).
\]
Thus the optimal density changes from below to above half filling at \(\mathrm{Pe}=2\), strictly before the bulk spinodal \(\mathrm{Pe}=4\).
3. As \(p\uparrow16\),
\[
\rho_*(p)=\frac34-\frac{16-p}{48}+O((16-p)^2),\qquad
V(\rho_*(p),p)\sim\frac{9\sqrt2}{4\sqrt\pi}\,(16-p)^{-1/2}.
\]
The maximizer at every fixed subcritical \(p\) is strictly interior and finite; the final divergence describes approaching, not crossing, the linearly unstable boundary.

## Assumptions and scope

The underlying model is the one-dimensional active exclusion lattice gas in [1, Section 2], not a generic active gas. Sites carry at most one particle, with internal right/left propulsion. In a system of length \(L\), there are symmetric exchanges at rate \(D>0\), exclusion-limited directed hops at rates proportional to \(\lambda/L\), and internal flips at rate \(\gamma/L^2\). Use the hydrodynamic and thermodynamic limits, spatially uniform quenched initial density \(\rho\), zero initial magnetization, and an effectively unbounded observation region as in [1, Section 8]. Set \(\mathrm{Pe}=\lambda/\sqrt{D\gamma}\). All constants and times in the displayed \(V\) use the dimensionless conventions of [1]; the physical-current coefficient acquires the positive rescaling stated in [1] and has the **same optimizing density** at fixed physical rates.

The function \(V\) is the coefficient of \(\sqrt T\) in the **macroscopic-fluctuation-theory current variance**, not an exact finite-lattice finite-time variance formula. The restriction \(0\le p<16\) ensures that every density \(\rho\in(0,1)\) is linearly stable, since \((1-\rho)(2\rho-1)\le1/8\). For \(p=16\), the density \(\rho=3/4\) is marginal, and the theorem makes no statement about a thermodynamic phase beyond that boundary.

## Proof

Write \(x=\rho\), \(A=x(1-x)[2+p(1-x)]\), and \(H=2-p(1-x)(2x-1)\). Since \(H>0\) for \(p<16\), the sign of the \(x\)-derivative of \(\sqrt\pi V=A/\sqrt H\) is the sign of \(N=2HA'-AH'\). Exact expansion gives
\[
\begin{aligned}
N(x,p)={}&8p^2x^4-23p^2x^3+24p^2x^2-11p^2x+2p^2\\
&-8px^3+30px^2-30px+8p-16x+8.
\end{aligned}
\]
In particular, \(N(0,p)=2(p+2)^2>0\), \(N(1,p)=-8<0\), and
\[
N(1/2,p)=\frac{p(p-4)}8,\qquad
N(3/4,p)=\frac{(p-16)(5p+16)}{64}.
\]

**Uniqueness for \(0\le p\le4\).** Substitute \(x=t/(1+t)\), \(t>0\). Then \((1+t)^4N\) is the polynomial
\[
2(p+2)^2-(p+2)(3p-8)t+3p(p-4)t^2-2(3p+8)t^3-8t^4.
\]
For every \(0\le p\le4\), its nonzero coefficient sequence has exactly one sign change, so Descartes' rule permits at most one positive root, counted with multiplicity. The endpoint signs give existence. Consequently the root is simple, the derivative is positive before it and negative after it, and the maximum is unique. The sign at half filling places the optimum below \(1/2\) for \(0<p<4\) and exactly at \(1/2\) for \(p=4\).

**Uniqueness for \(4<p<16\).** First, on \(0<x<1/2\), substitute \(x=t/[2(1+t)]\). The coefficients, from constant through fourth degree, of \((1+t)^4N\) are
\[
2(p+2)^2,\quad \frac{(p+2)(5p+24)}2,\quad
\frac{3(p^2+7p+16)}2,\quad \frac{5p^2+8p+64}{8},\quad
\frac{p(p-4)}8.
\]
All are positive; hence \(N>0\) on this interval. On \(3/4<x<1\), substitute \(x=(3/4+t)/(1+t)\). The coefficients become
\[
\frac{(p-16)(5p+16)}{64},\quad
\frac{15p^2-232p-1280}{64},\quad
\frac{3(p^2-22p-192)}{16},\quad
-\frac{3p+56}{2},\quad -8,
\]
all negative for \(4<p<16\). Thus \(N<0\) there.

Finally, on \(1/2<x<3/4\) set \(x=(1/2+3t/4)/(1+t)\). The coefficients of \((1+t)^3(-\partial_xN)\) are
\[
\frac{p^2+24p+64}{4},\quad 3(3p+16),\quad
\frac{3(3p^2+8p+256)}{16},\quad
\frac{5p^2-24p+256}{16}.
\]
All are strictly positive. (The last quadratic has negative discriminant and positive leading coefficient.) Therefore \(N\) strictly decreases across \((1/2,3/4)\). Its endpoint signs are opposite, proving exactly one zero there, with no others. This zero is simple and gives the unique global maximum. Combined with the preceding case, \(\rho_*(p)\) is smooth by the implicit-function theorem, including across \(p=4\).

**Reentrant turning point.** Differentiate \(N(\rho_*(p),p)=0\):
\[
\rho_*'(p)=-\frac{\partial_pN}{\partial_xN}.
\]
The resultant eliminating \(p\) from \(N=0\) and \(\partial_pN=0\) is exactly
\[
\operatorname{Res}_p(N,\partial_pN)
=-4x^2(x-1)^4(8x^2-7x+2)(16x^2+40x-23).
\]
The quadratic \(8x^2-7x+2\) has negative discriminant, while the only root of \(16x^2+40x-23\) in \((0,1)\) is \(x=\sqrt3-5/4\). Substituting this value into \(\partial_pN=0\) gives \(p=(64+48\sqrt3)/99\); direct substitution verifies \(N=0\). Since \(\rho_*'(0)=-1/32<0\) and \(\rho_*'(4)=1/88>0\), this is the sole stationary point of the optimizer curve and is its strict global minimum.

**Spinodal approach.** At the boundary point \((x,p)=(3/4,16)\), the polynomial satisfies \(N=0\), \(\partial_xN=-72\), \(\partial_pN=3/2\). The implicit-function theorem gives the stated expansion \(\rho_*(p)=3/4-(16-p)/48+O((16-p)^2)\). Moreover,
\[
H=\frac{16-p}{8}+2p(x-3/4)^2,
\]
while \(A\to9/8\) along the optimal branch. Hence the maximum prefactor has the asserted inverse-square-root divergence and constant.

## Verification

The standalone `verify.py` uses exact symbolic polynomial arithmetic to check the derivative identity, four interval transforms, resultant factorization, turning-point substitutions and spinodal derivatives. It also executes seven high-precision bisection and coefficient-normalization checks for representative squared activities. Run with `python verify.py` after installing `requirements.txt`. The analytic coefficient signs, Descartes argument and implicit-function steps above—not any finite grid—establish all-parameter uniqueness.

## Relationship to prior work

Jose, Dandekar and Ramola [1] derive the current-variance asymptotic prefactor, its density asymmetry and the crossover to enhanced active fluctuations; their Fig. 3 displays selected densities. Their equations (87), (98), (100), and (101) are the **inputs** here, not new results. The contribution is the complete global density-optimizer classification for the stable full-density interval, the reentrant turning point, the exact half-filling crossing at \(\mathrm{Pe}=2\), and the sharp approach to the spinodal.

Kourbane-Houssene et al. [2] obtain the underlying exact hydrodynamics and spinodal, and Agranov et al. [3,4] develop its fluctuating hydrodynamics and current large-deviation framework. Those results neither state the above density-optimizer classification for the infinite-line quenched current-variance coefficient nor directly compare all stable initial densities in that observable. Mukherjee et al. [5] study a different nonpolar hard-core lattice model and associated steady correlations; their different microscopic mobility does not imply this theorem. An unlocated general optimizer theorem or later analysis might subsume the present classification; no claim of definitive publication priority is made.

## Limitations

This is an exact optimization of the **published macroscopic-fluctuation-theory coefficient** within its stated validity regime, not a new microscopic derivation of macroscopic fluctuation theory or a uniform-in-activity finite-size estimate. Near \(p=16\), asymptotic times and system sizes needed to observe the hydrodynamic prefactor may become large; the divergence is not asserted at fixed finite size. Nothing is claimed for inhomogeneous initial conditions, nonzero magnetization, activity \(p\ge16\), or arbitrary active lattice gases. The identified optimizer is a mathematical variance-maximizer, not necessarily an experimentally optimal choice once noise measurement cost or finite-time effects are included.

## References

[1] S. Jose, R. Dandekar, and K. Ramola, *Current fluctuations in an interacting active lattice gas*, arXiv:2301.10680, first submitted 2023-01-25, Section 8, Eq. (101), Appendix B. https://arxiv.org/abs/2301.10680 and https://arxiv.org/html/2301.10680.

[2] M. Kourbane-Houssene, C. Erignoux, T. Bodineau, and J. Tailleur, *Exact Hydrodynamic Description of Active Lattice Gases*, arXiv:1801.08952 (2018). https://arxiv.org/abs/1801.08952.

[3] T. Agranov, S. Ro, Y. Kafri, and V. Lecomte, *Exact fluctuating hydrodynamics of active lattice gases—Typical fluctuations*, arXiv:2104.14650 (2021). https://arxiv.org/abs/2104.14650.

[4] T. Agranov, S. Ro, Y. Kafri, and V. Lecomte, *Macroscopic Fluctuation Theory and Current Fluctuations in Active Lattice Gases*, arXiv:2208.02124 (2022). https://arxiv.org/abs/2208.02124.

[5] R. Mukherjee, S. Saha, T. Sadhu, A. Dhar, and S. Sabhapandit, *Hydrodynamics of a hard-core non-polar active lattice gas*, arXiv:2405.19984 (2024). https://arxiv.org/abs/2405.19984.
