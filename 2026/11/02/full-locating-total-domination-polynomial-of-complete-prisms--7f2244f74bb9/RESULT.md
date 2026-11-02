# Full locating-total domination polynomial of complete prisms

## Finding
For every integer \(n\ge2\), let \(G_n=K_n\square K_2\), with two labeled clique layers \(A=\{a_1,\ldots,a_n\}\), \(B=\{b_1,\ldots,b_n\}\), and matching edges \(a_i b_i\). Let \(\mathcal L_n\) be the collection of locating-total dominating subsets of \(V(G_n)\), and define their size enumerator
\[
L_n(t)=\sum_{S\in\mathcal L_n}t^{|S|}.
\]
Then the **complete polynomial**, not only its smallest nonzero exponent, is
\[
\boxed{L_n(t)=
\begin{cases}
4t^2+4t^3+t^4,&n=2,\\[2pt]
t^n(t+2)^n+nt^{n-1}(t+2)^{n-1}-2nt^n-2n^2t^{n-1}+6t^2,&n=3,\\[2pt]
t^n(t+2)^n+nt^{n-1}(t+2)^{n-1}-2nt^n-2n^2t^{n-1},&n\ge4.
\end{cases}}
\]
In particular,
\[
\gamma_t^L(G_n)=\begin{cases}n,&2\le n\le4,\\n-1,&n\ge5,\end{cases}
\quad
\#\{S\in\mathcal L_n:|S|=\gamma_t^L(G_n)\}=
\begin{cases}
4,&n=2,\\
14,&n=3,\\
56,&n=4,\\
n(2^{n-1}-2n),&n\ge5.
\end{cases}
\]
For \(n\ge5\), the minimum sets are **exactly** those with one completely unselected matching column, one selected endpoint in each other column, and at least two selected endpoints in each clique layer. All sets are counted as labeled subsets.

## Assumptions and scope
Every graph is finite, undirected, and simple. A set \(S\subseteq V(G)\) is *locating-total dominating* (LTD) if (a) \(N(v)\cap S\ne\varnothing\) for **every** vertex \(v\in V(G)\) (including members of \(S\)), and (b) the nonempty sets \(N(v)\cap S\), for distinct \(v\in V(G)\setminus S\), are pairwise different. Neighborhoods are **open**. The matching column indexed by \(i\) consists of \(\{a_i,b_i\}\).

The complete structural classification, including nonminimum sets, is this. When \(n\ge3\), a set is LTD if and only if it has at most one empty column and one of the following three mutually exclusive layer-occupancy patterns:

1. At least two selected vertices from **each** layer.
2. Exactly one layer is fully selected and the other is empty (the two monochromatic-layer sets).
3. Exactly one layer has one selected vertex, this vertex's matched mate is also selected, and all columns other than this full column are singly selected in the opposite layer, apart from at most one empty column.

For \(n=2\), the same patterns are valid, together with the two additional sets selecting exactly one full matching column and leaving the other empty.

## Proof
**1. Neighborhood signatures and the empty-column obstruction.** Write \(A_S=A\cap S\), \(B_S=B\cap S\), \(p=|A_S|\), \(q=|B_S|\). For unselected \(a_i\) and \(b_j\), respectively,
\[
N(a_i)\cap S=A_S\cup(\{b_i\}\cap S),\qquad
N(b_j)\cap S=B_S\cup(\{a_j\}\cap S).
\]
If two columns \(i\ne j\) are empty, their unselected top vertices both have the signature \(A_S\). Thus a locating set has at most one empty column. Conversely, with at most one empty column, the signatures of unselected vertices **within the same layer** are distinct: a vertex with its matched opposite-layer mate selected has a signature featuring that uniquely indexed mate; those without a selected mate are contained in empty columns, of which at most one exists.

For a top outside vertex, its signature contains all \(p\) selected top vertices and at most one selected bottom vertex; for a bottom outside vertex the reverse is true. Therefore if \(p\ge2\) or \(q\ge2\), a top and a bottom outside vertex cannot share a signature. These observations completely settle the locating requirement except when \(p\le1\) and \(q\le1\).

**2. Total domination and classification.** A whole clique layer is internally totally dominated as soon as it contains at least two selected vertices. If \(p=1\), say \(A_S=\{a_i\}\), then the selected vertex \(a_i\) has a neighbor in \(S\) exactly when \(b_i\in S\). If \(p=0\), every \(a_j\) requires \(b_j\in S\), forcing \(B_S=B\). The same statements hold on interchanging layers.

Thus if \(p,q\ge2\), total domination is automatic and the locating condition reduces to at most one empty column, giving pattern 1. If \(p=0\) or \(q=0\), the other layer must be full, giving pattern 2. If exactly one of \(p,q\) equals 1 and the other is at least 2, the single vertex must be accompanied by its matched mate; at most one remaining column can be empty and every other column is singly selected in the opposite layer, giving pattern 3. The cross-layer signatures in all three patterns differ as established above.

If \(p=q=1\), the single selected vertex in each layer must be paired in the same column to satisfy total domination. Then there are \(n-1\) empty columns. This violates locating for \(n\ge3\); for \(n=2\), it produces exactly two additional feasible full-column sets. This proves necessity and sufficiency of the stated classification.

**3. Enumerate the three patterns.** Choose either zero or one empty columns. Each nonempty column can be top-only (weight \(t\)), bottom-only (weight \(t\)), or full (weight \(t^2\)). Put
\[
P_m(t)=(2t+t^2)^m=t^m(t+2)^m.
\]
An unrestricted assignment of these column states to \(m\) nonempty columns with at most one selected top vertex contributes
\[
E_m(t)=(m+1)t^m+mt^{m+1}:
\]
indeed, the top layer is entirely empty (one assignment), contains the top-only vertex of one column (\(m\) assignments), or contains the top vertex of one full column (\(m\) assignments). By symmetry the same polynomial counts at most one selected bottom vertex.

For \(n\ge4\), both \(m=n\) and \(m=n-1\) are at least 3, so the two low-layer-count classes do not overlap: \(p+q\ge m\ge3\). Hence the contribution from pattern 1 is
\[
P_n+nP_{n-1}-2E_n-2nE_{n-1}.
\]
Pattern 2 contributes \(2t^n\). Pattern 3 has \(n\) choices of its full column and two layer orientations; without an empty column it contributes \(2nt^{n+1}\), while choosing one of the remaining \(n-1\) columns to be empty contributes \(2n(n-1)t^n\). Adding and collecting terms gives
\[
L_n=P_n+nP_{n-1}-2nt^n-2n^2t^{n-1},\qquad n\ge4.
\]
For \(n=3\) the one-empty-column part has \(m=2\), where precisely two assignments (one top-only and one bottom-only column, in either order) were subtracted twice. Correcting for the three choices of empty column adds \(6t^2\) to the same formula. For \(n=2\), the graph is a four-cycle: its LTD sets are the four adjacent vertex pairs, the four three-vertex subsets, and the complete vertex set. This yields the displayed boundary polynomial.

**4. Minima and the transition.** For \(n\ge3\), the lowest possible degree in the polynomial is \(n-1\), with coefficient \(n(2^{n-1}-2n)\) for \(n\ge4\); it vanishes at \(n=4\), and at \(n=3\) the exceptional correction cancels the degree-two term. It is positive for all \(n\ge5\). The first nonzero coefficients in the cases \(n=2,3,4\) are respectively \(4,14,56\), all in degree \(n\). For \(n\ge5\), a size-\(n-1\) set has one empty column and exactly one selected vertex in every other column. By the classification, it must have at least two selections in each layer, and the choices number
\[
n\sum_{j=2}^{n-3}\binom{n-1}{j}
=n\big(2^{n-1}-2n\big).
\]
This also proves the minimum-set classification and completes the theorem.

## Verification
A standalone verifier `verify_prisms.py` constructs the graph independently from its adjacency rule, tests the original LTD definition on every one of the \(2^{2n}\) vertex subsets for each \(2\le n\le10\), and checks **all coefficients** of the proposed polynomial against the exhaustive counts. The observed total numbers of LTD sets for \(n=2,3,\ldots,10\) were \(9,36,149,588,2103,7178,23913,78552,255659\). A second verifier `verify_prisms_structure.py` independently checks the claimed minimum-size boundary and equality-class structures for all \(2\le n\le10\), and separately checks forty long constructions in larger instances. Both executed successfully after extraction from the delivered package.

These computations are finite corroborations, **not** proofs of the infinite assertion. The infinite proof is the preceding explicit neighborhood analysis and coefficient count.

## Relationship to prior work
Chakraborty, Foucaud, Hakanen, Henning, and Wagler prove a bound for all twin-free cobipartite graphs (their Theorem 3); for these complete prisms it yields an upper bound of \(n\) but neither the sharp \(n-1\) transition for \(n\ge5\) nor the full LTD enumerator. Foucaud and Henning prove a universal locating-total bound for line graphs. The graph here is equivalently the line graph \(L(K_{2,n})\), but that universal bound does not provide a family-specific enumeration.

A separate mathematical record on mixed metric bases of complete prisms concerns a *different* distance-vector invariant that resolves graph vertices and edges simultaneously. Its transversal constraints resemble the minimum configurations here, but it neither characterizes general LTD sets nor supplies the polynomial. A paper computing locating-total domination for ordinary cycle prisms \(C_n\square K_2\) concerns a different family from \(K_n\square K_2\). The present formula is claimed as a checked mathematical finding subject to the publication-priority limitation below, not as a certified first discovery.

## Limitations
The result is specific to open-neighborhood locating-total domination for two *complete* clique layers joined by a perfect matching. It does not count all-location/open-locating codes, metric resolving sets, clique products with more than two layers, or prisms of arbitrary graphs. The full published mathematical literature cannot be exhaustively checked; an equivalent unindexed or differently named result might exist. The checks described here are not an independent mathematical audit.

## References
1. D. Chakraborty, F. Foucaud, A. Hakanen, M. A. Henning, A. K. Wagler, “Progress towards the two-thirds conjecture on locating-total dominating sets,” arXiv:2211.14178, first posted 25 November 2022; Discrete Mathematics 347 (2024), 114176.
2. F. Foucaud, M. A. Henning, “Location-domination in line graphs,” arXiv:1506.02623, first posted 8 June 2015; discuss general locating-total domination bounds for line graphs.
3. H. Raza, N. Iqbal, H. Khan, T. Botmart, “Computing locating-total domination number in some rotationally symmetric graphs,” Science Progress, first published 17 November 2021, DOI 10.1177/00368504211053417. Its cyclic-prism family is distinct from the present complete prisms.
