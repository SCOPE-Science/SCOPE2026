# Exact Bernoulli product-weight profile for the four-cube simplex polynomial

## Finding

Let \(V=\{0,1\}^4\), choose arbitrary \(0<p_1,p_2,p_3,p_4<1\), and give each vertex \(v=(v_1,\ldots,v_4)\in V\) the independent-coordinate probability weight
\[
x_v=\prod_{i=1}^4 p_i^{v_i}(1-p_i)^{1-v_i}.
\]
Write \(q_i=p_i(1-p_i)\) and \(e_j(q)\) for the elementary symmetric polynomial of degree \(j\) in \(q_1,\ldots,q_4\). For each five-element subset \(U=\{v^{(0)},\ldots,v^{(4)}\}\subset V\), let
\[
d(U)=\left|\det\big(v^{(1)}-v^{(0)},\ldots,v^{(4)}-v^{(0)}\big)\right|,
\qquad
P(x)=\sum_{\substack{U\subset V\\|U|=5}}d(U)\prod_{v\in U}x_v.
\]
The choice of the ordering in the determinant does not change its absolute value. Then the exact four-parameter identity is
\[
\boxed{P(x)=e_4(q)\bigl(1-4e_3(q)+18e_4(q)\bigr).}
\]
Consequently the four-cube Hypercube-inequality deficit has the **sharp** product-variance refinement
\[
\boxed{\prod_{i=1}^4q_i-P(x)\ \ge\ 46\Bigl(\prod_{i=1}^4q_i\Bigr)^2>0.}
\]
Equality in the first inequality occurs if and only if all four biases equal \(1/2\); in that case \(P(x)/\prod_iq_i=105/128\). The multiplicative constant \(46\) cannot be increased. The identity and non-strict inequality extend continuously to boundary biases, where both sides of the original Hypercube inequality are zero whenever at least one coordinate is deterministic.

Equivalently, if \(X_0,\ldots,X_4\) are independent random vectors in \(V\), each with the above product-Bernoulli distribution, then
\[
\mathbb E\left|\det(X_1-X_0,\ldots,X_4-X_0)\right|
=5!\,e_4(q)\bigl(1-4e_3(q)+18e_4(q)\bigr).
\]

## Assumptions and scope

The ambient cube dimension is exactly four. All five-subsets are unordered, and \(d(U)=4!\operatorname{vol}_4(\operatorname{conv}U)\), so no additional factorial occurs in \(P(x)\). Independent-coordinate weighting is essential: an arbitrary assignment of sixteen nonnegative vertex weights is not covered. In the source's four-cube Hypercube inequality, the total weight is \(\sum_vx_v=1\), while the eight facet sums are \(p_i\) and \(1-p_i\), one pair per coordinate. Thus its left side is exactly \(P(x)\), and its right side is \(\prod_iq_i\).

## Proof

**1. Symmetry and degree reduction.** Regard \(P(x)\) as a polynomial in the four biases. Each vertex weight is affine in each individual bias, so \(\deg_{p_i}P\le5\). If \(p_i=0\) or \(p_i=1\), all vertices of positive weight lie in one three-dimensional cube facet, and every normalized four-simplex volume appearing in \(P\) is zero. Therefore the polynomial \(P\) is divisible by each \(q_i=p_i(1-p_i)\), and hence by \(e_4(q)=\prod_iq_i\).

Set \(R=P/e_4(q)\). Reflection across the middle of the \(i\)-th coordinate sends \(p_i\) to \(1-p_i\) and preserves all absolute simplex determinants. Thus \(R\) is invariant under each such reflection. Since \(\deg_{p_i}R\le3\), the invariant-polynomial identity \(\mathbb R[p_i]^{p_i\mapsto1-p_i}=\mathbb R[p_i(1-p_i)]\) shows that \(R\) has degree at most one in every \(q_i\). Indeed, reflection invariance makes the polynomial even in \(p_i-1/2\), whose square is \(1/4-q_i\). Permutations of the four cube coordinates preserve \(R\), hence there exist constants \(a_0,\ldots,a_4\) such that
\[
R=\sum_{j=0}^4 a_j e_j(q),\qquad e_0(q)=1.
\]
Knowing \(R\) on the diagonal \(q_1=\cdots=q_4=t\) uniquely determines all five coefficients, since \(e_j(t,t,t,t)=\binom4j t^j\).

**2. Exhaustive integer simplex census.** Specialize all biases to \(p\). Then \(x_v=p^{|v|}(1-p)^{4-|v|}\), where \(|v|\) is the Hamming weight. For each integer \(0\le k\le20\), let
\[
M_k=\sum_{\substack{U\subset V,\ |U|=5\\\sum_{v\in U}|v|=k}}d(U).
\]
All \(\binom{16}{5}=4368\) subsets can be enumerated with exact integer determinants. The complete nonzero coefficient census, listed consecutively for \(k=4,5,\ldots,16\), is
\[
(M_4,\ldots,M_{16})=(1,12,66,204,417,624,712,624,417,204,66,12,1),
\]
with every other coefficient zero. The determinant multiplicities are \(1360\) zero, \(2672\) of absolute value one, \(320\) of value two, and \(16\) of value three. Two independent exact integer determinant algorithms, and a check of the entire polynomial coefficient identity, are provided in `verify.py`.

It follows, by an exact binomial expansion of the displayed finite coefficient vector, that
\[
\sum_{k=0}^{20}M_kp^k(1-p)^{20-k}
=[p(1-p)]^4\bigl(1-16[p(1-p)]^3+18[p(1-p)]^4\bigr).
\]
The left side is \(P(x)\) on the equal-bias diagonal. Division by \(q^4\), where \(q=p(1-p)\), gives \(R(q,q,q,q)=1-16q^3+18q^4\). Comparing the symmetric-multiaffine coefficients from Step 1 yields \(a_0=1\), \(a_1=a_2=0\), \(a_3=-4\), and \(a_4=18\), proving the exact formula for **every** bias quadruple, not just those tested numerically.

**3. Sharp quantitative deficit.** As \(0<q_i\le1/4\), one has
\[
4e_3(q)-18e_4(q)
=e_4(q)\Bigl(4\sum_{i=1}^4q_i^{-1}-18\Bigr)
\ge46e_4(q),
\]
with equality exactly when every \(q_i=1/4\), i.e. \(p_i=1/2\). Multiplying by \(e_4(q)\) yields the claimed sharp deficit. Since \(e_4(q)>0\) in the open bias cube, the original Hypercube inequality is strict there.

**4. Random-determinant formulation.** When sampling five vertices independently with replacement, any repeated vertex produces determinant zero. Every unordered five-set has exactly \(5!\) orderings, each with the same absolute determinant and probability product. This gives the equivalent expectation identity without a probabilistic approximation.

## Verification

Run `python3 verify.py` with Python 3 and no external dependencies. The standalone program enumerates all \(4368\) five-sets, compares permutation-expansion determinants of their four difference columns with separate fraction-free elimination determinants of augmented five-by-five matrices, establishes the integer census above, and checks every coefficient of the degree-at-most-twenty polynomial identity. It also performs a separate exact-rational regression at unequal biases \((1/2,1/3,1/4,1/5)\). Successful execution prints `FOUR_CUBE_PRODUCT_WEIGHT_EXACT_CERTIFICATE_OK`. The analytic symmetry argument, not the finite numerical regression, proves extension from the diagonal to arbitrary real biases.

## Relationship to prior work

Averkov, von Dichter, and Soprunov formulated the weighted Hypercube inequality as their equation (2) and established it for cube dimension three; their Section 7.5 identifies cube dimension four as open. Their results provide the precise normalization and motivation used here but do not give the present product-Bernoulli identity. General results of Fradelizi and collaborators on Rayleigh properties of zonotope volume polynomials address a stronger property that fails in higher dimensions, rather than this weighted four-cube product distribution. The zonoid-algebra framework of Breiding, Bürgisser, Lerario, and Mathis relates random determinants and mixed volumes but does not supply the coefficients of this four-parameter formula. A separate symmetry-constrained analysis of weights constant on Hamming layers concerns a different family; its intersection with the strictly positive independent-coordinate family consists of equal unbiased weights only.

## Limitations

Nothing here proves the open four-cube Hypercube inequality for **all** sixteen nonnegative weights. The exact integer census is finite, exhaustive for the sixteen cube vertices, and reproducible, but it does not certify any infinite-dimensional or arbitrary-weight assertion. The originality assessment is based on examined literature, not a claim that every unpublished or unindexed calculation has been excluded. Independent validation has not been performed.

## References

1. G. Averkov, K. von Dichter, I. Soprunov, *On the Log-submodularity for zonoids: from Mixed Volume inequalities to the Hypercube*, arXiv:2608.14909, first posted August 14, 2026, especially equation (2) and Sections 4, 6, and 7.5.
2. M. Fradelizi, A. Hubard, A. Manui, C. S. Ndiaye, S. Wang, A. Zvavitch, *Volume and Projection Inequalities I: Zonoids and Courtade's Conjecture*, arXiv:2608.12681, first posted August 13, 2026.
3. P. Breiding, P. Bürgisser, A. Lerario, L. Mathis, *The zonoid algebra, generalized mixed volumes, and random determinants*, arXiv:2109.14996, especially Section 5.2.
