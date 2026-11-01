# Exact critical Gabor phase diagram for a half-frequency exponential sideband

## Finding

Let \(\lambda>0\), \(c>0\), \(r=e^{-\lambda}\), and
\[
g_{\lambda,c}(t)=e^{-\lambda t}(1+c e^{\pi i t})\mathbf 1_{[0,\infty)}(t).
\]
For the critical lattice \(\mathbb Z\times\mathbb Z\), let \(A_{\lambda,c}\) and \(B_{\lambda,c}\) be the optimal squared Gabor frame bounds (the lower bound is defined to be zero for a nonframe). Set
\[
c_-={1-r\over1+r},\qquad c_+={1+r\over1-r}.
\]
Then the complete sharp bounds are
\[
A_{\lambda,c}=r^2\begin{cases}
\left({1\over1+r}-{c\over1-r}\right)^2,&0<c<c_-,\\
0,&c_-\le c\le c_+,\\
\left({c\over1+r}-{1\over1-r}\right)^2,&c>c_+,
\end{cases}
\]
and
\[
B_{\lambda,c}=\begin{cases}
\left({1\over1-r}+{c\over1+r}\right)^2,&0<c\le1,\\
\left({1\over1+r}+{c\over1-r}\right)^2,&c\ge1.
\end{cases}
\]
In particular this Gabor system is a Riesz basis (equivalently a frame at critical density) precisely for \(0<c<c_-\) or \(c>c_+\). Each of the two summand windows separately generates a critical-density Riesz basis, whereas their positive-amplitude superposition fails throughout the entire closed interval \([c_-,c_+]\).

For \(c_-<c<c_+\), the Zak transform has exactly one zero in \((0,1)\times[0,1)\). Write
\[
u={ (c^2-1)(1+r^2)\over2r(c^2+1)},\quad
\omega_0={\arccos u\over2\pi},\quad
x_0=1-{1\over\pi}\arctan\left({2r\sqrt{1-u^2}\over1-r^2}\right).
\]
Then the unique zero is \((x_0,\omega_0)\). At \(c=c_-\) or \(c=c_+\), the zero reaches the excluded edge \(x\uparrow1\), causing the lower bound to vanish. The lower frame bound turns on *exactly quadratically* on each frame side:
\[
A_{\lambda,c}={r^2\over(1-r)^2}(c_--c)^2\quad(0<c<c_-),\qquad
A_{\lambda,c}={r^2\over(1+r)^2}(c-c_+)^2\quad(c>c_+).
\]
Moreover the spectral set of the frame operator, including in the nonframe regime, is exactly \([A_{\lambda,c},B_{\lambda,c}]\) and the operator has no eigenvalues. In both frame regions its condition number strictly exceeds \(((1+r)/(r(1-r)))^2\), which is approached only as \(c\downarrow0\) or \(c\to\infty\).

## Assumptions and scope

All assertions concern \(\lambda,c\in(0,\infty)\), the unnormalized complex window above, the unnormalized modulation \(M_m f(t)=e^{2\pi i m t}f(t)\), translation \(T_n f(t)=f(t-n)\), and the lattice \(m,n\in\mathbb Z\). Values at isolated jump points are immaterial in \(L^2\). The Zak transform is \(Zf(x,\omega)=\sum_{k\in\mathbb Z} f(x+k)e^{-2\pi i k\omega}\). Both coordinates of its fundamental domain have unit Lebesgue measure. The sharp bounds are essential infimum and supremum of \(|Zg|^2\).

## Proof

**1. Exact scalar fiber.** For \(0\le x<1\), with \(z=e^{-2\pi i\omega}\) and \(t=e^{\pi i x}\), the geometric series yield
\[
Zg(x,\omega)=r^x\left({1\over1-rz}+{ct\over1+rz}\right).
\]
Write \(a(z)=(1-rz)^{-1}\), \(b(z)=(1+rz)^{-1}\), and \(u=\Re z\). Thus \(|a(z)|=(1+r^2-2ru)^{-1/2}\), \(|b(z)|=(1+r^2+2ru)^{-1/2}\).

**2. Sharp maximum.** By the triangle inequality and \(r^x\le1\),
\[
|Zg(x,\omega)|\le(1+r^2-2ru)^{-1/2}+c(1+r^2+2ru)^{-1/2}=:H(u).
\]
Since \(H''(u)=3r^2[(1+r^2-2ru)^{-5/2}+c(1+r^2+2ru)^{-5/2}]>0\), the maximum on \([-1,1]\) is at an endpoint. At \(x=0\) and \(z=\pm1\), the summands are positive real, so the upper bound is attained. Comparing endpoint expressions gives the displayed formula for \(B_{\lambda,c}\).

**3. Sharp minimum outside the transition interval.** The ratio \(|a(z)|/|b(z)|=\sqrt{(1+r^2+2ru)/(1+r^2-2ru)}\) increases strictly with \(u\) and ranges precisely over \([c_-,c_+]\). If \(c<c_-\), the reverse triangle inequality yields
\[
|Zg|\ge r^x(|a|-c|b|)\ge r\big((1+r)^{-1}-c(1-r)^{-1}\big),
\]
because \(|a|-c|b|\) is strictly increasing with \(u\), hence minimal at \(u=-1\). Equality is approached as \(x\uparrow1\) and \(z=-1\), since \(t\to-1\). If \(c>c_+\), the reverse triangle inequality instead gives \(|Zg|\ge r^x(c|b|-|a|)\); the bracket is strictly decreasing with \(u\), is minimized at \(u=1\), and equality is approached as \(x\uparrow1,z=1\). Squaring gives both positive formulas for \(A_{\lambda,c}\).

**4. Zero set in the intermediate regime.** The equation \(Zg=0\) is \(t=-a(z)/(c b(z))=-(1+rz)/(c(1-rz))\). It requires \(c=|a(z)|/|b(z)|\), so for \(c_-<c<c_+\) exactly one \(u\in(-1,1)\) is possible, namely the formula displayed above. Furthermore
\[
{1+rz\over1-rz}={1-r^2+2ir\Im z\over|1-rz|^2}.
\]
As \(t=e^{\pi i x}\) traverses the *upper* semicircle, only the solution with \(\Im z<0\) is admissible. Its argument gives the stated unique \(\omega_0\in(0,1/2)\) and \(x_0\in(1/2,1)\). At \(c=c_\pm\) the only possible \(z\) is real and \(t=-1\), attainable solely as \(x\uparrow1\), proving essential lower bound zero there. This also proves all frame/nonframe assertions via the unitary critical Zak transform.

**5. Spectral and conditioning assertions.** On the open connected fundamental cylinder, \(|Zg|^2\) is continuous and nonconstant real analytic; its essential range is the full interval between the computed infimum and supremum. Each level set of a nonconstant real-analytic function has planar Lebesgue measure zero, so the multiplication operator has no eigenvalues. For \(0<c<c_-\), the positive square-root bound ratio is \(((1-r)^{-1}+c(1+r)^{-1})/[r((1+r)^{-1}-c(1-r)^{-1})]\), strictly increasing in \(c\); for \(c>c_+\) it is \(((1+r)^{-1}+c(1-r)^{-1})/[r(c(1+r)^{-1}-(1-r)^{-1})]\), strictly decreasing in \(c\). Their respective limits at \(0\) and infinity coincide at \((1+r)/(r(1-r))\). Squaring proves the strict conditioning penalty.

## Verification

The included standalone script `verify_sideband.py` checks the geometric-series Zak identity independently against truncated shift sums, verifies the endpoint extrema and the inequality against a dense finite grid for several distinct parameter regimes, and evaluates the explicit interior zero. It reports 672 passed supplementary assertions. These are diagnostics only: the universal quantifiers and equality cases follow from the inequalities and zero argument above, not from a finite grid.

## Relationship to prior work

Faulhuber and Shafkulovska, *Gabor frame bound optimizations* (arXiv:2204.02917, first public April 6, 2022), study sharp rectangular Gabor frame bounds of several standard exponential windows; their section 2.3 and section 7 cover the unmixed one-sided exponential. The present fixed-unit-lattice theorem instead treats coherent half-integer modulation interference, a whole nonframe coefficient interval, its moving unique Zak zero, and both exact bounds for every coefficient. The single-window statement does not imply the result for the sum. Classical critical Zak diagonalization is a prerequisite, not a novelty claim. Kloos and Stöckler, *Zak transforms and Gabor frames of totally positive functions and exponential B-splines* (arXiv:1311.7359), analyze zeros of totally positive and spline windows; the oscillating complex sideband family does not belong to those real total-positivity classes. No published source found in the checks performed established an equivalent complete two-sideband phase diagram. This is not a proof of historical priority.

## Limitations

The result applies to positive real sideband amplitudes, exactly half an integer modulation shift, and the critical *unit* lattice; it does not classify other relative phases, arbitrary detunings, irrational lattices, or multitone combinations. The analytical proof is complete under these assumptions, but independent mathematical review has not been performed. Historical priority could still be affected by an overlooked equivalent modulation-mixture or generic Zak-symbol theorem.

## References

1. M. Faulhuber and I. Shafkulovska, *Gabor frame bound optimizations*, arXiv:2204.02917 (first submitted 2022-04-06), https://arxiv.org/abs/2204.02917 ; open full text https://www.researchgate.net/publication/372319875_Gabor_frame_bound_optimizations .
2. T. Kloos and J. Stöckler, *Zak transforms and Gabor frames of totally positive functions and exponential B-splines*, arXiv:1311.7359 (2013), https://arxiv.org/abs/1311.7359 .
3. A. J. E. M. Janssen, *On generating tight Gabor frames at critical density*, J. Fourier Anal. Appl. 9 (2003), 175–214, https://doi.org/10.1007/s00041-003-0011-3 .
