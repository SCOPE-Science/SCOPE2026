# The Pappus graph reconstructs itself from optimal locating-dominating codes

## Finding
Let \(P\) be the eighteen-vertex Pappus incidence graph, defined explicitly below. Its minimum locating-dominating sets have cardinality \(6\), and there are exactly \(18\) of them. Join two distinct minimum sets when they intersect in exactly \(4\) vertices. **The resulting graph on the eighteen minimum sets is isomorphic to \(P\) itself.**

There is also an exact reconfiguration threshold. A move adds or removes one vertex, with the requirement that the selected set remains locating-dominating. Under the capacity bound \(|S|\le7\), no two different minimum sets can be reconfigured into one another. Under \(|S|\le8\), every pair can be reconfigured, and the shortest number of moves between any minimum sets \(S,T\) is exactly \(|S\triangle T|\). Thus two spare selected vertices suffice, and one does not.

The unordered-pair intersection distribution of the \(18\) optima is \(18\) pairs of intersection size \(0\), \(54\) of size \(1\), \(54\) of size \(2\), and \(27\) of size \(4\). The corresponding optimal reconfiguration distances at capacity \(8\) are respectively \(12,10,8,4\).

## Assumptions and scope
Write \(\mathbb F_3=\{0,1,2\}\). Define \(P\) as the bipartite graph on nine point vertices \(p_{x,y}\), nine nonvertical line vertices \(\ell_{m,d}\), and incidence edges
\[
 p_{x,y}\sim\ell_{m,d}\quad\Longleftrightarrow\quad y=mx+d\ \text{in }\mathbb F_3,
 \qquad x,y,m,d\in\mathbb F_3.
\]
This is the cubic Pappus graph, also presented by the LCF description \([5,7,-7,7,-7,-5]^3\). For a set \(S\) of graph vertices, write \(\tau_S(u)=N(u)\cap S\) for each \(u\notin S\). We call \(S\) locating-dominating if every such trace is nonempty and all traces of vertices outside \(S\) are pairwise distinct. Only the ordinary **open-neighborhood** notion is used; this is not metric resolving, identifying coding, ordinary domination, or total domination.

Let \(\mathcal R_k\) have all locating-dominating vertex subsets \(S\) with \(|S|\le k\) as vertices and adjacency \(|S\triangle T|=1\). No intermediate set may violate the locating-dominating condition. The theorem concerns this particular eighteen-vertex graph and this addition/removal move.

## Proof
**Minimum size.** Suppose \(|S|=6\). Of the \(12\) outside vertices, at most \(6\) can have singleton trace (since their traces must differ). Each of the other at least \(6\) vertices has a trace of size at least two, so the number of edges crossing from \(S\) to its complement is at least \(6+2(6)=18\), and is at most \(3|S|=18\). Hence every inequality is sharp: \(S\) is independent, there are six different singleton traces, and exactly six different two-element traces. For \(|S|\le5\), at most \(|S|\) outside vertices can have singleton trace, and the number of crossing edges is at least \(|S|+2(18-2|S|)=36-3|S|>3|S|\); thus no smaller set works.

Write \(p\) for the number of chosen point vertices and \(q\) for the number of chosen line vertices, so \(p+q=6\). The \(p+3\) unchosen line vertices have at most \(p\) singleton signatures, and hence require at least \(p+6\) crossings from the \(p\) chosen points. Thus \(3p\ge p+6\), giving \(p\ge3\). By duality \(q\ge3\), so \(p=q=3\). All three pairs of chosen points must have two-element signatures on distinct unchosen line vertices. Two points with the same first coordinate cannot share a nonvertical line, so the three chosen points have all three distinct first coordinates. Similarly, the three chosen lines have all three distinct slopes.

The chosen points therefore have the form \(\{p_{x,f(x)}:x\in\mathbb F_3\}\) for a unique polynomial \(f(x)=ax^2+bx+c\), of degree at most two. The chosen lines cannot meet any chosen point because \(S\) is independent. For each slope \(m\), the selected line's intercept must consequently be a value *omitted* by \(f(x)-mx\). If \(a=0\), only the slope \(m=b\) has any omitted intercept; thus \(a\ne0\). If \(a\in\{1,2\}\), the three values of \(f(x)-mx\) consist of exactly two elements of \(\mathbb F_3\), with unique omitted element
\[
 r_m=c-a-(b-m)^2/a.
\]
All arithmetic here is in \(\mathbb F_3\), and \(1/a\) is its inverse. Thus the only possible minimum sets are
\[
 S_{a,b,c}=\{p_{x,ax^2+bx+c}:x\in\mathbb F_3\}
 \ \cup\ \{\ell_{m,c-a-(b-m)^2/a}:m\in\mathbb F_3\},
 \qquad a\in\{1,2\},\quad b,c\in\mathbb F_3.
\]
Each is indeed locating-dominating: on either bipartition side, the six unchosen vertices have exactly three different singleton traces and three different pair traces. The polynomial representation gives \(18\) distinct sets and proves both minimality and completeness.

**Self-isomorphism.** Exhausting the three-element field in the displayed formula (or expanding the two quadratics) gives, for unordered pairs of distinct codes, the intersection-size histogram \(\{0:18,1:54,2:54,4:27\}\). In particular the intersection is of size \(4\) only for opposite values of \(a\). Define a map from the optimal-code intersection graph to \(P\) by
\[
 S_{1,b,c}\longmapsto p_{b,c+b^2-1},\qquad
 S_{2,b,c}\longmapsto\ell_{-b,c-b^2}.
\]
It is bijective onto all points and all lines. A direct expansion of the six selected vertices gives
\[
 |S_{1,b,c}\cap S_{2,b',c'}|=4
 \ \Longleftrightarrow\ \ c'=c-1+(b-b')^2
 \ \Longleftrightarrow\ \ p_{b,c+b^2-1}\sim\ell_{-b',c'-b'^2}.
\]
For equal \(a\) the intersection is never of size \(4\). Hence the bijection preserves edges and nonedges, proving the isomorphism.

**Capacity threshold and shortest moves.** Under capacity \(7\), every move incident with a size-\(6\) minimum code must add one vertex. Two different six-sets in a common component would have to share a seven-set immediate superset; but that would require intersection size at least \(5\), contrary to the histogram. Moreover, removing from a six-set is impossible by minimality. Therefore the \(18\) optima are in different \(\mathcal R_7\) components. For capacity \(8\), the exact finite traversal described next enumerates all valid vertex sets of sizes \(6,7,8\) and all legal additions/removals. Breadth-first searches rooted at each of the \(18\) optima show that each of the \(153\) unordered pairs has distance exactly its symmetric-difference cardinality. This exhaustively establishes the asserted upper bound; every single-vertex move changes at most one coordinate, giving the matching lower bound. There is no assertion of connectivity for **all** states at capacity \(8\).

## Verification
Run `python3 check_pappus.py` and `python3 independent_check.py` with a standard Python 3 interpreter; no external packages are required. The first implementation constructs the incidence graph over \(\mathbb F_3\), enumerates every subset up to cardinality \(8\), verifies the exact parameterization and explicit isomorphism, constructs both reconfiguration graphs, and checks all \(153\) optimum pairs by shortest-path search. The second builds the same graph independently from the LCF cycle/chords and uses an explicit graph isomorphism to align labels, then independently enumerates all relevant locating-dominating sets and state transitions. The exact computed number of valid sets at sizes \(6,7,8\) is \(18,540,4869\). The graphs \(\mathcal R_7\) and \(\mathcal R_8\) have respectively \(558\) vertices and \(216\) edges, and \(5427\) vertices and \(6156\) edges. At capacity \(7\), the component-size distribution is eighteen components of \(13\) states and \(324\) isolated states; at capacity \(8\), it is one component of \(4419\) states and \(1008\) isolated states. All \(18\) minimum sets lie in the large component at capacity \(8\). The file `representative_paths.json` records one explicit shortest sequence for each possible optimum-intersection size.

## Relationship to prior work
The general locating-domination bounds of Balbuena, Foucaud and Hansberg include lower bounds that already imply a minimum of at least six for this cubic eighteen-vertex graph, and hence the numeral \(6\) alone is not claimed as a new bound. Earlier work on the reconfiguration of ordinary dominating sets studies a **different admissibility predicate**; ordinary domination does not enforce unique external neighborhood signatures. The new contribution is the entire set of eighteen minimizing locating codes, their intersection-graph self-isomorphism, and the sharp two-spare-vertex reconfiguration theorem with Hamming-geodesic paths for every pair. Existing treatments of the classical Pappus graph give its graph-theoretic representation, but not this structural classification. Unindexed equivalent results or unpublished calculations could remain.

## Limitations
All structural and shortest-path assertions pertain to this finite specified graph; none establishes an analogous theorem for other incidence graphs, and the numerical distance claims use exhaustive finite proofs rather than an unrestricted symbolic theorem. The entire capacity-eight graph is disconnected because of isolated nonminimum states. Only self-review has occurred; no independent external audit or certification has been performed. Novelty checks cannot prove universal absence from inaccessible or unindexed literature.

## References
- W. Haas and K. Seyffarth, *The \(k\)-Dominating Graph*, arXiv:1209.5138 (first public 2012-09-24). Ordinary domination reconfiguration, distinguished above.
- N. Suzuki, A. E. Mouawad, and N. Nishimura, *Reconfiguration of Dominating Sets*, arXiv:1401.5714 (first public 2014-01-22). General ordinary domination problem.
- C. Balbuena, F. Foucaud, and A. Hansberg, *Locating-dominating sets and identifying codes in graphs of girth at least 5*, arXiv:1407.7263 (first public 2014-07-27). General locating-domination bounds.
- C. Hernando, M. Mora, and I. M. Pelayo, *On global location-domination in bipartite graphs*, arXiv:1506.03442 (first public 2015-06-10). Related but distinct global notion.
- E. W. Weisstein, *Pappus Graph*, MathWorld. Classical cubic graph and its LCF presentation, https://mathworld.wolfram.com/PappusGraph.html.
