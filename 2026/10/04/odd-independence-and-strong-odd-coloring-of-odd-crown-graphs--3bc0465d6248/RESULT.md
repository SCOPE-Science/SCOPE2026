# Odd independence and strong odd coloring of odd crown graphs
## Finding
For every odd integer \(n\ge3\), let \(\operatorname{Cr}_n=K_{n,n}-M_n\) be the crown graph with bipartition \(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\), where the deleted perfect matching is \(\{a_i b_i:1\le i\le n\}\). Then
\[
\alpha_{\mathrm{od}}(\operatorname{Cr}_n)=2,
\qquad
\chi_{\mathrm{so}}(\operatorname{Cr}_n)=n.
\]
The maximum odd independent sets are exactly the \(n\) deleted matched pairs \(\{a_i,b_i\}\). Every optimal strong odd coloring is, up to permutation of colors, exactly the partition of \(V(\operatorname{Cr}_n)\) into those matched pairs. In particular,
\[
\alpha_{\mathrm{od}}(\operatorname{Cr}_n)\chi_{\mathrm{so}}(\operatorname{Cr}_n)=2n=|V(\operatorname{Cr}_n)|.
\]
Thus the product lower bound for odd independence and strong odd coloring is sharp on an infinite connected regular bipartite family whose degree \(n-1\) is even.

## Assumptions and scope
An odd independent set \(S\) is an independent set such that every vertex outside \(S\) has either zero or an odd number of neighbors in \(S\). A strong odd coloring is a proper vertex coloring in which, for each vertex, every color occurring in its open neighborhood occurs an odd number of times there. The result concerns finite simple crown graphs \(\operatorname{Cr}_n\) for odd \(n\ge3\).

The initiating paper proves the general inequality \(\alpha_{\mathrm{od}}(G)\chi_{\mathrm{so}}(G)\ge |G|\). It also treats regular bipartite graphs of odd degree, but an odd crown graph has even degree \(n-1\); hence that exact odd-degree proposition does not apply to the family proved here.

## Proof
Let \(S\) be an independent set in \(\operatorname{Cr}_n\). If \(S\) meets both bipartition classes, then independence forces \(S\subseteq\{a_i,b_i\}\) for a single index \(i\), because \(a_i\) is adjacent to every \(b_j\) with \(j\ne i\). Hence every mixed independent set has size at most two. Each deleted matched pair \(\{a_i,b_i\}\) is odd independent: for \(j\ne i\), vertex \(a_j\) has exactly the neighbor \(b_i\) in the pair, and vertex \(b_j\) has exactly the neighbor \(a_i\) in the pair.

It remains to rule out odd independent sets of size at least two lying inside one bipartition class. Suppose \(S\subseteq A\) and put \(s=|S|\). For a vertex \(b_j\), the number of its neighbors in \(S\) is \(s-1\) when \(a_j\in S\), and \(s\) when \(a_j\notin S\). If \(1<s<n\), both types of vertices occur, so the two positive consecutive integers \(s-1\) and \(s\) would both have to be odd, which is impossible. If \(s=n\), every \(b_j\) has \(n-1\) neighbors in \(S\), which is positive and even because \(n\) is odd. Thus no such \(S\) is odd independent. The same argument applies in \(B\). Therefore the maximum odd independent sets are exactly the deleted matched pairs and \(\alpha_{\mathrm{od}}(\operatorname{Cr}_n)=2\).

Every color class in a strong odd coloring is an odd independent set: properness makes it independent, and the neighborhood parity condition is precisely the remaining requirement. Hence every color class has size at most two, so a coloring of the \(2n\) vertices needs at least \(n\) colors. Conversely, color \(a_i\) and \(b_i\) alike for each \(i\). Every color class is a deleted matched pair and is odd independent, so this is a strong odd coloring with \(n\) colors. Thus \(\chi_{\mathrm{so}}(\operatorname{Cr}_n)=n\). Equality forces all \(n\) color classes to have size two, and the preceding classification of two-vertex odd independent sets forces them to be exactly the deleted matching pairs. This also proves uniqueness up to color permutation.

## Verification
The accompanying script `verification/check_crown_odd.py` reconstructs \(\operatorname{Cr}_n\) directly from adjacency, enumerates all vertex subsets, tests odd independence from the definition, and computes the minimum partition into odd independent sets by exact bitmask dynamic programming. For each odd \(n\in\{3,5,7,9\}\), it checks the values \(\alpha_{\mathrm{od}}=2\), \(\chi_{\mathrm{so}}=n\), that there are exactly \(n\) maximum odd independent sets, and that there is exactly one optimal unlabeled partition. The finite computation is a stress test only; the proof above establishes all odd \(n\ge3\).

## Relationship to prior work
Caro, Petruševski, Škrekovski, and Tuza introduced the odd independence number and proved the general product inequality, together with the exact statement that an odd-degree regular bipartite graph satisfies \(\alpha_{\mathrm{od}}(G)=\alpha(G)=|G|/2\) and \(\chi_{\mathrm{so}}(G)=2\). Their paper also gives a general upper bound for even-degree regular graphs, but that bound does not determine the odd crown graphs considered here. The same paper's stated list of explicitly treated classical families includes cycles, paths, Moore graphs, Kneser graphs, complete subdivisions, half graphs, Cartesian products of complete graphs, hypercubes, and complements of triangle-free graphs, not crown graphs.

Earlier work on strong odd coloring notes that complete bipartite graphs can have strong odd chromatic number at most four, but deleting a perfect matching changes the neighborhood parity constraints. Direct searches using “crown graph,” the equivalent description \(K_{n,n}-M_n\), and the bipartite-Kneser alias \(H(n,1)\), together with the parameter names and notations, found no exact statement implying the odd-crown formula above. The even-\(n\) crown branch is already covered by the published odd-degree regular-bipartite proposition and is not claimed as new here.

## Limitations
The theorem is specific to odd crown graphs. It does not classify odd independence or strong odd colorings for arbitrary matching-deleted bicliques \(K_{a,b}-M_t\), nor does the finite verification substitute for the universal proof. Literature searches cannot establish absolute novelty; the closest primary sources and the specific implication comparisons used in the review are recorded separately.

## References
1. Y. Caro, M. Petruševski, R. Škrekovski, and Z. Tuza, “The odd independence number of graphs, I: Foundations and classical classes,” arXiv:2509.20763, first public 2025-09-25.
2. Y. Caro, M. Petruševski, R. Škrekovski, and Z. Tuza, “On strong odd colorings of graphs,” arXiv:2410.02336, first public 2024-10-03; published in *Discrete Mathematics* 348 (2025), 114601.
