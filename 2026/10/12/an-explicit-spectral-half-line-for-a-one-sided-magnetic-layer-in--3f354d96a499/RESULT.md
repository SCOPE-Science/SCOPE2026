# An explicit spectral half-line for a one-sided magnetic-layer interface

## Finding

For every constant magnetic field \(B>0\) and every pair of widths \(d_1,d_2>0\), the one-sided, Dirichlet-screen magnetic double layer has a spectral half-line, with an explicit cutoff depending only on these three parameters. In particular its spectrum has **only finitely many bounded open gaps**, whether the widths are commensurate or not.

Put \(L=d_1+d_2\), \(W=(L,d_1,d_2)\), and define
\[
K=\sum_{w\in W}\left(\frac{w}{\pi}+\frac{\pi}{12Bw}\right),\qquad
C=\sum_{w\in W}\frac{\pi^2}{12Bw^2},\qquad
A=K+\frac{L}{\pi},\qquad Q=C+\frac{L\sqrt{2B}}{\pi}.
\]
Let
\[
t_*=2B\left(A+\sqrt{A^2+Q/B}\right),\qquad
n_0=\min\left\{n\in\mathbb N_0:2Bn+\frac{\pi^2}{L^2}>t_*^2\right\},
\qquad E_*=B(2n_0+1)+\frac{\pi^2}{L^2}.
\]
The set defining \(n_0\) is nonempty. The assertion is
\[
\boxed{[E_*,\infty)\subseteq\sigma(H).}
\]
The cutoff is sufficient, not asserted optimal.

## Assumptions and scope

In coordinates \((x,y,z)\), take the full layer of transverse width \(L\) and remove the half-plane screen
\[
\Omega=\big(\mathbb R^2\times(-d_1,d_2)\big)
\setminus \{(x,y,0):x\ge0,\ y\in\mathbb R\}.
\]
The self-adjoint magnetic Dirichlet Laplacian is associated with the closed magnetic form of
\[
H=-\partial_x^2+(-i\partial_y+Bx)^2-\partial_z^2
\]
with Dirichlet trace on the two outside faces and on both faces of the half-plane screen. The screen is absent on \(x<0\) and separates the two layers on \(x>0\). There is no electric potential, periodic structure, or finite-width aperture. The magnetic field \(B\) is perpendicular to the layers and is homogeneous.

For \(w>0\), let \(N_w(E)\) count, with multiplicity of quantum-number labels, the values
\[
B(2n+1)+\left(\frac{\pi m}{w}\right)^2\le E,
\qquad n\in\mathbb N_0,\quad m\in\mathbb N.
\]
The limiting merged-strip and divided-strip counts are respectively
\[
N_{\rm m}(E)=N_L(E),\qquad N_{\rm d}(E)=N_{d_1}(E)+N_{d_2}(E).
\]
All equations below are valid also when these numerical energies coincide: multiplicities are never discarded.

## Proof

### Continuous fiber curves and limiting edges

Fourier transformation along the translation-invariant \(y\)-axis decomposes the operator into compact-resolvent fibers
\[
H(p)=-\partial_x^2+(p+Bx)^2-\partial_z^2,\qquad p\in\mathbb R,
\]
with the same Dirichlet-screen form domain for every \(p\). Denote the ordered eigenvalues, repeated according to multiplicity, by \(\lambda_j(p)\), \(j\ge1\). The polynomial dependence on \(p\) is an analytic family of closed forms, so each ordered eigenvalue is continuous in \(p\). Harmonic-oscillator localization, or Dirichlet–Neumann bracketing at an interface moving to infinity after the shift \(x\mapsto x+p/B\), gives
\[
\lim_{p\to-\infty}\lambda_j(p)=E_j^{\rm m},\qquad
\lim_{p\to+\infty}\lambda_j(p)=E_j^{\rm d},
\]
where \((E_j^{\rm m})_{j\ge1}\) is the nondecreasing list of the width-\(L\) levels and \((E_j^{\rm d})_{j\ge1}\) is the nondecreasing **union** of the two width-\(d_i\) level lists. This is the ordered-eigenvalue version of the asymptotic bracketing in Section 4 of Exner [1]. The limits hold with degeneracies because the min–max labels remain ordered. Form inclusion also implies \(E_j^{\rm m}\le\lambda_j(p)\le E_j^{\rm d}\).

By continuity and the limiting values, the closure of each fiber-curve range includes the whole interval \([E_j^{\rm m},E_j^{\rm d}]\). The spectrum of the direct integral contains this closed interval: a finite fiber parameter with a nearby eigenvalue produces a positive-measure set of approximately spectral fibers, and the limit endpoints belong to the closed spectrum.

### A quantitative counting lemma

For \(E\ge B\) set \(t=w\sqrt{E-B}/\pi\), \(c=\pi^2/(2Bw^2)\), and \(M=\lfloor t\rfloor\). Counting the oscillator labels first gives the exact identity
\[
N_w(E)=\sum_{m=1}^{M}\left(1+\left\lfloor c(t^2-m^2)\right\rfloor\right).
\]
Write \(t=M+\delta\) with \(0\le\delta<1\) and use the sum of the first \(M\) squares. The fractional-part remainder \(\varepsilon\) satisfies \(0\le\varepsilon\le M\), and
\[
N_w(E)=c\left(\frac23t^3-\frac12t^2\right)
+c\left[t\left(\delta-\delta^2-\frac16\right)+\frac{\delta^3}{3}-\frac{\delta^2}{2}+\frac\delta6\right]+\varepsilon.
\]
Since \(\left|\delta-\delta^2-1/6\right|\le1/6\), \(\left|\delta^3/3-\delta^2/2+\delta/6\right|\le1/6\), and \(M\le t\), this yields the rigorous, uniform estimate
\[
\left|N_w(E)-\frac{w}{3\pi B}(E-B)^{3/2}+\frac{E-B}{4B}\right|
\le\left(\frac{w}{\pi}+\frac{\pi}{12Bw}\right)\sqrt{E-B}+\frac{\pi^2}{12Bw^2}.
\tag{1}
\]
The linear correction is independent of \(w\); the leading cubic-root powers cancel when the merged count is compared with the sum of the two divided counts. Consequently, writing \(t=\sqrt{E-B}\), one obtains
\[
N_{\rm m}(E)-N_{\rm d}(E)\ge\frac{t^2}{4B}-Kt-C.
\tag{2}
\]
The exact Landau-step identity, valid for every \(E\ge B\), is
\[
N_w(E+2B)-N_w(E)=\left\lfloor\frac{w\sqrt{E+B}}{\pi}\right\rfloor.
\tag{3}
\]
Indeed, for each transverse mode with \((\pi m/w)^2\le E+B\), increasing the energy by \(2B\) admits exactly one further Landau index, including those modes newly entering the count; other modes contribute zero. Equations (2) and (3), followed by \(\sqrt{t^2+2B}\le t+\sqrt{2B}\), imply
\[
N_{\rm m}(E)-N_{\rm d}(E+2B)
\ge\frac{t^2}{4B}-At-Q.
\tag{4}
\]
The right-hand side is strictly positive whenever \(t>t_*\), by the stated explicit quadratic root.

### Covering the high-energy axis

For each integer \(n\ge n_0\) put
\[
x_n=B(2n+1)+\left(\frac{\pi}{L}\right)^2,
\qquad j_n=N_{\rm m}(x_n).
\]
By definition of \(j_n\), the \(j_n\)-th merged energy equals \(x_n\), including all degeneracies. Since \(\sqrt{x_n-B}>t_*\), inequality (4) gives
\[
N_{\rm d}(x_n+2B)<j_n,
\quad\text{and therefore}\quad E_{j_n}^{\rm d}>x_n+2B.
\]
The continuous fiber curve with index \(j_n\) has limits \(x_n\) and a value strictly exceeding \(x_n+2B\); its spectral band thus contains \([x_n,x_n+2B]\). These intervals meet exactly because \(x_{n+1}=x_n+2B\), hence cover \([x_{n_0},\infty)=[E_*,\infty)\).

Lastly, for any finite upper energy \(R\), the uniform lower bound \(\lambda_j(p)\ge E_j^{\rm m}\) leaves only finitely many indices \(j\) with any spectral values below \(R\). Each such fiber-curve range closes to a single interval. Thus the spectrum below the explicit cutoff is a finite union of closed intervals; together with the proved half-line this leaves finitely many bounded open complementary components.

## Verification

The standalone standard-library script `verify.py` checks the polynomial identity underpinning (1) using exact rational multivariate polynomial arithmetic. It then checks exact rational floor-count examples for (1) and (3), followed by independent numerical examples of the explicit sufficient cutoff; a test with \(B=1\), \(d_1=1\), and \(d_2=2\) returns \(n_0=99\). Execute `python3 verify.py` and require `VERIFY_OK`.

The infinite-energy theorem depends on the displayed algebra, counting bounds and fiber continuity; finite tests and the numerical sample do not prove an asymptotic assertion. Neither the source's printed dispersion sketches nor unverified external computations are needed.

## Relationship to prior work

Exner [1, Section 4, Theorem 4.1] identifies the one-sided barrier, its absolutely continuous/flat bands, their asymptotic levels, and a sufficient condition for an open low-energy gap. It does not state a universal finite-gap theorem or an explicit high-energy covering threshold. The result here uses the same limiting spectral families but adds the uniform two-term counting estimate (1), the exact one-Landau-step increment (3), and the overlap argument (4). Exner, Kalvoda and Tušek [2] study a different geometric magnetic layer and asymptotic fiber spectral behavior, not the present split-versus-merged Dirichlet screen. The finite-gap results of Borisov [3] concern periodic perturbations of planar strips, whereas the present barrier is a one-sided, nonperiodic magnetic interface.

## Limitations

The cutoff is deliberately conservative and need not locate the last actual open gap. No count or exact positions of possible low-energy gaps are provided. The conclusion is a **spectral** half-line, not a claim of a uniform lower bound on density of states, transport speed, or spectral multiplicity. The theorem assumes homogeneous nonzero normal field, two fixed positive Dirichlet widths, and an ideal one-sided straight screen; it is not proved for finite windows, curved screens, potential disorder, or varying fields. Weakly indexed equivalent proofs and possible differences in later publisher versions are residual literature risks.

## References

1. Pavel Exner, *Magnetic transport in laterally coupled layers*, arXiv:2207.01252v1 (first submitted 4 July 2022), Section 4 and Theorem 4.1; *Physica Scripta* 97 (2022), 104004, DOI:10.1088/1402-4896/ac925e. Full preprint: https://arxiv.org/abs/2207.01252 ; author-posted full text: https://web.ma.utexas.edu/mp_arc/c/22/22-33.pdf .
2. Pavel Exner, Tomáš Kalvoda, and Matěj Tušek, *A geometric Iwatsuka type effect in quantum layers*, arXiv:1701.05714, *Journal of Mathematical Physics* 59 (2018), 042105, DOI:10.1063/1.5030517.
3. D. I. Borisov, *Bethe-Sommerfeld conjecture for periodic Schrödinger operators in strip*, arXiv:1806.09292, https://arxiv.org/abs/1806.09292 .
