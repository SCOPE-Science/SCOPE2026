# Complete dissociation polynomial and Lucas maximum-set law for cycle prisms

## Finding
For every integer \(n\ge 3\), let \(P_n=C_n\square K_2\) be the prism with two parallel cyclic rows of length \(n\) and a rung joining their vertices in every column. A **dissociation set** is a vertex subset inducing maximum degree at most one. Let
\[
J_n(z)=\sum_{\substack{S\subseteq V(P_n)\\\Delta(P_n[S])\le 1}}z^{|S|}.
\]
Put
\[
Q(t,z)=(1+zt+z^2t^2)\bigl(1-(1+z)t-(z+2z^2)t^2+(z^3-z^2)t^3+z^4t^4\bigr).
\]
Then the **complete cardinality enumerator** satisfies the formal-power-series identity
\[
\boxed{\sum_{n\ge3}J_n(z)t^n=-t\frac{\partial}{\partial t}\log Q(t,z)-t-(1+2z)^2t^2.}
\]
Let the Lucas numbers be \(L_0=2\), \(L_1=1\), and \(L_{n+2}=L_{n+1}+L_n\). The largest dissociation sets have size exactly \(n\), and their number is
\[
\boxed{[z^n]J_n(z)=L_n+\begin{cases}2,&3\mid n,\\-1,&3\nmid n,\end{cases}+2\mathbf1_{2\mid n}.}
\]
Equivalently, every minimum vertex subset meeting each three-vertex path of \(P_n\) has size \(n\), and the number of such minimum three-vertex-path covers is the same displayed Lucas expression.

## Assumptions and scope
Graphs are finite, simple, undirected. The simple cycle \(C_n\) has vertices indexed modulo \(n\), and the two rows have vertices \((i,0),(i,1)\). The prism edges connect \((i,r)\) to \((i+1,r)\) and \((i,0)\) to \((i,1)\). The empty vertex set is counted. All identities are over integer polynomials or formal power series, for every \(n\ge3\). A three-vertex-path cover is a set that meets the vertex set of every (not necessarily induced) path on exactly three distinct vertices.

## Proof
**1. Local states and transfer.** For each column encode the selected vertices as \(0,T,B,D\): none, top only, bottom only, both. Their sizes are respectively \(0,1,1,2\). For any three consecutive columns \((a,b,c)\), the selected central vertices have induced degree at most one if and only if the predicate \(\mathcal L(a,b,c)\) holds: if \(b=D\), both \(a=c=0\); if \(b=T\), it is not the case that both \(a,c\) contain their top vertex; if \(b=B\), the analogous prohibition holds for the bottom vertex; and if \(b=0\), the predicate always holds. This is an exact necessity-and-sufficiency test because each vertex has just its rung neighbor and its two adjacent-row neighbors.

Index a \(16\times16\) matrix \(T(z)\) by ordered pairs \((a,b)\) from the four-symbol alphabet, with
\[
T(z)_{(a,b),(b',c)}=\mathbf1_{b=b'}\,\mathbf1_{\mathcal L(a,b,c)}\,z^{|c|}.
\]
A closed length-\(n\) walk in this state graph is equivalent, including its indexed starting column, to a legal cyclic \(n\)-column word. Each selected vertex contributes its weight exactly once, giving \(J_n(z)=\operatorname{tr}(T(z)^n)\). Direct exact determinant expansion (or Newton's identities applied to the traces) gives
\[
\det(I-tT(z))=Q(t,z).
\]
The attached standalone `verify.py` independently reconstructs this identity over \(\mathbb Z[z]\) from the first sixteen traces using Newton's identities. As a formal series, \(-t\partial_t\log\det(I-tT)=\sum_{n\ge1}\operatorname{tr}(T^n)t^n\). The formal trace in orders one and two is respectively \(1\) and \((1+2z)^2\). Removing these two terms proves the announced identity for \(n\ge3\).

**2. Maximum size and all equality cases.** Suppose a legal cyclic column word has \(e\) empty columns, \(d\) double columns, and \(s\) singleton columns. Every double column requires empty columns immediately before and after it. Sending each double column to the empty column immediately following it is injective. Consequently \(d\le e\) and the set has size \(2d+s=n+d-e\le n\). The alternating top-bottom singleton words show size \(n\) is always attainable: any cyclic binary word with no three consecutive equal symbols, such as a suitable repetition of alternating runs of length one or two, is legal; such a word exists for every \(n\ge3\).

In an equality word \(d=e\). If \(d>0\), the injection is bijective, so every empty column follows a double column. As each double column must also be preceded by an empty column, the entire cyclic sequence alternates \(D,0,D,0,\ldots\), requiring even \(n\). There are exactly two such cyclic words when the column indices are fixed. If \(d=e=0\), each column is a singleton, top or bottom. The local predicate then reduces exactly to avoidance of three consecutive identical row symbols, read cyclically.

**3. Counting singleton equality words.** Introduce the four-state automaton whose state is the two most recent binary symbols. It sends \((a,b)\) to \((b,c)\) unless \(a=b=c\). Its adjacency characteristic polynomial is
\[
(\lambda^2-\lambda-1)(\lambda^2+\lambda+1).
\]
The trace of its \(n\)-th power counts cyclic indexed binary words avoiding three equal consecutive symbols. The first quadratic contributes \(L_n\), while the two primitive third roots of unity from the second contribute \(2\) if \(3\mid n\) and \(-1\) otherwise. Adding the two alternating double-empty words when \(n\) is even proves the Lucas formula.

**4. Path-cover duality.** A vertex subset contains no three-vertex path if and only if its induced maximum degree is at most one: a vertex of induced degree at least two supplies a three-vertex path, and every three-vertex path supplies a degree-two central vertex. Taking complements bijects dissociation sets with three-vertex-path covers, reversing cardinalities. The maximum-size formula therefore proves the minimum-cover formula and its multiplicity.

## Verification
The standalone `verify.py` constructs the sixteen-state cyclic automaton, rebuilds its determinant polynomial by integer Newton identities through order sixteen, and checks every subset of the actual simple prism graph for each \(3\le n\le10\) against the transfer enumerator (\(1{,}398{,}080\) subsets total). It also checks the degree and exact Lucas leading coefficient for each \(3\le n\le40\). The check prints `VERIFY_OK`. Sample values are
\[
\begin{aligned}
J_3(z)&=1+6z+15z^2+6z^3,\\
J_4(z)&=1+8z+28z^2+32z^3+8z^4,\\
J_5(z)&=1+10z+45z^2+90z^3+75z^4+10z^5,\\
J_6(z)&=1+12z+66z^2+184z^3+261z^4+144z^5+22z^6.
\end{aligned}
\]
These finite tests corroborate the unrestricted combinatorial proof; they do not replace it.

## Relationship to prior work
Xiao and Kou (arXiv:1608.07022v1, posted 25 August 2016) give kernelization and parameterized algorithms for three-vertex-path covers, rather than exact counts for prism covers. Orlovich, Dolgui, Finke, Gordon and Werner (2011) study complexity and special solvable cases for dissociation-set problems, not a prism all-set cardinality polynomial. Zhou, Chen, Deng and Tu (2024) enumerate dissociation sets for rectangular grid graphs \(P_m\square P_n\) with open boundaries; their state-matrix framework is methodologically related but does not itself state the cyclic two-row formula here. Tu, Xiao, Lang and collaborators (2023) give general cubic-graph dissociation-set bounds rather than an exact cycle-prism distribution. Tian and Tu (2024) enumerate **inclusion-maximal** dissociation sets in several grid families including cyclical grids; inclusion-maximal and all dissociation sets are different enumerated classes. The last paper's abstract was accessible but the complete text was not, so equivalence hidden in that inaccessible full text cannot be completely excluded. The full enumerator and the exact extremal Lucas multiplicity are the contribution asserted here; no novelty is claimed for the definition of dissociation sets, standard transfer matrices, Lucas numbers or complement duality.

## Limitations
No formula is asserted for \(n<3\), where the graph construction and formal short traces differ. The result counts **all** dissociation sets, not only inclusion-maximal ones. The coefficient expression is a formal generating function rather than a positivity/unimodality assertion. Literature priority remains subject to further access to relevant cyclic-grid papers and possible equivalent terminology; no independent external mathematical audit has been performed.

## References
1. Y. Orlovich, A. Dolgui, G. Finke, V. Gordon and F. Werner, *The complexity of dissociation set problems in graphs*, Discrete Applied Mathematics 159 (2011), 1352–1366. DOI: 10.1016/j.dam.2011.04.023.
2. W. Zhou, G. Chen, H. Deng and J. Tu, *Enumeration of dissociation sets in grid graphs*, AIMS Mathematics 9 (2024), 14899–14912. DOI: 10.3934/math.2024721.
3. J. Tu et al., *Counting the number of dissociation sets in cubic graphs*, AIMS Mathematics 8 (2023). DOI: 10.3934/math.2023507.
4. Y. Tian and J. Tu, *Enumerating maximal dissociation sets in three classes of grid graphs*, Applied Mathematics and Computation 474 (2024), 128711. DOI: 10.1016/j.amc.2024.128711.
5. M. Xiao and S. Kou, *Kernelization and Parameterized Algorithms for 3-Path Vertex Cover*, arXiv:1608.07022v1, first posted 25 August 2016.
6. F. Kardoš, J. Katrenič and I. Schiermeyer, *On computing the minimum 3-path vertex cover and dissociation number of graphs*, Theoretical Computer Science 412 (2011), 7009–7017. DOI: 10.1016/j.tcs.2011.09.009.
