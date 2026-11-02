# Characteristic-two graphical groups: involution classes and maximal elementary abelian subgroups

## Finding

Let \(\Gamma=(V,E)\) be an arbitrary finite simple undirected graph, with \(n\geq 1\) vertices and \(m\) edges. For every \(q=2^e\), \(e\geq 1\), consider the graphical group \(G_\Gamma(q)\) defined below. Write \(I_\Gamma(t)=\sum_{S\subseteq V\text{ independent}}t^{|S|}\), and let \(N(S)\) denote the set of vertices outside \(S\) adjacent to at least one vertex of \(S\).

**Theorem (quadratic support, conjugacy, and elementary abelian subgroups).**

1. The number of group elements of order dividing two (including the identity) is
   \[
   T_2(\Gamma,q)=q^m I_\Gamma(q-1).
   \]
   In particular the number of nonidentity involutions is \(T_2(\Gamma,q)-1\). For every integer \(j\geq0\), the number of conjugacy classes consisting of elements of order dividing two and having class size \(q^j\) is
   \[
   K_j(\Gamma,q)=q^{m-j}\sum_{\substack{S\subseteq V\text{ independent}\\|N(S)|=j}}(q-1)^{|S|}.
   \]
   To count classes of *nonidentity* involutions, subtract one from \(K_0\) and leave the other coefficients unchanged.

2. Let \(W\cong(\mathbb F_q^E,+)\) be the canonical central edge subgroup. For every \(r\geq0\), the number \(A_r\) of elementary abelian subgroups \(H\) with \(W\leq H\) and \(|H|=2^{em+r}\) is
   \[
   A_r(\Gamma,e)=\sum_{t=0}^{n}a_t\sum_{j=0}^{t}(-1)^{t-j}\binom tj {ej\brack r}_2,
   \]
   where \(a_t=[z^t]I_\Gamma(z)\) and \({N\brack r}_2\) denotes the binary Gaussian coefficient, taken to be zero outside \(0\leq r\leq N\). This is a complete rank census of elementary abelian subgroups containing \(W\).

3. **All** inclusion-maximal elementary abelian subgroups of \(G_\Gamma(q)\) are precisely
   \[
   H_S=\{(x,z):\operatorname{supp}(x)\subseteq S,\ z\in\mathbb F_q^E\},
   \]
   indexed without repetition by the maximal independent vertex sets \(S\) of \(\Gamma\). Their orders are \(q^{m+|S|}\). Therefore the maximum possible order is \(q^{m+\alpha(\Gamma)}\), and exactly \(a_{\alpha(\Gamma)}\) elementary abelian subgroups attain it. All inclusion-maximal elementary abelian subgroups have equal order **if and only if** the graph is well-covered (all its maximal independent sets have the same cardinality).

All assertions hold without a connectivity assumption, including graphs with isolated vertices and the edgeless graph. They require only that \(q\) is a power of two.

## Assumptions and scope

Fix any ordering \(V=\{1,\ldots,n\}\) and orient each edge \(\{i,j\}\) for bookkeeping as \(i<j\). Elements are pairs \((x,z)\in \mathbb F_q^V\times\mathbb F_q^E\). Multiplication is
\[
(x,z)(y,w)=(x+y,z+w+B(x,y)),\qquad
B(x,y)_{\{i,j\}}=x_i y_j\quad(i<j).
\]
The bilinearity of \(B\) implies associativity. The identity is \((0,0)\), and \(W=\{(0,z):z\in\mathbb F_q^E\}\) is central and elementary abelian of rank \(em\) over \(\mathbb F_2\). This standard presentation is the finite-field graphical group of Rossmann. An elementary abelian subgroup here means a subgroup all of whose nonidentity elements have order two. An independent vertex set contains no edge; a maximal independent set need not have maximum cardinality.

For clarity, the conjugacy count \(K_j\) includes the identity as one size-one class; exact-order-two class counts omit it. The coefficient \({N\brack r}_2\) equals the number of \(r\)-dimensional \(\mathbb F_2\)-linear subspaces of \(\mathbb F_2^N\), with \({N\brack0}_2=1\). No assumption of odd characteristic or of exponent two for the entire graphical group is made: if \(E\neq\varnothing\), its exponent is four.

## Proof

**1. The square map.** The defining cocycle gives
\[
(x,z)^2=(0,Q(x)),\qquad Q(x)_{\{i,j\}}=x_i x_j.
\]
Thus \((x,z)^2=1\) if and only if the set \(S=\operatorname{supp}(x)\) is independent in \(\Gamma\). For every independent \(S\) there are \((q-1)^{|S|}\) vectors \(x\) with support exactly \(S\), and each admits \(q^m\) independent choices of \(z\). This proves the formula for \(T_2\).

**2. Conjugacy class sizes conditional on order two.** In characteristic two the commutator of \((x,z)\) and \((y,w)\) is \((0,C_x(y))\), with
\[
C_x(y)_{\{i,j\}}=x_i y_j+x_j y_i.
\]
Suppose that \(S=\operatorname{supp}(x)\) is independent. For every \(v\in N(S)\), the coordinate \(y_v\) contributes to at least one edge \(\{u,v\}\) with \(u\in S\), where the nonzero scalar \(x_u\) makes its coefficient nonzero. No edge contains two vertices of \(S\), and contributions from distinct \(v\notin S\) have disjoint sets of edge coordinates. Hence the linear map \(C_x\) has rank exactly \(|N(S)|\) over \(\mathbb F_q\). A conjugacy class in a class-two group is a coset of the image of this commutator map; it therefore has \(q^{|N(S)|}\) elements. Dividing the \(q^m(q-1)^{|S|}\) elements with support exactly \(S\) by this common class size proves \(K_j\). The identity belongs to \(S=\varnothing\).

**3. Elementary abelian subgroups above \(W\).** Quotienting by \(W\) gives the additive \(\mathbb F_2\)-space \(\mathbb F_q^V\) of dimension \(en\). Each subgroup \(H\) containing \(W\) is the full inverse image of one \(\mathbb F_2\)-linear subspace \(U\), and \(H\) is elementary abelian exactly when \(Q(u)=0\) for all \(u\in U\). Indeed, squaring is the identity test, and a group in which every element squares to the identity is automatically abelian.

Let \(S\subseteq V\) be the union of the supports of vectors of \(U\). If an edge \(\{i,j\}\) lay inside \(S\), the two coordinate maps \(U\to\mathbb F_q\), \(u\mapsto u_i\) and \(u\mapsto u_j\), would both be nonzero. Their kernels are proper \(\mathbb F_2\)-subspaces of \(U\). Since two proper subspaces cannot cover a vector space, some \(u\in U\) would satisfy \(u_i u_j\ne0\), contradicting \(Q(u)=0\). Therefore \(S\) is independent. Conversely every \(\mathbb F_2\)-subspace of \(\mathbb F_q^S\) has \(Q=0\) if \(S\) is independent.

For fixed independent \(S\) of cardinality \(t\), inclusion-exclusion over the coordinates computes the number of \(r\)-spaces \(U\leq\mathbb F_q^S\) whose union of supports is exactly \(S\):
\[
\sum_{T\subseteq S}(-1)^{|S|-|T|}{e|T|\brack r}_2
=\sum_{j=0}^{t}(-1)^{t-j}\binom tj{ej\brack r}_2.
\]
Summing over the \(a_t\) independent \(t\)-sets proves the stated formula for \(A_r\), without double counting.

**4. Maximality.** If \(H\) is elementary abelian, so is \(HW\), because \(W\) is central and elementary abelian. Every inclusion-maximal elementary abelian \(H\) therefore contains \(W\). Its quotient subspace \(U\) has some independent support \(S\) by part 3 and satisfies \(U\leq\mathbb F_q^S\). Maximality forces \(U=\mathbb F_q^S\), then forces \(S\) to be a maximal independent set. Conversely, for a maximal independent set \(S\), any elementary abelian enlargement of \(H_S\) would have independent support strictly containing \(S\), which is impossible. All remaining assertions about maximum order, multiplicity, and well-covered graphs follow.

## Verification

The accompanying Python 3 standard-library program `verify.py` independently implements finite-field multiplication, the group cocycle, squares, commutators, binary reduced-row-echelon subspace enumeration and the claimed graph-polynomial counts. It exhaustively checks every simple labeled graph on two, three and four vertices over \(\mathbb F_2\), and every simple labeled graph on two and three vertices over \(\mathbb F_4\): \(74+10=84\) graph-field configurations. For each it checks the number of elements of order dividing two, the order-restricted conjugacy-class size distribution, and every possible rank of an elementary abelian subgroup containing \(W\). Output: `VERIFY_OK 84 independent graph-field cases: group-square, conjugacy, F2-subspace census`.

For example, for the three-vertex path and \(q=2\), the group has \(32\) elements; exactly \(20\) have order dividing two. Its maximal elementary abelian subgroups have orders \(8\) and \(16\), corresponding respectively to the center vertex and the two endpoints. This test illustrates that *maximal by inclusion* and *maximum order* differ.

The program's exhaustive ranges are finite; the universal conclusions depend on the proof above, not on the computation. To reproduce, run `python3 verify.py` with no external dependencies.

## Relationship to prior work

Rossmann, *Enumerating conjugacy classes of graphical groups over finite fields*, arXiv:2107.05564 (publicly posted July 12, 2021; published in *Bulletin of the London Mathematical Society* 2022), defines the graphical groups and enumerates **all conjugacy classes by size**. That unconditioned class-size polynomial is prior work. The present conjugacy formula is a different joint statistic: it restricts to elements of order dividing two. The all-class distribution does not by itself determine which classes consist of involutions.

Qiao, *A q-analogue of graph independence polynomials with a group-theoretic interpretation*, arXiv:2408.09963 (publicly posted August 19, 2024), enumerates totally isotropic linear spaces and interprets them as abelian subgroups for **odd-prime** class-two groups of exponent the prime. Its group-theoretic interpretation does not classify elementary abelian subgroups of the characteristic-two **exponent-four** graphical groups here. In characteristic two the square map is a nontrivial quadratic refinement of the alternating commutator map, and being elementary abelian requires the stronger condition that all squares vanish. This distinction is essential: applying only the isotropy condition would incorrectly include some exponent-four abelian subgroups.

The independence polynomial and binary Gaussian coefficients are classical. The assessed contribution is their exact characteristic-two group-theoretic interpretation, including the involution/class-size joint distribution, full elementary abelian rank census above the edge center, and the classification of all inclusion-maximal elementary abelian subgroups.

## Limitations

The theorem is specific to the canonical graphical groups over fields of characteristic two. It does not count all abelian subgroups (many have exponent four), and the rank census \(A_r\) only concerns elementary abelian subgroups containing \(W\); the classification of **inclusion-maximal** elementary abelian subgroups concerns all of them. No claim is made that the full rank census of smaller elementary abelian subgroups avoiding \(W\) is given by \(A_r\). Statements about new publication priority are provisional, because an equivalent result could occur in broader work on quadratic maps and exponent-four class-two groups.

## References

1. Tobias Rossmann, *Enumerating conjugacy classes of graphical groups over finite fields*, arXiv:2107.05564, first public version July 12, 2021; *Bull. Lond. Math. Soc.* **54** (2022), 1923–1943. https://arxiv.org/abs/2107.05564 ; https://doi.org/10.1112/blms.12665.
2. Youming Qiao, *A q-analogue of graph independence polynomials with a group-theoretic interpretation*, arXiv:2408.09963, first public version August 19, 2024. https://arxiv.org/abs/2408.09963.
