# A finite-dimensional correlation sign law for projection-width energies of dual norm balls

## Finding

Fix an integer \(d\ge2\) and choose \(U\) from normalized surface area on the Euclidean sphere \(\mathbb S^{d-1}\). For \(r\ge1\) define
\[
P_r(U)=\sum_{i=1}^d|U_i|^r.
\]
The quantity \(P_r\) is a geometric directional projection-width energy: if \(K_r\) is the unit \(\ell_{r/(r-1)}\) ball for \(r>1\), and the unit cube for \(r=1\), then \(P_r(U)=(w_{K_r}(U)/2)^r\).

**Theorem.** For every integer \(m\ge2\) and every real \(r\ge1\),
\[
\operatorname{sgn}\operatorname{Cov}(P_r,P_{2m})
=\operatorname{sgn}(r-2).
\]
In particular, covariance is strictly negative when \(1\le r<2\), vanishes at the Euclidean exponent \(r=2\), and is strictly positive for every \(r>2\). The classification is exact in every finite dimension, not merely in a high-dimensional limit.

Put \(a=r/2\) and define the rising gamma quotient \((z)_t=\Gamma(z+t)/\Gamma(z)\). For \(z>0\), let
\[
F_z(a,m)=a\sum_{k=0}^{m-1}\frac{(z+a)_k}{(z+1)_k}.
\]
The theorem includes the exact covariance formula
\[
\boxed{\operatorname{Cov}(P_r,P_{2m})=
\frac{2d(\tfrac12)_a(\tfrac12)_m}{(\tfrac d2)_{a+m}}
\left(F_{1/2}(a,m)-F_{d/2}(a,m)\right).}
\]
For the fourth-power benchmark \(m=2\), this simplifies to
\[
\boxed{\operatorname{Cov}(P_r,P_4)=
\frac{d(\tfrac12)_a\,a(a-1)(\tfrac{d-1}{2})}
{(\tfrac d2)_{a+2}(\tfrac d2+1)}.}
\]
For instance, on \(\mathbb S^2\),
\[
\operatorname{Cov}(\|U\|_1,\|U\|_4^4)=-\frac1{40},
\qquad \operatorname{Var}(\|U\|_4^4)=\frac{16}{525}.
\]

The sign is not a trivial consequence of ordering two deterministic power sums: for example, the probability vectors \(z=(1/2,1/2,0)\) and \(z'=(7/10,3/20,3/20)\) satisfy \(\sum_i z_i^{6/5}>\sum_i (z'_i)^{6/5}\) but \(\sum_i z_i^2<\sum_i(z'_i)^2\). The theorem proves a distributional sign that persists despite such opposite deterministic orderings.

## Assumptions and scope

The sphere has dimension \(d-1\), and the same random direction is used in both widths; the directions are not sampled independently. The covariance concerns the **powers of the half-widths**, not the unpowered widths. All sphere norms use the standard Euclidean structure. At \(r=2\), \(P_2\equiv1\). For the proof, the following stronger purely probabilistic statement is established: for any symmetric Dirichlet random vector \(Z\sim\operatorname{Dirichlet}(\alpha,\ldots,\alpha)\), with \(d\ge2\), \(\alpha>0\), real \(a>0\) and integer \(m\ge2\), the covariance of \(\sum_i Z_i^a\) and \(\sum_i Z_i^m\) has sign \(a-1\).

## Proof

**1. Spherical-to-Dirichlet reduction.** Let \(G_i\) be independent standard Gaussians and \(U=G/\|G\|_2\). Then \(Z_i=U_i^2=G_i^2/\sum_jG_j^2\) have the symmetric Dirichlet distribution with parameter \(\alpha=1/2\). Thus \(P_r=\sum_iZ_i^a\) with \(a=r/2\), while \(P_{2m}=\sum_iZ_i^m\).

**2. Exact Dirichlet covariance.** Work first with arbitrary \(\alpha>0\), and put \(D=d\alpha\). The beta integral gives, for all nonnegative real exponents \(t_i\),
\[
\mathbb E\prod_i Z_i^{t_i}=\frac{\prod_i(\alpha)_{t_i}}{(D)_{\sum_i t_i}}.
\]
Consequently
\[
\begin{aligned}
\mathbb E\sum_iZ_i^a &=\frac{d(\alpha)_a}{(D)_a},\\
\mathbb E\sum_iZ_i^m &=\frac{d(\alpha)_m}{(D)_m},\\
\mathbb E\left[(\sum_iZ_i^a)(\sum_jZ_j^m)\right]
&=\frac{d(\alpha)_{a+m}+d(d-1)(\alpha)_a(\alpha)_m}{(D)_{a+m}}.
\end{aligned}
\]
Define \(R_z=(z+a)_m/(z)_m\) and \(F_z=z(R_z-1)\). Subtraction of the product of the two expectations, using \(D/\alpha=d\), proves
\[
\operatorname{Cov}\left(\sum_iZ_i^a,\sum_jZ_j^m\right)
=\frac{d(\alpha)_a(\alpha)_m}{\alpha(D)_{a+m}}
\left(F_\alpha-F_D\right).
\]
This prefactor is strictly positive.

**3. The nonstandard sign lemma.** For every positive real \(z,a\) and integer \(m\ge1\), telescoping the successive ratios yields the exact identity
\[
\begin{aligned}
F_z=z\left(\frac{(z+a)_m}{(z)_m}-1\right)
&=z\sum_{k=0}^{m-1}
\left(\frac{(z+a)_{k+1}}{(z)_{k+1}}-\frac{(z+a)_k}{(z)_k}\right)\\
&=a\sum_{k=0}^{m-1}\frac{(z+a)_k}{(z+1)_k}.
\end{aligned}
\]
For every \(k\ge1\), its summand contains the product
\[
\frac{(z+a)_k}{(z+1)_k}=
\prod_{j=0}^{k-1}\left(1+\frac{a-1}{z+1+j}\right).
\]
When \(a>1\), each strictly positive factor is strictly decreasing in \(z\); when \(0<a<1\), each is strictly increasing; and when \(a=1\), all factors are one. Because \(m\ge2\), the \(k=1\) summand enforces strictness. Hence \(F_z\) is strictly decreasing for \(a>1\), strictly increasing for \(0<a<1\), and constant for \(a=1\).

**4. Conclusion and boundary cases.** Since \(d\ge2\), \(D=d\alpha>\alpha\). Thus \(F_\alpha-F_D\) has the sign of \(a-1\), establishing the general Dirichlet assertion. Taking \(\alpha=1/2\) establishes the stated spherical width-energy sign and covariance formula. When \(a=1\), the covariance vanishes because \(\sum_i Z_i=1\) identically. For \(m=2\), the telescoped function is \(F_z=a(2+(a-1)/(z+1))\), which gives the displayed elementary fourth-power formula. Substitution of \(d=3\) and \(a=1/2\) or \(a=2\) gives the two exact numerical examples. All formulas are finite for the stated parameters, with no limiting or boundary interchange.

## Verification

The supplied standalone `verify.py` reproduces the theorem using three independent numerical representations: mixed Dirichlet gamma moments, the telescoped rational formula, and deterministic quadrature of the circle in dimension two. It also checks the exact fourth-power simplification and compares representative cases with seeded Gaussian-direction simulations. Execution returned `VERIFY_OK 1478 checks (Dirichlet exact moment and independent spherical tests)`. These tests are finite consistency checks; the universal sign statement follows from the algebraic proof above, not from simulation.

## Relationship to prior work

The Gaussian representation of random spherical directions, normalized-volume geometric projections, and the Dirichlet moment identity are standard. Paouris, Pivovarov, and Zinn [1] prove a high-dimensional central limit theorem for random cube projections, including the one-dimensional case associated with the \(\ell_1\) norm. Sakai and Iwata [2] give sharp **deterministic** bounds between \(\ell_p\) norms of probability vectors; their Theorems 1--3 concern feasible norm regions rather than covariance under a specified Dirichlet sampling law. Kabluchko, Prochno, and Thäle [3] prove multivariate high-dimensional limit theorems for \(\ell_q\) norms and display an asymptotic covariance matrix; they do not give the finite-dimensional sign classification above. Wang, Li, and Xu [4] study symmetric-Dirichlet power sums in random polygon extrapolation, including standard moments, products, and asymptotic variance calculations, but do not state the present exact finite-dimensional cross-exponent covariance sign law. No novelty is claimed for the standard Dirichlet moment formula or these established asymptotic results.

The retained assertion is a nonasymptotic **strict sign theorem for all dimensions, all real first exponents, and every even benchmark**, together with its exact covariance formula and symmetric-Dirichlet extension. Direct literature and indexed mathematical-record comparisons did not identify this statement or a result whose hypotheses imply it, but incomplete historical indexing remains a genuine priority risk.

## Limitations

The theorem compares \(r\) with an **even integer** \(2m\ge4\); it does not classify covariance at two arbitrary real exponents. It concerns covariance of the powers \(P_r\), not arbitrary nonlinear transformations of these powers or the ordinary Pearson covariance of unpowered projection widths. Symmetry of the Dirichlet parameters and common-direction sampling matter. It makes no independence or peer-review claim and does not extend automatically to arbitrary convex bodies or non-Haar directions.

## References

1. G. Paouris, P. Pivovarov, and J. Zinn, *A central limit theorem for projections of the cube*, arXiv:1210.7012, first submitted 2012-10-25; Probability Theory and Related Fields 159 (2014), 701--719.
2. Y. Sakai and K. Iwata, *Sharp Bounds Between Two Rényi Entropies of Distinct Positive Orders*, arXiv:1605.00019, first submitted 2016-04-29.
3. Z. Kabluchko, J. Prochno, and C. Thäle, *High-dimensional limit theorems for random vectors in \(\ell_p^n\)-balls*, arXiv:1709.09470, first submitted 2017-09-27; Communications in Contemporary Mathematics 21 (2019), 1750092.
4. S. Wang, Z. Li, and W.-Q. Xu, *Nonlinear Random Extrapolation Estimates of π under Dirichlet Distributions*, Journal of Numerical Analysis and Approximation Theory (2023), online 2023-12-22, https://ictp.acad.ro/jnaat/journal/article/view/1360/1463.
