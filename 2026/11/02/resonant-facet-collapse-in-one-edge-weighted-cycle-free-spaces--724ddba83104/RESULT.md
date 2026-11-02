# Resonant facet collapse in one-edge-weighted cycle free spaces

## Finding
For every integer \(n\ge4\) and real \(t>0\), let \(M_n(t)\) have the shortest-path metric of a cycle with \(n-1\) edges of length \(1\) and one edge of length \(t\). Write \(F_n(t)\) for the number of facets of the closed unit ball of the real Lipschitz-free space \(\mathcal F(M_n(t))\). For \(0<t<n-1\), the exact formula is
\[
\begin{aligned}
F_n(t)={}&\sum_{k=0}^{n-1}\binom{n-1}{k}\mathbf 1_{\{|2k-n+1|<t\}}\\
&+2(n-1)\sum_{k=0}^{n-2}\binom{n-2}{k}\mathbf 1_{\{|2k-n+2+t|<1\}}\\
&+2\sum_{k=0}^{n-1}\binom{n-1}{k}\mathbf 1_{\{2k-n+1=t\}}.
\end{aligned}
\]
For \(t\ge n-1\), \(F_n(t)=2^{n-1}\).

The facets are **all simplicial** except at the interior resonances \(t=s\), where \(s\) is an integer, \(0<s<n-1\), and \(s\equiv n-1\pmod2\). Exactly
\[
U_n(s)=2\binom{n-1}{(n-1+s)/2}
\]
facets there are nonsimplicial, each supported by precisely \(n\) vertices. All other facets have precisely \(n-1\) vertices.

The maximal facet count in the entire one-parameter family is
\[
\max_{t>0}F_n(t)=
\begin{cases}
2(n-1)\binom{n-2}{(n-2)/2},& n\text{ even},\\
n\binom{n-1}{(n-1)/2},& n\text{ odd}.
\end{cases}
\]
For even \(n\), the maximizing parameters are exactly \(t\in(0,1)\cup(1,3)\), whereas \(F_n(1)=\binom{n}{n/2}\), smaller by a factor of \(n/2\). For odd \(n\), all and only \(0<t<2\) maximize the count. In particular, the even unweighted cycle is a genuinely nongeneric facet-count minimum relative to arbitrarily small perturbations of its distinguished edge.

## Assumptions and scope
Only real Lipschitz-free spaces, finite vertex sets, \(n\ge4\), and strictly positive weights are involved. Distances are shortest-path distances in the graph, not Euclidean chord distances. A **facet** is a maximal proper face of dimension \(n-2\) of the \((n-1)\)-dimensional primal unit ball. A facet is simplicial if it has \(n-1\) vertices. A graph edge of weight at least the sum of the complementary edges is metrically redundant. Values of \(\mathbf1_{\{P\}}\) are one when the predicate \(P\) holds and zero otherwise.

## Proof
**1. Exact dual model and distinct vertices.** Orient edges cyclically and identify a Lipschitz function modulo constants with its edge increments \(x_1,\dots,x_n\). Telescoping gives \(\sum_i x_i=0\) and the Lipschitz condition on edge increments gives \(|x_i|\le1\) for \(i<n\), \(|x_n|\le t\). This defines the dual unit ball
\[
Q_{n,t}=\bigl\{x\in\mathbb R^n:\sum_i x_i=0,\ |x_i|\le1\ (i<n),\ |x_n|\le t\bigr\}.
\]
Even when an edge is metrically redundant, the edge constraints describe the same shortest-path Lipschitz norm: bounding differences across every path edge implies the triangle bound along any path, while each such bound is implied by the actual Lipschitz norm because the edge endpoints are no farther apart than the stated weight. Therefore \(Q_{n,t}\) is isometric to the dual unit ball and vertices of \(Q_{n,t}\) are in bijection with facets of the primal unit ball.

When \(0<t<n-1\), every edge has weight strictly less than its complementary path: this is obvious for the exceptional edge, and for an ordinary edge the complementary path has length \(n-2+t>1\). Consequently every signed edge molecule is an exposed extreme point of the primal unit ball. Indeed the edge is the unique shortest path between its endpoints; a Lipschitz potential which increases strictly at slope less than the edge's maximal slope on all other edges, but at maximal slope on that edge, exposes its molecule. Equivalently the dual inequality for each edge is a genuine facet of \(Q_{n,t}\). Hence precisely \(2n\) different signed edge molecules are the primal vertices for \(t<n-1\).

**2. Exhaustive classification of dual vertices.** The coordinate hyperplane \(\sum_i x_i=0\) has dimension \(n-1\). A feasible point of \(Q_{n,t}\) is a vertex if and only if at most one coordinate satisfies its strict coordinate bound: two slack coordinates admit a nonzero small opposite perturbation preserving the hyperplane, whereas \(n-1\) tight coordinates uniquely determine the remaining coordinate. This criterion is valid even at equality and uses no genericity assumption. Count vertices by disjoint classes according to their number and location of slack coordinates.

If only the special coordinate is slack, the ordinary coordinates are \(n-1\) signs with signed sum \(2k-(n-1)\); the special coordinate is their negative. The condition \(|2k-(n-1)|<t\) gives the first sum in the formula.

If only one ordinary coordinate is slack, fix the other \(n-2\) signs and fix the exceptional coordinate to either \(t\) or \(-t\). By global sign reversal the number for both signs is twice that for exceptional coordinate \(t\). The remaining ordinary coordinate is feasible and slack precisely when \(|2k-(n-2)+t|<1\). There are \(n-1\) choices of the slack ordinary index. This gives the second sum.

If no coordinate is slack, the exceptional coordinate equals \(t\) or \(-t\), while the sum of the \(n-1\) ordinary signs cancels it. Global sign reversal produces twice the number of ordinary sign patterns with signed sum \(t\). This yields the third sum. Strict inequalities in the first two terms avoid double counting equality points. The three classes exhaust all vertices, proving the exact count.

**3. Nongeneric facets.** A primal face exposed by a dual vertex \(x\) contains exactly the signed edge molecules at which \(x\) meets their corresponding coordinate bound. For \(0<t<n-1\), these molecules are all genuine distinct primal vertices. Thus a dual vertex with one slack coordinate exposes a simplex facet with \(n-1\) vertices; a fully tight vertex exposes a facet with \(n\) vertices. Fully tight vertices exist exactly when \(t\) equals the absolute value of the sum of \(n-1\) signs, namely \(s\in\{1,3,\ldots,n-1\}\) for even \(n\), or \(s\in\{2,4,\ldots,n-1\}\) for odd \(n\). At an interior resonance the number is twice the number of \((n-1)\)-sign patterns with signed sum \(s\), namely \(2\binom{n-1}{(n-1+s)/2}\). The case \(s=n-1\) is excluded: here the exceptional edge molecule ceases to be extreme, and the dual ball becomes a full \((n-1)\)-cube with simplicial primal polar.

**4. The redundant-edge range.** When \(t\ge n-1\), the bound \(|x_n|\le t\) follows from the other coordinate bounds and the zero-sum relation. Hence \(Q_{n,t}\) is linearly isometric to the \((n-1)\)-cube, with exactly \(2^{n-1}\) vertices. Its polar is a crosspolytope, with only simplicial facets.

**5. Global maximum and exact parameter ranges.** For even \(n=2h+2\) with \(h\ge1\), the sign sum of the ordinary \(2h+1\) coordinates is odd. On the open chamber \(\max(0,2j-1)<t<2j+1\), \(0\le j\le h\), direct evaluation of the three counting terms gives
\[
G_j=2\sum_{r=1}^{j}\binom{2h+1}{h+r}
+2(2h+1)\binom{2h}{h-j}.
\]
The binomial identities \(\binom{2h}{h-j-1}/\binom{2h}{h-j}=(h-j)/(h+j+1)\) and \(\binom{2h+1}{h+j+1}=(2h+1)\binom{2h}{h-j}/(h+j+1)\) give
\[
G_{j+1}-G_j=-\frac{4j(2h+1)}{h+j+1}\binom{2h}{h-j}
\quad(0\le j<h).
\]
Thus \(G_0=G_1\) and subsequent open chambers strictly decrease. At each interior odd integer \(t=2j+1\), the exact count is
\[
F_n(2j+1)=2\sum_{r=1}^{j+1}\binom{2h+1}{h+r},
\]
strictly below \(G_j\) and, when \(j<h\), also below or equal to \(G_0\); this excludes the resonances as global maximizers. At \(t\ge n-1\), the cube count \(2^{n-1}\) is strictly smaller than \(G_0\). Therefore the maximum is \(G_0=2(n-1)\binom{n-2}{(n-2)/2}\), attained exactly in the two stated open intervals. At \(t=1\), the displayed resonant formula simplifies via Pascal's identity to \(\binom{n}{n/2}\), and their ratio is \(n/2\).

For odd \(n=2h+1\) with \(h\ge2\), the ordinary sign sum is even. For \(2j<t<2j+2\), \(0\le j<h\), direct counting gives
\[
H_j=\binom{2h}{h}+2\sum_{r=1}^{j}\binom{2h}{h+r}
+4h\binom{2h-1}{h-1-j}.
\]
Similarly,
\[
H_{j+1}-H_j=-\frac{4h(2j+1)}{h+j+1}\binom{2h-1}{h-1-j}<0
\quad (0\le j<h-1).
\]
At each interior even integer \(t=2j\) the count is \(\binom{2h}{h}+2\sum_{r=1}^{j}\binom{2h}{h+r}\), strictly below \(H_0\). In the redundant-edge range the cube count \(2^{2h}\) is also below \(H_0\). Thus the maximum is \(H_0=(2h+1)\binom{2h}{h}\) attained exactly for \(0<t<2\). This completes the dimension-uniform proof.

## Verification
A standalone Python 3 script, `verify.py`, computes vertices by independently fixing all but one coordinate to signs, solving the zero-sum equation in exact rational arithmetic, deduplicating, and counting fully tight vertices. It compares these counts with the formula and the chamber formulas over \(408\) positive rational parameter/dimension cases for \(4\le n\le11\) and checks the stated maxima. The reproduced output is `VERIFY_OK exact_rational_grid_cases=408 dimensions=4..11; independent vertex enumeration, sign-count formula, closed binomial formula, maxima`. This finite check is corroboration; arbitrary real parameters and all dimensions follow from the proof above.

## Relationship to prior work
Jevtić, Timotijević and Živaljević (2018, arXiv:1812.00397v1) identify the combinatorial type of weighted-cycle Kantorovich–Rubinstein polytopes with a Bier-sphere boundary **under a genericity hypothesis**: no subset of edge lengths has exactly half the perimeter. Their generic classification covers, at least implicitly, the open-chamber combinatorics. It does not settle the fully tight vertices, nonsimplicial facet sizes, and exact exceptional-wall counts investigated here, precisely because the resonant parameters violate that hypothesis. The open-chamber formulas above are included to quantify the degeneration, not asserted as independent generic-combinatorics discoveries.

Braun and Bruegge (2022, arXiv:2201.13303v1) calculate facet counts for unweighted cycle symmetric-edge polytopes. At \(t=1\), these give \(\binom n{n/2}\) for even \(n\) and \(n\binom{n-1}{(n-1)/2}\) for odd \(n\). Their extremal unweighted unicyclic graph results concern a different admissible class: adding a pendant edge can attain the generic maximum for an even cycle, but does not by itself determine how the fixed cycle degenerates at an interior weighted resonance. D'Alì, Delucchi and Michałek (2019, arXiv:1910.05193v1) study face structure of symmetric-edge polytopes for graph metrics; their unweighted results do not give the continuously weighted wall classification. A published weighted-cycle numerical-index rigidity result analyzes the same cube hyperplane in another invariant, and its 'one slack coordinate' observation is used here only as an elementary starting point: it gives no explicit resonance multiplicities or primal facet sizes.

## Limitations
The count is for facets of the real Lipschitz-free unit ball over a finite shortest-path vertex metric, not for facets of the continuous geometric cycle, arbitrary positive weight vectors, or faces of all dimensions. The substantive proposed contribution lies at the nongeneric walls and the exact all-parameter phase diagram; generic weighted-cycle combinatorics and unweighted endpoint counts have direct precursors in the cited papers. A complete bibliographic exclusion of unpublished or unindexed descriptions of nongeneric weighted-cycle KR polytopes has not been established; independent originality assessment remains necessary.

## References
1. F. D. Jevtić, M. Timotijević, R. T. Živaljević, *Polytopal Bier spheres and Kantorovich-Rubinstein polytopes of weighted cycles*, arXiv:1812.00397v1 (first public 2018-12-02), https://arxiv.org/abs/1812.00397. Relevant: genericity hypothesis and weighted-cycle KR-polytope boundary classification, particularly Section 4.
2. B. Braun, K. Bruegge, *Facets of Symmetric Edge Polytopes for Graphs with Few Edges*, arXiv:2201.13303v1 (first public 2022-01-31), https://arxiv.org/abs/2201.13303. Relevant: Lemma 2.5 (cycle facets) and Theorem 3.2 (unicyclic maximum).
3. A. D'Alì, E. Delucchi, M. Michałek, *Many faces of symmetric edge polytopes*, arXiv:1910.05193v1 (first public 2019-10-11), https://arxiv.org/abs/1910.05193. Relevant: weighted versus unweighted graph metric context.
4. *Numerical-index-one rigidity for weighted cycles and positive cube sections* (2026), publicly accessible result at https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-numerical-index-one-rigidity-for-weighted-cycles-and-positive-cu--aa457cec74ea. Relevant: exact weighted cycle norm model but distinct numerical-index statement.
