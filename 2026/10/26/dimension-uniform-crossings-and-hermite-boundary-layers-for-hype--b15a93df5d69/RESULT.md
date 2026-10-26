# Dimension-uniform crossings and Hermite boundary layers for hyperspherical-cap concentration

## Finding
For any integer \(d\ge 2\), degree \(\ell\ge1\), and proper northern spherical cap
\(C_c=\{\omega\in S^d:\omega_{d+1}\ge c\}\), \(0<c<1\), let \(\mathcal H_\ell(S^d)\) be the complex spherical harmonics of exact degree \(\ell\). The positive concentration operator is the compression of multiplication by \(\mathbf1_{C_c}\) to this irreducible harmonic space. Its scalar eigenvalue at polar angular degree \(m\in\{0,\ldots,\ell\}\) is denoted by \(\Lambda_{\ell,m}^{(d)}(c)\), with multiplicity \(\dim\mathcal H_m(S^{d-1})\).

Put \(\lambda=(d-1)/2\), \(P(x)=C_\ell^\lambda(x)\), and \(P_m=P^{(m)}\), ordinary derivatives. Define
\[
N_m=\frac{\pi 2^{1-2\lambda}\Gamma(\ell+2\lambda+m)}{(\ell-m)!(\ell+\lambda)\Gamma(\lambda)^2}.
\]
Then, simultaneously for every dimension and every \(0\le m<\ell\),
\[
\boxed{\Lambda_{\ell,m}^{(d)}(c)-\Lambda_{\ell,m+1}^{(d)}(c)
=\frac{(1-c^2)^{\lambda+m+1/2}P_m(c)P_{m+1}(c)}{N_{m+1}}.}
\]
The two adjacent polar-order levels cross at exactly \(\ell-m-1\) points in \((0,1)\); every such crossing is simple and reverses the ordering. The total number of indexed adjacent-level crossings is \(\ell(\ell-1)/2\), independent of dimension. For \(1\le j<\ell\), a consecutive triple-level coincidence occurs exactly at the positive zeros of \(P_j\), giving \(\lfloor(\ell-1)^2/4\rfloor\) indexed triple resonances. No four consecutive polar-order levels coincide at a proper cap. If \(\ell\ge2\), the uniquely largest level is \(m=\ell-1\) sufficiently close to a hemisphere and \(m=0\) sufficiently close to a point cap; moreover \(\Lambda_{\ell,\ell-1}^{(d)}(c)>\Lambda_{\ell,\ell}^{(d)}(c)\) for all \(0<c<1\).

There is also a dimension-asymptotic statement for every fixed \(\ell\), \(m\), and \(y\ge0\). Let \(\alpha=\lambda+m\), \(n=\ell-m\), and \(H_n\) be the physicists' Hermite polynomial. As \(d\to\infty\),
\[
\boxed{\Lambda_{\ell,m}^{(d)}\!\left(\frac y{\sqrt\alpha}\right)
\longrightarrow \frac{1}{2^n n!\sqrt\pi}\int_y^\infty e^{-u^2}H_n(u)^2\,du,}
\]
uniformly on compact \(y\)-intervals, provided \(y<\sqrt\alpha\). The \(\ell-m-1\) positive crossings of adjacent levels, after multiplication of their cap parameters by \(\sqrt\lambda\), converge with \(O(1/\lambda)\) coordinatewise error to the combined ordered positive zero sets of \(H_{\ell-m}\) and \(H_{\ell-m-1}\). Thus all such crossings lie within an \(O(d^{-1/2})\) belt of the hemisphere; this precisely determines the high-dimensional crossing geometry.

## Assumptions and scope
Spheres have unit radius and normalized surface measure. A polar cap means \(0<c<1\), not a full hemisphere or its antipodal complement. The degree \(\ell\) is fixed within each concentration operator, rather than a low-pass sum of degrees. The polar order \(m\) indexes the irreducible \(\mathcal H_m(S^{d-1})\) summand under the subgroup fixing the polar axis; levels are indexed by \(m\), not counted with their geometric multiplicities. The asymptotic keeps \(\ell,m\) fixed while the ambient sphere dimension tends to infinity. A triple level means three consecutive polar-order values, not an eigenspace of dimension three. The conclusions do not classify arbitrary coincidences among nonconsecutive levels or eigenvalues of a full low-pass Slepian operator.

## Proof
**1. Exact polar-order reduction.** Write \(\omega=(\sqrt{1-t^2}\,\eta,t)\) with \(\eta\in S^{d-1}\) and \(t\in[-1,1]\). The spherical volume density in this decomposition is proportional to \((1-t^2)^{\lambda-1/2}dt\,d\eta\). Separation of the spherical Laplacian and the Gegenbauer differential equation show that a basis for the \(m\)-summand of exact-degree harmonics is
\[
(1-t^2)^{m/2} C_{\ell-m}^{\lambda+m}(t)Y_{m,j}(\eta),
\qquad Y_{m,j}\in\mathcal H_m(S^{d-1}).
\]
The cap indicator is independent of \(\eta\), so orthogonality of \(Y_{m,j}\) makes the compression scalar on each summand. Since
\(P_m(t)=2^m(\lambda)_m C_{\ell-m}^{\lambda+m}(t)\), the scalar equals
\[
\Lambda_{\ell,m}^{(d)}(c)=\frac{1}{N_m}\int_c^1(1-t^2)^{\lambda+m-1/2}P_m(t)^2\,dt,
\qquad N_m=\int_{-1}^1(1-t^2)^{\lambda+m-1/2}P_m(t)^2\,dt.
\]
The standard Gegenbauer square-norm formula
\[\int_{-1}^1(1-t^2)^{\alpha-1/2}[C_r^\alpha(t)]^2\,dt
=\frac{\pi 2^{1-2\alpha}\Gamma(r+2\alpha)}{r!(r+\alpha)\Gamma(\alpha)^2}\]
with \(r=\ell-m\), \(\alpha=\lambda+m\), gives the stated \(N_m\). In particular,
\(N_{m+1}=D_mN_m\), \(D_m=(\ell-m)(\ell+m+2\lambda)>0\).

**2. Boundary-factorization identity.** Differentiating the Gegenbauer equation \((1-t^2)P''-(2\lambda+1)tP'+\ell(\ell+2\lambda)P=0\) exactly \(m\) times yields
\[
(1-t^2)P_{m+2}-(2\lambda+2m+1)tP_{m+1}+D_mP_m=0.
\]
Consequently, on setting \(F_m(t)=(1-t^2)^{\lambda+m+1/2}P_m(t)P_{m+1}(t)\), a direct derivative gives
\[
F_m'(t)=(1-t^2)^{\lambda+m-1/2}
\big[(1-t^2)P_{m+1}(t)^2-D_mP_m(t)^2\big].
\]
Divide by \(N_{m+1}=D_mN_m\) and integrate from \(c\) to \(1\). Because \(\lambda>0\), \(F_m(1)=0\). The claimed adjacent-level identity follows, with no approximation.

**3. Exact root counts.** Each \(P_m\) is a positive multiple of \(C_{\ell-m}^{\lambda+m}\), hence has \(\ell-m\) simple real roots in \((-1,1)\), symmetric about zero; \(P_m\) and its derivative \(P_{m+1}\) interlace and have no common root. For \(c>0\), their total number of positive zeros is
\[
\left\lfloor\frac{\ell-m}{2}\right\rfloor+
\left\lfloor\frac{\ell-m-1}{2}\right\rfloor=\ell-m-1.
\]
At each such zero exactly one factor of the boundary product vanishes simply. This proves all crossing and sign-change assertions. Summing over \(m=0,\ldots,\ell-1\) gives \(\ell(\ell-1)/2\).

**4. Triple coincidences and their upper length.** A triple \(\Lambda_{j-1}=\Lambda_j=\Lambda_{j+1}\) requires \(P_{j-1}P_j=P_jP_{j+1}=0\) at the same \(c>0\). If \(P_j(c)\ne0\), then \(P_{j-1}(c)=P_{j+1}(c)=0\). The differentiated Gegenbauer equation for \(P_{j-1}\) gives
\((2\lambda+2j-1)cP_j(c)=0\), a contradiction. Conversely \(P_j(c)=0\) makes both gaps vanish. A quadruple would further require \(P_{j+1}P_{j+2}=0\). At a zero of \(P_j\), simplicity gives \(P_{j+1}\ne0\), and its differential equation gives \((1-c^2)P_{j+2}=(2\lambda+2j+1)cP_{j+1}\ne0\), impossible. Summing positive zeros of \(P_j\) for \(1\le j<\ell\) gives \(\sum_{r=1}^{\ell-1}\lfloor r/2\rfloor=\lfloor(\ell-1)^2/4\rfloor\).

**5. Dominant polar orders near the two cap endpoints.** Every \(\Lambda_m(0)=1/2\). If \(P_m(0)\ne0\), then \(\Lambda_m(c)=1/2-P_m(0)^2c/N_m+O(c^3)\). If \(P_m(0)=0\), then
\(\Lambda_m(c)=1/2-P_{m+1}(0)^2c^3/(3N_m)+O(c^5)\). The latter indices are precisely those for which \(\ell-m\) is odd. For two such indices \(m,m+2\), differentiating the Gegenbauer equation at zero shows
\(P_{m+3}(0)=-D_{m+1}P_{m+1}(0)\), whence
\[
\frac{P_{m+3}(0)^2/N_{m+2}}{P_{m+1}(0)^2/N_m}=
\frac{D_{m+1}}{D_m}<1.
\]
Thus the least cubic deficit occurs uniquely at \(m=\ell-1\), proving the first endpoint assertion. Near \(c=1\), the integral in step 1 is a positive constant times \((1-c)^{\lambda+m+1/2}(1+o(1))\); the smallest exponent belongs uniquely to \(m=0\). Finally \(P_{\ell-1}(c)P_\ell(c)>0\) for \(0<c<1\), proving the stated persistent last-order gap.

**6. Hermite boundary-layer limit and zero location.** Put \(\alpha=\lambda+m\), \(n=\ell-m\). By the terminating Gegenbauer expansion,
\[
\alpha^{-n/2}C_n^\alpha(u/\sqrt\alpha)
=\sum_{k=0}^{\lfloor n/2\rfloor}
\frac{(-1)^k(\alpha)_{n-k}\alpha^{-n+k}(2u)^{n-2k}}{k!(n-2k)!}
\longrightarrow\frac{H_n(u)}{n!}
\]
coefficientwise, with an \(O(\alpha^{-1})\) error on bounded \(u\)-sets. After changing variables \(t=u/\sqrt\alpha\) in the quotient of step 1, the density is proportional to \((1-u^2/\alpha)_+^{\alpha-1/2}\), which converges to \(e^{-u^2}\). For \(\alpha\ge1\) the density is bounded above by \(e^{-u^2/2}\), while the normalized polynomial is bounded by \(C_n(1+|u|)^n\). Dominated convergence proves the asserted integral limit (indeed uniformly for \(y\) in compact sets), using \(\int_\mathbb R e^{-u^2}H_n(u)^2du=2^nn!\sqrt\pi\).

The zeros giving adjacent crossings are the positive zeros of \(C_n^{\lambda+m}\) and \(C_{n-1}^{\lambda+m+1}\). Their rescaled polynomials converge coefficientwise to \(H_n/n!\) and \(H_{n-1}/(n-1)!\), respectively. The Hermite zeros are simple and strictly interlace. By local root perturbation, each rescaled root converges with \(O(1/\lambda)\) error to its corresponding positive Hermite zero. The roots of both families remain distinct for finite \(d\) by step 3; this completes the crossing-limit conclusion.

## Verification
The accompanying reproducible checker `check.py` independently verifies the differentiated polynomial identity and its exact boundary reduction for Gegenbauer parameters \(\lambda\in\{1/2,1,3/2,2,3\}\) and degrees \(1\le\ell\le9\). It isolates derivative roots and checks each predicted count, separately checks normalized cap integrals by numerical quadrature for dimensions \(2\le d\le7\) and degrees \(1\le\ell\le5\), and compares high-dimensional roots with Hermite limits for degrees \(2\le\ell\le8\). Its recorded run reports 1,070 assertion groups passed. These finite checks corroborate, but do not replace, the proof for all dimensions and degrees.

## Relationship to prior work
The 2020 work of Jaming and Speckbacher develops concentration estimates on two-point homogeneous spaces via the large sieve and Jacobi-polynomial ordering near an endpoint; it does not supply this all-cap, fixed-degree angular-order spectral flow. Campos and Silva (2020) develop hyperspherical associated Legendre functions in separation of variables, not cap concentration comparisons. Michel, Plattner and Seibert (2021) handle spherical-cap Slepian constructions, including spin weights, on \(S^2\); their setting and conclusions are distinct from the full \(S^d\) angular crossing classification. Peterson and Sengupta (2019), with older precursors, establish a general high-dimensional spherical-polynomial-to-Hermite limit; that ingredient is not independently claimed as novel here. An earlier result for \(S^2\) determines the corresponding Legendre angular crossings; this theorem extends the exact spectral factorization to every higher dimension and couples it to the complete Hermite-scale crossing geometry. The asserted contribution is the combined dimension-uniform spectral-flow and precise cap-boundary-layer theorem, rather than classical Gegenbauer or Hermite identities in isolation.

## Limitations
No general classification is asserted for coincidences among nonconsecutive polar orders. Dimension-asymptotic statements require fixed degree and order; no joint growing-degree estimate is supplied. The strong classical background in Gegenbauer/ultraspherical identities and the high-dimensional Hermite limit creates an unavoidable bibliographic equivalence risk. The theorem is reviewed for correctness, originality and value within this document package, but no independent mathematical audit or priority certification has been performed.

## References
1. P. Jaming and M. Speckbacher, *Concentration estimates for finite expansions of spherical harmonics on two-point homogeneous spaces via the large sieve principle*, arXiv:2004.02474 (first public version 2020-04-06), https://arxiv.org/abs/2004.02474 .
2. L. M. B. C. Campos and M. J. S. Silva, *On hyperspherical associated Legendre functions: the extension of spherical harmonics to N dimensions*, arXiv:2005.09603 (first public version 2020-05-19), https://arxiv.org/abs/2005.09603 .
3. A. Peterson and A. N. Sengupta, *Polynomials and High-Dimensional Spheres*, arXiv:1903.07697 (first public version 2019-03-18), https://arxiv.org/abs/1903.07697 .
4. V. Michel, A. Plattner and K. Seibert, *A Unified Approach to Scalar, Vector, and Tensor Slepian Functions on the Sphere and Their Construction by a Commuting Operator*, arXiv:2103.14650 (first public version 2021-03-26), https://arxiv.org/abs/2103.14650 .
5. Y. Umemura and N. Kono, *Infinite dimensional Laplacian and spherical harmonics*, Publ. RIMS 1 (1965), 163–186; classical spherical-to-Gaussian and Hermite convergence precedent, https://doi.org/10.2977/PRIMS/1195196331 .
