# Parity-frustrated optimal independent-set exchanges on Möbius ladders

## Finding
For every integer \(n\ge3\), let \(M_{2n}\) be the labeled Möbius ladder on \(\mathbb Z/(2n)\mathbb Z\), with edges joining each \(i\) to \(i-1\), \(i+1\), and \(i+n\) modulo \(2n\). Let \(\mathcal R_n\) have as vertices *all maximum independent sets* of \(M_{2n}\), with two vertices adjacent exactly when their sets differ by replacing one selected graph vertex with one unselected graph vertex. Then

\[
\alpha(M_{2n})=\begin{cases}n,&n\text{ odd},\\n-1,&n\text{ even},\end{cases}
\qquad
\mathcal R_n\cong\begin{cases}2K_1,&n\text{ odd},\\C_{2n},&n\text{ even}.\end{cases}
\]

For odd \(n\), the two maximum independent sets are the even and odd vertex classes of the outer cycle. For even \(n\), put
\[
I_0=\{1,3,\ldots,n-1\}\cup\{n+2,n+4,\ldots,2n-2\}.
\]
All \(2n\) maximum independent sets are precisely the distinct translates \(I_r=I_0+r\) for \(r\in\mathbb Z/(2n)\mathbb Z\). Their only exchanges are
\[
I_r\sim I_{r+(n-1)}\quad\text{and}\quad I_r\sim I_{r-(n-1)}.
\]
Therefore the even-parameter exchange graph has \(2n\) edges and diameter \(n\); the odd-parameter exchange graph has no edges. Minimum vertex covers are complements of these sets and obey the same exchange classification. Both the independence-number formula and the counts of optimum sets were already obtainable from a graded independent-domination polynomial for Möbius ladders; neither is claimed as new. The exact optimal-set exchange adjacencies, components, and diameter are the claim.

## Assumptions and scope
Here \(n\) is an integer at least three, \(M_{2n}\) is a simple undirected graph, and independent means no two selected vertices are adjacent in this graph. A *maximum* independent set has cardinality \(\alpha(M_{2n})\), as opposed to merely being inclusion-maximal. Edges in \(\mathcal R_n\) use a single simultaneous deletion and insertion, with cardinality maintained throughout. Every vertex and maximum set is labeled; no quotient by graph automorphisms is taken. Translating a vertex subset means adding the same residue modulo \(2n\) to each element.

## Proof
Partition the vertices into the \(n\) antipodal pairs
\[
P_i=\{i,i+n\},\qquad 0\le i<n.
\]
Every independent set contains at most one vertex from each \(P_i\), hence has at most \(n\) elements. Record an occupied pair \(P_i\) by the sign \(+\) if \(i\) is chosen and \(-\) if \(i+n\) is chosen; record an unoccupied pair by \(\circ\). Because of the two outer-cycle paths, consecutive occupied pairs \(P_i,P_{i+1}\) with \(0\le i\le n-2\) must have opposite signs. The seam between \(P_{n-1}\) and \(P_0\) instead forces equal signs, as its two outer-cycle edges go between opposite layers. These conditions, together with at most one choice per antipodal pair, are also sufficient for independence: they account for every edge.

If all \(n\) pairs are occupied, the \(n-1\) ordinary transitions force sign factor \((-1)^{n-1}\), whereas the seam demands factor \(+1\). Thus a full occupancy exists exactly when \(n\) is odd. In that case the first sign has two choices, and every other sign is fixed. The resulting vertex sets are the two parity classes of the outer \(2n\)-cycle. They are distinct and have cardinality \(n\); since they are disjoint and contain \(n\ge3\) vertices, their symmetric difference has size \(2n>2\), so no one-token exchange is possible.

Now let \(n\) be even. Full occupancy is impossible; omitting any one pair breaks the inconsistent signed cycle into a path of \(n-1\) occupied pairs. Choose a sign at the first occupied pair and propagate along this path. Both possible starting signs give valid independent sets of cardinality \(n-1\). Thus the optimum is \(n-1\), and there are exactly \(2n\) maximizers, two for each choice of omitted pair. The set \(I_0\) displayed above is one such maximizer and omits precisely \(P_0\). Its \(2n\) translates remain independent by graph rotation. Translate indices differing by \(n\) omit the same pair but choose opposite endpoints in each of the other \(n-1\) pairs, so they are distinct. Any two translates with different residues modulo \(n\) omit different pairs. Consequently the translates are all \(2n\) maximizers, without duplication.

For an exchange between two maximizers, first suppose they omit the same pair. They must be either equal or the two sign-opposite assignments on the remaining path. The latter disagree on \(n-1\ge3\) occupied pairs and cannot differ by one deletion and one insertion. Therefore any exchange changes the omitted pair from \(P_i\) to some \(P_j\), deleting the vertex chosen from \(P_j\) and inserting one vertex into \(P_i\). If \(P_j\) is not adjacent to \(P_i\) in the cyclic order of pairs, both neighboring pairs of \(P_i\) remain occupied. The two requirements on the sign at \(P_i\) are incompatible, as full occupancy of the signed cycle was impossible. Thus \(j=i-1\) or \(j=i+1\) modulo \(n\). Conversely, in either of these two cases, after deleting the selected vertex in \(P_j\), the other neighbor of \(P_i\) is occupied, so there is a unique admissible sign for the inserted vertex; this produces one maximizer for each choice of \(j\). It follows that each of the \(2n\) maximizers has exactly two exchange neighbors.

For the explicit rotational description, compare \(I_0\) with \(I_{n-1}\) and \(I_{n+1}\): a direct comparison of the two displayed parity progressions shows their symmetric differences each contain exactly two vertices. They omit \(P_{n-1}\) and \(P_1\), respectively, and hence are the two just-classified neighbors. Rotational symmetry gives the two claimed neighbors of every \(I_r\). Because \(n\) is even, \(\gcd(n-1,2n)=1\), so repeated application of the step \(n-1\) visits every residue \(r\) modulo \(2n\). The connected two-regular graph is therefore exactly \(C_{2n}\). All claims follow.

## Verification
Run `python3 verify.py` with Python 3 and no external dependencies. It independently constructs the adjacency lists, exhaustively enumerates independent subsets by outer-cycle recursion and separately by antipodal-pair choices, and compares the two maximum-set enumerations. It constructs exchange edges both by symmetric-difference testing and by direct slides along original graph edges, then checks the expected cycles and isolated vertices and their exact rotation adjacencies for every integer \(3\le n\le15\). The final replay from the embedded verifier produced `VERIFY_OK`. These finite checks support the proof but do not replace its all-\(n\) argument.

## Relationship to prior work
Bonsma, Kamiński and Wrochna (arXiv:1403.0359v1, March 3, 2014) establish the general equivalence between token jumping and token sliding for maximum independent sets (Proposition 1), which is acknowledged here. Their main algorithm addresses claw-free graphs; Möbius ladders contain induced claws. The familiar scalar independence number is tabulated in MathWorld, and a previously established graded maximal-independent-set polynomial for this same family already implies the two-versus-\(2n\) optimum-state count. Those scalar and counting results are expressly excluded from the originality claim; they do not give one-token exchange adjacencies, connectivity, or distances. Agarwal and Basak (arXiv:2608.30601, August 31, 2026) determine homotopy types of Möbius-ladder independence complexes, a different invariant: these homotopy equivalences neither specify the complete maximum-face set nor imply its exchange adjacency graph. The new claim concerns the full optimum-configuration exchange graph and its sharp parity split, not a numerical independence bound or a homotopy computation. Related terminology includes minimum vertex-cover exchange and maximum-face reconfiguration of the independence complex.

## Limitations
The result concerns maximum independent sets only, not all inclusion-maximal independent sets or reconfiguration at smaller cardinalities, and only Möbius ladders as defined above. It does not assert uniqueness in the entire literature or a new independence-number formula. The stated parity split is proved for every integer \(n\ge3\); the four-vertex degenerate case is deliberately excluded. The numerical verifier covers only finite sample orders, whereas the proof is uniform.

## References
- P. Bonsma, M. Kamiński, and M. Wrochna, *Reconfiguring Independent Sets in Claw-Free Graphs*, arXiv:1403.0359v1 (first posted 2014-03-03), especially Proposition 1. https://arxiv.org/abs/1403.0359
- A. Agarwal and B. Basak, *The Homotopy Types of the Independence and Perfect Matching Complexes of Möbius and Circular Ladder Graphs*, arXiv:2608.30601 (first posted 2026-08-31), Sections 3–4. https://arxiv.org/abs/2608.30601
- Wolfram MathWorld, *Independence Number*, Möbius ladder entry. https://mathworld.wolfram.com/IndependenceNumber.html
- Wolfram MathWorld, *Independent Vertex Set*, Möbius ladder enumeration entry. https://mathworld.wolfram.com/IndependentVertexSet.html
