# Thirty-eight four-spheres in the order-three partial Latin-square complex

## Finding
Let \(\mathcal P_3\) be the abstract simplicial complex on the 27 assignments \((r,c,s)\in\{0,1,2\}^3\). A set of assignments is a face if any two distinct assignments differ in at least two coordinates. Thus the faces are exactly the partial Latin squares of order three, ordered by containment, and \(\mathcal P_3=\operatorname{Ind}(H(3,3))\) for the Hamming graph with edges at Hamming distance one.

Then the **integral homotopy type** is
\[
\boxed{\mathcal P_3\simeq\bigvee^{38}S^4.}
\]
The full face-count vector, including the empty face and indexed by cardinality zero through nine, is
\[
(1,27,270,1278,3078,3834,2412,756,108,12).
\]
The inclusion-maximal faces consist of 54 five-entry partial Latin squares, 324 seven-entry partial Latin squares, and the 12 complete nine-entry Latin squares. In particular, this complex is nonpure and eight-dimensional, but its nontrivial reduced integral homology lies only in degree four, with rank 38.

## Assumptions and scope
The symbols, rows and columns are all individually labelled \(0,1,2\); faces are sets, not ordered lists. A face is compatible precisely when no two different assignments agree in two coordinate positions. The empty face is included for combinatorial enumeration but omitted from the ordinary geometric realization. The statement concerns this single finite complex, not all orders or the trade-space complex of a fixed Latin square.

Number the 27 assignments by \(v=9r+3c+s\) and represent each face by the integer bit mask \(\sum_{v\in F}2^v\). All calculations below use these deterministic labels and the increasing vertex order to orient simplices.

## Proof
**1. Complete face enumeration.** Start with the empty mask, then recursively adjoin increasing eligible vertices. Exclude a candidate vertex if it shares two coordinates with any vertex already selected. As every finite face has a unique increasing listing, the procedure enumerates all faces exactly once. Counting gives 11,776 faces including the empty face and the face vector above. A face is maximal exactly when none of the 27 single-vertex extensions is present; exhaustive comparison gives the three facet counts stated above.

**2. An explicit acyclic matching.** Maintain the set of unmatched face masks. In increasing order \(v=0,\ldots,26\), pair every available mask \(F\) omitting \(v\) with \(F\cup\{v\}\), provided both remain unmatched. The two masks are then removed before the next matching operation. This matches 5,868 pairs if the empty face is allowed. Unpair the pair \((\varnothing,\{0\})\), leaving 5,867 nonempty face pairs and one critical vertex. The remaining critical faces consist of one 3-simplex and 39 4-simplices. There are no other nonempty critical faces.

To certify acyclicity, orient every covering relation of the complete 11,776-element face poset from lower face to upper face except that a matched edge is reversed. The exact exhaustive topological-sort checker processes all 11,776 vertices of this directed graph, containing 56,619 covering edges. Hence it has no directed cycle, establishing a valid discrete-Morse matching. The empty face has no matched edge and can equivalently be omitted from this acyclicity test.

**3. Integral Morse differential.** The resulting Morse CW complex has one 0-cell, one 3-cell, and 39 4-cells. There are no 1- or 2-cells. For an oriented 3-face \(a\), let \(p(a)\in\mathbb Z\) be its coefficient when projected onto the single critical 3-cell. Set \(p(a)=1\) on the critical 3-face, \(p(a)=0\) when \(a\) is the upper member of a matched \((2,3)\)-pair, and for \(a\) paired upward with a 4-face \(b\), use the signed recurrence
\[
p(a)=-\frac{1}{[b:a]}\sum_{a'\ne a}[b:a']\,p(a'),
\]
where \([b:a]\in\{\pm1\}\) is the simplicial incidence coefficient. The acyclic matching makes the recurrence well-founded. Applying \(p\) to the oriented boundary of each of the 39 critical 4-faces yields 23 zero, nine \(+1\), and seven \(-1\) attaching degrees. In particular, the unique integral Morse boundary \(\mathbb Z^{39}\to\mathbb Z\) is primitive: its nonzero entries have gcd one.

**4. Homotopy conclusion.** The 3-skeleton of the Morse CW complex is \(S^3\). Its 39 4-cells are attached by maps \(S^3\to S^3\), hence are classified by their integer degrees. Elementary integral changes of basis among the 4-cell attaching maps take a primitive degree vector to \((1,0,\ldots,0)\). The degree-one 4-cell fills the 3-sphere, leaving 38 independent 4-spheres. This is a homotopy statement, not an inference from finite-field Betti numbers. Consequently \(\mathcal P_3\simeq\bigvee^{38}S^4\), proving the result.

## Verification
Execute `python3 verify_latin3.py` using only the Python standard library. The program independently regenerates every face, counts maximal faces, builds the deterministic matching, checks acyclicity by a complete directed-graph topological sort, and computes all 39 signed critical attaching degrees by exact integer recursion. It verifies their distribution \((-1:7,\ 0:23,\ +1:9)\) and gcd one. An independent mod-two boundary reduction checks the expected rank vector \((1,26,244,1034,2044,1752,660,96,12)\) in cardinality degrees one through nine. The final success marker is `VERIFY_OK_LATIN3_PARTIAL_SQUARE_HOMOTOPY`.

## Relationship to prior work
Falcón, *The set of autotopisms of partial Latin squares* (arXiv:1107.3248v1, 2011), gives the triple representation, isotopism symmetries, and counts of partial Latin squares fixed by given permutations. Its full-text statements address counting and completable partial squares, not the homotopy of the complex containing **all** partial Latin squares as faces.

Hämäläinen, *Latin trades and simplicial complexes* (arXiv:0907.1481v1, 2009), computes homology for a different construction: the trade-intersection complex attached to a *fixed* Latin square. That work's order-three back-circulant trade-space homology is not a homology computation for \(\mathcal P_3\). Also, the Vietoris–Rips construction on \(H(3,3)\), and the independence complex of the categorical product \(K_3\times K_3\times K_3\), have different simplex rules from \(\operatorname{Ind}(H(3,3))\); their existing homotopy computations cannot imply the present result.

## Limitations
The statement is confined to order three; it gives neither an all-order formula nor an equivariant homology representation. The acyclic matching and integer attaching-degree certificate are finite and complete for this complex. Originality comparisons cover indexed records and the materially inspected relevant primary literature, but cannot exclude an unindexed equivalent computation. No independent scientific audit is represented here.

## References
1. R. M. Falcón, *The set of autotopisms of partial Latin squares*, arXiv:1107.3248v1 (first submitted 2011-07-16), https://arxiv.org/html/1107.3248v1.
2. C. Hämäläinen, *Latin trades and simplicial complexes*, arXiv:0907.1481v1 (first submitted 2009-07-09), https://arxiv.org/html/0907.1481v1.
3. R. Forman, *Morse theory for cell complexes*, Adv. Math. 134 (1998), 90–145. General discrete-Morse framework, used only as methodological background.
