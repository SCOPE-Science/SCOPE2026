# Exact phase-retrieval fibers and one-probe completion for cyclic geometric windows

## Finding

For each integer \(N\geq2\) and each real \(r>0\), \(r\ne1\), take the cyclic geometric window \(g_r(j)=r^j\), \(0\leq j<N\), interpreted on \(\mathbb Z_N\). For a complex signal \(x\in\mathbb C^N\), observe every labelled intensity of the cyclic short-time Fourier transform
\[
S_r(x;m,\ell)=\left|\sum_{j=0}^{N-1}x_j g_r(j-m)e^{-2\pi i\ell j/N}\right|^2,\qquad (m,\ell)\in\mathbb Z_N^2.
\]
Then the full equivalence classes of signals with the same intensities are as follows, always modulo one global phase.

* If \(N\) is odd, the intensity data identify every signal uniquely.
* If \(N\) is even, a signal is uniquely identified unless its support is precisely a pair of antipodal indices \(\{j,j+N/2\}\) and its nonzero amplitudes have nonreal product. For an antipodal pair written, after a global phase choice, as \(x=a\delta_j+b\delta_{j+N/2}\) with \(a>0\) real, the entire fiber is represented by \(a\delta_j+b\delta_{j+N/2}\) and \(a\delta_j+\overline b\delta_{j+N/2}\). These coincide modulo phase exactly when \(b\) is real. Thus every nontrivial fiber contains exactly two projective signals; in particular every signal supported on at least three indices is identifiable.

When \(N\) is even, one **additional** intensity measurement is necessary and sufficient for global phase retrieval. Namely, with \(h=N/2\), define
\[
Q(x)=\left|\sum_{j=0}^{h-1}x_j+i\sum_{j=h}^{N-1}x_j\right|^2.
\]
The combined data \((S_r(x;m,\ell))_{m,\ell}\) and \(Q(x)\) distinguish all signals up to a global phase. No additional measurement is required for odd \(N\); for even \(N\), zero additional measurements cannot suffice.

The linear lifting by all \(N^2\) Gabor intensity projectors has real Hermitian kernel dimension exactly \(N/2\) for even \(N\), and zero for odd \(N\). Consequently one extra intensity repairs the *rank-one recovery* defect even though the corresponding lifted operator still has a nontrivial linear kernel when \(N\geq4\).

## Assumptions and scope

All indices are modulo \(N\), but the exponent in \(g_r(j)=r^j\) uses the unique representative \(0,\ldots,N-1\). No cyclic-extension identity \(r^{j+N}=r^j\) is assumed. The time-frequency intensities are individually labelled; recovery is up to multiplication by a scalar of absolute value one. The field is \(\mathbb C\), the ratio \(r\) is strictly positive and different from one, and the full \(N\times N\) discrete time-frequency grid is observed. Define the self-ambiguity coefficients by
\[
A_r(k,\ell)=\sum_{j=0}^{N-1}g_r(j)g_r(j-k)e^{-2\pi i\ell j/N}.
\]
They are unnormalized; changes of Fourier phase convention conjugate or reindex the coefficients but do not change their zero set.

## Proof

**Step 1: exact ambiguity zero set.** Write \(\omega=e^{2\pi i/N}\), \(s=r^2\omega^{-\ell}\), and \(t=r^N\). Splitting the cyclic sum into \(j<k\) and \(j\ge k\) gives, for every \(0\le k<N\),
\[
A_r(k,\ell)=r^{-k}\left(t\sum_{j=0}^{k-1}s^j+\sum_{j=k}^{N-1}s^j\right)
=r^{-k}(1-t)\frac{t+s^k}{1-s}.
\]
The expression is valid also for \(k=0\). Since \(r\ne1\), the factors \(1-s\) and \(1-t\) cannot vanish. The numerator \(t+s^k\) vanishes if and only if \(r^N=r^{2k}\) and \(\omega^{-\ell k}=-1\). Thus, if \(N\) is odd, all ambiguity coefficients are nonzero. If \(N=2h\) is even, the complete zero set is
\[
\{(k,\ell):A_r(k,\ell)=0\}=\{(h,\ell):\ell\text{ odd}\}.
\]
There are exactly \(h\) such zeros.

**Step 2: the exact lifted kernel.** Let \(\mathcal L(H)\) be the full array of inner products of a Hermitian matrix \(H\) with the Gabor rank-one projectors. Finite Weyl orthogonality gives the double-Fourier diagonalization: \(\mathcal L(H)=0\) exactly when the Fourier transform of the \(k\)-th cyclic matrix diagonal \(j\mapsto H_{j,j-k}\) vanishes at each \(\ell\) for which \(A_r(k,\ell)\ne0\). This follows by expanding all Gabor projectors in the orthogonal Weyl basis, or from the usual finite spectrogram ambiguity identity. When \(N\) is odd all diagonals vanish, so \(H=0\). When \(N=2h\), every diagonal except \(k=h\) vanishes. At \(k=h\), vanishing of all even Fourier coefficients is equivalent to
\[
H_{j+h,j}=-H_{j,j+h}\quad(0\le j<h).
\]
Hermiticity also says \(H_{j+h,j}=\overline{H_{j,j+h}}\), so the possible entries are precisely purely imaginary antipodal off-diagonal pairs. Each of the \(h\) unordered antipodal pairs contributes one independent real kernel parameter. In particular, all diagonal and all nonantipodal matrix entries are determined by the data, as is the real part of every antipodal entry.

**Step 3: the exact nonlinear fibers.** If \(x\) and \(y\) give equal intensities, then \(H=xx^*-yy^*\) belongs to the kernel above. The diagonal constraints imply \(|x_j|=|y_j|\) and hence identical supports. Whenever \(j\ne k\) are not antipodal, the offdiagonal constraints imply \(x_j\overline{x_k}=y_j\overline{y_k}\). On a support of at least three indices, the graph joining every nonantipodal pair is connected: a deleted antipodal matching cannot disconnect a complete graph on at least three vertices. Therefore all nonzero coordinate phases of \(x\) and \(y\) differ by a single common phase. The same conclusion holds for one-point supports and nonantipodal two-point supports. In the only remaining case, an antipodal two-point support, the data determine both absolute amplitudes and only the real part of their cross product. Choosing the first nonzero amplitude to be real positive leaves exactly the conjugate pair \(b,\overline b\), which coalesce precisely when \(b\) is real. The zero vector is uniquely characterized by zero measurements.

**Step 4: one additional scalar is exactly enough.** For antipodal two-point signals normalized as in Step 3, the extra measurement is \(Q(x)=|a+ib|^2=a^2+|b|^2+2\operatorname{Im}(a\overline b)\). Since the Gabor data already give \(a\), \(|b|\) and \(\operatorname{Re}(a\overline b)\), this uniquely fixes the remaining imaginary part, hence the signal up to global phase. On every other support the original data are already injective. The two genuinely distinct signals with \(a>0\) and \(b\notin\mathbb R\), \(b\) versus \(\bar b\), show that at least one extra intensity is necessary for even \(N\).

## Verification

The accompanying `verify_geometric_stft.py` runs exact cyclotomic-integer checks with \(r=2\) for every \(2\le N\le12\), every cyclic translation and modulation. It verifies the closed ambiguity formula and that the zero set is empty for odd \(N\) and exactly the half-translation/odd-modulation pairs for even \(N\). It additionally checks explicit antipodal two-point ambiguities and their resolution by the stated extra intensity in even dimensions through \(N=10\). The checker reports 690 assertions. These bounded checks corroborate the equations; the proof above establishes the theorem for all \(N\ge2\) and every allowed \(r\).

## Relationship to prior work

Bojarovska and Flinth (arXiv:1503.05800, Section 2.2) give the finite Weyl/ambiguity diagonalization and a sufficient condition for universal Gabor phase retrieval when every window ambiguity coefficient is nonzero. Their Section 2.4 gives general noninjective examples with substantially different zero sets. The present finding specializes the diagonalization to a real geometric window and, beyond the odd-order injectivity consequence, classifies the entire even-order phase-retrieval fiber, including support dependence, and proves one-probe completion.

Grohs, Liehr and Shafkulovska (arXiv:2211.05687) establish phaseless STFT sampling results for compactly supported signals in continuous function spaces, with different window and sampling assumptions. Their results motivate examining exact finite-dimensional sample fibers but do not yield this cyclic geometric-window classification directly. Li (arXiv:2609.09614, Section 3) analyzes an explicitly complex geometric seed to construct well-conditioned zero-free ambiguity functions; that seed is distinct from the positive real geometric family here, and the examined results do not give this family’s nonlinear fibers or one-probe completion.

## Limitations

The result is exact-data identifiability, not a stability or noise-amplification bound. The sole additional measurement need not be a time-frequency shift of the original window. When \(r=1\), the window is constant and the zero-set analysis changes; that case is excluded. The theorem does not describe incomplete time-frequency sampling or unknown measurement labels. General Weyl/ambiguity identities are prior mathematical tools, not claimed as new. Historical originality remains subject to an unindexed equivalent result for geometric finite-window phase retrieval.

## References

1. I. Bojarovska and A. Flinth, *Phase Retrieval from Gabor Measurements*, arXiv:1503.05800 (first publicly posted 2015-03-19), Section 2.2 and Section 2.4. https://arxiv.org/html/1503.05800v2
2. P. Grohs, L. Liehr and I. Shafkulovska, *From completeness of discrete translates to phaseless sampling of the short-time Fourier transform*, arXiv:2211.05687 (first publicly posted 2022-11-10). https://arxiv.org/abs/2211.05687
3. D. Li, *Explicit Full-Spark and Quantitatively Phase-Retrievable Gabor Windows via Algebraic Perturbations*, arXiv:2609.09614 (first publicly posted 2026-09-09), Section 3. https://arxiv.org/abs/2609.09614
