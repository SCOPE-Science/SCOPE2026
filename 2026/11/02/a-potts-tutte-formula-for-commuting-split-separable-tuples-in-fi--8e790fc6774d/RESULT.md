# A Potts–Tutte formula for commuting split-separable tuples in finite incidence algebras

## Finding

Let \(P\) be any nonempty finite poset, \(k=\mathbb F_q\) any finite field, \(S\subseteq k\) a set of \(r\ge2\) distinct scalars, and \(m\ge1\) an integer. Put
\[
 f_S(T)=\prod_{s\in S}(T-s),\qquad A=I(P,k),
\]
and consider the ordered commuting tuples
\[
 \mathcal X(P,S,m;k)=\{(a_1,\ldots,a_m)\in A^m:\ [a_i,a_j]=0\ \text{for all }i,j,\ f_S(a_i)=0\ \text{for all }i\}.
\]
Let \(G_P\) be the **comparability graph** of \(P\): distinct vertices are adjacent if and only if they are comparable. Write \(E=|E(G_P)|\), \(Q=r^m\), and, for a labeling \(c:P\to S^m\), let
\[
 b(c)=\#\{\{x,y\}\in E(G_P):c(x)\ne c(y)\}.
\]
Then the **complete fixed-diagonal fiber count** and total enumeration are
\[
 \boxed{\ |\mathcal X_c(P,S,m;k)|=q^{b(c)},\qquad
 |\mathcal X(P,S,m;k)|=\sum_{c:P\to S^m}q^{b(c)}.\ }
\]
Here \(\mathcal X_c\) consists of tuples whose joint diagonal eigenvalue at \(x\) is \(c(x)\). More strongly, each such fiber is a single conjugacy orbit under the unitriangular subgroup \(1+\operatorname{rad}A\).

With \(k(F)\) denoting the number of connected components of \((P,F)\), including isolated vertices, the same count has the **random-cluster/Tutte expansion**
\[
 \boxed{\ |\mathcal X(P,S,m;\mathbb F_q)|=
 \sum_{F\subseteq E(G_P)}Q^{k(F)}q^{E-|F|}(1-q)^{|F|}.
 \ }
\]
Equivalently, if \(Z_G(Q,v)=\sum_{F\subseteq E(G)}Q^{k(F)}v^{|F|}\), then
\[
 |\mathcal X(P,S,m;\mathbb F_q)|=q^E Z_{G_P}\!\left(Q,\frac{1-q}{q}\right).
\]
These formulas hold without a characteristic restriction and depend on \(S,m\) only through \(Q=r^m\). In particular, for commuting idempotent tuples one takes \(S=\{0,1\}\), and therefore \(Q=2^m\).

This gives two additional consequences. First, the counts for *all* \(m\ge1\) and all finite fields determine, and are determined by, the ordinary two-variable Tutte/random-cluster polynomial of \(G_P\): the displayed expansion is polynomial in the independent variables \(Q,q\), and the infinitely many evaluations \(Q=2^m\) and prime-power \(q\) uniquely determine it. Second, for any fixed \(Q\), the degree in \(q\) equals the maximum number of bichromatic edges in a \(Q\)-coloring of \(G_P\). If \(h(P)\) is the size of a longest chain, then
\[
 Q\ge h(P)\quad\Longleftrightarrow\quad
 \deg_q|\mathcal X(P,S,m;\mathbb F_q)|=E,
\]
where the left inequality is the condition for the leading term to exist, and its coefficient is the graph's chromatic polynomial evaluated at \(Q\), namely \(\chi_{G_P}(Q)\). For \(Q<h(P)\) the degree is strictly smaller than \(E\).

## Assumptions and scope

The incidence algebra \(I(P,k)\) has basis elements \(e_{xy}\) for \(x\le y\), with multiplication \(e_{xy}e_{uv}=\delta_{yu}e_{xv}\). Its radical \(J\) consists of the zero-diagonal elements; \(1+J\) is the unitriangular group. There is one radical coordinate for every strict comparable pair of \(P\), and hence \(|1+J|=q^E\). The elements of \(S\) must be distinct **in the given field**, so \(f_S\) is separable. The theorem is not asserted for inseparable polynomial constraints, nonsplit roots, or noncommuting tuples. The rank-two case \(S=\{0,1\}\) exists over every finite field.

## Proof

**Step 1 (joint spectral idempotents).** For each coordinate \(i\) and \(s\in S\), use the Lagrange polynomial
\[
 \ell_s(T)=\prod_{t\in S\setminus\{s\}}\frac{T-t}{s-t}.
\]
Since \(f_S(a_i)=0\) and the roots in \(S\) are distinct, the elements \(\ell_s(a_i)\), \(s\in S\), form a complete set of orthogonal idempotents for each \(i\). The \(a_i\) commute; hence the products
\[
 e_\alpha=\prod_{i=1}^m\ell_{\alpha_i}(a_i),\qquad \alpha\in S^m,
\]
are pairwise orthogonal idempotents satisfying \(\sum_\alpha e_\alpha=1\), and \(a_i=\sum_\alpha\alpha_i e_\alpha\). Their diagonal entries determine a unique joint label \(c:P\to S^m\).

**Step 2 (constructive simultaneous conjugation).** Let \(d_\alpha\) denote the diagonal idempotent supported on \(\{x\in P:c(x)=\alpha\}\). Put
\[
 u=\sum_{\alpha\in S^m}d_\alpha e_\alpha.
\]
At each vertex \(x\), exactly one label \(\alpha=c(x)\) contributes a diagonal \(1\), so \(u\) has all diagonal entries \(1\). Hence \(u\in1+J\) and is invertible. Orthogonality gives
\[
 ue_\beta=d_\beta e_\beta=d_\beta u.
\]
Thus \(ue_\beta u^{-1}=d_\beta\) for every \(\beta\), and consequently \(ua_i u^{-1}=\sum_\alpha\alpha_i d_\alpha\) for every coordinate. Conversely, conjugating this fixed diagonal tuple by any element of \(1+J\) produces a tuple in \(\mathcal X_c\). Therefore **the entire joint-diagonal fiber is one orbit**.

**Step 3 (orbit-stabilizer).** A unitriangular element \(v\) stabilizes this diagonal tuple exactly when it commutes with each coordinate diagonal. For every \(x<y\) in \(P\), the \((x,y)\)-entry of the \(i\)-th commutator is
\[
 (c_i(y)-c_i(x))v_{xy}.
\]
If \(c(x)\ne c(y)\), some coefficient is nonzero and forces \(v_{xy}=0\); otherwise that entry is free. Hence the stabilizer has exactly \(q^{E-b(c)}\) elements. Orbit-stabilizer proves the fiber size \(q^{b(c)}\), and summing over joint labels proves the first boxed formula.

**Step 4 (graph expansion).** For one edge \(\{x,y\}\), its contribution to \(q^{b(c)}\) is \(q+(1-q)\mathbf1_{c(x)=c(y)}\). Expanding the product over edges gives
\[
 \sum_{F\subseteq E(G_P)}q^{E-|F|}(1-q)^{|F|}
 \sum_{c:P\to[Q]}\prod_{\{x,y\}\in F}\mathbf1_{c(x)=c(y)}.
\]
A labeling contributes to the inner sum precisely when it is constant on each connected component of \((P,F)\), so the inner sum is \(Q^{k(F)}\). This establishes the second boxed formula.

**Step 5 (threshold and recovery).** Because each coefficient in the coloring expression is nonnegative, the highest exponent of \(q\) equals the largest possible number of differently colored comparable pairs. That exponent is \(E\) precisely when \(G_P\) admits a proper \(Q\)-coloring. Every chain of length \(h(P)\) forms a clique and requires \(h(P)\) colors. Conversely, coloring each vertex by the length of a longest chain ending there is a proper coloring using at most \(h(P)\) colors. Hence the claimed threshold is exact, and the leading coefficient is the number of proper \(Q\)-colorings, \(\chi_{G_P}(Q)\). Finally, the Fortuin–Kasteleyn expansion is a bivariate polynomial in \(Q,q\); infinitely many values \(Q=2^m\) and infinitely many prime-power values \(q\) determine it by polynomial identity, establishing recovery.

## Verification

Run `python3 checker.py` using Python 3 and the standard library. It constructs every element of several small incidence algebras directly as a matrix over \(\mathbb F_p\), tests the prescribed polynomial identity, and checks pairwise commutation by independent matrix products. It compares those direct counts with independent coloring sums. The test suite includes characteristic two and odd characteristic; arities one and two; two- and three-root split polynomials; chains, a four-vertex diamond, an antichain, and dual three-vertex forks. The observed marker is `INCIDENCE_SPLIT_TUPLE_POTTS_OK 32 5625`. The finite tests are not an infinite proof; Steps 1–5 prove the general theorem.

For a three-vertex fork or its order dual, the comparability graph is a path with two edges. Thus its common tuple-count polynomial is
\[
 Q+2Q(Q-1)q+Q(Q-1)^2q^2.
\]
These opposite orientations have nonisomorphic incidence algebras, but identical tuple counts for every \(q,S,m\). For commuting idempotent pairs in characteristic two, the count is \(196\) in either algebra.

## Relationship to prior work

Khripchenko and Novikov (2008, Theorem 3) prove that **one** idempotent in a finitary incidence algebra is conjugate to a diagonal idempotent; their Theorem 5 supplies poset recovery from the incidence algebra. The present argument handles an **entire commuting tuple** (and arbitrary split-separable polynomial roots) by simultaneous spectral idempotents, determines the finite-field stabilizer and full fiber size, and connects all arities to a graph polynomial. It does not claim the single-idempotent conjugacy result as new.

Can, Casimiro and Malheiro (2022, Theorem 3.2) establish the connected components and ordinary conjugacy orbits of the idempotent variety over the complex numbers, with an explicit dimension computation for complete bipartite posets in Proposition 4.6. They do not state the arbitrary-arity commuting-tuple count or the finite-field Potts–Tutte formula in the inspected full text. Their results are close conceptual predecessors, particularly for one idempotent; our claim is not a new classification of single-idempotent components.

Sokal's 2005 survey gives the established random-cluster/Potts polynomial \(Z_G(Q,v)\) and its combinatorial interpretation. The new assertion is the precise incidence-algebra realization and extraction of that polynomial from commuting split-separable tuple counts, not the definition or general combinatorial theory of the Tutte polynomial. More general separable-subalgebra lifting and homomorphism-variety literature might imply some orbit statements; the possibility of an unlocated equivalent enumeration is a residual publication-priority risk.

## Limitations

No count is claimed for tuples of matrices that do not commute, for inseparable minimal polynomials, or for prescribed irreducible nonsplit factors. The theorem concerns finite incidence algebras, not arbitrary triangular-pattern algebras whose patterns are not transitive. The formulas count ordered tuples, not tuples modulo the full unit group, and their graph invariance does not identify the incidence algebra up to isomorphism. Historical originality is provisional, and independent mathematical validation has not been performed.

## References

1. N. S. Khripchenko and B. V. Novikov, *Finitary incidence algebras*, arXiv:0803.0069v1, publicly submitted 2008-03-01, especially Theorems 2, 3 and 5. https://arxiv.org/abs/0803.0069
2. A. D. Sokal, *The multivariate Tutte polynomial (alias Potts model) for graphs and matroids*, arXiv:math/0503607v1, publicly submitted 2005-03-25, especially Section 1 and the Fortuin–Kasteleyn representation. https://arxiv.org/abs/math/0503607
3. M. Bilen Can, A. Casimiro and A. Malheiro, *Idempotent Varieties of Incidence Monoids and Bipartite Posets*, arXiv:2208.01073v1, publicly submitted 2022-08-01, especially Theorem 3.2 and Proposition 4.6. https://arxiv.org/abs/2208.01073
4. J. J. Garcés and M. Khrypchenko, *Potent preservers of incidence algebras*, Linear Algebra and its Applications **635** (2022), 171–200; DOI:10.1016/j.laa.2021.11.020. The paper concerns linear preservers, not finite-field tuple enumeration.
