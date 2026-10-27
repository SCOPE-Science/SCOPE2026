# Five-zero bifurcations of the Zak transform of a positive two-exponential window

## Finding
Consider the nonnegative, even, exponentially decaying window
\[
g_c(t)=e^{-|t|}-c e^{-2|t|},\qquad 0\le c\le1,
\]
and its unit-scale Zak transform
\[
Z_c(x,\omega)=\sum_{k\in\mathbb Z}g_c(x-k)e^{2\pi i k\omega},\qquad (x,\omega)\in[0,1)^2.
\]
Let \(q=e^{-1}\) and define the three exact critical coefficients
\[
 c_A=\frac{1+q^2}{(1+q)^2},\quad
 c_B=\frac{1+q^2}{2\sqrt q(1+q)},\quad
 c_C=\frac{(1+q^2)^2}{\sqrt q(1+q)^3}.
\]
They satisfy \(1/2<c_A<c_B<c_C<1\), with approximations \(0.6067761335\), \(0.6842165232\), and \(0.8303325129\), respectively. The number of distinct zeros in the fundamental cell is exactly
\[
\begin{array}{c|ccccc}
 c &[0,c_A)&\{c_A\}&(c_A,c_B)&[c_B,c_C]&(c_C,1]\\
 \#Z_c^{-1}(0)&1&2&5&3&5.
\end{array}
\]
There is always a zero at \((1/2,1/2)\). All additional zeros have the following explicit descriptions, with equality conventions as stated.

Put \(D_j(v)=1-2q^j v+q^{2j}\) for \(j=1,2\), and
\[
 R_0(v)=\frac{D_2(v)}{(1+q^2)D_1(v)},\qquad
 R_{1/2}(v)=\frac{D_2(v)}{\sqrt q(1+q)D_1(v)}.
\]
For \(c>c_A\), there are exactly two seam zeros \((0,\omega_0)\) and \((0,1-\omega_0)\), where \(0<\omega_0<1/2\) is the unique solution of \(c=R_0(\cos(2\pi\omega_0))\). At \(c=c_A\) these coalesce at the one additional zero \((0,1/2)\).

For \(c_A<c<c_B\), there are also precisely two spatial zeros \((1/2-\delta,1/2)\) and \((1/2+\delta,1/2)\), where
\[
 \delta=\operatorname{arcosh}\!\left(\frac{1+q^2}{2c\sqrt q(1+q)}\right)\in(0,1/2).
\]
For \(c>c_C\), there are instead two additional frequency zeros \((1/2,\omega_1)\) and \((1/2,1-\omega_1)\), where \(0<\omega_1<1/2\) is the unique solution of \(c=R_{1/2}(\cos(2\pi\omega_1))\). At the endpoints \(c_B\) and \(c_C\), the associated extra pair has merged into the universal central zero and does not count as an additional distinct zero.

## Assumptions and scope
The Zak convention uses \(e^{2\pi i k\omega}\) with \(g_c(x-k)\). Points \(x=0\) and \(x=1\) represent the same quasi-periodic seam; only \(x=0\) belongs to the chosen half-open cell. The classifications count distinct real Zak zeros, not complex multiplicities. All displayed statements include \(c=0\) and \(c=1\). The kernel \(g_c\) is nonnegative because \(g_c(t)=e^{-|t|}(1-ce^{-|t|})\); it is not unimodal for \(c>1/2\) because its right derivative at zero is \(-1+2c>0\) and it eventually decreases.

## Proof
Write \(v=e^{-x}\), \(w=e^{-(1-x)}\), \(q=vw\) and \(\phi=2\pi\omega\). Geometric summation gives, for \(0\le x<1\),
\[
 Z_c=\frac{A_1+B_1e^{i\phi}}{D_1(\cos\phi)}
 -c\frac{A_2+B_2e^{i\phi}}{D_2(\cos\phi)},
\]
where
\[
 A_1=v(1-w^2),\quad B_1=w(1-v^2),\quad
 A_2=v^2(1-w^4),\quad B_2=w^2(1-v^4).
\]
All denominators are strictly positive for real \(\phi\). At \(\phi=0\), the series is strictly positive term by term, hence there are no zeros. At \(\phi=\pi\),
\[
 Z_c(x,1/2)=\frac{v-w}{1+q}-c\frac{v^2-w^2}{1+q^2}.
\]
Thus \(x=1/2\) is always a zero. At any other \(x\), the exact zero condition is
\[
 c=\frac{1+q^2}{(1+q)(v+w)}.
\]
Because \(v+w=2\sqrt q\cosh(x-1/2)\), this takes every value strictly between \(c_A\) and \(c_B\) twice in \((0,1)\), the value \(c_A\) only on the identified seam, and the value \(c_B\) only at the universal central zero. This proves the entire \(\phi=\pi\) branch.

Now suppose \(\sin\phi\ne0\). On the seam \(x=0\), both \(B_j=0\) and the equation becomes \(c=R_0(\cos\phi)\). For \(0<x<1\), the vanishing imaginary part forces \(B_1/D_1=cB_2/D_2\), and the vanishing real part then forces \(A_1/D_1=cA_2/D_2\). Consequently \(A_2/A_1=B_2/B_1\), or
\[
 v(1+w^2)=w(1+v^2),\qquad
 (v-w)(1-vw)=0.
\]
As \(vw=q<1\), necessarily \(x=1/2\). There the remaining equation becomes \(c=R_{1/2}(\cos\phi)\). There are no other possibilities.

For any fixed positive constant \(r\), the derivative of \(rD_2(z)/D_1(z)\) with respect to \(z\) has the strictly positive sign of \(2q(1-q)(1-q^3)\), since \(D_2(z)-qD_1(z)=(1-q)(1-q^3)\). Therefore \(R_0\) and \(R_{1/2}\) increase strictly in \(z\in[-1,1]\). Their relevant endpoint values are
\[
 R_0(-1)=c_A,\quad R_0(1)=\frac{(1+q)^2}{1+q^2}>1,
\]
and
\[
 R_{1/2}(-1)=c_C,\quad R_{1/2}(1)=\frac{1+q}{\sqrt q}>1.
\]
The root formulas and every endpoint count follow. The inequalities \(c_A<c_B<c_C<1\) follow by elementary algebra with \(q=e^{-1}\) (and may be checked using the displayed exact expressions). Thus the five claimed zero-count regimes are exhaustive.

## Verification
The standalone `check_zak_two_exponentials.py` compares geometric closed forms with direct sums over integer shifts, at 420 sampled triples, and evaluates predicted zeros in ten damping regimes. All computed transform residuals were below \(5\times10^{-13}\). The preceding algebra, rather than finite sampling, proves completeness for every real parameter.

## Relationship to prior work
Kloos (2014) and Kloos–Stöckler (2013) establish uniqueness of the Zak zero for totally positive windows; Janssen (2003) studies the one-zero phenomenon in an even-unimodal positive class. The present family is nonnegative but non-unimodal throughout all three transitions. For \(c>1/2\), its Fourier transform \(2/(1+\xi^2)-4c/(4+\xi^2)\) changes sign and so the window is not totally positive. Neither of the cited hypotheses covers the multi-zero regimes here. The source comparisons remain bounded: the archived Janssen full text was not accessible through the available publisher link.

## Limitations
This theorem classifies only the unit-scale Zak zeros of the stated two-exponential family, not all Gabor lattice frame sets, general exponential mixtures, complex Zak zeros, or quantitative lower frame bounds. A zero-count transition alone does not prove frame failure for an oversampled lattice. Literature coverage is bounded and independent mathematical audit has not been performed.

## References
- T. Kloos, *Zeros of the Zak transform of totally positive functions*, arXiv:1411.1539v1, publicly posted 6 November 2014, https://arxiv.org/abs/1411.1539 .
- T. Kloos and J. Stöckler, *Zak transforms and Gabor frames of totally positive functions and exponential B-splines*, arXiv:1311.7359v1, publicly posted 28 November 2013, https://arxiv.org/abs/1311.7359 .
- A. J. E. M. Janssen, *On generating tight Gabor frames at critical density*, J. Fourier Anal. Appl. 9 (2003), 175–214, https://doi.org/10.1007/s00041-003-0011-3 .
