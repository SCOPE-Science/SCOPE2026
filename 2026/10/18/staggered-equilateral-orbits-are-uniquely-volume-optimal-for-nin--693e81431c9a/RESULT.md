# Staggered equilateral orbits are uniquely volume-optimal for nine Gaussian coherent measurements

## Finding

Let \(\mathcal H=\operatorname{span}\{1,z,z^2/\sqrt2\}\) with its Fock-orthonormal monomial basis, and let \(\operatorname{Herm}_3\) carry the real Hilbert–Schmidt inner product. Write
\[
 v(z)=(1,z,z^2/\sqrt2)^{\mathsf T},\qquad
 \mathcal M(H)_{ij}=e^{-|z_{ij}|^2}v(z_{ij})^*H v(z_{ij}),
 \quad z_{ij}=r_i e^{i(\delta_i+2\pi j/3)},
\]
for \(i=1,2,3\), \(j=0,1,2\), \(0<r_1<r_2<r_3\), and arbitrary real offsets \(\delta_i\). The determinant is taken in the standard real Euclidean measurement coordinates and any real Hilbert–Schmidt orthonormal basis of \(\operatorname{Herm}_3\); its absolute value is independent of the latter choice.

Define
\[
\begin{aligned}
 A&=r_1(r_3^2-r_2^2),\\
 B&=r_2(r_3^2-r_1^2),\\
 C&=r_3(r_2^2-r_1^2),\qquad u_i=e^{-3i\delta_i},\\
 \Delta_2&=\prod_{1\le i<j\le3}(r_j^2-r_i^2).
\end{aligned}
\]
Then the exact nine-dimensional volume formula is
\[
 \boxed{\;|\det_{\mathbb R}\mathcal M|
 =\frac{81\sqrt3}{8}
 e^{-3\sum_i r_i^2}(r_1r_2r_3)^2\Delta_2
 |{-A u_1+B u_2-C u_3}|^2.\;}
\]
In particular, every choice of offsets gives an injective map. Nine measurements are minimal for invertibility on the nine-dimensional real space \(\operatorname{Herm}_3\).

For fixed strictly ordered radii the unique maximizing relative orientation, modulo the individual threefold vertex relabellings and a common rotation, is
\[
 \boxed{\;u_1=u_3=-u_2,\quad\text{equivalently}\quad
 \delta_1\equiv\delta_3\pmod{2\pi/3},\quad
 \delta_2\equiv\delta_1+\pi/3\pmod{2\pi/3}.\;}
\]
Thus the middle equilateral triangle is rotated by half a triangle-step. The unique minimizing relative orientation is \(u_1=u_2=u_3\). The ratio between maximal and minimal absolute determinants is exactly
\[
 \boxed{\;\left[\frac{(r_1+r_2)(r_2+r_3)}{(r_2-r_1)(r_3-r_2)}\right]^2.\;}
\]

After maximizing the orientations, the determinant has a **unique global maximizer in ordered positive radii**. The maximizer is the unique critical point of the explicitly strictly log-concave function
\[
 \mathcal J(r_1,r_2,r_3)
 =e^{-3(r_1^2+r_2^2+r_3^2)}(r_1r_2r_3)^2
 (r_2-r_1)(r_3-r_2)(r_3-r_1)^3
 (r_1+r_2)^3(r_1+r_3)(r_2+r_3)^3.
\]
It satisfies the exact identity
\[
 \boxed{\;r_1^2+r_2^2+r_3^2=3.\;}
\]
Numerically, the ordered radii are
\[
 (r_1,r_2,r_3)\approx(0.4195865012772835,\ 0.9258607660691042,\ 1.4024011586560458),
\]
and the resulting optimal absolute real determinant is approximately \(0.008239970366854745\). These decimals are approximations; the critical-point characterization and the identities above are exact.

## Assumptions and scope

The signal object is an arbitrary Hermitian matrix \(H\), **not** only a rank-one positive matrix; the samples are linear Gaussian-weighted coherent-state intensity lifts, without trace-one or positivity constraints. For a pure state, the values reduce to squared magnitudes of a degree-two Bargmann polynomial with the corresponding coefficient convention. The rows are kept **unnormalized as written**: multiplying any measurement by a radius-dependent factor would change the optimization problem. The experiment-design interpretation assumes equal independent additive noise variances on these nine raw measurements, in which case maximizing \(|\det\mathcal M|\) is equivalent to maximizing the determinant of its Fisher-information matrix. This is not a result about Poisson count noise or minimum condition number.

The global optimization is among precisely those nine-point sampling designs formed by three threefold cyclic orbits with distinct positive radii. No assertion is made about nine arbitrary points or sampling families with different orbit sizes.

## Proof

**Step 1: angular Fourier decoupling.** For each \(i\), put \(Y_{ij}=e^{r_i^2}\mathcal M(H)_{ij}\). With \(\omega=e^{2\pi i/3}\), take \(c_{is}=\frac13\sum_{j=0}^2\omega^{-sj}Y_{ij}\). Direct expansion gives
\[
 c_{i0}=H_{00}+r_i^2H_{11}+\tfrac12r_i^4H_{22},
\]
\[
 c_{i1}=e^{i\delta_i}\left(r_iH_{01}+\tfrac{r_i^3}{\sqrt2}H_{12}\right)
 +e^{-2i\delta_i}\tfrac{r_i^2}{\sqrt2}H_{20},
 \qquad c_{i2}=\overline{c_{i1}}.
\]
Here the entries of \(H\) use the ordered basis indexed by \(0,1,2\). The three real diagonal coordinates affect only \(c_{i0}\); the three independent complex upper/lower off-diagonal coordinates affect only the three complex numbers \(c_{i1}\).

**Step 2: exact real Jacobian.** The diagonal Vandermonde determinant is \(\Delta_2/2\). Multiplying the complex off-diagonal row by \(e^{-i\delta_i}\), which preserves its real Jacobian magnitude, gives the complex matrix with rows
\[
 \left(r_i,\ \tfrac{r_i^3}{\sqrt2},\ \tfrac{r_i^2u_i}{\sqrt2}\right).
\]
Its complex determinant has modulus
\[
 \tfrac12r_1r_2r_3\,|A u_1-B u_2+C u_3|.
\]
The real determinant of a complex-linear matrix equals the square modulus of its complex determinant. Passing from the six real off-diagonal Hilbert–Schmidt orthonormal coordinates to three independent complex matrix entries contributes \(2^{-3}\). At each radius the real angular Fourier map \((Y_{i0},Y_{i1},Y_{i2})\mapsto(c_{i0},\operatorname{Re}c_{i1},\operatorname{Im}c_{i1})\) has absolute determinant \(\sqrt3/18\). Undoing all three angular transforms and the nine Gaussian factors gives
\[
 (18/\sqrt3)^3\cdot(\Delta_2/2)\cdot 2^{-3}
 \cdot\bigl[(r_1r_2r_3)^2|A u_1-B u_2+C u_3|^2/4\bigr]
 \cdot e^{-3\sum r_i^2},
\]
which simplifies to the claimed coefficient \(81\sqrt3/8\).

**Step 3: universal injectivity and sharp orientation extrema.** Elementary factorization gives
\[
 B-A-C=(r_2-r_1)(r_3-r_1)(r_3-r_2)>0,
\]
\[
 A+B+C=(r_1+r_2)(r_3-r_1)(r_2+r_3).
\]
The reverse and ordinary triangle inequalities yield
\[
 B-A-C\ \le\ |-Au_1+Bu_2-Cu_3|\ \le\ A+B+C.
\]
Equality in the first inequality holds precisely when all three \(u_i\) coincide; equality in the second holds precisely when \(u_1=u_3=-u_2\). Both bounds are strictly positive. This proves universal injectivity, the exact equality cases and the determinant ratio. Fewer than nine real scalar measurements cannot span \(\operatorname{Herm}_3\) because its real dimension is nine.

**Step 4: exact unrestricted-radius optimization within the three-orbit family.** Substitute the maximizing angular value \(A+B+C\) into the determinant formula and factor all squared differences. Apart from the fixed positive coefficient \(81\sqrt3/8\), the result is precisely \(\mathcal J\) displayed above. Its logarithm is a sum of \(-3\sum_i r_i^2\), \(2\sum_i\log r_i\), and positive multiples of logarithms of the positive linear forms
\[
 r_2-r_1,\ r_3-r_2,\ r_3-r_1,\ r_1+r_2,\ r_1+r_3,\ r_2+r_3.
\]
On the convex cone \(0<r_1<r_2<r_3\), every logarithmic term is concave, while the quadratic term has Hessian \(-6I\). Consequently \(\log\mathcal J\) is strictly concave, with negative-definite Hessian everywhere. Also \(\mathcal J\) tends to zero at every finite boundary face because the corresponding positive factors vanish, and tends to zero as the largest radius tends to infinity because the negative Gaussian quadratic dominates the degree-eighteen polynomial. Hence a unique global maximizer exists in the interior, and its gradient vanishes.

For reproducibility the three exact stationary equations are
\[
\begin{aligned}
0={}&-6r_1+\tfrac2{r_1}-\tfrac1{r_2-r_1}-\tfrac3{r_3-r_1}
 +\tfrac3{r_1+r_2}+\tfrac1{r_1+r_3},\\
0={}&-6r_2+\tfrac2{r_2}+\tfrac1{r_2-r_1}-\tfrac1{r_3-r_2}
 +\tfrac3{r_1+r_2}+\tfrac3{r_2+r_3},\\
0={}&-6r_3+\tfrac2{r_3}+\tfrac1{r_3-r_2}+\tfrac3{r_3-r_1}
 +\tfrac1{r_1+r_3}+\tfrac3{r_2+r_3}.
\end{aligned}
\]
The polynomial factor of \(\mathcal J\) is homogeneous of degree eighteen. Differentiating \(\log\mathcal J(tr_1,tr_2,tr_3)\) at \(t=1\) along the maximizer gives \(18-6\sum_i r_i^2=0\), proving the exact squared-radius sum identity.

## Verification

The standalone program `verify_design.py` constructs the nine-by-nine real Hermitian measurement matrix directly from the coherent vectors, without using the analytic Fourier decomposition. It checks forty determinant comparisons at different radii and arbitrary offsets, one hundred independent Hermitian-coordinate reconstructions, one hundred twenty orientation-bound tests, eighty sampled radial competitors, and a high-accuracy numerical solution of the stationary equations and exact squared-radius invariant. Execute with Python and NumPy/SciPy using `python verify_design.py` from the directory containing the program. Finite numerical tests are sanity checks only; all global, equality and invertibility assertions follow from the preceding analytic proof.

## Relationship to prior work

Wellershoff's *On a dense set of functions determined by sampled Gabor magnitude* (arXiv:2507.14556; first public July 19, 2025) provides a recent motivation for polynomial Bargmann-phase sampling, but its sufficient-density theorem addresses **infinite** discrete sample sets and a broader signal class. It does not give the exact Hermitian measurement determinant or optimize nine threefold orbits.

Sych, Řeháček, Hradil, Leuchs, and Sánchez-Soto, *Informational completeness of continuous-variable measurements* (arXiv:1211.4967), establish rank counts for multiple homodyne quadrature settings in truncated Fock spaces. Their sensing operators and sampling variables are different: their rank count alone neither implies this coherent-state determinant nor its angular extrema or unique radial optimum.

Nunn and collaborators, *Optimal experiment design revisited: fair, precise and minimal tomography* (arXiv:0911.4310), optimize state-estimation criteria and measurement-resource allocation; their experimental-information objective is not the determinant of these nine fixed-variance raw Gaussian intensity lifts. Earlier work on three-by-three Cartesian coherent sampling supplies injectivity for a different geometry but does not imply the cyclic angular rigidity or the D-optimal radii here. The general fields of coherent-state experimental design and phase retrieval are broad; an unindexed earlier equivalent calculation cannot be excluded by the searches performed.

## Limitations

This is a mathematically complete result **within the specified nine-node three-equilateral-orbit design family**. It makes no assertion of D-optimality among arbitrary nine-point coherent measurement placements, no statistical optimality for nonidentical or signal-dependent noise, no sharp condition-number claim, and no general statement for higher-degree Fock polynomials. Exact algebraic closed forms for individual optimum radii are not supplied; unique implicit equations and certified structural identities suffice for the theorem. Historical priority remains subject to independent literature assessment; no independent scientific audit has been performed.

## References

1. M. Wellershoff, *On a dense set of functions determined by sampled Gabor magnitude*, arXiv:2507.14556, first version July 19, 2025, https://arxiv.org/abs/2507.14556.
2. D. Sych, J. Řeháček, Z. Hradil, G. Leuchs, L. L. Sánchez-Soto, *Informational completeness of continuous-variable measurements*, arXiv:1211.4967 (2012), https://arxiv.org/abs/1211.4967.
3. J. Nunn et al., *Optimal experiment design revisited: fair, precise and minimal tomography*, arXiv:0911.4310 (2009), https://arxiv.org/abs/0911.4310.
