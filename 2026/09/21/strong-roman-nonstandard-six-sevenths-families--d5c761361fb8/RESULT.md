# Nonstandard exact 6/7 families for strong Roman domination

## Statement

For a graph \(G\) with maximum degree \(\Delta\), a **strong Roman dominating function** (StRDF) is a function
\[
f:V(G)\to\{0,1,\ldots,\lceil \Delta/2\rceil+1\}
\]
such that every vertex \(v\) with \(f(v)=0\) has a neighbor \(w\) satisfying
\[
f(w)\ge 1+\left\lceil\frac{|N(w)\cap V_0|}{2}\right\rceil,
\qquad V_0=\{x:f(x)=0\}.
\]
Its minimum weight is the strong Roman domination number \(\gamma_{StR}(G)\).

Let \(S\) be the subdivided claw \(S(K_{1,3})\), rooted at its center \(c\). Thus \(c\) is adjacent to three support vertices \(a,b,d\), and each support has one leaf \(a',b',d'\). Let \(H\) be obtained from \(S\) by adding the edge \(ab\). Hence \(H\) is a seven-vertex unicyclic graph whose unique cycle is the triangle \(cab\).

Let \(F\) be any connected graph on \(m\ge1\) vertices. Replace each vertex \(x\in V(F)\) independently by a rooted copy \(B_x\in\{S,H\}\), and for each edge \(xy\in E(F)\) join the roots of \(B_x\) and \(B_y\). Denote the resulting connected graph by \(R(F;B_x:x\in V(F))\).

**Theorem.** Every such mixed rooted construction satisfies
\[
\boxed{\gamma_{StR}(R(F;B_x))=6m=\frac67\,|V(R(F;B_x))|.}
\]
If at least one block is \(H\), the resulting graph is not isomorphic to a rooted product \(F'\circ_c S(K_{1,3})\) with connected base \(F'\).

Consequently there are infinitely many connected graphs with \(\gamma_{StR}(G)=6|V(G)|/7\) outside the equality family proposed in the closing remarks of Álvarez-Ruiz et al. (2017). This does **not** settle their separate open problem asking whether every connected graph of order at least three satisfies \(\gamma_{StR}(G)\le6|V(G)|/7\).

## Proof

### 1. A local lower bound for the two seven-vertex blocks

Consider an induced copy of either \(S\) or \(H\) inside a larger graph, under the sole condition that only its root \(c\) may have neighbors outside the copy. We claim that every StRDF on the larger graph has total weight at least six on the seven vertices of the copy.

For each support-leaf pair \((x,x')\), one always has \(f(x)+f(x')\ge1\). Moreover, if this sum equals one, then necessarily \(f(x)=0\) and \(f(x')=1\): the alternative \((1,0)\) leaves the zero leaf without a sufficiently strong neighbor.

For the subdivided claw \(S\), if \(f(c)\ge3\), the three pair inequalities already give weight at least six. If \(f(c)=2\) and the block weight were below six, all three pair sums would have to equal one, so all three supports would be zero. Then \(c\) has at least three zero neighbors and label two cannot satisfy the required threshold. If \(f(c)\le1\), every support-leaf pair has weight at least two: a support with pair weight one would be zero and would have no possible strong defender. Thus the block again has weight at least six. This recovers the local mechanism underlying the 2017 extremal tree construction.

Now consider \(H\), with the extra edge \(ab\).

- If \(f(c)\ge3\), the three pair sums give total weight at least six.
- If \(f(c)=2\) and the block weight were below six, again all three pairs would have weight one. Hence \(a,b,d\) are zero and \(a',b',d'\) are one. The root has at least three zero neighbors, so label two cannot defend any of them at the required threshold; in particular \(d\) has no other possible defender.
- If \(f(c)=1\), the \((d,d')\) pair has weight at least two. The two triangle-side pairs together have weight at least three, because if both had weight one then \(a=b=0\), \(a'=b'=1\), and neither zero support would have a strong defender. Hence the block weight is at least \(1+2+3=6\).
- If \(f(c)=0\), the \((d,d')\) pair again has weight at least two. Suppose the two triangle-side pairs had total weight at most three. One of them then has weight one; say \((f(a),f(a'))=(0,1)\). The other pair has weight at most two. The only case in which \(b\) could even have label two is \((f(b),f(b'))=(2,0)\), but then \(b\) has the three zero neighbors \(a,b',c\), so label two is below the required value three. All other possibilities give \(a\) no candidate strong defender at all. Contradiction. Thus the two triangle-side pairs have weight at least four, and the block has weight at least six.

Possible zero neighbors of \(c\) outside the block can only make any defense supplied by \(c\) harder, so the argument remains valid in the full graph.

The blocks are vertex-disjoint in the mixed construction, and only their roots have external neighbors. Summing the local bound over all \(m\) blocks yields
\[
\gamma_{StR}(R(F;B_x))\ge6m.
\]

### 2. Matching upper bound

Give every \(S\)-block the labels
\[
f(c)=3,\qquad f(a)=f(b)=f(d)=0,\qquad
f(a')=f(b')=f(d')=1.
\]
This has weight six and is a valid StRDF locally.

Give every \(H\)-block the labels
\[
f(c)=1,\quad f(a)=0,\quad f(a')=1,\quad
f(b)=2,\quad f(b')=0,\quad f(d)=0,\quad f(d')=2.
\]
Here \(b\) has exactly two zero neighbors \(a,b'\), while \(d'\) defends \(d\), so this also has weight six and is valid.

Every root receives a positive label. Therefore the added edges between roots create no new zero neighbors of a defending root and do not spoil any block labeling. Combining the block labelings gives a global StRDF of weight \(6m\). Hence
\[
\gamma_{StR}(R(F;B_x))=6m.
\]

### 3. The family is genuinely outside the proposed rooted-product equality class

Assume at least one block is \(H\). If \(m=1\), the graph is \(H\), which is unicyclic, whereas the only standard seven-vertex rooted product is the tree \(S\).

Now let \(m\ge2\) and let \(r\ge1\) be the number of \(H\)-blocks. In a standard rooted product \(F'\circ_c S\) on \(7m\) vertices with connected base, there are exactly \(3m\) vertices of degree two: the three support vertices in every block. Roots have degree at least four and leaves have degree one.

In the mixed graph, each \(S\)-block contributes three degree-two vertices, while each \(H\)-block contributes only one, because the two supports incident with the added edge have degree three. Thus the mixed graph has
\[
3(m-r)+r=3m-2r<3m
\]
degree-two vertices. It cannot be isomorphic to any standard rooted product of the same order.

## Relation to prior work

Álvarez-Ruiz, González Yero, Mediavilla-Gradolph, Sheikholeslami and Valenzuela-Tripodoro (2017) proved \(\gamma_{StR}(T)\le6|V(T)|/7\) for every tree and characterized equality by rooted products with the subdivided claw. In their closing Problem 1 they asked whether the same upper bound holds for every connected graph. Immediately after the problem they proposed that, if the bound is correct, equality should occur exactly for connected rooted products with the same subdivided-claw block.

Xu and Wang (2018) established the \(6n/7\) upper bound for several additional graph families and explicitly left the general problem open. Mahmoodi, Nazari-Moghaddam and Behmaram (2020) proved a related upper bound for unicyclic graphs and observed that adding an edge to a standard subdivided-claw extremal tree need not increase the strong Roman domination number; the presently identified triangularized block gives an exact, repeatable equality mechanism and mixed infinite families outside the proposed classification.

Poureidi, Abd Aziz, Jafari Rad and Kamarulhaili (2022) gave linear-time algorithms for trees and unicyclic graphs. The full theorem text of that paper was not inspected here, so it remains the most relevant literature risk for a previously noted seven-vertex unicyclic equality example. A 2026 paper by Valenzuela-Tripodoro et al. studies complexity and exact values for several specific graph families; no equivalent \(6/7\) mixed-block equality construction was located there.

The originality claim is therefore **to the best of our knowledge**. The result does not classify all connected graphs with equality and does not prove or disprove the universal \(6n/7\) upper-bound conjecture.

## Finite verification

A standalone verification script in `artifacts/verify_small.py` independently checks the two local seven-vertex block minima and exhaustively searches all 994 connected graphs of orders three through seven in the NetworkX Graph Atlas. No graph in this range violates \(\gamma_{StR}(G)\le6|V(G)|/7\). Exactly two connected seven-vertex graphs have equality: the subdivided claw and the triangularized claw \(H\), with degree sequences
\[
(1,1,1,2,2,2,3)
\quad\text{and}\quad
(1,1,1,2,3,3,3),
\]
respectively. This computation is corroborative only; the theorem above is proved analytically.

## References

1. M. P. Álvarez-Ruiz, I. González Yero, T. Mediavilla-Gradolph, S. M. Sheikholeslami, J. C. Valenzuela-Tripodoro, “On the strong Roman domination number of graphs,” *Discrete Applied Mathematics* 231 (2017), 44–59. https://doi.org/10.1016/j.dam.2016.12.013
2. J. Xu, Z. Wang, “Note on Strong Roman Domination in Graphs,” *Applied Mathematical Sciences* 12 (2018), 535–541. https://doi.org/10.12988/ams.2018.8351
3. A. Mahmoodi, S. Nazari-Moghaddam, A. Behmaram, “Some Results on the Strong Roman Domination Number of Graphs,” *Mathematics Interdisciplinary Research* 5 (2020), 259–277. https://doi.org/10.22052/mir.2020.225635.1205
4. A. Poureidi, N. A. A. Aziz, N. Jafari Rad, H. Kamarulhaili, “Computing Strong Roman Domination of Trees and Unicyclic Graphs in Linear Time,” *Bulletin of the Malaysian Mathematical Sciences Society* 45 (2022), 2509–2523. https://doi.org/10.1007/s40840-022-01301-4
5. J. C. Valenzuela-Tripodoro, M. A. Mateos-Camacho, M. Cera López, M. P. Álvarez-Ruíz, “Complexity and Exact Values for [k]-Roman and Strong Roman Domination for Specific Graph Families,” *Mathematics* 14 (2026), 1535. https://doi.org/10.3390/math14091535
