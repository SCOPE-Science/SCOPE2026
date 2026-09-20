# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The proof was checked against the exact trace-defect identity used in
arXiv:2609.12226 and against the hypotheses of its upper-bound theorem.

The self-similar construction has parameters
\[
\alpha=1-\theta,\qquad r=b^{-1/\alpha},\qquad
g=\frac{1-br}{b-1},
\]
with \(b\) chosen so that \((2b-1)r\le1\). This gives \(g\ge r\), which is
the inequality needed to fit a translated length-\(h\) source piece inside
every selected odd-level gap when \(r^n\ge h\). The endpoint-density lemma
uses two successive gap generations, which have opposite colors and lengths
bounded below by a fixed multiple of the inspected endpoint interval. The
count of level-\(n\) gaps and \(b=r^{-(1-\theta)}\) then give the lower
\(h^\theta\) translation law. The upper law follows from the boundary
neighborhood estimate.

The Fourier-annulus lemma was checked directly from Parseval:
\[
|E\triangle(E-h)|
=
\sum_k |e^{2\pi ikh}-1|^2|\widehat{\mathbf1_E}(k)|^2.
\]
The upper translation law controls each dyadic Fourier shell. At \(h=1/L\),
the low-frequency contribution is
\(O(a^{2-\theta}L^{-\theta})\), while the high-frequency tail is
\(O(B^{-\theta}L^{-\theta})\). Choosing \(a\) small and \(B\) large leaves
a fixed proportion of the lower translation mass in the middle annulus.

For discretization, the grid-cell approximation differs from \(E_\theta\)
only in cells meeting the boundary, so its \(L^1\) error is
\(O(N^{-\theta})\). The symmetric-difference metric then transfers the
continuous lower translation law to
\[
\#(\Omega_{\theta,N}^{(1)}
\triangle(\Omega_{\theta,N}^{(1)}-k))
\gtrsim N^{1-\theta}|k|^\theta
\]
once \(|k|\) exceeds a fixed constant and remains \(O(N)\).

The three trace lower bounds use nonnegative terms in the exact trace
identity, so no cancellation issue occurs. On the critical line, disjoint
geometric Fourier annuli each contribute \(N^{d-\theta}\), producing the
logarithm. For \(\gamma>\eta\), a single annulus at frequency scale
\(L\asymp N\) gives \(N^{d-\eta}\). For \(\gamma<\eta\), a fixed nonzero
Fourier mode gives \(N^{d-\gamma}\). Tensoring with full torus factors in
frequency and interval lattice factors in space contributes precisely
\(N^{d-1}\).

The endpoint \(\theta=1\) is covered separately by an interval, for which
the translation law is linear. No empirical computation is used as a
substitute for the proof.

## Originality

**PASS, to the best of our knowledge.**

The closest source is Azita Mayeli, arXiv:2609.12226. Its theorem supplies
the upper regimes
\[
R^{d-\gamma}\log R\quad(\gamma=\eta),\qquad
R^{d-\eta}\quad(\gamma>\eta),\qquad
R^{d-\gamma}\quad(\gamma<\eta).
\]
The source proves sharpness of the logarithm for the box case
\(\gamma=\eta=1\). Its Remark 9.4 explicitly leaves open whether the
logarithm is sharp for every \(0<\gamma=\eta<1\), and whether the two
off-critical powers are sharp. The paper also includes numerical experiments
for particular self-similar examples, but those are presented as numerical
evidence rather than proofs of the general lower bounds.

Searches covered the source identifier and title, "trace defect" with
Cantor/fractal boundaries, discrete Fourier concentration with translation
seminorms, Fourier concentration plunge-region sharpness, and equivalent
phrasing in terms of symmetric-difference moduli and Fourier shell energy.
No prior theorem was located that yields the explicit all-exponent
construction and all three two-sided growth regimes.

Marceca--Romero--Speckbacher, *Eigenvalue estimates for Fourier
concentration operators on two domains*, ARMA 248 (2024), was inspected as
the main earlier concentration-operator comparison. It treats regular
geometric boundaries and non-asymptotic spectral deviation, not the
fractional Cantor sharpness statement here.

The direct source is very recent, so unindexed concurrent work is a genuine
residual risk. No inaccessible paper was identified whose known statement
is specifically likely to imply the all-exponent theorem. Older
Landau--Widom/Slepian theory concerns smooth interval-type concentration and
does not by itself settle the fractional translation-exponent regimes.

## Value

**PASS.**

The result closes every growth-rate sharpness question posed in the direct
source's Remark 9.4, including a continuum of previously open critical
exponents. It also gives a reusable analytic mechanism connecting exact
indicator translation moduli, annular Fourier energy, and lattice
translation lower bounds. The same explicit family simultaneously realizes
the prescribed spatial and spectral exponents, rather than exploiting a
smoother example relabeled with a weaker exponent.

## Limitations

The statement is a sharpness theorem for growth rates, not an exact
asymptotic with leading constant. It does not characterize all extremizing
geometries, does not require connected examples, and does not improve
spectral-threshold dependence. The Cantor coloring is highly disconnected.
No independent validation or formal proof-assistant verification is claimed.
