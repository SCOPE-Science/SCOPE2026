# Fourth-harmonic Gaussian fluctuations of random cross-polytope hyperplane shadows

## Finding

For every integer \(d\ge3\), let \(C_d=\{x\in\mathbb R^d:\sum_{i=1}^d|x_i|\le1\}\), let \(U_d\) be uniformly distributed on the unit sphere, and let
\[
B_d=\operatorname{vol}_{d-1}(\operatorname{proj}_{U_d^\perp}C_d),\qquad
Z_d=\frac{(d-1)!}{2^{d-1}}B_d.
\]
Write \(\mu_d=\sqrt d\,\Gamma(d/2)/(\sqrt\pi\,\Gamma((d+1)/2))\). The exact second-moment identity is
\[
\mathbb E Z_d^2=\frac2{\pi 2^d}\sum_{k=0}^d\binom dk\left[\sqrt{1-\rho_{d,k}^2}+\rho_{d,k}\arcsin(\rho_{d,k})\right],\qquad \rho_{d,k}=1-\frac{2k}{d},
\]
and \(\mathbb E Z_d=\mu_d\). Consequently,
\[
\operatorname{Var}(Z_d)=\frac1{3\pi d^3}+O(d^{-4}),\qquad
 d^{3/2}(Z_d-\mu_d)\ \xrightarrow{\mathrm{law}}\ N\!\left(0,\frac1{3\pi}\right).
\]
In particular the normalized shadow's orientation fluctuations have order \(d^{-3/2}\), rather than order \(d^{-1/2}\). More precisely, their leading component is the degree-four spherical harmonic
\[
H_d(U)=\sum_{i=1}^dU_i^4-\frac3{d+2},\qquad
\beta_d=\mu_d\frac{(d+2)(d+4)(d+6)}{12d(d+1)(d+3)},
\]
with the quantitative \(L^2\) remainder bound
\[
\mathbb E\bigl[(Z_d-\mu_d-\beta_dH_d(U_d))^2\bigr]=O(d^{-4}).
\]
The first-order mean correction \(\mu_d=\sqrt{2/\pi}\,[1+1/(4d)+O(d^{-2})]\) is necessary for the stated fluctuation scale.

## Assumptions and scope

The cross-polytope has coordinate vertices \(\pm e_i\) and no rescaling; projection is Euclidean orthogonal projection onto the codimension-one subspace perpendicular to a Haar-uniform unit normal. All formulas hold for the integer dimensions indicated, with ordinary Euclidean intrinsic \((d-1)\)-volume. The central limit theorem concerns growing ambient dimension, not repeated sampling of a fixed body. \(N(0,\sigma^2)\) denotes the centered Gaussian law with variance \(\sigma^2\).

## Proof

**1. Brightness as a Rademacher functional.** Each of the \(2^d\) facets of \(C_d\) has outer unit normal \(s/\sqrt d\), where \(s\in\{\pm1\}^d\), and facet \((d-1)\)-volume \(\sqrt d/(d-1)!\). The Cauchy projection identity gives
\[
B_d(u)=\frac1{2(d-1)!}\sum_{s\in\{\pm1\}^d}|s\cdot u|.
\]
Thus \(Z_d(u)=2^{-d}\sum_s|s\cdot u|=\mathbb E_{\varepsilon}|\sum_i\varepsilon_i u_i|\). This is an exact geometric identity, not a central-limit approximation.

**2. First and second moments.** For a unit vector \(v\), spherical integration yields \(\mathbb E|v\cdot U_d|=\Gamma(d/2)/(\sqrt\pi\,\Gamma((d+1)/2))\). This proves \(\mathbb E Z_d=\mu_d\). For two sign vectors \(s,t\) set \(\rho=(s\cdot t)/d\). Writing a standard Gaussian \(G=R U_d\), with independent radius and direction and \(\mathbb E R^2=d\), and applying the bivariate Gaussian absolute-product identity, gives
\[
\mathbb E_{U_d}|s\cdot U_d|\,|t\cdot U_d|=\frac2\pi\left(\sqrt{1-\rho^2}+\rho\arcsin\rho\right).
\]
For fixed \(s\), precisely \(\binom dk\) choices of \(t\) have \(\rho=1-2k/d\); averaging proves the finite binomial second-moment formula.

**3. Sharp variance expansion.** Let \(\rho_d=d^{-1}\sum_{i=1}^d\xi_i\), where \(\xi_i\) are independent fair signs. For \(|x|\le1\), the continuous even function \(f(x)=\sqrt{1-x^2}+x\arcsin x\) satisfies, uniformly,
\[
f(x)=1+\tfrac12x^2+\tfrac1{24}x^4+\tfrac1{80}x^6+O(x^8).
\]
Direct expansion of independent sign moments gives
\[
\mathbb E\rho_d^2=d^{-1},\quad \mathbb E\rho_d^4=3d^{-2}-2d^{-3},\quad
\mathbb E\rho_d^6=15d^{-3}-30d^{-4}+16d^{-5},\quad \mathbb E\rho_d^8=O(d^{-4}).
\]
Hence
\[
\mathbb E Z_d^2=\frac2\pi\left(1+\frac1{2d}+\frac1{8d^2}+\frac5{48d^3}+O(d^{-4})\right).
\]
The gamma-ratio expansion, obtained by Stirling's formula with a uniform remainder, is
\[
\mu_d^2=\frac2\pi\left(1+\frac1{2d}+\frac1{8d^2}-\frac1{16d^3}+O(d^{-4})\right).
\]
Their difference proves \(\operatorname{Var}(Z_d)=1/(3\pi d^3)+O(d^{-4})\). Notice that the first two potential inverse-dimension variance terms cancel exactly.

**4. Identification of the fourth-harmonic component.** On the sphere, \(H_d(U)=\sum_i U_i^4-3/(d+2)\) has mean zero and is the restriction of the homogeneous harmonic polynomial \(\sum_i x_i^4-3|x|^4/(d+2)\). Uniform spherical coordinate moments give
\[
\mathbb E H_d^2=\frac{24(d-1)}{(d+2)^2(d+4)(d+6)}.
\]
By sign invariance, \(\mathbb E(Z_dH_d)=\mathbb E(|s\cdot U_d|H_d(U_d))\) for any fixed sign vector \(s\). Set \(v=s/\sqrt d\) and \(T=v\cdot U_d\). Conditioned on \(T=t\), write \(U_d=tv+\sqrt{1-t^2}\,W\), where \(W\) is uniform on the unit sphere of \(v^\perp\). Its coordinate fourth moments give
\[
\mathbb E\!\left[\sum_iU_i^4\mid T=t\right]
=\frac1d\left[t^4+6t^2(1-t^2)+\frac{3(d-1)}{d+1}(1-t^2)^2\right].
\]
Using \(\mathbb E|T|^3=2\mathbb E|T|/(d+1)\) and \(\mathbb E|T|^5=8\mathbb E|T|/((d+1)(d+3))\) yields
\[
\mathbb E[Z_dH_d]=\mu_d\frac{2(d-1)}{d(d+1)(d+2)(d+3)}=\beta_d\mathbb E H_d^2.
\]
Thus \(\beta_dH_d\) is the orthogonal \(L^2\) projection of the centered brightness onto this fourth-harmonic direction. By orthogonality,
\[
\mathbb E[(Z_d-\mu_d-\beta_dH_d)^2]=\operatorname{Var}(Z_d)-\beta_d^2\mathbb E H_d^2.
\]
The variance asymptotic of step 3, the displayed exact harmonic variance, and \(\beta_d\to\sqrt{2/\pi}/12\) show that the right side is \(O(d^{-4})\), establishing the quantitative approximation.

**5. Central limit theorem.** Let \(G_i\) be independent standard Gaussians and \(U_i=G_i/(\sum_jG_j^2)^{1/2}\). The multivariate classical CLT for \(d^{-1}\sum_i(G_i^4,G_i^2)\) and the delta method give
\[
d^{3/2}H_d(U)\ \xrightarrow{\mathrm{law}}\ N(0,24),
\]
because \(\operatorname{Var}(G^4-6G^2)=96+36\cdot2-12\cdot12=24\). The harmonic remainder in step 4, multiplied by \(d^{3/2}\), tends to zero in \(L^2\). Since \(\beta_d\to\sqrt{2/\pi}/12\), Slutsky's theorem gives the claimed normal limit with variance \(24(\sqrt{2/\pi}/12)^2=1/(3\pi)\).

## Verification

The included standalone script `verification/check_crosspolytope_brightness.py` independently implements the binomial second moment, spherical harmonic covariances and a planar convex-hull projection test for three-dimensional cross-polytopes. It checks the closed formulas at several dimensions and tests the approach to the limiting variance coefficient. Direct finite sampling and numerical computations corroborate but do not prove the all-dimensional formulas or central limit theorem. No external proof assistant or independent scientific review is claimed.

For the four-dimensional cross-polytope specifically,
\[
\mathbb E Z_4=\frac8{3\pi},\qquad
\mathbb E Z_4^2=\frac5{24}+\frac{\sqrt3}{2\pi}+\frac3{4\pi},
\]
so the finite sum also produces a concrete exact check with inverse trigonometric values eliminated.

## Relationship to prior work

Ivanov's 2026 theorem determines the *largest possible* lower-dimensional projection volume of a regular cross-polytope, with equality conditions, but not the full orientation variance or its normal fluctuation law. His 2018 article studies deterministic extremal projections and the conjectured lower bound. Gao and Qian's 2026 work treats fixed-coefficient higher Rademacher moments and their fourth-order mass; the present random-direction absolute *first*-moment functional, its exact angular second moment and its Gaussian fluctuation theorem have different quantifiers and conclusions. Abas's 2026 work develops random width/brightness methods, principally in dimension three, and folded-normal pair moments; that general technology can explain the second-moment kernel, but the dimension-dependent cross-polytope binomial specialization, fourth-harmonic cancellation and sharp \(d^{-3/2}\) fluctuation law are separate claims. See the accompanying review for access and historical-priority limitations.

## Limitations

The statement concerns only codimension-one orthogonal projections of regular coordinate cross-polytopes, and normalization by \(2^{d-1}/(d-1)!\) is essential. It does not provide the full finite-dimensional distribution, a Berry--Esseen rate, or corresponding fluctuation theorems for arbitrary subspace codimensions or nonregular cross-polytopes. A general finite-direction folded-normal formula is prior technology and is not claimed to be new. Some plausible related sources could not be read completely; equivalence to unindexed results remains a historical-priority risk. Independent audit has not been performed.

## References

1. Grigory Ivanov, *The maximal volume of projections of the cross-polytope*, arXiv:2607.12072v1, first posted 2026-07-13, https://arxiv.org/abs/2607.12072.
2. Grigory Ivanov, *On the volume of projections of the cross-polytope*, arXiv:1808.09165v1, first posted 2018-08-28, https://arxiv.org/abs/1808.09165.
3. Peigan Gao and Jian Qian, *Fourth-Moment Geometry of Rademacher Sums*, arXiv:2608.17802v1, first posted 2026-08-18, https://arxiv.org/abs/2608.17802.
4. Omri Abas, *Random Width and Brightness: Polyhedral Density Theory, Reconstruction, and Gaussian Identifiability*, arXiv:2609.26202, https://arxiv.org/abs/2609.26202.
