# Sharp odd-gap hemispherical concentration and an exact degree-peak law

## Finding
Let \(H\) be a hemisphere of the unit two-sphere, and let \(\mathcal H_j\) be the complex spherical harmonics of exact degree \(j\), with the usual area measure. For every integer \(\ell\ge0\) and every odd integer \(d\ge3\), put \(k=\ell+d\) and \(\mathcal V_{\ell,d}=\mathcal H_\ell\oplus\mathcal H_k\). Define
\[
B_{\ell,d}=\frac{\sqrt{(2\ell+1)(2\ell+2d+1)}}{2d(2\ell+d+1)}
\sqrt{\frac{d!}{(2\ell)!(2\ell+d)!}}
\frac{(2\ell-1)!!(2\ell+d)!!}{(d-1)!!},
\]
with \((-1)!!=0!!=1\). Then the **sharp, attained concentration inequality** is
\[
\int_H|f|^2\,d\omega\ \le\ \left(\frac12+B_{\ell,d}\right)
\int_{S^2}|f|^2\,d\omega,\qquad f\in\mathcal V_{\ell,d}.
\]
With the standard Condon--Shortley spherical harmonics, write \(\varepsilon_d=(-1)^{(d-1)/2}\). If \(\ell\ge1\), the entire maximizing eigenspace is
\[
\operatorname{span}_{\mathbb C}\{Y_{\ell,\ell}+\varepsilon_dY_{\ell+d,\ell},\;
Y_{\ell,-\ell}+\varepsilon_dY_{\ell+d,-\ell}\}.
\]
For \(\ell=0\), only the first combination (with order zero) is present. No other maximizing functions exist.

The **degree-peak law** is strict: for every fixed odd \(d\ge3\), \(B_{\ell,d}\) increases with the integer \(\ell\) from zero through \(\ell=d-1\), then decreases strictly thereafter. In particular, the unique maximally concentrating two-degree packet of fixed gap \(d\) begins at degree \(d-1\). For fixed \(d=2r+1\),
\[
\lim_{\ell\to\infty}B_{\ell,d}
=\frac{\sqrt{d!}}{d\,2^r r!\sqrt{2\pi}}.
\]

The complete spectrum and sharp spectral-stability gap are also explicit. For \(0\le m\le\ell\), let \(h_{\ell,d,m}\) be the absolute value of the overlap in the proof. The spectrum consists of \(\frac12\pm h_{\ell,d,|m|}\) for each signed \(m\) with \(|m|\le\ell\), together with exactly \(2d\) copies of \(\frac12\). Its largest eigenvalue is \(\frac12+B_{\ell,d}\); its second distinct eigenvalue is \(\frac12+h_{\ell,d,\ell-2}\) for \(\ell\ge2\), \(\frac12+h_{1,d,0}\) for \(\ell=1\), and \(\frac12\) for \(\ell=0\). All these eigenvalues have specified eigenvectors from the order-wise blocks.

## Assumptions and scope
The hemisphere may be rotated arbitrarily, as the spectrum is rotation invariant. Degrees are nonnegative integers, and the degree difference \(d\) is odd and at least three. This excludes the previously treated consecutive-degree case. The result concerns scalar complex spherical harmonics on \(S^2\), not arbitrary spectral masks, non-hemispherical caps, or spin-weighted harmonics. Norms and integrals use the same usual surface measure; concentration ratios are independent of its overall normalization.

Fix the north hemisphere and put \(x=\cos\theta\). For \(m\ge0\), use Condon--Shortley Ferrers functions \(P_j^m\) and normalized colatitudinal factors
\[
S_{jm}(x)=\sqrt{\frac{2j+1}{2}\frac{(j-m)!}{(j+m)!}}\,P_j^m(x),
\quad Y_{jm}(\theta,\phi)=(2\pi)^{-1/2}S_{jm}(\cos\theta)e^{im\phi}.
\]
For negative orders take \(Y_{j,-m}=(-1)^m\overline{Y_{jm}}\). Then \(\int_{-1}^{1}S_{jm}(x)^2dx=1\).

## Proof
**1. Two-degree concentration blocks.** The longitude integral separates signed azimuthal orders. Each order \(|m|\le\ell\) gives the Hermitian matrix
\[
Q_m=\begin{pmatrix}\frac12&I_m\\I_m&\frac12\end{pmatrix},\qquad
I_m=\int_0^1 S_{\ell,|m|}(x)S_{k,|m|}(x)\,dx.
\]
The diagonal entries are \(\frac12\), because the squared factors are even in \(x\) and have full integral one. For \(\ell<|m|\le k\), the only available mode has eigenvalue \(\frac12\), accounting for \(2d\) central eigenvalues. Opposite parity makes every \(I_m\) nonzero.

**2. Exact boundary formula.** Put \(\Delta=k(k+1)-\ell(\ell+1)=d(2\ell+d+1)>0\). The associated-Legendre Sturm--Liouville equation and integration by parts give
\[
I_m=\frac{S_{\ell m}(0)S'_{km}(0)-S_{km}(0)S'_{\ell m}(0)}{\Delta},\qquad m\ge0.
\]
At \(x=1\), the Wronskian endpoint vanishes. Since \(\ell+m\) and \(k+m\) have opposite parity, precisely one product in the numerator survives. Elementary double-factorial evaluations yield
\[
|S_{jm}(0)|=\sqrt{\frac{2j+1}{2}\frac{(j-m)!}{(j+m)!}}\,
\frac{(j+m-1)!!}{(j-m)!!}\quad(j+m\text{ even}),
\]
\[
|S'_{jm}(0)|=\sqrt{\frac{2j+1}{2}\frac{(j-m)!}{(j+m)!}}\,
\frac{(j+m)!!}{(j-m-1)!!}\quad(j+m\text{ odd}).
\]
Consequently, \(h_{\ell,d,m}=|I_m|\) is given explicitly by these products divided by \(\Delta\), including every multiplicity in the complete spectrum. At \(m=\ell\), they simplify to \(h_{\ell,d,\ell}=B_{\ell,d}\), exactly the factorial expression in the finding. The boundary signs, obtainable from Rodrigues' formula, show \(I_m=\varepsilon_d h_{\ell,d,m}\) in the stated convention.

**3. A strict ordering lemma valid for every odd gap.** The normalized order-raising identities at the equator are
\[
S_{j,m+1}(0)=-\frac{S'_{jm}(0)}{\sqrt{(j-m)(j+m+1)}},\qquad
S'_{j,m+1}(0)=\sqrt{(j-m)(j+m+1)}S_{jm}(0).
\]
For \(0\le m<\ell\), define
\[
R_m=\sqrt{\frac{k(k+1)-m(m+1)}{\ell(\ell+1)-m(m+1)}}
=\sqrt{1+\frac{\Delta}{\ell(\ell+1)-m(m+1)}}>1.
\]
These numbers increase strictly with \(m\). Applying the two boundary identities to the surviving Wronskian product gives
\[
\frac{h_{\ell,d,m+1}}{h_{\ell,d,m}}=
\begin{cases}R_m^{-1},&\ell+m\text{ even},\\ R_m,&\ell+m\text{ odd}.\end{cases}
\]
On the parity class \(\ell+m\) even, the two-step ratio is \(R_{m+1}/R_m>1\). Every member of the other parity class is strictly dominated by the next member of the even class. Therefore \(h_{\ell,d,\ell}\) is the **unique maximum** over \(m=0,1,\ldots,\ell\). This establishes the sharp bound and exactly the maximizing modes, including their signed-order degeneracy.

The same ordering proves that the second-largest \(h\)-value is \(h_{\ell,d,\ell-2}\) when \(\ell\ge2\), and \(h_{1,d,0}\) when \(\ell=1\). For \(\ell\ge2\), the sharp gap between the largest and second-largest eigenvalues equals
\[
g_{\ell,d}=B_{\ell,d}\left(1-\sqrt{\frac{1+\Delta/(4\ell-2)}{1+\Delta/(2\ell)}}\right)>0.
\]
For \(\ell=1\) the gap equals \(B_{1,d}(1-\sqrt{2/((d+1)(d+2))})\), and for \(\ell=0\) it equals \(B_{0,d}\). If \(\Pi_{\max}\) is the full-sphere orthogonal projector onto the maximizing eigenspace, the spectral theorem yields the sharp stability inequality
\[
\left(\frac12+B_{\ell,d}\right)\|f\|_2^2-\int_H|f|^2d\omega
\ge g_{\ell,d}\|f-\Pi_{\max}f\|_2^2.
\]
Sharpness of the gap follows by choosing an eigenvector at the second-largest distinct eigenvalue.

**4. A strict peak at the lower degree \(d-1\).** Direct cancellation of the factorial formula gives, for every \(\ell\ge0\),
\[
\frac{B_{\ell+1,d}^2}{B_{\ell,d}^2}=
\frac{(2\ell+3)(2\ell+2d+3)(2\ell+d+2)(2\ell+d+1)}
{(2\ell+2d+1)(2\ell+2)(2\ell+d+3)^2}.
\]
Subtracting one from the right-hand side leaves
\[
\frac{d\,q_d(\ell)}{2(\ell+1)(2\ell+d+3)^2(2d+2\ell+1)},
\quad q_d(\ell)=2d^2+2d\ell+d-4\ell^2-12\ell-9.
\]
For odd \(d\ge3\), \(q_d(0)=2d^2+d-9>0\) and \(q_d(d-2)=d-1>0\). Concavity gives positivity throughout the integer interval \(0\le\ell\le d-2\). At \(\ell=d-1\), \(q_d(d-1)=-5d-1<0\), and the quadratic is strictly decreasing from that point forward. Thus the sequence has its unique maximum at \(\ell=d-1\). Finally, writing \(d=2r+1\), Stirling's formula applied to the factorial expression gives the displayed positive fixed-gap limit.

## Verification
The included standalone Python checker `check_spherical_packet.py` performs \(9910\) exact-rational assertions verifying squared overlaps, consecutive-order ratios, the strict order comparison, the closed top coefficient, the degree-peak ratio and its sign. Independently, \(1260\) normalized associated-Legendre hemisphere overlaps are compared with Gauss--Legendre quadrature, with maximum absolute error below \(3\times10^{-14}\) on that finite test set. Executing `python check_spherical_packet.py` with NumPy and SciPy prints the reproduced totals. These are finite checks, not substitutes for the exact all-degree proof.

## Relationship to prior work
Simons, Dahlen and Wieczorek formulate spherical Slepian concentration and the azimuthal-order block eigenproblem for polar caps; their result provides the general matrix framework, not this all-odd-gap ordering or degree-peak law. Michel, Plattner and Seibert formulate the scalar and spin-weighted cap concentration matrices and commuting-operator reductions, again without determining the claimed nonconsecutive two-degree sharp eigenvalues and peak. Jaming and Speckbacher prove large-sieve concentration bounds on two-point homogeneous spaces rather than this exact spectral classification.

A published result on **exact half-energy multiplicities for arbitrary spherical-harmonic degree masks** proves the cross-parity Cauchy-rank law, but expressly does not determine the nonzero singular values. Its arbitrary-mask scope therefore does not imply the present strictly ordered positive eigenvalues, extremizer classification, or the degree-peak \(\ell=d-1\). The distinct previously treated consecutive-degree case \(d=1\) is excluded; its monotone-decreasing degree behavior differs qualitatively from the strict interior peak at every odd \(d\ge3\).

## Limitations
No claim is made for even gaps, arbitrary finite unions of degree bands, general polar caps, or higher-dimensional spheres. The bound and equality classification are exact only for the prescribed two-degree packet and hemisphere. The full spectral gap controls distance to the *entire* maximizing eigenspace, not to a unique maximizing function when \(\ell\ge1\). The originality assessment is best-knowledge: classical associated-Legendre recurrences make the formula potentially recoverable from older specialized literature, and an equivalent unindexed extremal-order statement has not been ruled out by an independent audit.

## References
1. V. Michel, A. Plattner and K. Seibert, *A Unified Approach to Scalar, Vector, and Tensor Slepian Functions on the Sphere and Their Construction by a Commuting Operator*, arXiv:2103.14650v1 (first public 2021-03-26), especially Section 3, Theorems 3.5, 3.7 and 3.13.
2. P. Jaming and M. Speckbacher, *Concentration estimates for finite expansions of spherical harmonics on two-point homogeneous spaces via the large sieve principle*, arXiv:2004.02474v1 (first public 2020-04-06), especially Section 1 and Theorem 4.4.
3. F. J. Simons, F. A. Dahlen and M. A. Wieczorek, *Spatiospectral concentration on a sphere*, arXiv:math/0408424v1 (first public 2004-08-31), especially Sections 4 and 5.
4. *Exact half-energy multiplicities for hemispherical spherical Slepian concentration with arbitrary degree masks*, publicly available mathematical result (2026-10-11), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-half-energy-multiplicities-for-hemispherical-spherical-sle--0284b88cef7a.
5. NIST Digital Library of Mathematical Functions, Section 14.10, *Recurrence Relations and Derivatives*, https://dlmf.nist.gov/14.10.
