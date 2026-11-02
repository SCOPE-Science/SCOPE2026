# Sharp Dirichlet-weighted affine projection norm and the rare-vertex concentration transition

## Finding
Let \(n\ge2\), let \(\alpha_1,\ldots,\alpha_n>0\), and equip the barycentric simplex \(\Delta_{n-1}\) with the Dirichlet probability measure \(\mu_{\boldsymbol\alpha}\). Put \(A=\sum_i\alpha_i\), \(a=\min_i\alpha_i\), and let \(P_{\boldsymbol\alpha}\) be the \(L^2(\mu_{\boldsymbol\alpha})\)-orthogonal projector onto all real affine functions on the simplex.

For \(u,v>0\) define the regularized incomplete beta function
\[
I_t(u,v)=\frac{\int_0^t s^{u-1}(1-s)^{v-1}\,ds}{\int_0^1 s^{u-1}(1-s)^{v-1}\,ds},\qquad 0\le t\le1.
\]
Set \(t=a/(A+1)\). The exact induced endpoint norm is
\[
\boxed{\ \|P_{\boldsymbol\alpha}\|_{L^\infty(\mu_{\boldsymbol\alpha})\to L^\infty(\mu_{\boldsymbol\alpha})}
=1+2\left[A I_t(a,A-a)-(A+1)I_t(a+1,A-a)\right].\ }
\]
The supremum of the absolute reproducing-kernel row integral occurs **exactly** at the simplex vertices with the smallest Dirichlet parameter. The sign of such a vertex's kernel row attains the operator norm. The corresponding sharp negative excursion of the projection on inputs \(0\le f\le1\) is the bracketed quantity in the display.

For each fixed total concentration \(A>0\) and fixed \(n\ge2\), the unique parameter vector minimizing the norm has \(\alpha_1=\cdots=\alpha_n=A/n\). Over all strictly positive parameter vectors of total \(A\), the sharp supremum is \(1+2A\); it is not attained.

Two dimension-growth regimes are distinct. When \(\alpha_i=\alpha>0\) for all \(i\),
\[
\lim_{n\to\infty}\frac{\|P_{\boldsymbol\alpha}\|}{n}
=\frac{2\alpha^\alpha e^{-\alpha}}{\Gamma(\alpha)}.
\]
When \(\alpha_i=\theta/n\) for all \(i\), with \(\theta>0\) fixed,
\[
\lim_{n\to\infty}\|P_{\boldsymbol\alpha}\|=1+2\theta.
\]
Thus maintaining per-coordinate concentration yields linear amplification, whereas maintaining total concentration yields finite amplification.

## Assumptions and scope
The standard barycentric simplex is
\[
\Delta_{n-1}=\{x\in[0,1]^n:\sum_{i=1}^n x_i=1\}.
\]
The probability measure has density proportional to \(\prod_i x_i^{\alpha_i-1}\) with respect to \((n-1)\)-dimensional simplex volume; all parameters are strictly positive and no boundary atoms are present. The target space consists of functions \(x\mapsto\sum_i c_i x_i\). The input consists of bounded measurable real functions, modulo \(\mu_{\boldsymbol\alpha}\)-null sets. The projected output is affine and continuous, so its essential supremum agrees with its maximum on the closed simplex. No claim concerns arbitrary non-Dirichlet measures or higher polynomial degree. An affine change of geometric simplex coordinates leaves all the statements unchanged.

## Proof
**1. Reproducing kernel.** Let \(Y\sim\operatorname{Dirichlet}(\alpha_1,\ldots,\alpha_n)\) and \(p_i=\alpha_i/A\). Standard Dirichlet moments, which follow by integrating the density, give
\[
G_{ij}=\mathbb E(Y_iY_j)
=\frac{\alpha_i(\alpha_j+\delta_{ij})}{A(A+1)}
=\frac{p_i\delta_{ij}+A p_ip_j}{A+1}.
\]
Since all \(p_i>0\), the barycentric Gram matrix is nonsingular; direct multiplication or the rank-one inverse formula yields
\[
G^{-1}=(A+1)\operatorname{diag}(p_1^{-1},\ldots,p_n^{-1})-A\mathbf1\mathbf1^{\mathsf T}.
\]
Consequently the orthogonal projection kernel is
\[
K(x,y)=x^{\mathsf T}G^{-1}y
=(A+1)\sum_{i=1}^n\frac{x_i y_i}{p_i}-A.
\]
It reproduces constants, so \(\mathbb E K(x,Y)=1\) for every \(x\).

**2. Only vertices can maximize the absolute row norm.** For every barycentric \(x\), \(K(x,y)=\sum_i x_iK(e_i,y)\). Hence convexity gives
\[
\mathbb E|K(x,Y)|\le\sum_i x_i\mathbb E|K(e_i,Y)|.
\]
For any distinct \(i,j\), a positive-measure neighborhood near \(e_i\) has \(K(e_i,y)>0>K(e_j,y)\): at \(y=e_i\), the former equals \((A+1)/p_i-A>0\) and the latter equals \(-A\). If \(x\) has at least two positive barycentric coordinates, the absolute-value triangle inequality is therefore strict on a positive-measure set (choose any two such coordinates). Thus every global row maximizer is a vertex, and no nonvertex can tie a maximizing vertex.

**3. Endpoint beta expression.** At vertex \(e_i\),
\[
K(e_i,Y)=A\left(\frac{A+1}{\alpha_i}Y_i-1\right),
\qquad Y_i\sim\operatorname{Beta}(\alpha_i,A-\alpha_i).
\]
Its sign changes at \(Y_i=\alpha_i/(A+1)\). Using \(\mathbb E K(e_i,Y)=1\),
\[
\mathbb E|K(e_i,Y)|=1+2\mathbb E[-K(e_i,Y)]_+.
\]
Writing \(a_i=\alpha_i\), \(t_i=a_i/(A+1)\), the truncated first beta moment is
\[
\mathbb E\big[Y_i\mathbf1_{\{Y_i<t_i\}}\big]
=\frac{a_i}{A}I_{t_i}(a_i+1,A-a_i).
\]
Therefore
\[
\mathbb E[-K(e_i,Y)]_+
=A I_{t_i}(a_i,A-a_i)-(A+1)I_{t_i}(a_i+1,A-a_i).
\]
The bounded input \(f(y)=\operatorname{sgn}K(e_i,y)\) realizes the absolute row integral at \(e_i\). The indicator of the negative row region realizes the negative excursion on \([0,1]\)-valued inputs.

**4. A strict ordering by the smallest shape parameter.** Keep \(A\) fixed and choose \(0<a<b<A\). Couple beta variables via a unit-scale gamma process \(G(s)\) with independent gamma increments. Put \(X_a=G(a)/G(A)\) and \(X_b=G(b)/G(A)\). Conditional on \(G(b),G(A)\), beta splitting gives
\[
\mathbb E\left[\frac{X_a}{a}\,\middle|\,G(b),G(A)\right]=\frac{X_b}{b}.
\]
Conditional Jensen for the convex function \(z\mapsto|A(A+1)z-A|\) proves
\[
\mathbb E\left|A(A+1)\frac{X_a}{a}-A\right|
\ge\mathbb E\left|A(A+1)\frac{X_b}{b}-A\right|.
\]
The inequality is strict. Indeed the conditional law of \(X_a/a\) has full support between zero and \(X_b/a\), and on the positive-probability event \(X_b>a/(A+1)\) that interval straddles the unique kink \(1/(A+1)\). Hence the largest vertex norm corresponds exactly to the smallest \(\alpha_i\). Together with Step 2 this proves the formula and the stated spatial extremizers.

**5. Optimization at fixed total concentration.** Every positive parameter vector of total \(A\) has \(a\le A/n\), with equality only when all parameters are equal. By the strict ordering proved in Step 4, the uniform vector uniquely minimizes the norm. Conversely, the kernel at any vertex is bounded below by \(-A\), and its mean is one. Therefore \(\mathbb E|K|=1+2\mathbb E[-K]_+<1+2A\), with strictness because \(\mathbb P(K>0)>0\). This yields the universal strict upper bound.

For sharpness, let the smallest shape \(a\downarrow0\) with total \(A\) fixed, distributing the remaining positive mass among the other coordinates. For any \(0<q<1\), beta moments give
\[
\mathbb E\left(\frac{Y_i}{a}\right)^q
=\frac{\Gamma(a+q)\Gamma(A)}{a^q\Gamma(a)\Gamma(A+q)}
=O(a^{1-q})\longrightarrow0.
\]
Thus \(Y_i/a\to0\) in probability and \([-K(e_i,Y)]_+\to A\) in probability. Because this negative part lies between zero and \(A\), its expectation tends to \(A\). The supremum \(1+2A\) follows, and it is not attained for positive parameters.

**6. Dimension asymptotics.** In the symmetric case \(\alpha_i=\alpha\), write \(Y_1=U/(U+V_n)\) with independent \(U\sim\operatorname{Gamma}(\alpha,1)\) and \(V_n\sim\operatorname{Gamma}((n-1)\alpha,1)\). Then \(nY_1\Rightarrow U/\alpha\) and
\[
\frac{K(e_1,Y)}n=(n\alpha+1)Y_1-\alpha\Rightarrow U-\alpha.
\]
The exact beta second moment gives \(\sup_{n\ge2}\mathbb E(nY_1)^2<\infty\), so the displayed family is uniformly integrable. Hence its absolute first moments converge. A gamma density integral, or one incomplete-gamma recurrence, gives
\[
\mathbb E|U-\alpha|
=2\frac{\alpha^\alpha e^{-\alpha}}{\Gamma(\alpha)}.
\]
This proves the first asymptotic formula.

For \(\alpha_i=\theta/n\), the total concentration is \(A=\theta\) and \(\mathbb EY_1=1/n\). Thus \(Y_1\to0\) in probability. Since \(K(e_1,Y)=n(\theta+1)Y_1-\theta\), its negative part is bounded by \(\theta\) and converges in probability to \(\theta\). Therefore \(\mathbb E[-K(e_1,Y)]_+\to\theta\), yielding the second asymptotic formula.

## Verification
Run `python3 verify.py` from the extracted package directory (Python standard library only). The checker exactly inverts barycentric moment matrices for 360 nonuniform integer-shape profiles, tests 7,650 inverse-matrix coefficients, compares two independently formed exact beta-integral expressions in 1,638 cases, checks 7,650 parameter-order instances, 406 fixed-total inequalities and 99 uniform-simplex specializations. All pass. The underlying theorem for arbitrary positive real parameters, the strict gamma-bridge ordering and infinite-dimensional asymptotic limits follow from the written proofs, not the finite checks.

## Relationship to prior work
Aktaş and Xu (2011, arXiv:1111.2994v1) develop Jacobi orthogonal-polynomial systems on a simplex with the same general positive-exponent weights; their main questions concern polynomial eigenbases and singular Sobolev extensions, not the degree-one endpoint projection norm or its optimal parameter design. Palombi and Toti (2014/2015, arXiv:1407.7404) use Dirichlet-weighted orthogonality and Ritz–Galerkin approximations on simplexes in fluctuation models; their analysis raises positivity and stability questions but does not state the present exact norm, strict shape-parameter ordering, or concentration transitions.

The published note *Exact positivity defect and max norm of the affine least-squares projector on a simplex* (published-finding corpus, 2026) proves the **unweighted** \(\alpha_i=1\) specialization. In fact our formula reduces in that case to the already known value \(2n(n/(n+1))^{n-1}-1\); that specialization is expressly **not** a novelty claim. The new claimed content is the full arbitrary positive Dirichlet-parameter norm, proof that only minimum-parameter vertices extremize, unique minimax design for fixed total concentration, sharp unattained envelope \(1+2A\), and the two differing high-dimensional concentration regimes. Those conclusions do not follow solely from the unweighted formula.

## Limitations
The result is for real affine \(L^2\)-projection on one full Dirichlet-weighted simplex, not arbitrary weights, boundary atoms, global continuous finite elements, other \(L^p\) norms, or higher-degree Jacobi projection. The sign extremizer is a discontinuous essentially bounded function. The norm can be read as a sharp conditioning and positivity-loss constant, not as a convergence rate for a numerical algorithm. A priority risk remains that an equivalent endpoint result could appear in older multivariate Jacobi or weighted finite-element literature under different notation. Finite exact checks do not eliminate that risk.

## References
1. R. Aktaş and Y. Xu, *Sobolev Orthogonal Polynomials on a Simplex*, arXiv:1111.2994v1, first publicly submitted 2011-11-13. https://arxiv.org/html/1111.2994v1
2. F. Palombi and S. Toti, *Use of Dirichlet Distributions and Orthogonal Projection Techniques for the Fluctuation Analysis of Steady–State Multivariate Birth–Death Systems*, arXiv:1407.7404, 2014 preprint, version 2 dated 2015-04-30. https://arxiv.org/html/1407.7404v2
3. *Exact positivity defect and max norm of the affine least-squares projector on a simplex*, published research note (2026), published-finding corpus identifier: 2026/10/4/SCOPE-exact-positivity-defect-and-max-norm-of-the-affine-least-squares--99c2b9dd9b34. https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-positivity-defect-and-max-norm-of-the-affine-least-squares--99c2b9dd9b34
