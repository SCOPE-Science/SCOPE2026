# Exact first-transition-band spherical Fourier norm and a dimension-dependent stability cusp

## Finding

Let \(d\geq1\) be an integer, let \(\sigma_d\) be normalized surface measure on \(\mathbb S^d\subset\mathbb R^{d+1}\), and let \(\mathbb P_j=\bigoplus_{k=0}^j\mathbb H_k\) denote the real spherical harmonics of degrees at most \(j\). Consider the **two-band spherical Fourier reproduction problem**
\[
\Lambda_d=\inf\{\|A\|_{C(\mathbb S^d)\to C(\mathbb S^d)}:\ A\text{ bounded and real linear},\ A|_{\mathbb P_1}=I,\ \operatorname{ran}A\subseteq\mathbb P_2\}.
\]
Then, in every dimension,
\[
\boxed{\Lambda_d=(d+1)\frac{\Gamma((d+1)/2)}{\sqrt\pi\,\Gamma((d+2)/2)}.}
\]
A globally minimizing operator is
\[
\boxed{(A_df)(x)=(d+1)\int_{\mathbb S^d}(x\cdot y)(1+x\cdot y)f(y)\,d\sigma_d(y).}
\]
It is the **unique orthogonally equivariant** minimizer. Its multipliers on degrees \(0,1,2\) are respectively \(1,1,2/(d+3)\), with all higher degrees annihilated. No assertion of uniqueness is made among non-equivariant operators.

The least positivity defect (maximal violation of the positive cone for a unital map) equals \((\Lambda_d-1)/2\). For the circle \(\Lambda_1=4/\pi\); for the ordinary sphere \(\Lambda_2=3/2\). As \(d\to\infty\), \(\Lambda_d\sim\sqrt{2d/\pi}\).

There is also a sharp **one-sided stability transition**. For real \(b\), set
\[
(T_{d,b}f)(x)=\int_{\mathbb S^d}K_{d,b}(x\cdot y)f(y)\,d\sigma_d(y),\qquad
K_{d,b}(u)=1+(d+1)u+b((d+1)u^2-1),
\]
and put \(N_d(b)=\|T_{d,b}\|\), \(c_d=\Gamma((d+1)/2)/(\sqrt\pi\Gamma(d/2))\). Thus \(A_d=T_{d,1}\). As \(\delta\to0\) through real values,
\[
\boxed{N_d(1+\delta)-\Lambda_d
=\frac{c_d}{d+1}\delta^2+B_d(\delta_+)^{d/2+1}
+O_d\!\left(|\delta|^3+(\delta_+)^{d/2+2}\right),}
\]
where \(\delta_+=\max\{\delta,0\}\) and
\[
B_d=\frac{2^{d/2}c_d\,d^{d/2+1}}{(d+1)^{d/2}(d/2)(d/2+1)}.
\]
In particular the right-hand excess in dimension one begins with \(4\delta^{3/2}/(3\pi)\), while the left-hand excess is \(\delta^2/(2\pi)+o(\delta^2)\). In dimension two the right and left quadratic coefficients are \(5/6\) and \(1/6\), respectively. For every \(d\geq3\), both sides have the same leading quadratic coefficient \(c_d/(d+1)\). The anomalous fractional cusp results from the vanishing or singularity of spherical-coordinate density at the antipodal endpoint.

## Assumptions and scope

All spaces and operators are real. An admissible \(A\) need not commute with rotations, be an integral operator, or have an absolutely continuous representing measure. The target degree two is the **first nonempty transition band** above exact reproduction through degree one. The norm is the uniform-to-uniform operator norm on continuous functions. The stability statement refers only to the complete one-parameter family of rotation-equivariant admissible operators, not to all possible non-equivariant optimizers.

The full optimization applies to every integer \(d\geq1\); all expansions in \(\delta\) hold for fixed \(d\). The first-public motivating manuscript was posted September 2, 2026; the result does not assert an all-bandwidth theorem or a dimension-uniform approximation rate.

## Proof

**1. Reduction to a single spherical multiplier.** Average any admissible \(A\) over the compact orthogonal group \(O(d+1)\), conjugating by isometric rotations. The averaged map is still admissible and its norm does not exceed \(\|A\|\). By the multiplicity-free spherical-harmonic decomposition for the real \(O(d+1)\)-action (including the standard \(O(2)\)-action at \(d=1\)), an equivariant map with range in \(\mathbb P_2\) is a scalar on each \(\mathbb H_0,\mathbb H_1,\mathbb H_2\) and vanishes on higher degrees. Its first two multipliers are fixed to one, and its last is free. With normalized reproducing kernels
\[
Z_0(u)=1,\quad Z_1(u)=(d+1)u,\quad
Z_2(u)=\frac{d+3}{2}\big((d+1)u^2-1\big),
\]
the scalar degree-two multiplier \(2b/(d+3)\) gives exactly \(K_{d,b}\). Its operator norm is \(N_d(b)=\int_{-1}^1|K_{d,b}(u)|w_d(u)\,du\), with
\[
w_d(u)=c_d(1-u^2)^{d/2-1},\qquad c_d=\frac{\Gamma((d+1)/2)}{\sqrt\pi\Gamma(d/2)}.
\]
The formula follows from rotational invariance of the kernel, the fact that \(w_d\) integrates to one, and approximation of its sign by continuous test functions. Hence the original infimum equals \(\inf_{b\in\mathbb R}N_d(b)\).

**2. A sharp dual sign certificate.** The function \(w_d\) is even. Since \(1\) and \((d+1)u^2-1\) are even,
\[
N_d(b)\geq\int_{-1}^1\operatorname{sgn}(u)K_{d,b}(u)w_d(u)\,du
=(d+1)\int_{-1}^1|u|w_d(u)\,du.
\]
At \(b=1\), the kernel factors as \(K_{d,1}(u)=(d+1)u(1+u)\), which has the same sign as \(u\) throughout \((-1,1)\). Thus equality is attained. Conversely, if equality holds for some \(b\), continuity and the strictly positive density on \((-1,1)\) force \(K_{d,b}\) to have the sign of \(u\) on both sides of zero. Hence \(K_{d,b}(0)=1-b=0\), so \(b=1\). This also proves uniqueness of the equivariant minimizer.

The beta integral gives
\[
\int_{-1}^1 |u|w_d(u)\,du
=\frac{\Gamma((d+1)/2)}{\sqrt\pi\Gamma((d+2)/2)},
\]
establishing the exact constant. The standard ratio asymptotic for Gamma functions gives the high-dimensional statement. The identity between unital operator norm and twice the negative mass plus one converts the norm into the stated positivity defect.

**3. Exact source of the asymmetric stability.** Put \(b=1+\delta\) and write
\[
K_{d,1+\delta}(u)=(d+1)u(1+u)+\delta\big((d+1)u^2-1\big).
\]
Subtracting the dual sign integral from its absolute-value integral gives an **exact** nonnegative expression: twice the integral of \(|K_{d,1+\delta}|w_d\) over those points where \(K_{d,1+\delta}\) has the wrong sign relative to \(u\). For sufficiently small nonzero \(\delta\), the sign-error region adjacent to zero has length \(|\delta|/(d+1)+O_d(\delta^2)\); the kernel there is \((d+1)u-\delta+O_d(u^2+|\delta|u^2)\). Its contribution is
\[
\frac{c_d}{d+1}\delta^2+O_d(|\delta|^3).
\]
When \(\delta<0\) this is the only sign-error component. When \(\delta>0\), a second component develops next to \(u=-1\). With \(v=u+1\), that component ends at \(v=d\delta/(d+1)+O_d(\delta^2)\), and
\[
K_{d,1+\delta}(-1+v)=d\delta-(d+1)v+O_d(\delta v+v^2),\quad
w_d(-1+v)=c_d(2v)^{d/2-1}(1+O_d(v)).
\]
Integrating twice the positive triangular profile against this endpoint density gives
\[
2c_d2^{d/2-1}\frac{(d\delta)^{d/2+1}}{(d+1)^{d/2}(d/2)(d/2+1)}
+O_d(\delta^{d/2+2})=B_d\delta^{d/2+1}+O_d(\delta^{d/2+2}).
\]
The quadratic and boundary terms exhaust the sign-error components for small \(|\delta|\), proving the expansion and its dimension-specific consequences.

## Verification

The accompanying standard-library program `verify.py` numerically integrates the kernels using independent spherical angular quadrature. It checks the exact norm for six dimensions, strict improvement at the optimizer against seven alternate multipliers per dimension, the constant-moment identity, and the one-sided asymptotic coefficients in several dimensions. It reports 60 passed checks. These finite checks are illustrative; the preceding symmetry, parity, beta-integral, and endpoint arguments establish the statements for all admissible dimensions and sufficiently small perturbations.

## Relationship to prior work

Hao-Ning Wu, *Positivity loss in bandlimited spectral reproduction on spheres* (arXiv:2609.02695, first posted September 2, 2026), defines the two-band norm and proves sharp **order** bounds in the ratio of reproduction and output bandwidths (Theorem 1.3), including a general symmetry reduction (Proposition 3.1). These known tools are credited. The exact \((L,N)=(1,2)\) invariant, explicit optimal multiplier, uniqueness within the equivariant class, and one-sided dimensional stability law above are not conclusions of the cited order estimates.

Defant, Galicer, Mansilla, Mastyło and Muro, *Minimal projections onto spaces of polynomials on real Euclidean spheres* (arXiv:2405.12123; subsequently published 2026), compute norms of true projections onto specified polynomial spaces. Defant and collaborators, *Projection Constants of Polynomial Spaces via Representation Theory* (arXiv:2609.22050, first posted September 18, 2026), develop representation-theoretic formulas for minimal projections onto invariant ranges. In both settings the operator is the identity on its **entire target**, whereas the present two-band problem permits a freely chosen multiplier on degree two. The earlier projection formulas consequently do not determine this exact two-band minimum or its perturbation cusp. Earlier de la Vallée–Poussin norm calculations are relevant to the circle case; the circle value is not independently claimed as a historically new constant.

## Limitations

The comparison with prior work is based on identifiable sources and targeted mathematical searches, not a proof of historical uniqueness; an unindexed exact generalized-projection identity could precede this statement. The proof does not identify all non-equivariant minimizers. The stability expansion covers the full one-parameter equivariant family but does not estimate distances to the optimum for arbitrary nonsymmetric maps. No numerical experiment is used to certify a universal identity. The first source principally studies approximation; the present claim is classified by its exact finite-band **spherical Fourier multiplier** content as MSC2020 42C10.

## References

1. H.-N. Wu, *Positivity loss in bandlimited spectral reproduction on spheres*, arXiv:2609.02695, first posted September 2, 2026. https://arxiv.org/abs/2609.02695
2. A. Defant, D. Galicer, M. Mansilla, M. Mastyło, S. Muro, *Minimal projections onto spaces of polynomials on real Euclidean spheres*, arXiv:2405.12123, first posted May 20, 2024; J. London Math. Soc. 113 (2026), e70429. https://arxiv.org/abs/2405.12123
3. A. Defant, D. Galicer, M. Mansilla, M. Mastyło, S. Muro, P. Zadunaisky, *Projection Constants of Polynomial Spaces via Representation Theory*, arXiv:2609.22050, first posted September 18, 2026. https://arxiv.org/abs/2609.22050
