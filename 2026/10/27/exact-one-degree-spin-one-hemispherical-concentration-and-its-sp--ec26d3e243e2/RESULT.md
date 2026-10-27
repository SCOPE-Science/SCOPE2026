# Exact one-degree spin-one hemispherical concentration and its spectral gap

## Finding

For every integer \(\ell\ge1\), the north-hemisphere concentration operator on the single-degree spin-one spherical-harmonic space has an explicit complete spectrum, a unique maximizing mode, and a sharp stability gap. More precisely, let \(Z_{\ell m}=\eth Y_{\ell m}/\sqrt{\ell(\ell+1)}\), \(-\ell\le m\le\ell\), with the eth convention specified below. For \(1\le k\le\ell\), define
\[
\Delta_{\ell,k}=\begin{cases}
\dfrac{(2\ell+1)k}{2\ell(\ell+1)}\dfrac{\binom{\ell+k}{(\ell+k)/2}\binom{\ell-k}{(\ell-k)/2}}{4^\ell},&\ell+k\text{ even},\\[2mm]
0,&\ell+k\text{ odd}.
\end{cases}
\]
Set \(\Delta_{\ell,0}=0\). In the ordered basis \(Z_{\ell m}\), the concentration operator has eigenvalues
\[
\boxed{\lambda_{\ell m}=\frac12-\operatorname{sgn}(m)\Delta_{\ell,|m|}.}
\]
Its largest eigenvalue is simple, with the **exact sharp concentration constant**
\[
\boxed{\Lambda_\ell=\frac12+D_\ell,\qquad D_\ell=\frac{2\ell+1}{2(\ell+1)}\frac{\binom{2\ell}{\ell}}{4^\ell},}
\]
attained precisely by nonzero complex scalar multiples of \(Z_{\ell,-\ell}\). The smallest eigenvalue is \(1-\Lambda_\ell\), attained precisely by multiples of \(Z_{\ell,\ell}\). Exactly \(\lfloor(\ell+1)/2\rfloor\) eigenvalues lie strictly above \(1/2\), the same number lie strictly below, and the multiplicity at \(1/2\) is \(\ell+1\) for even \(\ell\) and \(\ell\) for odd \(\ell\). The noncentral positive shifts are strictly ordered by \(k\) within the parity class \(\ell+k\) even.

The constants decrease strictly with degree, with
\[
D_{\ell+1}/D_\ell=\frac{2\ell+3}{2\ell+4},\qquad
\Lambda_\ell=\frac12+\frac{1+O(\ell^{-1})}{\sqrt{\pi\ell}}.
\]
For \(\ell\ge2\), the exact gap from the highest eigenvalue to the second highest is
\[
\boxed{g_\ell=D_\ell\frac{\ell+1}{2\ell-1};}
\]
for \(\ell=1\), \(g_1=D_1=3/8\). Consequently every \(f\) in the one-degree spin-one space satisfies the **sharp stability inequality**
\[
\Lambda_\ell\|f\|_{L^2(S^2)}^2-\int_{H}|f|^2\,d\omega\ \ge\
g_\ell\left(\|f\|_{L^2(S^2)}^2-|\langle f,Z_{\ell,-\ell}\rangle|^2\right).
\]
Here \(H=\{0\le\theta\le\pi/2\}\). Equality in this deficit bound is attained on the span of the top and second spectral sectors; in particular its constant cannot be increased. Examples are \(\Lambda_1=7/8\), \(\Lambda_2=13/16\), and \(\Lambda_3=99/128\).

## Assumptions and scope

The sphere has unit radius, area element \(d\omega=\sin\theta\,d\theta\,d\phi\), and complex-valued scalar spherical harmonics \(Y_{\ell m}\) are orthonormal in full-sphere \(L^2\). We use the spin-raising (eth) convention
\[
\eth f=-(\partial_\theta+i\csc\theta\,\partial_\phi)f
\]
when applied to a spin-zero function. The spin-one modes \(Z_{\ell m}\) have unit full-sphere norm because \(\|\eth Y_{\ell m}\|_2^2=\ell(\ell+1)\). Multiplication by \(\mathbf1_H\) is compressed to \(\operatorname{span}_{\mathbb C}\{Z_{\ell m}:-\ell\le m\le\ell\}\) using the full-sphere inner product. No assertion is made about multiple degrees, arbitrary caps, or spin weights other than one. Reversing the eth or hemisphere orientation convention interchanges the labels \(m\) and \(-m\) but preserves the eigenvalue multiset and sharp constants.

## Proof

**Diagonalization and symmetry.** For \(k=|m|\), choose the harmless azimuthal phase such that \(Y_{\ell m}(\theta,\phi)=N_{\ell k}P_\ell^k(\cos\theta)e^{im\phi}\), where
\[
N_{\ell k}^2=\frac{2\ell+1}{4\pi}\frac{(\ell-k)!}{(\ell+k)!}.
\]
Put \(U(\theta)=N_{\ell k}P_\ell^k(\cos\theta)\). Up to an irrelevant sign, \(\eth Y_{\ell m}=(-U'(\theta)+mU(\theta)/\sin\theta)e^{im\phi}\). Orthogonality of distinct azimuthal frequencies on both \(H\) and \(S^2\) diagonalizes the compressed matrix. The two squared factors \(U'^2+m^2U^2/\sin^2\theta\) are reflection-symmetric about the equator because \(P_\ell^k(-x)=(-1)^{\ell+k}P_\ell^k(x)\). Hence \(\lambda_{\ell,-m}+\lambda_{\ell,m}=1\); at \(m=0\), \(\lambda_{\ell,0}=1/2\).

**Equatorial boundary term.** Fix \(m>0\). Subtracting the two squared raising-operator formulas and integrating yields
\[
\lambda_{\ell,-m}-\lambda_{\ell,m}
=\frac{4\pi m}{\ell(\ell+1)}\bigl(U(\pi/2)^2-U(0)^2\bigr)
=\frac{4\pi mN_{\ell m}^2}{\ell(\ell+1)}\bigl[P_\ell^m(0)\bigr]^2,
\]
since \(U(0)=0\) when \(m>0\). If \(\ell+m\) is odd, associated-Legendre parity makes this zero. If \(\ell+m\) is even, with integers \(a=(\ell+m)/2\) and \(b=(\ell-m)/2\), the equatorial value is
\[
P_\ell^m(0)=(-1)^a\frac{(2a-1)!!}{(2b)!!},\qquad
\frac{(\ell-m)!}{(\ell+m)!}[P_\ell^m(0)]^2=\frac{\binom{2a}{a}\binom{2b}{b}}{4^\ell}.
\]
These identities give the exact \(\Delta_{\ell,k}\) and hence every claimed eigenvalue, without any finite-dimensional approximation.

**Strict order, spectral multiplicity, and stability.** For \(3\le k\le\ell\) with \(\ell+k\) even, let \(a=(\ell+k)/2\) and \(b=(\ell-k)/2\). Direct binomial cancellation gives
\[
\frac{\Delta_{\ell,k-2}}{\Delta_{\ell,k}}
=\frac{k-2}{k}\frac{a(2b+1)}{(2a-1)(b+1)}<1,
\]
because \((2a-1)(b+1)-a(2b+1)=k-1>0\). For \(k=2\) the next order is the zero shift. Therefore \(k=\ell\) is the unique maximizer among nonzero shifts. The number of positive integers \(k\le\ell\) sharing the parity of \(\ell\) is \(\lfloor(\ell+1)/2\rfloor\), giving the claimed central multiplicities. At the next highest shift \(k=\ell-2\), cancellation simplifies to
\[
\frac{\Delta_{\ell,\ell-2}}{D_\ell}=\frac{\ell-2}{2\ell-1} \quad (\ell\ge2),
\]
where for \(\ell=2\) this correctly denotes zero. The difference is exactly \(g_\ell\). Since the operator is Hermitian diagonal, expanding any \(f\) in this basis proves the deficit inequality; the presence of a second eigenvector makes it sharp. For \(\ell=1\), the only other eigenvalue is \(1/2\).

**Degree law.** From \(\binom{2\ell+2}{\ell+1}/4^{\ell+1}=\binom{2\ell}{\ell}(2\ell+1)/(2\ell+2)/4^\ell\), elementary cancellation yields \(D_{\ell+1}/D_\ell=(2\ell+3)/(2\ell+4)<1\). Stirling's central-binomial estimate yields the stated asymptotic.

## Verification

The included standalone `check.py` independently forms the eth-mode energy from associated Legendre derivatives. It checks 120 exact rational hemisphere integrals for degrees 1 through 10, numerical Gauss–Legendre integrals and traces through degree 28, and 1198 exact rational spectral, gap, and monotonicity checks through degree 200. See `verification_output.txt` for actual output. These finite checks corroborate but cannot substitute for the proof for all integer degrees.

## Relationship to prior work

Michel, Plattner, and Seibert (2021) establish the unified spin-weighted Slepian framework and commuting operators for spherical caps, including general spectral construction. Jahn and Bokor (2013) develop the related Sheppard–Török functions and the corresponding general cap concentration-kernel integrals. Plattner and Simons (2013) treat vector-field spherical concentration. These frameworks cover the setup and support deriving individual matrix entries; the presently asserted addition is a closed all-degree central-binomial **single-degree spin-one hemispherical spectrum**, strict order and equality classification, and its **exact next-eigenvalue gap**, rather than a new general cap kernel or a new commuting operator. This statement of novelty is limited to the inspected primary literature, not an assertion of absolute priority.

## Limitations

The result is for one fixed spherical-harmonic degree, spin weight \(+1\), and the north hemisphere with the displayed eth orientation. The formulas do not give arbitrary-cap or multi-degree spectra, nor sharp bounds for general tangential-vector mixtures beyond the one-helicity sector. General primary cap formulas already exist. Equivalent older formulations may remain unindexed; in particular, a relevant earlier thesis on spin-weighted spherical-cap Slepian functions was identified but its full text could not be examined. Independent mathematical and bibliographic audit has not been performed.

## References

1. V. Michel, A. Plattner, K. Seibert, *A Unified Approach to Scalar, Vector, and Tensor Slepian Functions on the Sphere and Their Construction by a Commuting Operator*, arXiv:2103.14650 (initially public 2021-03-26). https://arxiv.org/abs/2103.14650
2. K. Jahn, N. Bokor, *Revisiting the concentration problem of vector fields within a spherical cap: a commuting differential operator solution*, arXiv:1302.5261 (2013). https://arxiv.org/abs/1302.5261
3. A. Plattner, F. J. Simons, *Spatiospectral concentration of vector fields on a sphere*, arXiv:1306.3201 (2013). https://arxiv.org/abs/1306.3201
4. K. Seibert, *Spin-Weighted Spherical Harmonics and Their Application for the Construction of Tensor Slepian Functions on the Spherical Cap* (2018 thesis; bibliographic comparison limited by full-text access).
