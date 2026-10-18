# Exact integer-jet Parseval formulas for cubic and quartic cardinal splines

## Finding

Let \(B_n=\mathbf 1_{[0,1]}^{*(n+1)}\) be the normalized cardinal B-spline of degree \(n\), with \(n\in\{3,4\}\), and let \(f(x)=\sum_{j\in\mathbb Z}c_jB_n(x-j)\) for arbitrary \(c\in\ell^2(\mathbb Z)\). Then the knot evaluations of the first \(n\) jets form an **exact diagonal Parseval coefficient frame**:
\[
 \sum_{j\in\mathbb Z}|c_j|^2=\sum_{k\in\mathbb Z}\sum_{r=0}^{n-1}w_{n,r}|f^{(r)}(k)|^2.
\]
The complete weights, in ascending derivative order, are
\[
 (w_{3,0},w_{3,1},w_{3,2})=\left(1,\frac13,\frac1{18}\right),\qquad
 (w_{4,0},w_{4,1},w_{4,2},w_{4,3})=\left(1,\frac5{12},\frac{13}{144},\frac{11}{864}\right).
\]
They are the **unique** real constant diagonal weights satisfying this isometry with the displayed unit normalization. In particular, every listed derivative order is necessary for such a diagonal tight identity, even if arbitrary nonnegative weights are allowed on a proper subset.

There is an exact **finite-stencil reconstruction** of the underlying B-spline control coefficients from those physical knot jets:
\[
 c_j=\sum_{r=0}^{n-1}w_{n,r}\sum_{k\in\mathbb Z}f^{(r)}(k)B_n^{(r)}(k-j),\qquad j\in\mathbb Z.
\]
Each inner sum involves at most \(n\) nonzero terms. This is the adjoint reconstruction of an isometric coefficient-analysis operator, and hence has operator norm one for the corresponding weighted sample norm.

For the cubic spline, **value and first-derivative knot samples alone cannot beat squared frame condition number \(9\)** under any nonnegative diagonal weighting: their Fourier symbol has energy \(1\) at zero frequency and \(1/9\) at Nyquist after normalizing the value-channel weight to one, while the first-derivative channel vanishes at both endpoints. Value samples alone attain condition number \(9\). The curvature channel restores exact tightness with weight \(1/18\).

## Assumptions and scope

The spline \(B_n\) is the convolution of \(n+1\) unit-interval indicator functions, supported on \([0,n+1]\), rather than a centered or \(L^2\)-normalized variant. The derivative order satisfies \(0\le r\le n-1\), so derivatives are continuous at integer knots. Samples run over every integer without endpoint truncation. The norm on the spline space is **the \(\ell^2\) norm of its unique B-spline control coefficients**, not the ambient \(L^2(\mathbb R)\) norm of the function. Complex coefficient sequences are permitted. No claims are made for nonuniform knots, off-diagonal sample weights, different lattice phases, or degrees other than three and four.

## Proof

For each degree \(n\), derivative order \(r<n\), and integer \(1\le h\le n\), the cardinal truncated-power formula gives
\[
 a_{n,r}(h):=B_n^{(r)}(h)=\frac1{(n-r)!}\sum_{\ell=0}^{h}(-1)^\ell\binom{n+1}{\ell}(h-\ell)^{n-r}.
\]
All other integer samples vanish. Its finite Fourier symbol is \(H_{n,r}(z)=\sum_{h=1}^{n}a_{n,r}(h)z^h\), where \(|z|=1\). The full tap sequences \((a_{n,r}(1),\ldots,a_{n,r}(n))\) are:

| Degree | Derivative order | Integer-knot filter taps |
| --- | --- | --- |
| \(3\) | \(0\) | \((1/6,\ 2/3,\ 1/6)\) |
| \(3\) | \(1\) | \((1/2,\ 0,\ -1/2)\) |
| \(3\) | \(2\) | \((1,\ -2,\ 1)\) |
| \(4\) | \(0\) | \((1/24,\ 11/24,\ 11/24,\ 1/24)\) |
| \(4\) | \(1\) | \((1/6,\ 1/2,\ -1/2,\ -1/6)\) |
| \(4\) | \(2\) | \((1/2,\ -1/2,\ -1/2,\ 1/2)\) |
| \(4\) | \(3\) | \((1,\ -3,\ 3,\ -1)\) |

Put \(s=2-z-z^{-1}=2-2\cos\theta\), for \(z=e^{i\theta}\). Direct products \(H_{n,r}(z)H_{n,r}(z^{-1})\) yield the following exact polynomials \(A_{n,r}(s)=|H_{n,r}(e^{i\theta})|^2\):
\[
\begin{aligned}
 A_{3,0}(s)&=(1-s/6)^2,\\
 A_{3,1}(s)&=s(1-s/4),\\
 A_{3,2}(s)&=s^2;
\end{aligned}
\qquad
\begin{aligned}
 A_{4,0}(s)&=(1-s/4)(1-s/12)^2,\\
 A_{4,1}(s)&=s(s-6)^2/36,\\
 A_{4,2}(s)&=s^2(1-s/4),\\
 A_{4,3}(s)&=s^3.
\end{aligned}
\]
Substitution proves the two identities
\[
 A_{3,0}+\tfrac13A_{3,1}+\tfrac1{18}A_{3,2}=1,
\qquad
 A_{4,0}+\tfrac5{12}A_{4,1}+\tfrac{13}{144}A_{4,2}+\tfrac{11}{864}A_{4,3}=1.
\]
By discrete Plancherel, for finitely supported \(c\), each discrete sample sequence \(f^{(r)}(k)=\sum_jc_ja_{n,r}(k-j)\) has squared norm \((2\pi)^{-1}\int_0^{2\pi}|\widehat c(\theta)|^2A_{n,r}(s)\,d\theta\). Weighted summation gives the coefficient isometry. Finite-support sequences are dense in \(\ell^2\), and the finite filters are bounded convolutions, so the identity extends to every \(c\in\ell^2\).

For uniqueness, suppose real constants \(v_r\) give \(\sum_rv_rA_{n,r}(s)\equiv1\). Because \(A_{n,0}(0)=1\) and \(A_{n,r}\) has a zero of **exact order \(r\)** at \(s=0\) with nonzero leading coefficient for every \(r\ge1\), the successive coefficients of \(s^0,s^1,\ldots,s^{n-1}\) determine every \(v_r\) uniquely. The displayed solutions are strictly positive; omitting any derivative order is therefore incompatible with tightness under diagonal weights.

Let \(T\) map a coefficient sequence to the weighted jet samples. The identity gives \(T^*T=I\) by polarization, so \(c=T^*Tc\). Writing out its finite-filter adjoint yields the stated local reconstruction formula. As \(T\) is an isometry, \(\|T^*\|=1\) in the weighted sample norm. Finally, for cubic values plus first derivatives the Nyquist and zero-frequency symbols are \(A_{3,0}(4)=1/9\), \(A_{3,0}(0)=1\), and \(A_{3,1}(0)=A_{3,1}(4)=0\). Hence the ratio of essential spectral maximum to minimum is at least \(9\) whenever nonnegative diagonal weights produce a positive lower bound. For values alone the symbol is decreasing on \([0,4]\), so the ratio is exactly \(9\).

## Verification

The standalone verifier `verify_spline_jets.py` computes every integer-knot derivative tap from the truncated-power formula over rational arithmetic, tests all nonconstant Laurent coefficients of the weighted symbol, checks invertibility and uniqueness of the diagonal-weight system, and confirms all displayed polynomial factorizations at representative unit-circle points. It also performs forty exact-rational finite-signal Parseval and local reconstruction trials for each degree, plus the cubic Nyquist identity; its recorded execution reported 1,449 assertions with no failure. The infinite-sequence statement follows analytically from Plancherel and bounded convolution, **not** from these finite trials.

Reproduce with Python 3 and SymPy: `python verify_spline_jets.py`.

## Relationship to prior work

Fageot–Aziznejad–Unser–Uhlmann (arXiv:1902.02565) study support optimality and approximation constants for cubic Hermite splines, and relate them to cardinal cubic B-splines. Their investigated Hermite interpolation uses a two-generator basis; its stated results do not furnish the diagonal knot-jet isometries here for a one-generator cubic or quartic cardinal B-spline space.

Shen–Xu (arXiv:1112.5771) construct **dilated wavelet-framelet systems** from B-spline refinable functions and represent some framelets through derivatives of box splines; this differs from undilated integer-knot observations and a Parseval frame for a *control-coefficient* Hilbert space. Gröchenig–Romero–Stöckler (DOI:10.1007/s00365-019-09456-3) establish density criteria for derivative sampling with totally positive generators, not exact diagonal tight weights of these spline coefficient sample filters. Gröchenig–Shafkulovska (arXiv:2311.08352) prove derivative-sampling and local collocation invertibility for periodic exponential B-splines, a family encompassing the polynomial cardinal case, but their main theorems give sampling sufficiency via gaps and densities, not these exact unit-tight weights, diagonal uniqueness or explicit adjoint FIR synthesis. Unser–Aldroubi–Eden (DOI:10.1109/78.193220) characterize the B-spline sampling filters and recursive interpolation, but the accessible summary does not assert this exact multi-jet Parseval identity or uniqueness.

## Limitations

These formulas hold only for the cardinal degrees \(3\) and \(4\) and coefficient-space energy. The physical \(L^2(\mathbb R)\) spline norm is not identified with the coefficient norm. A finite-support proof does not alone establish general spline-space sampling; the bounded-operator extension is essential. Arbitrary non-diagonal weighting, incomplete or noisy knot observations, and nonuniform grids are not classified. The exact filters and an algebraic derivation are reproducible, but priority relative to all older spline-filter constructions remains a bibliographic risk. No independent audit has been performed.

## References

1. J. Fageot, S. Aziznejad, M. Unser, and V. Uhlmann, *Support and Approximation Properties of Hermite Splines*, arXiv:1902.02565, first posted 2019-02-07, https://arxiv.org/abs/1902.02565.
2. Z. Shen and Z. Xu, *On B-Spline Framelets Derived from the Unitary Extension Principle*, arXiv:1112.5771, https://arxiv.org/abs/1112.5771.
3. K. Gröchenig, J. L. Romero, and J. Stöckler, *Sharp Results on Sampling with Derivatives in Shift-Invariant Spaces and Multi-Window Gabor Frames*, arXiv:1712.07899, first posted 2017-12-21, DOI:10.1007/s00365-019-09456-3.
4. K. Gröchenig and I. Shafkulovska, *Sampling theorems with derivatives in shift-invariant spaces generated by periodic exponential B-splines*, arXiv:2311.08352, first posted 2023-11-14, https://arxiv.org/abs/2311.08352.
5. M. Unser, A. Aldroubi, and M. Eden, *B-Spline Signal Processing: Part I—Theory*, DOI:10.1109/78.193220.
