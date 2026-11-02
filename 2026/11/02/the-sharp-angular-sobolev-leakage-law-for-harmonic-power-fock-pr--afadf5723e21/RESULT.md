# The sharp angular Sobolev leakage law for harmonic power-Fock projections

## Finding
For every real \(\alpha>0\) and every \(a\in L^2(\mathbb T)\), extend the angular function to \(\mathbb C\setminus\{0\}\) by \(a(re^{i\theta})=a(e^{i\theta})\). On the harmonic power-Fock space defined below, let \(P_\alpha\) denote the orthogonal projection, and let \((e_j)_{j\in\mathbb Z}\) be its normalized angular basis. Define the nonnegative, finite truncated leakage
\[
\mathcal L_N(a)=\sum_{|j|\le N}\|(I-P_\alpha)(a e_j)\|_{L^2(d\mu_\alpha)}^2,\qquad N\ge2.
\]
Writing \(a_m=(2\pi)^{-1}\int_0^{2\pi}a(e^{i\theta})e^{-im\theta}\,d\theta\), the sharp limit is
\[
\boxed{\lim_{N\to\infty}\frac{\mathcal L_N(a)}{\log N}
=\frac1\alpha\sum_{m\in\mathbb Z}m^2|a_m|^2\in[0,+\infty].}
\]
The limit is finite if and only if \(a\in H^1(\mathbb T)\). For those symbols its value is the exact Dirichlet energy \((2\pi\alpha)^{-1}\int_0^{2\pi}|a'(e^{i\theta})|^2\,d\theta\), where the derivative is taken with respect to \(\theta\). For \(a\notin H^1\) the normalized leakage tends to \(+\infty\), rather than merely having an unbounded subsequence.

When \(a\in L^\infty(\mathbb T)\) is unimodular, put \(T_a=P_\alpha M_a|_{\mathcal H_\alpha}\) and \(Q_N=\sum_{|j|\le N}|e_j\rangle\langle e_j|\). The identical formula applies to \(\operatorname{tr}\bigl(Q_N(I-T_a^*T_a)Q_N\bigr)/\log N\), so this determines a sharp logarithmic singular-value-defect coefficient for a natural bounded Toeplitz family.

## Assumptions and scope
Fix \(\alpha>0\) and the probability measure
\[
d\mu_\alpha(z)=\frac{\alpha}{2\pi\Gamma(2/\alpha)}e^{-|z|^\alpha}\,dA(z)
\]
on \(\mathbb C\). Let \(\mathcal H_\alpha\) be the space of complex-valued harmonic functions in \(L^2(\mathbb C,d\mu_\alpha)\). By angular Fourier decomposition and regularity at the origin, it has the complete orthonormal basis
\[
e_j(re^{i\theta})=
\left(\frac{\Gamma(2/\alpha)}{\Gamma((2|j|+2)/\alpha)}\right)^{1/2}r^{|j|}e^{ij\theta},\qquad j\in\mathbb Z.
\]
The value of an angular symbol at the origin is immaterial. For each fixed \(j\), the product \(ae_j\) is square-integrable even if \(a\) is not bounded; no globally bounded multiplication or Toeplitz operator is asserted for unbounded \(a\).

## Proof
**Exact angular decomposition.** For \(j,m\in\mathbb Z\), set
\[
W_\alpha(j,m)=
\frac{\Gamma((|j|+|j+m|+2)/\alpha)}{
\sqrt{\Gamma((2|j|+2)/\alpha)\Gamma((2|j+m|+2)/\alpha)}}.
\]
Radial integration and angular orthogonality give
\[
\langle ae_j,e_{j+m}\rangle=a_mW_\alpha(j,m),\qquad
P_\alpha(ae_j)=\sum_{m\in\mathbb Z}a_mW_\alpha(j,m)e_{j+m}.
\]
The gamma-factor square obeys \(0<W_\alpha(j,m)^2\le1\) by Cauchy–Schwarz for radial monomials (equivalently, by log-convexity of \(\Gamma\)). Thus Parseval and Pythagoras yield the *exact*, absolutely convergent, nonnegative identity
\[
\mathcal L_N(a)=\sum_{m\in\mathbb Z}|a_m|^2S_N(m),\qquad
S_N(m)=\sum_{|j|\le N}\bigl(1-W_\alpha(j,m)^2\bigr).
\]
In particular \(S_N(0)=0\). The interchange of the two nonnegative sums follows from Tonelli and needs no boundedness assumption on \(a\).

**One Fourier frequency.** Fix \(m\ne0\). For \(j\) tending to either infinity, set \(p=|j|\), \(q=|j+m|\), and \(x=(2p+2)/\alpha\), \(y=(2q+2)/\alpha\). Then
\[
-\log W_\alpha(j,m)^2
=\log\Gamma(x)+\log\Gamma(y)-2\log\Gamma((x+y)/2).
\]
The midpoint second-difference formula for \(\log\Gamma\), together with \(\psi_1(t)=t^{-1}+O(t^{-2})\) as \(t\to+\infty\), shows that
\[
1-W_\alpha(j,m)^2
=\frac{m^2}{2\alpha|j|}+O_{\alpha,m}(|j|^{-2})
\quad (|j|\to\infty).
\]
There are two infinite angular tails, hence
\[
S_N(m)=\frac{m^2}{\alpha}\log N+O_{\alpha,m}(1),
\qquad \lim_{N\to\infty}\frac{S_N(m)}{\log N}=\frac{m^2}{\alpha}.
\]

**A bound uniform in the Fourier frequency.** For \(|j|\le2|m|\), at most \(4|m|+1\) summands occur and each is at most one. For \(|j|>2|m|\), the same gamma midpoint difference is bounded using the positive trigamma function and
\[
\psi_1(t)=\sum_{k=0}^\infty(t+k)^{-2}\le t^{-1}+t^{-2},\qquad t>0.
\]
Because \(\min(|j|,|j+m|)>|j|/2\) in this range, there exists \(C_\alpha<\infty\), independent of \(j\) and \(m\), such that
\[
0\le1-W_\alpha(j,m)^2\le \frac{C_\alpha m^2}{|j|+1}.
\]
Summation gives the all-frequency majorant
\[
0\le\frac{S_N(m)}{\log N}\le C'_\alpha m^2
\qquad(N\ge2,\ m\in\mathbb Z),
\]
with the zero-frequency case understood as zero.

**Passing from frequencies to arbitrary angular data.** If \(\sum_m m^2|a_m|^2<\infty\), dominated convergence for the nonnegative Fourier series, using the preceding majorant, proves the displayed sharp limit. If this series diverges, Fatou's lemma and the fixed-frequency limit imply
\[
\liminf_{N\to\infty}\frac{\mathcal L_N(a)}{\log N}\ge
\sum_m\frac{m^2}{\alpha}|a_m|^2=+\infty.
\]
This proves the extended-value limit and the \(H^1\) characterization. Standard Parseval for the weak angular derivative identifies the coefficient with the circle Dirichlet energy. If \(|a|=1\) almost everywhere, the operator identity
\[
I-T_a^*T_a=P_\alpha M_{\bar a}(I-P_\alpha)M_a|_{\mathcal H_\alpha}
\]
on \(\mathcal H_\alpha\) gives the stated Toeplitz interpretation.

## Verification
For the Gaussian case \(\alpha=2\) with the single vortex \(a(e^{i\theta})=e^{2i\theta}\), direct evaluation of the gamma ratios gives the exact identity
\[
\mathcal L_N(a)=H_N+H_{N+2}-2,\qquad H_n=\sum_{k=1}^n\frac1k,
\]
for every integer \(N\ge2\). Its leading term \(2\log N\) agrees with the general coefficient \(m^2/\alpha=2\). The exceptional basis index \(j=-1\) has zero leakage, which is included in this identity.

The accompanying standalone standard-library Python program `check_harmonic_fock_leakage.py` checked 1907 finite identities and inequalities, including gamma-factor contraction, exact Gaussian harmonic-number sums, Fourier-sign symmetry, independent radial numerical quadrature, and sample logarithmic remainders. Those checks supplement rather than replace the proof of the infinite-frequency and arbitrary-symbol statements.

## Relationship to prior work
Agbor (2017), especially Lemma 5.5, provides fixed-quasihomogeneous Toeplitz matrix actions in Gaussian pluriharmonic Fock space, furnishing relevant antecedents for a *single Fourier mode*. Fulsche (2019) investigates quantization and essential spectra for pluriharmonic Toeplitz operators. Sun, Du, and Qi (2024) establish radial-symbol spectral decompositions on harmonic Fock space. Zeng, Wang, and Hu (2023) study Schatten classes of Hankel operators on *holomorphic* Fock-type spaces. None of those inspected results states the present exact two-sided harmonic power-Fock \(L^2\)-angular leakage law, its \(H^1\)-if-and-only-if cutoff, or its universal \(1/\alpha\) coefficient. These comparisons do not establish exhaustive historical priority.

## Limitations
The theorem concerns one complex variable, rotationally invariant weights exactly of power-exponential form, and the symmetric spectral cutoff \(|j|\le N\). It does not claim operator boundedness for an arbitrary \(L^2\) angular symbol, a rate uniform over all \(H^1\) symbols, or the same coefficient for arbitrary radial weights. No independent validation or comprehensive priority determination has been performed.

## References
- D. Agbor, *Algebraic Properties of Toeplitz Operators on the Pluri-harmonic Fock Space*, Journal of Mathematics Research **9** (2017), 67ff., DOI: `10.5539/jmr.v9n6p67`; online October 26, 2017.
- R. Fulsche, *Toeplitz operators on pluriharmonic function spaces: Deformation quantization and spectral theory*, arXiv:`1901.02644` (first posted January 9, 2019), later Integral Equations and Operator Theory **91** (2019).
- H. Sun, J. Du, and J. Qi, *Toeplitz Operators on Harmonic Fock Spaces with Radial Symbols*, Mathematics **12** (2024), 565, DOI: `10.3390/math12040565`; published February 13, 2024.
- Z. Zeng, X. Wang, and Z. Hu, *Bounded, compact and Schatten class Hankel operators on Fock-type spaces*, arXiv:`2311.15464`; first posted November 27, 2023.
