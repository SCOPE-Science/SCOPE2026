# Optimal edge-failure monitors and token jumping on four-edge theta networks

## Finding

**Theorem.** Let \(r\ge 3\) be an integer. Form \(\Theta_{r,4}\) from \(r\) internally disjoint paths \(u-a_i-c_i-b_i-v\), each of length four and sharing precisely their endpoints \(u,v\), with \(i\in[r]\). Then

\[
\operatorname{meg}(\Theta_{r,4})=r+1.
\]

Every minimum monitoring edge-geodetic (MEG) set is exactly one of the following, where \(B,A\) are nonempty subsets of \([r]\):

\[
\begin{aligned}
U(B)&=\{u\}\cup\{b_i:i\in B\}\cup\{c_i:i\notin B\},\\
V(A)&=\{v\}\cup\{a_i:i\in A\}\cup\{c_i:i\notin A\},\\
W_i&=\{a_i,b_i\}\cup\{c_j:j\ne i\}\qquad(i\in[r]).
\end{aligned}
\]

The three families are disjoint, so exactly \(2^{r+1}+r-2\) minimum MEG-sets exist.

Let \(\mathcal R_r\) be their **token-jumping reconfiguration graph**: two minimum sets are adjacent if one selected vertex can be replaced by one unselected vertex. Then \(\mathcal R_r\) consists of two copies of \(Q_r-\{0^r\}\), indexed respectively by \(U(B)\) and \(V(A)\) for nonempty bitmasks, with \(r\) internally disjoint length-two links \(U(\{i\})-W_i-V(\{i\})\). In particular,

\[
|V(\mathcal R_r)|=2^{r+1}+r-2,\qquad
|E(\mathcal R_r)|=r2^r,\qquad
\operatorname{diam}(\mathcal R_r)=2r.
\]

The network of optimum solutions is connected. Every \(U\)- or \(V\)-type solution has reconfiguration degree \(r\); each \(W\)-type solution has degree \(2\).

## Assumptions and scope

All graphs are finite, simple, undirected, and unweighted; all distances are shortest-path edge counts. Two distinct selected vertices \(x,y\) **monitor** an edge \(e\) when every shortest \(x\)-\(y\) path traverses \(e\), equivalently \(d_{G-e}(x,y)>d_G(x,y)\). A vertex subset is a monitoring edge-geodetic set if each edge has such a selected witness pair. Its minimum possible size is \(\operatorname{meg}(G)\).

The theorem concerns precisely \(r\ge3\) and arm length four, or equivalently the graph obtained by subdividing once each edge of \(K_{2,r}\). It makes no claim about unequal-length arms, arm lengths other than four, or unrestricted two-terminal series-parallel graphs.

## Proof

**1. Each arm must contain an internal probe.** Suppose a selected pair has no endpoint among \(a_i,c_i,b_i\), but a shortest path between the selected vertices traverses an edge on arm \(i\). Such a simple path must traverse the entire \(u\)-\(v\) arm. Since at least one other equal-length \(u\)-\(v\) arm exists, replacing the arm segment produces a second shortest path avoiding the edge. Thus neither endpoint-outside pair can monitor any edge of arm \(i\). Every MEG-set therefore contains at least one vertex from each of the \(r\) arm interiors.

**2. Cross-arm shortest paths.** Place coordinate \(1\) at \(a_i\), \(2\) at \(c_i\), and \(3\) at \(b_i\), measured from \(u\). For internal vertices on distinct arms at positions \(p,q\), the route through \(u\) has length \(p+q\), and the route through \(v\) has length \(8-p-q\). The \(u\)-route is the unique geodesic if \(p+q<4\), the \(v\)-route is unique if \(p+q>4\), and at equality both are shortest. Since the only intersections between arms are the two terminals, no other route can be shorter.

Consequently, if an arm has just one selected internal vertex and neither terminal is selected, that vertex must be \(c_i\). Indeed, a unique \(a_i\) could not monitor its distal edge \(b_i v\): outside internal endpoints lie at \(q\le3\), so \(1+q\le4\), ruling out a unique route through \(v\). Similarly, a unique \(b_i\) cannot monitor \(u a_i\), since \(3+q\ge4\) rules out a unique route through \(u\). Pairs of selected vertices on other arms cannot monitor the edge by Step 1.

**3. Sharp lower bound.** If an MEG-set had size \(r\), Step 1 would force exactly one selected internal vertex on each arm and no terminals. Step 2 forces all those vertices to be the \(c_i\). Yet for distinct \(i,j\), both the \(u\)-route and the \(v\)-route from \(c_i\) to \(c_j\) have length four, and no arm edges are common to all these geodesics. Thus no edge is monitored. Therefore every MEG-set has at least \(r+1\) vertices.

**4. Classification at equality.** Let \(|S|=r+1\). There cannot be two selected terminals because then only \(r-1\) internal selections remain. If \(u\) is selected, exactly one internal vertex is selected per arm. The distal edge \(b_i v\) rules out \(a_i\), so choices are \(b_i\) and \(c_i\). At least one \(b_i\) is needed: if all selections are \(c_i\), each selected pair either uses \(u\) and monitors only proximal edges, or joins two centers with tied geodesics. Conversely, any nonempty collection of \(b_i\) makes \(U(B)\) feasible: the pairs \((u,b_i)\) or \((u,c_i)\) cover each arm's proximal portion; for every remaining distal portion, pair its selected internal vertex with a chosen \(b_j\) on another arm. These cross-arm pairs have coordinate sum exceeding four, so their unique shortest path runs through \(v\). For an arm whose selected vertex is itself \(b_j\), choose any other selected internal vertex; its coordinate is at least two, again yielding the unique \(v\)-route. The symmetric argument with \(u,v\) interchanged gives exactly the sets \(V(A)\).

If neither terminal is selected, exactly one arm, say \(i\), has two selected internal vertices and every other arm has exactly one. The singleton vertices are forced to be \(c_j\) by Step 2. To monitor both \(u a_j\) and \(b_j v\) on each singleton-center arm, selected internal witnesses on the doubled arm must have coordinate one and coordinate three, respectively: only these yield strict \(u\)- and \(v\)-routes from position two. Thus the doubled arm selects exactly \(a_i,b_i\). Such a set \(W_i\) is feasible: \((a_i,b_i)\) monitors its arm's two middle edges, while every \((a_i,c_j)\) and \((b_i,c_j)\), with \(j\ne i\), has respectively a unique \(u\)- and \(v\)-route, covering all remaining edges including the doubled arm's outer edges. This completes the classification, verifies attainability, and gives \((2^r-1)+(2^r-1)+r=2^{r+1}+r-2\).

**5. Token jumps.** Two different \(U\)-type solutions differ by one selected vertex precisely when their nonempty index sets differ in one bit, and the analogous statement holds for \(V\)-type solutions. An \(U\)-type solution and a \(V\)-type solution differ in at least three vertices and cannot be directly adjacent. Each \(W_i\) is adjacent exactly to \(U(\{i\})\) and \(V(\{i\})\); there are no \(W_i\)-\(W_j\) edges. This is the claimed two-cubes-plus-links graph. A punctured hypercube has \(r2^{r-1}-r\) edges, so the edge total is \(2(r2^{r-1}-r)+2r=r2^r\); the degree claims follow directly.

The punctured hypercube is isometric in \(Q_r\): a shortest Hamming path between nonzero subsets can add an element of the target before removing the last element of the source, and otherwise flips differing bits in any order. Thus within each copy the distance is Hamming distance at most \(r\). Between \(U(A)\) and \(V(B)\), choose a bridge indexed by \(i\). If \(A\cap B\ne\varnothing\), choosing \(i\) there gives length \((|A|-1)+2+(|B|-1)=|A|+|B|\le2r\). If \(A\cap B=\varnothing\), choose \(i\in A\), giving length \((|A|-1)+2+(|B|+1)=|A|+|B|+2\le r+2\le2r\). A \(W_i\) is within \(r+1\) steps of every cube vertex, and any two distinct \(W_i,W_j\) are at distance at most four, so every pair is at distance at most \(2r\).

Conversely, any path from \(U([r])\) to \(V([r])\) must first reach a singleton \(U(\{i\})\), requiring at least \(r-1\) cube flips, then cross at least two bridging edges, and finally leave a singleton \(V(\{j\})\) and make at least \(r-1\) cube flips. Even a path using multiple bridges cannot be shorter. The distance is at least \(2r\), proving the diameter formula and connectivity.

## Verification

The companion program `verify.py` independently constructs every \(\Theta_{r,4}\) for \(3\le r\le7\), computes all-pairs graph distances both before and after each individual edge deletion, and tests every vertex subset of sizes \(r\) and \(r+1\). It compares the complete optimal-set collection to the three predicted families, constructs token-jumping adjacency from symmetric differences, and checks the graph structure, degree distribution, edge count, connectivity, and diameter. The run examined exactly 873813 candidate vertex subsets and passed every test. Execute `python3 verify.py` from the directory holding the checker. The reproducible recorded output is `verification_output.txt`.

## Relationship to prior work

Dev, Dey, Foucaud, Krishna, and Ramasubramony Sulochana introduced monitoring edge-geodetic sets and exact values for several basic families [1]. Haslegrave studied computational hardness and Cartesian/strong graph products [2]. Foucaud and collaborators studied general extremal bounds, optimal-vertex conditions, clique sums, and edge subdivisions [3], but their general subdivision comparison applies after at least two subdivisions per edge, whereas \(\Theta_{r,4}\) is the *once*-subdivided \(K_{2,r}\). Subsequent graph-class characterizations [4] and cyclomatic-number bounds [5] do not determine these minimum sets or their reconfiguration graph. The present result concerns the exact equality cases and single-token transitions for this fixed, natural parallel-path family, not a rephrasing of the general inequalities.

The related but different notions of ordinary edge-geodetic sets, strong edge-geodetic sets, distance-edge-monitoring sets (one selected endpoint suffices), and edge-general-position sets must not be substituted for the two-selected-endpoint MEG condition. Their numerical results alone cannot imply the optimal-set classification above.

## Limitations

The theorem is restricted to equal paths of length four and \(r\ge3\). The standalone finite verifier covers \(3\le r\le7\) only; the proof, not the enumeration, establishes all larger values. We do not determine distances under more restrictive reconfiguration moves, such as token sliding. A comprehensive guarantee that equivalent results do not appear in unindexed or inaccessible literature is unavailable. Independent validation has not been performed.

## References

1. S. R. Dev, S. Dey, F. Foucaud, N. Krishna, and L. Ramasubramony Sulochana, *Monitoring edge-geodetic sets in graphs*, arXiv:2210.03774, first posted 7 October 2022. https://arxiv.org/abs/2210.03774
2. J. Haslegrave, *Monitoring edge-geodetic sets: Hardness and graph products*, arXiv:2210.08955, 2022. https://arxiv.org/abs/2210.08955
3. F. Foucaud et al., *Bounds and extremal graphs for monitoring edge-geodetic sets in graphs*, arXiv:2403.09122, first posted 14 March 2024. https://arxiv.org/abs/2403.09122
4. F. Foucaud, N. Pandey, and S. Paul, *Characterizing optimal monitoring edge-geodetic sets for some structured graph classes*, arXiv:2503.06086, 2025. https://arxiv.org/abs/2503.06086
5. A. Chakraborty, F. Foucaud, and T. Hakanen, *Distance-based (and path-based) covering problems for graphs of given cyclomatic number*, arXiv:2509.00383, 2025. https://arxiv.org/abs/2509.00383
