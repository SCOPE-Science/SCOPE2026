# Flag rigidity and sharp exchange threshold for connected domination in projective-plane incidence graphs

## Finding
Let \(\Pi\) be **any finite projective plane of order \(q\ge 2\)**, including non-Desarguesian planes, and let \(G_\Pi\) be its undirected bipartite point–line incidence graph. A *connected dominating set* is a vertex set \(D\) for which every vertex outside \(D\) has a neighbor in \(D\) and the induced graph \(G_\Pi[D]\) is connected. A *flag* is an incident point–line pair \((p,\ell)\). Define the **flag double star**
\[
D(p,\ell)=\{x:x\text{ is a point on }\ell\}\cup\{m:m\text{ is a line through }p\}.
\]

**Theorem.** The connected domination number and its entire minimizing family are
\[
\gamma_c(G_\Pi)=2(q+1),\qquad
\operatorname{MinCD}(G_\Pi)=\{D(p,\ell):p\in\ell\}.
\]
Every minimizing set has exactly \(q+1\) point-vertices and \(q+1\) line-vertices, induces a tree consisting of two adjacent centers and \(q\) leaves at each center, and has a unique neighbor inside the set for **every** exterior vertex. There are exactly \((q^2+q+1)(q+1)\) minimizing sets.

Consequently, the maximum number of leaves of a spanning tree is \(2q^2\), and there are exactly \((q^2+q+1)(q+1)\) spanning trees attaining this maximum, one for each flag.

For an integer \(r\ge1\), define the **optimal \(r\)-exchange graph** whose vertices are the minimum connected dominating sets and whose distinct vertices \(D,D'\) are adjacent when \(|D\setminus D'|=|D'\setminus D|\le r\). For \(1\le r<q\), this graph has no edges. For \(r=q\), it is canonically the line graph \(L(G_\Pi)\), has \((q^2+q+1)(q+1)\) vertices, \(q(q^2+q+1)(q+1)\) edges, degree \(2q\), and radius and diameter three. Therefore **\(q\) simultaneous replacements is the exact threshold at which all optimal configurations become mutually reconfigurable.**

## Assumptions and scope
A projective plane of order \(q\) has \(v=q^2+q+1\) points and the same number of lines; each point lies on \(q+1\) lines and each line contains \(q+1\) points; two distinct points have exactly one common line and two distinct lines exactly one common point. Throughout, \(q\) is an integer for which such a plane exists, and \(q\ge2\). No field coordinatization or transitive automorphism group is assumed. The graph \(G_\Pi\) has \(2v\) vertices and is regular of degree \(q+1\).

The exchange move removes and adds **the same number of vertices, at most \(r\), in one simultaneous operation**. It does not require intermediate sets to remain feasible during the operation. All statements concern unweighted simple graphs and ordinary vertex-induced connected domination.

## Proof
**1. Universal lower bound and equality conditions.** Write \(n=2v\), \(d=q+1\), and let \(D\) be connected dominating with \(k=|D|\). Its induced graph has at least \(k-1\) edges. Thus its edge boundary satisfies
\[
|E(D,V\setminus D)|=dk-2|E(G_\Pi[D])|\le (q-1)k+2.
\]
Every one of the \(n-k\) exterior vertices needs at least one boundary edge. Therefore
\[
2v-k\le(q-1)k+2,\qquad
qk\ge2(v-1)=2q(q+1),
\]
and \(k\ge2(q+1)\). For equality, both inequalities must be tight: \(G_\Pi[D]\) is a tree and every exterior vertex has **exactly one** neighbor in \(D\).

**2. A flag attains equality.** Given a flag \((p,\ell)\), the set \(D(p,\ell)\) contains \(q+1\) points on \(\ell\) and \(q+1\) lines through \(p\). Since \(p\in\ell\), its induced graph is a double star centered at \(p\) and \(\ell\), hence connected. A point outside \(\ell\) lies on exactly one selected line, the line joining it to \(p\); a line not through \(p\) meets \(\ell\) at exactly one selected point. Therefore the set dominates and every exterior vertex has one selected neighbor. The lower bound is sharp.

**3. Rigidity of every equality case.** Let \(D\) attain the lower bound, with its selected point set \(A\) and selected line set \(B\). Both sets contain at least two elements. Indeed if, say, \(|A|=1\), connectedness forces all chosen lines to pass through that sole point, so \(|D|\le q+2<2q+2\); an empty part is also impossible. The dual argument gives \(|B|\ge2\).

The unique-exterior-neighbor condition forces the joining line of **any two** chosen points to lie in \(B\): otherwise that unselected line would have two selected neighbors. Dually, the intersection of **any two** chosen lines is in \(A\). No three chosen points can be noncollinear, because their three distinct joining lines, all selected, would form a six-cycle in \(G_\Pi[D]\), contradicting that it is a tree. Thus all points of \(A\) lie on one line \(\ell\), and the pairwise-joining rule forces \(\ell\in B\). The dual argument makes all lines of \(B\) concurrent at one point \(p\in A\). It follows that \(p\in\ell\).

Every point of \(\ell\) must be selected. Otherwise an omitted point \(x\in\ell\setminus\{p\}\) admits a line \(m\ne\ell\) through \(x\) but not \(p\). Such a line is not selected, and since \(A\subseteq\ell\) it has no selected point-neighbor, contradicting domination. Dually, every line through \(p\) must be selected: if an omitted \(m\ni p\), choose a point \(x\in m\setminus\ell\). This point is unselected and its only possible selected-line neighbor would have been \(m\), again contradicting domination. Therefore \(D=D(p,\ell)\). Distinct flags give distinct sets, and their count is the number of incidence pairs \(v(q+1)\).

**4. Optimal spanning trees.** In any spanning tree with at least three vertices, its internal (nonleaf) vertices form a connected dominating set. Hence there are at most \(2v-2(q+1)=2q^2\) leaves. For each flag, take the induced double-star edges and attach every exterior vertex by the unique edge to its selected neighbor. This is a spanning tree with precisely \(2q^2\) leaves, because every selected vertex has tree degree at least two for \(q\ge2\). Conversely, a spanning tree with \(2q^2\) leaves has exactly \(2(q+1)\) internal vertices and therefore has a unique flag double star as its internal vertex set. The tree edges within that set are forced by its double-star structure; every exterior leaf has a uniquely determined attachment. Thus the association between flags and maximum-leaf spanning trees is a bijection.

**5. Sharp reconfiguration threshold.** For two distinct flags with common point \(p\) but different lines, the two sets share their entire line-pencil part and exactly one point, so their symmetric exchange size is \(q\). The dual holds for flags with a common line. If the flags share neither point nor line, their selected point sets intersect at exactly \(\ell\cap\ell'\), and their selected line sets at the joining line of \(p,p'\); thus their intersection has two vertices and the exchange size is \(2q\). No two distinct sets differ in fewer than \(q\) removals. At the threshold \(r=q\), two flags are adjacent precisely when their corresponding edges in \(G_\Pi\) share an endpoint: the exchange graph is exactly \(L(G_\Pi)\). Its degree is \(2q\) and its edge count \(qv(q+1)\).

Every pair of edges in \(G_\Pi\) can be joined through a common point-to-point line in at most three edge steps, so \(\operatorname{diam}(L(G_\Pi))\le3\). More explicitly for flags \((p,\ell)\) and \((p',\ell')\), if neither shared endpoint nor crossed incidence connects them directly, the intermediate flags \((p,pp')\) and \((p',pp')\) form a path of length three. There exist pairs with \(p\notin\ell'\) and \(p'\notin\ell\) for every \(q\ge2\), forcing distance three. The plane's incidence symmetries are not needed for the uniform radius: from any fixed flag one can choose a point \(p'\notin\ell\) and a line \(\ell'\ni p'\) avoiding \(p\), giving distance three. Hence radius and diameter are both three.

## Verification
Two self-contained standard-library programs provide independent finite checks of the proof's sharpness and classification: `verify_binary_plane.py` constructs the order-two plane from nonzero binary vectors, verifies every connected dominating vertex subset of its 14-vertex incidence graph, enumerates its 21 minimizing flags, explicitly builds all 21 maximum-leaf spanning trees, and confirms the two-exchange graph has 42 edges and diameter three. `verify_ternary_plane.py` independently builds the order-three plane using normalized ternary projective coordinates and dual covectors, evaluates all \(\binom{26}{8}=1{,}562{,}275\) size-eight subsets, finds exactly 52 connected dominating sets, proves the three-exchange threshold and reconfiguration distances at that order, and verifies unique exterior attachments. Run `python3 verify_binary_plane.py` and `python3 verify_ternary_plane.py` beside these documents. Corresponding actual outputs are provided as `binary_check.txt` and `ternary_check.txt`. These finite tests corroborate, but do **not** establish, the theorem for arbitrary \(q\); Steps 1–5 above provide the universal proof.

## Relationship to prior work
Caro, West and Yuster [1] explain the general equivalence between minimum connected domination and maximum-leaf spanning trees, and establish broad bounds. The present exact projective-plane rigidity, enumeration, and batch-reconfiguration threshold are additional claims, not consequences of their displayed general bounds.

Goldberg, Rajendraprasad and Mathew [2] address **ordinary domination** in design incidence graphs. Their projective-plane ordinary domination number \(2q\) does not determine the connected domination number, its minimizing structures, or its exchange graph. Héger and Nagy [3] classify small **ordinary** dominating sets; their results about minimal dominating sets address a distinct inclusion-minimal condition and do not assert that the flag double stars are exactly the minimum **connected** dominating sets or determine their transition threshold.

Relevant mathematical-record searches for projective-plane flag exchange, connected domination of Levi graphs, and maximum-leaf incidence spanning trees found no result implying this exact structural classification. In particular, results on total domination in subspace **intersection** graphs, on doubly connected domination in complete multipartite graphs, and on topological complexes of incidence graphs do not yield the claimed incidence-graph connected-domination result. Unindexed equivalent formulations remain possible.

## Limitations
The classification presupposes existence of a finite projective plane of order \(q\); it does not establish existence for any particular order. The simultaneous-exchange threshold does not imply connectivity under sequential single-vertex moves. The proof is exact and independent of the finite enumerations, but priority has not been independently certified. The full article of [1] was not materially inspected beyond its publisher abstract and bibliographic information; targeted portions of the full-text manuscripts [2] and [3] were inspected. This access limitation leaves a residual possibility of unobserved prior exact examples or reformulations. No independent external audit was performed.

## References
[1] Yair Caro, Douglas B. West, Raphael Yuster, *Connected Domination and Spanning Trees with Many Leaves*, SIAM Journal on Discrete Mathematics 13 (2000), 202–211, DOI: 10.1137/S0895480199353780. Official online publication date shown as 2006-08-01 at https://epubs.siam.org/doi/10.1137/S0895480199353780.

[2] Felix Goldberg, Deepak Rajendraprasad, Rogers Mathew, *Domination in Designs*, arXiv:1405.3436v1, 2014-05-14, https://arxiv.org/abs/1405.3436.

[3] Tamás Héger, Zoltán Lóránt Nagy, *Dominating Sets in Projective Planes*, arXiv:1603.02933v1, 2016-03-09, https://arxiv.org/abs/1603.02933.
