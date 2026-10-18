# A universal rare-vertex principle for Bernoulli first-chaos multipliers

## Finding
Fix an integer \(n\geq1\). Let \(Y_1,\ldots,Y_n\) be independent Bernoulli variables with \(0<p_i<1\), and let \(\mu\) be their joint law on \(\{0,1\}^n\). Let \(r_i\) be a less likely value of \(Y_i\) (choose either value if both are equally likely), set \(a_i=\mathbb P(Y_i=r_i)=\min\{p_i,1-p_i\}\), and write
\[
\chi_i(x)=\frac{\mathbf 1_{\{x_i=r_i\}}-a_i}{\sqrt{a_i(1-a_i)}}.
\]
For arbitrary complex coefficients \(c_1,\ldots,c_n\), define the first-chaos diagonal multiplier on complex \(L^\infty(\mu)\) by
\[
(T_c f)(x)=\sum_{i=1}^n c_i\chi_i(x)\mathbb E[\chi_i(Y)f(Y)].
\]
Then **the same vertex \(x^\star=(r_1,\ldots,r_n)\) maximizes the absolute kernel-row sum for every coefficient vector**, and
\[
\boxed{\displaystyle \|T_c\|_{L^\infty(\mu)\to L^\infty(\mu)}
=\mathbb E\left|\sum_{i=1}^n c_i\frac{Z_i-a_i}{a_i}\right|,}
\qquad Z_i=\mathbf 1_{\{Y_i=r_i\}}\sim\operatorname{Bernoulli}(a_i).
\]
The same formula holds for the complex \(L^1(\mu)\)-operator norm. In particular, for the canonical first-chaos projection \(P_1=T_{(1,\ldots,1)}\) with homogeneous bias \(a_i=a\leq1/2\),
\[
\boxed{\displaystyle\|P_1\|_{L^\infty\to L^\infty}
=2n(1-a)\binom{n-1}{\lfloor na\rfloor}
 a^{\lfloor na\rfloor}(1-a)^{n-1-\lfloor na\rfloor}.}
\]
For each fixed \(0<a\leq1/2\) the norm is asymptotic to \(\sqrt{2n(1-a)/(\pi a)}\). If instead \(a=c/n\) with fixed \(c>0\) and sufficiently large \(n\), then
\[
\lim_{n\to\infty}\frac{\|P_1\|_{L^\infty\to L^\infty}}n
=2e^{-c}\frac{c^{\lfloor c\rfloor}}{\lfloor c\rfloor!}.
\]

## Assumptions and scope
The probability measure is a product of strictly positive two-point laws; the coefficients may be arbitrary complex numbers, including zeros. Every point has positive measure, so the essential supremum equals the maximum over the finite cube. The first-chaos coordinates are orthonormal in \(L^2(\mu)\). This result concerns **the specified orthogonal multiplier**, not the minimum norm among all projections onto its range, and it asserts no optimality of another projection. The rare vertex depends only on the measure, not on the multiplier. Ties at bias one-half may yield additional maximizers.

## Proof
**Kernel reduction.** Orthogonality and finite support give the integral kernel
\[
K_c(x,y)=\sum_{i=1}^n c_i\chi_i(x)\chi_i(y),
\qquad (T_cf)(x)=\mathbb E[K_c(x,Y)f(Y)].
\]
For any fixed \(x\), the largest possible modulus of the latter expression over \(\|f\|_\infty\leq1\) is \(\mathbb E|K_c(x,Y)|\). Equality follows by choosing the complex phase of \(f(y)\) to cancel that of \(K_c(x,y)\), with an arbitrary unit phase at zeros. Consequently
\[
\|T_c\|_{\infty\to\infty}=\max_x\mathbb E|K_c(x,Y)|.
\]

**A two-point convex-order lemma.** Fix \(0<a\leq1/2\) and let \(Z\sim\operatorname{Bernoulli}(a)\). Put
\[
U=\frac{Z-a}{a},\qquad V=-\frac{Z-a}{1-a},\qquad M=\frac{1-a}{a}\geq1.
\]
The variable \(U\) takes the values \(-1,M\) with respective probabilities \(1-a,a\). The variable \(V\) has mean zero and takes values only in \([-1,M]\): specifically its values are \(-1,a/(1-a)\). For every real convex function \(\varphi\) on \([-1,M]\), the secant inequality at the endpoints gives
\[
\mathbb E\varphi(V)
\leq\frac{M}{M+1}\varphi(-1)+\frac1{M+1}\varphi(M)
=\mathbb E\varphi(U).
\]
There is no smoothness assumption on \(\varphi\).

**The universal maximizing vertex.** Fix all coordinates of \(x\) except \(x_i\), and condition on the variables \(Z_j\), \(j\neq i\). Their contribution to \(K_c(x,Y)\) is then a fixed complex number \(s\). If \(x_i=r_i\), the remaining term is \(c_i U_i\); otherwise it is \(c_i V_i\). The real function \(t\mapsto|s+c_it|\) is convex on \(\mathbb R\), even for complex \(s,c_i\). Applying the convex-order lemma and averaging over the other coordinates shows that replacing \(x_i\) by \(r_i\) never decreases the row sum. Replace every coordinate successively. Thus \(x^\star\) maximizes for every \(c\), and at that vertex \(\chi_i(x^\star)\chi_i(Y)=(Z_i-a_i)/a_i\), proving the first formula. The Banach adjoint of \(T_c\) on the weighted \(L^1\) dual is \(T_{\overline c}\), so \(\|T_c\|_{1\to1}=\|T_{\overline c}\|_{\infty\to\infty}\). Complex conjugation leaves the displayed expected modulus unchanged, proving the \(L^1\) assertion.

**Homogeneous exact formula.** For \(c_i=1\) and \(a_i=a\), the first formula becomes \(a^{-1}\mathbb E|B-na|\) with \(B\sim\operatorname{Binomial}(n,a)\). Its centered mean is zero. If \(k=\lfloor na\rfloor\), then the elementary identity
\[
(j-na)\binom nj a^j(1-a)^{n-j}
=na(1-a)\bigl(\mathbb P(B_{n-1}=j-1)-\mathbb P(B_{n-1}=j)\bigr),
\]
where \(B_{n-1}\sim\operatorname{Binomial}(n-1,a)\), telescopes over \(j\geq k+1\). Therefore
\[
\mathbb E|B-na|=2na(1-a)\mathbb P(B_{n-1}=k),
\]
and the asserted closed form follows for all \(n\geq1\), including integer \(na\) and boundary binomial indices.

**Asymptotics.** At fixed \(a\), the standardized binomial variable converges to a standard normal, and its uniformly bounded second moments give uniform integrability of absolute values. This yields \(\mathbb E|B-na|\sim\sqrt{2na(1-a)/\pi}\). When \(a=c/n\), the local binomial probability in the closed form tends to \(e^{-c}c^{\lfloor c\rfloor}/\lfloor c\rfloor!\) for noninteger \(c\). At integer \(c=m\), the index remains \(m\) and the same limit holds. Both conclusions establish the limits without extrapolating finite calculations.

## Verification
The standalone `verify.py` enumerates all kernel-row sums with exact rational arithmetic for one heterogeneous product family in dimensions \(1\) through \(6\) and compares each with the rare vertex (126 inequalities). It independently checks the homogeneous binomial formula for five rational biases and dimensions \(1\) through \(12\) (60 identities). It also compares 62 kernel rows with complex coefficients. The computations test implementations and boundary conventions; the convex-order argument and telescoping establish the universal claims.

## Relationship to prior work
Kobos's work on finite-dimensional projection constants emphasizes sharp operator-norm problems for projections, particularly onto hyperplanes; its statements do not evaluate multipliers on biased product cubes. Nayar's archival study sets out the biased orthonormal Walsh coordinates but proves an \(L^2\) stability theorem for Boolean functions, not the present endpoint norm. Defant, Galicer, Mansilla, Mastyło, and Muro give exact integral formulas for invariant Fourier projections on the **uniform** Boolean cube; their first-degree uniform-measure case is encompassed here, but translation symmetry does not apply to unequal Bernoulli biases or the simultaneous extremality of the rare vertex for arbitrary complex diagonal multipliers. The contribution is the convex-order collapse of all kernel rows in the heterogeneous setting and its sharp Gaussian-to-Poisson behavior.

## Limitations
The proof does not address multipliers involving second or higher chaos, or arbitrary correlated measures, where coordinatewise replacement need not work. Nor does it determine minimum projection norms onto first-chaos subspaces. It does not classify all maximizing vertices: the rare vertex is guaranteed to be one. Although targeted searches and full relevant source sections were examined, an equivalent convex-order observation under different terminology elsewhere in the literature remains a residual originality risk.

## References
1. T. Kobos, *Hyperplanes of finite-dimensional normed spaces with the maximal relative projection constant*, arXiv:1411.6214v1 (first public 2014-11-23); Bulletin of the Australian Mathematical Society 91 (2015), 447–463. Primary MSC includes 47A30.
2. P. Nayar, *FKN Theorem on the biased cube*, arXiv:1311.3179v1 (first public 2013-11-13); Colloquium Mathematicum 137 (2014), 253–261.
3. A. Defant, D. Galicer, M. Mansilla, M. Mastyło, and S. Muro, *Asymptotic insights for projection, Gordon–Lewis and Sidon constants in Boolean cube function spaces*, arXiv:2302.00233v1 (first public 2023-02-01); full-text v2 available at arxiv.org/html/2302.00233v2.
