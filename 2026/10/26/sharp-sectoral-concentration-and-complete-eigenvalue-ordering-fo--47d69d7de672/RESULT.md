# Sharp sectoral concentration and complete eigenvalue ordering for two adjacent spherical degrees

## Finding
Let \(H=\{(x,y,z)\in S^2:z>0\}\), and let \(\mathcal H_j\) be the complex spherical harmonics of exactly degree \(j\) with their usual \(L^2(S^2)\) normalization. For every integer \(\ell\ge0\), consider the two-shell space
\[
V_\ell=\mathcal H_\ell\oplus\mathcal H_{\ell+1},\qquad C_\ell=P_{V_\ell}\mathbf1_H P_{V_\ell}\big|_{V_\ell}.
\]
For \(j\ge0\), put \(b_j=\binom{2j}{j}/4^j\) and
\[
Q_\ell=\frac{\sqrt{(2\ell+1)(2\ell+3)}}{4(\ell+1)},\quad
f_j=\sqrt{2j+1}\,b_j,\quad
g_j=\frac{2j+1}{\sqrt{2j+2}}\,b_j.
\]
For each order \(0\le m\le\ell\), define the positive scalar
\[
c_{\ell,m}=\begin{cases}
Q_\ell f_{(\ell+m)/2}f_{(\ell-m)/2},&\ell+m\ \text{even},\\
Q_\ell g_{(\ell+m-1)/2}g_{(\ell-m-1)/2},&\ell+m\ \text{odd}.
\end{cases}
\]
Then the complete spectrum of \(C_\ell\) is \(\tfrac12\pm c_{\ell,m}\) for \(0\le m\le\ell\), each with multiplicity one for \(m=0\) and multiplicity two for each \(m\ge1\), together with exactly two additional eigenvalues equal to \(\tfrac12\). There are no other eigenvalues. Every \(c_{\ell,m}\) lies strictly between zero and \(\tfrac12\).

**Sharp ordering:** The scalars for orders \(m\) with \(\ell+m\) even are all strictly larger than those for orders with \(\ell+m\) odd. Along the former parity chain \(c_{\ell,m}\) strictly increases as \(m\) increases by two; along the latter it strictly decreases. Thus the unique maximizing absolute order is \(m=\ell\), for every \(\ell\ge0\), and the largest concentration eigenvalue is
\[
\boxed{\lambda_{\max}(C_\ell)=\frac12+a_\ell,\qquad
 a_\ell=\frac{(2\ell+1)\sqrt{2\ell+3}}{4(\ell+1)}\frac{\binom{2\ell}{\ell}}{4^\ell}.}
\]
For \(\ell\ge1\) the maximizing eigenspace has dimension two, spanned in the standard Condon--Shortley convention by \((Y_\ell^{\ell}+Y_{\ell+1}^{\ell})/\sqrt2\) and \((Y_\ell^{-\ell}+Y_{\ell+1}^{-\ell})/\sqrt2\); for \(\ell=0\) it has dimension one. Moreover \(a_\ell\) decreases strictly from \(a_0=\sqrt3/4\) to \(1/\sqrt{2\pi}\), with
\[
a_\ell=\frac1{\sqrt{2\pi}}\left(1+\frac1{8\ell}+O(\ell^{-2})\right)\quad(\ell\to\infty).
\]
In particular, the sharp lower bound on opposite-hemisphere leakage, uniform over all two-adjacent-degree spaces and all unit-norm vectors, is
\[
\boxed{\int_{S^2\setminus H}|v|^2\,d\Omega\ge\frac12-\frac{\sqrt3}{4};}
\]
equality occurs precisely in the maximizing line at \(\ell=0\). For a fixed shell pair the sharp lower bound is \(\tfrac12-a_\ell\), which increases to \(\tfrac12-1/\sqrt{2\pi}\).

## Assumptions and scope
The sphere has its standard surface measure (total area \(4\pi\)); spherical harmonics \(Y_j^m\) are orthonormal for this measure. The north-south axis defining \(H\) is arbitrary by rotational invariance. Concentration means the fraction \(\int_H|v|^2/\int_{S^2}|v|^2\) for a nonzero complex or real vector \(v\in V_\ell\). Real and complex formulations have the same eigenvalues with the corresponding real-dimensional multiplicities. The exact degree mask comprises **only** \(\ell\) and \(\ell+1\), not the low-pass band of all lower degrees. No assertion is made for wider degree masks or caps different from a hemisphere.

## Proof
Fix the complex Condon--Shortley spherical harmonics
\[
Y_j^m(\theta,\phi)=N_{j,m}P_j^{m}(\cos\theta)e^{im\phi},\quad
N_{j,m}=\sqrt{\frac{2j+1}{4\pi}\frac{(j-m)!}{(j+m)!}},\quad 0\le m\le j.
\]
The negative-order blocks are unitarily equivalent. Longitude integration makes the concentration matrix diagonal by the signed order. Each single-degree diagonal entry is \(1/2\), because \(|Y_j^m|^2\) is symmetric across the equator. For \(0\le m\le\ell\) the remaining block in the basis \(Y_\ell^m,Y_{\ell+1}^m\) is
\[
\begin{pmatrix}1/2&c_{\ell,m}\\c_{\ell,m}&1/2\end{pmatrix},\quad
c_{\ell,m}=2\pi N_{\ell,m}N_{\ell+1,m}\int_0^1P_\ell^m(x)P_{\ell+1}^m(x)\,dx.
\]
For the two orders \(m=\pm(\ell+1)\), only \(Y_{\ell+1}^m\) is available, giving the two additional half-energy eigenvalues.

For completeness, apply the associated-Legendre Sturm--Liouville equations with eigenvalues \(j(j+1)\), integrate the Lagrange identity, and use the vanishing endpoint term at \(x=1\):
\[
\int_0^1 P_\ell^m P_{\ell+1}^m\,dx=
\frac{P_\ell^m(0)(P_{\ell+1}^m)'(0)-(P_\ell^m)'(0)P_{\ell+1}^m(0)}{2(\ell+1)}.
\]
The recurrences \((P_{\ell+1}^m)'(0)=(\ell+m+1)P_\ell^m(0)\) when \(\ell+m\) is even and \((P_\ell^m)'(0)=(\ell+m)P_{\ell-1}^m(0)\), \(P_{\ell+1}^m(0)=-(\ell+m)P_{\ell-1}^m(0)/(\ell-m+1)\) when it is odd, together with
\[
P_j^m(0)=(-1)^{(j+m)/2}\frac{(j+m-1)!!}{(j-m)!!}
\quad\text{for even }j+m,
\]
(with the usual \(0!!=(-1)!!=1\)), reduce both cases by factorial cancellation to the displayed products of \(f_j\) and \(g_j\). They also show \(c_{\ell,m}>0\). Strict Cauchy--Schwarz on the hemisphere gives \(c_{\ell,m}<1/2\), since consecutive-degree colatitudinal functions cannot be proportional on a nonempty interval.

The decisive inequalities are the exact ratios
\[
\frac{f_{j+1}}{f_j}=\sqrt{1-\frac1{4(j+1)^2}},\qquad
\frac{g_{j+1}}{g_j}=\sqrt{1+\frac1{4(j+1)(j+2)}}.
\]
Thus \(f_j\) decreases strictly with increasing consecutive ratios (strict log-convexity), while \(g_j\) increases strictly with decreasing consecutive ratios (strict log-concavity). Stirling's formula gives the common limit \(\sqrt{2/\pi}\); consequently \(f_j>\sqrt{2/\pi}>g_k\) for every finite nonnegative \(j,k\). In the first parity chain the two indices \((\ell+m)/2,(\ell-m)/2\) have fixed sum \(\ell\), so the strict log-convexity makes their product strictly increase as \(m\) increases by two. In the other chain the two indices have fixed sum \(\ell-1\), so strict log-concavity makes their product strictly decrease. The uniform inequality between \(f\) and \(g\) places every first-chain eigenvalue gap above every second-chain gap. The largest gap is therefore at \(m=\ell\), with the stated closed form.

Finally direct cancellation of central binomial factors gives
\[
\frac{a_{\ell+1}}{a_\ell}=
\frac{\sqrt{(2\ell+3)(2\ell+5)}}{2\ell+4}
=\sqrt{1-\frac1{4(\ell+2)^2}}<1.
\]
Stirling expansion yields the stated asymptotic. The variational characterization of the top and bottom eigenvalues yields the sharp leakage bounds and equality cases.

## Verification
The standalone script `verify.py` evaluates the off-diagonal overlaps independently by Gauss--Legendre quadrature using normalized associated Legendre polynomials, compares them with the factorial products, diagonalizes the independently evaluated \(2\times2\) blocks, and checks ordering and dimension monotonicity. With Python 3, NumPy and SciPy installed, execute `python verify.py` in this directory. The packaged output in `verification_output.txt` reports 630 overlap comparisons for \(0\le\ell\le34\), 136 direct spectral blocks for \(0\le\ell\le15\), and strict formula checks through \(\ell=300\). Its largest quadrature discrepancy is approximately \(2.21\times10^{-14}\). This finite test does not establish the infinite statements; the ratio identities and Sturm--Liouville proof do.

## Relationship to prior work
Simons, Dahlen, and Wieczorek's 31 August 2004 arXiv paper derives general spherical-cap concentration matrices and order decomposition (Sections 3 and 5), with numerical emphasis on conventional contiguous low-pass spaces. Ramamoorthi's 2002 hemispherical-lighting analysis uses restricted spherical-harmonic orthogonality and computes low-degree matrices. A published 2026 mathematical record, *Exact half-energy multiplicities for hemispherical spherical Slepian concentration with arbitrary degree masks*, proves the general parity/Cauchy rank law, including the multiplicity of eigenvalues \(1/2\), but explicitly leaves noncentral singular values without closed forms. The present two-shell calculation uses the same classical ingredients but establishes the previously unreported **strict inter-order spectral ranking, exact universal maximizing sectoral order, and optimal all-degree leakage** by an additional pair of opposing Wallis-product monotonicity inequalities. No claim is made to having originated spherical Slepian theory, order decomposition, or the parity half-energy law.

## Limitations
This is an exact statement for a two-adjacent-degree spherical-harmonic subspace on \(S^2\) and a hemispherical observation region. The theorem does not optimize multi-shell masks, unequal cap radii, or weighted anisotropic surface regions. Although focused searches and inspected sources did not uncover the sharp sectoral ordering statement, classical special-function or hemisphere-sampling literature might contain an equivalent inequality or an immediate named corollary. Independent publication-priority assessment has not been performed.

## References
1. F. J. Simons, F. A. Dahlen, and M. A. Wieczorek, *Spatiospectral concentration on a sphere*, arXiv:math/0408424v1, first public 31 August 2004, Sections 3 and 5 and Appendix A; later SIAM Review 48 (2006), 504--536. Primary MSC 42B05. https://arxiv.org/abs/math/0408424
2. R. Ramamoorthi, *Analytic PCA construction for theoretical analysis of lighting variability in images of a Lambertian object*, IEEE Transactions on Pattern Analysis and Machine Intelligence 24 (2002), 1322--1333, especially hemispherical orthogonality and the finite numerical eigenproblem, https://www.cvl.iis.u-tokyo.ac.jp/class2004/wedenesday/Ramamoorthi.pdf
3. *Exact half-energy multiplicities for hemispherical spherical Slepian concentration with arbitrary degree masks*, public mathematical record (2026), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-half-energy-multiplicities-for-hemispherical-spherical-sle--0284b88cef7a
