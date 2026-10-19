# Three-distance law and Wiener polynomial for annihilator-inclusion graphs of finite principal ideal rings

## Finding

Let \(R\) be a finite commutative principal ideal ring. Write its local decomposition as \(R\cong\prod_{i=1}^{r}R_i\), where \(r\geq1\), every \(R_i\) is a finite chain ring, \(q_i=|R_i/\mathfrak m_i|\), and \(m_i\geq1\) is the least index satisfying \(\mathfrak m_i^{m_i}=0\). Define the annihilator-inclusion graph \(\mathcal I(R)\) to have vertices the nonzero zero divisors of \(R\), with distinct vertices adjacent when their annihilator ideals are comparable by inclusion.

Put
\[
P=\prod_{i=1}^{r}q_i^{m_i},\qquad
U=\prod_{i=1}^{r}(q_i-1)q_i^{m_i-1},\qquad
N=P-U-1,
\]
\[
T=\prod_{i=1}^{r}\frac{q_i^{2m_i+1}+1}{q_i+1},\qquad
Q=\prod_{i=1}^{r}\frac{(q_i-1)q_i^{2m_i}+2}{q_i+1},
\]
and
\[
E=T-(U+1)P+U-\frac{Q-U^2-1+N}{2}.
\]
Then \(N\) is the number of vertices and \(E\) is the number of edges of \(\mathcal I(R)\). For unordered distinct vertex pairs, let \(D_k\) count pairs at distance \(k\).

**Disconnected boundary.** If \(r=2\) and \(m_1=m_2=1\), the graph is a disjoint union of two complete graphs. Exactly \(U\) unordered pairs lie in different components; \(D_1=E\) and \(D_2=D_3=0\).

**All other cases.** Every pair is connected, and
\[
\boxed{D_1=E,\qquad D_3=(2^{r-1}-1)U,\qquad D_2=\binom N2-E-(2^{r-1}-1)U.}
\]
The factor \(2^{r-1}-1\) is zero at \(r=1\). Consequently the exact Wiener polynomial (unordered-pair convention) is
\[
\boxed{\mathcal W_R(t)=Et+\left(\binom N2-E-(2^{r-1}-1)U\right)t^2+(2^{r-1}-1)Ut^3,}
\]
and the Wiener index is
\[
\boxed{W(\mathcal I(R))=N(N-1)-E+(2^{r-1}-1)U.}
\]
For \(r\geq2\) outside the disconnected boundary, the diameter is exactly three; for \(r=1\), the graph is complete, if nonempty. The polynomial is defined as zero when there are fewer than two vertices.

As a direct finite consequence, for \(R=\mathbb Z/4\mathbb Z\times\mathbb Z/4\mathbb Z\),
\[
N=11,\quad D_1=30,\quad D_2=21,\quad D_3=4,\quad W=84,\quad\operatorname{diam}=3.
\]
This corrects the value four asserted for that ring in Example 2.1 of Safari--Shaveisi--Nikandish (2026), with the graph definition unchanged.

## Assumptions and scope

All rings are commutative and unital. A finite chain ring has a totally ordered ideal lattice \(R_i\supsetneq\mathfrak m_i\supsetneq\cdots\supsetneq\mathfrak m_i^{m_i}=0\); a field is allowed with \(m_i=1\). The decomposition into chain rings exists for every finite commutative principal ideal ring. The graph is simple and loopless; \(0\) and all units are excluded. The definition comes from Safari--Shaveisi--Nikandish (2026), not from Badawi's different annihilator graph. The Wiener index is used only for the connected cases, since standard disconnected-pair distances would be infinite.

For \(x_i\in R_i\), define \(v_i(x_i)=j\) if \(x_i\in\mathfrak m_i^j\setminus\mathfrak m_i^{j+1}\), and set \(v_i(0)=m_i\). Its level size is
\[
w_i(j)=\begin{cases}(q_i-1)q_i^{m_i-j-1},&0\leq j<m_i,\\1,&j=m_i.\end{cases}
\]
A vertex of \(\mathcal I(R)\) has valuation vector in the product of intervals \(\prod_i\{0,\ldots,m_i\}\), except for the bottom vector \(\mathbf 0\) (units) and top vector \(\mathbf m\) (zero). Its multiplicity is \(\prod_iw_i(v_i)\). For each vector, all associated vertices form a clique, and two distinct vector classes are completely joined exactly when their vectors are coordinatewise comparable.

## Proof

**1. Reduction to a weighted product of chains.** On a chain factor, annihilator ideals increase with valuation: \(\operatorname{ann}_{R_i}(x_i)=\mathfrak m_i^{m_i-v_i(x_i)}\). Thus the annihilators of two elements of \(R\) are comparable if and only if their valuation vectors are comparable in the coordinatewise order. The number of elements in each valuation class is \(\prod_iw_i(v_i)\), proving the clique-blowup description. Since every nonunit of a finite commutative ring is a zero divisor, precisely the bottom and top vectors are excluded. This gives \(N=P-U-1\).

**2. Exact edge count.** The number of ordered pairs \((x,y)\in R^2\) with \(v(x)\leq v(y)\) factors as \(T\), because on a single chain
\[
\sum_{j=0}^{m} w(j)\sum_{k=j}^{m}w(k)=\sum_{j=0}^{m}w(j)q^{m-j}=\frac{q^{2m+1}+1}{q+1}.
\]
The number of ordered pairs with equal valuation vectors is \(Q\), since
\[
\sum_{j=0}^{m}w(j)^2=\frac{(q-1)q^{2m}+2}{q+1}.
\]
Deleting all pairs with a unit or with zero leaves \(T_V=T-(U+1)P+U\) ordered comparable pairs: a unit can occur as the lower vector, zero as the upper, and their \(U\) cross pairs are counted twice. Equal-vector pairs remaining number \(Q_V=Q-U^2-1\). Every edge between distinct vectors contributes one ordered comparable pair, whereas within each clique the ordered-pair count is twice the number of edges plus the diagonal. Therefore
\[
E=T_V-\frac{Q_V+N}{2}=T-(U+1)P+U-\frac{Q-U^2-1+N}{2}.
\]

**3. Which pairs need three steps.** Consider two *incomparable* valuation vectors \(a,b\). A common neighbor has valuation vector at most both, or at least both: a mixed comparison would force \(a,b\) themselves comparable. Thus there is a common neighbor if and only if their coordinatewise meet differs from the bottom vector, or their coordinatewise join differs from the top vector. An existing non-endpoint meet or join is an allowable graph vertex and is distinct from both incomparable endpoints. Failure of both alternatives forces, coordinate by coordinate, \(\{a_i,b_i\}=\{0,m_i\}\). Hence the only potential distance-three pairs are opposite nonempty proper Boolean corners.

For \(r\geq3\), write one corner as support \(S\subsetneq\{1,\dots,r\}\). After interchanging endpoints if needed, \(|S|\geq2\). Select \(i\in S\); the nonempty proper supports \(\{i\}\) and \(\{i\}\cup S^c\) supply a three-edge path from \(S\) to \(S^c\). Since no common neighbor exists, three is the exact distance. For \(r=2\) with (say) \(m_1\geq2\), the opposite corners \((m_1,0)\), \((0,m_2)\) are joined by
\[
(m_1,0)\;\text{--}\;(1,0)\;\text{--}\;(1,m_2)\;\text{--}\;(0,m_2).
\]
Its intermediate vectors are neither bottom nor top. If both chain lengths equal one, there are only the two opposite nonempty corners and no path between them: the graph is a disjoint union of two cliques. For \(r=1\), every pair of allowable vectors is comparable, so the graph is complete.

**4. Counting opposite corners and all other distances.** A corner with support \(S\) (valuation \(m_i\) precisely on \(S\)) has multiplicity \(\prod_{i\notin S}|R_i^\times|\); its opposite corner has multiplicity \(\prod_{i\in S}|R_i^\times|\). Their product is always \(U\). The nonempty proper subsets of the \(r\) factors form \(2^{r-1}-1\) unordered complementary pairs. Thus there are \((2^{r-1}-1)U\) opposite-corner element pairs, at distance three except in the disconnected two-field case. All remaining nonedges lie at distance two. Substituting the edge count gives the stated distance distribution and Wiener formulas.

**5. Exact small-ring correction.** The direct count for \((\mathbb Z/4\mathbb Z)^2\) gives eleven vertices, thirty edges, twenty-one distance-two pairs and four distance-three pairs, so diameter three. For an illustrative diameter-three pair, \((1,0)\) and \((0,1)\) are connected by the valid three-edge path
\[
(1,0)\;\text{--}\;(1,2)\;\text{--}\;(0,2)\;\text{--}\;(0,1).
\]
The coordinatewise classification excludes any four-step shortest path, including for other pairs.

## Verification

Run the standalone Python 3 standard-library script `verify.py`. It directly enumerates elements and nonunits of 29 residue rings \(\mathbb Z/n\mathbb Z\) using integer gcd divisibility, then enumerates nine actual direct products of prime-power residue rings, including \((\mathbb Z/4\mathbb Z)^2\). Each graph is constructed independently of the closed formulas, and breadth-first search gives the exact counts of distances one, two, three and disconnected pairs. Six additional weighted-valuation models include nonprime residue-field cardinalities \(4\) and \(8\). The program recomputes the claimed closed-form values separately and asserts complete agreement.

Expected terminal summary: `VERIFY_OK 29 cyclic rings, 9 direct products, and 6 nonprime-field valuation models`. In particular, the actual product ring \((\mathbb Z/4\mathbb Z)^2\) gives `(30, 21, 4, 0)` at distances \((1,2,3,\infty)\). These finite tests supplement rather than establish the general proof.

## Relationship to prior work

Safari, Shaveisi and Nikandish (2026, Theorems 2.1--2.3) define the inclusion graph of annihilators, characterize disconnection and obtain a general connected diameter bound of four. Their Example 2.1 states diameter four for \((\mathbb Z/4\mathbb Z)^2\); the present complete distance classification proves that the diameter is three. The full theorem here is confined to finite commutative principal ideal rings and is not a global bound for all commutative rings.

For finite rings, the graph is exactly the complement of the cozero-divisor graph. Afkhami and Khashyarmanesh (2012) explicitly study this complement; Nouri Jouybari, Talebi and Firouzian (2019) recognize it as an induced part of a scalar-product graph. The complement identification and comparability adjacency are *prior knowledge*, not new assertions. Baloda, Mathil, Kumar and Barapatre (2022) give Wiener formulas for the **cozero-divisor graph itself**, whose edges correspond to incomparable principal ideals; the present theorem gives the full distance distribution and Wiener index of its **complement**, with distinct geodesics and an exceptional disconnected case. Badawi's annihilator graph is a third, different graph, and its published metric formulas do not imply this theorem merely through shared terminology.

## Limitations

The result assumes all local factors are chain rings; it does not treat arbitrary nonprincipal finite local rings or arbitrary infinite rings. The polynomial is only defined for finite pair distances; in the disconnected case the standard Wiener index is not finite, so only the componentwise edge and disconnected-pair census is asserted. The ring is not reconstructed from the distance polynomial. An equivalent older computation under scalar-product or cozero-complement terminology remains a bibliographic possibility. Independent validation of the mathematical argument has not been performed.

## References

1. H. Safari, F. Shaveisi and R. Nikandish, *Inclusion graph of annihilators in a commutative ring*, arXiv:2606.15498 (first public version 13 June 2026), https://arxiv.org/abs/2606.15498.
2. M. Afkhami and K. Khashyarmanesh, *On the Cozero-Divisor Graphs of Commutative Rings and Their Complements*, Bull. Malays. Math. Sci. Soc. 35(4) (2012), 935--944, https://math.usm.my/bulletin/pdf/v35n4/v35n4p10.pdf.
3. M. Nouri Jouybari, Y. Talebi and S. Firouzian, *Scalar Product Graphs of Modules*, Int. J. Nonlinear Anal. Appl. 10 (2019), 75--82, https://doi.org/10.22075/IJNAA.2019.4398.
4. B. Baloda, P. Mathil, J. Kumar and A. Barapatre, *Wiener index of the Cozero-divisor graph of a finite commutative ring*, arXiv:2210.01570 (2022), https://arxiv.org/abs/2210.01570.
