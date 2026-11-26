# Three-distance law and Wiener polynomial for annihilator-inclusion graphs of finite principal ideal rings

## Finding

Let \(R\cong\prod_{i=1}^r R_i\) be a nonzero finite commutative principal ideal ring, with \(r\ge1\) and finite chain-ring factors. For factor \(i\), let \(\mathfrak m_i\) be its maximal ideal, \(q_i=|R_i/\mathfrak m_i|\), and \(m_i\ge1\) be the least index such that \(\mathfrak m_i^{m_i}=0\). The annihilator-inclusion graph \(\mathcal I(R)\) has vertices the nonzero zero divisors of \(R\). Distinct vertices are adjacent if their annihilators are comparable by inclusion. Write
\[
P=\prod_i q_i^{m_i},\qquad U=\prod_i(q_i-1)q_i^{m_i-1},\qquad N=P-U-1,
\]
\[
T=\prod_i\frac{q_i^{2m_i+1}+1}{q_i+1},\qquad
Q=\prod_i\frac{(q_i-1)q_i^{2m_i}+2}{q_i+1},\qquad
E=T-(U+1)P+U-\frac{Q-U^2-1+N}{2}.
\]
There are \(N\) vertices and \(E\) edges. For unordered pairs of distinct vertices, let \(D_j\) count pairs at distance \(j\).

If \(r=2\) and \(m_1=m_2=1\), the graph consists of two disjoint cliques, with \(U\) unordered pairs in different components and \(D_1=E,\ D_2=D_3=0\). In all other cases, every pair is connected, and
\[
D_1=E,\qquad D_3=(2^{r-1}-1)U,\qquad D_2=\binom N2-E-D_3.
\]
The Wiener polynomial over unordered distinct pairs and its corresponding Wiener index are
\[
\mathcal W_R(t)=Et+\bigl(\tbinom N2-E-(2^{r-1}-1)U\bigr)t^2+(2^{r-1}-1)Ut^3,
\qquad W(\mathcal I(R))=N(N-1)-E+(2^{r-1}-1)U.
\]
For \(r\ge2\) outside the disconnected two-field case, the diameter is exactly three. For \(r=1\) the graph is complete if nonempty. The polynomial is zero when there are fewer than two vertices. In the disconnected case only the pair counts, not a finite Wiener index, are asserted.

For \(R=(\mathbb Z/4\mathbb Z)^2\) the formulas give \(N=11\), \((D_1,D_2,D_3)=(30,21,4)\), \(W=84\), and diameter three. This corrects the value four in Example 2.1 of Safari–Shaveisi–Nikandish, using their definition without modification.

## Assumptions and scope

All rings are commutative and unital. A field is a chain factor with \(m_i=1\). The chain-factor decomposition is that of finite commutative principal ideal rings. Vertices are elements, not principal ideals or equivalence classes; the graph is simple and has no loops. The zero ring is not part of the nonzero-ring hypotheses above; if included separately, its vertex set is empty.

## Proof

**Valuation model.** In one chain factor, a generator \(\pi\) of the maximal ideal has powers giving the ideal chain. An element of valuation \(j<m\) is a unit times \(\pi^j\), and zero has valuation \(m\). The annihilator at level \(j\) is \(\mathfrak m^{m-j}\), so annihilator comparisons are coordinatewise comparisons of valuation vectors \(v\). The number of elements of level \(j\) is
\[
w(j)=(q-1)q^{m-j-1}\quad(j<m),\qquad w(m)=1,
\]
by the one-dimensional successive ideal quotients over the residue field. Each valuation vector is therefore represented by a clique of size \(\prod_i w_i(v_i)\); between different vector cliques all cross edges occur precisely when the vectors are comparable. The excluded vectors are the bottom \(\mathbf 0\) (the \(U\) units) and the top \(\mathbf m\) (the one zero element). Indeed, any nonunit in a finite commutative ring is a zero divisor, since its multiplication map is not surjective and hence is not injective. This proves the vertex formula.

**Edges.** Over the whole ring the count of ordered element pairs with \(v(x)\le v(y)\) factors as \(T\) and the count with equal vectors as \(Q\). On a single factor the two sums are
\[
\sum_{j=0}^{m} w(j)\sum_{k=j}^{m}w(k)=\sum_{j=0}^{m}w(j)q^{m-j}=\frac{q^{2m+1}+1}{q+1},\qquad
\sum_{j=0}^{m}w(j)^2=\frac{(q-1)q^{2m}+2}{q+1}.
\]
Removing comparable ordered pairs with a lower unit or an upper zero subtracts \(UP+P-U\); their \(U\) intersections must be subtracted once, not twice. Removing equal-vector pairs at the bottom and top subtracts \(U^2+1\). On the remaining comparable ordered pairs an edge between distinct profiles contributes once, an edge within a profile twice, and a diagonal pair once. The within-profile ordered count is twice the number of within-profile edges plus \(N\). Consequently the edge count is
\[
T-(U+1)P+U-\frac{Q-U^2-1+N}{2}.
\]

**Distances.** For two incomparable profiles \(a,b\), the profile of any common neighbor must be at most both or at least both, since mixed orientations imply comparability by transitivity. Thus a common neighbor exists exactly when the coordinatewise meet is not the deleted bottom or the coordinatewise join is not the deleted top. For incomparable endpoints such a meet or join is distinct from either endpoint. Failure of both tests means that each coordinate has values \(\{0,m_i\}\) in the two profiles, so the two are opposite nonempty proper Boolean corners.

For \(r\ge3\), identify these corners with supports \(S,S^c\), interchange if necessary so that \(|S|\ge2\), and choose \(i\in S\). The proper nonempty supports \(\{i\}\) and \(\{i\}\cup S^c\) give the three-edge path \(S\)--\(\{i\}\)--\((\{i\}\cup S^c)\)--\(S^c\). For \(r=2\) with \(m_1\ge2\), there is a path of profiles
\[
(m_1,0)\;\text{--}\;(1,0)\;\text{--}\;(1,m_2)\;\text{--}\;(0,m_2),
\]
and interchanging coordinates treats \(m_2\ge2\). Each intermediate class represents at least one vertex and is neither bottom nor top. If both lengths equal one, only the two incomparable corner cliques remain, so there is no path between them. When \(r=1\) all profiles are comparable.

**Census.** A corner with support \(S\) has multiplicity \(\prod_{i\notin S}|R_i^\times|\), and its opposite has multiplicity \(\prod_{i\in S}|R_i^\times|\). Their product is \(U\). There are \(2^{r-1}-1\) unordered complementary nonempty proper support pairs. In the connected cases these account for all distance-three pairs; other nonedges are at distance two. As soon as \(r\ge2\) these opposite corners exist, proving the claimed diameter outside the disconnected case. In the exceptional two-field case their single complementary support pair gives the \(U\) disconnected pairs. Subtraction from \(\binom N2\) and the weighted sum \(D_1+2D_2+3D_3\) give the stated Wiener formulas.

**Small-ring example.** For \((\mathbb Z/4\mathbb Z)^2\) one has \((P,U,T,Q)=(16,4,121,36)\) and the displayed counts follow. Actual elements \((1,0)\) and \((0,1)\) have opposite corner profiles, so no common neighbor; an element-level three-edge path is \((1,0)\)--\((1,2)\)--\((0,2)\)--\((0,1)\).

## Verification

The companion standard-library Python 3 script `verify.py` checks 29 cyclic rings using gcd divisibility, nine products of residue rings, and six weighted-valuation models including nonprime residue-field sizes. The expected terminal line is `VERIFY_OK 29 cyclic rings, 9 direct products, and 6 nonprime-field valuation models`. For the actual product ring \((\mathbb Z/4\mathbb Z)^2\) the distance categories \((1,2,3,\infty)\) have counts \((30,21,4,0)\) of unordered distinct pairs. The finite tests are supplementary; the universal claim rests on the proof above.

## Relationship to prior work

Safari–Shaveisi–Nikandish [1, §2] introduce this annihilator-inclusion graph, study disconnectedness, and give a general connected diameter bound of four. Their Example 2.1 states diameter four for \((\mathbb Z/4\mathbb Z)^2\), while the pair census above gives three under the same definition. The present distance theorem does not assert a global bound for arbitrary commutative rings.

**For finite commutative principal ideal rings**, this graph agrees with the complement of the cozero-divisor graph: local principal ideals \((x_i)=\mathfrak m_i^{v_i(x_i)}\) reverse valuation order, whereas local annihilators preserve it, so both lead to exactly the same comparability adjacency in the product. The equivalence is not asserted for arbitrary finite commutative rings. For instance, in \(\mathbb F_2[x,y]/(x,y)^2\) the residue classes of \(x\) and \(y\) have the same annihilator but incomparable principal ideals. Afkhami–Khashyarmanesh [2] study the cozero-divisor complement, and Nouri Jouybari–Talebi–Firouzian [3, Remark 2.5] give the cyclic-submodule comparability rule in the scalar-product graph, which yields that complement upon restriction to the relevant elements. These comparability formulations are not new. Baloda et al. [4] compute Wiener formulas for the cozero-divisor graph itself, with incomparable principal ideals adjacent; that is not the metric of its complement. Badawi's annihilator graph is a different graph as well.

## Limitations

The pair classification uses chain local factors and does not treat arbitrary nonprincipal finite local rings or infinite rings. No finite all-pair Wiener index is asserted for the disconnected boundary. An equivalent earlier weighted comparability-graph computation under different terminology remains possible.

## References

1. H. Safari, F. Shaveisi and R. Nikandish, *Inclusion graph of annihilators in a commutative ring*, arXiv:2606.15498, https://arxiv.org/abs/2606.15498.
2. M. Afkhami and K. Khashyarmanesh, *On the Cozero-Divisor Graphs of Commutative Rings and Their Complements*, Bull. Malays. Math. Sci. Soc. 35(4) (2012), 935–944, https://math.usm.my/bulletin/pdf/v35n4/v35n4p10.pdf.
3. M. Nouri Jouybari, Y. Talebi and S. Firouzian, *Scalar Product Graphs of Modules*, Int. J. Nonlinear Anal. Appl. 10 (2019), 75–82, https://doi.org/10.22075/IJNAA.2019.4398.
4. B. Baloda, P. Mathil, J. Kumar and A. Barapatre, *Wiener index of the Cozero-divisor graph of a finite commutative ring*, arXiv:2210.01570, https://arxiv.org/abs/2210.01570.
