# Finite-column erasure robustness for Poisson Gabor frames at half-frequency sampling

## Finding
For every real \(w>0\) and every **finite** set \(F\subset\mathbb Z\), let
\[
 g_w(x)=\frac{1}{x^2+w^2},\qquad
 \mathcal G_{w,F}=\{e^{\pi imx}g_w(x-k):m\in\mathbb Z,\ k\in\mathbb Z\setminus F\}.
\]
Then \(\mathcal G_{w,F}\) is a frame for \(L^2(\mathbb R)\). In particular, there are constants \(0<A(w,F)\le B(w,F)<\infty\) such that, for every \(f\in L^2(\mathbb R)\),
\[
 A(w,F)\|f\|_2^2\le
 \sum_{k\in\mathbb Z\setminus F}\sum_{m\in\mathbb Z}
 \left|\int_{\mathbb R}f(x)e^{-\pi imx}g_w(x-k)\,dx\right|^2
 \le B(w,F)\|f\|_2^2.
\]
The removal of a finite number of entire translation columns, each containing infinitely many modulations, does not destroy the frame. This is a result about **one specific oversampling ratio** and the Poisson window, not a general finite-erasure theorem for arbitrary windows.

There is a contrasting one-sided obstruction: when the allowed translations are \(k\le0\), the same system has no positive lower frame bound for any \(w>0\). Hence finite-column robustness does not extend to an unrestricted infinite deletion statement.

## Assumptions and scope
We use the Fourier modulation convention \(M_{m/2}g(x)=e^{\pi imx}g(x)\), integer translations \(T_kg(x)=g(x-k)\), and unnormalized Lebesgue \(L^2\) norm. There is no assumption that \(F\) is contiguous or centered. Its size is arbitrary but finite. The frame bounds may depend on both \(w\) and the precise locations of \(F\); they are not asserted to have a uniform positive lower bound over all finite \(F\).

For \(t\in[0,2]\), write \(u_j=f(t+2j)\). The map \(f\mapsto\{u_j(t)\}_{j\in\mathbb Z}\) is the standard isometric decomposition into \(L^2([0,2];\ell^2(\mathbb Z))\). Put
\[
 a_{t,j}=g_w(t-2j),\qquad b_{t,j}=g_w(t-1-2j).
\]
Both are uniformly \(\ell^1\) sequences as \(t\) ranges over \([0,2]\), so their convolution maps vary continuously in operator norm.

## Proof
**1. Fiber frame identity.** The frequency exponentials \(e^{\pi imx}/\sqrt2\), restricted to an interval of length two, form an orthonormal basis. Periodizing the product \(fg_w(\cdot-k)\) over this interval and applying Parseval gives
\[
 \sum_{m\in\mathbb Z}|\langle f,M_{m/2}T_kg_w\rangle|^2
 =2\int_0^2\left|\sum_{j\in\mathbb Z}f(t+2j)g_w(t+2j-k)\right|^2dt.
\]
For \(k=2\ell\), the inner output is a convolution of \(u\) with \(a_t\); for \(k=2\ell+1\), it is a convolution with \(b_t\). Each deletion \(k\in F\) removes one coefficient from exactly one of these two convolution outputs. Consequently the frame inequality is equivalent to uniform lower and upper bounds for the two-channel coefficient-erased convolution operator on \(\ell^2(\mathbb Z)\), for almost every \(t\in[0,2]\).

**2. The two complete channels have no common Fourier zero.** Define their continuous trigonometric symbols by
\[
 A_t(\theta)=\sum_{j\in\mathbb Z}\frac{e^{ij\theta}}{(t-2j)^2+w^2},
 \qquad A_{t-1}(\theta)=\sum_{j\in\mathbb Z}\frac{e^{ij\theta}}{(t-1-2j)^2+w^2}.
\]
The Poisson-kernel Fourier integral is \(\int_{\mathbb R}(x^2+w^2)^{-1}e^{-i\xi x}\,dx=(\pi/w)e^{-w|\xi|}\). Apply Poisson summation with spacing two, split the dual sum at zero, and sum the two geometric series. For \(0<\theta<2\pi\), put \(r=e^{-\pi w}\), \(z=e^{i\pi t}\), and
\[
 a=\frac1{1-rz},\quad b=\frac r{z-r},\qquad
 a'=\frac1{1+rz},\quad b'=-\frac r{z+r}.
\]
The resulting exact symbols are
\[
 A_t(\theta)=\frac\pi{2w}e^{it\theta/2}
  (ae^{-w\theta/2}+be^{w\theta/2}),
\]
\[
 A_{t-1}(\theta)=\frac\pi{2w}e^{i(t-1)\theta/2}
  (a'e^{-w\theta/2}+b'e^{w\theta/2}).
\]
Their coefficient determinant is
\[
 ab'-a'b=
 -\frac{2rz(1-r^2)}{(1-rz)(1+rz)(z-r)(z+r)}\ne0
\]
for every \(t\in\mathbb R\) and \(w>0\), since \(|z|=1\) and \(0<r<1\). Therefore the symbols cannot vanish simultaneously on the open interval; continuity covers its endpoints. The two-channel complete convolution operator has lower Fourier multiplier \(|A_t|^2+|A_{t-1}|^2>0\). Compactness of \([0,2]\times[0,2\pi]\) yields a positive uniform minimum. The corresponding complete frame operator \(S_t\) on \(\ell^2\) is bounded and invertible for all \(t\in[0,2]\).

**3. Nonrationality of the channel ratio.** For any fixed \(t\) and \(w>0\), on any open subinterval where the denominator is nonzero,
\[
 \frac{A_t(\theta)}{A_{t-1}(\theta)}
 =e^{i\theta/2}\frac{a+b e^{w\theta}}{a'+b'e^{w\theta}}.
\]
This function **cannot** agree on an open interval with any rational function \(R(e^{i\theta})\) of the unit-circle variable. Indeed both are meromorphic in the complex \(\theta\)-plane, and agreement on an interval would imply a meromorphic identity by the identity theorem. Thus the displayed right side would be \(2\pi\)-periodic. But shifting \(\theta\) by \(2\pi\) negates the factor \(e^{i\theta/2}\) and multiplies \(X=e^{w\theta}\) by \(q=e^{2\pi w}\). Periodicity would require the polynomial identity
\[
 -(a+bqX)(a'+b'X)=(a+bX)(a'+b'qX).
\]
Its constant term forces \(-aa'=aa'\), impossible because \(a\) and \(a'\) are nonzero. This argument also covers cases where an individual channel symbol has isolated zeros.

**4. A finite set of erased columns cannot create a fiber kernel.** Let \(E_{t,F}\) retain exactly the finitely many scalar output coefficients whose translation indices belong to \(F\). The erased fiber frame operator is
\[
 S_{t,F}=S_t-E_{t,F}^*E_{t,F}.
\]
It is a positive finite-rank perturbation of an invertible self-adjoint operator, hence Fredholm of index zero. Suppose \(u\in\ker S_{t,F}\) is nonzero. All but finitely many outputs in each convolution channel vanish. Taking the \(\ell^2\) Fourier transform of \(u\) gives, almost everywhere on the unit circle,
\[
 A_t(\theta)U(\theta)=P(e^{i\theta}),\qquad
 A_{t-1}(\theta)U(\theta)=Q(e^{i\theta}),
\]
where \(P,Q\) are Laurent polynomials (finite supports determined by \(F\)). Neither is identically zero, because each analytic channel symbol is nonzero almost everywhere and \(U\ne0\). Dividing shows that \(A_t/A_{t-1}=P/Q\) wherever defined, contradicting Step 3. Thus \(\ker S_{t,F}=\{0\}\). Fredholmness yields bounded invertibility of each \(S_{t,F}\).

The maps \(t\mapsto S_{t,F}\) are norm-continuous on the compact interval \([0,2]\): this follows from uniform absolute convergence of the sampled kernel sequences and the finite-rank form of the erasures. Hence the individual positive spectral lower bounds admit a common positive minimum, and upper bounds are uniformly finite. Integration in Step 1 proves the announced frame inequalities for all \(f\in L^2(\mathbb R)\).

**5. One-sided deletion counterexample.** Keep only translations \(k\le0\). For an integer \(R\ge2\), let \(f_R=\mathbf1_{[R,R+1]}\), so \(\|f_R\|_2=1\). Parseval for the same modulation lattice yields
\[
 \sum_{k\le0}\sum_{m\in\mathbb Z}
 |\langle f_R,M_{m/2}T_kg_w\rangle|^2
 =2\sum_{k\le0}\int_R^{R+1}g_w(x-k)^2\,dx
 \le2\sum_{n\ge R}\frac1{n^4}=O(R^{-3}).
\]
The sum tends to zero, so no positive lower frame bound exists for the half-line translation set.

## Verification
The independent standalone script `CHECK.py` uses only Python's standard library and checks the rational determinant identity at exact fractions, the sampled Poisson-summation formula against directly truncated Fourier series, and the half-line energy decay bound. Invoke `python3 CHECK.py`; it prints `CHECK_OK assertions=67` on completion. Direct Fourier-series comparisons use \(12001\) terms and an absolute tolerance \(3\cdot10^{-8}\). The script is a finite consistency check, **not** a substitute for the analytic nonrationality and Fredholm arguments, which establish the result for all \(w>0\), all finite \(F\), and all \(f\in L^2\).

## Relationship to prior work
Belov and Semenov (2026) provide a general criterion for the Poisson kernel with an irregular **modulation** set and regular translations, and explicitly distinguish the unclassified reverse orientation. The present result establishes finite-translation-hole robustness in one reverse-orientation family. The complete lattice frame property at density two is classical; its use in Step 2 is only the starting point. Gröchenig and Koppensteiner (2018) explain the standard lattice and fiber criteria, but their lattice characterizations alone do not ensure robustness after infinitely many atoms arranged in complete modulation columns are deleted. Belov, Kulikov and Lyubarskii (2021) treat a single complex Cauchy kernel and different sampling criteria; their theorem does not directly apply to the symmetric real Poisson kernel. The scope of the contribution is the nonrational-transfer obstruction and resulting uniform finite-column-erasure theorem, not general excess or generic finite-point erasures.

## Limitations
No explicit best numerical frame bounds are computed. Lower bounds can deteriorate severely as \(F\) grows; finite-column robustness should not be interpreted as uniform robustness over all finite deletions. The theorem covers the frequency spacing \(1/2\), translation spacing \(1\), the Poisson window, and no arbitrary perturbations of the surviving time-frequency nodes. It does not provide a general criterion for all irregular translation sets, and does not determine whether particular infinite sets other than the half-line counterexample retain a frame.

## References
1. Y. Belov and A. V. Semenov, *Irregular Gabor Frames for the Poisson Kernel*, arXiv:2610.30037v1 (first submitted 21 October 2026), https://arxiv.org/abs/2610.30037 .
2. K. Gröchenig and S. Koppensteiner, *Gabor Frames: Characterizations and Coarse Structure*, arXiv:1803.05271v1 (2018), https://arxiv.org/abs/1803.05271 .
3. Y. Belov, A. Kulikov and Y. Lyubarskii, *Irregular Gabor frames of Cauchy kernels*, arXiv:2104.01121v1 (2021), https://arxiv.org/abs/2104.01121 .
4. R. Balan, P. G. Casazza, C. Heil and Z. Landau, *Excesses of Gabor frames*, Applied and Computational Harmonic Analysis 14 (2003), 87–106, DOI:10.1016/S1063-5203(03)00006-X.
