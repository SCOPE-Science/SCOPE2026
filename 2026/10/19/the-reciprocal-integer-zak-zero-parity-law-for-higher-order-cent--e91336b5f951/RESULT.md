# The reciprocal-integer Zak-zero parity law for higher-order centered B-splines

## Finding

Let \(n\ge3\) and \(m\ge2\) be arbitrary integers. For centered cardinal B-splines and the Zak normalization stated below, the complete zero set at scale \(\lambda=1/m\) is
\[
\mathcal Z_{n,m}=\bigcup_{j=1}^{m-1}\bigl([0,1)\times\{j/m\}\bigr)
\quad\text{if }m\text{ is even},
\]
and
\[
\mathcal Z_{n,m}=\left(\bigcup_{j=1}^{m-1}[0,1)\times\{j/m\}\right)\cup\{(1/2,1/2)\}
\quad\text{if }m\text{ is odd}.
\]
The second union is disjoint when \(m\) is odd. These are **all** zeros on the fundamental domain, including off-symmetry zeros. Every generic point of each zero line has *exact* order \(n\) in frequency; the unique exceptional point for even \(m\) has order at least \(n+1\).

## Assumptions and scope

Define \(B_1=\mathbf1_{[-1/2,1/2]}\), with endpoint values irrelevant to convolutions of order at least two, and \(B_n=B_1^{*n}\). For any compactly supported \(g\) set
\[
Z_\lambda g(x,\nu)=\sqrt{\lambda}\sum_{k\in\mathbb Z}g(\lambda(x-k))e^{2\pi i k\nu}.
\]
All sums here are finite for each \(x\), and the transform is periodic in \(\nu\), quasi-periodic in \(x\): \(Z_\lambda g(x+1,\nu)=e^{2\pi i\nu}Z_\lambda g(x,\nu)\). The domain is \([0,1)\times[0,1)\). The results hold for every integer \(n\ge3\), every integer \(m\ge2\), and no claim is made for nonreciprocal scales. The first source [1] uses exactly this Zak normalization and spline convention.

Write
\[
K=\left\lfloor\frac{n(m-1)}2\right\rfloor,\qquad
r=\frac{n(m-1)}2-K\in\{0,1/2\},\qquad z=e^{2\pi i\nu}.
\]
The precise generating identity is
\[
\boxed{Z_{1/m}B_n(x,\nu)=m^{1/2-n}z^K
\left(1+z^{-1}+\cdots+z^{-(m-1)}\right)^n
Z_1 B_n(x+r,\nu).}
\]

## Proof

**1. Derive the exact refinement factor.** With \(\widehat f(\xi)=\int f(t)e^{-2\pi i t\xi}\,dt\), the centered spline has \(\widehat{B_n}(\xi)=\operatorname{sinc}(\xi)^n\), where \(\operatorname{sinc}(\xi)=\sin(\pi\xi)/(\pi\xi)\) with value \(1\) at the origin. Put \(h(t)=B_n(t/m)\). Then
\[
\widehat h(\xi)=m\operatorname{sinc}(m\xi)^n
=m^{1-n}\widehat{B_n}(\xi)
\left(\sum_{j=0}^{m-1}e^{2\pi i((m-1)/2-j)\xi}\right)^n.
\]
The equality follows from the finite geometric identity for the sine quotient, and it extends across its removable singularities. Fourier inversion yields the *finite*, exact translation identity
\[
B_n(t/m)=m^{1-n}\sum_{j_1,\ldots,j_n=0}^{m-1}
B_n\left(t+\frac{n(m-1)}2-\sum_{a=1}^n j_a\right).
\]
Substitute \(t=x-k\) into the Zak sum. Reindex the Zak integer by \(k'=k-K+\sum_a j_a\). The phase becomes \(z^{k'+K-\sum_a j_a}\) and the B-spline argument becomes \(x+r-k'\). Pulling out the finite character sum and \(m^{-1/2}\) from Zak normalization proves the boxed identity for all real \(x,\nu\).

**2. Locate every frequency factor zero.** For \(z\ne0\), the Laurent polynomial \(D_m(z)=\sum_{j=0}^{m-1}z^{-j}\) vanishes precisely at the nonidentity \(m\)-th roots of unity, all simply: indeed \(D_m(z)=z^{1-m}(z^m-1)/(z-1)\). Thus \(D_m(e^{2\pi i\nu})^n=0\) if and only if \(\nu=j/m\) with \(1\le j\le m-1\), with exact root order \(n\) before the final Zak factor is considered.

**3. Exclude all extraneous zeros.** The classical Schoenberg–Euler-spline zero theorem, in the centered convention stated in [1, §1 and §2.1], asserts that for all \(n\ge2\) the unit-scale transform \(Z_1B_n(y,\nu)\) has exactly one zero modulo the Zak fundamental lattice, namely \((y,\nu)=(1/2,1/2)\). This published theorem is a *premise*, not reproved here. Hence the last factor can vanish only if \(\nu=1/2\) and \(x+r\equiv1/2\pmod1\). When \(m\) is even, \(\nu=1/2\) is already one of the horizontal zero lines; when \(m\) is odd, it is on none of them. In the odd case, \(m-1\) is even, so \(r=0\) and the extra point is \((1/2,1/2)\). This gives the complete zero set, not merely a necessary condition.

**4. Frequency multiplicity.** Since every nonidentity \(m\)-th root of unity is a *simple* zero of \(D_m\), at each horizontal line the frequency order is exactly \(n\) whenever the unit-scale factor is nonzero. The unit-scale theorem says that additional vanishing can occur only if \(m\) is even, \(j=m/2\), and \(x\equiv1/2-r\pmod1\). At that one point the order is at least \(n+1\) because the remaining factor is a finite Laurent polynomial in \(z\) vanishing at \(z=-1\). No upper bound on the exceptional multiplicity is needed or asserted.

## Verification

The included file `verify_b_spline_reciprocal_zak.py` is a standalone Python 3 checker using only the standard library. Run `python3 verify_b_spline_reciprocal_zak.py` in the directory containing the file. It independently expands the centered cardinal B-spline by truncated powers and compares the *complete finite Laurent coefficients*, exactly over rational numbers, with the refinement prediction. It performs 216 exact polynomial coefficient comparisons for \(3\le n\le8\), \(2\le m\le7\), and six rational spatial fibers, plus 252 numerical root-line comparisons. It prints `VERIFY_OK 468 exact rational polynomial and numerical root checks; n=3..8, m=2..7` when successful. These tests independently catch phase shifts and normalization factors but do not establish the claim for arbitrary integer parameters; that follows from the proof and the cited classical unit-scale theorem.

## Relationship to prior work

Hasannasab–Lemvig [1] explicitly identify complete Zak zero sets for the second-order hat spline at all positive scales and for all higher orders in their large-scale regime. Their Proposition 4.1 establishes the horizontal zero lines at reciprocal-integer scales but does not assert that these lines, plus at most the symmetry point, **exhaust** the zeros for higher-order splines. Lemvig–Nielsen [2] established the earlier horizontal-line obstruction, not the complete off-line exclusion. The unit-scale unique-zero theorem used in Step 3 is classical, dating to Schoenberg and the work of Jetter–Riemenschneider–Sivakumar [4], and is explicitly credited rather than presented as new. Kloos–Stöckler [3] likewise treat unique unit-scale zeros. The result here combines an explicit reciprocal-integer refinement-Zak factorization with that known theorem to finish a natural infinite subfamily \(\lambda=1/m<1\) of the previously unclassified higher-order region. The known second-order treatment [5] is not claimed as new. The broader \(0<\lambda<1\) problem for nonreciprocal \(\lambda\) remains open here.

## Limitations

This is an exact theorem in a special arithmetic subfamily, not a classification at general \(\lambda<1\) and not a new frame-set theorem. The unique-zero theorem for unit-scale B-splines is used as a published mathematical premise. The finite checker does not independently verify the infinite-dimensional classical lemma. The multiplicity at the exceptional even-scale point is bounded below but not calculated exactly. Historical priority is not conclusively established: a classical spline-refinement reference could contain this same fact in equivalent language, despite the comparison against the closest inspected primary sources.

## References

[1] Marzieh Hasannasab and Jakob Lemvig, The zero set of the Zak transform of B-splines with applications to Gabor frames (2026), arXiv:2609.13116, https://arxiv.org/abs/2609.13116 .

[2] Jakob Lemvig and Kamilla Haahr Nielsen, Counterexamples to the B-spline conjecture for Gabor frames (2015/2016), arXiv:1507.03982, https://arxiv.org/abs/1507.03982 .

[3] Tobias Kloos and Joachim Stöckler, Zak transforms and Gabor frames of totally positive functions and exponential B-splines (2013/2014), arXiv:1311.7359, https://arxiv.org/abs/1311.7359 .

[4] K. Jetter, S. D. Riemenschneider, and N. Sivakumar, Schoenberg's exponential Euler spline curves, Proceedings of the Royal Society of Edinburgh Section A 118 (1991), 21–33. (Classical theorem cited in arXiv:2609.13116.)

[5] Alexander Stangl and Christina Frederick, The frameset of the second-order B-Spline along \(ab=1/q\) (2026), arXiv:2609.00481, https://arxiv.org/abs/2609.00481 .
