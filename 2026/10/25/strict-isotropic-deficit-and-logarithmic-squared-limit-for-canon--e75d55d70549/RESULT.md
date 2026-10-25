# Strict isotropic deficit and logarithmic-squared limit for canonical signohedra

## Finding
For every integer \(d\ge1\), let
\[
C_d=[-1,1]^d,\qquad \Diamond_d=\operatorname{conv}\{\pm e_1,\dots,\pm e_d\},\qquad
\Sigma_d=(C_d+\Diamond_d)^\circ
=\left\{x\in\mathbb R^d:\sum_{i=1}^d|x_i|+\max_i|x_i|\le1\right\}.
\]
Write \(H_m=\sum_{k=1}^{m}1/k\) and \(H_m^{(2)}=\sum_{k=1}^{m}1/k^2\). For a uniformly volume-distributed random point \(X\in\Sigma_d\), the Euclidean volume and covariance are
\[
\boxed{\operatorname{vol}_d(\Sigma_d)=\frac{2^d}{(d+1)!}},\qquad
\boxed{\operatorname{Cov}(X)=v_d I_d,\quad
v_d=\frac{2(d+1)-H_{d+1}^2-H_{d+1}^{(2)}}{d(d+1)(d+2)}}.
\]
Normalize the affine-invariant isotropic constant by
\[
L(K)^{2d}=\frac{\det(\operatorname{Cov}(\operatorname{Unif}(K)))}{\operatorname{vol}_d(K)^2}.
\]
Then
\[
\boxed{L(\Sigma_d)=\frac{((d+1)!)^{1/d}}2\sqrt{v_d}}.
\]
Relative to the \(d\)-dimensional cross-polytope \(\Diamond_d\), whose isotropic constant is
\[
L(\Diamond_d)=\frac{(d!)^{1/d}}{\sqrt{2(d+1)(d+2)}},
\]
the **strict all-dimensional inequality** and **sharp asymptotic deficit** are
\[
\boxed{L(\Sigma_d)<L(\Diamond_d)\quad\text{for every integer }d\ge2},\qquad
\boxed{\lim_{d\to\infty}\frac{d}{(\log d)^2}\left(1-\frac{L(\Sigma_d)}{L(\Diamond_d)}\right)=\frac14}.
\]
At \(d=1\) the two isotropic constants agree. Both approach \(1/(e\sqrt2)\) as \(d\to\infty\). This comparison is for one canonical Euclidean representative; an arbitrary affine realization of the same combinatorial type has the same isotropic constant but not necessarily the stated coordinate covariance.

## Assumptions and scope
The polar \(K^\circ=\{x:\langle x,y\rangle\le1\text{ for all }y\in K\}\) is taken in the standard inner product. The standard cube and cross-polytope are both full-dimensional and centrally symmetric. Their Minkowski sum has support function \(\|x\|_1+\|x\|_\infty\), giving the displayed gauge of \(\Sigma_d\). All moments concern uniform *volume* measure, not uniform vertex measure or random directional width. A logarithm is natural, and the quantified limit is through positive integers \(d\to\infty\).

## Proof
**1. Simplex chambers and volume.** Ignore the measure-zero coordinate ties and coordinate hyperplanes. By independent sign changes and permutations, one may work on a chamber with
\[
y_1>y_2>\cdots>y_d>0,\qquad y_1+\cdots+y_d+y_1\le1.
\]
Put \(t_j=y_j-y_{j+1}\) for \(1\le j<d\), \(t_d=y_d\), and \(z_j=(j+1)t_j\). Then \(t_j\ge0\), \(\sum_{j=1}^d z_j\le1\), and
\[
y_i=\sum_{j=i}^d\frac{z_j}{j+1}.
\]
The triangular transformation from \(t\) to \(y\) has determinant one and the subsequent diagonal transformation has Jacobian \(1/(d+1)!\). A standard \(d\)-simplex has coordinate volume \(1/d!\). There are exactly \(2^d d!\) congruent chambers, proving the volume formula.

**2. Exact covariance.** Uniform volume on one chamber corresponds, after normalization, to the first \(d\) coordinates of a Dirichlet distribution with \(d+1\) parameters all equal to one. In particular,
\[
\mathbb E z_jz_k=\frac{1+\mathbf1_{\{j=k\}}}{(d+1)(d+2)}.
\]
Consequently,
\[
\mathbb E y_i^2=\frac{\left(\sum_{j=i}^d\frac1{j+1}\right)^2+\sum_{j=i}^d\frac1{(j+1)^2}}{(d+1)(d+2)}.
\]
Signs and permutations make the centroid zero, every off-diagonal covariance zero, and every diagonal equal to the average of these \(d\) square moments. To simplify their sum, write
\[
T_d=\sum_{i=1}^d\left[\left(\sum_{j=i}^d\frac1{j+1}\right)^2+\sum_{j=i}^d\frac1{(j+1)^2}\right].
\]
A direct comparison of the \(d\) and \(d-1\) summations gives
\[
T_d-T_{d-1}=\frac{2}{d+1}\left(d-H_d\right)+\frac{2d}{(d+1)^2}=2-\frac{2H_{d+1}}{d+1}.
\]
Starting with \(T_0=0\), summation yields exactly
\[
T_d=2(d+1)-H_{d+1}^2-H_{d+1}^{(2)}.
\]
Division by \(d(d+1)(d+2)\) proves the stated covariance.

**3. Comparison with the cross-polytope.** For \(Y\) uniform on \(\Diamond_d\), standard orthant-simplex integration gives \(\operatorname{vol}(\Diamond_d)=2^d/d!\) and \(\operatorname{Cov}(Y)=2I_d/((d+1)(d+2))\). Define
\[
m=d+1,\quad c_m=H_m^2+H_m^{(2)}-2,\quad R_d=\frac{L(\Sigma_d)}{L(\Diamond_d)}.
\]
The exact formulas give the equivalent comparison
\[
R_d^2=m^{2/d}\left(1-\frac{c_m}{2d}\right).
\]
For \(2\le d\le18\), the strict inequalities \(R_d<1\) are verified by the **exact rational** tests
\[
\boxed{m^2\left(\frac{2m-H_m^2-H_m^{(2)}}{2d}\right)^d<1},\quad m=d+1,
\]
one for each of these seventeen integer dimensions; the complete finite test and all rational inputs are provided in `verify.py`.

For the remaining \(d\ge19\), use \(m\ge20\). First,
\[
c_{20}>12>4\log20.
\]
The first comparison is an exact rational check; the second follows from \(e^3>20\), certified by retaining terms through degree eight of its positive Taylor series. Moreover for \(m\ge6\),
\[
(c_m-4\log m)-(c_{m-1}-4\log(m-1))
=\frac{2H_m}{m}-4\log\frac m{m-1}
>\frac{2H_m}{m}-\frac4{m-1}>0.
\]
The last inequality uses \(H_m\ge H_6=49/20>2m/(m-1)\) for all \(m\ge6\). Thus \(c_m>4\log m\) whenever \(m\ge20\). Since \(1-e^{-u}<u\) for all \(u>0\),
\[
\frac{c_m}{2d}>\frac{2\log m}{d}>1-m^{-2/d}.
\]
Therefore \(R_d^2<1\), as required. The endpoint \(d=1\) gives \(\Sigma_1=[-1/2,1/2]\), an affine copy of \(\Diamond_1=[-1,1]\), so equality holds only there.

**4. Sharp limit.** The classical harmonic estimates imply
\[
c_{d+1}=(\log d)^2+O(\log d).
\]
Consequently
\[
\log R_d=\frac{\log(d+1)}{d}+
\frac12\log\left(1-\frac{c_{d+1}}{2d}\right)
=-\frac{(\log d)^2}{4d}+O\left(\frac{\log d}{d}\right).
\]
Exponentiation gives the claimed coefficient \(1/4\). Finally Stirling's formula applied to the cross-polytope expression gives \(L(\Diamond_d)\to1/(e\sqrt2)\), hence the same limit for \(L(\Sigma_d)\).

## Verification
Running `python3 verify.py` prints `VERIFY_OK exact_dirichlet_traces=60 strict_ratios=17 planar_area=2/3 planar_variance=23/432 tail_base=20`. The exact rational checker independently recomputes the coordinate second-moment sum for dimensions \(1\) through \(60\), exhausts the seventeen exceptional dimensions for the comparison theorem, and checks the exact tail inequalities. A separate shoelace polygon computation in dimension two gives area \(2/3\) and coordinate variance \(23/432\). These finite computations are diagnostic and auxiliary; the chamber transformation, Dirichlet identities, and analytic tail are the dimension-independent proof.

## Relationship to prior work
Black and De Loera introduced the canonical signohedron as the polar of a cube–cross-polytope Minkowski sum, giving its combinatorial interpretation, facets, and vertices. Their inspected open full text does not state the volume-uniform covariance, isotropic-constant formula, comparison, or asymptotic deficit above. Independently published work on the same canonical realization gives its Euclidean inradius, circumradius, tangent facets, and finite vertex-radius shells; those **vertex and boundary** statistics do not determine **uniform interior-volume** second moments. Work on Hanner polytopes proves a sharp isotropic range *within that class*, with the cross-polytope its lower endpoint. Indeed, the canonical signohedron has \(3^d-1\) vertices for \(d\ge2\), whereas every \(d\)-dimensional Hanner polytope has at most \(2^d\) vertices: this follows inductively because Cartesian products multiply vertex counts and coordinate \(\ell_1\)-sums add them. Hence the Hanner lower bound does not govern this family, which can have a strictly smaller value. Kipp gives the normalization of isotropic constants and structural theorems for certain other polytopes, not an exact formula for this body. No matching theorem was found in the sources compared, but absence from a search index does not establish publication priority.

## Limitations
The Euclidean covariance formula concerns the fixed standard-coordinate representative. The isotropic constant is affine invariant, but the coordinate covariance formula is not. The strict inequality does not contradict a lower extremum for the cross-polytope inside the restricted Hanner class; nor is it a universal lower bound for all centrally symmetric convex bodies. There is no claim of global extremality for signohedra or of independent proof certification. Older literature on the norm \(\|x\|_1+\|x\|_\infty\) may contain an unindexed equivalent formula or inequality.

## References
1. Alexander E. Black and Jesús A. De Loera, *Monotone Paths on Cross-Polytopes*, arXiv:2102.01237, first public version 2021-02-02; Theorem 1.1(d) and Section 3. https://arxiv.org/html/2102.01237v2
2. Christian Kipp, *Isotropic constants and platonic solids*, arXiv:2407.01353, first posted 2024-07-01; equation (1.2) and introductory comparison with cross-polytopes. https://arxiv.org/abs/2407.01353
3. *Canonical signohedra are tangential with \(d\) exact radial shells*, published research record (2026), accessible result text: https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-canonical-signohedra-are-tangential-with-d-exact-radial-shells--c04451515c1c
4. *Sharp isotropic-constant range of all Hanner polytopes*, published research record (2026), accessible result text: https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-isotropic-constant-range-of-all-hanner-polytopes--7976b0937cd2
