# Three symmetry types of maximum two-use zero-error codes for the \(7\)-cycle channel
## Finding
Let \(C_7\) be the cycle on \(\mathbb Z_7\), with two symbols confusable exactly when they differ by \(1\) or \(-1\) modulo \(7\). A two-use zero-error code is an independent set in the strong square \(C_7\boxtimes C_7\).

The known maximum size is \(10\), and the known number of labeled maximum codes is \(980\). Under the natural symmetry group
\[
G=(D_{14}\times D_{14})\rtimes S_2,
\]
of order \(392\), these \(980\) maximum codes split into exactly three orbits. Their orbit sizes are
\[
392,\qquad 392,\qquad 196,
\]
so the corresponding stabilizer orders are \(1,1,2\).

For \(a,b\in\mathbb Z_7\), define the cyclic distance
\[
\delta(a,b)=\min(|a-b|,7-|a-b|).
\]
For an unordered pair of codewords \((x_1,x_2),(y_1,y_2)\), sort the two coordinate distances \(\delta(x_1,y_1)\) and \(\delta(x_2,y_2)\). Let \(u\) be the number of codeword pairs with sorted distance multiset \(\{0,3\}\), and let \(v\) be the number with sorted distance multiset \(\{2,2\}\). The three natural-symmetry orbits have fingerprints
\[
(u,v)=(0,2),\qquad (1,1),\qquad (1,2),
\]
respectively, so this two-number invariant already separates the three extremal types.

Every maximum code has coordinate multiplicity profile \((2,2,2,1,1,1,1)\) in each coordinate. Canonical representatives for the three orbits are
\[
\begin{aligned}
&\{00,02,14,20,22,34,41,46,53,65\},\\
&\{00,02,14,21,26,33,40,45,52,64\},\\
&\{00,02,14,20,32,34,46,51,53,65\},
\end{aligned}
\]
where \(ab\) abbreviates the vertex \((a,b)\in\mathbb Z_7^2\).

## Assumptions and scope
The graph \(C_7\boxtimes C_7\) has vertex set \(\mathbb Z_7^2\). Distinct vertices are adjacent exactly when, in each coordinate, the entries are equal or adjacent in \(C_7\). Hence a set is independent exactly when every two distinct codewords have cyclic coordinate distance at least \(2\) in at least one coordinate.

The natural group used here consists of independent dihedral actions on the two \(7\)-cycles, together with interchange of the two coordinates. Each \(D_{14}\) has order \(14\), so the group has order \(14^2\cdot2=392\). The orbit statement is only for this explicit group.

## Proof
The verifier reconstructs the extremal set in two independent ways.

First, it uses a transfer computation by rows. There are exactly \(29\) independent subsets of one copy of \(C_7\). Treating such subsets as possible row states, it computes compatibility between consecutive rows and closes the seven-row cycle. This yields the complete independence polynomial
\[
1+49x+980x^2+10388x^3+63553x^4+229908x^5+486668x^6+576856x^7+346381x^8+81095x^9+980x^{10}.
\]
Thus the independence number is \(10\), and there are exactly \(980\) labeled maximum independent sets.

Second, the verifier builds the compatibility graph on the \(49\) vertices of \(\mathbb Z_7^2\), joining two vertices when they may coexist in an independent set of \(C_7\boxtimes C_7\). A complete branch-and-bound clique search enumerates every size-\(10\) code containing \(00\), finding exactly \(200\). Translating each of these codes by all \(49\) elements of \(\mathbb Z_7^2\) produces exactly the same \(980\) labeled maxima. The incidence identity
\[
980\cdot10=200\cdot49
\]
provides an independent consistency check.

The verifier then enumerates all \(392\) elements of \(G\), applies them to every maximum code, and canonically partitions the complete \(980\)-set collection into orbits. Exactly three orbits occur, with sizes \(392,392,196\). Direct stabilizer counting gives orders \(1,1,2\).

Finally, \(u\), \(v\), and each coordinate multiplicity multiset are invariant under every generator of \(G\). Computing them on the complete census gives precisely the three fingerprints \((0,2),(1,1),(1,2)\), while every maximum has coordinate profile \((2,2,2,1,1,1,1)\).

## Verification
The standalone `verify.py` uses only the Python standard library. It regenerates the \(29\) row states, the full independence polynomial, the \(200\) origin-normalized maxima, all \(980\) labeled maxima, all \(392\) natural symmetries, the three orbit representatives, and the stated fingerprints.

For canonical reproducibility, the newline-terminated list of the \(200\) maxima containing \(00\) has SHA-256
`2e8d95cfc42c76a63db408aa2c68122678e83dd8f3ec0e4190e605cc810f2675`,
and the corresponding canonical list of all \(980\) labeled maxima has SHA-256
`91a218e8c389d722d411f23ba32fee36aecf2072afb12619c7954b2d31f15bc5`.

A fresh replay returned:
`VERIFY_OK vertices=49 layer_states=29 maximum=10 maxima=980 normalized_origin=200 natural_group=392 orbits=3 orbit_sizes=196,392,392 stabilizers=2,1,1 orbit_fingerprints=(0,2):392;(1,1):392;(1,2):196 row_col_profile=2,2,2,1,1,1,1 normalized_sha256=2e8d95cfc42c76a63db408aa2c68122678e83dd8f3ec0e4190e605cc810f2675 maxima_sha256=91a218e8c389d722d411f23ba32fee36aecf2072afb12619c7954b2d31f15bc5`.

## Relationship to prior work
Shannon introduced zero-error capacity and the graph-product formulation of repeated channel use. Hales later proved exact independence-number formulas for strong products of odd cycles; specializing his square formula to \(C_7\) gives the maximum size \(10\).

A recent transfer-operator computation gives the complete independence polynomial above and therefore the exact count \(980\) of maximum independent sets. That work also uses dihedral orbit compression for the \(29\) single-cycle row states, but it does not classify the \(980\) maximum independent sets of the strong square under the natural order-\(392\) symmetry group.

Work on Shannon capacity of odd cycles, including \(C_7\), studies higher strong powers and improved lower bounds. The present result is instead an equality-case classification at the classical two-use level.

## Limitations
This is a finite structural classification for \(C_7\boxtimes C_7\). It does not improve a Shannon-capacity lower bound for \(C_7\), and it does not classify maximum codes in higher strong powers. The natural order-\(392\) group is explicit, but equality with the full automorphism group of \(C_7\boxtimes C_7\) is not asserted. A residual historical-priority risk remains for an obscure or unindexed equality-case classification not found in the checked literature or semantic searches.

## References
1. Claude E. Shannon, “The zero error capacity of a noisy channel,” *IRE Transactions on Information Theory* 2(3), 8–19 (1956), DOI 10.1109/TIT.1956.1056798. Public date: 1956-09-01.
2. R. S. Hales, “Numerical invariants and the strong product of graphs,” *Journal of Combinatorial Theory, Series B* 15, 146–155 (1973), DOI 10.1016/0095-8956(73)90014-2.
3. Frédéric Mathew and Patric R. J. Östergård, “New Lower Bounds for the Shannon Capacity of Odd Cycles,” arXiv:1504.01472.
4. Richard Hildebrant, “Transfer Operators and Independence Polynomials for Strong Powers of Circulant Graphs,” arXiv:2604.14416.
