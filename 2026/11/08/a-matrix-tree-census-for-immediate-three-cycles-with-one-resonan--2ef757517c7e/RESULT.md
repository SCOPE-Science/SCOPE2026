# A matrix-tree census for immediate three-cycles with one resonant graph cycle

## Finding
Let \(G\) be a finite, connected, simple, undirected graph. Assume that among all simple cycles of \(G\), **exactly one** has length divisible by three; denote it by \(C\). Every vertex has a nonnegative integer chip count. At each synchronous update, a vertex holding at least its degree sends one chip to every neighbor; all vertices update simultaneously. Write \(U\) for this map and
\[
P_3(G)=\bigl|\{x\in\mathbb Z_{\ge0}^{V(G)}:U^3x=x\ne Ux\}\bigr|.
\]
Contract all vertices and edges of \(C\) to one vertex, retaining parallel edges arising from distinct original edges and discarding loops. For the resulting connected multigraph \(G/C\), write \(\tau(G/C)\) for its number of spanning trees, counting parallel edges separately. Then
\[
\boxed{P_3(G)=12\,\tau(G/C).}
\]
If \(G\) has **no** simple cycle of length divisible by three, then \(P_3(G)=0\). For a connected cactus with exactly one cycle whose length is divisible by three, and other simple-cycle lengths \(\ell_1,\ldots,\ell_s\) not divisible by three, the formula specializes to
\[
\boxed{P_3(G)=12\prod_{j=1}^s\ell_j.}
\]
The number of *distinct* temporal orbits of least period three is \(P_3(G)/3\). All counts distinguish chip assignments to the specified vertices, and concern periodicity **from the initial time**, without any transient.

## Assumptions and scope
A graph is simple and connected, with at least three vertices under the unique-cycle hypothesis. Every degree \(d_v\) is positive. The update is \(U(x)_v=x_v-d_vf_v(x)+\sum_{w\sim v}f_w(x)\), where \(f_v(x)=1\) exactly when \(x_v\ge d_v\). Contraction must retain distinct parallel edges; their multiplicities matter for the matrix-tree count. A graph is a cactus if any two of its simple cycles have at most one vertex in common. The theorem makes no assertion about eventual periods after transients, primitive periods other than three, or multiple length-divisible-by-three simple cycles.

## Proof
**1. Uniform firing density.** If \(U^3x=x\), let \(m_v\) be the number of times \(v\) fires during steps \(0,1,2\). Summing updates gives \(L m=0\), where \(L\) is the ordinary graph Laplacian. Connectedness forces \(m_v=m\) for every vertex, for some \(m\in\{0,1,2,3\}\). If \(m=0\), nobody fires in any of the three steps, and the initial state is fixed. If \(m=3\), everybody fires at each step, and the state is fixed. Thus primitive period three has exactly one or exactly two firings per vertex in its three-step cycle.

**2. Exact local phase multiplicity.** First assume exactly one firing per vertex. Mark its firing time by \(a_v\in\mathbb Z/3\mathbb Z\). Let
\[
r_v(a)=\#\{w\sim v:a_w=a_v-1\pmod3\}.
\]
Take the moment at which \(v\) fires and write its chip count as \(z_v\). If the numbers of its neighbors firing at its own time, at the following time, and at the preceding time are \(b_0,b_1,r_v\), respectively, then \(b_0+b_1+r_v=d_v\). Its chip values for the three successive instants are
\[
z_v,\qquad z_v-d_v+b_0,\qquad z_v-r_v.
\]
The first must be at least \(d_v\), and the latter two must lie in \([0,d_v-1]\). Those requirements are equivalent to
\[
\boxed{d_v\le z_v\le d_v+r_v(a)-1.}
\]
Indeed the last waiting inequality is the strongest upper bound, the first waiting inequality then follows from \(b_0+r_v\le d_v\), and all values are nonnegative. Since the firing phases are specified, these vertex inequalities are independent: each allowed value of \(z_v\) determines a unique initial chip value at \(v\). Therefore the number of configurations firing once per three steps is exactly
\[
Q_3(G)=\sum_{a:V(G)\to\mathbb Z/3\mathbb Z}\prod_{v\in V(G)}r_v(a).
\]
In particular there are no such configurations when no phase assignment has a predecessor-colored neighbor at every vertex.

**3. Complement symmetry.** At every vertex of a once-per-three configuration, its chip count throughout the cycle belongs to \([0,2d_v-1]\): at a waiting instant it is below \(d_v\), and at the firing instant it is at most \(d_v+r_v-1\le2d_v-1\). The transformation \(x_v\mapsto2d_v-1-x_v\) on the periodic orbit interchanges firing and waiting and commutes with the update. Conversely, each twice-per-three configuration is in the same bounded box: a firing instant either follows a waiting instant (and can gain at most \(d_v\)) or follows a firing instant (and cannot increase the chip count), so its value never exceeds \(2d_v-1\). Complementation therefore bijects the once- and twice-firing period-three configurations. Consequently \(P_3(G)=2Q_3(G)\).

**4. Functional-digraph interpretation.** Fix an arbitrary ordering of the neighbors of each vertex. For a fixed phase assignment \(a\), the integer \(z_v-d_v\in\{0,\ldots,r_v(a)-1\}\) picks, by rank, one neighbor \(p(v)\) satisfying \(a_{p(v)}=a_v-1\pmod3\). Conversely, a phase assignment and one such neighbor per vertex determine the unique chip configuration using the bounds in step 2. Orient the selected edge from \(v\) toward \(p(v)\). Every vertex has exactly one selected outgoing edge. Following an arrow decreases the phase modulo three, so each directed cycle has length divisible by three. A directed two-cycle is impossible, and any longer directed cycle is an ordinary simple undirected cycle of the graph. Every component of this directed functional graph consists of a directed cycle with directed trees feeding it.

**5. Unique resonant cycle.** Under the hypothesis there is only one permitted underlying directed cycle, namely \(C\); hence the selected arrows must include the whole of \(C\), directed consistently in one of its two orientations. Every other vertex eventually points toward \(C\), and its arrows form a forest rooted at vertices of \(C\). Such rooted forests are in bijection with spanning trees of the multigraph \(G/C\): contract the common roots, retaining the chosen individual edges. There are \(\tau(G/C)\) choices. For each orientation and forest there are exactly three phase assignments, obtained by choosing the phase of one reference vertex on \(C\); all other phases follow uniquely along the arrows. Therefore \(Q_3(G)=2\cdot3\cdot\tau(G/C)=6\tau(G/C)\), and step 3 proves the asserted factor twelve.

If no length-divisible-by-three simple cycle exists, step 4 supplies a directed-cycle obstruction, proving \(P_3(G)=0\). For a cactus, every bridge is forced into a spanning tree of \(G/C\), while from each remaining undirected cycle one may omit exactly one of its \(\ell_j\) edges. Thus \(\tau(G/C)=\prod_j\ell_j\), proving the block-product corollary.

## Verification
The proof above establishes the infinite-family statement. Two independently structured finite checks are provided:

* `check_single_resonance.py` enumerates all connected labelled simple graphs on three through six vertices, extracts **all** undirected simple cycles (not merely a cycle basis), and compares the exact phase-product count with \(12\tau(G/C)\). It verifies 4,963 graphs with exactly one resonant cycle and 3,460 graphs with none; the contracted-tree count is computed with an exact integer Laplacian determinant.
* `check_direct_chip.py` instead runs the original chip-firing update on every configuration with \(0\le x_v<2d_v\) for eight named graphs, including a cycle, a branched triangle, a triangle-plus-square, a six-cycle with a chord, a two-triangle boundary case, and a three-path theta graph. Its output confirms, among other cases, \(P_3=48\) on a triangle joined to a four-cycle at a vertex and \(P_3=36\) on the theta graph whose three path lengths are \(2,3,4\).

Replay with Python 3 and `networkx` 3.6.1 and `sympy` 1.14.0; the exact captured outputs are embedded alongside the programs. The scripts are checks of finite instances, not substitutes for the proof.

## Relationship to prior work
Dall'Asta's 2006 preprint on the one-dimensional deterministic fixed-energy sandpile gives a ring-specific periodic-block analysis, including period-three states. Jiang, Scully and Zhang's 2012 preprint studies general firing patterns and glider propagation through tree-like attachments; its conclusion explicitly presents graphs whose vertices belong to at most one cycle as a direction for further study. Jiang's 2010 preprint addresses attainable periods on complete bipartite and complete multipartite graphs. Backman's 2012 spanning-tree bijection concerns sink-based hereditary chip-firing stabilization, rather than these synchronous, sink-free immediate period-three configurations. None of the inspected primary statements gives the present unique-resonant-cycle contraction formula. These are distinctions of claims and hypotheses, not a guarantee that no equivalent unpublished or differently titled theorem exists.

## Limitations
The condition of a **unique** simple cycle of length divisible by three is essential for the stated contraction formula. With several such cycles, selected functional digraphs can have multiple directed cycles, so a single contracted-tree count does not capture the full census. For instance, two triangles meeting in a single vertex have 72 immediate primitive-three configurations, not the 12 configurations of a lone triangle. The characterization counts states already on a least-period-three orbit only; it does not count their basins or constrain all eventual periods. Priority remains subject to further full-literature inspection and independent audit.

## References
1. L. Dall'Asta, *Exact solution of the one-dimensional deterministic fixed-energy sandpile*, arXiv:cond-mat/0601267 (first posted January 12, 2006), https://arxiv.org/abs/cond-mat/0601267.
2. T.-Y. Jiang, Z. Scully and Y. X. Zhang, *Motors and impossible firing patterns in the parallel chip-firing game*, arXiv:1211.6786 (first posted November 29, 2012), https://arxiv.org/abs/1211.6786.
3. T.-Y. Jiang, *On the period lengths of the parallel chip-firing game*, arXiv:1003.0943 (first posted March 4, 2010), https://arxiv.org/abs/1003.0943.
4. S. Backman, *A bijection between the recurrent configurations of a hereditary chip-firing model and spanning trees*, arXiv:1207.6175 (first posted July 26, 2012), https://arxiv.org/abs/1207.6175.
