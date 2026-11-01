# Star-boundary sphere wedges in open-neighborhood complexes of high-girth line graphs

## Finding
**Theorem.** Let \(H\) be any finite connected simple graph of girth at least five (no triangles or quadrilaterals) and minimum degree at least three. Write \(n=|V(H)|\), \(m=|E(H)|\), \(d_v=\deg_H(v)\), and \(n_3=|\{v\in V(H):d_v=3\}|\). Let \(L(H)\) be the line graph: its vertices are edges of \(H\), and two are adjacent exactly when their original edges meet. Write \(\mathcal N(G)\) for the **open** Lovász neighborhood complex whose faces are vertex subsets having a common adjacent vertex (without allowing a vertex to be adjacent to itself).

Then there is a sequence of elementary simplicial collapses from \(\mathcal N(L(H))\) onto an explicitly described graph-of-star-boundaries, and
\[
\boxed{\mathcal N(L(H))\simeq
\bigvee^{2m-n+1+n_3} S^1\ \vee\
\bigvee_{\substack{v\in V(H)\\d_v\ge4}}S^{d_v-2}.}
\]
Thus its fundamental group is free on \(2m-n+1+n_3\) generators; for \(k\ge2\), its reduced integral homology is free of rank \(|\{v:d_v=k+2\}|\) in degree \(k\), and vanishes in all other degrees. In particular, there is no torsion. The classification includes high-degree, non-block line graphs and graphs with intersecting long cycles.

The structural contribution is the uniform **relative collapse of every two-star open neighborhood**, whose mixed edges uniquely identify their generating edge when the base graph has no short cycles. The resulting wedge formula applies to a base graph having vertices of degree at least four, where previously available low-degree and block-graph formulas do not apply.

For instance, the incidence graph of the projective plane of order three is a connected four-regular graph with \(n=26\), \(m=52\), and girth six; its line-graph neighborhood complex has homotopy type \(\bigvee^{79}S^1\vee\bigvee^{26}S^2\).

## Assumptions and scope
All graphs are finite, undirected, loopless and without parallel edges. Connectedness and minimum degree at least three ensure every base edge has at least two other edges available at each endpoint. Girth at least five excludes all cycles of lengths three and four, whether or not induced. The complex \(\mathcal N\) uses **open**, not closed, neighborhoods; a closed-neighborhood Čech complex is a different construction. A wedge with zero summands of a given dimension is omitted.

For a base vertex \(v\), set \(S_v=\{e\in E(H):v\in e\}\) and \(X_v=\partial\Delta(S_v)\), the boundary of the simplex on its incident edges; \(X_v\cong S^{d_v-2}\) because \(d_v\ge3\). For a base edge \(e=uv\), set \(A_e=S_u\setminus\{e\}\) and \(B_e=S_v\setminus\{e\}\). These sets are nonempty and disjoint. Select arbitrary \(a_e\in A_e\), \(b_e\in B_e\).

## Proof
**1. The exact neighborhood cover.** The open neighbors in \(L(H)\) of its vertex \(e=uv\) are the base edges other than \(e\) incident with \(u\) or \(v\). Therefore
\[
\mathcal N(L(H))=\bigcup_{e=uv\in E(H)}\Delta(A_e\sqcup B_e).
\]
Its unmixed faces lie in \(X=\bigcup_{v\in V(H)}X_v\): every \(\Delta(A_e)\) is a facet of \(X_u\) and every \(\Delta(B_e)\) is a facet of \(X_v\). Conversely every facet of \(X_v\) equals \(\Delta(S_v\setminus\{e\})\) for some incident edge \(e\), so \(X\) is exactly the union of unmixed faces.

**2. Unique generating edge for every mixed face.** Let \(a\in A_e\), \(b\in B_e\) with \(e=uv\). They have the form \(a=uw\) and \(b=vz\). As \(H\) has no triangle, \(w\ne z\), so \(a,b\) are disjoint base edges. Any generating edge \(f\) whose open neighborhood in \(L(H)\) contains both \(a,b\) must connect one endpoint of \(a\) to one endpoint of \(b\), and must be distinct from them. One choice is \(e=uv\). An additional choice shares an endpoint with \(e\) and creates a triangle using \(a\) or \(b\), or has endpoints \(w,z\) and creates the four-cycle \(u-w-z-v-u\). Both are forbidden. Hence **the mixed pair \(\{a,b\}\) lies in exactly one generating simplex**, namely \(\Delta(A_e\sqcup B_e)\). All cofaces of any mixed face containing that pair lie in the same generating simplex. This uniqueness is global, even when long cycles in \(H\) overlap.

**3. Explicit elementary collapses of each two-block simplex, relative to the unmixed faces.** Fix \(e\), abbreviate \(A=A_e\), \(B=B_e\), and choose \(a_0=a_e\), \(b_0=b_e\). Every face meeting both \(A\) and \(B\) belongs exclusively to this block. Perform the following codimension-one elementary collapses **within this block**, retaining every unmixed face:

First, for every nonempty \(U\subseteq A\setminus\{a_0\}\) and every nonempty \(V\subseteq B\), pair the lower mixed face \(U\cup V\) with the upper mixed face \(U\cup V\cup\{a_0\}\). Remove pairs in decreasing size of the lower face. At a given step all other proper cofaces of the lower face have been removed: any coface still inside the block is either a larger lower face or the upper partner of a larger lower face, except its own paired upper face. There are no cofaces outside the block by step 2. Thus every step removes a genuine free-face/facet pair.

Second, for each nonempty \(V\subseteq B\setminus\{b_0\}\), pair \(\{a_0\}\cup V\) with \(\{a_0,b_0\}\cup V\), again in decreasing lower-face size. The same freeness argument applies after the first stage, since all mixed faces containing a member of \(A\setminus\{a_0\}\) are gone. These two stages remove every mixed face except the edge \(\{a_0,b_0\}\) and its vertices. They leave the complete unmixed faces untouched.

Different blocks cannot share a mixed face by step 2, so their elementary-collapse sequences cannot interfere. It follows that the **entire** neighborhood complex simplicially collapses onto
\[
Y=X\ \cup\ \bigcup_{e\in E(H)}\{\{a_e,b_e\}\}.
\]
The edge \(\{a_e,b_e\}\) is not already in \(X\), because the two base edges it joins are disjoint. Different choices of \(e\) give different retained edges by step 2.

**4. Graph of spaces and integral homotopy type.** Each \(X_v\) is a sphere of dimension at least one. For distinct vertices \(u,v\), \(X_u\cap X_v\) is precisely the vertex of the line graph labeled \(uv\) if \(uv\in E(H)\), and empty otherwise. Three distinct \(X_v\)'s never meet. The associated incidence graph of these sphere-subspaces is precisely \(H\). A connected graph of path-connected spaces attached at single points has homotopy type of the wedge of its vertex spaces with \(m-n+1\) additional circles: this follows by collapsing a spanning tree of the incidence graph and retaining its other edges. Therefore
\[
X\simeq\left(\bigvee^{m-n+1}S^1\right)\vee\bigvee_{v\in V(H)}S^{d_v-2}.
\]
Each of the \(m\) extra retained edges \(\{a_e,b_e\}\) joins two points in the connected space \(X\) and is otherwise disjoint from \(X\) and from the other added edge interiors. Attaching such an interval adds one circle, by contracting a path in \(X\) between its endpoints. Thus
\[
Y\simeq X\vee\bigvee^{m}S^1.
\]
Finally, exactly the \(n_3\) star boundaries of degree-three vertices are circles; every other star boundary has dimension at least two. Combining the circle multiplicities yields \((m-n+1)+m+n_3=2m-n+1+n_3\). The proposed homotopy type and all integral homological consequences follow. No finite-experiment inference is used.

## Verification
The standalone Python program `verify.py` reconstructs each simple graph, rejects examples violating connectedness, minimum degree or the short-cycle restriction, directly enumerates the actual open-neighborhood complex \(\mathcal N(L(H))\), and builds the proposed retained subcomplex \(Y\). It checks that every cross-block pair has exactly one generating neighborhood. It executes **every** specified elementary collapse and checks immediately beforehand that each lower face has exactly its single paired strict coface among all remaining faces. It then compares the complete simplicial face set to \(Y\), computes independent reduced binary boundary ranks of both complexes, and checks the theorem's predicted ranks.

Six graphs were checked: the Petersen and Heawood graphs, the 26-vertex projective-plane incidence graph, that incidence graph with one and two pairwise disjoint edges deleted, and a girth-five graph formed by bridging the Petersen and projective-plane incidence graphs. Together these have 11,766 augmented simplicial faces and 5,062 verified elementary collapse pairs. The projective-plane case has 26 nontrivial two-sphere summands; the edge-deletion cases have 24 and 22, respectively. The bridge-joined nonbipartite example has 110 circle summands, 26 two-spheres and one three-sphere. Run `python3 verify.py`; all exact finite tests must return `EXACT_GLOBAL_COLLAPSE_AND_MOD2_HOMOLOGY_OK`. In addition, the script checks counterexamples outside the domain: for \(H=K_4\) (triangles), the actual line-graph neighborhood complex has first reduced binary Betti number \(1\), not the naive extrapolation \(13\); for \(H=K_{3,3}\) (squares), the actual first and second reduced binary Betti numbers are \(2\) and \(1\), not the extrapolated circle-only answer. These examples motivate the forbidden-cycle boundary. The proof of the universal result is in the preceding sections, not the finite checks.

## Relationship to prior work
Shukla [1] studies open-neighborhood complexes of graphs with maximum degree at most three, plus a restricted class of four-regular circulants. The **line graph** of the high-degree base graphs here has vertices of degree at least four, and the explicitly exhibited 26 higher-dimensional sphere summands cannot be explained by the cubic maximum-degree result.

The published *Blockwise sphere bouquets in neighborhood complexes of block graphs* [2] classifies block graphs, including line graphs of trees. Every present base graph with a cycle has a chordless cycle of length at least five, inducing a cycle in its line graph, which therefore is not a block graph. The degree-at-least-four and cyclic cases are outside that result. The published *Graph-like neighborhood complexes with edge-disjoint four-cycles* [3] classifies a different family whose neighborhood complexes reduce to graph spines: a degree-four vertex in \(H\) supplies a clique \(K_4\) inside \(L(H)\), containing overlapping four-cycles and violating its hypothesis. Thus the present higher-sphere cases are not consequences of [3]. The cubic-only special case is not asserted as a new phenomenon.

Goyal, Shukla and Singh [4] classify **clique** complexes \(\operatorname{Cl}(L(H))\), which differ from the open-neighborhood complex constructed here. Their result \(\operatorname{Cl}(L(H))\simeq H\) for triangle-free base graphs has only degree-one homology and cannot imply the higher sphere summands here. The earlier result *A scale-two Čech collapse theorem for line graphs of girth at least five* [5] concerns the **closed-neighborhood** Čech complex \(\bigcup_{e=uv}\Delta(S_u\cup S_v)\), again a different complex. Our open-neighborhood construction systematically deletes the generating edge \(e\) from each facet, changing the homotopy type. The decisive new step is the unique mixed-edge collapse for these **open** neighborhoods.

## Limitations
The theorem requires minimum degree at least three and excludes triangles and quadrilaterals. It makes no claim for graphs with short cycles or pendant vertices, and it does not determine a canonical equivariant splitting of the degree-one part under automorphisms. The output is an ordinary integral homotopy classification, not a claim that all target spheres are realized by disjoint simplicial subcomplexes. The checker supplies exhaustive **finite** verification only for the six listed examples; arbitrary graphs are covered by the abstract proof. A targeted literature and research-record comparison supports originality against the inspected claims but cannot establish absolute priority over unindexed equivalent results.

## References
1. S. Shukla, *Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs*, arXiv:1802.04526, first public 2018-02-13, https://arxiv.org/abs/1802.04526.
2. *Blockwise sphere bouquets in neighborhood complexes of block graphs*, publicly archived mathematical finding, 2026, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-blockwise-sphere-bouquets-in-neighborhood-complexes-of-block-gra--2a7bb737f35c.
3. *Graph-like neighborhood complexes with edge-disjoint four-cycles*, publicly archived mathematical finding, 2026, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-graph-like-neighborhood-complexes-with-edge-disjoint-four-cycles--d8f86495e49d.
4. S. Goyal, S. Shukla, and A. Singh, *Topology of Clique Complexes of Line Graphs*, arXiv:2009.12130, first public 2020-09-25, https://arxiv.org/abs/2009.12130.
5. *A scale-two Čech collapse theorem for line graphs of girth at least five*, publicly archived mathematical finding, 2026, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-a-scale-two-ech-collapse-theorem-for-line-graphs-of-girth-at-lea--69ae03a7604c.
