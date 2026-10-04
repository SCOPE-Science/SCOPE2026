# A parity dichotomy for Malikiosis's quadratic-exponent Gabor window
## Finding
For each integer \(N\ge2\), put \(\omega=e^{2\pi i/N}\) and define
\[
\eta_N(j)=e^{-j^2},\qquad j=0,\ldots,N-1.
\]
The full finite Gabor orbit \(\{M_\ell T_k\eta_N:k,\ell\in\mathbb Z_N\}\) is full spark for every \(N\). When \(N\ge3\) is odd, the same window has zero-free self-ambiguity and in fact
\[
\min_{k,\ell\in\mathbb Z_N}|\langle\eta_N,M_\ell T_k\eta_N\rangle|
\ge \frac45 e^{-(N-1)^2/4}.
\]
Hence, by the standard nonvanishing-ambiguity criterion, this one closed-form window is simultaneously full spark and phase retrievable for the finite Schrödinger representation in every odd cyclic dimension.

There is a sharp parity obstruction for this particular certificate. If \(N\) is even, then
\[
\langle\eta_N,M_\ell T_{N/2}\eta_N\rangle=0
\]
for every odd \(\ell\). This even-dimensional identity says that the zero-free-ambiguity criterion fails for the unmodified quadratic-exponent seed; it does not by itself prove failure of phase retrieval.

## Assumptions and scope
Translations and modulations on \(\mathbb C^N\) are
\[
(T_k f)(j)=f(j-k),\qquad (M_\ell f)(j)=\omega^{\ell j}f(j),
\]
with indices reduced modulo \(N\) to representatives in \(\{0,\ldots,N-1\}\). The ambiguity function is
\[
A_\eta(k,\ell)=\langle\eta,M_\ell T_k\eta\rangle.
\]
The phase-retrieval conclusion uses all \(N^2\) finite Gabor measurements. The full-spark conclusion is the ordinary statement that every \(N\)-element subfamily of the \(N^2\)-element Gabor orbit is a basis of \(\mathbb C^N\).

## Proof
Malikiosis proves that, after the substitution \(z_j=\xi^{j^2}\), every \(N\times N\) Gabor minor becomes a nonzero polynomial over \(\mathbb Q(\omega)\). Corollary 5.2 of arXiv:1304.7709 therefore gives full spark whenever \(\xi\) is transcendental. Taking \(\xi=e^{-1}\) yields precisely \(\eta_N(j)=e^{-j^2}\), so the Gabor orbit is full spark for every \(N\).

It remains to analyze the ambiguity function. Fix \(k\in\{0,\ldots,N-1\}\), and let \(r_k(j)\in\{0,\ldots,N-1\}\) be the representative of \(j-k\pmod N\). Since \(\eta_N\) is real,
\[
A_{\eta_N}(k,\ell)=\sum_{j=0}^{N-1}\omega^{-\ell j}e^{-s_k(j)},
\qquad
s_k(j)=j^2+r_k(j)^2.
\]
For \(j\ge k\),
\[
s_k(j)=j^2+(j-k)^2,
\]
which is strictly increasing with \(j\) on that branch and is minimized there at \(j=k\), with value \(k^2\). For \(j<k\),
\[
s_k(j)=j^2+(j-k+N)^2,
\]
which is strictly increasing with \(j\) on that branch and is minimized there at \(j=0\), with value \((N-k)^2\). Thus the two possible branch minima agree exactly when \(2k=N\).

Assume now that \(N\) is odd. The global minimum
\[
m_k=\min\{k^2,(N-k)^2\}
\]
is unique. Suppose first that \(0\le k\le(N-1)/2\), so the minimizing term is \(j=k\). Writing \(j=k+r\) on the same branch gives
\[
s_k(k+r)-m_k=2r(k+r)\ge2r^2.
\]
The other branch starts at a gap
\[
(N-k)^2-k^2=N(N-2k)\ge N,
\]
and successive exponents on that branch increase by at least \(N+3\). Therefore the sum of the magnitudes of all nonleading terms, divided by the leading magnitude \(e^{-m_k}\), is at most
\[
\frac{e^{-2}}{1-e^{-6}}+\frac{e^{-N}}{1-e^{-(N+3)}}
\le
\frac{e^{-2}+e^{-3}}{1-e^{-6}}
<\frac15.
\]
The case \(k\ge(N+1)/2\) is symmetric: the minimizing term is \(j=0\), the same-branch tail is bounded by \(e^{-2}/(1-e^{-6})\), and the opposite branch again starts at a gap at least \(N\) with successive gaps at least \(N+3\). Consequently, for every \(k,\ell\),
\[
|A_{\eta_N}(k,\ell)|
\ge e^{-m_k}\left(1-\frac15\right)
\ge \frac45 e^{-(N-1)^2/4}>0.
\]
Bojarovska and Flinth's Theorem 2.2 then implies phase retrieval from the full Gabor orbit.

If \(N\) is even, set \(k=N/2\). Pair the summand indexed by \(j\in\{0,\ldots,N/2-1\}\) with the summand indexed by \(j+N/2\). Their positive weights are equal because the shift by \(N/2\) swaps the two squared indices in \(s_k\). Their modulation factors differ by
\[
\omega^{-\ell N/2}=(-1)^\ell.
\]
Hence every pair cancels when \(\ell\) is odd, proving \(A_{\eta_N}(N/2,\ell)=0\).

## Verification
The proof is symbolic and does not infer an infinite statement from finite experiments. The only numerical inequality used is
\[
\frac{e^{-2}+e^{-3}}{1-e^{-6}}<\frac15,
\]
which is a direct elementary estimate. The full-spark input is exactly Malikiosis's Corollary 5.2 with the transcendental choice \(\xi=e^{-1}\). The phase-retrieval input is exactly the nonvanishing self-Gabor-coefficient hypothesis of Bojarovska--Flinth Theorem 2.2.

The boundary cases were checked in the proof rather than suppressed: for \(k=0\) the opposite branch is empty; for odd \(N\) the equality \(k=N/2\) never occurs; and for even \(N\) the half-period pairing gives an exact cancellation for every odd modulation index.

## Relationship to prior work
Malikiosis, arXiv:1304.7709, constructs the quadratic-exponent family \(z_j=\xi^{j^2}\) and proves it is full spark for transcendental \(\xi\), explicitly mentioning \(e\) and \(\pi\) as choices. That paper does not establish phase retrieval for this seed.

Bojarovska and Flinth, arXiv:1503.05800, prove that a finite Gabor generator whose self-Gabor coefficients are all nonzero yields phase retrieval. Führ and Oussa, arXiv:2201.08654, use the same sufficient criterion for the finite Schrödinger representation and explicitly ask for vectors that are simultaneously phase retrievable and full spark. The present calculation shows that Malikiosis's original explicit full-spark template, with \(\xi=e^{-1}\), already has both properties in every odd cyclic dimension.

Abreu--Balazs--Holighaus--Luef--Speckbacher, arXiv:2209.04191, construct a different explicit full-spark Gabor frame in odd dimensions from periodized Gaussian methods. Their result does not identify the quadratic-exponent seed or its ambiguity parity behavior.

A later preprint, arXiv:2609.09614, gives explicit simultaneous full-spark and phase-retrievable Gabor windows in every cyclic dimension by algebraic regularization and obtains substantially stronger quantitative ambiguity margins for other seeds. Thus the existence problem is now known in greater generality. The contribution here is narrower: an exact, elementary parity classification and explicit margin for the earlier quadratic-exponent full-spark seed itself.

## Limitations
The even-dimensional ambiguity zeros do not prove that \(\eta_N\) fails phase retrieval; they prove only that the standard zero-free-ambiguity sufficient criterion cannot certify it. The odd-dimensional lower bound is exponentially small in \(N^2\) and is not competitive with later constructions designed for quantitative stability.

The accessible material for arXiv:2609.09614 established its broader all-dimension existence theorem and its perturbative mechanism, but a formula-level full-text comparison with the exact seed \(e^{-j^2}\) was not available. An unindexed or formula-specific observation in that recent work therefore remains the principal originality risk.

## References
1. R.-D. Malikiosis, *A note on Gabor frames in finite dimensions*, arXiv:1304.7709, especially Lemma 5.1 and Corollary 5.2.
2. I. Bojarovska and A. Flinth, *Phase Retrieval from Gabor Measurements*, arXiv:1503.05800, Theorem 2.2.
3. H. Führ and V. Oussa, *Phase retrieval for nilpotent groups*, arXiv:2201.08654, finite Schrödinger example and the explicit simultaneous-construction problem.
4. L. D. Abreu, P. Balazs, N. Holighaus, F. Luef, M. Speckbacher, *Time-frequency analysis on flat tori and Gabor frames in finite dimensions*, arXiv:2209.04191.
5. D. Li, *Explicit Full-Spark and Quantitatively Phase-Retrievable Gabor Windows via Algebraic Perturbations*, arXiv:2609.09614.
