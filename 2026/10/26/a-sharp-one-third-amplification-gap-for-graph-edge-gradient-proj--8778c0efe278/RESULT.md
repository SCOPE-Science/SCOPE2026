# A sharp one-third amplification gap for graph edge-gradient projection

## Finding

Let \(G=(V,E)\) be any finite connected simple unweighted undirected graph with at least one edge. Give its edges arbitrary orientations, let \(B:\mathbb R^V\to\mathbb R^E\) be the signed incidence map, and let \(L=B^{\mathsf T}B\). The Euclidean orthogonal projector onto the gradient subspace is
\[
P_G=BL^\dagger B^{\mathsf T}.
\]
Its induced coordinatewise maximum norm satisfies the following sharp gap and complete boundary classification:
\[
\|P_G\|_{\infty\to\infty}=1 \quad\text{if }G\text{ is a tree};
\qquad
\|P_G\|_{\infty\to\infty}\ge\frac43 \quad\text{otherwise}.
\]
Equality at \(4/3\) holds **if and only if** every cyclic block of \(G\) is a triangle, equivalently \(G\) is a cactus whose cycles are all triangles, and at least one triangle occurs. A bridge is allowed as a two-vertex block.

More generally, for a connected unweighted cactus whose cycle lengths are \(\ell_1,\ldots,\ell_s\),
\[
\|P_G\|_{\infty\to\infty}
=\max\bigl\{1,2-2/\ell_1,\ldots,2-2/\ell_s\bigr\};
\]
for \(s=0\), this maximum is \(1\). Every bound is an attained operator norm. Thus an arbitrarily small **positive** excess over \(1\) cannot arise for an unweighted simple graph with any cycle.

## Assumptions and scope

All graphs are finite, connected, simple and unweighted. Edge signs depend on arbitrary orientations but the norm does not: reversing an edge conjugates \(P_G\) by a diagonal sign matrix. The norm is the induced norm between real edge-coordinate \(\ell^\infty\) spaces, not the Euclidean norm of \(P_G\), which is always \(1\). The same numerical bound applies to complex edge data because the matrix is real and its maximum absolute row sum determines both scalar-field operator norms. Pseudoinversion is with respect to the counting-measure Euclidean inner products; no normalization by degrees is used.

## Proof

**Step 1: electrical-flow row identity.** Fix a nonbridge edge \(e=uv\) and orient it from \(u\) to \(v\). Delete it to obtain the connected graph \(H=G-e\). Let \(h:V\to[0,1]\) be the unique voltage potential equal to \(1\) at \(u\), to \(0\) at \(v\), and harmonic at all other vertices of \(H\). The discrete maximum principle gives the indicated range. Let
\[
c=\sum_{w\sim_H u}(1-h(w))>0,\qquad
T=\sum_{ab\in E(H)}|h(a)-h(b)|.
\]
Here \(c\) is the effective conductance between \(u\) and \(v\) through \(H\); harmonicity makes the total current arriving at \(v\) also equal to \(c\). The full-graph potential \(h\) has Laplacian \(Lh=(1+c)(\mathbf1_u-\mathbf1_v)\). Hence the column \(P_G\mathbf1_e\) is the signed gradient of \(h/(1+c)\); using symmetry of \(P_G\), the absolute sum of row \(e\) is exactly
\[
S_e=\sum_{f\in E}|(P_G)_{ef}|=\frac{1+T}{1+c}.
\]
A bridge has row equal to its coordinate unit vector: any cycle-space vector vanishes on each bridge, so \(P_G\mathbf1_e=\mathbf1_e\).

**Step 2: a universal gap.** A path in \(H\) from \(u\) to \(v\) implies \(T\ge1\) by telescoping and the triangle inequality. Because the original graph is simple, no edge of \(H\) joins \(u\) directly to \(v\); consequently the sets of edges incident to \(u\) and to \(v\) are disjoint. Each has total absolute voltage drop \(c\), so \(T\ge2c\). It follows that
\[
S_e\ge\frac{1+\max\{1,2c\}}{1+c}\ge\frac43.
\]
Indeed, the right-hand expression is \(2/(1+c)\) for \(c\le1/2\), strictly decreasing to \(4/3\), and \((1+2c)/(1+c)\) for \(c\ge1/2\), strictly increasing from \(4/3\). The minimum forces \(c=1/2\) and, for equality, \(T=1=2c\). Every cyclic graph has a nonbridge edge and therefore satisfies the gap.

**Step 3: equality forces only triangular cycles.** Assume a nonbridge edge \(uv\) has \(S_e=4/3\). The equality \(T=2c\) says that every edge of \(H\) not incident to \(u\) or \(v\) has zero voltage drop. If a vertex \(w\) adjacent to \(u\), but not \(v\), had \(h(w)<1\), harmonicity at \(w\) would force the strictly negative contribution \(h(w)-h(u)\) to be canceled. But its other incident edges, being nonterminal, have zero drop: contradiction. Thus only vertices adjacent to both \(u\) and \(v\) can carry a nonzero current away from \(u\). For each such common neighbor \(w\), harmonicity forces \(h(w)=1/2\), since all edges other than \(uw\) and \(wv\) have zero drop. Consequently \(c=k/2\), where \(k\) is the number of common neighbors of \(u\) and \(v\). Since \(c=1/2\), precisely one common neighbor exists. All nonzero-current edges in \(H\) are those of its two-edge \(u\)-to-\(v\) path. Any other simple \(u\)-to-\(v\) path would need a net potential drop of one but could only use these same two current-carrying edges; thus no distinct simple path exists. In \(G\), the edge \(e\) belongs to precisely one simple cycle, a triangle.

If \(\|P_G\|_{\infty\to\infty}=4/3\), Step 2 and the maximum-row-sum definition force **each** nonbridge edge to have \(S_e=4/3\). Therefore every cycle is a triangle and no two cycles share an edge. If two different triangles shared an edge, their union would also contain a simple four-cycle, contradiction. Hence all cyclic blocks are single triangles and \(G\) is a triangular cactus.

**Step 4: converse and cactus formula.** For a cactus, choose one signed oriented cycle indicator \(z_C\) on each cycle. The cycle indicators span the cycle space \(\ker B^{\mathsf T}\) and have pairwise disjoint edge supports, hence are orthogonal. Thus the complementary projector satisfies
\[
I-P_G=\sum_C\frac{z_Cz_C^{\mathsf T}}{|C|}.
\]
Every bridge row of \(P_G\) has absolute sum \(1\). A row belonging to a cycle of length \(\ell\) has diagonal magnitude \(1-1/\ell\), exactly \(\ell-1\) other nonzero entries each of magnitude \(1/\ell\), and hence absolute sum \(2-2/\ell\). The formula and the sharp equality characterization follow. A triangle gives \(4/3\), proving the universal bound cannot be increased. In all cases a sign vector of a maximizing row realizes its absolute row sum, proving attainment.

## Verification

A standalone checker reconstructs each Euclidean edge-gradient projection from its incidence matrix and compares its maximum absolute row sum against the predicted lower gap and triangular-cactus equality condition for every non-tree connected unlabeled simple graph on three through seven vertices in the standard NetworkX graph atlas. The case counts, grouped by vertex number, are \(1,4,18,106,842\); among them the equality counts are \(1,1,4,10,30\). No discrepancy was observed at tolerance \(10^{-7}\). These finite checks support but do not replace the proof for all graph sizes.

## Relationship to prior work

The classical graph-Hodge treatment of Jiang–Lim–Yao–Ye (2008) studies the Euclidean edge-flow gradient projection in ranking problems. Kelner–Maymounkov (2009) investigates electrical routing and norms related to the graph Laplacian. Schild–Rao–Srivastava (2017) addresses averages of the edgewise \(\ell^1\) magnitudes of unit electrical flows, and Gurel-Gurevich–Nachmias–Sachdeva (2026) improves such average upper bounds. Their inspected statements do not state the pointwise **lower** \(4/3\) gap over all cyclic simple graphs or the characterization of graphs attaining it. An exact graph-family projection calculation for complete multipartite graphs, and an upper-envelope result in cycle rank two, concern narrower domains and do not imply this universal lower gap. Novelty here is restricted to the sharp universal lower gap and its complete extremal-graph classification, not to the electrical-flow formula itself.

## Limitations

Simplicity and unit conductances are essential for the proof of the numerical gap. Parallel edges, nonuniform conductances or other edge-space weightings are not covered. The theorem concerns the canonical **Euclidean** orthogonal projector; it does not prove a minimum over all possibly nonorthogonal projections. The literature comparison is bounded by discoverability of earlier computations; a mathematically equivalent unindexed historical formula remains possible. The finite graph census is nonexhaustive for arbitrarily large graphs.

## References

1. X. Jiang, L.-H. Lim, Y. Yao and Y. Ye, *Statistical ranking and combinatorial Hodge theory*, arXiv:0811.1067, first posted 2008-11-07, https://arxiv.org/abs/0811.1067.
2. J. Kelner and P. Maymounkov, *Electric routing and concurrent flow cutting*, arXiv:0909.2859, first posted 2009-09-15, https://arxiv.org/abs/0909.2859.
3. A. Schild, S. Rao and N. Srivastava, *Localization of electrical flows*, arXiv:1708.01632, first posted 2017-08-04, https://arxiv.org/abs/1708.01632.
4. O. Gurel-Gurevich, A. Nachmias and S. Sachdeva, *A tight bound on localization of electrical flows*, arXiv:2605.24130, first posted 2026-05-22, https://arxiv.org/abs/2605.24130.
