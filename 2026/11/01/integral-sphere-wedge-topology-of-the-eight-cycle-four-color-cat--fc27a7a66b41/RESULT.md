# Integral sphere-wedge topology of the eight-cycle four-color categorical product

## Finding
For the ordinary independence complex of the categorical product \(C_8\times K_4\), we prove the exact integral homotopy classification
\[
\operatorname{Ind}(C_8\times K_4)\simeq
\bigvee^{3}S^{4}\vee\bigvee^{6}S^{5}.
\]
The only nonzero reduced integral homology groups are \(\mathbb Z^3\) in degree \(4\) and \(\mathbb Z^6\) in degree \(5\). This is a specific torsion-free case in the unresolved general question concerning independence complexes of categorical products of cycles and complete graphs.

## Assumptions and scope
The graph is simple and finite, with vertex set \(\{(i,a):i\in\mathbb Z/8\mathbb Z,\ a\in\{0,1,2,3\}\}\). Distinct \((i,a)\) and \((j,b)\) are adjacent exactly when \(j-i\equiv \pm1\pmod 8\) and \(a\ne b\). The graph has \(32\) vertices and \(96\) edges. Its independence complex comprises the nonempty vertex subsets containing no graph edge, together with the empty face. All homotopy and homology statements are over the ordinary geometric realization; no coefficient field is needed for the theorem.

## Proof
Index each graph vertex by \(4i+a\). The included verifier enumerates all independent sets inductively: at vertex \(v\), retain every previous face, and adjoin \(v\) to precisely the previous independent sets disjoint from its graph-neighbor set. This visits every independent set exactly once, yielding exactly \(196226\) nonempty simplices.

Construct an acyclic discrete Morse matching by processing vertices \(v=0,\ldots,31\) in increasing order. At stage \(v\), for each currently unmatched simplex \(\sigma\) not containing \(v\), pair \(\sigma\) with \(\sigma\cup\{v\}\) if both are still unmatched. There are exactly \(98087\) disjoint pairs, leaving one critical vertex, \(24\) critical 4-simplices and \(27\) critical 5-simplices. The complete oriented Hasse diagram (unmatched incidences down and matching incidences up) has \(1457216\) arrows. Exhaustive topological sorting visits all \(196226\) face-poset vertices, proving acyclicity (not merely counting pairs). Forman's discrete Morse theorem gives a CW complex with precisely these critical cells.

Use the increasing vertex order to orient the simplices. For each matched pair \((\sigma,\tau)\), the simplicial incidence number of \(\sigma\) in \(\partial\tau\) is \(\pm1\). Exact algebraic Morse cancellation recursively rewrites every matched lower face using that unit boundary coefficient, sends matched upper faces to zero, and retains critical faces. Applied to the \(27\) critical 5-simplices, this produces the integer boundary homomorphism \(\partial^M_5:\mathbb Z^{27}\to\mathbb Z^{24}\). The verifier computes its full matrix and proves its rational rank is \(21\) by exact fraction arithmetic. Taking zero-based row indices
\[
(0,1,\ldots,19,21)
\]
and column indices
\[
(1,2,3,4,5,6,7,8,9,10,11,14,15,16,17,18,19,20,21,22,23)
\]
gives a \(21\times21\) minor whose exact integer determinant is \(-1\). Thus all nonzero Smith factors are \(1\), and no integral torsion occurs. Since there are no other positive-dimensional Morse cells, the reduced homology is free of ranks \(24-21=3\) and \(27-21=6\) in dimensions four and five.

Finally, the Morse CW model has one 0-cell and cells only in degrees four and five. Its 4-skeleton is a wedge of 24 four-spheres, and each 5-cell attaches by an element of \(\pi_4(\bigvee^{24}S^4)\cong\mathbb Z^{24}\). Integral changes of bases of four-cell generators and five-cell attaching maps realize the Smith reduction homotopically, canceling the 21 unit pairs. The resulting homotopy type is \(\bigvee^3S^4\vee\bigvee^6S^5\).

## Verification
Run `python3 verify_c8_k4.py` using Python 3's standard library. It reconstructs the graph, enumerates every independent face, constructs and checks every matching pair, proves complete Hasse acyclicity, computes the integral Morse boundary, checks its exact rank and unimodular minor, and independently checks the face-vector Euler characteristic. The recorded successful run is `verification_output.txt`; the decisive output marker is `CYCLE8_K4_INTEGRAL_MORSE_VERIFIED`. See `VERIFICATION.md` for numerical counts and reproducibility limits.

## Relationship to prior work
Antolín Camarena and Carnero Bravo, *Homotopy type of the independence complex of some categorical products of graphs*, first publicly released on July 23, 2023, gives general restrictions for \(\operatorname{Ind}(C_m\times K_n)\) when \(m\) is not divisible by three: a possible wedge of spheres in neighboring degrees and Moore-space summands. Their Theorem 23 and Question 24 do not settle torsion-freeness or the exact ranks for the eight-cycle and four-color case. The paper mentions some calculations for the three-color eight-cycle, which is a different graph and does not imply this result. A later paper by Carnero Bravo, *On independence complexes of graph products* (2025), provides formulas when one categorical factor is a path, not the four-vertex complete graph considered here. The present claim is the precise integral homotopy type in this additional canonical case.

## Limitations
The theorem covers exactly \(C_8\times K_4\). No all-color or all-cycle-length recurrence is proved, and no equivariant homology representation or canonical suspension map to another cycle-product complex is claimed. The reproducible exhaustive discrete-Morse certificate is finite and proves this finite theorem; it does not decide the all-parameter torsion question. Published work could contain an equivalent result under alternate graph-product terminology; bibliographic searches cannot prove novelty absolutely.

## References
- O. Antolín Camarena and A. Carnero Bravo, *Homotopy type of the independence complex of some categorical products of graphs*, arXiv:2307.12401v1 (first public 2023-07-23), Theorem 23 and Question 24. https://arxiv.org/pdf/2307.12401
- A. Carnero Bravo, *On independence complexes of graph products*, arXiv:2505.06457v1 (first public 2025-05-09), Section 3. https://arxiv.org/pdf/2505.06457
- R. Forman, *Morse theory for cell complexes*, Adv. Math. 134 (1998), 90–145 (discrete Morse theorem).
