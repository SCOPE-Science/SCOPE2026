# One-bit information capacity at every attainable Sarmanov rank correlation

## Finding

Consider the class of absolutely continuous bivariate rank-one Sarmanov copulas with densities
\[
 c(u,v)=1+q(u)p(v),\qquad (u,v)\in[0,1]^2,
\]
where \(p,q\) are real essentially bounded measurable functions with zero integral and \(c\geq0\) almost everywhere. Let \(\rho_S\) be population Spearman correlation, \(\tau\) population Kendall correlation, and \(I(U;V)=\int_{[0,1]^2}c\log c\) mutual information in nats, with \(0\log0=0\).

**Theorem.** Every copula in this class satisfies
\[
0\leq I(U;V)\leq\log2,\qquad
|\rho_S|\leq\frac34,\qquad
\tau=\frac23\rho_S.
\]
Equality \(I(U;V)=\log2\) occurs **if and only if**, up to sets of measure zero,
\[
 c(u,v)=2\mathbf1_A(u)\mathbf1_B(v)
       +2\mathbf1_{A^c}(u)\mathbf1_{B^c}(v),
 \qquad |A|=|B|=\frac12.
\]
Here \(A,B\subseteq[0,1]\) are measurable and \(|\cdot|\) denotes Lebesgue measure. In particular, for **every** attainable \(r\in[-3/4,3/4]\),
\[
\boxed{\max_{\rho_S(C)=r} I(U;V)=\log2.}
\]
The same flat upper envelope holds for each fixed \(\tau\in[-1/2,1/2]\), by the identity \(\tau=2\rho_S/3\). The maximizers at fixed \(r\) are exactly the displayed equal-measure bipartition densities satisfying
\[
12\Bigl(\int_0^1u(2\mathbf1_A(u)-1)\,du\Bigr)
\Bigl(\int_0^1v(2\mathbf1_B(v)-1)\,dv\Bigr)=r.
\]
Thus even **zero Spearman and zero Kendall correlation** can coexist with the largest mutual information achievable anywhere in this entire model class.

## Assumptions and scope

All assertions concern a bivariate copula with uniform continuous margins, a Lebesgue density, and a *single* essentially bounded separable perturbation of independence. The kernels are only required to be measurable and essentially bounded, not continuous. Equivalently its distribution function is \(C(u,v)=uv+g(u)h(v)\), where \(g,h\) are absolutely continuous with essentially bounded derivatives and vanish at both endpoints. Singular copulas, multiple perturbation terms and higher-dimensional copulas are outside scope. Natural logarithms are used; the capacity is one bit after conversion from nats.

If \(q p=0\) almost everywhere, then \(c=1\) and \(I=\rho_S=\tau=0\). Otherwise both centered kernels are nonconstant and take both signs on sets of positive measure. We prove the nontrivial case below.

## Proof

**1. A binary separator gives the universal information bound.** Put \(\alpha=\operatorname*{ess\,inf}q<0\), \(\beta=\operatorname*{ess\,sup}q>0\), and
\[
\pi=\frac{-\alpha}{\beta-\alpha}\in(0,1),\quad
w(u)=\frac{q(u)-\alpha}{\beta-\alpha}\in[0,1],\quad
 d_0(v)=1+\alpha p(v),\quad d_1(v)=1+\beta p(v).
\]
Since \(c(u,v)\geq0\) almost everywhere, taking essential-limit values of \(q\) on positive-measure sets shows \(d_0,d_1\geq0\) almost everywhere. Both integrate to one because \(\int p=0\), and \(\int w=\pi\) because \(\int q=0\). Algebra gives the identities
\[
 c(u,v)=(1-w(u))d_0(v)+w(u)d_1(v),\qquad
 (1-\pi)d_0(v)+\pi d_1(v)=1.
\]
Construct \(U\sim\mathrm{Unif}(0,1)\), a Bernoulli variable \(J\) with \(\Pr(J=1\mid U=u)=w(u)\), and, conditionally on \(J=j\), a variable \(V\) of density \(d_j\), independent of \(U\) given \(J\). Then \(U\to J\to V\) is a Markov chain, and the joint density of \((U,V)\) is exactly \(c\); both margins are uniform. The data-processing inequality and binary entropy inequality therefore give
\[
 I(U;V)\leq I(U;J)\leq H(J)=h(\pi)\leq\log2.
\]
The information integral is finite because \(c\) is bounded. Its nonnegativity is Gibbs' inequality applied to \(c\) and the uniform product density.

**2. All equality cases.** Suppose \(I(U;V)=\log2\). Every inequality above is equality, so \(\pi=1/2\), \(H(J\mid U)=0\), and, using the other data-processing bound \(I(U;V)\leq I(J;V)\), also \(H(J\mid V)=0\). Thus \(J\) is almost surely a measurable function of \(U\) and also of \(V\): there are measurable sets \(A,B\) such that \(J=\mathbf1_A(U)=\mathbf1_B(V)\) almost surely. Uniform margins and \(\Pr(J=1)=1/2\) imply \(|A|=|B|=1/2\). Conditional on \(J\), the coordinates are independent and uniformly distributed on their respective sets, so their density is exactly
\[
2\mathbf1_A(u)\mathbf1_B(v)+2\mathbf1_{A^c}(u)\mathbf1_{B^c}(v).
\]
Conversely any such bipartition density equals \(1+s_A(u)s_B(v)\), with \(s_A=2\mathbf1_A-1\) and \(s_B=2\mathbf1_B-1\), so belongs to the assumed class. The common deterministic Bernoulli label \(\mathbf1_A(U)=\mathbf1_B(V)\) has entropy \(\log2\), while \(U,V\) are conditionally independent given the label. Hence \(I(U;V)=\log2\). This proves necessity and sufficiency, including equality at all parameter boundaries.

**3. Rank range and concordance identity.** For the binary separator above, conditional independence gives
\[
\operatorname{Cov}(U,V)=\pi(1-\pi)
\bigl(\mathbb E[U\mid J=1]-\mathbb E[U\mid J=0]\bigr)
\bigl(\mathbb E[V\mid J=1]-\mathbb E[V\mid J=0]\bigr).
\]
For a uniform variable \(U\) and any Bernoulli separator with \(\Pr(J=1)=\pi\), the difference of its conditional means has magnitude at most \(1/2\). Indeed, \(\int uw(u)\,du\) with \(0\leq w\leq1\) and \(\int w=\pi\) lies between the integrals of \(u\) over the lowest and highest intervals of length \(\pi\), respectively, which yield differences of \(-1/2\) and \(+1/2\). The same holds for \(V\). Therefore \(|\operatorname{Cov}(U,V)|\leq\pi(1-\pi)/4\leq1/16\), so \(|\rho_S|=12|\operatorname{Cov}(U,V)|\leq3/4\).

For the identity with Kendall's coefficient, write \(g(u)=\int_0^u q(s)\,ds\), \(h(v)=\int_0^v p(t)\,dt\), \(G=\int_0^1g\), \(H=\int_0^1h\). Endpoint zeroes and integration by parts yield \(\int_0^1 u q(u)\,du=-G\), \(\int_0^1 v p(v)\,dv=-H\), and \(\int gq=\int hp=0\). The rank-correlation formulas thus give
\[
 \rho_S=12GH,\qquad
 \tau=4\iint C(u,v)c(u,v)\,du\,dv-1=8GH=\frac23\rho_S.
\]
In the middle equality, expansion of \(C c=(uv+gh)(1+qp)\) integrates to \(1/4+2GH\), since the \(ghqp\) product has zero integral.

**4. Exact maximizers at every rank value.** Fix any real \(r\in[-3/4,3/4]\) and set \(t=1/4-r/3\in[0,1/2]\). Define the half-measure sets
\[
 A_t=[0,t]\cup[t+1/2,1],\qquad B=[1/2,1].
\]
Intervals of length zero at the endpoints cause no difficulty. Set \(s_t=2\mathbf1_{A_t}-1\), \(b=2\mathbf1_B-1\), and
\[
 c_t(u,v)=1+s_t(u)b(v).
\]
It is zero or two almost everywhere, is nonnegative, has both margins uniform, and therefore is an admissible rank-one Sarmanov copula. The two signs have zero integrals and satisfy
\[
 \int_0^1 u s_t(u)\,du=\frac14-t,\qquad
 \int_0^1 v b(v)\,dv=\frac14.
\]
Consequently \(\rho_S(c_t)=12(1/4-t)(1/4)=3/4-3t=r\), and \(\tau(c_t)=2r/3\). The construction has density two on a set of area exactly one half, so
\[
 I(c_t)=\frac12\,(2\log2)=\log2.
\]
Combined with Step 1 this proves the flat upper envelope. Step 2 gives the complete equality classification, while the preceding rank formula gives the stated fixed-rank condition on \(A,B\).

## Verification

A standalone pure-Python `checker.py` uses exact rational arithmetic and independent rectangular-cell convolution sums for twelve admissible rational values of \(r\), including both endpoints and zero. For each value it verifies row and column masses, normalizations, that all density cells are zero or two, and that the exact formulas \(\rho_S=r\) and \(\tau=2r/3\) hold. It also verifies that the total mass on density-two cells is one, which proves the finite-cell integral of \(c\log c\) equals \(\log2\). Run it as `python checker.py`. These finite checks are diagnostics: the theorem for every real \(r\) and arbitrary bounded measurable kernels follows from the preceding analytical proof.

## Relationship to prior work

Blier-Wong, *Stochastic representation of Sarmanov copulas* (arXiv:2601.09016v1, first public 13 January 2026), establishes a Bernoulli-mixture representation and the sharp global Spearman range \([-3/4,3/4]\), building on earlier rank-bound work. These are acknowledged inputs and context; the new claim is the **information envelope conditional on every rank value**, together with the equality classification and nonmonotone equality construction. The source's full accessible Sections 2 and 5 and appendices contain no asserted mutual-information-capacity theorem. The present proof is independently reconstructed without requiring its Bernoulli-pair theorem.

Sukeda and Sei, *On the minimum information checkerboard copulas under fixed Kendall's rank correlation* (arXiv:2306.01604), minimize mutual information over checkerboards with a fixed rank constraint, whereas this theorem **maximizes** it over the rank-one Sarmanov family; minimizing does not imply the flat upper envelope. Lin, Wang, Zhang and Zhao, *The checkerboard copula and dependence concepts* (arXiv:2404.15023), study maximum-entropy copula selection when margins are not fully continuous, a different optimization. The binary entropy bound and data processing themselves are classical facts, not newly claimed.

There is an unresolved bibliographic priority risk involving Ebrahimi, Jalali and Soofi, *Comparison, utility, and partition of dependence under absolutely continuous and singular distributions* (Journal of Multivariate Analysis 131 (2014), 32–50, DOI:10.1016/j.jmva.2014.06.014), whose abstract discusses mutual information in a class of uncorrelated dependence models. Its full text was not available for a statement-by-statement comparison, so no claim of noncoverage of that article is made. A related 2022 Sarmanov-family information-measures article likewise has limited accessible text; neither unavailability nor unsuccessful keyword search proves novelty.

## Limitations

The one-bit upper bound is **not** asserted for arbitrary copulas, whose mutual information need not be bounded by one bit. It depends crucially on a single separable, bounded-density perturbation. The maximizing copulas have density zero on half the square and are not everywhere strictly positive; strict positivity was not imposed. With continuity requirements on the *density* rather than on the integrated kernels, attainment may need reformulation. No multivariate or sum-of-separable-terms capacity claim is made. The structural entropy bound is a consequence of a binary Markov separator, not a new information-theoretic inequality.

## References

1. Christopher Blier-Wong, *Stochastic representation of Sarmanov copulas*, arXiv:2601.09016v1 (13 January 2026), https://arxiv.org/html/2601.09016v1 .
2. Issey Sukeda and Tomonari Sei, *On the minimum information checkerboard copulas under fixed Kendall's rank correlation*, arXiv:2306.01604 (2023), https://arxiv.org/abs/2306.01604 .
3. Liyuan Lin, Ruodu Wang, Ruixun Zhang and Chaoyi Zhao, *The checkerboard copula and dependence concepts*, arXiv:2404.15023 (2024), https://arxiv.org/abs/2404.15023 .
4. Nader Ebrahimi, Nima Y. Jalali and Ehsan S. Soofi, *Comparison, utility, and partition of dependence under absolutely continuous and singular distributions*, Journal of Multivariate Analysis 131 (2014), 32–50, DOI:10.1016/j.jmva.2014.06.014 (full-text comparison outstanding).
5. T. M. Cover and J. A. Thomas, *Elements of Information Theory*, 2nd ed., Wiley (2006), standard data-processing and binary entropy identities.
