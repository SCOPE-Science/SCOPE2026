# Fourth-coefficient extremizers for 2-regular triple systems
## Finding
Let \(G\) be a finite simple \(3\)-uniform, \(2\)-regular hypergraph on \(n\) vertices, and let \(i_3^{(4)}(G)\) denote the number of \(4\)-vertex subsets containing no hyperedge of \(G\). Necessarily \(3\mid n\) and \(n\ge 6\). Then
\[
i_3^{(4)}(G)\le \binom{n}{4}-\frac{n(2n-7)}{3}.
\]
Equality holds exactly when the dual loopless cubic multigraph \(F(G)\) is a disjoint union of even cycles in which every other support edge is doubled. Equivalently, each connected component of \(F(G)\) is obtained from \(C_{2\ell}\), for some \(\ell\ge2\), by doubling one of its two alternating perfect matchings.

Consequently, if \(6\mid n\), then the coefficient-wise conjecture of Sarantis, Tetali, and Zheng holds for the parameter slice \((r,d,k)=(3,2,4)\):
\[
i_3^{(4)}(G)\le i_3^{(4)}(H_{3,2}^{\,n}),
\]
where \(H_{3,2}^{\,n}\) is the disjoint union of \(n/6\) copies of \(H_{3,2}\). The equality isomorphism types are indexed by partitions of \(n/3\) into parts at least \(2\).

## Assumptions and scope
A hypergraph is simple when it has no repeated hyperedges. It is \(3\)-uniform when every hyperedge has three vertices and \(2\)-regular when every vertex lies in exactly two hyperedges. A weak independent set is a vertex set containing no hyperedge.

The dual multigraph \(F(G)\) has one vertex for each hyperedge of \(G\). Each vertex \(x\in V(G)\), which lies in exactly two distinct hyperedges \(e\) and \(f\), becomes one multigraph edge \(ef\). Thus \(F(G)\) is loopless and cubic. Simplicity of \(G\) forces every dual edge multiplicity to be at most \(2\).

The result concerns only the coefficient counting independent \(4\)-sets. It does not assert coefficient-wise inequalities for larger set sizes.

## Proof
Write \(m=|E(G)|\). Counting incidences gives
\[
3m=2n,
\]
so \(m=2n/3\).

For each \(4\)-set \(S\subseteq V(G)\), let \(t(S)\) be the number of hyperedges contained in \(S\). Counting pairs \((S,e)\) with \(e\subseteq S\) gives
\[
\sum_{|S|=4}t(S)=m(n-3).
\]
No \(4\)-set can contain three distinct hyperedges. Indeed, three distinct \(3\)-subsets of a fixed \(4\)-set omit three distinct vertices, so the fourth vertex belongs to all three triples, contradicting \(2\)-regularity. Hence \(t(S)\in\{0,1,2\}\).

Let
\[
P(G)=\#\bigl\{\{e,f\}\subseteq E(G): |e\cap f|=2\bigr\}.
\]
A \(4\)-set has \(t(S)=2\) exactly when it is the union of a unique pair counted by \(P(G)\). Therefore the number of dependent \(4\)-sets is \(m(n-3)-P(G)\), and
\[
i_3^{(4)}(G)=\binom{n}{4}-m(n-3)+P(G).
\]

A fixed hyperedge \(e\) can share two vertices with at most one other hyperedge. Otherwise, if \(e\) shared two vertices with distinct \(f\) and \(g\), the two \(2\)-subsets \(e\cap f\) and \(e\cap g\) would intersect, giving a vertex lying in \(e,f,g\), again contradicting \(2\)-regularity. Thus the graph on \(E(G)\) whose edges are the pairs counted by \(P(G)\) has maximum degree \(1\). Consequently
\[
P(G)\le \frac{m}{2}=\frac{n}{3}.
\]
Substitution yields
\[
i_3^{(4)}(G)\le \binom{n}{4}-\frac{2n}{3}(n-3)+\frac{n}{3}
=\binom{n}{4}-\frac{n(2n-7)}{3}.
\]

It remains to characterize equality. Equality in the bound for \(P(G)\) means every hyperedge has a unique mate sharing two vertices. In \(F(G)\), this says every dual vertex is incident with exactly one doubled edge. Since \(F(G)\) is cubic, every dual vertex has exactly one remaining incident simple edge. The doubled support edges form a perfect matching, and the remaining simple edges form another perfect matching. Their union is therefore a \(2\)-regular simple graph whose cycles alternate between the two matchings. Every such cycle has even length at least \(4\), because a \(2\)-cycle would create multiplicity \(3\) in \(F(G)\). Thus every component is an alternating-doubled \(C_{2\ell}\) with \(\ell\ge2\).

Conversely, any disjoint union of alternating-doubled \(C_{2\ell}\) components is a loopless cubic multigraph of maximum multiplicity \(2\), so it is dual to a finite simple \(3\)-uniform, \(2\)-regular hypergraph. Every dual vertex lies in a doubled pair, hence \(P(G)=n/3\) and equality holds.

A component based on \(C_{2\ell}\) has \(2\ell\) dual vertices and \(3\ell\) dual edges, hence corresponds to a hypergraph component on \(3\ell\) vertices. Therefore equality isomorphism types are in bijection with multisets of integers \(\ell\ge2\) whose sum is \(n/3\), that is, partitions of \(n/3\) with no part \(1\).

For the coefficient-wise consequence, \(H_{3,2}\) may be written on marked vertices \(a,b\) and two disjoint pairs \(\{x_1,x_2\}\), \(\{y_1,y_2\}\), with hyperedges
\[
\{a,x_1,x_2\},\ \{b,x_1,x_2\},\ \{a,y_1,y_2\},\ \{b,y_1,y_2\}.
\]
Its dual is an alternating-doubled \(C_4\). Hence a disjoint union \(H_{3,2}^{\,n}\) has \(P(G)=n/3\), and its \(4\)-set coefficient equals the displayed upper bound.

## Verification
Two exact checks accompany the proof.

The first enumerates all labeled loopless cubic multigraphs with edge multiplicity at most \(2\) on \(4\), \(6\), and \(8\) vertices. It finds respectively \(7\), \(640\), and \(170555\) such multigraphs. The maximum numbers of doubled support edges are \(2\), \(3\), and \(4\), exactly half the dual order. Every equality case has the predicted alternating-cycle form. On eight dual vertices the equality signatures are precisely one \(C_8\) component or two \(C_4\) components.

The second check directly enumerates all \(75\) labeled simple \(3\)-uniform, \(2\)-regular hypergraphs on six vertices and finds the maximum \(i_3^{(4)}(G)=5\), attained by \(45\) labeled systems. It also constructs the connected alternating-cycle equality family for \(6\le n\le21\) with \(3\mid n\) and brute-force counts the independent \(4\)-sets, agreeing with
\[
\binom{n}{4}-\frac{n(2n-7)}{3}.
\]

The complete verification programs and their exact outputs are included as standalone artifacts.

## Relationship to prior work
Sarantis, Tetali, and Zheng formulate a coefficient-wise strengthening of the Balogh--Bollobás--Narayanan independent-set conjecture. Their Proposition 3.3 proves the \(k=4\) coefficient inequality for \(3\)-uniform regular hypergraphs under a no-cross-edge hypothesis, while their Theorem 1.8 proves the total independent-set conjecture for all \(2\)-regular hypergraphs of odd uniformity. The present result removes the no-cross-edge hypothesis in the specific coefficient slice \((r,d,k)=(3,2,4)\) and also determines every equality type.

The total partition-function inequality from the degree-two theorem does not by itself imply a coefficient-wise inequality, so this coefficient statement is not a formal corollary of that result.

## Limitations
The argument is special to \(3\)-uniformity, degree \(2\), and the coefficient \(k=4\). Its key simplifications are that a \(4\)-set cannot contain three hyperedges under \(2\)-regularity and that overlap-by-two pairs form a matching on the hyperedges. Neither feature directly controls higher coefficients or higher degrees.

The originality assessment is best-of-knowledge based on the cited recent paper, targeted literature searches for the same parameter slice and dual characterization, and semantic comparison against indexed mathematical findings. Unpublished or unindexed prior work cannot be excluded. Independent audit, proof-assistant verification, and expert attestation have not been performed.

## References
1. M. Sarantis, P. Tetali, and Z. Zheng, *On Counting Independent Sets in Regular Hypergraphs*, arXiv:2609.17468v1, 15 September 2026.
2. J. Balogh, B. Bollobás, and B. P. Narayanan, *Counting independent sets in regular hypergraphs*, Journal of Combinatorial Theory, Series A 180 (2021), 105405, doi:10.1016/j.jcta.2021.105405.
