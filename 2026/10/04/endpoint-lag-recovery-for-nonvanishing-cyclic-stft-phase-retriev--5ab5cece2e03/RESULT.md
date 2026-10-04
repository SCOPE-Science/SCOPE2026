# Endpoint-lag recovery for nonvanishing cyclic STFT phase retrieval
## Finding
Let \(d\ge 3\) be odd, let \(1\le L<d/2\), and assume
\[
\gcd(d,L)=1.
\]
Let \(g\in\mathbb C^d\) satisfy
\[
\operatorname{supp}g\subseteq\{0,\ldots,L\},\qquad g_0g_L\ne0.
\]
Interior samples of \(g\) may vanish. Define the cyclic short-time Fourier transform by
\[
V_gf(k,\ell)=\sum_{j=0}^{d-1}f_j\overline{g_{j-k}}e^{-2\pi i j\ell/d},
\qquad k,\ell\in\mathbb Z_d.
\]
Then every coordinatewise nonvanishing \(f\in\mathbb C^d\) is determined, up to multiplication by one unimodular scalar, by the full magnitude data \(|V_gf|\).

No condition is required on the zero set of the ambiguity function \(V_gg\), and in particular no nonvanishing condition is required on the discrete Fourier transform of \(|g|^2\).

In fact the data directly recover all cyclic endpoint products
\[
p_k=f_{k+L}\overline{f_k},\qquad k\in\mathbb Z_d,
\]
through
\[
p_k=
\frac{1}{\overline{g_L}g_0}\,
\frac1d\sum_{\ell=0}^{d-1}|V_gf(k,\ell)|^2e^{2\pi iL\ell/d}.
\]
These products alone determine \(f\) up to global phase.

## Assumptions and scope
All indices are modulo \(d\). The support condition is normalized to the interval \(\{0,\ldots,L\}\); translating the window gives the equivalent translated statement. The strict inequality \(L<d/2\) prevents wraparound in the endpoint-correlation extraction. The signal is assumed nonzero at every coordinate. The arithmetic hypothesis can equivalently be written \(\gcd(d,2L)=1\).

The theorem is a signal-class result, not a claim that such a window retrieves every signal. It makes no assertion for even \(d\), for \(\gcd(d,L)>1\), or for signals having zeros.

## Proof
Put \(\omega=e^{2\pi i/d}\). For fixed \(k\), expand
\[
|V_gf(k,\ell)|^2
=
\sum_{j,m\in\mathbb Z_d}
 f_j\overline{f_m}\,
 \overline{g_{j-k}}g_{m-k}\,
 \omega^{-(j-m)\ell}.
\]
Taking the \(L\)-th discrete Fourier coefficient in \(\ell\) gives
\[
\frac1d\sum_{\ell=0}^{d-1}|V_gf(k,\ell)|^2\omega^{L\ell}
=
\sum_{j-m\equiv L\pmod d}
 f_j\overline{f_m}\,
 \overline{g_{j-k}}g_{m-k}.
\]
Whenever a summand is nonzero, both \(j-k\) and \(m-k\) lie in \(\{0,\ldots,L\}\). Their ordinary integer difference is therefore in \([-L,L]\). Because \(d>2L\), the congruence \(j-m\equiv L\pmod d\) forces the ordinary equality \(j-m=L\). The only pair in \(\{0,\ldots,L\}^2\) with difference \(L\) is \((L,0)\). Hence
\[
\frac1d\sum_{\ell=0}^{d-1}|V_gf(k,\ell)|^2\omega^{L\ell}
=
 f_{k+L}\overline{f_k}\,\overline{g_L}g_0,
\]
which proves the displayed endpoint-product formula.

Now suppose \(h\in\mathbb C^d\) has the same STFT magnitude as \(f\). Equality of the recovered endpoint products gives
\[
h_{k+L}\overline{h_k}=f_{k+L}\overline{f_k}
\quad\text{for every }k\in\mathbb Z_d.
\]
The right side is nonzero, so \(h\) is also coordinatewise nonvanishing. Set
\[
r_k=\frac{h_k}{f_k}.
\]
Then
\[
r_{k+L}\overline{r_k}=1.
\]
Applying this relation at \(k+L\) yields
\[
r_{k+2L}=r_k.
\]
Since \(d\) is odd and \(\gcd(d,L)=1\), one has \(\gcd(d,2L)=1\). Thus translation by \(2L\) is a single cycle on \(\mathbb Z_d\), so every \(r_k\) equals one constant \(r\). The preceding relation then gives \(|r|=1\). Therefore \(h=rf\), which is exactly global-phase uniqueness.

There is also a direct reconstruction. Reindex by \(z_n=f_{nL}\) and put \(q_n=p_{nL}=z_{n+1}\overline{z_n}\), with indices modulo \(d\). If \(b_n=|z_n|\), then \(|q_n|=b_{n+1}b_n\). Since \(d\) is odd,
\[
b_0^2=\prod_{n=0}^{d-1}|q_n|^{(-1)^n}.
\]
Choose the positive square root for \(b_0\), fix \(z_0=b_0\), and recursively set
\[
z_{n+1}=\frac{q_n}{\overline{z_n}}.
\]
This reconstructs one representative of the global-phase class.

## Verification
The accompanying `verify.py` checks the endpoint-correlation identity and the explicit reconstruction for every admissible pair \((d,L)\) with odd \(3\le d\le31\), using deterministic nonvanishing test signals and windows whose interiors include zeros. There are \(106\) tested parameter pairs. The script reconstructs the full STFT numerically, takes the stated Fourier coefficient of the squared magnitudes, compares it with \(f_{k+L}\overline{f_k}\), reconstructs the signal from those products, and prints `VERIFY_OK 106`.

The computation is only a finite consistency check. The universal statement follows from the exact orthogonality and cycle argument in the proof.

## Relationship to prior work
Bartusel studies finite cyclic STFT phase retrieval with short windows and explicitly records three nearby regimes: almost every nonvanishing signal is recoverable for a fixed short window; earlier all-signal-on-the-nonvanishing-class results assume a nonvanishing ambiguity row such as \(\{0\}\times\mathbb Z_d\); and the paper's own short-window theorem treats separated sparse signals. The full text also emphasizes the problem of weakening ambiguity-support assumptions. The theorem here is different: for odd coprime \((d,L)\), it retrieves every nonvanishing signal from every endpoint-nonzero short window, even when the zero-lag ambiguity row has zeros and even when interior window samples vanish.

Eldar--Sidorenko--Mixon--Barel--Cohen prove recovery of arbitrary nonvanishing signals under additional window conditions. Jaganathan--Eldar--Hassibi prove an almost-everywhere nonvanishing-signal statement for fixed short windows. Li--Cheng--Han--Sun--Shi give related sufficient rank conditions. None of the inspected statements gives the endpoint-only odd-cycle criterion above.

A 2026 preprint of Bartusel gives new sufficient conditions in terms of how much of the window ambiguity function is nonzero. Its accessible abstract does not state the endpoint-only result; because only its abstract was available for this comparison, it remains a residual literature risk rather than evidence of noncoverage.

## Limitations
The proof uses coordinatewise nonvanishing of the signal essentially when ratios are formed. The criterion is sufficient, not claimed necessary. Even-dimensional cycles and noncoprime \((d,L)\) can carry additional degrees of freedom at the endpoint-product level, and the theorem does not classify whether other ambiguity rows remove them. No stability estimate is proved; the alternating product used for magnitude reconstruction may be poorly conditioned in noise.

## References
1. D. Bartusel, "Injectivity Conditions for STFT Phase Retrieval on \(\mathbb Z\), \(\mathbb Z_d\) and \(\mathbb R^d\)," arXiv:2206.06729, first posted 14 June 2022; Journal of Fourier Analysis and Applications 29 (2023), article 53.
2. Y. C. Eldar, P. Sidorenko, D. G. Mixon, S. Barel, O. Cohen, "Sparse Phase Retrieval from Short-Time Fourier Measurements," IEEE Signal Processing Letters 22 (2015), 638--642.
3. K. Jaganathan, Y. C. Eldar, B. Hassibi, "STFT Phase Retrieval: Uniqueness Guarantees and Recovery Algorithms," IEEE Journal of Selected Topics in Signal Processing 10 (2016), 770--781.
4. L. Li, C. Cheng, D. Han, Q. Sun, G. Shi, "Phase Retrieval from Multiple-Window Short-Time Fourier Measurements," IEEE Signal Processing Letters 24 (2017), 372--376.
5. D. Bartusel, "Uncertainty Principles as a Tool for STFT Phase Retrieval," arXiv:2605.31507 (2026).
