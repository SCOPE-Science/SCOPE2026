# A sharp square-root dimension barrier for Gaussian polynomial-density optimization

## Finding

Consider the Gaussian measure-based upper hierarchy for the natural radial quadratic objective. A fixed-dimensional \(O(1/r)\) convergence theorem does not control simultaneous dimension growth. The exact finite-degree value is a least generalized Laguerre zero, and the hierarchy has a sharp degree-versus-dimension transition:

\[
\boxed{\lambda_{r,d}=2\xi_{\lfloor r/2\rfloor+1,1}^{(d/2-1)},\qquad \lambda_{r,d}\ge (\sqrt{r+d}-\sqrt r)^2.}
\]

For any integer sequence \(d_r\ge1\), if \(d_r/\sqrt r\to c<\infty\), then

\[
\boxed{\lim_{r\to\infty}\lambda_{r,d_r}=c^2/4.}
\]

If \(d_r/\sqrt r\to\infty\), the bounds diverge. Thus convergence to the true optimum zero holds **if and only if** \(d_r=o(\sqrt r)\); at the critical scale \(d_r\sim c\sqrt r\) the gap tends to the strictly positive constant \(c^2/4\) whenever \(c>0\).

## Assumptions and scope

Let \(d\in\mathbb N\), \(d\ge1\), and \(r\in\mathbb N_0\). Write \(\gamma_d\) for the standard Gaussian probability measure on \(\mathbb R^d\). The polynomial \(f_d(x)=\|x\|_2^2\) attains its global minimum zero. Define

\[
\lambda_{r,d}=\inf_{\substack{h\in\mathbb R[x_1,\ldots,x_d]\\ \deg h\le r,\ \int h^2\,d\gamma_d=1}}\int \|x\|_2^2 h(x)^2\,d\gamma_d(x).
\]

This is also the usual measure-based hierarchy over sum-of-squares densities of degree at most \(2r\), since a linear objective over the positive semidefinite Gram-matrix trace-one section attains its minimum on a rank-one matrix. Let \(L_n^{(\alpha)}\) denote the generalized Laguerre polynomial orthogonal on \((0,\infty)\) with weight \(t^\alpha e^{-t}\), \(\alpha>-1\). Its smallest positive zero is \(\xi_{n,1}^{(\alpha)}\). The dimension may vary with the degree; no assertion is made about general objective families or other reference measures.

## Proof

**1. Radial compression is exactly optimal.** For \(d\ge2\), the Fischer/spherical-harmonic decomposition orthogonally separates the polynomial space into sectors \(\|x\|^\ell Y_{\ell,j}(x/\|x\|)p(\|x\|^2)\), with \(\ell+2\deg p\le r\). In sector \(\ell\), the substitution \(t=\|x\|^2/2\) reduces the Rayleigh quotient to twice that of multiplication by \(t\) on polynomials of degree at most \(\lfloor(r-\ell)/2\rfloor\), with weight \(t^{d/2+\ell-1}e^{-t}\). Its smallest eigenvalue is twice the smallest zero of \(L_{\lfloor(r-\ell)/2\rfloor+1}^{(d/2+\ell-1)}\), by the three-term recurrence of orthogonal polynomials. The same even/odd sector decomposition works for \(d=1\), with \(\ell=0,1\). Zeros interlace strictly as polynomial degree increases, and every Laguerre zero increases strictly with its weight parameter. Consequently \(\ell=0\) is the globally minimizing sector, giving the stated exact formula. An optimizer may always be chosen radial.

For completeness, the parameter monotonicity used here follows without an unverified ordering assumption. Let \(x_1<\cdots<x_n\) be the positive zeros of \(L_n^{(\alpha)}\). At a zero, the Laguerre differential equation and its product expansion give

\[
2\sum_{j\ne i}\frac1{x_i-x_j}+\frac{\alpha+1}{x_i}-1=0.
\]

Differentiating in \(\alpha\) yields a linear system for the derivatives \(x_i'\), whose diagonal entries are \((\alpha+1)/x_i^2+2\sum_{j\ne i}(x_i-x_j)^{-2}\) and whose off-diagonal entries are \(-2(x_i-x_j)^{-2}\), with right-hand side \(1/x_i>0\). This strictly diagonally dominant irreducible Stieltjes matrix has a nonnegative inverse, so all \(x_i'>0\). Interlacing in degree follows from the symmetric irreducible tridiagonal Jacobi matrix and principal-submatrix interlacing.

**2. A dimension-dependent universal lower bound.** Expand a normalized \(h\) in the multivariate orthonormal Hermite basis, and let \(N\) be its (nonnegative) Hermite degree operator. Creation and annihilation operators satisfy \(x_i=a_i+a_i^*\), \(\sum_i\|a_i h\|_2^2=\langle Nh,h\rangle\), and \(\sum_i\|a_i^*h\|_2^2=\langle Nh,h\rangle+d\). Applying the reverse triangle inequality to the vectors \((a_i h)_i\) and \((a_i^*h)_i\) gives

\[
\int \|x\|_2^2h^2\,d\gamma_d\ge\bigl(\sqrt{\langle Nh,h\rangle+d}-\sqrt{\langle Nh,h\rangle}\bigr)^2
\ge (\sqrt{r+d}-\sqrt r)^2,
\]

because \(0\le\langle Nh,h\rangle\le r\) and the final expression decreases in the degree expectation. The case \(r=0\) has value \(d\), in agreement with both formulas.

**3. A matching critical-scale trial family.** In the normalized radial Laguerre basis of degrees \(j=0,\ldots,m=\lfloor r/2\rfloor\), multiplication by \(\|x\|^2\) has diagonal and upper off-diagonal coefficients

\[
 a_j=4j+d,\qquad b_j=2\sqrt{(j+1)(j+d/2)}.
\]

Suppose \(d=O(\sqrt r)\) and choose \(L=\lfloor r^{3/4}\rfloor\). For sufficiently large \(r\), \(m\ge L\). Define \(u_j=\sqrt{2/(L+1)}\sin(\pi(j-m+L)/(L+1))\) for \(m-L+1\le j\le m\) and zero elsewhere, and use alternating Jacobi coefficients \((-1)^ju_j\). The squared norm is one. Extend the zero sequence outside its support. The Rayleigh quotient is exactly

\[
\sum_{j=m-L+1}^{m}(a_j-b_{j-1}-b_j)u_j^2
+\sum_{j=m-L}^{m}b_j(u_{j+1}-u_j)^2.
\]

For \(j=m+O(L)\) and \(d=O(\sqrt r)\), Taylor expansion of the two square roots, with the remainder uniform on this interval, gives

\[
 a_j-b_{j-1}-b_j=\frac{(d/2-1)^2}{2j}+O\!\left(\frac{(d+2)^3}{j^2}\right)
=\frac{d^2}{4r}+o(1),
\]

uniformly over the support. The discrete Dirichlet sine identity gives \(\sum_j(u_{j+1}-u_j)^2=4\sin^2(\pi/[2(L+1)])\); since \(\max b_j=O(r)\), the second term is \(O(r/L^2)=o(1)\). Therefore

\[
 \lambda_{r,d}\le\frac{d^2}{4r}+o(1)
\]

uniformly when \(d=O(\sqrt r)\). The lower bound from Step 2 tends to \(c^2/4\) whenever \(d/\sqrt r\to c\in[0,\infty)\); the upper bound has the same limit. If \(d/\sqrt r\to\infty\), the lower bound diverges. Finally, if \(\lambda_{r,d_r}\to0\), the lower bound forces \(d_r/\sqrt r\to0\), proving the if-and-only-if statement.

## Verification

The included program `verify.py` constructs the full Hermite compression for \(1\le d\le4\), \(1\le r\le6\), and compares its smallest eigenvalue against the radial tridiagonal matrix: all 24 comparisons agree to within \(2\times10^{-12}\). It also reports the radial eigenvalue at growing degrees for critical ratios \(d/\sqrt r\) near \(1/2\), \(1\), and \(2\), alongside the analytic lower bound and predicted limit. Execute `OPENBLAS_NUM_THREADS=1 python verify.py` with NumPy and SciPy installed. These finite computations check normalization and limiting trends; they are not substitutes for the proof above.

## Relationship to prior work

Gribling, Klep and Kumar, arXiv:2610.22030v1 (October 15, 2026), establish \(O(1/r)\) convergence for each *fixed* dimension and polynomial objective attaining its minimum; Section 5.1 treats the univariate quadratic through a Hermite Jacobi matrix. Their bound has dimension-dependent constants and does not supply the joint \(d,r\) transition above. De Klerk and Laurent, arXiv:1804.05524, connect hierarchy bounds to orthogonal-polynomial zeros over a compact hypercube, not the noncompact multivariate Gaussian radial setting. Classical Laguerre theory supplies the special-function components; the contribution here is the exact *full multivariate* compression and its sharp variable-dimension hierarchy phase law, including the necessity-and-sufficiency criterion. Related asymptotic studies of varying-parameter Laguerre zeros may provide an alternative derivation.

## Limitations

The phase law concerns only the radial quadratic \(\|x\|^2\) under standard Gaussian reference measure; it is not a dimension-uniform theorem for all quadratic or polynomial objectives. The root formula uses real polynomials of total degree at most \(r\), and changing the degree convention changes constants. The conclusion is mathematical, not a floating-point solver's runtime or measured numerical accuracy. The exact root formula is classical in its radial one-variable form; an earlier result phrased through special-function zeros could imply parts of this conclusion. No external independent audit has been carried out.

## References

1. S. Gribling, I. Klep, P. Kumar, *Convergence Rates for Lasserre’s Upper-Bound Hierarchy on \(\mathbb R^d\) with Gaussian Measure*, arXiv:2610.22030v1, first public 2026-10-15. https://arxiv.org/abs/2610.22030
2. E. de Klerk and M. Laurent, *Worst-case examples for Lasserre's measure-based hierarchy for polynomial optimization on the hypercube*, arXiv:1804.05524v1 (2018). https://arxiv.org/abs/1804.05524
3. G. Szegő, *Orthogonal Polynomials*, fourth edition, American Mathematical Society, 1975 (generalized Laguerre recurrence and interlacing).
4. I. Krasikov, *On zeros of polynomials and allied functions satisfying second order differential equations*, arXiv:math/0211190 (2002), for broader extreme-zero bounds.
