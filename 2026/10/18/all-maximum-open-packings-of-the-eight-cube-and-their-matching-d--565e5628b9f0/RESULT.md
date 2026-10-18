# All maximum open packings of the eight-cube and their matching-direction profiles

## Finding

Let \(Q_8\) have vertex set \(\mathbb F_2^8\), with two vertices adjacent when they differ in one coordinate. An **open packing** is a vertex subset \(S\) such that the open neighborhoods of distinct vertices of \(S\) are disjoint. Every maximum open packing of \(Q_8\) contains \(32\) vertices. **Exactly \(57\,600\) labeled subsets attain this maximum.**

For each such subset, the induced graph \(Q_8[S]\) is a perfect matching of \(16\) edges. Count its edges in each of the eight coordinate directions and sort the eight counts in nonincreasing order. The possible profiles, and the numbers of maximum open packings realizing them, are exactly

| Matching-direction profile | Number of maximum open packings |
| --- | ---: |
| \((16,0,0,0,0,0,0,0)\) | \(1\,920\) |
| \((8,8,0,0,0,0,0,0)\) | \(13\,440\) |
| \((4,4,4,4,0,0,0,0)\) | \(26\,880\) |
| \((2,2,2,2,2,2,2,2)\) | \(15\,360\) |

Every maximum open packing has a **unique decomposition into an ordered pair of binary length-seven 1-perfect codes**, as made precise below. In particular, exactly \(1\,920\) of the \(57\,600\) optimal subsets are unions of both vertices over the members of a length-seven 1-perfect code in one fixed coordinate direction. The remaining \(55\,680\) optimal subsets are not of that fiber form in any coordinate direction.

## Assumptions and scope

The vertex labels of \(Q_8\) are fixed: distinct subsets of the labeled set \(\mathbb F_2^8\) are counted separately; graph automorphism orbits are **not** being counted. A binary length-seven **1-perfect code** means a subset \(A\subset\mathbb F_2^7\) of \(16\) words whose radius-one Hamming balls partition \(\mathbb F_2^7\). A Fano plane is a collection of seven triples on seven points in which each unordered pair occurs exactly once. All distances and neighborhoods are those in the corresponding hypercubes.

For \(u\in\mathbb F_2^7\), let \(p(u)\in\mathbb F_2\) be the sum of its seven coordinates modulo two, and define \(E_\epsilon(u)=(u,p(u)+\epsilon)\) for \(\epsilon\in\{0,1\}\). Thus \(E_0\) and \(E_1\) are bijections from \(\mathbb F_2^7\) to the even and odd halves of the eight-cube, respectively.

## Proof

**1. Independent halves.** Every vertex of \(Q_8\) has eight neighbors. If \(S\) is an open packing, its even vertices have pairwise-disjoint eight-element open neighborhoods within the \(128\) odd vertices. Hence at most \(16\) even vertices belong to \(S\). The same argument gives at most \(16\) odd vertices, so \(|S|\le32\).

For distinct words \(u,v\) of length seven, the distance between \(E_\epsilon(u)\) and \(E_\epsilon(v)\) is \(d(u,v)\) when \(d(u,v)\) is even and \(d(u,v)+1\) when it is odd. Their open neighborhoods intersect precisely when that distance equals two, or equivalently when \(d(u,v)\in\{1,2\}\). Thus an even-side subset \(E_0(A)\) has disjoint open neighborhoods exactly when \(A\) has minimum distance at least three; likewise for the odd side. The open neighborhoods of vertices of opposite parity lie in disjoint parity classes, so there are no cross-side conflicts.

If \(|S|=32\), both sides have size \(16\). The disjoint closed radius-one balls around the corresponding length-seven codewords each contain eight words; hence they partition all \(128\) words, and the codes are 1-perfect. Conversely, any ordered pair \((A,B)\) of binary length-seven 1-perfect codes yields the maximum open packing
\[
S(A,B)=E_0(A)\cup E_1(B).
\]
The parity halves recover \(A\) and \(B\) uniquely. Standard Hamming parity-check constructions prove existence of these codes, and therefore \(\rho^\mathrm{o}(Q_8)=32\).

**2. The \(240\) labeled length-seven 1-perfect codes.** Translate any such code so that it contains the zero word. It cannot have words of weights one or two. Every weight-two word lies at distance one from exactly one weight-three codeword; since a weight-three word contains exactly three weight-two words, there must be seven weight-three codewords. Their supports are the seven triples of a Fano plane.

A weight-four codeword must contain no Fano triple, else its distance from the corresponding weight-three codeword would be one. Exactly seven four-subsets avoid Fano lines: of the \(35\) four-subsets, precisely \(7\cdot4=28\) contain a line, and no four-subset contains two lines because any two Fano lines meet. The seven permissible four-subsets are the complements of the Fano lines, and all must be codewords, since the other \(28\) weight-three vectors need unique weight-four code neighbors, four per word.

A weight-five vector is within distance one of a forced weight-four codeword: its missing two coordinates lie on a Fano line, whose complement is at distance one. A weight-six vector is at distance two from the complement of a Fano line through its missing coordinate. Thus the remaining sixteenth codeword is the all-one word. The entire zero-containing code is forced by the seven Fano triples. Conversely, identifying the seven coordinates with the nonzero vectors of \(\mathbb F_2^3\) produces exactly such a code as the kernel of a three-row Hamming parity-check matrix, so it is linear.

The Fano plane is the unique Steiner triple system of order seven up to relabeling. Indeed, fixing one line and using the three pairings of its four exterior points forces the other six lines. Its automorphism group is \(\operatorname{GL}(3,2)\) of order \(7\cdot6\cdot4=168\). There are therefore \(7!/168=30\) labeled Fano planes, hence \(30\) different linear length-seven Hamming codes containing zero. Every one has eight distinct cosets. All labeled 1-perfect codes are such cosets, giving \(30\cdot8=240\) codes. The ordered-pair classification now counts \(240^2=57\,600\) maximum open packings.

**3. The induced matching.** Fix 1-perfect codes \(A,B\). For each \(a\in A\), exactly one \(b\in B\) satisfies \(d(a,b)\le1\). If \(a=b\), the corresponding vertices \(E_0(a),E_1(b)\) differ in the eighth coordinate. If \(a\) and \(b\) differ in coordinate \(i\le7\), their lifted vertices differ only in coordinate \(i\). This gives each vertex of \(E_0(A)\) exactly one neighbor in \(E_1(B)\); the symmetric perfect-code property gives each vertex of \(E_1(B)\) exactly one neighbor in \(E_0(A)\). There are no edges within one parity half, so the induced graph is a perfect matching of \(16\) edges.

Write \(A=a+U\) and \(B=b+V\), where \(U,V\) are dimension-four linear Hamming codes, and put \(d=\dim(U\cap V)\). For each coordinate \(i\le7\), the number of matching edges parallel to coordinate \(i\) is \(|A\cap(B+e_i)|\), and the number parallel to coordinate eight is \(|A\cap B|\). Each of these eight intersections is either empty or an affine coset of \(U\cap V\) of cardinality \(2^d\). Since the matching has \(16\) edges, precisely \(2^{4-d}\) directions have \(2^d\) edges each.

**4. Distribution of the intersection dimensions.** Fix one Fano plane \(F\) and let \(r\) denote the number of triples common to \(F\) and a second labeled Fano plane \(F'\). The corresponding Hamming codes intersect in exactly their zero word, their all-one word, the \(r\) common weight-three words, and the \(r\) complementary weight-four words. Consequently \(2^d=2+2r\), which forces \(r\in\{0,1,3,7\}\) and \(d\in\{1,2,3,4\}\).

Let \(n_r\) count the possible \(F'\) for a fixed \(F\). Exactly six of the \(30\) labeled Fano planes contain any specified triple, by counting \(30\cdot7\) incidences across \(35\) triples. Exactly two contain any specified pair of intersecting triples, by counting \(30\binom72\) incidences across the \(315\) unordered pairs of triples meeting at one point. All Fano-line pairs meet once. Together with \(n_7=1\), these facts give
\[
\sum_r n_r=30,\qquad \sum_r r n_r=42,\qquad
\sum_r\binom r2 n_r=42,\qquad n_7=1.
\]
Solving gives \((n_7,n_3,n_1,n_0)=(1,7,14,8)\), corresponding to \(d=(4,3,2,1)\). Fixing \(A\), each of the \(30\) underlying choices of \(V\) has eight affine cosets available as \(B\), and every profile is invariant under translations and coordinate permutations of \(A\). Thus multiplying the counts of Hamming spaces by \(8\) and then by the \(240\) choices of \(A\) gives respectively
\[
240\cdot8(1,7,14,8)
=(1920,13440,26880,15360).
\]
These are exactly the four profile counts in the statement. A matching consisting entirely of edges in one coordinate direction yields exactly a doubled code fiber and conversely. Therefore the fiber count is \(1920\) and the other \(57600-1920=55680\) are not fibers in any direction. This completes the proof.

## Verification

The included standard-library script `verify.py` enumerates all \(30\) labeled Fano planes by exact pair covering; constructs all \(240\) length-seven perfect codes; separately reconstructs the \(30\) linear Hamming codes using all coordinate permutations of a parity-check code; and verifies the common-line distribution. For one fixed code \(A\), it checks all \(240\) choices of \(B\), explicitly builds the lifted \(32\)-vertex sets, tests disjointness of all open neighborhoods, reconstructs all \(16\) matching edges, and checks their direction profiles. These checks reproduce the asserted four counts after multiplication by the **mathematically proved** transitivity factor \(240\). It does not exhaust arbitrary subsets of the \(256\)-vertex cube; the completeness and the multiplication factor are proven above rather than inferred from the experiment. Run `python3 verify.py` to reproduce `verification_output.txt` and the final `VERIFY_OK` marker.

## Relationship to prior work

Brešar, Klavžar and Rall determine \(\rho^\mathrm{o}(Q_8)=32\) and establish the bipartite-prism relation \(\rho^\mathrm{o}(G\square K_2)=2\rho_2(G)\), as well as a transformation to a product-form optimizer; these earlier facts do **not** count all maximizing subsets or classify the matching-direction vectors of every optimizer. In particular, existence of a product-form optimum does not assert that all optima are product-form. The present result resolves the complete labeled extremizer census and the directional profile distribution, not the previously known scalar optimum. Brešar, Samadi and Yero study injective colorings and perfect injective colorability of hypercubes, but the inspected hypercube section determines neither the labeled extremizer census nor its matching-direction profiles. The uniqueness of the order-seven Fano plane and the Hamming code construction are classical inputs rather than new claims.

## Limitations

This theorem concerns labeled subsets in \(Q_8\) only; it neither classifies optimal packings of cubes in other dimensions nor classifies automorphism orbits of the \(57\,600\) subsets. The four counts do not enumerate distinct injective colorings of the whole cube. Code enumeration and finite verification supplement, but do not replace, the proof. Overlap with unindexed or differently formulated historical coding-theory classifications remains possible.

## References

1. B. Brešar, S. Klavžar and D. F. Rall, *Packings in bipartite prisms and hypercubes*, arXiv:2309.04963v1 (first submitted 10 September 2023), especially Theorem 2.2, Section 4 and the \(Q_8\) entry of Table 1. https://arxiv.org/abs/2309.04963
2. B. Brešar, B. Samadi and I. G. Yero, *Injective coloring of graphs revisited*, arXiv:2106.09823v2 (first submitted 17 June 2021), especially Section 4 and Theorem 19. https://arxiv.org/abs/2106.09823
3. Classical order-seven Steiner triple-system uniqueness and the binary \((7,16,3)\) Hamming code; elementary arguments and an independent finite enumeration are included above.
