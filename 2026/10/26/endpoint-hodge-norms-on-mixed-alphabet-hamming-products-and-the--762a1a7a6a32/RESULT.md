# Endpoint Hodge Norms on Mixed-Alphabet Hamming Products and the Smallest-Factor Law

## Finding
Let \(d\ge3\) and let \(\mathbf q=(q_1,\ldots,q_d)\) be integers with \(q_i\ge2\), not all equal. Set
\[
G(\mathbf q)=K_{q_1}\square\cdots\square K_{q_d}
\]
with all edges of unit weight. On its real oriented edge space let \(Q\) denote the Euclidean-orthogonal projection onto the cut space and let \(C=I-Q\) denote the Euclidean-orthogonal projection onto the cycle-flow space.

For every coordinate \(i\), define
\[
A_i=2\left(1-\frac1{q_i}\right)
     +2\sum_{j\ne i}\frac{q_j-1}{q_i+q_j},
\]
\[
\alpha_i=\frac1{\prod_{j\ne i}q_j}
\sum_{S\subseteq[d]\setminus\{i\}}
\frac{\prod_{j\in S}(q_j-1)}{q_i+\sum_{j\in S}q_j},
\qquad B_i=1+A_i-4\alpha_i.
\]
For an oriented edge changing coordinate \(i\), the exact induced \(\ell_1\) column norms of \(Q\) and \(C\) are respectively \(A_i\) and \(B_i\). If \(i_*\) is any index with \(q_{i_*}=\min_j q_j\), then
\[
\boxed{\|Q\|_{1\to1}=A_{i_*},\qquad
       \|C\|_{1\to1}=B_{i_*}.}
\]
In both projections, an edge direction is maximizing **if and only if** its alphabet size is minimal. The same exact formulas hold for \(\|Q\|_{\infty\to\infty}\) and \(\|C\|_{\infty\to\infty}\).

For example, the mixed three-coordinate graph \(K_2\square K_3\square K_4\) has
\[
\|Q\|_{1\to1}=\frac{14}{5},\qquad
\|C\|_{1\to1}=\frac{28}{9},
\]
with both maxima attained precisely by edges changing its binary coordinate.

## Assumptions and scope
The graph is a finite Cartesian product of complete simple graphs with \(d\ge3\), unit conductances and standard coordinate edge norms. Choose any edge orientation. Let \(D:\mathbb R^{E}\to\mathbb R^{V}\) be the signed incidence matrix, \(L=DD^{\mathsf T}\), and \(L^+\) its Moore--Penrose inverse. Then
\[
Q=D^{\mathsf T}L^+D,\qquad C=I-Q.
\]
These are real-linear Euclidean-orthogonal projections considered as operators on real \(\ell_1^E\) or \(\ell_\infty^E\). The claim concerns **their** norms, not the infimum over all projections having the same range. All equal-alphabet cases and the two-factor case are outside the claim of new coverage.

## Proof
**1. A positive product resolvent.** In the vertex Hilbert space of \(K_{q_j}\), write \(P_j=I-J_j/q_j\), where \(J_j\) is the all-ones matrix. Its Laplacian is \(q_jP_j\). Fix an edge \(e\) changing coordinate \(i\), with labels \(u\ne v\) there and fixed labels \(a_j\) elsewhere. Its incidence vector is \((\delta_u-\delta_v)\otimes\delta_{\mathbf a}\). Since \(\delta_u-\delta_v\) is a \(q_i\)-eigenvector of the first-factor Laplacian, the vertex potential \(L^+De\) equals
\[
(\delta_u-\delta_v)\otimes g_i,\quad
 g_i=\left(q_i I+\sum_{j\ne i}q_jP_j\right)^{-1}\delta_{\mathbf a}.
\]
This is legitimate despite the constant kernel of \(L\), because the displayed edge incidence lies in a strictly positive eigenspace. The resolvent has the heat-kernel integral
\[
g_i(\mathbf x)=\int_0^\infty e^{-q_it}
\prod_{j\ne i}\left(\frac1{q_j}+
 e^{-q_jt}\left(\mathbf1_{x_j=a_j}-\frac1{q_j}\right)\right)dt.
\]
Every factor in this product is nonnegative. Consequently \(g_i\ge0\), \(\sum_{\mathbf x}g_i(\mathbf x)=1/q_i\), and replacing the distinguished value \(x_j=a_j\) by any other \(x_j\) strictly decreases \(g_i\) pointwise when the remaining coordinates are fixed.

**2. Exact column variation.** Along edges in coordinate \(i\), the potential is \(g_i(\mathbf x)\) times \(\delta_u-\delta_v\). The sum of absolute gradients of this latter vector over all edges of \(K_{q_i}\) is \(2(q_i-1)\). Therefore the total contribution of the edges in direction \(i\) to the column \(Qe\) is \(2(q_i-1)/q_i\).

For \(j\ne i\), only the two vertex layers \(x_i=u,v\) contribute. Within each layer, the positivity and one-distinguished-label monotonicity just proved imply that the only nonzero \(j\)-edge gradients connect the label \(a_j\) to one of the other \(q_j-1\) labels, all with a common absolute sign. Summing over the other coordinates reduces the difference to the resolvent of \(q_i I+q_jP_j\), whose distinguished-minus-other value is exactly \(1/(q_i+q_j)\). The total in direction \(j\) is thus \(2(q_j-1)/(q_i+q_j)\). Summing contributions establishes \(\|Qe\|_1=A_i\).

The diagonal entry is \(Q_{ee}=2g_i(\mathbf a)=2\alpha_i\). The displayed subset formula for \(\alpha_i\) follows by expanding the heat-kernel product at \(\mathbf x=\mathbf a\) and integrating each exponential. Since \(Q\) is an orthogonal projection, \(0\le Q_{ee}\le1\). Hence
\[
\|Ce\|_1=|1-Q_{ee}|+\sum_{f\ne e}|Q_{fe}|
=1+A_i-4\alpha_i=B_i.
\]
Independent coordinate relabelings act transitively on the edges in each direction, so these formulas describe every column.

**3. Which direction maximizes the cut norm?** Suppose \(a=q_i<b=q_j\). Direct subtraction gives
\[
\frac{A_i-A_j}{2(b-a)}
=\frac1{a+b}-\frac1{ab}
+\sum_{k\ne i,j}\frac{q_k-1}{(a+q_k)(b+q_k)}.
\]
For integers \(2\le a<b\), one has \(ab>a+b\); therefore this expression is strictly positive, and all maximizing directions of \(Q\) have minimal alphabet.

**4. Which direction maximizes the cycle norm?** With the same \(a<b\), let \(X_k\), for \(k\ne i,j\), be independent Bernoulli variables with
\(\Pr(X_k=1)=(q_k-1)/q_k\), and set \(Z=\sum_{k\ne i,j}q_kX_k\). Expanding the resolvent products, or integrating each exponential conditional on the \(X_k\), yields the exact identity
\[
\alpha_i-\alpha_j
=(b-a)\,\mathbb E\left[\frac1{(a+Z)(b+Z)(a+b+Z)}\right].
\]
Define \(\Phi(z)=1/[(a+z)(b+z)(a+b+z)]\). It is positive and decreasing for \(z\ge0\). Combining the two differences gives
\[
\frac{B_i-B_j}{2(b-a)}=
\frac1{a+b}-\frac1{ab}
+\sum_{k\ne i,j}\frac{q_k-1}{(a+q_k)(b+q_k)}
-2\mathbb E\Phi(Z).
\]
If \((a,b)\ne(2,3)\), use \(\mathbb E\Phi(Z)\le\Phi(0)\) to bound this expression below by
\[
\frac{ab-a-b-2}{ab(a+b)}
+\sum_{k\ne i,j}\frac{q_k-1}{(a+q_k)(b+q_k)}.
\]
For integers \(2\le a<b\), \(ab-a-b-2\ge0\) except at \((a,b)=(2,3)\). There is at least one remaining factor because \(d\ge3\), so the displayed bound is strictly positive.

In the exceptional pair \((a,b)=(2,3)\), select any other factor size \(c\ge2\). Because adding nonnegative contributions to \(Z\) decreases \(\Phi\), one has
\[
\mathbb E\Phi(Z)
\le\frac{1}{30c}+
\frac{c-1}{c(c+2)(c+3)(c+5)}
\le\frac{1}{30c}+
\frac{1}{(c+2)(c+3)(c+5)}.
\]
Consequently the preceding expression for \((B_i-B_j)/(2(b-a))\) is at least
\[
\left(\frac1{30}-\frac1{15c}\right)
+\frac{c-1}{(c+2)(c+3)}
-\frac{2}{(c+2)(c+3)(c+5)}>0
\]
for all integers \(c\ge2\). Thus \(B_i>B_j\) whenever \(q_i<q_j\), completing the smallest-factor law for both projections.

**5. Endpoint duality.** Both \(Q\) and \(C\) have symmetric real matrices. Thus their largest absolute row sums equal their largest absolute column sums, so their induced \(\ell_\infty\) norms equal the corresponding \(\ell_1\) norms.

## Verification
A standalone Python 3 standard-library exact-rational checker is included as `check_exact.py`. It constructs the full graph and oriented incidence edges, inverts the grounded integer graph Laplacian using rational Gauss--Jordan elimination, reconstructs every column of \(Q\) and \(C\), and checks the two claimed norms and the diagonal coefficient for each edge against the closed formulas. It also verifies the maximizing-factor statement for every tested parameter tuple. The seven genuinely mixed cases
\[
(2,2,3),\ (2,3,3),\ (2,3,4),\ (3,3,4),\
(2,2,2,3),\ (2,2,3,3),\ (2,2,2,2,3)
\]
cover 579 edge columns. Every exact rational comparison passed. These finite calculations are supporting checks; the all-parameter proof is the resolvent-and-inequality argument above.

## Relationship to prior work
Dilworth, Kutzarova and Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost* (first publicly posted 21 May 2023), develop the cycle/cut projection framework. Their Section 2.6 and Theorem 43 treat **equal-size** alphabet powers, and their Section 2.7 and Theorem 45 determine the binary cube cut-projection norm. Those results provide context but do not state the present mixed-size product formula or the strict smallest-factor extremizer law for both complementary projections. The equal-alphabet endpoint formulas are known and are not asserted as new here. The two-factor rook-graph case is also not asserted as new coverage.

Dilworth, Kutzarova and Ostrovskii, *Lipschitz free spaces on finite metric spaces* (2018 preprint), explain the transportation-cost quotient by cycle space and general projection methods, without the quantitative statement above for mixed Hamming products. The computations here concern **orthogonal projection norms**; the stronger problem of minimizing over all projections is not addressed.

## Limitations
All edges have unit conductance. The result concerns finite products of complete graphs with at least three factors and at least two distinct alphabet sizes, real coordinate edge norms, and canonical orthogonal projections. It does not assert minimality among arbitrary nonorthogonal projections, exact \(\ell_p\) norms for interior exponents, or analogous formulas for weighted edges or general Cartesian factors. Originality assessment is based on accessible primary full text and mathematical record searches; unindexed equivalent results cannot be completely ruled out. No independent mathematical audit has occurred.

## References
1. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582v1 (21 May 2023). https://arxiv.org/abs/2305.12582
2. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Lipschitz free spaces on finite metric spaces*, arXiv:1807.03814 (10 July 2018). https://arxiv.org/abs/1807.03814
