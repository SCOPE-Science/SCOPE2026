# Sharp one- and two-site phase retrieval for three-mode periodic Schrödinger waves

## Finding

**Theorem (arithmetic resonance, minimal site count, and exact demixing stability).** Fix three known, distinct nonnegative integers \(k_0<k_1<k_2\). For nonzero complex coefficients \(a_0,a_1,a_2\), define the free periodic Schrödinger wave
\[
u(x,t)=\sum_{j=0}^{2}a_j e^{i(k_j x-k_j^2t)},\qquad (x,t)\in(\mathbb R/2\pi\mathbb Z)^2.
\]
At any prescribed spatial site, continuously observe \(I_x(t)=|u(x,t)|^2\) during one complete time period. Define \(d_1=k_1^2-k_0^2>0\) and \(d_2=k_2^2-k_1^2>0\).

1. If \(d_1\ne d_2\), one spatial site determines all three coefficients modulo their common unimodular phase, for **every** nonzero complex coefficient vector.
2. If \(d_1=d_2\), equivalently \(k_0^2+k_2^2=2k_1^2\), no single site is universally phase retrieving on this class. Its one-site measurement fiber has at most four global-phase classes, and four classes really occur for a nonempty open set of coefficient vectors. In particular, the four triples \((6,-5,1)\), \((3,-7,2)\), \((2,-7,3)\), \((1,-5,6)\) give exactly the same one-site intensities at \(x=0\) for \((k_0,k_1,k_2)=(1,5,7)\).
3. In the resonant case, two spatial sites separated by \(h\) determine every nonzero coefficient vector modulo common phase **if and only if**
\[
e^{i(k_2-2k_1+k_0)h}\ne1.
\]
Thus two is the exact minimum number of sites for universal retrieval in the resonant case. Define \(\Delta=k_2-2k_1+k_0\ne0\). The two-by-two linear map demixing the colliding temporal Fourier coefficient has sharp Euclidean singular values
\[
\sigma_\pm(h)=\sqrt{2\pm2|\cos(\Delta h/2)|}.
\]
Its spectral condition number is minimized to \(1\) precisely when \(\Delta h\equiv\pi\pmod{2\pi}\), and diverges at \(\Delta h\equiv0\pmod{2\pi}\). At each singular site separation \(h_0\),
\[
\|M_h^{-1}\|_2\sim\frac{2}{|\Delta|\,|h-h_0|}\qquad(h\to h_0,\ h\ne h_0).
\]
The singular-value and inverse-norm statements concern **the linear product-demixing step**, not the global Lipschitz constant for recovery when some input coefficients tend to zero.

## Assumptions and scope

The spectrum of three distinct nonnegative integer wave numbers is known. All three coefficients are nonzero, their values are unknown, and the measurement at each site is the entire real-valued intensity function of time over a complete period \(2\pi\), including its time origin. Spatial locations are known modulo \(2\pi\). The only equivalence in reconstruction is multiplying all coefficients by a single unit-modulus complex number. There are no bounded-noise or discrete-time sampling claims. The periodic wave solves \(i\partial_tu+\partial_x^2u=0\).

## Proof

**Step 1: Temporal Fourier coefficients.** Define
\[
\widehat I_x(n)=\frac1{2\pi}\int_0^{2\pi}I_x(t)e^{int}\,dt.
\]
Orthogonality gives \(\widehat I_x(0)=\sum_{j=0}^2|a_j|^2\), and at positive integers \(n\),
\[
\widehat I_x(n)=\sum_{0\le i<j\le2:\,k_j^2-k_i^2=n}a_j\overline{a_i}e^{i(k_j-k_i)x}.
\]
The positive gaps are exactly \(d_1,d_2,d_1+d_2\). Hence their only possible collision is \(d_1=d_2\).

**Step 2: Isolated gaps imply universal one-site recovery.** Fix a site \(x_0\), put \(b_j=a_je^{ik_jx_0}\), and let \(p=b_1\overline b_0\), \(q=b_2\overline b_1\), \(r=b_2\overline b_0\). In the nonresonant case these products are individually measured as \(\widehat I_{x_0}(d_1)=p\), \(\widehat I_{x_0}(d_2)=q\), and \(\widehat I_{x_0}(d_1+d_2)=r\). Since all coefficients are nonzero, the positive real number \(pq/r=|b_1|^2\) is known. Fix the global phase by requiring \(b_1=\sqrt{pq/r}>0\); then \(b_0=\overline p/b_1\) and \(b_2=q/b_1\). Finally \(a_j=b_je^{-ik_jx_0}\). This proves reconstruction for every input, not merely generically.

**Step 3: Resonant one-site fibers.** If \(d_1=d_2=d\), the intensity at \(x_0\), apart from an irrelevant unit carrier, is the squared modulus of a quadratic polynomial \(P(z)=b_0+b_1z+b_2z^2\) on the unit circle, with \(z=e^{-idt}\). If \(P\) has roots \(r_1,r_2\), the reflected zero pairs in its power spectrum are \(\{r_j,1/\overline{r_j}\}\). Any quadratic spectral factor with the same unit-circle modulus must choose a member of each reflected pair (with multiplicity). These are at most four choices; once roots are chosen, the modulus of the overall scalar is fixed, leaving only common global phase. The upper bound remains true at coincident or unit-circle roots. For distinct nonreciprocal roots off the unit circle and nonzero coefficients in all four factors, all four choices are inequivalent, an open condition. For example \(P(z)=6-5z+z^2=(z-2)(z-3)\) gives the four coefficient triples displayed in the finding; replacing each root by its reciprocal conjugate and multiplying the factor by its modulus preserves \(|P(e^{it})|\). These are genuinely distinct modulo phase. At an arbitrary single site the same example is obtained by incorporating \(e^{-ik_jx_0}\) in the coefficients.

**Step 4: Two-site demixing.** For the resonant case set \(m_1=k_1-k_0\) and \(m_2=k_2-k_1\). They are different: if they were equal, the strict convexity of squares would force \(d_2>d_1\). Relative to \(x_0\), the two measurements at separation \(h\) of the colliding temporal frequency \(d\) are
\[
\begin{pmatrix}\widehat I_{x_0}(d)\\\widehat I_{x_0+h}(d)\end{pmatrix}
=M_h\begin{pmatrix}p\\q\end{pmatrix},\quad
M_h=\begin{pmatrix}1&1\\e^{im_1h}&e^{im_2h}\end{pmatrix}.
\]
Meanwhile \(r=\widehat I_{x_0}(2d)\) is directly known. The determinant of \(M_h\) is \(e^{im_2h}-e^{im_1h}\), so the displayed angular condition is equivalent to recovering \(p,q\). Step 2 reconstructs the signal. When the determinant vanishes, the identity \(e^{im_1h}=e^{im_2h}\) implies, with \(s=m_1h/d\), the exact equality \(u(x_0+h,t)=e^{i(k_0h-k_0^2s)}u(x_0,t-s)\). Hence the second intensity is just a time translate of the first. The fourfold ambiguity in Step 3 therefore persists, proving necessity and minimality.

**Step 5: Optimal separations.** Direct multiplication yields \(M_h^*M_h\) with diagonal entries \(2\) and off-diagonal entry \(1+e^{i(m_2-m_1)h}\). Its eigenvalues are \(2\pm2|\cos((m_2-m_1)h/2)|\). Taking square roots proves the singular-value formula. Both are \(\sqrt2\) exactly at odd half-turns \(\Delta h\equiv\pi\), the unique condition-number minima. At an even half-turn \(\Delta h_0\equiv0\), expansion gives \(\sigma_-(h)\sim |\Delta||h-h_0|/2\), proving the stated inverse norm asymptotic.

## Verification

The self-contained `CHECK.py` reproduces temporal Fourier coefficients by direct quadrature, tests the four explicit ambiguous triples, checks reconstruction from the isolated energy gaps, compares the two-site demixing singular values with independent numerical SVD, and tests the optimal \(h=\pi/2\) separation for the triple \((1,5,7)\). It completes 1,497 comparisons. The all-frequency theorem follows analytically from Steps 1–5, not by extrapolating these tests.

## Relationship to prior work

Pineau–Ramos–Taylor (2026, arXiv:2609.30511) establish continuous full-space mass-density uniqueness for one-dimensional Schrödinger waves on \(\mathbb R\), including broad potentials. Their Theorem A assumes intensity for almost all space-time points; it does **not** supply a one- versus two-point sensor classification for periodic three-mode waves. Jaming–Mayeli (2026, arXiv:2607.26705) give spectral conditions for full-vertex dynamical phase retrieval on finite graphs; their setting and observation geometry differ from the present sparse spatial sensors. Classical polynomial root-reflection ambiguity and sparse Fourier autocorrelation inversion supply established ingredients. The result here combines them into an exact arithmetic transition and a sharp sensor-placement/demixing law for the specified periodic dispersion relation.

## Limitations

The theorem is restricted to known three-mode, nonnegative integer spectral supports with all coefficients nonzero. A single site's full temporal data is required. It does not assert uniform nonlinear reconstruction stability as amplitudes approach zero, minimal finite time samples, higher-mode classifications, or recovery with unknown spectral support. Other earlier works on finite-dimensional dynamical phase retrieval could contain an equivalent specialization, so historical priority requires continued scholarly checking. The fourfold statement is a generic **upper bound with attainability**, not a claim that every resonant signal has four inequivalent factors.

## References

1. B. Pineau, J. P. G. Ramos, M. A. Taylor, *Phase retrieval for Schrödinger evolutions*, arXiv:2609.30511, first submitted 24 September 2026. https://arxiv.org/abs/2609.30511
2. P. Jaming, A. Mayeli, *Dynamical phase retrieval for Schrödinger evolution on finite graphs*, arXiv:2607.26705, first submitted 29 July 2026. https://arxiv.org/abs/2607.26705
3. R. Beinert, G. Plonka, *Sparse phase retrieval of one-dimensional signals by Prony's method*, arXiv:1701.08947 (2017). https://arxiv.org/abs/1701.08947
