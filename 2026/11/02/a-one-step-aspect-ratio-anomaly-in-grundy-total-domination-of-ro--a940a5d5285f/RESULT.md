# A one-step aspect-ratio anomaly in Grundy total domination of rook graphs

## Finding

For every pair of integers \(m,n\ge 2\), let \(R_{m,n}=K_m\square K_n=L(K_{m,n})\), with vertices the \(mn\) ordered row-column cells and with distinct cells adjacent exactly when they share a row or a column. Its Grundy total domination number is

\[
\gamma_{\mathrm{gr}}^t(R_{m,n})=m+n-2+\mathbf 1_{\{|m-n|=1\}}.
\]

Moreover, if \(\{m,n\}=\{a,a+1\}\), then **every** longest legal open-neighborhood sequence is obtained by the following recipe: first choose an *ordered matching* of size \(a\) in the root graph \(K_{a,a+1}\); next connect its single uncovered root vertex on the larger side to a root vertex on the smaller side; finally, in any order, join each remaining isolated matching edge by one edge to the growing nontrivial component. At each final attachment either endpoint of the isolated matching edge can be used, with the new edge crossing to a previously used vertex on the opposite side of the growing component. The total number of distinct longest sequences of labeled cells is

\[
(a+1)!(a!)^2(2a-1)!!,
\]

where \((2a-1)!!=1\cdot3\cdot5\cdots(2a-1)\). Sequences, rather than their underlying unordered cell sets, are counted.

## Assumptions and scope

Graphs are finite, simple, undirected, and labeled. A sequence \(S=(v_1,\ldots,v_t)\) of pairwise distinct vertices is *legal* when \(N(v_j)\setminus\bigcup_{h<j}N(v_h)\ne\varnothing\) for each \(j\). It is a *total dominating sequence* if the union of these open neighborhoods is all of \(V(G)\). A longest legal sequence necessarily totally dominates any graph with no isolated vertices: if a vertex remains undominated, any one of its neighbors is unchosen and can be added legally. The invariant \(\gamma_{\mathrm{gr}}^t\) is the maximum possible length.

In the identification \(R_{m,n}=L(K_{m,n})\), a selected cell is an edge of the root complete bipartite graph, and the currently selected cells form a root edge set \(H\). Let \(U\) be the set of root vertices incident with \(H\), let \(r,s\) denote the numbers of unused root vertices in the two sides, and let \(i\) be the number of connected components of \(H\) consisting of a single edge. Isolated root vertices are **not** included in \(i\). Put \(\Phi=|U|-i\).

## Proof

**Uncovered-edge lemma.** An edge \(f\) of the root graph is not adjacent, in the rook graph, to any currently selected cell exactly in one of two disjoint cases: (i) both endpoints of \(f\) are unused root vertices, or (ii) \(f\) is itself a selected edge forming a one-edge component of \(H\). Indeed, an unselected edge meeting a selected edge is already dominated; a selected edge is dominated if and only if it meets a *different* selected edge. The root edges of type (i) form \(K_{r,s}\), and those of type (ii) are precisely the \(i\) isolated components.

**Progress lemma.** Each legal new selected root edge increases \(\Phi\) by either one or two. If its endpoints are both unused, it forms a new isolated component, increasing \(|U|\) by two and \(i\) by one. If exactly one endpoint is unused, \(|U|\) increases by one; \(i\) decreases by one if the other endpoint belongs to an isolated component and is otherwise unchanged. If neither endpoint is unused, legality (using the uncovered-edge lemma) forces it to meet at least one isolated component; it absorbs one or two such components, respectively raising \(\Phi\) by one or two. No edge can meet more than two one-edge components.

Before \(H\) first has a component containing two or more edges, \(H\) is a matching. The edge producing the first nontrivial component either joins two isolated matching edges, or attaches a fresh root vertex to an isolated matching edge. In either case the increase in \(\Phi\) is **two**. If no nontrivial component ever occurs, the sequence has at most \(\min\{m,n\}\le m+n-2\) terms. Otherwise, starting at \(\Phi=0\), a length-\(t\) sequence has \(\Phi\ge t+1\). As \(\Phi\le |U|\le m+n\), this gives

\[
t\le m+n-1.\]

**Rigidity at the upper endpoint.** Suppose a legal sequence has \(m+n-1\) terms. Then equality throughout the preceding inequalities forces \(|U|=m+n\), \(i=0\), exactly one increment of two, and every other increment of one. That single increment of two is the first formation of a nontrivial root component, so the preceding selected edges form a matching.

A legal increment-of-one step **cannot** exhaust the unused root vertices if any remain. For an edge having two fresh endpoints, legality requires a *different* uncovered root edge that shares a fresh endpoint with it, which necessarily leaves another unused root vertex after the step. For an edge having precisely one fresh endpoint, increment one means its used endpoint is not in an isolated component. Legality then requires an uncovered edge in \(K_{r,s}\) sharing its fresh endpoint, so again another unused root vertex remains. Steps using no fresh endpoints clearly cannot exhaust a nonempty unused set. It follows that the final fresh root vertex must be used at the unique increment-of-two step.

This step must therefore attach **one** fresh vertex to one of the preceding matching edges. The prior matching covers all but one of the \(m+n\) root vertices. A matching in a complete bipartite graph that covers all but one vertex exists only when \(|m-n|=1\), and necessarily has size \(a=\min\{m,n\}\). At that step the spare vertex is on the larger side and is joined to the smaller-side endpoint of a matching edge. No unused roots remain thereafter. Every subsequent legal increment-one edge must connect an as-yet-isolated matching edge to the unique growing nontrivial component, thereby absorbing one isolated matching component at each step. This proves the claimed exhaustive description of the equality sequences and excludes length \(m+n-1\) when \(|m-n|\ne1\).

**Constructions.** For all \(m,n\ge2\), select the cells

\[
(1,1),(1,2),\ldots,(1,n-1),(2,1),(3,1),\ldots,(m,1).
\]

Each choice in the initial row, except possibly the first, newly dominates a cell in its column and in an unused row; the first dominates \((1,n)\). Each later \((j,1)\) newly dominates \((j,n)\). Hence all \(m+n-2\) steps are legal. When \(\{m,n\}=\{a,a+1\}\), start instead with any ordered perfect matching saturating the smaller root side, attach the sole remaining larger-side vertex to one matching edge, and join the other matching edges one by one to the resulting component. Every matching choice is legal because an additional uncovered edge through a fresh root endpoint remains; each later choice newly dominates a previously isolated selected root edge. This yields \(2a=m+n-1\) steps and completes the maximum formula.

**Counting all exceptional optimizers.** Assume \(m=a,n=a+1\), without loss of generality. The initial ordered matching has \((a+1)!a!\) possibilities: an injection from the smaller labeled side into the larger, followed by an ordering of the matching edges. Its one extra root vertex can be attached to any of the \(a\) smaller-side matched vertices. The other \(a-1\) isolated matching edges may be absorbed in any order. When \(j\) matching components have been absorbed, the growing component has \(j\) smaller-side and \(j+1\) larger-side vertices. The next isolated matching edge may connect its smaller-side endpoint to any of the \(j+1\) larger-side vertices in this component or its larger-side endpoint to any of the \(j\) smaller-side vertices; these are \(2j+1\) distinct moves. Multiplying all independent choices gives

\[
(a+1)!a!\times a\times (a-1)!\times\prod_{j=1}^{a-1}(2j+1)
=(a+1)!(a!)^2(2a-1)!!.
\]

Every choice in the recipe produces a legal sequence; equality rigidity proves there are no other longest sequences. The same count applies when the two factor orders are swapped.

## Verification

The standalone `verify.py` constructs each rook graph directly from the adjacency condition and computes longest sequences and their multiplicities using memoized exhaustive recursion over the selected-vertex and dominated-vertex masks. It checks every board \((m,n)\) with \(m=2\) and \(2\le n\le7\), \(m=3\) and \(3\le n\le6\), and \((m,n)=(4,4),(4,5)\). In particular it obtains exactly 72, 12,960, and 7,257,600 ordered longest sequences for the \(2\times3\), \(3\times4\), and \(4\times5\) boards. For the first two exceptional boards, it also inspects every longest sequence and checks the matching-plus-absorption description. The program ends with `VERIFY_OK`. The theorem for arbitrary \(m,n\) is established by the proof, not extrapolated from the finite tests.

To replay: `python3 verify.py` (standard library only). The checker asserts that a terminal state of its recursion has dominated every cell, and enumerates using open—not closed—neighborhoods.

## Relationship to prior work

Brešar, Henning, and Rall introduced Grundy total domination via legal sequences of **open** neighborhoods and established general results in *Total Dominating Sequences in Graphs* (arXiv:1601.07525v1, 27 January 2016). The graph-product framework and the relation to skew zero forcing appear in Brešar and collaborators' *On Grundy total domination number in product graphs* (arXiv:1712.08780v1, 23 December 2017). That work investigates Cartesian products whose factors are paths or cycles in its Section 5; its complete-graph product remarks concern the **direct** product, not the Cartesian product of two cliques. Neither of these inspected texts states this aspect-ratio formula or the equality-sequence classification.

The general identity \(\gamma_{\mathrm{gr}}^t(G)=|V(G)|-Z^-(G)\), credited in the latter paper to Lin, implies the equivalent skew-zero-forcing consequence \(Z^-(R_{m,n})=mn-m-n+2-\mathbf1_{\{|m-n|=1\}}\). This identity is prior work and is not claimed as independently new. Papers on *ordinary* zero forcing or Grundy coloring are not equivalent: both the local rule and invariant differ.

## Limitations

The proof classifies and counts longest sequences **only** in the one-apart factor-order regime; it does not enumerate all optimum sequences in the other regimes. It assumes \(m,n\ge2\) and labeled graphs. Completeness of the mathematical proof is not a publication-priority guarantee: an earlier result indexed under skew zero forcing, edge-covering sequences, or line-graph terminology could exist beyond the inspected sources and retrieved records. No independent external mathematical audit is asserted.

## References

1. B. Brešar, M. A. Henning, D. F. Rall, *Total Dominating Sequences in Graphs*, arXiv:1601.07525v1 (2016-01-27), https://arxiv.org/abs/1601.07525 .
2. B. Brešar, C. Bujtás, T. Gologranc, S. Klavžar, G. Košmrlj, T. Marc, B. Patkós, Z. Tuza, M. Vizer, *On Grundy total domination number in product graphs*, arXiv:1712.08780v1 (2017-12-23), https://arxiv.org/abs/1712.08780 .
3. F.-H. Chang, *Grundy Total Domination and Skew Zero Forcing in Cartesian Products of Paths and Cycles*, arXiv:2608.27804v1 (2026-08-28), https://arxiv.org/abs/2608.27804 (different factor families).
