# A complete cycle-anchor invariant and geodesic formula for graph flexes

## Finding

Let \(G=(V,E)\) be any finite, connected, simple undirected graph with at least one edge. Let \(X,Y\) be two orientations. A *flex* reverses every edge incident to a vertex which is a source or a sink in the current orientation, as in Kozlov's flex complex. The following criterion completely decides whether \(X\) and \(Y\) lie in one connected component of \(\operatorname{Flex}(G)\), and gives their exact shortest-path distance.

Fix any reference direction for each undirected edge. Let \(\sigma_X\) denote the integral cycle signature, obtained by evaluating the orientation's signed \(1\)-cochain on integral cycles. If \(\sigma_X\ne\sigma_Y\), then the orientations are not flex-connected. If the signatures agree, there is a vertex function \(h:V\to\mathbb Z\), unique up to an additive constant, characterized on every arc \(u\to v\) of \(X\) by
\[
h(u)-h(v)=\begin{cases}1,&\text{if the arc is reversed in }Y,\\0,&\text{if it is unchanged in }Y.\end{cases}
\]
Let \(C_X\subseteq V\) be the set of vertices lying on at least one directed cycle in \(X\). Then \(C_X=C_Y\), and the orientations are flex-connected **if and only if** either \(C_X=\varnothing\), or \(h\) is constant on \(C_X\).

When connected, their exact distance in the \(1\)-skeleton is
\[
d_{\mathrm{flex}}(X,Y)=
\begin{cases}
\displaystyle\min_{k\in\mathbb Z}\sum_{v\in V}|h(v)-k|,&C_X=\varnothing,\\[5pt]
\displaystyle\sum_{v\in V}|h(v)-h(c)|,&C_X\ne\varnothing\quad(c\in C_X).
\end{cases}
\]
The first minimum is attained by any median of the finitely many integers \(h(v)\). A shortest sequence of legal flexes can be constructed by repeatedly flipping a source at the maximum positive potential, and then a sink at the minimum negative potential, after the indicated normalization. If either criterion fails, the flex distance is infinite.

Consequently, a complete algebraic invariant of the components is the integral cycle signature together with the *relative cycle-anchor potential*: within one signature class, compare \(h|_{C_X}\) modulo constant functions. This answers Question 2 of Kozlov's 2026 paper, and also determines exact geodesic lengths.

## Assumptions and scope

The graph is finite, connected, undirected, loopless and without multiple edges; orientations assign exactly one direction to each edge. The flex operation is legal only at a vertex with all incident edges pointing in or all pointing out. Directed cycles are ordinary directed cycles, and \(C_X\) is the union of their vertex sets. No acyclicity assumption on \(X\) or \(Y\) is imposed. The theorem concerns the \(1\)-skeleton distance of the cubical flex complex, not the metric on its geometric realization.

The signature \(\sigma_X\) is the homomorphism \(Z_1(G;\mathbb Z)\to\mathbb Z\) obtained from the orientation's \(\pm1\) signed edge cochain. Choosing another reference direction changes coordinates but not equality of two signatures. The criterion using \(h\) is independent of its arbitrary additive normalization.

## Proof

**1. Integer potential and cycle stability.** Let \(a_X\) be the signed \(1\)-cochain of \(X\) relative to fixed edge directions. The cochain \((a_X-a_Y)/2\) takes only the values \(0,1,-1\), and its integral around a cycle equals \((\sigma_X-\sigma_Y)/2\) on that cycle. Hence equality of signatures is equivalent to the vanishing of all its cycle sums. Integrating along a spanning tree produces an integral potential \(h\), unique modulo constants because \(G\) is connected, with the displayed edge-difference rule. In particular \(h(u)\ge h(v)\) along every arc \(u\to v\) of \(X\), and the decrease is at most one.

If \(u_0\to u_1\to\cdots\to u_r=u_0\) is a directed cycle of \(X\), the sum of its signed edge evaluations in \(X\) equals its length. The same signature in \(Y\) forces every edge of that cycle to retain its orientation, since each contributes at most \(1\). The converse follows symmetrically, giving \(C_X=C_Y\). Also, summing the nonnegative differences \(h(u_i)-h(u_{i+1})\) around the cycle shows that \(h\) is constant along each directed cycle, though the constants may differ between cycles.

**2. Obstruction from distinct cyclic anchors.** No vertex on a directed cycle can be a source or sink. A legal flex does not alter any edge of a directed cycle, so the set \(C_X\) remains unchanged along every flex path. Along a path of flexes, the change in the signed orientation cochain is a sum of vertex coboundaries supported at the vertices actually flexed. Each vertex in \(C_X\) is never flexed. The potential for the initial and final orientations must therefore be constant across *all* vertices in \(C_X\). This establishes the necessity of the cycle-anchor condition; invariance of the signature under a flex follows by the same coboundary calculation.

**3. Constructive sufficiency.** Suppose the signatures agree and the cycle-anchor condition holds. If \(C_X\ne\varnothing\), subtract the common value of \(h\) on \(C_X\); otherwise subtract any median of the values of \(h\). In either case the normalized potential vanishes on \(C_X\) when that set is nonempty.

If \(M=\max_v h(v)>0\), let \(U=\{v:h(v)=M\}\). Since \(h\) cannot increase along an arc of \(X\), no arc points into \(U\) from its complement. Every directed cycle inside \(U\) would lie in \(C_X\) but have potential \(M>0\), a contradiction. The induced orientation on \(U\) is therefore acyclic and has a source \(u\). With no incoming arcs from outside \(U\), this is also a source of the full orientation. Flex \(u\). The resulting orientation has a potential relative to \(Y\) equal to the old \(h\) except that its value at \(u\) decreases by one: this is checked directly on incident arcs, using that each pre-flex edge potential drop is either zero or one. The sum \(\sum_v|h(v)|\) decreases by one.

Repeat until every potential is nonpositive. If \(m=\min_v h(v)<0\), take \(W=\{v:h(v)=m\}\). No arc can leave \(W\) for its complement. As before, \(W\) contains no directed cycle, so it has an induced sink, which is a sink in the full orientation. Flexing it increases its potential by one and again reduces \(\sum_v|h(v)|\) by one. Repetition terminates with \(h\equiv0\); the edge-difference characterization then forces every arc to agree with \(Y\). This produces a legal flex path and proves sufficiency.

**4. Optimality.** A flex at one vertex changes only that vertex's potential by exactly one, after keeping the potential's additive gauge coherent along the path. Therefore any path must make at least \(|h(v)-k|\) flips at each vertex \(v\) for some common integer \(k\). In the cyclic case, no cyclic vertex is ever flexed, forcing \(k=h(c)\) on the common cyclic set. In the acyclic case, minimization over \(k\in\mathbb Z\) gives the median formula. The construction in Step 3 uses exactly that many flips, attaining the lower bound.

## Verification

The independently executable standard-library program `verify_flex.py` enumerates all orientations of eleven representative connected graphs (paths, cycles, complete and complete-bipartite graphs, a chorded cycle, two directed-cycle blocks joined by a bridge, and another bridged cyclic graph). For each ordered pair it constructs the integer potential and cycle-anchor condition, independently computes shortest flex distances by breadth-first search in the full orientation-state graph, and compares reachability and exact distances. The command `python3 verify_flex.py` completed with `VERIFY_OK graphs=11 ordered_orientation_pairs=62804`. These are finite checks of examples, not the proof for all finite graphs; Steps 1–4 provide the general argument.

## Relationship to prior work

Kozlov introduces \(\operatorname{Flex}(G)\), proves signature invariance in Proposition 7.2, exhibits a pair of orientations with equal signatures in distinct components, and explicitly asks in Question 2 for extra algebraic data completing component classification. The cycle-anchor potential supplies exactly such data and further gives a closed shortest-flex-distance formula.

Aichholzer, Cardinal, Huynh, Knauer, Mütze, Steiner and Vogtenhuber study shortest vertex flips among \(c\)-orientations. Their Theorem 10 treats acyclic \(c\)-orientations with a fixed unflippable root; §2.6 contracts directed cycles before applying that acyclic theory. Our acyclic branch is consistent with the classical flip-lattice results. Contracting cyclic strongly connected regions, however, does not preserve *individual-vertex* flex paths on the original graph: vertices lying on directed cycles cannot flex, and different anchored potentials on several cyclic regions can separate equal-signature orientations. The present criterion includes these disconnected cyclic cases without contraction, and the formula is for the original unrooted flex operation.

## Limitations

The theorem supplies a complete classification of vertices by connected component and their graph-theoretic shortest-path lengths, not a new classification of higher-dimensional cells, homotopy types, or cubical attaching maps. It does not extend directly to disconnected graphs without applying the argument componentwise. The exact integer potential assumes unchanged cycle signature; an inequality or approximate equality of signatures does not suffice.

## References

1. Dmitry N. Kozlov, *Flex complexes of graphs*, Journal of Applied and Computational Topology **10** (2026), article 10, published online 23 May 2026. DOI: 10.1007/s41468-026-00235-1. See §7, Proposition 7.2, Fig. 18, and Question 2.
2. Oswin Aichholzer, Jean Cardinal, Tony Huynh, Kolja Knauer, Torsten Mütze, Raphael Steiner, and Birgit Vogtenhuber, *Flip Distances Between Graph Orientations*, Algorithmica **83** (2021), 116–158; preprint arXiv:1902.06103. See §2.6 and Theorems 6 and 10.
3. James Propp, *Lattice structure for orientations of graphs*, arXiv:math/0209005 (2002). Foundational lattice theory for fixed-circulation orientations and distinguished-vertex flips.
