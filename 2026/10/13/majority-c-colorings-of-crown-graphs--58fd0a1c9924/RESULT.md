# Majority C-colorings of crown graphs
## Finding
For every integer \(n\ge 6\), let \(\operatorname{Cr}_n=K_{n,n}-M_n\) be the crown graph with deleted matching \(M_n=\{a_i b_i:1\le i\le n\}\). Its majority C-chromatic number is exactly \(\overline{\chi}_{\geqslant}(\operatorname{Cr}_n)=2\). Moreover, all optimal two-colorings can be classified from the two index sets \(S=\{i:a_i\text{ has color }1\}\) and \(T=\{i:b_i\text{ has color }1\}\). If \(n=2r\), then necessarily \(|S|=|T|=r\) and \(T=[n]\setminus S\), so there are \(\binom{n}{n/2}\) optimal colorings with the labeled palette \(\{1,2\}\). If \(n=2r+1\), then \((|S|,|T|,|S\cap T|)\) is exactly one of \((r,r,0)\), \((r,r+1,0)\), \((r+1,r,0)\), or \((r+1,r+1,1)\); hence the number of labeled optimal colorings is \((n+3)\binom{n}{(n-1)/2}\).

Thus deleting one perfect matching from an odd complete bipartite graph produces a sharp change for this recent invariant: the initiating paper proves \(\overline{\chi}_{\geqslant}(K_{n,n})=1\) when \(n\) is odd, whereas the crown graph has value \(2\) for every odd \(n\ge7\).

## Assumptions and scope
All graphs are finite, simple, and undirected. For \(n\ge6\), write
\[
A=\{a_1,\ldots,a_n\},\qquad B=\{b_1,\ldots,b_n\},
\]
and let \(\operatorname{Cr}_n\) have every edge \(a_i b_j\) with \(i\ne j\). Every vertex has degree \(n-1\). A majority C-coloring is a surjective vertex coloring in which every vertex shares its color with at least half of its neighbors. Hence each vertex of \(\operatorname{Cr}_n\) needs at least
\[
h=\left\lceil\frac{n-1}2\right\rceil=\left\lfloor\frac n2\right\rfloor
\]
same-colored neighbors.

The theorem claims the exact maximum number of colors and classifies every coloring attaining that maximum for \(n\ge6\). Small crowns are discussed only as prior-work boundaries, not as part of the new claim.

## Proof
Fix a used color class \(C\). Because \(h\ge1\), \(C\) cannot lie wholly in one bipartition shore: a vertex in such a class would have no same-colored neighbor. If \(C\) contains a vertex of \(A\), it must contain at least \(h\) vertices of \(B\); symmetrically it must contain at least \(h\) vertices of \(A\). Therefore every used color class has size at least \(2h\).

If \(n=2r\), then \(2h=n\), so at most two color classes fit into the \(2n\) vertices. If \(n=2r+1\ge7\), then \(2h=n-1\), and
\[
\left\lfloor\frac{2n}{n-1}\right\rfloor=2.
\]
Thus \(\overline{\chi}_{\geqslant}(\operatorname{Cr}_n)\le2\) for every \(n\ge6\).

Two colors always exist. For even \(n=2r\), choose \(S\subseteq[n]\) with \(|S|=r\), color \(a_i\) with color \(1\) exactly for \(i\in S\), and color \(b_i\) with color \(1\) exactly for \(i\notin S\). Every vertex then has exactly \(r\) same-colored neighbors. For odd \(n=2r+1\), choose disjoint sets \(S,T\subseteq[n]\) with \(|S|=r\), \(|T|=r+1\), and \(S\cup T=[n]\); color \(a_i\) with color \(1\) exactly for \(i\in S\) and \(b_i\) with color \(1\) exactly for \(i\in T\). Each vertex then has either \(r\) or \(r+1\) same-colored neighbors. Hence the upper bound is attained.

It remains to classify every optimal two-coloring. Let
\[
S=\{i:a_i\text{ has color }1\},\qquad T=\{i:b_i\text{ has color }1\},
\]
and put \(a=|S|\), \(b=|T|\), and \(c=|S\cap T|\).

For even \(n=2r\), each of the two color classes has at least \(2r\) vertices, so both have exactly \(2r\). Consequently \(a=b=r\). If \(c>0\), a same-colored deleted pair \(a_i,b_i\) would leave either endpoint with only \(r-1\) same-colored neighbors, below the threshold \(r\). Thus \(c=0\), and since \(|S|=|T|=r\), necessarily \(T=[n]\setminus S\). There are exactly \(\binom nr\) labeled choices.

For odd \(n=2r+1\), applying the lower bound of \(r\) vertices on each shore to both colors yields
\[
r\le a,b\le r+1.
\]
If \(c>0\), a color-\(1\) deleted pair forces both \(a\) and \(b\) to be at least \(r+1\), so \(a=b=r+1\). Pigeonhole then gives \(c\ge1\). If \(c\ge2\), the color-\(2\) class contains a deleted pair and only \(r\) vertices on each shore, so that pair would have only \(r-1\) same-colored neighbors. Hence \(c=1\). In every other size pattern we must have \(c=0\). This gives exactly the four triples stated in the finding.

For \((a,b,c)=(r,r,0)\), there are \(\binom nr(r+1)\) choices: choose \(S\), then choose the disjoint \(T\) by omitting one of the \(r+1\) remaining indices. The complementary type \((r+1,r+1,1)\) has the same count. Each mixed type \((r,r+1,0)\) and \((r+1,r,0)\) has \(\binom nr\) choices. Therefore the labeled count is
\[
2\binom nr(r+1)+2\binom nr=2(r+2)\binom nr=(n+3)\binom{n}{(n-1)/2}.
\]
This proves the full statement.

## Verification
The standalone `verify.py` constructs crown graphs directly from the deleted matching and tests the neighborhood condition, without using the structural proof as its feasibility test. It exhaustively checks all labeled two-color assignments for \(2\le n\le9\), confirms the structural classification and exact count, exhaustively checks all labeled three-color assignments for \(2\le n\le5\), and tests the explicit two-color construction through \(n=200\). Replay of the packaged artifact returns:

`ALL CHECKS PASSED; two_color_assignment_checks=349520; two_color_counts=[(2, 2), (3, 18), (4, 6), (5, 80), (6, 20), (7, 350), (8, 70), (9, 1512)]; three_color_small_counts={2: 0, 3: 12, 4: 0, 5: 0}; construction_range=2..200; exact_claim_range=n>=6`

These finite checks are stress tests. The all-\(n\) upper bound, constructions, classification, and counting formula are proved analytically above.

## Relationship to prior work
Bujtás, Dettlaff, Furmańczyk, and Laskowska introduced majority C-coloring in *Majority C-coloring of graphs*, first public as arXiv:2604.20752v1 on 2026-04-22. The paper lists primary MSC 05C15, defines the invariant, and gives exact values for cycles and complete bipartite graphs. In particular, it proves \(\overline{\chi}_{\geqslant}(K_{m,n})=2\) exactly when both shores are even and \(1\) otherwise. It also records known satisfactory-partition existence results for cubic and 4-regular graphs. Those general results settle existence of two colors for the small crown cases of degree \(3\) and \(4\), but they do not determine the accepted range \(n\ge6\), where the degree is at least \(5\), nor do they classify or enumerate optimal colorings. A direct full-text search of the initiating paper finds no occurrence of “crown.”

The same authors identify two-color majority C-colorings with satisfactory partitions and arbitrary-color majority C-colorings with sum satisfactory partitions. Older satisfactory-partition literature was therefore included in the overlap search. Publicly accessible abstracts confirm the same local-majority partition problem, but no inspected source states the crown-family formula or optimizer count. The closest semantic-index crown records concern other invariants, including proper conflict-free coloring and restrained domination, and do not imply this result.

A prior exact majority C-result for complete multipartite graphs is also not covering: for \(n\ge3\), \(\operatorname{Cr}_n\) is not complete multipartite. In particular, the odd-crown phenomenon here is genuinely different from the complete-bipartite parity law in the initiating paper.

## Limitations
The theorem is restricted to crown graphs \(\operatorname{Cr}_n\) with \(n\ge6\) and to the one-half open-neighborhood threshold defining majority C-coloring. It does not classify majority C-colorings using fewer than the optimum number of colors, nor does it treat arbitrary bipartite graphs with a deleted matching of non-perfect size.

The literature comparison cannot exclude an unindexed older statement under satisfactory-partition terminology. One older highly relevant satisfactory-partition paper was accessible only through its public abstract/bibliographic record, so it is retained as a residual originality risk rather than treated as whole-document noncoverage. The correctness proof does not depend on any unproved literature assertion.

## References
1. C. Bujtás, M. Dettlaff, H. Furmańczyk, and A. Laskowska, *Majority C-coloring of graphs*, arXiv:2604.20752v1, first public 2026-04-22; primary MSC 05C15.
2. C. Bazgan, Z. Tuza, and D. Vanderpooten, *The satisfactory partition problem*, Discrete Applied Mathematics 154 (2006), 1236–1245, DOI:10.1016/j.dam.2005.10.014.
3. K. H. Shafique and R. D. Dutton, *On satisfactory partitioning of graphs*, cited in the initiating majority C-coloring paper as foundational satisfactory-partition literature.
