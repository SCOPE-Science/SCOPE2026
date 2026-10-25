# Strongly obtuse inscribed-triangle counts: exact variance and a two-sided spectral limit

## Finding

Let \(n\ge3\), and sample \(n\) independent points \(X_1,\ldots,X_n\) uniformly by arclength from the unit circle. Fix a strict angle threshold \(\alpha\in(\pi/2,\pi)\), and set \(b=1-\alpha/\pi\in(0,1/2)\). Let \(A_n(b)\) be the number of unordered triples of sampled points whose inscribed triangle has its **largest interior angle strictly greater than** \(\alpha\). Then

\[
\mathbb E A_n(b)=3b^2\binom n3,
\quad
\operatorname{Var} A_n(b)=3b^2(1-3b^2)\binom n3+2\left(\frac{14}{3}b^3-9b^4\right)\binom n2\binom{n-2}{2}.
\]

For each positive integer \(k\), define the explicit real number
\[
\lambda_k(b)=\frac{b\sin(2\pi kb)}{\pi k}+\frac{1-\cos(2\pi kb)}{2\pi^2k^2}.
\]
Let \(E_1,E_2,\ldots\) be independent exponential random variables of mean one. The centered, scaled count has the **non-Gaussian spectral limit**
\[
\frac{A_n(b)-3b^2\binom n3}{n^2}\ \Longrightarrow\ Z_b=\sum_{k=1}^{\infty}\lambda_k(b)(E_k-1),
\qquad n\to\infty,
\]
with convergence of the infinite series in \(L^2\) and \(\operatorname{Var}(Z_b)=\frac73b^3-\frac92b^4\). For **every** strict \(b\in(0,1/2)\), positive and negative spectral coefficients both occur, and the limiting law has support all of \(\mathbb R\). The natural right-angle endpoint \(b=1/2\) instead has only nonnegative spectral coefficients and a half-line supported limit; that endpoint is already covered by the classical theory of simplicial depth and is included here only as a contrast, not as the claimed novel result.

In particular, at the geometrically distinguished \(120^\circ\) threshold \(b=1/3\),
\[
\mathbb E A_n(1/3)=\tfrac13\binom n3,\quad
\operatorname{Var} A_n(1/3)=\tfrac29\binom n3+\tfrac{10}{81}\binom n2\binom{n-2}{2},
\quad \operatorname{Var}(Z_{1/3})=\tfrac5{162}.
\]

## Assumptions and scope

The points are independent, have exactly uniform angular (equivalently arclength) law, and the center and circle radius are fixed. Triangles are formed without replacement from each \(n\)-point sample; the statistic is an unnormalized triple count, not a sample of independent random triangles. Genericity conditions (no duplicate points, no angle exactly \(\alpha\)) hold with probability one. The threshold is fixed as \(n\to\infty\); no claim is made about shrinking thresholds depending on \(n\). The principal theorem is for \(\pi/2<\alpha<\pi\).

## Proof

**1. Circular spacing and an exact counting identity.** Write each sample point's angle as a fraction \(\theta_i\in[0,1)\) of one revolution. For three distinct cyclically ordered angles, let their three positive cyclic spacings be \(g_1,g_2,g_3\), summing to one. By the inscribed-angle theorem the triangle's interior angles are exactly \(\pi g_1,\pi g_2,\pi g_3\), in some order. As \(1-b>1/2\), at most one \(g_i\) exceeds \(1-b\). Thus a counted triangle is exactly a triple inside a circular arc shorter than \(b\), with a **unique** long empty complementary gap.

For each observed point \(\theta_i\), let \(m_i(b)\) be the number of other sample points in the clockwise open arc \((\theta_i,\theta_i+b)\) modulo one. Every counted triple has a unique first point immediately clockwise after its long empty complementary gap, and exactly two further points in that arc. Consequently the following finite-sample identity is exact, not asymptotic:
\[
A_n(b)=\sum_{i=1}^n\binom{m_i(b)}2.
\]
It also yields a deterministic \(O(n\log n)\) algorithm by sorting the angular positions and using a moving arc endpoint.

**2. Mean and pairwise conditional kernel.** Three independent circular spacings have the Dirichlet\((1,1,1)\) distribution. A particular spacing exceeds \(1-b\) with probability \(b^2\), and these three events are disjoint. Hence the event probability for one unordered triple is \(p_b=3b^2\), establishing the mean.

Condition instead on two selected sample points separated by minor circular gap \(s\in[0,1/2]\). The third point is uniform. If \(s\ge b\), no three-point circular arc of length \(b\) contains both fixed points. If \(s<b\), the third point can fall between the fixed points on their short arc (length \(s\)), or on either adjacent outer arc of length \(b-s\). Therefore
\[
q_b(s):=\Pr\{\text{large angle}\mid\text{fixed pair at minor gap }s\}
=\begin{cases}2b-s,&0\le s<b,\\0,&b\le s\le1/2.\end{cases}
\]
For two independent uniform angles, their minor gap \(s\) has density \(2\) on \((0,1/2)\), so
\[
\mathbb E q_b(s)=2\int_0^b(2b-s)\,ds=3b^2=p_b,
\quad
\mathbb E q_b(s)^2=2\int_0^b(2b-s)^2\,ds=\frac{14}{3}b^3.
\]
Thus two distinct triple indicators sharing exactly two vertices have covariance \(\zeta_b=\frac{14}{3}b^3-9b^4\). Two indicators with no shared vertices are independent. Two sharing only one vertex have zero covariance because, conditional on that fixed vertex, their other vertex pairs are independent and their conditional event probability is the constant \(p_b\) by rotational invariance. Counting unordered pairs of triples sharing an edge gives \(\binom n2\binom{n-2}{2}\). Summing diagonal variances and twice the edge-sharing covariances yields the stated exact variance for every integer \(n\ge3\).

**3. Second projection and Fourier spectrum.** Let \(H(x,y,z)\) be the zero-one triple indicator. Its first centered conditional projection vanishes: \(\mathbb E[H\mid X_1=x]-p_b=0\) for every \(x\). The second conditional projection on the circle is the translation-invariant kernel
\[
h_2(x,y)=q_b\bigl(d(x,y)/(2\pi)\bigr)-p_b,
\]
where \(d(x,y)\in[0,\pi]\) is the smaller angular separation. With \(u_{kc}(\theta)=\sqrt2\cos(k\theta)\) and \(u_{ks}(\theta)=\sqrt2\sin(k\theta)\), the orthonormal Fourier expansion in \(L^2\) of the uniform product-circle measure is
\[
h_2(x,y)=\sum_{k\ge1}\lambda_k(b)
\left[u_{kc}(x)u_{kc}(y)+u_{ks}(x)u_{ks}(y)\right].
\]
Indeed, the operator eigenvalue at frequency \(k\ne0\) is
\[
2\int_0^b(2b-s)\cos(2\pi ks)\,ds
=\frac{b\sin(2\pi kb)}{\pi k}+\frac{1-\cos(2\pi kb)}{2\pi^2k^2}.
\]
The constant Fourier coefficient vanishes because \(\mathbb E q_b=p_b\). Parseval supplies \(2\sum_{k\ge1}\lambda_k(b)^2=\zeta_b\); the coefficients are square summable.

**4. Limit with all normalizations.** The canonical Hoeffding expansion for the *unnormalized* triple count is
\[
A_n(b)-p_b\binom n3=(n-2)\sum_{i<j}h_2(X_i,X_j)+\sum_{i<j<k}h_3(X_i,X_j,X_k),
\]
where \(h_3=H-p_b-h_2(X_i,X_j)-h_2(X_i,X_k)-h_2(X_j,X_k)\) satisfies \(\mathbb E[h_3\mid\text{any fixed pair}]=0\). Since \(h_3\) is bounded for fixed \(b\) and distinct canonical triples are orthogonal, the final term has variance exactly \(\binom n3\mathbb E h_3^2=O(n^3)\). Dividing by \(n^2\) makes it vanish in \(L^2\).

For a finite Fourier truncation, rewrite each pair sum using the square of \(n^{-1/2}\sum_i u_{kc}(X_i)\) and its sine counterpart. The finite-dimensional multivariate central limit theorem and law of large numbers give
\[
\frac{n-2}{n^2}\sum_{i<j}h_2^{(K)}(X_i,X_j)
\Longrightarrow\frac12\sum_{k=1}^K\lambda_k(b)
\bigl(G_{kc}^2+G_{ks}^2-2\bigr),
\]
for independent standard normals \(G_{kc},G_{ks}\). The squared \(L^2\) error from omitting frequencies beyond \(K\), uniformly in \(n\), is bounded by a constant times \(\sum_{k>K}\lambda_k(b)^2\), because the residual pair kernel is canonical. Letting \(K\to\infty\), and using \((G_{kc}^2+G_{ks}^2)/2\stackrel{d}=E_k\sim\operatorname{Exp}(1)\), gives the asserted \(Z_b=\sum\lambda_k(E_k-1)\). Its variance is \(\sum\lambda_k^2=\zeta_b/2\), agreeing with the limit of the exact finite variance divided by \(n^4\).

**5. Spectral signs and full support.** For every \(0<b<1/2\), the coefficient \(\lambda_1(b)>0\) since \(\sin(2\pi b)>0\). Some coefficients are strictly negative: if \(b\) is rational, choose a periodic residue class \(k\) with \(\sin(2\pi kb)<0\); since its reduced denominator is at least three, such a class exists. Along infinitely many integers in that class the negative \(k^{-1}\) term dominates the nonnegative \(O(k^{-2})\) term. If \(b\) is irrational, density of fractional parts of \(kb\) produces infinitely many large indices with sine bounded below a negative constant, with the same conclusion. One independent exponential corresponding to a positive eigenvalue and one to a negative eigenvalue yield a distribution with positive density on all real values after convolution; the independent convergent remainder does not destroy that support. Thus \(\operatorname{supp}Z_b=\mathbb R\) for every strict strongly obtuse threshold. At \(b=1/2\), the displayed eigenvalues formally become \(\lambda_k=(1-(-1)^k)/(2\pi^2 k^2)\ge0\), the classical one-sided simplicial-depth regime. This endpoint is acknowledged as prior mathematics, not claimed as new.

## Verification

`verify.py` is a self-contained reproducibility script requiring Python 3 and NumPy. It compares the sliding-arc identity against exhaustive direct angle-triple evaluation, checks the exact mean and variance against independent Monte Carlo samples for five thresholds, compares the Fourier Parseval sum with its geometric covariance, checks both spectral signs for strict thresholds, and compares the \(n=300\) finite-sample scaled variance with the limiting chaos variance at the \(120^\circ\) threshold. The exact symbolic/rational evaluations for \(b=1/3\) can also be checked by direct substitution. These finite experiments are corroboration, not replacements for steps 1–5, which provide an infinite-sample proof.

## Relationship to prior work

The arXiv v1 of Koroleva and Nikitin (7 January 2013) supplies the archived circular-sampling and U-statistics setting; its inspected introduction and inscribed-polygon sections concern **extreme perimeters and areas**, not counts of triangles exceeding an angular threshold. The standard U-statistics theory of Serfling provides the general degeneracy and spectral-limit method, but not the present threshold-dependent Fourier eigenvalues, exact finite-sample covariance, or spectral-support dichotomy.

The origin-containing/acute-triangle count at the **right-angle endpoint** is substantially covered by Oja–Nyblom (1989), Killeen–Hettmansperger (2020/2021), and the thorough discussion of Jentsch–Nagy–Wendler (2026). Their known endpoint limit is explicitly **excluded from the claimed novelty**. The last article's inspected Introduction and Section 2 address degeneracy of simplicial depth and cite the earlier exact endpoint distributions, not the \(\alpha>\pi/2\) angle-count family. The earlier Killeen–Hettmansperger full text could not be retrieved through permitted access; its abstract and the later full-text exposition were inspected, leaving a stated historical-priority risk. No claim of a complete literature census or external certification is made.

## Limitations

The threshold is strictly larger than a right angle and fixed as the sample size increases. These formulas do not describe nonuniform angular sampling, points sampled in a disk, noncircular curves, or threshold sequences approaching an endpoint as \(n\to\infty\). The scope is a single scalar angle-threshold statistic, not a proven functional central-limit theorem for the entire angle-count process. Historical priority is provisional because related older full texts were inaccessible; absence of a matching search result is not proof of uniqueness. No independent mathematical audit has been performed.

## References

1. E. V. Koroleva and Ya. Yu. Nikitin, *U-max-Statistics and Limit Theorems for Perimeters and Areas of Random Polygons*, arXiv:1301.1360v1, first public version 7 January 2013, https://arxiv.org/html/1301.1360v1.
2. R. Y. Liu, *On a notion of simplicial depth*, Proceedings of the National Academy of Sciences 85 (1988), 1732–1734, DOI 10.1073/pnas.85.6.1732.
3. H. Oja and J. Nyblom, *Bivariate Sign Tests*, Journal of the American Statistical Association 84 (1989), 249–259, DOI 10.1080/01621459.1989.10478763.
4. T. J. Killeen and T. P. Hettmansperger, *A bivariate test for location based on simplicial depth*, Communications in Statistics—Theory and Methods 50 (2021), 3954–3971; first online 2 March 2020, DOI 10.1080/03610926.2019.1710205.
5. C. Jentsch, S. Nagy and M. Wendler, *Resampling simplicial depth*, arXiv:2608.11131, public 11 August 2026, https://arxiv.org/abs/2608.11131 (full HTML inspected).
6. R. Serfling, *Approximation Theorems of Mathematical Statistics*, Wiley, 1980, Section 5.5 (general U-statistic decomposition and degenerate limits).
