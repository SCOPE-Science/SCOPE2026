# Sharp unrestricted fourth Fourier moment on the six-mode quadratic simplex

## Finding
Let \(S=\{(i,j)\in\mathbb Z_{\ge0}^2:i+j\le2\}\), and let
\[
P(z,w)=\sum_{(i,j)\in S}c_{ij}z^iw^j,
\qquad T=\sum_{(i,j)\in S}|c_{ij}|^2.
\]
For normalized Haar measure on \(\mathbb T^2\), every complex coefficient array satisfies the **sharp** inequality
\[
\int_{\mathbb T^2}|P|^4\,dm\le\mathcal K T^2,
\quad \mathcal K=\frac{15+48\rho^2+24\rho^3+15\rho^4}{9(1+\rho^2)^2}
=2.949235612050376\ldots,
\]
where \(\rho=1.402255788644281\ldots\) is the unique positive root of
\[
2\rho^3+3\rho^2-6\rho-3=0.
\]
For \(T>0\), equality holds **if and only if** there exist \(\lambda\in\mathbb C\setminus\{0\}\), \(\eta,\xi\in\mathbb T\) such that
\[
c_{ij}=\lambda\eta^i\xi^j\times
\begin{cases}
1,&(i,j)\in\{(0,0),(2,0),(0,2)\},\\
\rho,&(i,j)\in\{(1,0),(0,1),(1,1)\}.
\end{cases}
\]
The identical optimal constant and complete equality family hold when the fourth moment is averaged over the discrete grids \(\mathbb Z_m\times\mathbb Z_n\) with \(m,n\ge5\). The cutoff is optimal for square grids: at \(m=n=4\) the continuous best constant is strictly exceeded.

## Assumptions and scope
All six coefficients are **arbitrary complex numbers**, possibly zero; the extremizers are necessarily nonzero at all six frequencies. Haar and finite-grid measures are probability measures; \(T=\|P\|_2^2\). Characters \(z,w\) are independent. The operator-norm statement is equivalently the exact \(\ell^2(S)\)-to-\(L^4(\mathbb T^2)\) synthesis norm \(\mathcal K^{1/4}\). No positivity, phase-alphabet, or uniform-amplitude hypothesis is imposed.

## Proof
**1. Reduction to nonnegative magnitudes.** Fourier orthogonality and convolution give
\[
\int|P|^4dm=\sum_{s\in S+S}\left|\sum_{u+v=s}c_uc_v\right|^2.
\]
Replacing each \(c_u\) by \(|c_u|\) does not decrease any summand. It therefore suffices to maximize the moment for six nonnegative real amplitudes.

**2. Exact six-variable identity.** Label the three corner magnitudes by
\(x_0=|c_{00}|\), \(x_1=|c_{20}|\), \(x_2=|c_{02}|\), and the opposite side-midpoint magnitudes by
\(y_0=|c_{11}|\), \(y_1=|c_{01}|\), \(y_2=|c_{10}|\).
Put \(U_i=x_i^2\), \(V_i=y_i^2\), \(X=\sum_iU_i\), \(Y=\sum_iV_i\), \(T=X+Y\).
Expanding the 15 two-sum fibers gives exactly
\[
Q:=\int\left|\sum_{u\in S}|c_u|z^{u_1}w^{u_2}\right|^4dm
=2T^2-\sum_i(U_i^2+V_i^2)
+4\sum_{i=0}^2x_{i+1}x_{i+2}V_i
+8(x_0+x_1+x_2)y_0y_1y_2,
\]
where corner indices in products are taken modulo three. Since
\[
2x_{i+1}x_{i+2}=U_{i+1}+U_{i+2}-(x_{i+1}-x_{i+2})^2,
\]
this becomes the **sum-of-squares identity**
\[
Q=2T^2+2XY-\sum_{i=0}^2(U_i+V_i)^2
-2\sum_{i=0}^2V_i(x_{i+1}-x_{i+2})^2
+8(x_0+x_1+x_2)y_0y_1y_2.\tag{1}
\]
This algebraic identity holds for every nonnegative six-tuple, including boundary points.

**3. Rigorous two-mass reduction.** Cauchy–Schwarz and arithmetic–geometric mean imply
\[
\sum_i(U_i+V_i)^2\ge\frac{T^2}{3},\quad
\sum_ix_i\le\sqrt{3X},\quad
\prod_i y_i\le(Y/3)^{3/2}.
\]
The explicit square term in (1) is nonpositive. Thus
\[
Q\le\frac53T^2+2XY+\frac83\sqrt X\,Y^{3/2}.\tag{2}
\]
For \(X,Y>0\), equality in (2) forces all \(x_i\) equal and all \(y_i\) equal: equality in the product bound forces uniform positive side-midpoints; the square term then forces uniform corners. Conversely, these configurations attain equality. At \(X=0\) or \(Y=0\), (2) gives at most \(5T^2/3\), strictly below the final optimum.

**4. One-variable sharp optimization.** Write \(r=\sqrt{Y/X}>0\). Dividing (2) by \(T^2\) gives
\[
F(r)=\frac{15+48r^2+24r^3+15r^4}{9(1+r^2)^2}.
\]
A direct derivative calculation gives
\[
F'(r)=-\frac{4r(2r^3+3r^2-6r-3)}{3(1+r^2)^3}.
\]
The cubic has exactly one positive root by Descartes' rule of signs, and changes from negative to positive across that root. Hence \(F\) strictly increases then decreases, with unique maximum \(F(\rho)=\mathcal K\). Since \(F(0)=\lim_{r\to\infty}F(r)=5/3\), no boundary extremizer is omitted. The equal-within-orbit maximizing amplitudes satisfy \(y_i/x_i=\rho\).

**5. Full complex equality classification.** At the optimum all six amplitudes are positive. Equality in the coefficient-modulus reduction therefore forces agreement of the phases of all nonzero terms in each two-sum convolution fiber. Comparing \((1,0)+(1,0)=(0,0)+(2,0)\), \((0,1)+(0,1)=(0,0)+(0,2)\), and \((1,0)+(0,1)=(0,0)+(1,1)\) yields
\[
\theta_{20}=2\theta_{10}-\theta_{00},\quad
\theta_{02}=2\theta_{01}-\theta_{00},\quad
\theta_{11}=\theta_{10}+\theta_{01}-\theta_{00}\pmod{2\pi}.
\]
Thus every extremal phase has precisely the claimed affine-character form. Conversely, these phases align every convolution fiber, and the amplitudes attain (2).

**6. Exact finite-grid threshold.** The two-sum frequencies lie in \(\{0,1,2,3,4\}^2\). Reduction of distinct sums modulo \((m,n)\) is injective when \(m,n\ge5\); finite character orthogonality therefore reproduces the identical convolution identity and all equality cases. At square grid order four, sums \((0,0)\), \((4,0)\), and \((0,4)\) alias. Taking all phases one and the above positive optimizing magnitudes makes those additional cross-products strictly positive, so the order-four sampled fourth moment exceeds \(\mathcal K T^2\). This proves sharpness of the square-grid threshold.

## Verification
The standalone `checker.py` derives the exact 27-monomial polynomial identity by independently enumerating all ordered two-sum pairs, tests the two-stage analytic majorants on 600 random complex coefficient arrays, checks a nonuniform character-phase extremizer, compares exact Fourier moments with nonalias finite-grid averages for orders 5, 6, 7, and 9, and detects alias excess at order 4. Run `python3 checker.py` using only Python 3's standard library. `checker_output.txt` records an actual successful invocation. Numerical tests are corroboration, not a substitute for the proof's universal inequalities and equality analysis.

## Relationship to prior work
A previously published six-frequency triangular-aperture computation establishes the sharp **unimodular** fourth-moment range \([48,102]\); its greatest normalized ratio is \(102/36=17/6\). The present theorem instead optimizes over **all complex amplitudes**, gives the strictly larger ratio \(\mathcal K>17/6\), and determines a necessarily nonflat corner/midpoint magnitude ratio. Neither a unimodular upper endpoint nor its phase-only equality classification implies the unrestricted synthesis norm. Ganzburg's work on multivariate polynomial inequalities and Newton polyhedra studies asymptotic constants and different metrics, rather than this finite six-mode \(\ell^2\)-to-\(L^4\) constant. Published work on multidimensional complementary Golay arrays addresses complementary pairs/quads and their correlation cancellation, not the unrestricted maximal single-array fourth moment. General Fourier convolution identities are standard and are used here without a priority claim.

## Limitations
The exact constant is only asserted for the six-mode quadratic simplex and finite grids satisfying the nonalias condition; no all-degree or arbitrary-polytopal extension follows. The order-four lower threshold concerns square grids, not an exhaustive classification of every smaller rectangle. The best-knowledge originality assessment cannot rule out unindexed earlier calculations or more general theorems not located by the described searches. The result has not undergone independent external validation.

## References
- M. I. Ganzburg, *Sharp Constants of Approximation Theory. V. An Asymptotic Equality Related to Polynomials with Given Newton Polyhedra*, arXiv:2007.08439v1, first public 2020-07-16, https://arxiv.org/abs/2007.08439.
- Z. Gu, Z. Zhou, A. R. Adhikary, Y. Feng, P. Fan, *New Constructions of Golay Complementary Pair/Array with Large Zero Correlation Zone*, arXiv:2108.05657v1, first public 2021-08-12, https://arxiv.org/abs/2108.05657.
- C. Du and Y. Jiang, *Constructions of Polyphase Golay Complementary Arrays*, arXiv:2204.09372v1, first public 2022-04-20, https://arxiv.org/abs/2204.09372.
- *Sharp fourth-moment phase rigidity for the six-point triangular Fourier aperture*, published research record 2026-10-11, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-fourth-moment-phase-rigidity-for-the-six-point-triangular--bea9cf2ed885.
