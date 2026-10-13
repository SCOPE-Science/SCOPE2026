# Cardinality profile of minimal dominating sets in crown graphs
## Finding
For every integer \(n\ge3\), let the crown graph \(\operatorname{Cr}_n=K_{n,n}-M\) have bipartition
\(A=\{a_1,\ldots,a_n\}\) and \(B=\{b_1,\ldots,b_n\}\), where the deleted perfect matching is
\(M=\{a_i b_i:1\le i\le n\}\). A set \(S\subseteq V(\operatorname{Cr}_n)\) is an inclusion-minimal dominating set if and only if it is one of the following:

1. one full bipartition class, \(S=A\) or \(S=B\);
2. one deleted-matching pair, \(S=\{a_i,b_i\}\);
3. a four-vertex set \(S=\{a_i,a_j,b_k,b_\ell\}\) with \(\{i,j\}\cap\{k,\ell\}=\varnothing\).

Hence, if
\[\mathcal M(\operatorname{Cr}_n;x)=\sum_{S	ext{ minimal dominating}}x^{|S|},\]
then
\[\mathcal M(\operatorname{Cr}_n;x)=n x^2+6\binom{n}{4}x^4+2x^n.\]
In particular, \(\Gamma(\operatorname{Cr}_n)=n\). There are exactly \(2\) upper dominating sets when \(n=3\), exactly \(8\) when \(n=4\), and exactly \(2\) when \(n\ge5\).

The total number
\[\mathcal M(\operatorname{Cr}_n;1)=n+2+6\binom{n}{4}\]
is already represented by the crown-graph sequence OEIS A289121. The retained result is the structural classification and the size profile, not that total count or the scalar domination number.

## Assumptions and scope
Graphs are finite, simple, and undirected. Domination is ordinary closed-neighborhood domination. “Minimal” means minimal under set inclusion, not minimum cardinality. The statement covers every crown graph \(\operatorname{Cr}_n\) with \(n\ge3\).

For a candidate set \(S\), write
\[P=\{i:a_i\in S\},\qquad Q=\{i:b_i\in S\}.\]
The proof uses only the defining adjacency rule \(a_i b_j\in E\) exactly when \(i\ne j\).

## Proof
First characterize domination. If \(Q=\varnothing\), then no vertex of \(A\setminus S\) has a neighbor in \(S\), so domination forces \(P=\{1,\ldots,n\}\). Symmetrically, if \(P=\varnothing\), domination forces \(Q=\{1,\ldots,n\}\).

Assume now that \(P\) and \(Q\) are both nonempty. An unselected vertex \(a_i\) is dominated exactly when \(Q\) contains an index different from \(i\). Thus if \(|Q|\ge2\), every unselected vertex of \(A\) is dominated automatically; if \(Q=\{q\}\), domination on the \(A\)-side is equivalent to \(q\in P\). Symmetrically, if \(|P|=1\), with \(P=\{p\}\), domination on the \(B\)-side is equivalent to \(p\in Q\).

The two full sides \(A\) and \(B\) are minimal dominating: deleting a selected vertex leaves that same-side vertex with no selected neighbor. If \(|P|=|Q|=1\), the preceding domination criterion forces \(P=Q=\{i\}\), producing exactly the deleted-matching pair \(\{a_i,b_i\}\); deleting either endpoint leaves the other bipartition side undominated, so the pair is minimal.

Suppose \(|P|=1\) and \(|Q|\ge2\). The domination criterion forces the unique index of \(P\) to lie in \(Q\). Deleting any selected \(b_j\) whose index differs from that unique index leaves a dominating set, so such a set is not minimal. The case \(|Q|=1\), \(|P|\ge2\), is symmetric.

Finally suppose \(|P|,|Q|\ge2\). If \(|P|\ge3\), deleting any one selected \(a_i\) leaves at least two selected vertices on each side, hence still dominates; the same holds if \(|Q|\ge3\). Minimality therefore forces \(|P|=|Q|=2\). Write \(P=\{i,j\}\). After deleting \(a_i\), the reduced set has singleton \(P=\{j\}\), and by the domination criterion it remains dominating exactly when \(j\in Q\). Thus every deletion of an \(A\)-vertex must break domination exactly when \(P\cap Q=\varnothing\); the symmetric deletion test on the \(B\)-vertices gives the same condition. Hence the four-vertex minimal sets are precisely the disjoint-index \(2+2\) sets.

There are \(n\) deleted-matching pairs. For a four-vertex set, choose four distinct indices and then choose which two belong to \(P\), giving \(\binom n4\binom42=6\binom n4\) sets. Together with \(A\) and \(B\), this proves the enumerator. Its largest exponent is \(n\), so \(\Gamma(\operatorname{Cr}_n)=n\). At \(n=4\), the six disjoint-index four-sets tie the two full sides at size \(4\); otherwise only the two full sides attain size \(n\).

## Verification
A standalone exhaustive checker enumerates every vertex subset for \(3\le n\le9\), independently tests domination and inclusion-minimality, compares the result with the three structural families, verifies every coefficient of the enumerator, verifies the upper domination number, and checks that the total agrees with OEIS A289121. Its replay output is:

`VERIFY_OK n_range=3..9 subset_checks=349497 minimal_checks=1568 classification_checks=349497 coefficient_checks=19 enumerator=n*x^2+6*C(n,4)*x^4+2*x^n upper_domination=n oeis_total_match=A289121 max_order=18`

This finite computation is only a consistency check. The all-\(n\) statement is proved by the case analysis above.

## Relationship to prior work
Alikhani and Peng introduced the domination polynomial, which counts all dominating sets by cardinality; their framework motivates keeping cardinality information rather than only a scalar parameter. AbouEisha et al. define upper domination as maximum cardinality among inclusion-minimal dominating sets and study its algorithmic complexity. Neither inspected text gives a crown-graph minimal-dominating-set profile.

A same-object 2015 paper by R. Mary Jeya Jothi defines crown graphs and proves the existence of a minimal dominating set of cardinality \(n\); that statement is strictly weaker than a classification of every minimal dominating set. OEIS A289121 tabulates the total number associated with minimal dominating sets of crown graphs, and Graph::Maker::Crown explicitly identifies A289121 with that total. Therefore the identity \(n+2+6\binom n4\) at \(x=1\) is prior-covered and is used here as an external consistency check, not as a novelty claim.

The retained contribution is the exact structural decomposition into three families and its cardinality enumerator, which separates the previously aggregated total by size and immediately determines all upper-dominating extremals.

## Limitations
The theorem is specific to crown graphs and ordinary domination. It does not claim a corresponding classification for general bipartite graphs, rook-complement graphs of arbitrary dimensions, or other domination variants. A specialized source not surfaced by the exact-name and alias searches could contain the same profile; the strongest directly relevant database source located records the total count but not the size distribution. The 2015 same-object PDF was available as parsed text for the relevant crown section, while a page-image retrieval attempt was unsuccessful; the theorem comparison therefore relies on the recoverable text of that section.

## References
1. S. Alikhani and Y.-H. Peng, *Introduction to Domination Polynomial of a Graph*, arXiv:0905.2251v1, first posted 14 May 2009.
2. H. AbouEisha, S. Hussain, V. Lozin, J. Monnot, B. Ries, and V. Zamaraev, *Upper Domination: towards a dichotomy through boundary properties*, arXiv:1609.01510v1, first posted 6 September 2016.
3. R. Mary Jeya Jothi, *A Discussion on SSP Structure of Pan, Helm and Crown Graphs*, ARPN Journal of Engineering and Applied Sciences 10(9) (2015), 4115–4121.
4. OEIS A289121, total number associated with minimal dominating sets of crown graphs.
5. Graph::Maker::Crown documentation, crown definition and OEIS cross-reference to A289121.
