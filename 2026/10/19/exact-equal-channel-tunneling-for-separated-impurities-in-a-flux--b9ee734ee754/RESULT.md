# Exact equal-channel tunneling for separated impurities in a flux-threaded diamond chain

## Finding

Let two identical, weak, positive onsite impurity pairs be placed on plaquettes separated by an integer \(d\ge2\) in an infinite, uniformly flux-threaded diamond chain. For every flux \(0<\phi<\pi\), the four nonzero eigenvalues of the *exact flat-band compression* of the unit-strength impurity operator are
\[
\mu_{\sigma,\tau}=\frac12+\sigma h_d+\tau\sqrt{\frac{r^2}{4}+h_d^2},\qquad \sigma,\tau\in\{-1,+1\},
\]
where
\[
r=\exp[-\operatorname{arcosh}(\sec(\phi/2))],\qquad h_d=\frac{1-r^2}{4}r^{d-1}.
\]
Consequently, each of the two separated upper and lower impurity doublets has exactly the same compressed splitting \(2h_d\). For the physical Hamiltonian with onsite strength \(\varepsilon>0\), each doublet has leading splitting \(2\varepsilon h_d+O(\varepsilon^2)\), so that its effective half-splitting is
\[
 t_{\pm}(d,\varepsilon)=\frac{\varepsilon}{4}(1-r^2)r^{d-1}+O(\varepsilon^2),\qquad \varepsilon\downarrow0.
\]
The leading coupling ratio for separations \(d_1,d_2\ge2\) is \(r^{d_1-d_2}\). In particular, at \(\phi=\pi/2\), the ratio for separations eight and six is exactly \(3-2\sqrt2\approx0.171572875\). The equality of the two channels is an exact property of the flat-band compression and a first-order statement for the full diamond Hamiltonian, **not** an identity for nonzero finite-strength physical eigenvalue splittings.

## Assumptions and scope

The one-particle Hilbert space is \(\ell^2(\mathbb Z)\otimes\mathbb C^3\), with orthonormal cell sites \(A_j,B_j,C_j\). Fix \(J>0\), \(0<\phi<\pi\), and impose the following nonzero hopping matrix elements, together with their Hermitian conjugates:
\[
\langle A_{j-1}|H_0|B_j\rangle=Je^{-i\phi/2},\quad
\langle A_{j-1}|H_0|C_j\rangle=J,\quad
\langle A_j|H_0|B_j\rangle=J,\quad
\langle A_j|H_0|C_j\rangle=Je^{-i\phi/2}.
\]
All onsite terms of \(H_0\) vanish. Define the orthogonal projection \(P\) onto \(\ker H_0\), and the unit-strength positive onsite perturbation
\[
W_d=|B_0\rangle\langle B_0|+|C_0\rangle\langle C_0|+|B_d\rangle\langle B_d|+|C_d\rangle\langle C_d|.
\]
The physical model is \(H_\varepsilon=H_0+\varepsilon W_d\). The unperturbed bands are \(0\) and \(\pm 2J\sqrt{1+\cos(k)\cos(\phi/2)}\), so \(0\) is a spectrally isolated flat band, with gap \(2J\sqrt{1-\cos(\phi/2)}>0\). Thus the four small nonzero eigenvalues are unambiguously counted near zero for sufficiently small \(\varepsilon\) at fixed \(J,\phi,d\); other zero flat-band states remain at zero.

## Proof

**1. Flat-band basis and exact inverse Gram kernel.** The compact localized states
\[
|\ell_j\rangle=\frac12\bigl(|B_j\rangle-e^{-i\phi/2}|C_j\rangle+e^{-i\phi/2}|B_{j+1}\rangle-|C_{j+1}\rangle\bigr)
\]
are annihilated by \(H_0\). Their infinite Gram operator is the positive invertible Toeplitz matrix
\[
S_{ij}=\langle\ell_i|\ell_j\rangle=\delta_{ij}+s(\delta_{i,j+1}+\delta_{i,j-1}),\quad
s=\frac12\cos(\phi/2)=\frac{r}{1+r^2}.
\]
Its Fourier symbol is \(1+2s\cos k>0\), and the zero-energy fiber is one-dimensional; hence these states constitute a Riesz basis of the zero band. Solving the recurrence \(sG_{n-1}+G_n+sG_{n+1}=\delta_{n0}\) with decay at infinity yields
\[
 (S^{-1})_{ij}=\frac{1+r^2}{1-r^2}(-r)^{|i-j|}.
\]
The solution follows since the decaying characteristic root is \(-r\), and its central normalization is \((1+r^2)/(1-r^2)\).

**2. Four-coordinate reduction.** Only the four compact states indexed by \(I=(-1,0,d-1,d)\) have nonzero matrix elements of \(W_d\). Their impurity Gram matrix \(V_I=(\langle\ell_i|W_d|\ell_j\rangle)_{i,j\in I}\) is the direct sum of two identical blocks
\[
B=\begin{pmatrix}1/2&s\\s&1/2\end{pmatrix}.
\]
Because the flat-band projector in this Riesz basis is \(P=L S^{-1}L^*\), the four nonzero eigenvalues of \(PW_dP\) coincide with those of the positive Hermitian matrix \(V_I^{1/2}(S^{-1})_{I,I}V_I^{1/2}\) (the nonzero spectra of \(XY\) and \(YX\) coincide). After passing separately in each impurity pair to symmetric and antisymmetric coordinates, this matrix is unitarily equivalent to
\[
M=\begin{pmatrix}
(1+r)/2&0&-t&-t\\
0&(1-r)/2&t&t\\
-t&t&(1+r)/2&0\\
-t&t&0&(1-r)/2
\end{pmatrix},\qquad t=(-1)^dh_d.
\]
All entries follow by multiplying the four explicit entries of the inverse Gram kernel by the two square roots of \(B\). A direct determinant calculation gives
\[
\det(xI-M)=\left[(x-\tfrac12)^2-\tfrac{r^2}{4}\right]^2-4t^2(x-\tfrac12)^2.
\]
Factoring into the two quadratics \((x-\tfrac12)^2-\tfrac{r^2}{4}\pm2t(x-\tfrac12)\), and solving yields the claimed four values \(\frac12\pm h_d\pm\sqrt{r^2/4+h_d^2}\). For \(0<r<1\) and \(d\ge2\), they are positive and distinct, and the difference between the two values with a common sign on the square root is exactly \(2h_d\).

**3. Physical weak-impurity eigenvalues.** The gap around zero and the finite rank of \(W_d\) permit a Riesz-spectral-projection/Feshbach perturbation reduction. Its leading finite-rank effective operator is \(\varepsilon PW_dP\), while the remainder has operator norm \(O(\varepsilon^2)\) for fixed \(J,\phi,d\). Hence precisely four nonzero eigenvalues bifurcate from the isolated zero flat band and satisfy \(\lambda_{\sigma,\tau}(\varepsilon)=\varepsilon\mu_{\sigma,\tau}+O(\varepsilon^2)\). The two branch splittings therefore have identical first derivatives \(2h_d\). Finally, at quarter-turn flux \(\cos(\phi/2)=1/\sqrt2\), giving \(r=\sqrt2-1\), so the ratio for \(d_1=8,d_2=6\) is \(r^2=3-2\sqrt2\).

## Verification

Run `python VERIFY.py` with NumPy and SymPy. It constructs the physical nearest-neighbor Hamiltonian independently of the closed formula, checks compact-state annihilation and overlap, symbolically factors the \(4\times4\) characteristic polynomial, compares six finite-chain compressed spectra to the infinite-volume prediction, and checks twelve small-strength full-chain spectra. The finite-chain comparisons are numerical diagnostics; the all-size and infinite-volume conclusions come from the preceding proof. A run reproduced the ratio \(0.171572875254\) and reported that all diagnostic checks passed. The finite sections have distant boundaries; their discrepancies vanish exponentially as those boundaries are moved outward.

## Relationship to prior work

Viedma, Marques, Dias, and Ahufinger (arXiv:2407.15789, first posted July 22, 2024) introduced the flux-controlled impurity-decorated diamond chain and demonstrated effective SSH-like systems. In their Appendix A they investigated the gap between *two separated impurity pairs* numerically, observed exponential distance dependence, and noted that the upper and lower branch couplings are approximately equal. The present result analytically identifies the exact projected four-level characteristic polynomial, the explicit distance-dependent prefactor, and the precise reason the two projected channels have equal splitting. Its quarter-flux ratio recovers their quoted numerical value near \(0.17\), but the source does not state this exact ratio or the four-eigenvalue theorem. Marques, Viedma, Ahufinger, and Dias (arXiv:2407.14405, first posted July 19, 2024) developed the flat-band projection framework and the single-impurity-pair eigenvalues. Those are recovered in the infinite-separation limit; they do not determine the joint finite-separation four-level spectrum. The derivation uses this established framework but answers a distinct two-impurity comparison left numerical in the later paper.

## Limitations

The theorem applies to an infinite, translation-invariant, one-particle Hermitian diamond chain, two identical real positive impurity pairs, integer separation \(d\ge2\), fixed \(0<\phi<\pi\), and first order in impurity strength for the physical spectrum. It does not assert equality of the two full-chain splittings at finite \(\varepsilon\), finite-volume exactness, many-body interactions, a uniform small-flux or large-separation expansion, or a rigorous bound on transport or topological protection. The numerical diagnostics do not replace the analytic derivation. A related 2024 doctoral thesis was located in an index but its complete relevant section was not accessible in this examination; it remains a priority-comparison risk.

## References

1. D. Viedma, A. M. Marques, R. G. Dias, and V. Ahufinger, “Flux-mediated effective Su–Schrieffer–Heeger model in an impurity decorated diamond chain,” arXiv:2407.15789v1 (July 22, 2024), especially Sec. II and Appendix A; later APL Photonics **9**, 120801 (2024). https://arxiv.org/abs/2407.15789 ; https://pubs.aip.org/aip/app/article/9/12/120801/3325099/Flux-mediated-effective-Su-Schrieffer-Heeger-model
2. A. M. Marques, D. Viedma, V. Ahufinger, and R. G. Dias, “Impurity flat band states in the diamond chain,” arXiv:2407.14405v1 (July 19, 2024), especially the analysis of one impurity pair. https://arxiv.org/abs/2407.14405
