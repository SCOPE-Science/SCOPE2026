# Six extremal \(\mathcal C_{[4,6]}\)-saturated graphs on eight vertices
## Finding
Let \(\mathcal C_{[4,6]}=\{C_4,C_5,C_6\}\). Among graphs on eight vertices with the minimum possible number of edges for \(\mathcal C_{[4,6]}\)-saturation, there are exactly six isomorphism classes. The known saturation number is
\[
\operatorname{sat}(8,\mathcal C_{[4,6]})=9.
\]
Thus the classification concerns all eight-vertex, nine-edge \(\mathcal C_{[4,6]}\)-saturated graphs.

On the vertex set \(\{0,1,\ldots,7\}\), canonical representatives may be taken with the following edge sets. An edge \(ij\) denotes \(\{i,j\}\).

1. \(\{07,16,24,27,35,36,45,47,56\}\), degree sequence \((1,1,2,2,3,3,3,3)\), two triangles, automorphism order \(2\), labeled orbit size \(20160\).
2. \(\{06,15,23,27,37,45,46,47,56\}\), degree sequence \((1,1,2,2,3,3,3,3)\), two triangles, automorphism order \(4\), labeled orbit size \(10080\).
3. \(\{06,07,15,17,24,26,34,35,67\}\), degree sequence \((2,2,2,2,2,2,3,3)\), one triangle, automorphism order \(2\), labeled orbit size \(20160\).
4. \(\{06,15,24,36,37,45,47,57,67\}\), degree sequence \((1,1,1,2,3,3,3,4)\), two triangles, automorphism order \(2\), labeled orbit size \(20160\).
5. \(\{07,16,25,36,37,45,47,57,67\}\), degree sequence \((1,1,1,2,2,3,3,5)\), two triangles, automorphism order \(2\), labeled orbit size \(20160\).
6. \(\{07,16,25,34,37,47,56,57,67\}\), degree sequence \((1,1,1,2,2,3,3,5)\), two triangles, automorphism order \(4\), labeled orbit size \(10080\).

Consequently there are exactly \(100800\) labeled extremal graphs on a fixed eight-element vertex set.
## Assumptions and scope
Graphs are finite, simple, and undirected. A graph is \(\mathcal C_{[4,6]}\)-saturated when it contains no cycle of length four, five, or six, but adding any missing edge creates at least one such cycle. The classification is only for order eight and minimum size nine. The value nine is taken from the cited saturation-number theorem; the new finite statement is the complete isomorphism classification at this order.
## Proof
The saturation-number theorem of Liu, Wang, and Gong gives
\[
\operatorname{sat}(n,\mathcal C_{[4,6]})=\left\lceil\frac{5n}{4}-\frac{7}{4}\right\rceil
\]
for the relevant range, hence the minimum at \(n=8\) is nine.

It remains to classify all nine-edge graphs on eight vertices. There are exactly
\[
\binom{28}{9}=6906900
\]
labeled nine-edge graphs. The verifier enumerates every one.

For a missing edge \(uv\), adding \(uv\) creates a cycle of length \(4\), \(5\), or \(6\) if and only if the original graph contains a simple \(u\)-to-\(v\) path of length \(3\), \(4\), or \(5\), respectively. Therefore saturation can be tested exactly by two finite conditions: the graph contains no simple cycle of lengths \(4,5,6\), and every nonedge has a simple endpoint path of one of the three lengths \(3,4,5\). Connectivity is also necessary and is used only as a safe preliminary rejection.

The exhaustive check returns exactly \(100800\) labeled graphs satisfying these conditions. To quotient by isomorphism, the verifier uses degree classes, which every isomorphism preserves. It maps equal-degree vertices through every permutation within their degree class into fixed target blocks ordered by degree and takes the lexicographically least 28-bit edge mask. Two graphs have the same resulting mask exactly when one of these degree-preserving relabelings identifies them. The \(100800\) labeled solutions yield exactly the six masks listed above.

For each class, the labeled count agrees with orbit-stabilizer:
\[
|\operatorname{Orb}(G)|=\frac{8!}{|\operatorname{Aut}(G)|}.
\]
The six orbit sizes are \(20160,10080,20160,20160,20160,10080\), which sum to \(100800\). This proves both completeness and pairwise non-isomorphism of the listed representatives.
## Verification
`artifacts/verify_c46_n8.cpp` is a standalone C++17 exhaustive verifier. It enumerates all \(6906900\) nine-edge graphs, tests the exact cycle/path characterization above, canonically groups the successful graphs, and prints the six class records. `artifacts/verification_output.txt` records the reviewed output. The verifier uses only integer and bit-set operations; there is no numerical tolerance.

The classification was also checked against degree sequences, triangle counts, automorphism orders, orbit sizes, and the identity that the six orbit sizes sum to the complete labeled count.
## Relationship to prior work
Liu, Wang, and Gong determine the exact minimum edge count for \(\mathcal C_{[4,6]}\)-saturation, which gives nine edges at order eight. Their result supplies the numerical extremal threshold used here. The present result adds the complete order-eight equality classification to that numerical threshold. Ma's earlier work determines the analogous minimum for forbidding \(C_4\) and \(C_5\), but it concerns a different forbidden family.
## Limitations
This is a finite, computer-assisted classification at \(n=8\); it does not classify minimum \(\mathcal C_{[4,6]}\)-saturated graphs for larger orders. The exhaustive argument depends on the correctness of the supplied verifier and the stated path-cycle equivalence, although both are simple enough to inspect directly. The result is a finite structural benchmark rather than a general-order theorem. Independent audit, proof-assistant verification, and expert attestation have not been performed.
## References
1. Qi Liu, Dijian Wang, and Shicai Gong, *Minimizing the number of edges in \(\mathcal C_{[4,6]}\)-saturated graphs*, arXiv:2608.18551v1, submitted 19 August 2026, MSC 05C35.
2. Yue Ma, *Minimum saturated graphs without \(4\)-cycles and \(5\)-cycles*, arXiv:2503.16839v1, DOI 10.1016/j.disc.2025.114690.
