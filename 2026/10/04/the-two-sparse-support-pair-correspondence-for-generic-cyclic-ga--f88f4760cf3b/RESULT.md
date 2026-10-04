# The two-sparse support-pair correspondence for generic cyclic Gabor windows
## Finding
For every integer \(N\ge 2\), there is a nonempty Zariski-open, hence full-measure, set of windows \(g\in\mathbb C^N\) such that the following holds simultaneously for every two-point support. Fix distinct \(u,v\in\mathbb Z_N\), write \(s=v-u\) and \(d=\gcd(N,s)\), and let \(f\) range over signals whose support is exactly \(\{u,v\}\). The attainable short-time Fourier support sizes are exactly
\[
\{N^2,\ N^2-d\}.
\]
For the same fixed support, the attainable ordinary Fourier support sizes are exactly
\[
\{N,\ N-d\}.
\]
Thus, at exact signal-support size two, the two support spectra agree after the shift \(N^2-N\). Equivalently,
\[
\bigl\{\lvert\operatorname{supp}V_gf\rvert:\lvert\operatorname{supp}f\rvert=2\bigr\}
=\{N^2\}\cup\bigl\{N^2-d:d\mid N,\ d<N\bigr\}.
\]
If \(p\) is the least prime divisor of \(N\), then the generic optimum introduced for support at most two is
\[
\phi(\mathbb Z_N,2)=N^2-\frac{N}{p}.
\]

## Assumptions and scope
The group is \(\mathbb Z_N\), with \(N\ge2\). We use the unnormalized short-time Fourier transform
\[
V_gf(x,\xi)=\sum_{t\in\mathbb Z_N} f(t)\overline{g(t-x)}\exp(-2\pi i\xi t/N).
\]
The theorem concerns a generic window: the exceptional windows lie in a finite union of proper algebraic hypersurfaces together with coordinate hyperplanes. It classifies the attainable support cardinalities for signals of exact support size two; it does not claim that a particular signal has ordinary-Fourier and short-time-Fourier supports related by the shift.

## Proof
Translate the two-point support to \(\{0,s\}\); support cardinalities are unchanged. Write \(f=a\delta_0+b\delta_s\) with \(ab\ne0\), put \(q=a/b\), \(d=\gcd(N,s)\), and \(L=N/d\). For a fixed time index, relabel it by \(j=-x\). Then
\[
V_gf(x,\xi)=a\overline{g(j)}+b\overline{g(j+s)}\omega^{-s\xi},
\qquad \omega=\exp(2\pi i/N).
\]
The map \(\xi\mapsto\omega^{-s\xi}\) has image the group \(\mu_L\) of \(L\)-th roots of unity and every image value has exactly \(d\) preimages. Hence the entire frequency slice at time \(j\) has either zero zeros or exactly \(d\) zeros, and the latter occurs precisely when
\[
q\in C_j(g):=-\frac{\overline{g(j+s)}}{\overline{g(j)}}\mu_L.
\]
We now impose that every coordinate of \(g\) is nonzero and that the \(N\) cosets \(C_j(g)\) are pairwise disjoint for every nonzero \(s\). An overlap between the cosets for distinct \(j,k\) forces, for some \(\eta\in\mu_L\),
\[
g(j+s)g(k)-\eta g(j)g(k+s)=0.
\]
Each displayed relation is a nonzero polynomial: taking the coordinates of \(g\) to be distinct positive primes makes all positive ratios \(g(j+s)/g(j)\) distinct, and a positive real ratio can be an \(L\)-th root of unity only when it is \(1\). Therefore none of these finitely many polynomial conditions is identically zero. Their complement, after also excluding coordinate hyperplanes, is a nonempty Zariski-open set and has full Lebesgue measure.

For a window in this set, a coefficient ratio \(q\) belongs to at most one \(C_j(g)\). Therefore a two-point signal has either no short-time Fourier zeros or exactly \(d\) of them. Both cases occur: choose \(q\) outside the finite union of the \(C_j(g)\), or choose \(q\in C_j(g)\) for any fixed \(j\). This proves the short-time Fourier spectrum \(\{N^2,N^2-d\}\).

For the ordinary Fourier transform,
\[
\widehat f(\xi)=b\bigl(q+\omega^{-s\xi}\bigr)
\]
up to a nowhere-zero phase caused by the initial translation. Thus it has exactly \(d\) zeros when \(q\in-\mu_L\), and no zeros otherwise. Hence its support spectrum is \(\{N,N-d\}\). As \(s\) varies, \(\gcd(N,s)\) runs through every proper divisor of \(N\), proving the global formula and the support-pair correspondence at exact support size two.

Finally let \(p\) be the least prime divisor of \(N\). The largest proper divisor is \(N/p\), so a generic window has minimum short-time Fourier support \(N^2-N/p\) among signals of support at most two. No window can do better: if a window has a zero coordinate, a singleton signal has support at most \(N(N-1)\le N^2-N/p\); if it has full support, take \(s=N/p\) and choose the coefficient ratio to force one frequency slice to have \(N/p\) zeros. Therefore \(\phi(\mathbb Z_N,2)=N^2-N/p\).

## Verification
The accompanying `verify_two_sparse_generic_stft.py` is an exact standard-library replay. For every \(2\le N\le300\), it uses a window whose coordinates are distinct positive primes. It checks all nonzero differences \(s\), verifies exact pairwise distinctness of the rational ratios \(g(j+s)/g(j)\), verifies that the character map has exactly \(N/\gcd(N,s)\) image values with fibers of size \(\gcd(N,s)\), checks the shifted support spectra, and checks the least-prime-divisor formula. The replay performs \(8,999,900\) exact ratio-distinctness checks, \(8,999,900\) exact kernel-fiber checks, and \(44,850\) difference-spectrum checks, ending with `VERIFY_OK`.

The finite replay is a stress test, not the infinite proof. The proof for arbitrary \(N\) is the root-coset argument above together with the finite-union-of-proper-hypersurfaces argument.

## Relationship to prior work
Krahmer, Pfander, and Rashkov asked whether, for cyclic groups and almost every window, the set of pairs formed by signal-support size and short-time-Fourier-support size is exactly the ordinary Fourier support-pair set shifted by \(N^2-N\). Their paper proves the prime-order case and reports numerical evidence for small cyclic groups, but leaves the composite-order correspondence open.

Malikiosis later proved that almost all cyclic Gabor windows are full spark and, in the uncertainty formulation, proved the inclusion from ordinary Fourier support pairs into shifted short-time-Fourier support pairs. In the same section he states that the reverse inclusion is the difficult direction for composite order. The result here proves that reverse inclusion, and therefore equality, on the complete exact-support-two stratum for every cyclic order. It also gives the explicit value \(\phi(\mathbb Z_N,2)=N^2-N/p\), which for \(N=6\) yields \(33\), matching the earlier numerical table.

Targeted semantic searches for the exact two-sparse statement, its gcd formulation, the formula for \(\phi(\mathbb Z_N,2)\), and the support-pair reverse inclusion did not return a statement implying this theorem. Failed search is not a novelty proof; the residual risk is a differently phrased or poorly indexed treatment of this stratum.

## Limitations
The theorem addresses exact support size two only. It does not settle support sizes \(3\) through \(N\), does not characterize exceptional windows, and does not assert a pointwise identity relating the two transforms for the same signal. The Zariski-open condition used in the proof is sufficient for the stated generic theorem and may be stronger than necessary.

## References
1. F. Krahmer, G. E. Pfander, P. Rashkov, “Uncertainty in time-frequency representations on finite Abelian groups and applications,” arXiv:math/0611493v1 (first posted 2006-11-16), Applied and Computational Harmonic Analysis 25 (2008), 209–225, DOI 10.1016/j.acha.2007.09.008.
2. R.-D. Malikiosis, “A note on Gabor frames in finite dimensions,” arXiv:1304.7709v1 (first posted 2013-04-29), Applied and Computational Harmonic Analysis 38 (2015), 318–330.
3. R.-D. Malikiosis, “Spark deficient Gabor frames,” arXiv:1602.09012v1 (first posted 2016-02-29), Pacific Journal of Mathematics 294 (2018), 159–180, DOI 10.2140/pjm.2018.294.159.
