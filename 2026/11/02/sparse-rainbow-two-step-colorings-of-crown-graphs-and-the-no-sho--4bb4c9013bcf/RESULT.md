# Sparse rainbow two-step colorings of crown graphs and the no-short-cycle permutation law

## Finding

Let \(\operatorname{Cr}_n\) be the labelled crown graph with vertex classes \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\), where \(a_i b_j\) is an edge exactly when \(i\ne j\). Let red and blue be two **named** edge colors. Call such a coloring *distance-two rainbow-complete* when each unordered pair of graph vertices at distance exactly two is connected by a two-edge path with one red and one blue edge. Define \(\rho_n\) as the minimum possible number of red edges, and \(N_n\) as the number of labelled colorings achieving it.

**Theorem.** For every \(n\ge4\),
\[
\boxed{\rho_n=n-1,\qquad N_n=n\,a_{n-1}},
\]
where \(a_m\) counts permutations of \(m\) labelled elements with **every cycle of length at least three**. The red edges of every optimal coloring form a matching of size \(n-1\) omitting precisely the two vertices \(a_s,b_s\) for a unique index \(s\). After excluding index \(s\), the red matching is the permutation graph of a permutation having no fixed point or two-cycle; conversely every such matching is optimal. Its exponential generating function is
\[
\boxed{\sum_{m\ge0}a_m\frac{z^m}{m!}=\frac{\exp(-z-z^2/2)}{1-z}}.
\]
At the boundary \(n=3\), \(\rho_3=3\) and \(N_3=2\): the two colorings alternate red and blue around the six-cycle. The minimum-red counts for \(n=3,4,5,6,7,8\) are \(2,8,30,144,1120,9120\), respectively.

Every two-coloring necessarily leaves the \(n\) nonadjacent pairs \(\{a_i,b_i\}\) without a rainbow path, because they are at distance three. The colorings above connect *every other vertex pair* by a rainbow path (an edge for adjacent vertices; a rainbow two-edge path for distance-two pairs), so this is an optimal partial rainbow-connection statement, **not** a claim that \(\operatorname{Cr}_n\) has rainbow connection number two.

## Assumptions and scope

Graphs are finite, simple, undirected, and vertex-labelled. The integer \(n\) satisfies \(n\ge3\). The two edge colors are distinguished; they need not form a proper edge-coloring. The phrase distance-two rainbow-complete imposes a condition only on pairs of graph distance two. It does not demand an impossible two-color rainbow path between missing matching partners at distance three. The quantity minimized is the number of edges assigned the *specific* color red, not the number of colors or the total number of edges.

## Proof

**1. Characterization of pairs.** For every \(n\ge3\), two vertices in the same part, such as \(a_i,a_j\) with \(i\ne j\), lie at distance two, and their possible intermediates are exactly the \(b_k\) with \(k\notin\{i,j\}\). Similarly the intermediates of \(b_i,b_j\) are the \(a_k\) for \(k\notin\{i,j\}\). Distinct partners \(a_i,b_i\) are at distance three. Thus the imposed property means that each two different rows and each two different columns of the off-diagonal \(n\)-by-\(n\) red-incidence matrix differ in some position outside their two corresponding diagonal indices.

**2. Sharp lower bound.** If two vertices of the same part are incident with no red edges, then every two-edge path between them is all blue. Thus at most one vertex of each of \(A\) and \(B\) can have red degree zero. At least \(n-1\) vertices of \(A\) must have a red incident edge, whence every valid coloring has at least \(n-1\) red edges.

**3. Equality forces a matching and the same omitted index.** Suppose exactly \(n-1\) red edges occur. The preceding lower bound forces them to be incident with exactly \(n-1\) distinct vertices on each side; hence they form a matching. Write \(a_s\) for the unique red-isolated vertex on the left and \(b_t\) for the unique red-isolated vertex on the right. If \(s\ne t\), vertex \(b_s\) belongs to a red matching edge \(a_i b_s\) for some \(i\ne s\). Every two-edge path from \(a_s\) to \(a_i\) uses a middle vertex \(b_k\) with \(k\notin\{s,i\}\), so it avoids the sole red edge incident with \(a_i\) and has no red edge incident with \(a_s\). This violates the distance-two rainbow condition. Therefore \(t=s\).

**4. No-short-cycle characterization.** The red matching now defines a permutation \(\pi\) of \(\{1,\ldots,n\}\setminus\{s\}\): its edges are exactly \(a_i b_{\pi(i)}\). Every red edge belongs to the crown graph, so \(\pi(i)\ne i\). For distinct remaining indices \(i,j\), the only places where rows \(i,j\) can differ from blue are columns \(\pi(i),\pi(j)\). The pair \(a_i,a_j\) fails if and only if both these columns are unavailable intermediates, i.e. precisely when \(\pi(i)=j\) and \(\pi(j)=i\). Rows involving the omitted index \(s\) always work: the unique red neighbor of any other row is not on diagonal \(s\), since column \(s\) is also red-isolated, and not on that row's diagonal. The argument for two right-part vertices is identical for the inverse permutation \(\pi^{-1}\), which has a two-cycle exactly when \(\pi\) does. Therefore the coloring is valid exactly when all cycles of \(\pi\) have length at least three. For \(n\ge4\), such permutations exist (a single cycle of length \(n-1\)), proving equality in the lower bound and the promised exhaustive classification.

**5. Exact enumeration.** There are \(n\) choices for \(s\) and, independently, \(a_{n-1}\) choices for \(\pi\); distinct choices give distinct red sets and hence distinct named colorings. The exponential formula for labelled permutations gives
\[
\sum_{m\ge0}a_m\frac{z^m}{m!}
=\exp\!\left(\sum_{j\ge3}\frac{z^j}{j}\right)
=\frac{e^{-z-z^2/2}}{1-z}.
\]
Equivalently, \(a_0=1\), \(a_1=a_2=0\), and for each \(m\ge1\), by considering the length \(j\) of the cycle containing the least label,
\[
a_m=\sum_{j=3}^{m}\frac{(m-1)!}{(m-j)!}\,a_{m-j}.
\]
This gives the stated counts.

**6. Small case.** The crown \(\operatorname{Cr}_3\) is the six-cycle. Every graph-distance-two pair has exactly one common neighbor; therefore the two edges at every vertex must have different colors. A two-coloring of an even cycle is alternating if and only if this holds. The six-cycle has exactly two alternating named colorings, each with three red edges; thus \(\rho_3=3\), \(N_3=2\).

## Verification

Run the supplied standard-library script with `python3 verify.py`. It independently reconstructs the original graph and checks all unordered vertex pairs of graph distance two by searching for red-blue geodesics. Exhaustive searches over all colorings at successive red cardinalities establish, for \(n=3,4,5\), that the minimum layers are exactly the predicted sets. The script then checks every predicted optimum for \(n=6,7,8\), verifies their counts, and independently counts no-short-cycle permutations through seven elements. Expected final line: `VERIFY_OK`. Finite tests are corroboration, not a proof for unbounded \(n\).

## Relationship to prior work

Barát, Boyadzhiyska and Freschi (2026, arXiv:2609.11437v1) study two-edge-color rainbow connectivity near the Dirac minimum-degree threshold, including an asymptotic theorem allowing a vanishing proportion of unsuccessfully connected pairs. Their sufficient hypotheses concern graphs of minimum degree at least half their order (or very near that bound), whereas the crown graph on \(2n\) vertices has minimum degree \(n-1\) and diameter three. Their results do not determine the smallest size of a distinguished color class for connecting every *reachable* distance-two pair, or enumerate its extremal colorings. The classical interpretation of a crown as \(K_{n,n}\) with a perfect matching deleted is standard; neither the graph definition nor the rainbow-geodesic definition is new. The new aspect here is the exact sparse-color optimum and its cycle-cover classification, not any claim about the standard rainbow connection number.

## Limitations

The theorem concerns two named colors, graph-distance-two pairs, and crown graphs only. It does not give a full two-color rainbow connection of any crown graph, because its missing matched pairs have distance three. It does not give the count of nonoptimal colorings, the three-color strong rainbow connection number, or analogous sparsity formulas on arbitrary bipartite graphs. The priority comparison is necessarily limited to the accessible cited literature and available mathematical-record searches; unindexed equivalents may exist. Independent mathematical validation has not been performed.

## References

1. J. Barát, S. Boyadzhiyska and A. Freschi, *Rainbow connecting 2-colorings of super-Dirac graphs*, arXiv:2609.11437v1, first submitted 10 September 2026, https://arxiv.org/pdf/2609.11437v1.
2. E. W. Weisstein, *Crown Graph*, MathWorld, https://mathworld.wolfram.com/CrownGraph.html (standard graph definition).
3. G. Chartrand, G. L. Johns, K. A. McKeon and P. Zhang, *Rainbow connection in graphs*, Mathematica Bohemica 133 (2008), 85–98 (classical rainbow-connection terminology).
