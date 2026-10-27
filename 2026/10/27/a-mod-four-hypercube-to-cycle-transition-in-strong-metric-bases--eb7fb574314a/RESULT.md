# A mod-four hypercube-to-cycle transition in strong metric bases of squared cycles

## Finding
For every integer \(n\ge6\), let \(G_n=C_n^2\) have vertex set \(\mathbb Z_n\), joining two distinct vertices when their cyclic separation is one or two. A vertex \(w\) *strongly resolves* \(u,v\) if a shortest \(w\)-to-\(u\) path contains \(v\), or a shortest \(w\)-to-\(v\) path contains \(u\). A *strong metric basis* is a minimum-cardinality set strongly resolving every unordered vertex pair. Let \(\mathcal B_n\) have all such bases as vertices, with an edge whenever one selected vertex is replaced by one unselected vertex and the result is another basis.

Then the strong metric dimension and the complete basis-exchange graph obey the exact classification

\[
\begin{array}{c|c|c|c}
n\pmod4 & \operatorname{sdim}(G_n)& |V(\mathcal B_n)|&\mathcal B_n\\\hline
0&n/2+1&n&C_n\\
1&(n+3)/2&n&C_n\\
2&n/2&2^{n/2}&Q_{n/2}\\
3&(n+1)/2&n&C_n
\end{array}
\]

Here \(Q_d\) is the graph on binary words of length \(d\), with an edge for changing one bit. Thus \(\mathcal B_n\) is always connected. Its diameter is \(\lfloor n/2\rfloor\) in the cycle cases and \(n/2\) in the hypercube case (these coincide numerically for even \(n\), but the graphs do not). The exact exchange-edge count is \(n\) in the cycle cases and \((n/2)2^{n/2-1}\) when \(n\equiv2\pmod4\).

The classification includes **every** basis, not only the minimum size. Its complements, which are the maximum independent sets of the strong resolving graph, are given explicitly below, with all indices reduced modulo \(n\):

* If \(n=4q\) with \(q\ge2\), they are \(I_t=\{t,t+1,\ldots,t+2q-2\}\), for \(t\in\mathbb Z_n\).
* If \(n=4q+1\) with \(q\ge2\), put \(\phi(j)=2qj\pmod n\); they are \(I_t=\{\phi(t+2j):0\le j\le2q-2\}\), for \(t\in\mathbb Z_n\).
* If \(n=4q+2\) with \(q\ge1\), they are all \(I_{\epsilon}=\{i+\epsilon_i(2q+1):0\le i\le2q\}\), for \(\epsilon\in\{0,1\}^{2q+1}\).
* If \(n=4q+3\) with \(q\ge1\), put \(\psi(j)=(2q+1)j\pmod n\); they are \(I_t=\{\psi(t+2j):0\le j\le2q\}\), for \(t\in\mathbb Z_n\).

In every case the strong metric bases themselves are exactly \(\mathbb Z_n\setminus I\) for the displayed \(I\).

## Assumptions and scope
All graphs are finite, simple and unweighted, and graph distances count edges. The exponent in \(C_n^2\) means the second graph power, not the Cartesian square. The strong resolving graph includes all \(n\) original vertices, including any isolated vertices (none occur here). Exchange is token jumping, not token sliding: the removed and inserted vertices need not be adjacent in \(G_n\). The result covers precisely all integers \(n\ge6\); for \(n\le5\), the second cycle power is complete or requires separate conventional definitions and is not claimed to follow this table.

## Proof
**Step 1: identify mutual maximal distance.** Write \(\delta(a,b)=\min\{(a-b)\bmod n,(b-a)\bmod n\}\). In the second cycle power,
\[
d_{G_n}(a,b)=\left\lceil\delta(a,b)/2\right\rceil.
\]
One vertex \(a\) is maximally distant from \(b\) if no neighbor of \(a\) is farther from \(b\) than \(a\) is. Rotational and reflectional symmetry makes this mutual condition equivalent to checking that none of \(a\pm1,a\pm2\) increases the displayed distance from \(b\). Substitution, including the change in cyclic separation at the antipode, gives the following complete list of nonzero step lengths for mutually maximally distant pairs:
\[
\begin{array}{c|c}
n& \text{cyclic step lengths in the strong resolving graph}\\\hline
4q&2q-1,\ 2q\\
4q+1&2q-1,\ 2q\\
4q+2&2q+1\\
4q+3&2q+1.
\end{array}
\]
For each row every smaller positive separation has a neighbor at strictly larger graph distance, and each listed separation has none; symmetry handles separations above \(\lfloor n/2\rfloor\). Hence this table determines **all** edges of the strong resolving graph \(H_n\).

**Step 2: transfer to maximum independent sets.** The vertex-cover theorem for the strong resolving graph, proved by Oellermann and Peters-Fransen [1, Theorem 2.1], asserts that \(S\subseteq V(G_n)\) is strongly resolving if and only if \(S\) covers every edge of \(H_n\). Thus every basis is the complement of a maximum independent set of \(H_n\). We classify these independent sets case by case.

**Step 3: residue \(2\).** For \(n=4q+2\), \(H_n\) is exactly the perfect matching \(\{\{i,i+2q+1\}:0\le i\le2q\}\). An independent set has at most one vertex from each matched pair; equality requires exactly one choice per pair. This gives the \(2^{2q+1}\) transversals displayed in the finding, each of cardinality \(2q+1\).

**Step 4: residue \(3\).** For \(n=4q+3\), the sole step \(s=2q+1\) is relatively prime to \(n\), since \(n-2s=1\). The relabeling \(j\mapsto sj\bmod n\) identifies \(H_n\) with an ordinary cycle of odd order \(n\). An independent set of cardinality \(r\) has cyclic gaps at least two, so \(r\le(n-1)/2=2q+1\). Equality leaves exactly one unit of slack beyond gaps of length two: exactly one gap is three and all others are two. These are precisely the \(n\) cyclic translates displayed above.

**Step 5: residue \(1\).** Let \(n=4q+1\). Multiplication by \(2q\) changes the step set \(\{1,3\}\) into \(\{2q,2q-1\}\) because \(6q\equiv2q-1\pmod{4q+1}\). Since \(\gcd(2q,4q+1)=1\), this is an isomorphism from \(C_n(1,3)\) onto \(H_n\). In \(C_n(1,3)\), independence is equivalent to every cyclic gap between successive selected vertices being at least two and different from three: nonconsecutive selected vertices are separated by sums of at least two such gaps and cannot have cyclic separation one or three. A hypothetical independent set of size \(2q\) would have total gap slack \(n-2(2q)=1\), forcing a forbidden gap of three. At size \(2q-1\) the slack is three; a gap's positive slack cannot be one, so exactly one gap has slack three (length five), with every other gap equal to two. This proves that the displayed \(n\) sets are all and only the maxima.

**Step 6: residue \(0\).** Let \(n=4q\). The length-\(2q\) edges pair up antipodes \(P_i=\{i,i+2q\}\), \(0\le i<2q\), so an independent set has at most \(2q\) vertices. If it occupied every pair, record side \(0\) for \(i\) and side \(1\) for \(i+2q\). The additional step-\(2q+1\) (equivalently \(2q-1\)) edges force identical sides on every successive pair \(P_i,P_{i+1}\), \(0\le i<2q-1\), but force opposite sides between \(P_{2q-1}\) and \(P_0\). Such a full choice is impossible. If exactly one pair \(P_j\) is unoccupied, the other occupied pairs form a path with forced side propagation and exactly two independent assignments. They are precisely the intervals \(I_{j+1}\) and \(I_{j+2q+1}\) described in the finding. Hence the maximum has size \(2q-1\) and there are exactly \(2(2q)=4q=n\) maxima.

**Step 7: identify every exchange.** Complementation preserves symmetric differences; hence two bases differ by one exchange exactly when their complementary independent sets do. For residue \(2\), exchanging one chosen endpoint for the other in one antipodal pair is the only possible move: this is exactly one coordinate flip in \(Q_{2q+1}\). For residue \(0\), the \(n\) sets are cyclic intervals of length \(2q-1\), and two distinct such intervals intersect in all but one vertex exactly when their starting indices differ by \(\pm1\). Their exchange graph is therefore \(C_n\).

For residues \(1\) and \(3\), work in the respective relabeled cycle. Each maximum independent set has a unique long gap (of length five or three, respectively), and all its other gaps are two. Removing a selected vertex away from either endpoint of the long gap creates a gap of length four in addition to the long gap; the only feasible insertion restores the deleted vertex. Removing a vertex adjacent to the long gap merges a length-two gap with the long gap; this merged gap can be split legally in two ways, one restoring the original and the other shifting the long gap one selected position. Consequently, the only nontrivial exchanges link the indexed maxima \(I_t\) to \(I_{t\pm2}\). Since \(n\) is odd, this is a single \(n\)-cycle. The tabulated basis sizes, counts, diameters, and edge counts now follow.

## Verification
Run `python3 verify.py` using Python 3 and its standard library. The checker builds each squared cycle from its adjacency list, obtains all-pairs distances by independent breadth-first searches, constructs the mutual-maximal-distance graph, and separately tests every proposed minimum-cardinality subset against the **geodesic definition** of strong resolution. It confirms exact agreement with the four explicit basis families, reconstructs exchanges, and checks components, degrees, edges and diameter. For \(6\le n\le15\), it also tests every smaller-cardinality subset directly for failure. All \(15\) consecutive orders \(6\le n\le20\) pass, including the hypercube orders \(6,10,14,18\). This finite test corroborates, but does not replace, the unrestricted proof above.

## Relationship to prior work
Oellermann and Peters-Fransen [1] established the strong resolving graph/vertex-cover equivalence, including cases of Cartesian products of cycles; we use their established equivalence, but \(C_n^2\) is a **graph power**, not that Cartesian product. Kang and Yi [2] compare zero forcing and strong metric dimension generally. Jamil and coauthors [3] analyze **local fractional** strong resolving neighborhoods of the same circulant \(C_n(1,2)\), not integer strong metric bases or their exchanges. Nasir and coauthors [4] study **edge-based doubly resolving** sets for this circulant, another genuinely different resolution condition. None of these inspected statements contains the complete mod-four integer strong-basis family or its cycle/hypercube exchange transition. Independent earlier equivalent treatment under other terminology remains possible.

## Limitations
This is a theorem only for the second power of an ordinary simple cycle, and only for single-vertex exchanges at optimum cardinality. It does not address higher cycle powers, sliding-only moves, resilience to basis failures, or sampling of nonminimum resolving sets. The independent computational checks are finite. Search and source inspection cannot certify absolute priority against all unpublished or unindexed work; an independent assessment of novelty and proof has not been performed.

## References
[1] O. R. Oellermann and J. Peters-Fransen, “The strong metric dimension of graphs and digraphs,” *Discrete Applied Mathematics* 155 (2007), 356–364, DOI: 10.1016/j.dam.2006.06.009. Publicly available online August 21, 2006.

[2] C. X. Kang and E. Yi, “A Comparison between the Zero Forcing Number and the Strong Metric Dimension of Graphs,” arXiv:1401.3008, first posted January 13, 2014.

[3] F. Jamil, A. Kashif, S. Zafar and M. O. Ojiema, “Local Fractional Strong Metric Dimension of Certain Complex Networks,” *Complexity* (2023), Article 3635342, DOI: 10.1155/2023/3635342.

[4] R. Nasir, M. Ahmad, Z. Zahid, S. A. Bajri and H. A. E.-W. Khalifa, “Characterizing edge-based doubly resolving sets within circulant networks \(C_n(1,2)\),” *AIMS Mathematics* 9 (2024), 15857–15874, DOI: 10.3934/math.2024766.
