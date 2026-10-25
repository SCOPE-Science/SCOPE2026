# A fourth-order arrow of time and lag-sign reversal in a harmonically filtered resetting Brownian bath

## Finding
Consider a stationary harmonic position coordinate driven by Brownian forcing that resets independently to zero at Poisson times. Although its stationary two-time *covariance* can be reproduced by a reversible Gaussian colored-noise model, the observed position trajectory is never time reversible. The first nonvanishing polynomial two-time witness has order four. Its sign near zero lag changes at an explicit forcing-reset/relaxation ratio, and throughout a nonempty interval the witness necessarily changes sign as the observation lag increases.

Precisely, for every reset rate \(\rho>0\), define
\[
A_\rho(t)=\mathbb E[X_0^3X_t]-\mathbb E[X_0X_t^3],\qquad t\geq0.
\]
Its unilateral Laplace transform, for \(p>0\), is
\[
\widehat A_\rho(p)=
\frac{24N_\rho(p)}{\rho(\rho+1)^2(\rho+2)(\rho+3)
(p+\rho)^2(p+1)(p+3)(p+\rho+1)(p+\rho+2)},
\]
with
\[
\begin{aligned}
N_\rho(p)={}&(6\rho^2-9\rho-9)p^2\\
&+(17\rho^3-\rho^2-45\rho-27)p\\
&+14\rho^4+23\rho^3-21\rho^2-42\rho-18.
\end{aligned}
\]
The first nonzero generic short-lag derivative is
\[
A_\rho'''(0^+)=
\frac{72(2\rho^2-3\rho-3)}{\rho(\rho+1)^2(\rho+2)(\rho+3)}.
\]
Writing \(\rho_*=(3+\sqrt{33})/4\), the asymmetry is negative for sufficiently small positive lags when \(0<\rho<\rho_*\), and positive for sufficiently small positive lags when \(\rho>\rho_*\). At the boundary, the cubic term disappears but
\[
A_{\rho_*}^{(4)}(0^+)=
\frac{12(7\rho_*+3)}{\rho_*(\rho_*+1)^2(\rho_*+2)}>0.
\]
Therefore \(A_\rho\) is nonzero for every \(\rho>0\), proving time irreversibility of the stationary position-only process.

The dominant large-lag terms are
\[
A_\rho(t)\sim
\begin{cases}
\displaystyle\frac{36}{\rho(\rho-3)(\rho+1)}\,t e^{-\rho t},&0<\rho<1,\\[5pt]
-4t e^{-t},&\rho=1,\\[5pt]
\displaystyle\frac{24(7\rho+3)}{\rho(\rho-1)(\rho+1)^2(\rho+2)(\rho+3)}e^{-t},&\rho>1.
\end{cases}
\]
In particular, **for every \(1<\rho<\rho_*\), the fourth-order time-order witness is negative at sufficiently short lag and positive at sufficiently large lag, and hence has at least one positive-lag zero**. No uniqueness of this zero is asserted.

## Assumptions and scope
Let \(W_t\) be a two-sided standard Brownian motion and let an independent rate-\(\rho\) stationary Poisson point process reset the forcing coordinate to zero. Between resets, for all times,
\[
dX_t=(-X_t+Y_t)\,dt,\qquad dY_t=\sqrt2\,dW_t;
\]
at a reset time, \(Y_t=0\) but \(X_t\) is continuous and unchanged. The rate \(\rho>0\) is fixed, the harmonic relaxation rate is one, and the forcing Brownian diffusivity is one. This is a time-and-amplitude normalization of the harmonically confined active particle driven by resetting Brownian noise in the cited physical model. The stationary forcing has covariance
\[\mathbb E[Y_0Y_t]=\frac2\rho e^{-\rho|t|}.\]
The unique stationary position is the exponentially stable past convolution
\[X_t=\int_{-\infty}^t e^{-(t-s)}Y_s\,ds.\]
All moments used here are finite: the forcing's backward reset age is exponentially distributed and the conditional Gaussian moments are polynomial in that age; exponential filtering controls the position moments. Finite-dimensional position laws are invariant under global sign reversal, so all odd-total-degree position moments vanish.

For dimensional parameters \(\mu>0\), forcing reset rate \(r>0\), thermal noise strength \(D>0\), and original position equation \(\dot x=-\mu x+r y\), the normalization is \(\rho=r/\mu\), rescaled time \(s=\mu t\), \(Y=\sqrt{\mu/D}\,y\), \(X=\mu^{3/2}x/(r\sqrt D)\). Statements refer to the stationary two-sided process, not a transient initialized at the reset state.

## Proof
**Stationarity and moments.** The Markov pair \((X,Y)\) has the polynomial generator
\[
\mathcal L(x^iy^j)=-(i+\rho\mathbf1_{j>0})x^iy^j
+i x^{i-1}y^{j+1}+j(j-1)x^iy^{j-2}
\]
for nonnegative integers \(i,j\), with zero-coefficient terms omitted. The unique stationary measure is supplied by stationary resetting Brownian forcing and the stable convolution above. The identity \(\mathbb E[\mathcal L(x^iy^j)]=0\) implies, writing \(m_{ij}=\mathbb E[X^iY^j]\),
\[
\begin{aligned}
m_{02}&=2/\rho, &m_{11}=m_{20}&=2/[\rho(\rho+1)],\\
m_{04}&=24/\rho^2,&m_{13}&=12(3\rho+2)/[\rho^2(\rho+1)^2],\\
m_{22}&=4(\rho^2+19\rho+12)/[\rho^2(\rho+1)^2(\rho+2)],\\
m_{31}=m_{40}&=12(\rho^2+19\rho+12)/[\rho^2(\rho+1)^2(\rho+2)(\rho+3)].
\end{aligned}
\]
This lists the complete mixed moments necessary to reconstruct the claim; the stationary fourth position moment itself is already available in the motivating source and is not offered as new.

**Two semigroup evaluations.** The conditional first moment is
\[
\mathbb E[X_t\mid X_0,Y_0]
=e^{-t}X_0+Y_0\frac{e^{-\rho t}-e^{-t}}{1-\rho}
\]
for \(\rho\ne1\), continuously extended to the term \(t e^{-t}Y_0\) at \(\rho=1\). Consequently,
\[
\mathcal L_t\{\mathbb E[X_0^3X_t]\}(p)
=\frac{m_{40}}{p+1}+\frac{m_{31}}{(p+1)(p+\rho)}.
\]
For the cubic conditional moment, order the polynomial basis as
\((x^3,x^2y,xy^2,y^3,x,y)\). The generator on this basis is the matrix
\[
B=\begin{pmatrix}
-3&3&0&0&0&0\\
0&-\rho-2&2&0&0&0\\
0&0&-\rho-1&1&2&0\\
0&0&0&-\rho&0&6\\
0&0&0&0&-1&1\\
0&0&0&0&0&-\rho
\end{pmatrix}.
\]
With \(v=(m_{40},m_{31},m_{22},m_{13},m_{20},m_{11})^\top\), the second ordered moment has transform
\[
\mathcal L_t\{\mathbb E[X_0X_t^3]\}(p)
=e_1^\top(pI-B)^{-1}v.
\]
Subtracting, using the explicit stationary moments, and rationally simplifying gives \(\widehat A_\rho(p)\) in the Finding. This exact generator/resolvent identity also establishes every stated boundary without relying on numerical fitting.

**Short-lag signs.** Repeated action of the degree-one and degree-three polynomial generators yields \(A_\rho(0)=A_\rho'(0^+)=A_\rho''(0^+)=0\) and the displayed third derivative. The unique positive root of \(2\rho^2-3\rho-3=0\) is \(\rho_*\). At this root the independently evaluated fourth derivative is the strictly positive expression displayed above. Taylor expansion of the finite-dimensional polynomial semigroup justifies the short-lag sign conclusions for each fixed positive rate.

**Long-lag signs and crossing.** When \(0<\rho<1\), the slowest pole of the transform is a double pole at \(p=-\rho\), whose coefficient is \(36/[\rho(\rho-3)(\rho+1)]<0\). When \(\rho>1\), the slowest pole is simple at \(p=-1\), with positive residue \(24(7\rho+3)/[\rho(\rho-1)(\rho+1)^2(\rho+2)(\rho+3)]\). At \(\rho=1\), direct partial fractions give
\[
\widehat A_1(p)=\frac{7}{2(p+3)}+\frac1{(p+3)^2}-\frac{10}{p+2}+\frac{13}{2(p+1)}-\frac4{(p+1)^2},
\]
so the leading term is \(-4te^{-t}\). Since each \(A_\rho(t)\) is continuous in \(t\), the opposing short- and long-lag signs when \(1<\rho<\rho_*\) imply the existence of at least one positive-lag sign reversal.

**Why fourth order is the first witness.** All odd-total-degree joint moments of \(X\) vanish by forcing sign symmetry. A stationary real scalar process has symmetric two-time covariance, \(\mathbb E[X_0X_t]=\mathbb E[X_0X_{-t}]\), purely by covariance symmetry and stationarity. For total polynomial degree at most three there is therefore no nonzero two-time ordering difference. Nonzero \(A_\rho(t)\) is incompatible with time reversal of the stationary observed position process.

## Verification
The standalone `check.py` supplied alongside this result reconstructs the stationary moment balances, cubic generator, rational resolvent, low-lag derivatives, critical rate, leading long-lag residues, and the pole-coalescence case at \(\rho=1\). It compares independently evaluated matrix-exponential semigroup values to high-precision numerical inverse Laplace transforms at 35 parameter/lag points and separately checks stationary second/fourth moments against last-reset Gaussian-mixture sampling. Run with Python 3 and `sympy`, `numpy`, `scipy`, and `mpmath` installed: `python check.py`. The checked run reported `PASS 75 checks`. The proof is exact; finite sampling and numerical evaluations supply additional consistency checks only.

## Relationship to prior work
Guéneau, Majumdar, and Schehr's 2023 study gives this resetting Brownian forcing model, its stationary distribution and even stationary moments, and its two-time covariance; those are pre-existing results. In particular, the fourth *one-time* position moment and the equality of second-order covariance with the standard Ornstein–Uhlenbeck colored-force comparator are not presented as discoveries here. A scalar stationary Gaussian process with that covariance is time reversible, while the present nonlinear resetting process has the nonzero fourth-order antisymmetric temporal statistic calculated above. General treatments of active-matter irreversibility and a Lévy-driven parabolic-trap arrow-of-time study motivate higher-order diagnostics but have different forcing laws and do not supply the displayed finite-moment two-time rational transform. The claim is specifically the exact position-only fourth-order time-asymmetry law and its lag-sign reversal, not an independent new stationary density.

## Limitations
The model has linear harmonic filtering and instantaneous complete resets of the forcing, not position resets, thermal diffusion, nonlinear trapping, non-Poisson resetting or arbitrary driving. Stationarity and finite positive \(\rho\) are essential. The result proves at least one lag zero only for \(1<\rho<\rho_*\); it does not classify every zero, establish uniqueness, compute entropy production, or quantify finite-sample detection power. The exact model and covariance comparison are established literature. Broader polynomial-process or time-series theory may provide other representations or imply parts of the result; scholarly priority is not independently certified.

## References
1. M. Guéneau, S. N. Majumdar, and G. Schehr, *Active particle in a harmonic trap driven by a resetting noise*, arXiv:2306.09453, first public June 15, 2023. https://arxiv.org/abs/2306.09453
2. L. Dabelow and A. Eichhorn, *Irreversibility in Active Matter: General Framework for Active Ornstein–Uhlenbeck Particles*, Frontiers in Physics (2021), DOI: 10.3389/fphy.2020.582992. https://doi.org/10.3389/fphy.2020.582992
3. S. Yuvan and M. Bier, *Breaking of time-reversal symmetry for a particle in a parabolic potential that is subjected to Lévy noise*, Physical Review E 104, 014119 (2021), DOI: 10.1103/PhysRevE.104.014119. https://doi.org/10.1103/PhysRevE.104.014119
