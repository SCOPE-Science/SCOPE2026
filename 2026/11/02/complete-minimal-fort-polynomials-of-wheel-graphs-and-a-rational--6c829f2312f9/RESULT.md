# Complete minimal-fort polynomials of wheel graphs

## Finding
For each integer \(n\ge3\), define the wheel \(W_{n+1}=K_1\vee C_n\) with one hub \(h\) and \(n\) cyclically labeled rim vertices. A nonempty vertex set \(F\) is a **fort** if no vertex outside \(F\) has exactly one neighbor in \(F\); it is **inclusion-minimal** if no proper subset is a fort.

Let \(A_n(z)\) enumerate inclusion-minimal forts containing \(h\), weighted by \(z^{|F|}\), and \(B_n(z)\) enumerate those omitting \(h\). Put
\[
D(u,z)=1-zu^2-zu^3-z^2u^4+z^3u^6.
\]
Then the complete two-parameter size distributions have rational generating functions
\[
\boxed{\sum_{n\ge3}A_n(z)u^n=zu\frac{\partial}{\partial u}\log\left(\frac{1-zu^2}{D(u,z)}\right)},
\]
\[
\boxed{\sum_{n\ge3}B_n(z)u^n=-u\frac{\partial}{\partial u}\log(1-zu^2-z^2u^3)-2zu^2}.
\]
The complete minimal-fort polynomial is \(M_n(z)=A_n(z)+B_n(z)\). These identities are understood as formal power series over \(\mathbb Q[z][[u]]\); the logarithmic derivatives are rational series with integer coefficients.

In particular, if \(a_n=A_n(1)\), then
\[
\boxed{\sum_{n\ge3}a_nu^n=\frac{u^3(3+4u-u^2-8u^3+4u^5)}{(1-u^2)(1-u^2-u^3-u^4+u^6)}}.
\]
The values for rim orders \(3,4,\ldots,15\) are \(3,4,5,3,14,12,21,25,44,55,78,112,158\). A general formula for the central-vertex sequence was explicitly left open in the earlier wheel-graph treatment [1].

## Assumptions and scope
All graphs are finite, simple, and undirected; vertices are individually labeled. The cycle has \(n\ge3\) vertices. “Minimal” always means inclusion-minimal, not merely minimum cardinality. The generating-function variable \(u\) records the rim order, and \(z\) records the number of vertices in a fort, including the hub if selected. Empty vertex sets are excluded by definition.

For a nonempty rim selection \(R\), write \(r=|R|\) and let \((g_1,\ldots,g_r)\) be the positive cyclic distances, measured in rim edges, between successive vertices of \(R\); then \(g_1+\cdots+g_r=n\). The tuple is read from a selected starting vertex and is cyclically ordered.

## Proof
**1. Hub-omitting forts.** Let \(h\notin F\), and set \(R=F\subseteq V(C_n)\). Since the hub is outside \(F\), the fort property requires \(|R|\ne1\). Every omitted rim vertex must have either zero or two selected rim neighbors, since it has no selected hub neighbor. If \(R\ne\varnothing\), any cyclic run of two or more omitted rim vertices has a boundary omitted vertex with exactly one selected rim neighbor, which is forbidden. Thus omitted rim vertices form an independent set \(I\) of \(C_n\); conversely every independent \(I\) gives a fort \(R=V(C_n)\setminus I\). For \(n\ge3\), these complements always contain at least two vertices. Inclusion-minimality of \(R\) is therefore equivalent to maximality of \(I\) among independent sets. An independent set of a cycle is maximal precisely when successive chosen vertices are separated by two or three rim edges. If \(|I|=s\), the cyclic gap composition has \(s\) parts, each two or three, and the complement \(R\) has \(n-s\) vertices. Hence
\[
[z^{n-s}]B_n(z)=\frac ns\binom{s}{n-2s}\quad\text{when }s\ge1,\ 2s\le n\le3s,
\]
with the coefficient zero otherwise. This counts a labeled starting vertex \(n\) times and divides by the \(s\) selected independent-set vertices. Summing over all \(s\ge1\) as cyclic compositions yields
\[
-u\frac{\partial}{\partial u}\log(1-zu^2-z^2u^3).
\]
Its formal term \(2zu^2\) comes from the inadmissible two-vertex cycle and is removed, establishing the second displayed formula for all \(n\ge3\).

**2. Hub-containing forts.** Let \(F=\{h\}\cup R\). A rim vertex outside \(R\) already has one neighbor in \(F\), namely the hub. It may therefore have zero or two selected rim neighbors, but not exactly one. The equivalent condition is that no gap between successive selected rim vertices has length exceeding three: if a gap were at least four, an unselected vertex two edges after a selected endpoint would have no selected rim neighbors and therefore exactly one neighbor in \(F\), namely the hub, whereas gaps of lengths one, two, or three are allowed. The rim selection must be nonempty: \(\{h\}\) is not a fort.

Within the class of hub-containing forts, adding rim vertices preserves the fort property, because it only shortens gaps. Thus deleting a selected rim vertex is the only possible one-step obstruction to inclusion-minimality. Such a deletion merges its adjacent gaps; the result remains a fort precisely if their sum is at most three. Consequently every selected rim vertex is necessary exactly when
\[
g_i\in\{1,2,3\}\quad\text{and}\quad g_{i-1}+g_i\ge4\quad\text{for all cyclic }i.
\]
For \(r=1\), the unique gap must be three, covering the smallest wheel.

Deleting the hub leaves \(R\), which is a fort exactly when its omitted rim vertices form an independent set, equivalently all the gaps are at most two. Under the adjacent-gap inequalities, that is equivalent to every gap being two. Thus the hub is essential precisely when **at least one gap equals three**. Deleting one vertex at a time suffices: any proper fort subset with the hub would contradict the rim-deletion criterion by upward closure within that class; any proper fort subset omitting the hub would imply \(R\) itself is a fort by upward closure of hub-omitting forts.

**3. Weighted transfer and exact labeling.** Use gap states \(1,2,3\) and a transition from gap \(a\) to \(b\) only when \(a+b\ge4\), weighted by \(u^b\). The transfer matrix is
\[
T(u)=\begin{pmatrix}0&0&u^3\\0&u^2&u^3\\u&u^2&u^3\end{pmatrix},\qquad
\det(I-zT(u))=D(u,z).
\]
For each \(r\ge1\), \(\operatorname{tr}(T(u)^r)\) counts admissible cyclic \(r\)-gap words, with coefficient \([u^n]\) recording total gap length \(n\). Exactly one such word has all gaps two; it contributes \(u^{2r}\). Every labeled fort with \(r\) selected rim vertices corresponds to \(r\) choices of a selected starting vertex, whereas the rim has \(n\) choices of labeled start. Therefore
\[
[z^{r+1}]A_n(z)=\frac nr[u^n]\big(\operatorname{tr}(T(u)^r)-u^{2r}\big).
\]
Using \(-\log\det(I-zT)=\sum_{r\ge1}z^r\operatorname{tr}(T^r)/r\) and applying \(zu\partial/\partial u\) gives
\[
\sum_{n\ge3}A_n(z)u^n
=zu\frac{\partial}{\partial u}\left(-\log D(u,z)+\log(1-zu^2)\right).
\]
This is the first formula. Substituting \(z=1\) and simplifying the derivative gives the rational generating function for the hub-containing sequence.

## Verification
The standalone Python 3 script `verify_wheel_minimal_forts.py` constructs wheel adjacencies and directly checks the fort definition and inclusion-minimality against **all** proper fort subsets for rim lengths \(4\) through \(15\). It exhaustively inspected 131,028 vertex subsets across 12 wheel orders, with no mismatch. It independently enumerates admissible cyclic gap tuples and maximal independent-set gap compositions, matches the 13 published hub counts through rim order \(15\), and expands the two rational bivariate generating functions through rim order \(40\). The execution terminates with `VERIFY_OK`.

These finite tests corroborate, but do not replace, the unrestricted bijective proof above. The graph-order-three boundary follows directly from the proof and appears in the formal-series check.

## Relationship to prior work
Becker, Cameron, Hanely, Ong, and Previte [1, Section 5.1, especially Corollary 21] established lower bounds for minimal forts of wheel graphs and listed the central-vertex sequence \(3,4,5,3,14,\ldots\), explicitly observing that no formula for those central-vertex counts was known. The present result supplies a rational generating function for precisely that sequence, and a stronger size-refined enumeration of **all** minimal forts, distinguishing whether the hub is included. Their zero-forcing interpretation is consistent: complements of inclusion-minimal forts are maximal failed zero forcing sets. Previously established lower bounds and listed terms are not claimed as new. General fort-hypergraph and Cartesian-product results [2] do not themselves produce these wheel enumerators; general zero-forcing span results [3] concern another invariant.

Literature comparison included the author-preprint full text and available bibliographic descriptions of its subsequent 2025 journal version. The journal version's entire text was not available for an independent section-by-section comparison, so its possible revisions remain a publication-priority risk.

## Limitations
The formulas are for wheel graphs with one universal hub and a simple cycle rim, not for general fan graphs, multi-hub cones, or arbitrary cacti. They count labeled vertex subsets rather than symmetry classes. The proof is complete internally, but originality has not received independent external certification and could be affected by unavailable later revisions or unindexed equivalent literature.

## References
[1] P. Becker, T. R. Cameron, D. Hanely, B. Ong, J. P. Previte, *On the Number of Minimal Forts of a Graph*, arXiv:2404.05963 (first posted 2024-04-09), especially Section 5.1 and Corollary 21; journal version *Graphs and Combinatorics* 41 (2025), article 25, DOI 10.1007/s00373-025-02891-z.

[2] T. R. Cameron et al., *Forts, (fractional) zero forcing, and Cartesian products of graphs*, arXiv:2310.17904 (2023).

[3] S. Jacob, *Zero Forcing Span of a Graph*, arXiv:2309.06234 (2023).
