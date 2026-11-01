# Five-primary torsion and a Moore summand in the Paley-25 neighborhood complex

## Finding
Let \(P_{25}\) be the quadratic-residue Paley graph over \(\mathbb F_{25}\) and let \(X=\mathcal N(P_{25})\) be its ordinary Lovász **open-neighborhood complex**. Then there is an integral homotopy equivalence
\[
X\simeq M(\mathbb Z/5,3)\vee\bigvee^{205}S^3\vee\bigvee^{4}S^4,
\]
where \(M(\mathbb Z/5,3)\) denotes the mapping cone of the degree-\(5\) map \(S^3\to S^3\). Equivalently, the only nonzero reduced integral homology is
\[
\widetilde H_3(X;\mathbb Z)\cong\mathbb Z^{205}\oplus\mathbb Z/5,
\qquad
\widetilde H_4(X;\mathbb Z)\cong\mathbb Z^{4}.
\]
Although \(X\) is pure of simplicial dimension \(11\), it is not shellable. In particular, the fifth-prime torsion is intrinsic to the common-open-neighbor construction, and the complex is not an integral wedge of spheres.

## Assumptions and scope
Use the concrete model \(\mathbb F_{25}=\mathbb F_5[t]/(t^2-2)\); represent \(a+bt\), with \(0\le a,b\le4\), by the integer \(a+5b\). Distinct vertices \(x,y\) of \(P_{25}\) are adjacent precisely when \(y-x\) is a nonzero square in this field. The graph is strongly regular with parameters \((25,12,5,6)\), verified directly in the checker. The simplices of \(X\) are exactly the nonempty sets of graph vertices with a common **open** neighbor; loops and the witnessing neighbor itself are excluded. Its facets are the \(25\) distinct neighborhoods of cardinality \(12\), so it is pure eleven-dimensional. The claim is for this one finite complex, over integral coefficients, with no assertion for arbitrary Paley orders.

## Proof
**1. Enumeration.** For each of the \(25\) vertices, enumerate all nonempty subsets of its \(12\)-element open neighborhood and take their union as bit masks. The resulting face vector, in dimensions \(0\) through \(11\), is
\[
(25,300,2200,9475,18750,22950,19800,12375,5500,1650,300,25).
\]
There are \(93350\) nonempty faces. As a cross-check of the finite-field graph, the code independently obtains the published count of \(75\) four-cliques.

**2. Acyclic matching.** Start with all nonempty faces available. At each vertex label \(v=0,1,\dots,24\), pair every still-available face \(\sigma\) not containing \(v\) with \(\sigma\cup\{v\}\) if both remain available, and delete both. These disjoint pairs form an acyclic matching: the checker reverses every matched arrow in the whole Hasse diagram, keeps every other covering arrow downward, and checks that all \(93350\) vertices of this directed diagram are topologically sorted. Exactly \(583750\) covering incidences are tested. The \(46529\) pairs leave precisely one critical vertex, \(246\) critical three-faces and \(45\) critical four-faces, and no others.

**3. Integral Morse boundary.** Give each simplex the orientation of its increasing ordered vertex list. For each three-face \(\tau\) paired upward with a four-face \(U\), the relation in the reduced chain quotient is
\[
[\tau]=-\epsilon(\tau,U)\sum_{\eta\ne\tau}\epsilon(\eta,U)[\eta],
\]
where \(\epsilon(\eta,U)\in\{\pm1\}\) is the signed simplicial incidence. Recursively eliminate all upward-paired three-faces; three-faces paired downward to two-faces project to zero, and critical three-faces project to their basis vectors. Apply the resulting projection to the oriented boundaries of all critical four-faces. This gives an exact integer \(246\times45\) Morse boundary matrix with \(1051\) nonzero entries. Its nonzero Smith invariant factors are \(40\) copies of \(1\) and one copy of \(5\). Therefore its kernel is \(\mathbb Z^4\) and its cokernel is \(\mathbb Z^{205}\oplus\mathbb Z/5\). The Morse complex has no other nonzero reduced chain groups. This proves the complete reduced integral homology.

**4. Homotopy rather than just homology.** The discrete-Morse theorem replaces \(X\) by a CW complex having only a single zero-cell, \(246\) three-cells and \(45\) four-cells. The three-skeleton is a wedge of \(246\) copies of \(S^3\), and \(\pi_3\) of that wedge is \(\mathbb Z^{246}\), with maps classified by their integer degrees on the summands. Hence the exact Smith operations can be realized by homotopy-equivalences and changes of the four-cell attaching maps. The \(40\) unit entries give contractible sphere–cell pairs; the entry \(5\) yields \(M(\mathbb Z/5,3)\); the remaining cells are \(205\) free three-spheres and \(4\) free four-spheres. This proves the claimed homotopy equivalence. Because a pure shellable eleven-dimensional complex can have reduced homology only in dimension \(11\), nonzero degree-three homology also proves nonshellability.

## Verification
The provided `check_paley25.py` reconstructs the finite-field graph, face set, full oriented Hasse diagram, two exhaustive acyclic Morse matchings, and both signed Morse boundaries. It verifies the certificate `paley25_certificate.json` byte-for-byte; run `python3 check_paley25.py` in the directory containing both files (requires Python 3.10+ and SymPy). The first matching has \(246\) three-cells and \(45\) four-cells, with Smith factors \(1^{40},5\); a different even-then-odd vertex order gives \(237\) three-cells and \(36\) four-cells, with Smith factors \(1^{31},5\). Ranks of the first boundary over characteristics \(2,3,5,7,11\) are respectively \(41,41,40,41,41\), as an additional independent finite-field check. Both agree on integral homology; the Euler characteristic of the original face vector and the CW model is \(-200\).

## Relationship to prior work
Goryainov, Shalaginov and Yip study the same \(25\)-vertex Paley graph as \(\mathrm{GP}(25,2)\) in Example 6.5 of their 2022 preprint, including its \(75\) four-cliques. Their results concern maximal cliques and eigenfunctions, not the open-neighborhood complex. Shukla's 2018 classification treats graphs of maximum degree at most three and four-regular circulants, not this degree-twelve, noncyclic field-additive Cayley graph. Dochtermann and Singh's 2021 directed Hom-complex framework treats directed objects and does not supply this integral finite calculation. A separately indexed neighborhood-complex calculation for the seventeen-vertex Paley graph has different parameters and three-primary torsion; it does not imply this order-twenty-five, five-primary statement. Searches for the names, equivalent box/Hom terminology, Moore-space decomposition, finite-field parameters and potential broader theorems did not identify a covering result. This is evidence of originality, not a claim of exhaustive bibliographic uniqueness.

## Limitations
The homotopy classification does not determine the action of graph automorphisms on the integral homology, the homotopy type of natural quotients, integral persistence maps or a uniform theorem for larger Paley graphs. The calculation is reproducible from finite bit-mask enumeration and exact integer Smith reduction but is not an independent formal proof-assistant certification. A related unindexed classification could exist; the identified directly relevant source concerns cliques rather than neighborhood topology. No independent external audit has been performed.

## References
1. S. Goryainov, L. Shalaginov, C. H. Yip, *On eigenfunctions and maximal cliques of generalised Paley graphs of square order*, arXiv:2203.16081, first public 2022-03-30, especially definition in §1 and Example 6.5. https://arxiv.org/abs/2203.16081
2. S. Shukla, *Homotopy type of the neighborhood complexes of graphs of maximal degree at most 3 and 4-regular circulant graphs*, arXiv:1802.04526, first public 2018-02-13, §2. https://arxiv.org/abs/1802.04526
3. A. Dochtermann, A. Singh, *Homomorphism complexes, reconfiguration, and homotopy for directed graphs*, arXiv:2108.10948, first public 2021-08-24, introductory Hom/neighborhood relation. https://arxiv.org/abs/2108.10948
