# Exact two-pair correlation law for the four-dimensional Hypercube polynomial

## Finding

Let \(Q=\{0,1\}^4\). For positive parameters \(a,b,c,d\), assign each vertex \(v\in Q\) the weight
\[
x_v=\begin{cases}a&v_1=v_2,\\ b&v_1\ne v_2\end{cases}
\begin{cases}c&v_3=v_4,\\ d&v_3\ne v_4.\end{cases}
\]
For every five-vertex subset \(U\) let \(\operatorname{Vol}(U)=4!\,\operatorname{vol}_4(\operatorname{conv}U)\), and define
\[
P=\sum_{|U|=5}\operatorname{Vol}(U)\prod_{v\in U}x_v,\quad T=\sum_{v\in Q}x_v,\quad S_F=\sum_{v\in F}x_v
\]
for each of the eight cube facets \(F\). Set \(\rho=(a-b)/(a+b)\) and \(\sigma=(c-d)/(c+d)\). The **exact identity** is
\[
\boxed{\frac{PT^3}{\prod_F S_F}=\frac{(1-\rho^2)(1-\sigma^2)\bigl(105+15\rho^2+15\sigma^2-7\rho^2\sigma^2\bigr)}{128}.}
\]
For all \(a,b,c,d>0\), this ratio belongs to \((0,105/128]\), with equality at the upper endpoint **if and only if** \(a=b\) and \(c=d\). It decreases strictly in either squared within-pair correlation while the other is fixed. This is the sharp enhanced estimate and entire correlation profile for the stated pair-product family; it is not a new proof of the unrestricted Hypercube inequality, which had already been proved in every dimension in the October 18, 2026 version of Averkov–von Dichter–Soprunov.

## Scope and interpretation

The two coordinate pairs are independent, and the bits within each pair are individually unbiased but may be correlated. Indeed
\[
\frac{x_v}{T}=\frac{\bigl(1+\rho(-1)^{v_1+v_2}\bigr)\bigl(1+\sigma(-1)^{v_3+v_4}\bigr)}{16}.
\]
The domain \((\rho,\sigma)\in(-1,1)^2\) is exact after quotienting independent positive scale factors of \((a,b)\) and \((c,d)\). We do **not** claim the improved bound \(105/128\) for unrestricted nonnegative sixteen-vertex weight vectors, for biased pair marginals, or for an arbitrary four-bit joint distribution.

## Complete proof

**Facet normalization.** Each coordinate marginal is unbiased because, for fixed one coordinate of a pair, the sum of the two pair weights is \(a+b\) (respectively \(c+d\)). Direct summation gives
\[
T=4(a+b)(c+d),\qquad S_F=2(a+b)(c+d)=T/2
\]
for each of the eight facets. Therefore
\[
\frac{PT^3}{\prod_FS_F}=\frac{P}{4(a+b)^5(c+d)^5}.
\]

**Finite exact coefficient identity.** There are exactly \(\binom{16}{5}=4368\) unordered five-vertex subsets of \(Q\). For each subset, translate one vertex to the origin, take the absolute determinant of the resulting integer \(4\times4\) coordinate-difference matrix, and group by the pair-parity exponents. Every nonzero term is a monomial \(a^jb^{5-j}c^kd^{5-k}\) with \(j,k\in\{1,2,3,4\}\). The complete matrix of its coefficients (rows \(j=1,2,3,4\), columns \(k=1,2,3,4\)) is
\[
\begin{pmatrix}64&176&176&64\\176&424&424&176\\176&424&424&176\\64&176&176&64\end{pmatrix}.
\]
The independent exhaustive determinant reconstruction finds \(1360\) zero-volume subsets and normalized-volume multiplicities \(2672,320,16\) for volumes \(1,2,3\); these exhaust the \(4368\) subsets. Expanding the coefficient table yields the exact factorization
\[
P=8abcd(a+b)(c+d)\bigl[8(a^2+b^2)(c^2+d^2)
+14(a^2+b^2)cd+14ab(c^2+d^2)+17abcd\bigr].
\]
This is a **finite polynomial identity**, not an inference from sampled weights. Its coefficients can be reproduced by either exact integer elimination or an independent Leibniz-determinant summation over all subsets (see the unchanged verifier supplied with the original package).

**Closed form.** Put \(r=ab/(a+b)^2\) and \(s=cd/(c+d)^2\). Substitution of the factorization into the normalized ratio and cancellation give
\[
\frac{PT^3}{\prod_F S_F}=2rs(8-2r-2s-7rs).
\]
Using \(r=(1-\rho^2)/4\), \(s=(1-\sigma^2)/4\) gives the announced correlation identity.

**Sharpness, uniqueness and boundaries.** Write \(u=\rho^2\), \(v=\sigma^2\), with \(0\le u,v<1\), and let \(R(u,v)\) denote the boxed expression. Exact differentiation gives
\[
\frac{\partial R}{\partial u}=-\frac{(1-v)(90+30u+22v-14uv)}{128}<0,
\]
with the symmetric formula for \(\partial R/\partial v\). The displayed polynomial is strictly positive on \([0,1)^2\), and all factors \(1-u,1-v\) are positive. Hence \(R\) has its unique maximum at \((u,v)=(0,0)\), where \(R=105/128\), and is positive everywhere in the stated domain. Since \(u=v=0\) means \(a=b,c=d\), the equality case is rigid. The ratio tends to zero as either squared correlation tends to one.

## Relationship to prior work and revised chronology

**The general Hypercube inequality is no longer open.** Averkov, von Dichter and Soprunov's arXiv:2608.14909v1 (August 14, 2026) proved the three-cube case and formulated general-dimensional conjectures. Their **arXiv:2608.14909v2 (October 18, 2026), Section 7**, incorporates a probabilistic proof of the inequality for *every* cube dimension. In particular the unrestricted four-dimensional inequality \(PT^3\le\prod_F S_F\) was proved before this restricted computation was recorded. That already-established broad bound is \(1\), not the sharp \(105/128\) obtained here; the general proof does not state the exact polynomial in \(\rho^2,\sigma^2\), this restricted optimum, or strict correlation monotonicity. The contribution assessed here is solely that exact quantitative profile on the natural two-independent-correlated-pair family.

The earlier published result *Sharp symmetric gap for the first open hypercube inequality* (October 11, 2026) obtains the same sharp factor \(105/128\) on the cone invariant under full coordinate permutation and complementation, with vertex weights depending on Hamming-weight classes. Its three-parameter cone and the present parity-pair cone are not nested: equal-Hamming-weight vertices need not have equal pair-parity weights, and vice versa. The identical maximizing value at uniform weights does not establish equivalence of the restricted inequalities. Separately, the independent-Bernoulli family has zero within-pair correlation and therefore does not give the two-variable profile.

## Verification and limits

An unchanged standard-library checker in the source package exhausts all \(4368\) subsets, independently computes determinants, recovers the \(4\times4\) coefficient matrix, and checks the factorization. The unrestricted real-parameter conclusion follows from this exact finite polynomial identity and the derivative sign, **not** from finite numerical samples. This result is a restricted exact identity and sharp quantitative refinement of a now-proved general inequality. It establishes neither global sharpness for arbitrary vertex weights nor historical uniqueness against all less-indexed computations. No external certification is asserted.

## References

1. G. Averkov, K. von Dichter, I. Soprunov, *On the Log-submodularity for zonoids: from Mixed Volume inequalities to the Hypercube*, arXiv:2608.14909v2 (October 18, 2026), especially Sections 4 and 7. https://arxiv.org/html/2608.14909v2.
2. *Sharp symmetric gap for the first open hypercube inequality*, complete published mathematical result (October 11, 2026), https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-sharp-symmetric-gap-for-the-first-open-hypercube-inequality--4f3e013d18c9/RESULT.md.
