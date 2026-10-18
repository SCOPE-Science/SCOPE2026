# Vertex–centroid positivity-loss separation for quadratic simplex projection

## Finding
Let \(d\ge2\), let \(T\) be any nondegenerate \(d\)-simplex with normalized uniform measure \(\mu\), and let \(\Pi_2\) be the \(L^2(\mu)\)-orthogonal projection onto all polynomials of total degree at most two. Write \(n=d+1\), use barycentric coordinates \(x_1,\ldots,x_n\), and let \(K_n(x,y)\) denote its reproducing kernel. The exact pointwise amplification of bounded input is
\[
\Lambda_n(x)=\sup_{\|f\|_{L^\infty}\le1}|(\Pi_2f)(x)|=\int_T|K_n(x,y)|\,d\mu(y).
\]
At every vertex \(v\), with \(t=y_1\) after relabeling,
\[
K_n(v,y)=\frac{n(n+1)}4\big[(n+2)(n+3)t^2-4(n+2)t+2\big].
\]
Define
\[
r_{n,\pm}=\frac{2(n+2)\pm\sqrt{2(n+1)(n+2)}}{(n+2)(n+3)}.
\]
Both roots lie strictly between zero and one, the kernel is negative precisely between them, and the **exact finite-dimensional vertex amplification** is
\[
\Lambda_n(v)=1-2(n-1)\int_{r_{n,-}}^{r_{n,+}}
 (1-t)^{n-2}K_n(v,t)\,dt.
\]
This is an elementary closed expression: the integrand is a polynomial for every integer \(n\). For instance, \(\Lambda_3(v)=1+128\sqrt{10}/135\).

At the barycenter \(c=(1/n,\ldots,1/n)\), put \(S(y)=\sum_{i=1}^n y_i^2\). The **exact kernel** is instead
\[
K_n(c,y)=1-\frac{(n+1)(n+2)(n+3)}{4n}
 \left(S(y)-\frac2{n+1}\right).
\]
These geometrically distinct evaluation functionals satisfy the two sharp dimension laws
\[
\boxed{\lim_{n\to\infty}\frac{\Lambda_n(v)}{n^2}
=\gamma:=(\sqrt2-1)e^{-2+\sqrt2}+(\sqrt2+1)e^{-2-\sqrt2}=0.3100125\ldots,}
\]
\[
\boxed{\lim_{n\to\infty}\frac{\Lambda_n(c)}{\sqrt n}=\frac1{\sqrt{2\pi}}.}
\]
Consequently,
\[
\frac{\Lambda_n(v)}{\Lambda_n(c)}\sim
\gamma\sqrt{2\pi}\,n^{3/2}.
\]
The **sharp positive-input undershoot at a specified evaluation point** is
\[
\sup_{0\le f\le1}[-(\Pi_2f)(x)]
=\frac{\Lambda_n(x)-1}{2}.
\]
Thus positivity loss is of quadratic order at vertices and square-root order at the barycenter. In contrast, the local affine \(L^2\) projector has kernel identically one at the barycenter and hence no positivity loss there, in every dimension. No global maximum of \(\Lambda_n(x)\) over \(T\) is asserted.

## Assumptions and scope
The projection is local to one full simplex and uses ordinary uniform-volume \(L^2\) measure, not a mass-lumped, constrained, or globally coupled finite-element projector. Degree means total polynomial degree \(\le2\), including constants and affine terms. Every statement is affine-shape invariant. The finite kernels are exact for all integers \(n\ge3\); the limits take \(n\to\infty\) with the degree fixed at two. The supremum defining \(\Lambda_n\) is over measurable essentially bounded real functions, and the equality is unchanged if continuous functions are allowed by approximation in the relevant integral.

## Proof
**1. Vertex reduction.** Under uniform measure, \(Y=(Y_1,\ldots,Y_n)\) has the Dirichlet \((1,\ldots,1)\) law; \(Y_1\) has density \((n-1)(1-t)^{n-2}\) on \((0,1)\). For a polynomial \(p\) of total degree at most two, \(\mathbb E[p(Y)\mid Y_1=t]\) is a polynomial of degree at most two in \(t\) and its value at \(t=1\) equals \(p(v)\). Therefore the multivariate vertex reproducing kernel is the one-dimensional endpoint kernel for the Beta\((1,n-1)\) weight. Inverting the \(3\times3\) moment Gram matrix \(G_{ij}=\mathbb E[Y_1^{i+j}]=(i+j)!/(n)_{i+j}\), with \(0\le i,j\le2\), gives the displayed \(K_n(v,y)\). Equivalently it is \(\binom{n+1}{2}P_2^{(n-1,0)}(2t-1)\), with the standard Jacobi normalization. Its first three moments against the Beta weight are each one when tested against \(1,t,t^2\), as required for evaluation at \(t=1\). Its quadratic discriminant is \(8(n+1)(n+2)\) before the positive prefactor, proving the stated roots; direct substitution shows \(0<r_{n,-}<r_{n,+}<1\). Since \(\int K_n(v,y)d\mu=1\), splitting the negative interval gives the exact \(L^1\) formula.

**2. Barycenter reduction.** Permutation invariance under all \(n\) barycentric coordinates forces \(K_n(c,\cdot)\), as a symmetric polynomial of degree at most two, to lie in \(\operatorname{span}\{1,S\}\). With \(\mathbb E S=2/(n+1)\) and
\[
\operatorname{Var}(S)=\frac{4(n-1)}{(n+1)^2(n+2)(n+3)},
\]
reproduction of \(1\) and \(S\), using \(S(c)=1/n\), gives
\[
K_n(c,Y)=1+\frac{S(c)-\mathbb ES}{\operatorname{Var}(S)}(S(Y)-\mathbb ES),
\]
which is precisely the stated formula. Symmetrizing any polynomial of degree at most two reduces it to \(\operatorname{span}\{1,S\}\); because the evaluation at \(c\) and the displayed kernel functional are permutation invariant, reproducing these two quantities proves reproduction of every degree-two polynomial.

For the affine projector, permutation invariance and degree at most one force its barycenter kernel to be constant; reproduction of constants makes it identically one.

**3. Vertex limit.** Set \(Z_n=nY_1\). Its exact survival probability is \(\Pr(Z_n>u)=(1-u/n)^{n-1}\) for \(0\le u\le n\), hence \(Z_n\Rightarrow Z\), where \(Z\) is exponential with mean one. The explicit kernel implies
\[
\frac{K_n(v,Y)}{n^2}\Rightarrow \frac{Z^2-4Z+2}{4}.
\]
Uniform exponential tails for \(Z_n\) imply bounded moments of every fixed order, so the absolute values are uniformly integrable. Their expectations converge to \(\frac14\mathbb E|Z^2-4Z+2|\). The polynomial changes sign at \(2\pm\sqrt2\); direct integration of \(e^{-u}(u^2-4u+2)\) on this negative interval gives exactly \(\gamma\).

**4. Barycenter limit.** Let \(E_1,E_2,\ldots\) be independent exponential random variables of mean one. Dirichlet sampling gives \(Y_i=E_i/\sum_{j=1}^nE_j\). Hence
\[
nS(Y)=\frac{n^{-1}\sum E_i^2}{(n^{-1}\sum E_i)^2}.
\]
The bivariate central limit theorem for the sample means of \(E\) and \(E^2\), followed by the delta method at \((1,2)\), yields
\[
\sqrt n\,(nS-2)\Rightarrow N(0,4),
\]
using \(\operatorname{Var}(E)=1\), \(\operatorname{Var}(E^2)=20\), and \(\operatorname{Cov}(E,E^2)=4\). Since the coefficient in the barycenter kernel is asymptotic to \(n^2/4\), it follows that \(K_n(c,Y)/\sqrt n\Rightarrow N(0,1/4)\). Moreover the reproducing identity and the exact kernel give
\[
\mathbb E K_n(c,Y)^2=K_n(c,c)
=1+\frac{(n-1)(n+2)(n+3)}{4n^2},
\]
so the squared normalized kernels have uniformly bounded expectations. This proves uniform integrability of their absolute values and consequently convergence of their means to \(\mathbb E|N(0,1/4)|=1/\sqrt{2\pi}\).

**5. Positive data.** For any fixed \(x\), \(\int K_n(x,y)d\mu=1\). The minimum of \(\int K_n(x,y) f(y)d\mu\) over \(0\le f\le1\) is \(\int\min\{K_n(x,y),0\}d\mu=(1-\Lambda_n(x))/2\), attained by the indicator of the negative-kernel set. This proves the sharp pointwise undershoot formula.

## Verification
The standalone `check.py` uses rational arithmetic for kernel moment reproduction, the Dirichlet Simpson-index variance, barycenter quadratic-monomial reproduction, and exact triangle vertex mass. It reports `VERIFY_OK exact_or_precision_checks=333`. The checker is finite corroboration: asymptotic claims follow from the explicit kernels, exponential convergence, the central limit theorem, and the uniform-integrability arguments above. An independent computation of the triangle Gram matrix produces the vertex kernel \(90t^2-60t+6\), agreeing with the general formula at \(n=3\).

## Relationship to prior work
Classical simplex Jacobi theory supplies the orthogonal basis and Beta marginal. Aktaş and Xu (2011) develop orthogonal polynomials on simplices, including singular Sobolev variants; Melenk and Wurzer (2013) prove boundary trace stability for degree-dependent \(L^2\) projections on triangles and tetrahedra. Neither inspected full text establishes this precise fixed-quadratic, growing-dimension \(L^1\)-kernel contrast. Chernov (2012) studies simplex \(L^2\) projection trace estimates; only the abstract could be accessed, so equivalent hidden coverage remains a risk. Previously published affine-simplex projection calculations establish linear-order vertex positivity loss for degree one, but do not imply the quadratic vertex scale or the square-root barycenter loss, since orthogonal-projection \(L^\infty\) norms need not be monotone under enlargement of a subspace. The vertex Jacobi formula itself is classical machinery; the claimed contribution is its pairing with the exact barycenter Simpson-index formula and the two proved, quantitatively different stability laws.

## Limitations
This result identifies exact pointwise kernels and the corresponding sharp local evaluation/undershoot norms only at vertices and barycenters. It does not determine the global \(L^\infty\)-operator norm \(\|\Pi_2\|\), prove vertices maximize the Lebesgue function, handle nonuniform Dirichlet weights, or cover polynomial degrees increasing with dimension. The leading constants and distributional limits are analytic, not experimentally certified. Equivalent historical formulations under multivariate Christoffel kernels or Dirichlet quadratic functionals remain possible; independent bibliographic assessment has not been performed.

## References
1. R. Aktaş and Y. Xu, *Sobolev orthogonal polynomials on a simplex*, arXiv:1111.2994 (first posted 2011-11-13), especially Section 2 on classical Jacobi-simplex polynomials.
2. J. M. Melenk and T. Wurzer, *On the stability of the boundary trace of the polynomial L2-projection on triangles and tetrahedra*, arXiv:1302.7189 (first posted 2013-02-28), especially Sections 1, 3 and 4.
3. A. Chernov, *Optimal convergence estimates for the trace of the polynomial L2-projection operator on a simplex*, Math. Comp. 81 (2012), 765–787, DOI:10.1090/S0025-5718-2011-02513-5.
4. Y. Xu, *Hahn, Jacobi, and Krawtchouck polynomials of several variables*, arXiv:1309.1510 (first posted 2013-09-05); continuous Jacobi basis and discrete reproducing-kernel context.
