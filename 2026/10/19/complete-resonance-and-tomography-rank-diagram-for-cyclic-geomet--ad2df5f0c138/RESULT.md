# Complete resonance and tomography-rank diagram for cyclic geometric Gabor windows

## Finding

Fix an integer \(N\ge3\), a nonzero complex number \(\gamma\), and the window \(g_\gamma(j)=\gamma^j\) for \(j=0,\ldots,N-1\), viewed as a function on \(\mathbb Z_N\). Let \(T_k g(j)=g(j-k\bmod N)\), \(M_b g(j)=e^{2\pi i bj/N}g(j)\), and let \(A_\gamma(k,b)=\langle g_\gamma,M_bT_kg_\gamma\rangle\), with the first argument conjugate-linear. Write \(w=\gamma^N\), \(r=|\gamma|\), and \(\omega=e^{2\pi i/N}\). The following is the *complete* self-ambiguity zero classification.

**Nonunit geometric ratios** (\(r\ne1\)). When \(N\) is odd, there are no zeros. When \(N=2m\) is even, there are no zeros unless \(w\) is real. If \(w>0\), the zero set is precisely \(\{(m,b):b\text{ odd}\}\); if \(w<0\), it is precisely \(\{(m,b):b\text{ even}\}\). Thus the number of missing ambiguity coefficients is either zero or \(m\).

**Unit-modulus ratios** (\(r=1\)). If \(w=1\), the zeros are precisely \(\{(k,b):b\ne0\}\). If \(w\ne1\), they are precisely \(\{(k,b): b\ne0,\ N\mid kb\}\), together with \((N/2,0)\) exactly in the case that \(N\) is even and \(w=-1\).

Let \(\mathcal P_\gamma\) denote the complex linear span of all \(N^2\) projectors \((M_bT_kg_\gamma)(M_bT_kg_\gamma)^*\). The exact rank is
\[
\dim_\mathbb C\mathcal P_\gamma=
\begin{cases}
N^2, & r\ne1,\ N\text{ odd or }w\notin\mathbb R,\\
N^2-N/2, & r\ne1,\ N\text{ even},\ w\in\mathbb R,\\
N, & r=1,\ w=1,\\
N^2+N-\displaystyle\sum_{d\mid N}d\varphi(N/d)-\mathbf1_{\{N\ \mathrm{even},\,w=-1\}},&r=1,\ w\ne1.
\end{cases}
\]
Here \(\varphi\) is Euler's totient function. Therefore the orbit performs full complex operator tomography (and phase retrieval for arbitrary complex signals) exactly when \(r\ne1\) and either \(N\) is odd or \(\gamma^N\notin\mathbb R\). In every other case it fails phase retrieval for arbitrary signals, not merely operator tomography. Nevertheless every nonunit ratio performs phase retrieval for *nowhere-zero* signals, even on the resonant even-dimensional phase loci.

In the nonunit even resonant case, the Hermitian measurement kernel is exactly \(m\)-dimensional over \(\mathbb R\), spanned by the following disjoint-pair matrices for \(0\le j<m\):
\[
H_j=\begin{cases}
i(E_{j,j+m}-E_{j+m,j}),&w>0,\\
E_{j,j+m}+E_{j+m,j},&w<0.
\end{cases}
\]
The two spectral eigenvectors of each \(H_j\) give explicit two-supported signals with identical intensity measurements but inequivalent global phases.

## Assumptions and scope

The dimension satisfies \(N\ge3\); the geometric ratio is any \(\gamma\in\mathbb C\setminus\{0\}\), with no algebraicity or number-theoretic restriction. The base vector is not normalized, but its nonzero scale does not change zero sets, projector span, or phase-retrieval injectivity. The result concerns the *complete* orbit with all \((k,b)\in\mathbb Z_N^2\), and operator rank is taken over complex matrices. The phrase 'phase retrieval' means injectivity on rank-one positive semidefinite matrices, or equivalently on vectors modulo unit-modulus scalar. No full-spark assertion is made.

## Proof

**1. Exact wrap-around evaluation.** For \(z=r^2\omega^b\), split the finite sum defining \(A_\gamma(k,b)\) into \(0\le j<k\) and \(k\le j<N\). This gives, whenever \(z\ne1\),
\[
A_\gamma(k,b)=\gamma^{-k}\left(w\sum_{j=0}^{k-1}z^j+\sum_{j=k}^{N-1}z^j\right)
=\gamma^{-k}\frac{w-|w|^2+(1-w)z^k}{1-z}.
\]
Here \(z^N=r^{2N}=|w|^2\). The sole possibility \(z=1\) occurs when \(r=1\) and \(b=0\), where direct summation instead yields
\[
A_\gamma(k,0)=\gamma^{-k}(kw+N-k).
\]
These identities include \(k=0\) and every frequency boundary.

**2. Nonunit case.** If \(r\ne1\), then \(w\ne1\) and \(z\ne1\). A zero is equivalent to
\[
z^k=\frac{w(\overline w-1)}{1-w}.
\]
The right side has modulus \(|w|=r^N\), whereas the left side has modulus \(r^{2k}\). Since \(r\ne1\), equality forces \(2k=N\). Thus only \(N=2m\) is possible. Writing \(w=s u\), with \(s=r^N>0\) and \(|u|=1\), the remaining condition is
\[
(-1)^b=\frac{s-u}{1-su}.
\]
Since \(s\ne1\), the right side equals \(+1\) precisely when \(u=-1\), and equals \(-1\) precisely when \(u=1\). This gives both exact parity rows and excludes every other zero.

**3. Unit-modulus case.** When \(r=1\) and \(b\ne0\), the geometric sum becomes
\[
A_\gamma(k,b)=\gamma^{-k}(w-1)\frac{1-\omega^{bk}}{1-\omega^b}.
\]
If \(w=1\), this always vanishes; if \(w\ne1\), it vanishes exactly when \(N\mid bk\). The separate \(b=0\) identity can vanish only for \(k=N/2\) and \(w=-1\). For fixed \(k\), precisely \(\gcd(k,N)-1\) nonzero frequencies satisfy \(N\mid kb\). Summing these counts gives \(\sum_{k=0}^{N-1}\gcd(k,N)-N\); the classical divisor grouping identity converts \(\sum_k\gcd(k,N)\) into \(\sum_{d\mid N}d\varphi(N/d)\).

**4. Exact rank.** The matrices \(\{N^{-1/2}M_bT_k\}\) form a Hilbert--Schmidt orthonormal basis. The discrete symplectic Fourier transform of the projector orbit diagonalizes the corresponding intensity-lifting operator, with one diagonal factor proportional to \(A_\gamma(k,b)\) for each Weyl index. Therefore its rank is exactly the number of nonzero ambiguity coefficients; the formulas follow by subtraction. This uses the standard finite Gabor lifting identity rather than assuming that intensity injectivity is equivalent to zero-free ambiguity.

**5. Phase retrieval and full-support boundary.** If the ambiguity has no zeros, injectivity on all complex matrices implies arbitrary-signal phase retrieval. If \(r=1\), every Gabor atom has constant coordinate magnitudes, so any two distinct coordinate unit vectors have identical intensity data. If \(r\ne1\), \(N=2m\), and \(w\in\mathbb R\), the only missing Weyl indices are \((m,b)\) of one parity. Fourier inversion in the modulation variable identifies the Hermitian kernel with the \(m\) matrices \(H_j\) displayed above: odd Fourier parity means opposite purely imaginary off-diagonal pair entries; even Fourier parity means equal real entries. Each \(H_j\) has two opposite nonzero eigenvalues and equals the difference of two inequivalent rank-one positive operators. This proves phase-retrieval failure at every singular nonunit ratio and identifies the full Hermitian kernel.

Finally, for any \(r\ne1\) and \(N\ge3\), the ambiguity coefficients with shifts \(k=0\) and \(k=1\) are all nonzero by step 2 (since the only possible zero shift is \(N/2\ge2\)). Thus the diagonal and first cyclic off-diagonal of a rank-one matrix can be recovered from all Gabor intensities. For nowhere-zero signals these diagonals determine all magnitudes and every neighboring phase ratio, hence the entire vector up to a global phase. This last mechanism is the published full-support criterion, applied here to its exact admissible parameter range.

## Verification

The accompanying `verify.py` uses Python's standard library to compare the direct finite ambiguity sums with the closed forms, every predicted zero/no-zero condition, and the arithmetic rank counts for twelve cyclic dimensions and seven representative complex ratios. It separately checks explicit unequal signal pairs at each two-dimensional rank-drop type. Run `python3 verify.py` from the directory containing this document and the script. Expected output: `VERIFY_OK 7070 direct-vs-formula / zero-pattern comparisons; 12 independent ambiguity witnesses; N=3..14`. These finite computations corroborate, but do not replace, the parameter-uniform proof above.

## Relationship to prior work

Dongwei Li, *Explicit Full-Spark and Quantitatively Phase-Retrievable Gabor Windows via Algebraic Perturbations* (arXiv:2609.09614, first posted 2026-09-09), proves a nonvanishing *single chosen complex geometric seed* with \(\gamma^N=2i\), along with a uniform ambiguity-margin estimate and a further algebraic full-spark regularization. Its Section 3.1 already contains the wrap-around summation mechanism. That mechanism is explicitly credited here. The present statement instead determines **every zero and the precise projector rank for every nonzero complex ratio in every cyclic dimension**, including the full unit-circle arithmetic strata, plus the entire rank-deficient Hermitian kernel and exact arbitrary-signal versus nowhere-zero-signal phase-retrieval boundary. These conclusions are not presented as consequences of full spark.

Bojarovska and Flinth, *Phase Retrieval from Gabor Measurements* (arXiv:1503.05800, first posted 2015-03-19), establish the nonvanishing-ambiguity sufficient condition and a general nowhere-zero signal criterion. These general implications are used, not claimed as new. Related finite Gabor projector-rank classifications for different window families provide contextual comparisons, not identical results.

## Limitations

This theorem concerns one natural two-real-parameter family \(g_\gamma(j)=\gamma^j\), not arbitrary Gabor windows. Its rank formula does not determine the numerical conditioning of nondegenerate ratios, full spark, performance under erasures, or recovery algorithms. For the singular even-dimensional ratios, nowhere-zero signals remain uniquely identifiable, while arbitrary-signal phase retrieval fails. The originality comparison is literature-based and may miss an equivalent older calculation in unindexed sources; no independent audit has been performed.

## References

1. D. Li, *Explicit Full-Spark and Quantitatively Phase-Retrievable Gabor Windows via Algebraic Perturbations*, arXiv:2609.09614 (2026), Section 3.1 and Proposition 3.11; https://arxiv.org/abs/2609.09614.
2. I. Bojarovska and A. Flinth, *Phase Retrieval from Gabor Measurements*, arXiv:1503.05800 (2015), Theorems 2.2--2.4; https://arxiv.org/abs/1503.05800.
