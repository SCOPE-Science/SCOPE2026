# The Cayley exchange graph of minimum connected dominating sets in the four-cube

## Finding
Let \(Q_4\) be the graph on \(\{0,1\}^4\), where two vertices are adjacent when they differ in one coordinate. A connected dominating set \(S\) is a vertex subset with connected induced graph \(Q_4[S]\) and closed neighborhood \(N[S]=V(Q_4)\). Write \(\mathcal C\) for the sets of minimum cardinality and form the **token-jumping exchange graph** \(\mathcal R\) on \(\mathcal C\), with an edge precisely when \(|S\setminus T|=|T\setminus S|=1\). The token-sliding exchange graph imposes the additional condition that the removed and inserted vertices are adjacent in \(Q_4\).

Then \(\gamma_c(Q_4)=6\) and \(|\mathcal C|=192\). Every member of \(\mathcal C\) induces a six-vertex path, and all arise from five successive coordinate changes \((a,b,c,d,a)\), with \(a,b,c,d\) a permutation of the four coordinates, allowing either path orientation.

More strongly, \(\mathcal R\) is the undirected **right Cayley graph** of \(H=\mathbb F_2^4\rtimes A_4\), with four specified inverse-closed generators. It has \(192\) vertices, \(384\) edges, is connected and \(4\)-regular, has radius and diameter \(7\), and has odd girth \(11\). Every vertex has the same distance-layer sizes
\[
(1,4,10,23,45,76,30,3).
\]
In contrast, the token-sliding graph on the same \(192\) configurations has **no edges**.

The principal finding is the Cayley identification together with the exact reachability, metric, odd-girth and token-sliding obstruction; the minimum size, path description and number of configurations are included to specify the finite configuration domain, not asserted to be historically unrecorded.

## Assumptions and scope
This is an exact finite theorem for the labelled four-dimensional binary cube, not a claim about arbitrary hypercubes. Identify cube vertices with integers \(0,\ldots,15\) using their four binary coordinates, indexed \(0,1,2,3\). Write \(v\sim w\) when the exclusive-or of their binary labels is one of \(1,2,4,8\). A **jump** removes any vertex of a six-element configuration and inserts any presently unselected vertex, preserving both domination and connectivity; a **slide** further requires the removed and inserted cube vertices to be adjacent.

For the Cayley description, an element of \(H\) is a pair \((p,t)\), with \(p\in A_4\) an even permutation of the four *coordinate positions* and \(t\in\mathbb F_2^4\). It acts on binary vertices by \(v\mapsto p(v)\oplus t\) and hence on vertex sets. Coordinates of \(t\) are encoded as integers \(0,\ldots,15\). Multiplication is \((p,t)(q,u)=(p\circ q,t\oplus p(u))\). The selected base set is
\[
S_0=\{0,1,2,5,10,13\}.
\]
The following four group elements form the generators, expressed as \((p(0),p(1),p(2),p(3);t)\):
\[
(1,0,3,2;0),\quad(2,3,0,1;5),\quad(2,0,1,3;4),\quad(1,2,0,3;1).
\]
The first two are involutions; the last two are mutual inverses.

## Proof
**1. Exhaustion of optimal configurations.** Enumerate each binary characteristic mask of a subset of the sixteen cube vertices for cardinalities \(1\) through \(6\). Connectivity is determined by a graph traversal entirely within the mask, and domination by the bitwise union of the five-point closed neighborhoods of its selected vertices. The complete executable enumeration in `verify_subsets.py` checks *every* subset at these sizes. No connected dominating set has size at most \(5\); exactly \(192\) six-element sets pass, and for each the six induced degrees sort as \((1,1,2,2,2,2)\), so its connected induced graph is \(P_6\). This is an exhaustive finite proof, not extrapolation from a sequence of smaller cubes.

A second exhaustive method in `verify_group.py` grows *all connected subsets* from singletons by adjoining boundary neighbors, independently testing domination at each size. It obtains \(784\) connected five-vertex sets (none dominating; their largest closed neighborhood has size \(14\)), \(1952\) connected six-vertex sets, and again precisely \(192\) connected dominating six-vertex sets. Directly generating the paths obtained by a direction word \((a,b,c,d,a)\) yields the same \(192\) distinct sets: there are \(16\cdot4!=384\) oriented descriptions and each undirected path has two orientations.

**2. All exchanges and the Cayley action.** Examine, for each optimal set \(S\), every ordered choice \((u,w)\) with \(u\in S\), \(w\notin S\), retaining the replacement \((S\setminus\{u\})\cup\{w\}\) if and only if it belongs to the computed optimal-state set. This gives exactly four distinct neighbors per state, \(384\) undirected exchange edges, and never an adjacent pair \(u\sim w\); thus every optimum is token-slide isolated.

The group \(H\) has \(16\cdot12=192\) elements. `verify_group.py` enumerates all of them and verifies that the images of \(S_0\) are \(192\) *different* optimal sets; hence \(H\) acts freely and transitively on the whole optimal-state set. The four optimal neighbors of \(S_0\) are
\[
\begin{split}
&\{0,1,2,5,10,14\},\quad\{0,1,2,5,13,15\},\\
&\{0,2,4,5,10,13\},\quad\{1,2,3,5,10,13\}.
\end{split}
\]
Their unique preimages in \(H\) are exactly the four generators above. Since any cube automorphism preserves connected domination and one-for-one exchange, the neighbors of \(gS_0\) are exactly \(gkS_0\) over these four generators \(k\). This is the claimed exact right-Cayley isomorphism; the software independently checks the equality for all \(192\) group elements.

**3. Metric and odd girth.** A breadth-first search in the exact 192-element Cayley multiplication table, starting at the identity, yields the distance-layer multiplicities \((1,4,10,23,45,76,30,3)\). Its terminal layer is nonempty and no element is farther than seven steps; vertex transitivity propagates this distance distribution to every configuration, proving connectedness and radius equal to diameter equal to seven. An independent BFS on the token-jump graph for *every* root gives the identical layers.

For odd girth, form the double graph on \(H\times\mathbb Z/2\mathbb Z\) whose edges join \((g,\varepsilon)\) to \((gk,1-\varepsilon)\). Exhaustive BFS finds that the shortest path from \((e,0)\) to \((e,1)\) has length \(11\). Such paths correspond to odd closed walks at \(e\); each odd closed walk contains an odd cycle of no greater length. Conversely any odd cycle gives such a walk by conjugating to a chosen base vertex. Vertex-transitivity therefore proves that the shortest odd cycle has length exactly \(11\). For a concrete upper-bound witness, label the generators above \(A,B,C,D\) in order: direct multiplication gives the odd identity word \(ABACCBCCBCC=e\), of length \(11\). The independent token-jump implementation repeats the lower-bound check at every root.

All enumeration domains, membership tests, multiplication formulas, and graph traversals appear in the two complete standard-library-only programs included in this result. Both run to completion with the stated assertions, and their captured outputs are supplied separately.

## Verification
Run `python3 verify_subsets.py` and `python3 verify_group.py` from a directory containing those files. The programs have no external packages or input data. Their recorded stdout files are `verify_subsets.out` and `verify_group.out`. Both terminate with `VERIFY_OK`. The first independently enumerates all small vertex subsets and computes all token-jump distances; the second builds connected subsets by frontier growth, enumerates all direction-word paths, and verifies the exact affine-group Cayley structure and odd relation. Agreement on the 192 optimal states, 384 exchange edges, distance layers, absence of slides, and odd girth is a cross-check; the full exhaustive tests (not sampled finite evidence) prove the specifically stated finite result.

## Relationship to prior work
Fricke, Hedetniemi, Hedetniemi and Hutson (2011) initiated minimum-dominating-set \(\gamma\)-graphs under **adjacent** one-token slides, without imposing connectivity of the selected configuration. Haas and Seyffarth (2013) and Suzuki, Mouawad and Nishimura (2014) consider dominating sets of size *at most* a threshold, with single-vertex additions or deletions; their graphs differ from fixed-cardinality jumps preserving connected domination. Golovach, Heggernes and Kratsch (2015) study enumeration of minimal connected dominating sets, not their exact token-jumping state graph. Lomarda and Canoy (2015) study one-movable connected domination with local moves; this differs from the global jump relation used here. Dvořák, Havel and Mollard (2003) study paths and cycles dominating hypercubes; that may include some of the path configurations counted here but does not, on the accessible abstract, establish the Cayley exchange graph, its distance layers or odd girth. The full text of that last highly relevant publication was not accessible, so an overlap risk remains.

The structurally substantive claims are the exchange graph, its regular affine-Cayley action, the metric/odd-girth profile and the jump-versus-slide separation, not an assertion that a size-six dominating path was previously unknown. Searches under *connected domination*, *four-cube*, *hypercube*, *gamma-graph*, *token jumping*, and *Cayley exchange graph* revealed no published covering theorem in the examined material. Absence from search results is not a proof of priority.

## Limitations
The theorem is finite and limited to the four-cube; no formula for higher-dimensional hypercubes is proved. The finite verification uses exact exhaustive enumeration, not an interactive theorem prover. Historical publication priority has not been independently established. The inaccessible full texts of Dvořák–Havel–Mollard (2003) and Lomarda–Canoy (2015) leave a genuine literature-overlap risk, most notably for the path-shape and movement comparisons. In particular, source-date metadata names the earliest *day-verified* cited reconfiguration source; it does not date the invention of connected domination or dominating paths. An external scientific audit has not been performed.

## References
1. G. H. Fricke, S. M. Hedetniemi, S. T. Hedetniemi and K. R. Hutson, “γ-Graphs of Graphs,” *Discussiones Mathematicae Graph Theory* 31 (2011), 517–531. DOI: `10.7151/dmgt.1562`.
2. R. Haas and K. Seyffarth, “The k-Dominating Graph,” *Graphs and Combinatorics* 30 (2014), 609–617; publicly available accepted manuscript dated 2013. DOI: `10.1007/s00373-013-1302-3`.
3. A. Suzuki, A. E. Mouawad and N. Nishimura, “Reconfiguration of Dominating Sets,” arXiv:`1401.5714`, first posted 2014-01-22.
4. P. A. Golovach, P. Heggernes and D. Kratsch, “Enumerating Minimal Connected Dominating Sets in Graphs of Bounded Chordality,” *IPEC 2015*, DOI: `10.4230/LIPIcs.IPEC.2015.307`.
5. T. Dvořák, I. Havel and M. Mollard, “On Paths and Cycles Dominating Hypercubes,” *Discrete Mathematics* 262 (2003), 121–129. DOI: `10.1016/S0012-365X(02)00524-1` (abstract available; full text not obtained).
6. J. Lomarda and S. R. Canoy Jr., “1-Movable Connected Dominating Sets in Graphs,” *Applied Mathematical Sciences* 9 (2015), 507–514. DOI: `10.12988/ams.2015.411941` (accessible metadata and indexed excerpts; complete text not obtained).
