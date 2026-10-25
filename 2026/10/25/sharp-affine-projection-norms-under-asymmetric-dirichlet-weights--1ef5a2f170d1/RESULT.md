# Sharp affine-projection norms under asymmetric Dirichlet weights

## Finding
Let \(n\ge2\), let \(\alpha_1,\ldots,\alpha_n>0\), and set \(S=\sum_{i=1}^n\alpha_i\) and \(p_i=\alpha_i/S\). Equip the standard simplex \(\Delta_{n-1}=\{x_i\ge0,\ \sum_i x_i=1\}\) with the Dirichlet probability measure \(\mu_\alpha\) having density proportional to \(\prod_i x_i^{\alpha_i-1}\). Let \(P_\alpha\) be the \(L^2(\mu_\alpha)\)-orthogonal projector onto all affine functions (constants and coordinate functions). Define, for \(S>0\), \(0<p<1\), and \(t=Sp/(S+1)\),
\[
F_S(p)=1+2\left[S I_t(Sp,S(1-p))-(S+1)I_t(Sp+1,S(1-p))\right],
\]
where \(I_t(a,b)=B(a,b)^{-1}\int_0^t u^{a-1}(1-u)^{b-1}\,du\) is the regularized incomplete beta function.

**Sharp norm and extremizers.** The endpoint norms agree and satisfy
\[
\boxed{\|P_\alpha\|_{L^1\to L^1}=\|P_\alpha\|_{L^\infty\to L^\infty}=F_S(p_{\min}),\qquad p_{\min}=\min_i p_i.}
\]
The maximum of the \(L^\infty\) Lebesgue function over the closed simplex is attained **only** at those vertices \(e_i\) for which \(p_i=p_{\min}\). At any such vertex, the sign-valued input
\[
f_i(y)=\operatorname{sgn}\!\left(\frac{S+1}{p_i}y_i-S\right)
\]
attains the sharp \(L^\infty\)-operator norm. The \(L^1\) norm follows by kernel symmetry/duality (a point-mass input is not asserted to attain it).

**Strict weight ordering and optimal balance.** For every fixed \(S>0\), the function \(p\mapsto F_S(p)\) is strictly decreasing on \((0,1)\). Consequently, among positive parameter vectors with \(\sum_i\alpha_i=S\), the unique minimizer (up to coordinate permutation, which leaves it unchanged) is the balanced vector \(\alpha_i=S/n\). The sharp range is
\[
\boxed{F_S(1/n)\le\|P_\alpha\|<1+2S,}
\]
with equality on the left **if and only if** all \(\alpha_i\) are equal, and with the right endpoint a nonattained supremum approached by any sequence with \(p_{\min}\downarrow0\) and fixed \(S\). In particular, arbitrarily small barycentric weights govern the entire worst-case projection norm, even when the remaining weights are unequal.

**Three scaling regimes for balanced weights.** Write \(\Lambda_n(a)=\|P_{(a,\ldots,a)}\|\), with \(n\) entries. For every fixed \(a>0\),
\[
\boxed{\lim_{n\to\infty}\frac{\Lambda_n(a)}{n}=\frac{2a^a e^{-a}}{\Gamma(a)}.}
\]
For every fixed total concentration \(S>0\),
\[
\boxed{\lim_{n\to\infty}\|P_{(S/n,\ldots,S/n)}\|=1+2S,}
\]
whereas for every fixed \(n\ge2\), as \(S\to\infty\),
\[
\boxed{\lim_{S\to\infty}\frac{\|P_{(S/n,\ldots,S/n)}\|}{\sqrt S}=\sqrt{\frac{2(n-1)}{\pi}}.}
\]
Thus high-dimensional stability depends sharply on whether the total or per-coordinate Dirichlet concentration is held fixed.

## Assumptions and scope
The measure is a probability measure with every \(\alpha_i>0\); it has full support in the simplex relative topology. No singular boundary Dirichlet measures are included. Functions are real-valued, and all endpoint operator norms are induced by the usual \(L^1(\mu_\alpha)\) or \(L^\infty(\mu_\alpha)\) norm. The projection acts on the full degree-at-most-one polynomial space, not on the homogeneous degree-one component alone. The formula is invariant under affine changes of the physical simplex, provided the weights are transported in barycentric coordinates. Any assertion of a maximum at a vertex refers to the continuous affine representative of the output/Lebesgue function; although a vertex has measure zero, full support makes its supremum the essential supremum.

The proof explicitly uses beta and Dirichlet laws only as probability measures for evaluating and comparing the kernel; the claimed mathematical invariant is the sharp operator norm and its optimization within a fixed-concentration family. Primary subject: norms and approximation operators.

## Proof
**1. Reproducing kernel.** Let \(Y\sim\operatorname{Dirichlet}(\alpha_1,\ldots,\alpha_n)\). The elementary moments are
\[
\mathbb E Y_i=p_i,\qquad \mathbb E(Y_iY_j)=\frac{S p_i p_j+\delta_{ij}p_i}{S+1}.
\]
Define
\[
K(x,y)=(S+1)\sum_{i=1}^n\frac{x_i y_i}{p_i}-S.
\]
The moment identities yield \(\int K(x,y)\,d\mu_\alpha(y)=1\) and \(\int y_jK(x,y)\,d\mu_\alpha(y)=x_j\). Since \(K(x,\cdot)\) is affine, this is the reproducing kernel of the orthogonal projector onto the affine subspace. It is real and symmetric, and \(P_\alpha f(x)=\int K(x,y)f(y)\,d\mu_\alpha(y)\).

**2. Vertex reduction, strictness, and sharp input.** Because \(K(x,y)=\sum_i x_iK(e_i,y)\) and \(x_i\ge0\),
\[
L(x):=\int|K(x,y)|\,d\mu_\alpha(y)\le\sum_i x_i L(e_i)\le\max_iL(e_i).
\]
For any nonvertex \(x\), at least two distinct coordinates \(x_i,x_j\) are positive. On a positive-measure neighborhood of \(y=e_j\), \(K(e_i,y)<0<K(e_j,y)\); hence the first inequality is strict by the strict triangle inequality on that neighborhood. Full support and continuity then imply that **only** vertices maximize \(L\). For a maximizing vertex \(e_i\), the bounded measurable sign of \(K(e_i,y)\) produces \((P_\alpha f_i)(e_i)=L(e_i)\), and therefore attains the sharp \(L^\infty\) norm. Symmetry of \(K\) gives the equal \(L^1\) norm by Banach-space duality.

**3. Beta formula.** The marginal \(Y_i\) has distribution \(\operatorname{Beta}(\alpha_i,S-\alpha_i)\), and \(K(e_i,Y)=(S+1)Y_i/p_i-S\), which has expectation one. Its negative set is \(Y_i<t_i\), where \(t_i=Sp_i/(S+1)\). Hence
\[
L(e_i)=1+2\mathbb E\left[\left(S-\frac{S+1}{p_i}Y_i\right)_+\right]
=1+2\left[S I_{t_i}(\alpha_i,S-\alpha_i)-(S+1)I_{t_i}(\alpha_i+1,S-\alpha_i)\right]=F_S(p_i).
\]
The second equality uses \(\mathbb E[Y_i\mathbf1_{Y_i<t_i}]=p_i I_{t_i}(\alpha_i+1,S-\alpha_i)\). In particular, \(1<F_S(p)<1+2S\) for every \(0<p<1\), since both signs occur and the negative part is strictly less than \(S\) almost surely.

**4. Strict ordering by Dirichlet aggregation.** Fix \(S>0\) and \(0<p<q<1\). Couple random coordinates by taking
\[
(A,B,C)\sim\operatorname{Dirichlet}(Sp,S(q-p),S(1-q)).
\]
Then \(A\sim\operatorname{Beta}(Sp,S(1-p))\), \(A+B\sim\operatorname{Beta}(Sq,S(1-q))\), and the Dirichlet conditional-mean identity gives
\[
\mathbb E\!\left[\frac A p\Bigm|A+B\right]=\frac{A+B}{q}.
\]
Apply conditional Jensen to the convex function \(\phi(z)=|(S+1)z-S|\):
\[
F_S(p)=\mathbb E\phi(A/p)\ge\mathbb E\phi((A+B)/q)=F_S(q).
\]
This inequality is **strict**. Indeed, on the event \(A+B>Sp/(S+1)\), which has positive probability, the conditional law of \(A/p\) has strictly positive density throughout \((0,(A+B)/p)\), an interval straddling the kink \(S/(S+1)\) of \(\phi\). Conditional Jensen is strict there. Thus \(F_S\) is strictly decreasing. Since \(p_{\min}\le1/n\) and equality forces all \(p_i=1/n\), the fixed-total balancing result follows.

**5. Boundary supremum for fixed total concentration.** As \(p\downarrow0\) with \(S\) fixed, write \(U_p\sim\operatorname{Beta}(Sp,S(1-p))\), \(Z_p=U_p/p\). For any \(0<r<1\), the beta moment identity gives
\[
\mathbb E[Z_p^r]=p^{-r}\frac{\Gamma(Sp+r)\Gamma(S)}{\Gamma(Sp)\Gamma(S+r)}=O(p^{1-r})\longrightarrow0.
\]
Thus \(Z_p\to0\) in probability. The bounded nonnegative variable \((S-(S+1)Z_p)_+\le S\) converges in probability to \(S\); bounded convergence in expectation gives \(F_S(p)\to1+2S\). Strictness from step 3 shows this supremum is unattained with positive parameters.

**6. Three asymptotic regimes.** For fixed \(a>0\), represent the balanced Dirichlet vector as normalized independent \(G_j\sim\operatorname{Gamma}(a,1)\). The law of large numbers yields \(nY_1\Rightarrow G_1/a\). Also \(\mathbb E(nY_1)=1=\mathbb E(G_1/a)\); for nonnegative random variables this convergence together with convergence of expectations implies uniform integrability, so the convergence is in \(L^1\) under a suitable coupling. Dividing the vertex kernel by \(n\) gives
\[
\frac{K(e_1,Y)}n=\left(a+\frac1n\right)nY_1-a\ \Longrightarrow\ G_1-a
\]
with convergence of absolute expectations. The Gamma recurrence \(\gamma(a+1,a)=a\gamma(a,a)-a^a e^{-a}\) then gives
\[
\mathbb E|G_1-a|=2\mathbb E[(a-G_1)_+]=2a^a e^{-a}/\Gamma(a),
\]
proving the first limit. (Here \(\gamma\) denotes the lower incomplete gamma function.)

For fixed \(S\), write \(a=S/n\), \(p=1/n\), and apply the moment bound from step 5 to \(Z=nY_1\): for \(0<r<1\), \(\mathbb E Z^r=O(n^{r-1})\to0\). Therefore \(F_S(1/n)\to1+2S\) by the same bounded-negative-part argument.

Finally, for fixed \(n\), the multivariate Dirichlet central limit theorem (or the independent-Gamma representation and the delta method) implies that the vertex kernel, divided by \(\sqrt S\), converges in distribution to a centered Gaussian with variance \(n-1\), as \(S\to\infty\) under balanced parameters. Explicitly, \(\mathbb E K(e_1,Y)=1\) and \(\operatorname{Var}(K(e_1,Y))=(n-1)(S+1)\), so the normalized absolute values are uniformly integrable by their uniformly bounded second moments. Their expected absolute values converge to \(\sqrt{2(n-1)/\pi}\). This proves the third limit.

## Verification
The standalone `checker.py` runs deterministic exact-rational beta-integral comparisons for integer Dirichlet parameters, exact Dirichlet-moment reproducing-kernel checks, non-integer parameter ordering checks, fixed-concentration and dimension-scaling comparisons, and direct numerical integration of the absolute projection kernel on two-coordinate simplices. It passed 394 assertions when executed in an isolated file path. The checker does **not** certify all real parameters or all dimensions: the analytical arguments above prove those quantifiers. For example, at \(n=3\) and total concentration \(S=6\), the parameters \((1,2,3)\) give norm approximately \(4.55197239245552\), whereas the balanced parameters \((2,2,2)\) give approximately \(3.09055750580115\).

To reproduce with Python 3 and the `mpmath` package, place `checker.py` next to this file and execute `python checker.py`. No network access or private data is required.

## Relationship to prior work
Griffiths and Spanò (2010, arXiv:1003.5131, Proposition 2.1 and equations (2.19), (2.30)--(2.32)) developed Dirichlet orthogonal-polynomial kernels, including the first-degree kernel and its beta marginalization. The kernel itself and elementary Dirichlet aggregation are **not** claimed as new. Li (2012) treated degree-one generalized Jacobi polynomials and their tight frames. Aktas and Xu (2011) developed related Jacobi polynomial theory on simplices. These are foundational tools and adjacent polynomial-space results; the examined material does not supply the present endpoint-norm optimization.

A previously published note, *Exact positivity defect and max norm of the affine least-squares projector on a simplex* (2026), establishes the **uniform Lebesgue** special case \(\alpha_i=1\) and its dimension asymptotic. That special case is explicitly subsumed by the formula above, with \(\lim_{n\to\infty}\Lambda_n(1)/n=2/e\), and is not presented here as new. The present assertion instead covers every asymmetric positive Dirichlet parameter vector, its strictly ordered vertex sensitivities, a unique balancing optimum for a fixed total, and the fixed-total versus fixed-coordinate versus fixed-dimension scaling trichotomy.

Arab, Oliveira, and Wiklund (2020/2021) determined convex-transform ordering for beta laws and associated exceedance probabilities; that differs from the mean-normalized **ordinary convex order** established by the three-component Dirichlet coupling in step 4. Their results neither state nor directly supply the weighted affine-projector norm or the unique balancing conclusion. Searches also considered the general approximation-theoretic literature on Fourier--Jacobi Lebesgue constants, which may contain differently indexed special cases.

## Limitations
This is degree-one local projection on one Dirichlet-weighted simplex. No claim is made for higher degrees, boundary-singular limiting measures, globally coupled finite elements, or arbitrary non-Dirichlet weights. The strength of the novelty assessment is limited by the bibliographic record actually inspected; it is not a proof of historical priority. The first-degree kernel and the uniform-weight norm are prior results. The asymptotic statements distinguish fixed quantities explicitly and do not assert uniformity as both dimension and concentration vary without a specified scaling.

## References
1. Robert C. Griffiths and Dario Spanò, *n-Kernel Orthogonal Polynomials on the Dirichlet, Dirichlet-Multinomial, Poisson-Dirichlet and Ewens' Sampling Distributions, and Positive-Definite Sequences*, arXiv:1003.5131v1, first public 2010-03-26, https://arxiv.org/abs/1003.5131 ; full open manuscript https://wrap.warwick.ac.uk/id/eprint/35071/1/WRAP_Griffiths_10-07w.pdf .
2. Xiaoyang Li, *Generalised Jacobi Polynomials on a Simplex*, University of Auckland dissertation (2012), https://www.math.auckland.ac.nz/~waldron/Students/Harry/Xiaoyang_Li_Dissertation_2012.pdf .
3. Rabia Aktas and Yuan Xu, *Sobolev Orthogonal Polynomials on a Simplex*, arXiv:1111.2994v1 (2011-11-13), https://arxiv.org/abs/1111.2994 .
4. Idir Arab, Paulo Eduardo Oliveira, and Tilo Wiklund, *Convex Transform Order of Beta Distributions with Some Consequences*, arXiv:2005.08204, https://arxiv.org/pdf/2005.08204 ; *Statistica Neerlandica* 75 (2021), 238--256, DOI: 10.1111/stan.12233.
5. *Exact positivity defect and max norm of the affine least-squares projector on a simplex*, published mathematical note (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-positivity-defect-and-max-norm-of-the-affine-least-squares--99c2b9dd9b34 .
