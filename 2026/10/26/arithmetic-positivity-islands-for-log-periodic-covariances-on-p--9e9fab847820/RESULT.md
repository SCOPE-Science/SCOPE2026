# Arithmetic positivity islands for log-periodic covariances on p-adic integers

## Finding
Fix any prime \(p\), \(0<r<1\), \(0<a\le 1/2\), \(0\le\varepsilon\le1\), and \(0\le\theta\le\pi\). For \(G=\mathbb Z_p\), let \(v_p(0)=\infty\) and define the continuous real radial function
\[
 f(0)=1,\qquad f(x)=1-a r^{v_p(x)}[1+\varepsilon\cos(\theta v_p(x))]\quad(x\ne0).
\]
The translation-invariant kernel \(K(x,y)=f(x-y)\) is positive definite if and only if the following explicit amplitude criterion holds. Put
\[
 A=\frac{1-r}{1-r/p},\quad z=r e^{i\theta},\quad C=\frac{1-z}{1-z/p}.
\]
At \(\theta=0\), every allowed \(\varepsilon\) is admissible. For \(0<\theta\le\pi\), set \(\varepsilon_*(\theta)=A/M(\theta)\), where
\[
 M(\theta)=\begin{cases}
 |C|,&\theta/(2\pi)\notin\mathbb Q,\\
 |C|\cos\delta_v,&\theta/(2\pi)=u/v\text{ in lowest terms},\ v\ge2,
 \end{cases}
\]
with \(\delta_v=\min_{0\le j<v}\operatorname{dist}_{\mathbb S^1}(\arg C+2\pi j/v,\pi)\in[0,\pi/v]\). Then \(K\) is positive definite precisely when \(\varepsilon\le\varepsilon_*(\theta)\). This includes equality and applies in the stipulated range \(0\le\varepsilon\le1\); values of \(\varepsilon_*\) above one mean all allowed amplitudes are admissible.

The threshold has arithmetic upward jumps at rational angles whenever \(\delta_v>0\) and the amplitude cap does not conceal the jump. For example, at \(p=2\), \(r=3/5\) and \(\theta=2\pi/3\), the exact threshold is \(139/182\), compared with the limiting irrational-angle threshold \((4/7)/|C|\approx0.4812173928\). An explicit admissible covariance at \(a=1/2\), \(\varepsilon=7/10\) is nonmonotone across adjacent valuation shells: \(f_2=883/1000>f_3=2041/2500\). It therefore lies outside the elementary cone of nonnegative nested-ball mixtures although it remains positive definite.

## Assumptions and scope
\(\mathbb Z_p\) denotes the compact additive group of \(p\)-adic integers with normalized Haar measure. A nonzero element has valuation \(v_p(x)=k\in\{0,1,\ldots\}\) when \(x\in p^k\mathbb Z_p\setminus p^{k+1}\mathbb Z_p\). A character has conductor \(p^m\) if it is trivial on \(p^m\mathbb Z_p\) but not on \(p^{m-1}\mathbb Z_p\), for \(m\ge1\). Positive definiteness means all matrices \([f(x_i-x_j)]\) are Hermitian positive semidefinite for every finite set of points, with repetitions permitted. The parameters and angle range are exactly those stated above. The profile satisfies \(0\le f(x)\le1\), so positivity failure is not a two-point overshoot of the diagonal.

## Proof
Write \(f_k=1-a r^k(1+\varepsilon\cos(k\theta))\), so \(f_k\to1\). Uniformly on \(\mathbb Z_p\),
\[
 f=f_0+\sum_{j=1}^{\infty}(f_j-f_{j-1})\mathbf1_{p^j\mathbb Z_p}.
\]
The Fourier integral of \(\mathbf1_{p^j\mathbb Z_p}\) against a character of conductor \(p^m\) equals \(p^{-j}\) for \(j\ge m\) and zero otherwise. Therefore, since \(z=r e^{i\theta}\), for every \(m\ge1\),
\[
 \widehat f(m)=a p^{-m}r^{m-1}\left[\frac{1-r}{1-r/p}+\varepsilon\operatorname{Re}\left(\frac{1-z}{1-z/p}e^{i(m-1)\theta}\right)\right]. \tag{1}
\]
Here \(\widehat f(m)\) is the common Fourier coefficient at every character of conductor \(p^m\); this is an exact identity rather than an asymptotic. At the trivial character,
\[
 \widehat f(0)=1-a(1-p^{-1})\left[\frac1{1-r/p}+\varepsilon\operatorname{Re}\frac1{1-z/p}\right]>0,\tag{2}
\]
because \(f\ge0\) pointwise and is positive on infinitely many shells of positive measure. By Fourier--Bochner theory on compact abelian groups, \(K\) is positive definite exactly when every coefficient in (1) is nonnegative.

If \(\theta=0\), \(C=A>0\), and all (1) are strictly positive. For \(0<\theta\le\pi\), the real part of \(C\) is strictly positive, since it is proportional to \(1+r^2/p-r(1+1/p)\cos\theta>0\). Hence the circle orbit of \(C e^{ik\theta}\) has a negative real part at some \(k\ge0\). If \(\theta/(2\pi)\) is irrational, the orbit is dense on the circle, giving the infimum \(-|C|\). If it is \(u/v\) in lowest terms, the orbit consists of the \(v\) evenly spaced phases; its smallest real part is \(-|C|\cos\delta_v\). In this range \(M(\theta)>0\), including the order-two endpoint. Substitution into (1) proves the criterion, with equality allowed. Taking limits through irrational angles proves the rational resonance jumps when \(\delta_v>0\).

For the explicit nonmonotone example, exact algebra yields \(A=4/7\), \(C=(163-15i\sqrt3)/139\), and the three possible real values \(\operatorname{Re}(C e^{ik\theta})\) are \(163/139\), \(-59/139\), \(-104/139\). Thus \(M=104/139\), \(\varepsilon_*=139/182\), and at \(\varepsilon=7/10\) the minimum spectral bracket is \(232/4865>0\). Direct shell values are \(f_0=3/20\), \(f_1=161/200\), \(f_2=883/1000\), \(f_3=2041/2500\), with \(f_3-f_2=-333/5000\). Every positive nested-ball mixture would have nondecreasing values \(f_k\), proving the asserted separation.

## Verification
Run \(python3\) on the included \(verify.py\). This standard-library-only checker evaluates direct finite cyclic Fourier sums independently of the geometric-series formula for the periodic quotient in 108 instances, with maximum observed absolute error below \(6\cdot10^{-15}\). It also checks the exact rational resonance coefficients and a negative adjacent-shell difference. Finite tests support but do not replace the infinite-group proof above.

## Relationship to prior work
Kozyrev (2000) develops \(p\)-adic wavelet/Fourier-scale eigenfunctions and ball indicators; Bendikov--Grigor'yan--Pittet--Woess (2013) develop positive-weighted ball averaging and isotropic Markov semigroup spectra; Bendikov--Cygan--Woess (2016) analyze logarithmic-time oscillations of ultrametric heat kernels. Those structural tools motivate the valuation-shell decomposition. The present result instead classifies positivity of an explicitly modulated spatial covariance, including rational-angle threshold jumps and nonmonotone admissible shell values. The inspected claims do not state or imply that particular amplitude classification without a separate sign computation.

## Limitations
Only \(0<a\le1/2\), \(0\le\varepsilon\le1\), \(0<r<1\), and the compact group \(\mathbb Z_p\) are classified. The result neither classifies larger amplitudes nor other non-Archimedean groups. Spectral positivity is proved analytically; no independent mathematical audit has been conducted. Exhaustive novelty outside the inspected primary literature is not claimed.

## References
1. S. Kozyrev, *Wavelet analysis as a p-adic spectral analysis*, arXiv:math-ph/0012019, first public 2000-12-09; relevant sections 1--2.
2. A. Bendikov, A. Grigor'yan, C. Pittet and W. Woess, *Isotropic Markov semigroups on ultra-metric spaces*, arXiv:1304.6271, first public 2013-04-23; relevant sections 1--3.
3. A. Bendikov, W. Cygan and W. Woess, *Oscillating heat kernels on ultrametric spaces*, arXiv:1610.03292, first public 2016-10-11; relevant sections 1--3.
