# Critical Sobolev circle polynomials: an effective-weight limit and a sharp first correction

## Finding
Fix \(\lambda>0\) and \(0<c<1/2\). Give the unit circle normalized Haar measure \(dm=d\theta/(2\pi)\), and let \(d\nu(e^{i\theta})=(1+2c\cos\theta)\,dm\). For each integer \(n\ge1\), let \(Q_n\) be the degree-\(n\) monic polynomial orthogonal to all lower-degree polynomials under
\[
\langle f,g\rangle_n=\int f\overline g\,dm+\frac{\lambda}{n^2}\int f'\overline{g'}\,d\nu.
\]
Set
\[
\Delta=\sqrt{(1+\lambda)^2-4\lambda^2c^2},\qquad
\rho=\frac{1+\lambda-\Delta}{2\lambda c},\qquad
A=-\frac1\Delta,\qquad B=1-\frac{1+\lambda}{\Delta^2}.
\]
Then \(0<\rho<1\). Uniformly for each fixed \(R>1\) and all \(|z|\ge R\),
\[
\boxed{\frac{Q_n(z)}{z^n}=\frac1{1-q}+\frac1n\left[ A\frac{q(1+q)}{(1-q)^3}+B\frac q{(1-q)^2}\right]+O_{\lambda,c,R}(n^{-2}),\qquad q=-\frac\rho z.}
\]
The correction is nonzero as a rational function, so the order \(n^{-1}\) is sharp at every exterior point outside its zero set. The limit \(z/(z+\rho)\) varies strictly with \(\lambda\) for fixed \(c\); it is the normalized exterior Szegő function for the effective weight \(1+2\lambda c(1+\lambda)^{-1}\cos\theta\), not for the derivative weight \(d\nu\) alone.

A stronger coefficient statement holds. Writing
\[
Q_n(z)=\sum_{k=0}^{n-1}(-1)^ku_{n,k}z^{n-k},\quad u_{n,0}=1,
\]
there is a constant \(C_{\lambda,c}\) independent of \(n\) such that
\[
\max_{0\le k\le n-1}\left|u_{n,k}-\rho^k\left(1+\frac{Ak^2+Bk}{n}\right)\right|\le \frac{C_{\lambda,c}}{n^2}.
\]

## Assumptions and scope
All parameters are real with \(\lambda>0\), \(0<c<1/2\); \(n\) is any positive integer. The derivative is the complex polynomial derivative. Both measures are probability measures, continuous and bounded above and below by positive constants, and belong to the Szegő class. The inner product changes with polynomial degree, so this is not the fixed-penalty Sobolev problem. The asymptotic statement is uniform on unbounded exterior regions \(|z|\ge R>1\) after division by \(z^n\). The coefficient bound is uniform even for indices of order \(n\), without claiming a relative error there.

## Proof
**1. Exact banded Gram equations.** For nonnegative integers \(j,k\), Fourier orthogonality gives
\[
\langle z^j,z^k\rangle_n=\delta_{jk}+\frac{\lambda jk}{n^2}\bigl(\delta_{jk}+c\delta_{j,k+1}+c\delta_{j,k-1}\bigr).
\]
Since \(1\) is orthogonal to every positive power, the constant coefficient of \(Q_n\) vanishes. Thus the displayed coefficient representation exists. Orthogonality to \(z^{n-k}\), \(1\le k\le n-1\), yields
\[
\left(1+\lambda(1-k/n)^2\right)u_{n,k}
-\lambda c(1-k/n)(1-(k-1)/n)u_{n,k-1}
-\lambda c(1-k/n)(1-(k+1)/n)u_{n,k+1}=0.
\tag{1}
\]
Here \(u_{n,0}=1\), while the term involving \(u_{n,n}\) has coefficient zero and is omitted.

**2. Stable operator.** Regard (1) as a linear system for \(u_{n,1},\ldots,u_{n,n-1}\). Its real tridiagonal matrix has positive diagonal, nonpositive neighboring entries, and diagonal excess at least
\[
1+\lambda(1-2c)(1-k/n)^2\ge1.
\]
The omitted boundary entries only increase this excess. By the elementary maximum-component argument, its inverse has \(\ell^\infty\)-operator norm at most one: at an index of maximal absolute value of a vector \(x\), the corresponding absolute value of the matrix-vector product is at least \(\|x\|_\infty\). This also proves existence and uniqueness independently of the positive Gram form.

**3. Root and exact cancellation.** The number \(\rho\) is the small root of
\[
\lambda c(\rho+\rho^{-1})=1+\lambda.
\]
Consequently \(\Delta=\lambda c(\rho^{-1}-\rho)>0\). Let \(h(k)=Ak^2+Bk\) and insert
\[
v_{n,k}=\rho^k\bigl(1+h(k)/n\bigr)
\]
into the left side of (1). The coefficient of order \(n^0\), after division by \(\rho^k\), vanishes by the root identity. The coefficient of order \(n^{-1}\) is
\[
(1+\lambda)h(k)-\lambda c\bigl(\rho^{-1}h(k-1)+\rho h(k+1)\bigr)+\Delta-2k.
\]
For the linear operator in this expression, its action on \(k\) is \(\Delta\), and on \(k^2\) is \(2\Delta k-(1+\lambda)\). With \(A=-1/\Delta\) and \(B=1-(1+\lambda)/\Delta^2\), the whole first-order expression is identically zero for every integer \(k\). The remaining terms of the exact substitution have the form \(\rho^k n^{-2}P_2(k)+\rho^k n^{-3}P_3(k)\), where \(P_2,P_3\) are polynomials (depending on \(\lambda,c\), not on \(n\)). Since \(0<\rho<1\) and \(n\ge1\), their supremum over all indices is \(O_{\lambda,c}(n^{-2})\). At \(k=n-1\) the nonexistent final neighbor has zero prefactor, so the same estimate applies. The boundary data \(v_{n,0}=u_{n,0}=1\) agree.

Subtract the equations for the true vector and the comparison vector. Step 2 bounds the maximum coefficient error by the maximum residual, giving the coefficient claim. For \(n=1\) the claim is immediate because \(Q_1=z\).

**4. Exterior summation and sharpness.** Divide the polynomial by \(z^n\), insert the coefficient estimate, and set \(q=-\rho/z\). For \(|z|\ge R>1\), the sum of \(n\) coefficient errors divided by \(|z|^k\) is bounded by \(O_{\lambda,c,R}(n^{-2})\) since \(\sum_{k\ge0}R^{-k}<\infty\). The tails beyond \(k=n-1\) in the explicit geometric, first- and second-moment series are \(O_{\lambda,c,R}(n^{-2})\), in fact exponentially small. Using
\[
\sum_{k\ge0}q^k=(1-q)^{-1},\quad
\sum_{k\ge0}kq^k=q(1-q)^{-2},\quad
\sum_{k\ge0}k^2q^k=q(1+q)(1-q)^{-3}
\]
proves the announced formula. Because \(A\ne0\), its rational correction cannot vanish identically; away from its finite zero set, multiplying the difference from the limit by \(n\) gives a nonzero limit.

Finally, \(\lambda c/(1+\lambda)\) increases strictly with \(\lambda\), and \(\rho\) is the unique solution in \((0,1)\) of \(\rho/(1+\rho^2)=\lambda c/(1+\lambda)\); hence \(\rho\) increases strictly with \(\lambda\). This proves that the exterior limit cannot depend only on the fixed derivative measure.

## Verification
The standalone standard-library script `verify.py` constructs and solves the full finite Gram equations **in exact rational arithmetic** for two parameter triples with rational \(\rho\), checks orthogonality and the tridiagonal recurrence for degrees \(2\) through \(12\), checks comparison residuals, and independently runs a degree-\(300\) floating-point tridiagonal solution against the first-order coefficient prediction. Successful execution prints `FINITE_CHECKS_OK`. The uniformly valid operator bound and the polynomial cancellation above, not numerical extrapolation, prove the infinite statements.

## Relationship to prior work
Majumder and Swaminathan, *Sobolev Orthogonal Polynomials on the unit circle with varying inner product*, arXiv:2610.31994v1 (public October 22, 2026), consider the same critical coefficient \(\lambda/n^2\) for two measures. Their Theorem 3.2 and Corollary 3.2 state a limit determined only by the derivative measure. The example proved here falls under their printed measure hypotheses but has an exactly computed, nonconstant \(\lambda\)-dependent limit. In this family, the second-measure-only formula is therefore not the correct limiting expression. The present statement also provides an explicit sharp first correction and uniform coefficient control, not merely a limiting comparison. This is a precise mathematical comparison of assertions, not an assertion that their entire framework is invalid.

Castillo, Garza and Marcellán (2013) treat balanced Sobolev orthogonality with a **single common measure**, which cannot imply the two-distinct-measure example. Marcellán and Sri Ranga (2017) investigate coherent pairs with a **fixed Sobolev multiplier**; that setting does not imply this degree-dependent critical asymptotic or its first correction. Older fixed-penalty unit-circle and real-line Sobolev asymptotics also use materially different scaling.

## Limitations
This is an exact two-measure, one-Fourier-mode model, not a theorem for all Szegő-class measure pairs or other critical exponents. The result concerns monic polynomial normalization, not orthonormal leading-coefficient asymptotics. The comparison with the October 2026 source is based on the stated theorem and its hypotheses; potential future corrections to that source are unknown. Coverage by obscure earlier tridiagonal/Toeplitz asymptotic treatments cannot be excluded definitively. No independent mathematical audit has been performed.

## References
1. S. Majumder and A. Swaminathan, *Sobolev Orthogonal Polynomials on the unit circle with varying inner product*, arXiv:2610.31994v1, October 22, 2026, Sections 1 and 3, particularly Theorem 3.2. https://arxiv.org/html/2610.31994v1
2. K. Castillo, L. E. Garza and F. Marcellán, *Asymptotic behaviour of Sobolev orthogonal polynomials on the unit circle*, Integral Transforms and Special Functions **24** (2013), 23–38. DOI: 10.1080/10652469.2011.649751.
3. F. Marcellán and A. Sri Ranga, *Sobolev Orthogonal Polynomials on the Unit Circle and Coherent Pairs of Measures of the Second Kind*, Results in Mathematics **71** (2017), 1127–1149. DOI: 10.1007/s00025-016-0631-y. Open manuscript: https://repositorio.unesp.br/bitstreams/301c5e4c-5839-4538-82d5-7150f4f63184/download
