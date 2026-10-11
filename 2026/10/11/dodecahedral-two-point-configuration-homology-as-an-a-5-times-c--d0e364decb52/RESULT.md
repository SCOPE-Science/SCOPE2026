# Dodecahedral two-point configuration homology as an \(A_5\times C_2\)-module
## Finding
Let \(D=G(10,2)\) be the dodecahedral graph, and let \(X=\operatorname{UConf}_2(D)\) be the unordered configuration space of two distinct points on \(D\). The full graph automorphism group is \(\operatorname{Aut}(D)\cong A_5\times C_2\). Let \(z\) denote the central involution, and let \(V_4,V_5,V_6\) be the rational irreducible \(A_5\)-modules of dimensions \(4,5,6\), with \(V_6\) the rational form obtained from the two complex \(3\)-dimensional irreducibles.

Then
\[
H_0(X;\mathbb Q)\cong\mathbb Q,\qquad \dim H_1(X;\mathbb Q)=12,\qquad \dim H_2(X;\mathbb Q)=36,
\]
and \(H_i(X;\mathbb Q)=0\) for \(i>2\). As an \(A_5\times C_2\)-module,
\[
H_1(X;\mathbb Q)\cong V_6^+\oplus(\mathbf 1\oplus V_5)^-,
\]
\[
H_2(X;\mathbb Q)\cong(V_4\oplus V_5\oplus V_6)^+\oplus(V_4\oplus V_5\oplus2V_6)^-,
\]
where \(+\) and \(-\) denote the \(+1\)- and \(-1\)-eigenspaces for \(z\).

Equivalently, on the rotational \(A_5\)-classes of orders \(1,2,3,5\), the \(H_1\)-character is \((12,0,0,2)\), while the character on their products with \(z\) is \((0,-4,0,0)\). The corresponding \(H_2\)-characters are \((36,-4,0,1)\) and \((-6,2,0,-1)\).

## Assumptions and scope
The graph \(D\) is the generalized Petersen graph \(G(10,2)\), with ten outer cycle edges, ten spokes, and ten inner step-two edges. The configuration space is unordered and contains exactly two particles. The calculation is over \(\mathbb Q\); no integral torsion statement is asserted.

The standard discretized two-particle cubical model applies because \(D\) is sufficiently subdivided for two points: distinct essential vertices are separated by at least one edge, and every nontrivial cycle has at least three edges. Thus the cubical model has the homotopy type of \(X\).

## Proof
The unordered discretized configuration complex has one cell for every unordered pair of disjoint open cells of \(D\). Its cell counts are
\[
(c_0,c_1,c_2)=(190,540,375).
\]
The one-skeleton is connected, hence the first cellular boundary has rank \(189\). For the second boundary \(\partial_2:C_2\to C_1\), the supplied certificate contains \(36\) integral kernel vectors whose distinguished coordinates form the identity matrix, proving \(\dim_{\mathbb Q}\ker\partial_2\ge36\) and therefore \(\operatorname{rank}_{\mathbb Q}\partial_2\le339\). Independently, row reduction over \(\mathbb F_2\) gives rank \(339\), which is a lower bound for the rational rank. Hence
\[
\operatorname{rank}_{\mathbb Q}\partial_2=339.
\]
The stated Betti numbers follow immediately.

Every graph automorphism acts cellularly on this cubical model. Exhaustive enumeration gives \(120\) automorphisms. The parity of the induced permutation of the thirty graph edges cuts out a subgroup of order \(60\), the rotational \(A_5\), while the unique nonidentity central automorphism \(z\) gives the complementary coset. The rotational class counts by orders \(1,2,3,5\) are \(1,15,20,24\).

For each automorphism, the signed action on oriented cells gives cellular traces. The integral \(36\)-cycle certificate is in normalized free-coordinate form, so the trace on \(H_2\) is read exactly from the transformed basis vectors. The \(H_1\)-trace is then obtained from the Lefschetz identity
\[
\operatorname{tr}(g\mid H_0)-\operatorname{tr}(g\mid H_1)+\operatorname{tr}(g\mid H_2)
=
\operatorname{tr}(g\mid C_0)-\operatorname{tr}(g\mid C_1)+\operatorname{tr}(g\mid C_2).
\]
This yields the two character rows in the finding.

For the rational \(A_5\)-irreducibles on the merged classes of orders \(1,2,3,5\), the characters of \(V_4,V_5,V_6\) are respectively \((4,0,1,-1)\), \((5,1,-1,0)\), and \((6,-2,0,1)\). Splitting each homology character into the \(z\)-eigenspaces gives \((6,-2,0,1)\) and \((6,2,0,1)\) in degree one, and \((15,-1,0,0)\) and \((21,-3,0,1)\) in degree two. These decompose exactly as claimed.

## Verification
Running `python verifier.py` reconstructs \(G(10,2)\), its two-particle discrete configuration complex, both boundary ranks, all \(120\) graph automorphisms, the class partition, the signed cellular actions, the homology characters, and the irreducible decompositions. The accompanying `kernel_certificate.json` supplies the integral \(H_2\)-cycle basis used for the exact rank upper bound and exact trace calculation. The recorded replay output is in `verifier_output.txt`.

## Relationship to prior work
Agarwal, Banks, Gadish, and Miyata develop deletion and contraction maps for graph configuration spaces and emphasize naturality with respect to graph automorphisms; their first public version is arXiv:2005.13666, dated 2020-05-27, with primary MSC 55R80. Their framework motivates extracting automorphism-sensitive homology data but does not compute the dodecahedral two-particle representation.

An and Knudsen determine structural generators for second homology of planar graph braid groups in arXiv:2008.10371. Their theorem is broader at the generator level, but it neither identifies the dodecahedral \(H_2\)-module nor gives its full automorphism character. Bibby, Chan, Gadish, and Yun study homology representations for compactified graph configuration spaces in arXiv:2109.03302, with different spaces and symmetry actions; their paper contains no dodecahedral specialization. The earlier chain-model work arXiv:1708.02351 supplies functorial computational infrastructure but not this representation.

Targeted database and web searches under dodecahedral, dodecahedron, graph braid group, unordered two-point configuration, automorphism representation, and \(A_5\times C_2\) aliases found no statement implying the character or decomposition above. The closest indexed dodecahedral findings concern matching and independence complexes, which are different spaces and do not imply configuration-space homology.

## Limitations
The result is specific to two unordered particles on the dodecahedral graph and to rational homology. It does not claim an integral \(A_5\times C_2\)-lattice decomposition, a presentation of the graph braid group, or a uniform formula for other Platonic graphs. The originality comparison cannot exclude unindexed or inaccessible specialized computations, although the most directly relevant configuration-space and representation papers were inspected.

## References
1. S. Agarwal, M. Banks, N. Gadish, and D. Miyata, *Deletion and contraction in configuration spaces of graphs*, arXiv:2005.13666.
2. B. H. An and B. Knudsen, *On the second homology of planar graph braid groups*, arXiv:2008.10371.
3. C. Bibby, M. Chan, N. Gadish, and C. H. Yun, *Homology representations of compactified configurations on graphs applied to \(\mathcal M_{2,n}\)*, arXiv:2109.03302.
4. B. H. An, G. C. Drummond-Cole, and B. Knudsen, *Subdivisional spaces and graph braid groups*, arXiv:1708.02351.
