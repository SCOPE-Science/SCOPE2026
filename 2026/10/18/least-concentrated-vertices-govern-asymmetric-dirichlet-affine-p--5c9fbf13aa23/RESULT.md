# Least-concentrated vertices govern asymmetric Dirichlet affine-projection stability

## Finding
Let \(m\ge2\), let \(\boldsymbol\alpha=(\alpha_1,\ldots,\alpha_m)\) have strictly positive coordinates, and write \(A=\sum_{i=1}^m\alpha_i\) and \(a_*=\min_i\alpha_i\). On the standard simplex \(\Delta_{m-1}\), equip the space of functions with the probability measure \(\mu_{\boldsymbol\alpha}=\operatorname{Dirichlet}(\boldsymbol\alpha)\). Denote by \(P_{\boldsymbol\alpha}\) the \(L^2(\mu_{\boldsymbol\alpha})\)-orthogonal projection onto the affine functions.

Define, for \(0<a<A\),
\[
F_A(a)=1+2\left[A I_{a/(A+1)}(a,A-a)-(A+1)I_{a/(A+1)}(a+1,A-a)\right],
\]
where \(I_t(u,v)=B(u,v)^{-1}\int_0^t s^{u-1}(1-s)^{v-1}\,ds\) is the regularized incomplete beta function. Then
\[
\boxed{\|P_{\boldsymbol\alpha}\|_{L^\infty\to L^\infty}=\|P_{\boldsymbol\alpha}\|_{L^1\to L^1}=F_A(a_*) .}
\]
Moreover, the pointwise Lebesgue function \(\Lambda_{\boldsymbol\alpha}(x)\) attains its global maximum *exactly* at the vertices \(e_i\) satisfying \(\alpha_i=a_*\). The function \(a\mapsto F_A(a)\) is continuous and strictly decreasing on \((0,A)\).

Consequently, among all positive parameter vectors of length \(m\) having a prescribed total concentration \(A\), the **unique minimizer** of the sharp endpoint projection norm is the balanced vector \(\alpha_i=A/m\); its minimum is \(F_A(A/m)\). The supremum of these norms over the same positive parameter simplex is \(1+2A\), approached as a coordinate tends to zero, but never attained with every parameter positive.

For any fixed positive fractions \(p_1,\ldots,p_m\) summing to one, put \(\alpha_i=A p_i\). With \(p_*=\min_i p_i\), the large-concentration stability law is
\[
\boxed{\lim_{A\to\infty}\frac{\|P_{A\boldsymbol p}\|}{\sqrt A}=\sqrt{\frac2\pi}\sqrt{\frac{1-p_*}{p_*}} .}
\]
The same limit applies separately to both endpoint norms. For example, at \(\boldsymbol\alpha=(1,2,5)\) the sharp norm is approximately \(6.01539817632102571\); balancing the same total \(A=8\) reduces it to approximately \(3.48181400685446193\).

## Assumptions and scope
The simplex is \(\Delta_{m-1}=\{x\in[0,1]^m:\sum_i x_i=1\}\), with the usual Dirichlet probability law, and all \(\alpha_i>0\). The operator is the **unconstrained, affine \(L^2\)-orthogonal projector** with respect to that law. The explicit finite-rank integral kernel extends it to bounded operators on \(L^1(\mu_{\boldsymbol\alpha})\) and \(L^\infty(\mu_{\boldsymbol\alpha})\). Every assertion holds for real or complex inputs. No claim is made about degree-two projection, different probability laws, interpolation, or multi-element finite-element coupling. The \(A\to\infty\) asymptotic assumes fixed \(m\) and fixed strictly positive fractions \(p_i\).

## Proof
**Kernel reconstruction.** The barycentric coordinate functions \(y\mapsto y_i\), \(1\le i\le m\), span the affine polynomial space because \(\sum_i y_i=1\). Their Gram matrix satisfies
\[
G_{ij}=\mathbb E[Y_iY_j]=\frac{\alpha_i\alpha_j+\delta_{ij}\alpha_i}{A(A+1)},
\quad
(G^{-1})_{ij}=\frac{A(A+1)}{\alpha_i}\delta_{ij}-A.
\]
The inverse is verified by direct multiplication (or a rank-one inversion formula). Hence the reproducing kernel is
\[
K_{\boldsymbol\alpha}(x,y)=A(A+1)\sum_{i=1}^m\frac{x_i y_i}{\alpha_i}-A,
\qquad
(P_{\boldsymbol\alpha}f)(x)=\int K_{\boldsymbol\alpha}(x,y)f(y)\,d\mu_{\boldsymbol\alpha}(y).
\]
It is real symmetric, continuous on the compact simplex, and integrates to one in either argument. It reproduces each coordinate, so this is indeed the orthogonal projector. The usual duality and kernel-norm identities give equal \(L^1\) and \(L^\infty\) norms, each equal to \(\max_x\Lambda_{\boldsymbol\alpha}(x)\), where \(\Lambda_{\boldsymbol\alpha}(x)=\mathbb E|K_{\boldsymbol\alpha}(x,Y)|\). In the \(L^1\) case the boundary supremum is understood by approximation from the interior, where the Dirichlet density is positive.

**Rigid vertex localization.** For every \(x\in\Delta_{m-1}\),
\[
K_{\boldsymbol\alpha}(x,Y)=\sum_{i=1}^m x_i K_{\boldsymbol\alpha}(e_i,Y),
\quad
\Lambda_{\boldsymbol\alpha}(x)\le\sum_i x_i\Lambda_{\boldsymbol\alpha}(e_i)
\le\max_i\Lambda_{\boldsymbol\alpha}(e_i).
\]
If \(x\) has at least two positive components, choose distinct such indices \(i,j\). On an open set of positive Dirichlet measure near \(Y=e_i\), the two kernel values \(K(e_i,Y)>0\) and \(K(e_j,Y)<0\) have opposite signs. The triangle inequality is therefore strict after integration, regardless of the values of the other components. Thus every maximizing point must be a vertex, and a vertex maximizes precisely when its individual kernel norm is largest.

**Exact vertex integral.** At \(e_i\), writing \(a=\alpha_i\), the random variable \(Y_i\) has the beta law \(\operatorname{Beta}(a,A-a)\). The kernel value is
\[
Z_a=\frac{A(A+1)}aY_i-A,
\qquad \mathbb E Z_a=1.
\]
Its negative part is supported exactly where \(Y_i<a/(A+1)\). Since \(\mathbb E|Z_a|=1+2\mathbb E(Z_a)_-\), beta integration and the first truncated beta moment give
\[
\mathbb E(Z_a)_-=A I_{a/(A+1)}(a,A-a)-(A+1)I_{a/(A+1)}(a+1,A-a).
\]
This proves \(\Lambda(e_i)=F_A(\alpha_i)\).

**Strict ordering across unequal parameters.** Fix \(0<a<b<A\). Take independent unit-scale gamma variables \(U\), \(V\), and \(W\) with respective shapes \(a\), \(b-a\), and \(A-b\), and set \(T=U+V+W\). Then \(Y_a=U/T\sim\operatorname{Beta}(a,A-a)\) and \(Y_b=(U+V)/T\sim\operatorname{Beta}(b,A-b)\). Conditional on \(Y_b\), the beta splitting property gives \(\mathbb E[Y_a/a\mid Y_b]=Y_b/b\). Thus, with \(Z_a=A(A+1)Y_a/a-A\) and \(Z_b=A(A+1)Y_b/b-A\),
\[
\mathbb E[Z_a\mid Y_b]=Z_b.
\]
Conditional Jensen yields \(F_A(a)=\mathbb E|Z_a|\ge\mathbb E|Z_b|=F_A(b)\). The inequality is **strict**: on the positive-probability event \(Y_b>a/(A+1)\), the conditional beta-split density has support spanning values that make \(Z_a\) both negative and positive. Therefore strict Jensen applies on that event. Continuity follows from the beta-integral representation. Combining this strict ordering with vertex localization proves the exact maximizing-vertex classification and the norm formula.

**Optimal distribution of total concentration.** With \(\sum_i\alpha_i=A\), one always has \(a_*\le A/m\), with equality if and only if all \(\alpha_i=A/m\). Since \(F_A\) decreases strictly, the balanced vector is the unique minimizer. For a fixed \(A>0\) and \(a\downarrow0\), the gamma representation gives \(Y_a/a\to0\) in probability: the Laplace transform of a gamma variable \(U_a/a\) with shape \(a\) is \((1+t/a)^{-a}\to1\), while the remaining denominator converges to a positive gamma variable. The bounded negative part \((A-A(A+1)Y_a/a)_+\) consequently converges in mean to \(A\). Hence \(F_A(a)\to1+2A\); for every positive \(a\), the negative part has expectation strictly less than \(A\). This proves the strict, nonattained concentration-budget supremum.

**Gaussian large-concentration regime.** If \(a=Ap\) with fixed \(0<p<1\), then \(Y_a\sim\operatorname{Beta}(Ap,A(1-p))\) satisfies \(\sqrt A(Y_a-p)\Rightarrow N(0,p(1-p))\). Since \(Z_a=1+(A+1)(Y_a-p)/p\), it follows that \(Z_a/\sqrt A\Rightarrow N(0,(1-p)/p)\). Furthermore \(\mathbb E[Z_a^2]/A\) stays bounded, by the exact beta variance \(p(1-p)/(A+1)\), so the absolute first moments are uniformly integrable. Thus \(F_A(Ap)/\sqrt A\to\sqrt{2/\pi}\sqrt{(1-p)/p}\). Applying the exact minimum-parameter characterization gives the stated norm asymptotic.

## Verification
The accompanying `check_dirichlet_affine.py` checks 241 finite assertions using exact-rational Dirichlet Gram matrices, explicit inverses, polynomial-reproduction identities, independent high-precision beta quadrature (with an endpoint-singularity-removing substitution), strict parameter ordering on finite test grids, interior-point comparisons in one-dimensional simplexes, fixed-proportion Gaussian scaling, and vanishing-shape behavior. The included examples are reproduced with 45-decimal-digit `mpmath`. Run `python check_dirichlet_affine.py` with Python 3 and `mpmath` installed. These finite tests do not prove a universal ordering or any asymptotic; the arguments above supply the infinite-parameter proofs.

## Relationship to prior work
Griffiths and Spanò, *Orthogonal polynomial kernels and canonical correlations for Dirichlet measures* (Bernoulli 2013, originally public in March 2010), provide the general Dirichlet orthogonal-polynomial kernel framework. In particular, their degree-one kernel in Section 2.2 is an acknowledged exact input. Their investigation concerns orthogonal kernels, canonical correlations and Pólya urns, not the sharp endpoint norm, concentration-allocation optimizer or vertex classification established here.

A published finite-element note, *Exact positivity defect and max norm of the affine least-squares projector on a simplex* (2026), treats the uniformly weighted simplex: it yields the specialization \(\alpha_i=1\) but not heterogeneous Dirichlet parameters or the strict allocation ordering. Classical symmetric-Dirichlet formulas likewise correspond to the diagonal case \(\alpha_1=\cdots=\alpha_m\), which alone cannot identify the worst vertex under asymmetry or solve the total-concentration minimax problem. Arab, Oliveira and Wiklund (2021) study convex-transform orders for beta distributions; their transform-order characterization is different from the conditional mean-preserving beta splitting used here and does not state the projector stability theorem.

## Limitations
Only the affine degree-one projector is addressed. The fixed-proportion Gaussian asymptotic does not cover simultaneous vanishing proportions, and no sharp rates are claimed. The proof uses standard Dirichlet moment identities, beta-gamma splitting and a strictly convex-order comparison of a particular absolute deviation; those ingredients are acknowledged rather than asserted to be new separately. Bibliographic priority is provisional: complete texts of some potentially relevant general orthogonal-polynomial papers were unavailable, and an equivalent formulation under weighted projector terminology could exist.

## References
1. R. C. Griffiths and D. Spanò, *Orthogonal polynomial kernels and canonical correlations for Dirichlet measures*, Bernoulli **19** (2013), 548–598, DOI: 10.3150/11-BEJ403; preprint arXiv:1003.5131 (first public 2010-03-26). Full text: https://warwick.ac.uk/fac/sci/statistics/staff/academic-research/spano/pub/bej403.pdf.
2. Y. Xu, *Hahn, Jacobi, and Krawtchouck polynomials of several variables*, arXiv:1309.1510 (2013); full-text access not established in this examination.
3. I. Arab, P. E. Oliveira and T. Wiklund, *Convex transform order of Beta distributions with some consequences*, Statistica Neerlandica **75** (2021), 238–256, DOI: 10.1111/stan.12233.
4. *Exact positivity defect and max norm of the affine least-squares projector on a simplex* (public mathematical record, 2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-positivity-defect-and-max-norm-of-the-affine-least-squares--99c2b9dd9b34.
