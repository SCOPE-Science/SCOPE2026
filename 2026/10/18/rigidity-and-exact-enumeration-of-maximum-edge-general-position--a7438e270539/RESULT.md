# Rigidity and exact enumeration of maximum edge-general-position sets in equal-arm theta graphs

## Finding

**Theorem.** Let \(m\ge3\) and \(L\ge2\) be integers. Write \(\Theta_{m,L}\) for the simple graph formed by \(m\) internally vertex-disjoint paths of length \(L\) with common distinct endpoints \(s,t\). Number the edges on arm \(i\) by \(1,2,\ldots,L\), starting at \(s\). Then
\[
\operatorname{gp}_e(\Theta_{m,L})=2m.
\]
Every maximum edge-general-position set is, for a **unique** integer \(a\) with \(1\le a\le\lfloor L/2\rfloor\), exactly the \(2m\) edges in positions \(a\) and \(L+1-a\) on *every* arm. Thus the number of maximum sets on the given labeled edge set is
\[
N_{\max}(\Theta_{m,L})=\lfloor L/2\rfloor,
\]
independent of the number of arms.

## Assumptions and scope

All graphs are finite, undirected and simple. The arms have mutually disjoint internal vertices. An **edge-general-position set** \(S\subseteq E(G)\) is an edge subset satisfying \(|S\cap E(Q)|\le2\) for **every** shortest vertex-to-vertex path (geodesic) \(Q\) in \(G\). The number \(\operatorname{gp}_e(G)\) is the maximum cardinality of such an \(S\). The count \(N_{\max}\) distinguishes subsets of the *labeled* edges; it is not a count of automorphism orbits.

The two endpoint vertices may be named \(s,t\) arbitrarily: reversing the names sends \(a\) to \(L+1-a\), but the unordered pair of selected levels does not change. We require \(m\ge3\) for the uniqueness implication; for two arms the graph is an ordinary cycle, so the stated rigidity characterization need not hold. The lower bound \(L\ge2\) ensures the graph is simple for arbitrary \(m\).

## Proof

**1. Sharp upper bound.** Each of the \(m\) specified \(s\)-to-\(t\) arms is a geodesic of length \(L\), because every simple \(s\)-to-\(t\) path is one complete arm. Hence every edge-general-position set meets each arm in at most two edges. As the arms partition the edge set, \(|S|\le2m\).

**2. Existence.** Fix any integer \(a\) with \(1\le a\le\lfloor L/2\rfloor\), set \(b=L+1-a\) (so \(a<b\)), and select positions \(a,b\) in every arm. Any geodesic whose endpoints lie on one arm has at most two chosen edges: except when the endpoints are \(s,t\), its unique geodesic is the direct subpath of that arm; for \(s,t\), each geodesic is a complete arm.

Now take internal vertices on distinct arms \(i,j\) at distances \(x,y\) from \(s\), respectively. Every geodesic between them goes via \(s\), of length \(x+y\), or via \(t\), of length \(2L-x-y\). The first route is geodesic only if \(x+y\le L\), and the second only if \(x+y\ge L\); both may be geodesics when equality holds. No path traversing a third complete arm can be shorter.

A route via \(s\) containing at least three selected edges must contain both chosen edges from one arm's initial segment and at least one from the other initial segment. Therefore its endpoint coordinates satisfy \(x\ge b\) and \(y\ge a\), up to swapping the arms, so \(x+y\ge a+b=L+1\): it cannot be a geodesic via \(s\). Similarly, a route via \(t\) containing at least three selected edges must include both chosen edges in one terminal suffix and at least one from the other suffix, forcing \(x\le a-1\) and \(y\le b-1\), up to swapping; hence \(x+y\le a+b-2=L-1\): it cannot be a geodesic via \(t\). Pairs with an endpoint equal to \(s\) or \(t\) reduce to one arm or to two prefixes/suffixes; any potentially violating two-arm route is handled by the same inequalities. Thus the selected set is edge-general-position and has \(2m\) edges, matching the upper bound.

**3. Necessity and rigidity.** Let \(S\) be any edge-general-position set of cardinality \(2m\). Sharpness of the armwise upper bound forces precisely two selected positions \(1\le a_i<b_i\le L\) on each arm \(i\).

For distinct arms \(i,j\), we claim
\[
b_i+a_j\ge L+1.
\]
Otherwise, with internal endpoints at respective coordinates \(x=b_i\) on arm \(i\) and \(y=a_j\) on arm \(j\), the route through \(s\) has length \(x+y\le L\) and is geodesic. It contains the selected edges \(a_i,b_i\) on arm \(i\) and the selected edge \(a_j\) on arm \(j\), a forbidden triple. (The assumed inequality ensures these endpoints really are internal.)

We also claim, for distinct arms \(i,j\), that
\[
a_i+b_j\le L+1.
\]
Otherwise \(a_i+b_j\ge L+2\); take internal endpoints at \(x=a_i-1\) on arm \(i\) and \(y=b_j-1\) on arm \(j\). Their route through \(t\) has length \(2L-x-y\le x+y\), hence is geodesic. Its terminal suffix on arm \(i\) includes both selected edges \(a_i,b_i\), and its suffix on arm \(j\) includes \(b_j\), again a forbidden triple.

Apply the first inequality with the ordered indices \(j,i\) and the second with \(i,j\). Their common left-hand side gives
\[
a_i+b_j=L+1\qquad\text{whenever }i\ne j.
\]
Because \(m\ge3\), for any arms \(i,j\) we can choose a third arm \(k\). Then \(a_i+b_k=a_j+b_k\), so every \(a_i\) has the same value \(a\). The displayed equality then forces all \(b_j\) to equal \(b=L+1-a\). Since \(a<b\), necessarily \(1\le a\le\lfloor L/2\rfloor\). This is exactly the previously constructed form.

**4. Enumeration.** Each allowable value of \(a\) produces a different labeled edge subset (its least selected position is \(a\)), and step 3 proves no other maximum subset exists. There are \(\lfloor L/2\rfloor\) such values. \(\square\)

## Verification

The included standalone standard-library Python program `theta_verify.py` constructs equal-arm theta graphs, enumerates all vertex-pair geodesics by breadth-first distances and predecessor backtracking, and tests the forbidden-three-edge condition as bit masks. It exhaustively enumerates *all* edge subsets of cardinality \(2m\) on six small graphs; independently enumerates every two-edges-per-arm candidate on thirteen parameter pairs; and checks every predicted construction on further parameters through \(m=7\), \(L=12\). The program prints the exact number of checked cases. The all-parameter conclusion is supplied by the proof above, not by finite testing.

Reproduce with `python3 theta_verify.py` (Python standard library only).

## Relationship to prior work

The invariant was introduced by Manuel, Prabha, and Klavžar, whose 2021 preprint gives exact results for trees, rectangular grids, and hypercubes [1]. The later generalization of Manuel, Prabha, and Klavžar proves a geodesic-cover upper bound; taking the \(m\) arms as an edge-geodesic cover recovers the upper estimate \(2m\) but neither supplies a realization nor classifies the extremizers [2]. Tian, Klavžar, and Tan analyze extremal small edge-general-position numbers and block graphs, not parallel-path theta graphs with \(m\ge3\) [3]. Cao, Ji, and Wang use three-path theta subgraphs to show that noncactus graphs cannot have edge-general-position number four; their theorem classifies graphs with the number equal to four, not the present \(2m\ge6\) or the maximum-set counts [4]. Their construction of five selected edges is weaker than the exact value here and does not imply rigidity.

The distinguishing contribution is the *complete* structure of all optimal sets and a count independent of the number of arms. Literature searches and full-text comparisons described in the accompanying review did not identify an equivalent theta-graph theorem; that observation is not a uniqueness certificate.

## Limitations

The rigidity assertion uses at least three internally disjoint arms of **equal lengths**. It is not asserted for two-arm cycles, unequal lengths, parallel-edge multigraphs, nonoptimal sets, or other edge-geodesic invariants. The proof is mathematical rather than formally mechanically certified. No independent scientific review is claimed, and unindexed or inaccessible equivalent literature remains a possible originality risk.

## References

[1] P. Manuel, R. Prabha, and S. Klavžar, *Edge general position problem*, arXiv:2105.04292 (first public version 10 May 2021); subsequently published in *Bulletin of the Malaysian Mathematical Sciences Society* 45 (2022), 2997–3009. https://arxiv.org/abs/2105.04292

[2] P. Manuel, R. Prabha, and S. Klavžar, *Generalization of edge general position problem*, arXiv:2207.07357 (15 July 2022); *The Art of Discrete and Applied Mathematics* 8 (2025), DOI:10.26493/2590-9770.1745.5f4. https://arxiv.org/abs/2207.07357

[3] J. Tian, S. Klavžar, and E. Tan, *Extremal Edge General Position Sets in Some Graphs*, arXiv:2302.01587; *Graphs and Combinatorics* 40 (2024), article 40, DOI:10.1007/s00373-024-02770-z. https://link.springer.com/article/10.1007/s00373-024-02770-z

[4] Y. Cao, S. Ji, and L. Wang, *The Edge General Position Number of Some Graphs*, *Bulletin of the Malaysian Mathematical Sciences Society* 48 (2025), DOI:10.1007/s40840-025-01873-x. Author-posted full manuscript: https://www.researchgate.net/publication/391511435_The_Edge_General_Position_Number_of_Some_Graphs
