# Exact full-support phase fibers for the three-site cyclic boxcar window

## Finding
Let \(N\ge8\) be even with \(3\nmid N\). Fix the cyclic window \(g=\mathbf1_{\{0,1,2\}}\) on \(\mathbb Z_N\). For every coordinatewise nonzero signal \(x\in\mathbb C^N\), the complete set of signals with the same full cyclic short-time Fourier transform (STFT) magnitudes as \(x\), modulo a common unimodular scalar, has **either one or two elements**. The two-element case occurs precisely for signals of the form
\[
 x_{2j}=a\lambda^j,\qquad x_{2j+1}=b\lambda^j,
 \quad 0\le j<N/2,\quad
 a,b\in\mathbb C\setminus\{0\},\quad
 \lambda^{N/2}=1,
\]
subject to the strict phase condition
\[
 b\overline a\ne a\overline b\,\lambda.
\]
In that case, besides the phase class of \(x\), the **only** other class is represented by
\[
 y_{2j}=a\lambda^j,\qquad
 y_{2j+1}=\frac{a}{\overline a}\,\overline b\,\lambda^{j+1}
 \qquad (0\le j<N/2).
\]
When the displayed phase condition is an equality, and for all signals not having the indicated two-progression form, the fiber contains just the phase class of \(x\). Both alternatives in a two-element fiber are coordinatewise nonzero and have exactly the same coordinate magnitudes.

Equivalently, the failure of uniqueness for this window and dimension range is **a twofold phase-conjugation ambiguity on precisely described alternating geometric progressions**, rather than an amplitude-exchange ambiguity. There is no other full-support ambiguity.

## Assumptions and scope
Use cyclic indices and the unnormalized transform
\[
 V_gx(m,k)=\sum_{t\in\mathbb Z_N}x_t\overline{g_{t-m}}
 e^{-2\pi i kt/N},\qquad m,k\in\mathbb Z_N.
\]
The measurements are all \(N^2\) values \(\lvert V_gx(m,k)\rvert\). Common phase is the only equivalence imposed; time shifts, reflection, and modulation are **not** factored out. All signal coordinates must be nonzero. The arithmetic restriction \(3\nmid N\) makes the length-three cyclic sum invertible, while the even-order restriction creates the one-dimensional alternating kernel of the adjacent-product recovery map. The lower bound \(N\ge8\) prevents aliasing among the frequency lags \(0,\pm1,\pm2\).

## Proof
**1. Extract three rows of cyclic correlations.** Put \(\omega=e^{2\pi i/N}\) and
\[
 C_r(m)=\frac1N\sum_{k=0}^{N-1}\lvert V_gx(m,k)\rvert^2\omega^{kr},
 \qquad r\in\{0,1,2\}.
\]
Expanding the three-term transform and using Fourier orthogonality gives exactly
\[
 \begin{aligned}
 C_0(m)&=\lvert x_m\rvert^2+\lvert x_{m+1}\rvert^2+\lvert x_{m+2}\rvert^2,\\
 C_1(m)&=x_{m+1}\overline{x_m}+x_{m+2}\overline{x_{m+1}},\\
 C_2(m)&=x_{m+2}\overline{x_m}.
 \end{aligned}
\]
Here \(N\ge8\) ensures the differences between positions \(0,1,2\) do not coincide modulo \(N\). The negative-lag correlations are the conjugates of these rows, so the displayed three rows determine the entire STFT intensity array.

**2. Magnitudes and every second-neighbor product are fixed.** Suppose \(y\) has the same STFT magnitudes as \(x\). Put \(d_m=\lvert y_m\rvert^2-\lvert x_m\rvert^2\). Equality of \(C_0\) gives \(d_m+d_{m+1}+d_{m+2}=0\) at every position. Subtracting consecutive equations yields \(d_{m+3}=d_m\). Since \(3\nmid N\), a sequence both \(3\)-periodic and \(N\)-periodic is constant. Therefore \(3d_m=0\) and \(d_m=0\) for all \(m\).

Since the coordinates of \(x\) are nonzero, the coordinates of \(y\) are also nonzero. Write \(z_m=y_m/x_m\); the preceding step gives \(\lvert z_m\rvert=1\). Equality of \(C_2\) gives \(z_{m+2}\overline{z_m}=1\), hence \(z_{m+2}=z_m\). As \(N\) is even, \(z_m\) equals some \(U\in\mathbb T\) on even indices and some \(V\in\mathbb T\) on odd indices. Divide \(y\) by the global phase \(U\) and write \(W=V/U\). Thus any possible alternative has
\[
 y_{2j}=x_{2j},\qquad y_{2j+1}=Wx_{2j+1},\qquad \lvert W\rvert=1.
\]

**3. The adjacent-product constraint classifies every alternative.** Set \(B_m=x_{m+1}\overline{x_m}\). Equality of \(C_1\) means
\[
 (W-1)B_m+(\overline W-1)B_{m+1}=0\quad(m\text{ even}),
\]
and the same equation with the coefficients interchanged for odd \(m\). If \(W=1\) the signals agree up to global phase. Otherwise \(\overline W-1=-(W-1)/W\), so
\[
 B_{m+1}=WB_m\quad(m\text{ even}),\qquad
 B_{m+1}=W^{-1}B_m\quad(m\text{ odd}).
\]
In particular, all \(B_{2j}\) have one constant value \(\beta\ne0\), all \(B_{2j+1}\) another constant value \(\alpha=W\beta\ne0\), and \(W=\alpha/\beta\).

For any such sequence, the identity
\[
 \frac{x_{2j+2}}{x_{2j}}=
 \frac{B_{2j+1}}{\overline{B_{2j}}}
 =\frac{\alpha}{\overline\beta}=: \lambda
\]
shows that \(x_{2j}=a\lambda^j\) for \(a=x_0\ne0\). Cyclicity forces \(\lambda^{N/2}=1\), hence \(\lvert\lambda\rvert=1\). The relation \(B_{2j}=\beta\) then gives \(x_{2j+1}=b\lambda^j\), with \(b=x_1\ne0\). For these parameters,
\[
 \beta=b\overline a,\qquad \alpha=a\overline b\,\lambda,
 \qquad W=\frac{a\overline b\,\lambda}{b\overline a}.
\]
Thus \(W\ne1\) is equivalent to the strict phase condition in the theorem. It is also unimodular. The value of \(W\), and therefore the alternate signal \(y\), is forced uniquely, proving that there can be no third phase class.

**4. Construct and verify the alternative.** Conversely, take any nonzero \(a,b\) and any \((N/2)\)-th root of unity \(\lambda\). Define \(x\) by the two-progression formula and put \(W=\alpha/\beta\) as above. The signal \(y_{2j}=x_{2j}\), \(y_{2j+1}=Wx_{2j+1}\) has equal coordinate magnitudes, so its \(C_0\) agrees with that of \(x\). Its two-step products are identical, so its \(C_2\) agrees. Its adjacent-product sequence alternates between \(\beta\) and \(\alpha\), and the identity
\[
 W\beta+\overline W\alpha=\alpha+\beta
\]
is immediate from \(W=\alpha/\beta\). Thus its \(C_1\) agrees as well. Hence **all** STFT intensities agree. Simplifying \(Wb=(a/\overline a)\overline b\,\lambda\) yields the explicit displayed alternative. It differs by more than a global phase exactly when \(W\ne1\), as asserted.

## Verification
`CHECK.py` is a Python-standard-library consistency checker. Execute `python3 CHECK.py`. It directly computes STFT intensity arrays from the three-tap window, independently extracts Fourier coefficients, verifies the three analytic correlation formulas, and constructs phase-distinct ambiguous pairs across many even cyclic orders that are not divisible by three. The packaged checker completed with `CHECK_OK 29120` (29,120 supplementary assertions). Tests do not establish the theorem for arbitrary \(N\); the all-order proof is the preceding finite-correlation and periodicity argument.

An elementary exact example at \(\lambda=1\), \(a=1\), \(b=1+i\) has alternating entries \(1,1+i\), while its only nontrivial partner has alternating entries \(1,1-i\). They have identical spectrograms for every admissible \(N\), and neither is a common-phase multiple of the other.

## Relationship to prior work
Bartusel's 2026 preprint [1] studies how ambiguity-function zeros interact with finite STFT phase retrieval and gives broad sufficient criteria. It motivates the need to understand highly singular but structured windows. Its accessible abstract does not give the present exceptional-fiber classification; the full paper could not be inspected, which remains a literature risk.

The earlier complete analysis of cyclic STFT conditions by Bartusel [2], especially Section 4.2's generic-window theorem and Section 4.3's sparse-signal theorems, is not an equivalent classification: the present three-site equal window has a missing adjacent-product Fourier mode in even order, and the theorem treats nonvanishing signals instead of those with consecutive zeros. The three-row correlation identity used in the proof is a specialization of classical STFT autocorrelation extraction (cf. [2], Lemma 4.3.3); that identity itself is not claimed as new.

A published exact fiber classification for an **even two-site** cyclic STFT window [3] has a different mechanism: it permits a swap of alternating **amplitude levels**. Here all amplitudes are uniquely recovered and the sole exceptional freedom is alternating **phase conjugation**. Published odd-order endpoint-lag recovery [4] explicitly excludes even orders. A published exact operator-span rank formula for boxcar Gabor measurements [5] addresses linear informational completeness, and explicitly does not classify nonlinear pure-state phase-retrieval fibers. A three-tap self-ambiguity support-spectrum result [6] classifies spectral zero counts, not distinct full-support input signals with identical intensity data.

## Limitations
The classification is limited to even \(N\ge8\) with \(3\nmid N\), the equal-weight three-consecutive-site window, the full (not subsampled) cyclic spectrogram, and nowhere-zero signals. The cases \(3\mid N\), general three-tap weights, sparse input signals, stability under noise, and incomplete frequency sampling are not solved. An equivalent unindexed earlier result is possible. The 2026 motivating paper was only available in abstract form, so no whole-document noncoverage claim is made for that source.

## References
1. D. Bartusel, *Uncertainty Principles as a Tool for STFT Phase Retrieval*, arXiv:2605.31507v1, first posted 2026-05-29, https://arxiv.org/abs/2605.31507 .
2. D. Bartusel, *Injectivity Conditions for STFT Phase Retrieval on Z, Zd and Rd*, arXiv:2206.06729v1 (2022), Sections 4.2--4.3, https://arxiv.org/html/2206.06729v1 .
3. *Exact nonvanishing phase-retrieval fibers for an even two-point cyclic STFT window*, public mathematical record `2026/10/4/SCOPE-exact-nonvanishing-phase-retrieval-fibers-for-an-even-two-point--29afd3fc909d`, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-nonvanishing-phase-retrieval-fibers-for-an-even-two-point--29afd3fc909d .
4. *Endpoint-lag recovery for nonvanishing cyclic STFT phase retrieval*, public mathematical record `2026/10/4/SCOPE-endpoint-lag-recovery-for-nonvanishing-cyclic-stft-phase-retriev--5ab5cece2e03`, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-endpoint-lag-recovery-for-nonvanishing-cyclic-stft-phase-retriev--5ab5cece2e03 .
5. *Exact operator-span rank and arithmetic thresholds for cyclic boxcar Gabor measurements*, public mathematical record `2026/10/11/SCOPE-exact-operator-span-rank-and-arithmetic-thresholds-for-cyclic-bo--98526b581328`, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-operator-span-rank-and-arithmetic-thresholds-for-cyclic-bo--98526b581328 .
6. *Parity-rigid ambiguity-support spectra for primitive three-tap cyclic signals*, public mathematical record `2026/10/11/SCOPE-parity-rigid-ambiguity-support-spectra-for-primitive-three-tap-c--4fe8e5c0fab7`, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-parity-rigid-ambiguity-support-spectra-for-primitive-three-tap-c--4fe8e5c0fab7 .
