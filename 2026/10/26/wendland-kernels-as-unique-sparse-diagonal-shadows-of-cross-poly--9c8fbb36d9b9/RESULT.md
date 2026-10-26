# Wendland kernels as unique sparse diagonal shadows of cross-polytopes

## Finding
For every integer \(k\geq1\), define \(d=3k-1\) and the regular cross-polytope
\[
 B_1^d=\bigl\{x\in\mathbb R^d:\sum_{j=1}^d|x_j|\leq1\bigr\}.
\]
Let \(X\) be uniformly distributed with respect to normalized volume on \(B_1^d\), and set \(Y=\sum_{j=1}^kX_j\). Define the integral operator \((\mathcal I f)(r)=\int_r^1 u f(u)\,du\) for \(0\leq r\leq1\), and put
\[
 W_k(r)=\mathcal I^{k-1}(1-r)^k,\qquad Z_k=2\int_0^1W_k(r)\,dr.
\]
Here \(W_1(r)=1-r\) and \(\mathcal I^0\) is the identity. **For every \(k\geq1\), the exact probability density of \(Y\) is**
\[
 p_k(y)=\begin{cases}W_k(|y|)/Z_k,&|y|\leq1,\\0,&|y|>1.\end{cases}
\]
Thus the complete one-dimensional family of normalized order-\(k-1\) Wendland radial basis functions is realized by sparse diagonal projections of uniform regular cross-polytopes. This supplies an explicit exact random sampler, using \(3k\) independent unit exponentials and \(k\) independent fair signs.

The ambient dimension is uniquely determined among all integer dimensions \(d\geq k\) if one fixes a projection onto **exactly \(k\) unit-weight coordinate directions** and requires the same normalized density: \(d=3k-1\) is necessary and sufficient. Neither statement asserts uniqueness among arbitrary convex bodies, weighted directions, or nonuniform distributions.

For example, the positive-half-axis densities are \(p_1(r)=1-r\), \(p_2(r)=\frac54(1-r)^3(1+3r)\), and \(p_3(r)=\frac32(1-r)^5(1+5r+8r^2)\), for \(0\leq r\leq1\).

## Assumptions and scope
All dimensions and sparsities are integers, \(k\geq1\) and \(d\geq k\). “Uniform” means Lebesgue measure divided by \(\operatorname{vol}(B_1^d)=2^d/d!\). The signs and exponentials in the sampling construction are mutually independent. The normalized kernels are even and supported on \([-1,1]\); the result concerns probability densities and an exact geometric realization, not a claim to have introduced the Wendland functions or their Fourier-positivity theorem.

## Proof
**1. Gamma–Dirichlet representation.** Let \(E_1,\ldots,E_{d+1}\) be independent unit exponential variables, let \(S=\sum_{i=1}^{d+1}E_i\), and let \(\varepsilon_1,\ldots,\varepsilon_d\) be independent fair signs. The vector
\[
 X_i=\varepsilon_iE_i/S\quad(1\leq i\leq d)
\]
is uniform on \(B_1^d\): normalized exponentials give the uniform Dirichlet distribution on the nonnegative \(d\)-simplex, and independent orthant signs give constant density \(d!/2^d\). The vector \((E_i/S)_{i=1}^{d+1}\) is independent of \(S\), and \(S\) has Gamma shape \(d+1\) and unit scale.

**2. All even moments of a sparse diagonal shadow.** Since \(S Y=\sum_{i=1}^k\varepsilon_iE_i\), each summand is a centered two-sided exponential with characteristic function \((1+t^2)^{-1}\). Independence gives
\[
 \mathbb E[e^{itSY}]=(1+t^2)^{-k}.
\]
Differentiating at zero and using the independence of \(S\) and \(Y\) yields, for every integer \(n\geq0\),
\[
 \mathbb E[Y^{2n}]
 =\frac{(2n)!(k)_n}{n!\,(d+1)_{2n}},
 \qquad \mathbb E[Y^{2n+1}]=0.
\]
The rising factorial \((a)_m=a(a+1)\cdots(a+m-1)\) has \((a)_0=1\). In particular,
\[
 \mathbb E[Y^2]=\frac{2k}{(d+1)(d+2)}.
\]

**3. All even moments of the iterated Wendland profile.** For every integer \(m\geq0\), repeated Fubini integration gives
\[
 \int_0^1r^mW_k(r)\,dr
 =\frac{B(m+2k-1,k+1)}{\prod_{j=0}^{k-2}(m+2j+1)},
\]
where the empty product for \(k=1\) equals \(1\). Taking the ratio at \(m=2n\) and \(m=0\), followed by duplication of rising factorials, yields
\[
 \frac{\int_0^1r^{2n}W_k(r)\,dr}{\int_0^1W_k(r)\,dr}
 =\frac{(2n)!(k)_n}{n!\,(3k)_{2n}}.
\]
Both laws are symmetric and supported on \([-1,1]\). At \(d=3k-1\) their moments agree for every nonnegative degree. Polynomial density in \(C([-1,1])\) implies equality of the probability measures; both have continuous densities in the interior, so the stated pointwise density formula follows (with the displayed continuous representatives at endpoints).

**4. Unique ambient dimension.** If a \(k\)-coordinate sparse projection from some \(B_1^d\), \(d\geq k\), has density \(W_k(|y|)/Z_k\), comparison of second moments gives \((d+1)(d+2)=(3k)(3k+1)\). The left side is strictly increasing for integers \(d\geq k\), hence \(d=3k-1\).

**5. Exact random sampler.** Draw \(3k\) independent unit exponentials and \(k\) fair signs; divide the signed sum of the first \(k\) exponentials by the sum of all \(3k\) exponentials. Steps 1–3 prove that the output has density \(W_k(|y|)/Z_k\) exactly, without rejection sampling or approximation.

## Verification
The standalone `checker.py` recomputes the projected density from the Dirichlet grouped-sign integral using exact symbolic arithmetic, independently computes \(W_k\) by repeated integration, and compares both formulas for \(1\leq k\leq6\). It also checks ten even moments per order and the second-moment dimension fingerprint (72 exact symbolic checks total). Its recorded output is in `checker_output.txt`. Execute `python checker.py` with SymPy installed. The analytical moment argument above covers every integer \(k\), whereas the finite checker does not prove the unbounded case by itself.

## Relationship to prior work
Wendland (1995) constructs and classifies the compactly supported radial functions \(\mathcal I^j(1-r)_+^{j+1}\) in one dimension and establishes positive definiteness; the functions themselves and their general positivity are **prior work**, not a new claim here. Fields–Ismail (1975) establishes general positivity statements for associated \({}_1F_2\) functions. The present claim instead identifies their **entire hierarchy of normalized profiles as exact geometric probability shadows of regular cross-polytopes**, with a uniquely determined ambient dimension and a concrete all-order sampling law. Bell (2016) presents harmonic analysis and volume facts about cross-polytopes, not this Wendland shadow identity. Literature and research-record searches for the geometric/probabilistic identification did not reveal a direct antecedent; an unlocated older special-function or kernel-probability representation remains possible.

The general sparse-shadow characteristic function, which also follows from Step 2, is
\[
 \mathbb E[e^{itY}]={}_1F_2\left(k;\frac{d+1}{2},\frac{d+2}{2};-\frac{t^2}{4}\right).
\]
This formula is useful for comparing existing positivity theorems but is not independently claimed as a new special-function positivity result.

## Limitations
The theorem is an exact one-dimensional marginal identity, not a representation of a multivariate Wendland kernel, and it requires unit weights on a fixed set of coordinate directions. Independent publication-priority audit has not been performed. Known general hypergeometric-positivity results cover some Fourier consequences and are not part of the asserted novelty. The sampling description is an exact distributional construction; practical floating-point code can introduce roundoff errors. The symbolic verifier tests finitely many orders.

## References
1. H. Wendland, “Piecewise polynomial, positive definite and compactly supported radial functions of minimal degree,” *Advances in Computational Mathematics* 4 (1995), 389–396. DOI: https://doi.org/10.1007/BF02123482 .
2. J. L. Fields and M. E. H. Ismail, “On the positivity of some \({}_1F_2\)'s,” *SIAM Journal on Mathematical Analysis* 6 (1975), 551–559. DOI: https://doi.org/10.1137/0506050 .
3. J. Bell, “The cross-polytope, the ball, and the cube,” dated 2016-03-28. https://jordanbell.info/LaTeX/mathematics/cube/ .
4. V. Lacko and R. Harman, “A conditional distribution approach to uniform sampling on spheres and balls in \(L_p\) spaces,” *Metrika* 75 (2012), 939–951. DOI: https://doi.org/10.1007/s00184-011-0360-x (bibliographic context; the geometric identification here is independently derived).
