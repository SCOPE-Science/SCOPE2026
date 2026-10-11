# Exact half-energy multiplicities for hemispherical spherical Slepian concentration with arbitrary degree masks
## Finding
Let \(\Lambda\subset\mathbb N_0\) be any finite nonempty set of spherical-harmonic degrees on \(S^2\). Write
\[
\mathcal S_\Lambda=\bigoplus_{\ell\in\Lambda}\mathcal H_\ell,
\qquad
C_{\Lambda,H}=P_\Lambda 1_H P_\Lambda\big|_{\mathcal S_\Lambda},
\]
where \(H\) is a hemisphere and \(P_\Lambda\) is orthogonal projection onto \(\mathcal S_\Lambda\). Put \(M=\max\Lambda\). For every \(0\le m\le M\), define
\[
e_m=\#\{\ell\in\Lambda:\ell\ge m,\ \ell+m\equiv0\pmod2\},\qquad
o_m=\#\{\ell\in\Lambda:\ell\ge m,\ \ell+m\equiv1\pmod2\}.
\]
In either complex signed order-\(m\) block, after placing the two degree parities together, the concentration matrix has the exact form
\[
D_m=\begin{pmatrix}\tfrac12 I_{e_m}&B_m\\B_m^*&\tfrac12 I_{o_m}\end{pmatrix},
\]
and \(B_m\) has rank \(\min(e_m,o_m)\). Hence the block spectrum is
\[
\left\{\tfrac12+s_{m,j},\tfrac12-s_{m,j}:1\le j\le\min(e_m,o_m)\right\}
\]
together with exactly \(|e_m-o_m|\) copies of \(1/2\), where every \(s_{m,j}>0\). Thus the whole spectrum is symmetric about \(1/2\), and the exact global multiplicity of \(1/2\) is
\[
\mu_\Lambda=|e_0-o_0|+2\sum_{m=1}^{M}|e_m-o_m|.
\]
For the contiguous band \(\Lambda=\{L_0,L_0+1,\ldots,L_1\}\), with \(w=L_1-L_0+1\),
\[
\mu_\Lambda=
\begin{cases}
w,&w\text{ even},\\
L_0+L_1+1,&w\text{ odd}.
\end{cases}
\]
In particular, the classical low-pass space \(\Lambda=\{0,1,\ldots,L\}\) has exactly \(L+1\) half-energy eigenfunctions. Since its dimension is \((L+1)^2\), exactly \(L(L+1)/2\) eigenvalues are strictly above \(1/2\) and exactly the same number are strictly below \(1/2\).

## Assumptions and scope
The sphere carries its usual rotation-invariant area measure, and the concentration eigenvalue of a nonzero \(g\in\mathcal S_\Lambda\) is the fraction of its total \(L^2(S^2)\) energy lying in the hemisphere. The boundary great circle has measure zero, so either closed or open hemispheres give the same operator. The result allows an arbitrary finite degree mask \(\Lambda\), including low-pass, bandpass, and gapped masks. It concerns scalar spherical harmonics on \(S^2\); no claim is made here for spin-weighted, vector, or higher-dimensional spherical harmonics.

## Proof
Fix an order \(m\ge0\). Using complex harmonics, the \(+m\) and \(-m\) blocks are unitarily equivalent, so it is enough to study one of them. Choose normalized colatitudinal factors \(X_{\ell m}(x)\), with \(x=\cos\theta\), so that
\[
2\pi\int_{-1}^{1}X_{\ell m}(x)X_{k m}(x)\,dx=\delta_{\ell k}.
\]
Associated Legendre parity gives
\[
X_{\ell m}(-x)=(-1)^{\ell+m}X_{\ell m}(x).
\]
If \(\ell+m\) and \(k+m\) have the same parity, the product is even. Whole-sphere orthogonality therefore implies
\[
2\pi\int_0^1X_{\ell m}(x)X_{k m}(x)\,dx=\tfrac12\delta_{\ell k}.
\]
Thus same-parity blocks are exactly one half of the identity; all nontrivial coupling is between opposite parities.

For \(\ell+m\) even and \(k+m\) odd, the associated Legendre Sturm--Liouville equations and one integration by parts give the Lagrange identity
\[
2\pi\int_0^1X_{\ell m}(x)X_{k m}(x)\,dx
=
\frac{2\pi X_{\ell m}(0)X'_{k m}(0)}{k(k+1)-\ell(\ell+1)}.
\]
The endpoint term at \(x=1\) vanishes because of the factor \(1-x^2\) in the Sturm--Liouville operator. For the indicated parities, \(X_{\ell m}(0)\ne0\) and \(X'_{k m}(0)\ne0\). Hence, after row and column scaling by nonzero factors, the cross-parity matrix is
\[
\left(\frac{1}{k(k+1)-\ell(\ell+1)}\right)_{\ell,k},
\]
a rectangular Cauchy matrix. Its degree nodes are distinct, so every maximal square Cauchy minor is nonzero. Therefore \(\operatorname{rank}B_m=\min(e_m,o_m)\).

Now write \(D_m=\tfrac12 I+A_m\) with
\[
A_m=\begin{pmatrix}0&B_m\\B_m^*&0\end{pmatrix}.
\]
The nonzero eigenvalues of \(A_m\) are exactly the pairs \(\pm s_{m,j}\), where \(s_{m,j}\) are the nonzero singular values of \(B_m\), and its nullity is \(|e_m-o_m|\). This proves the fixed-order statement. Counting the \(m=0\) block once and every \(m>0\) block twice gives the formula for \(\mu_\Lambda\).

For a contiguous band, before the lower edge \(L_0\) every order sees the same band width, while at and above \(L_0\) it sees a terminal string of consecutive degrees. A consecutive string has parity imbalance one exactly when its length is odd. Summing these imbalances gives \(w\) for even \(w\), and \(L_0+L_1+1\) for odd \(w\). Setting \(L_0=0\) yields \(\mu_\Lambda=L+1\). The remaining low-pass eigenvalues pair about \(1/2\), so the strict-above and strict-below counts are both \(L(L+1)/2\).

## Verification
The proof is exact and uses only parity, spherical-harmonic orthogonality, the associated Legendre Sturm--Liouville equation, and the full-rank formula for Cauchy matrices. A numerical checker independently constructs hemispherical concentration blocks by Gauss--Legendre quadrature for low-pass and randomly gapped degree masks, diagonalizes them, and compares the observed half-energy multiplicities and paired spectra with the theorem. On the packaged checker it reports `VERIFY_OK blocks=1298 lowpass_L=0..40 max_pair_err=5.929e-14 max_half_err=2.176e-14`. These finite computations corroborate the algebra; they are not used as an infinite proof.

## Relationship to prior work
Simons, Dahlen and Wieczorek formulated the spherical Slepian concentration problem, its spectral localization matrix, the Shannon number, and the special commuting operator for polar caps. Their 2004 public version treats the standard low-pass space and does not state the hemispherical parity/Cauchy decomposition or an exact multiplicity law at concentration \(1/2\). A later bandpass implementation by Beggan, Saarimäki, Whaler and Simons explicitly removes low degrees and says the corresponding dimensional changes are straightforward, but it does not derive a hemispherical spectrum or a half-energy multiplicity formula. Ramamoorthi studied an upper-hemisphere spherical-harmonic orthogonality matrix in a Lambertian-image PCA problem and computed low-order examples; that weighted finite-dimensional application does not state the arbitrary-degree-mask Cauchy-rank theorem above.

The present statement is therefore not the known Shannon-number trace identity: it determines the exact eigenspace sitting at the transition value \(1/2\), and for arbitrary masks it depends on order-by-order parity imbalance rather than only on area and total dimension.

## Limitations
No closed forms are asserted for the positive singular values \(s_{m,j}\), so the theorem fixes the exact central multiplicity and the reflection symmetry of the rest of the spectrum but not every individual concentration eigenvalue. The originality search found no covering statement under Slepian, bandpass, hemisphere, parity, associated-Legendre, or Cauchy-matrix formulations; nevertheless, an equivalent linear-algebra observation could exist in specialized approximation, geodesy, computer-vision, or special-function literature under different terminology.

## References
1. F. J. Simons, F. A. Dahlen, and M. A. Wieczorek, “Spatiospectral concentration on a sphere,” arXiv:math/0408424v1, first public 31 August 2004; later SIAM Review. Primary MSC: 42B05.
2. C. D. Beggan, J. Saarimäki, K. A. Whaler, and F. J. Simons, “Spectral and spatial decomposition of lithospheric magnetic field models using spherical Slepian functions,” Geophysical Journal International 193 (2013), 136–148, DOI: 10.1093/gji/ggs122.
3. R. Ramamoorthi, “Analytic PCA Construction for Theoretical Analysis of Lighting Variability in Images of a Lambertian Object,” IEEE Transactions on Pattern Analysis and Machine Intelligence 24 (2002), 1322–1335.
