# Sharp dual mutual-visibility colorings of the four- and five-dimensional cubes
## Finding
Write \(Q_d\) for the binary hypercube on \(\{0,1\}^{d}\), and \(\chi_{\mu_{\mathrm d}}\) for the chromatic number whose color classes must each be dual mutual-visibility sets. The sharp first higher-dimensional values include
\[
\chi_{\mu_{\mathrm d}}(Q_3)=\chi_{\mu_{\mathrm d}}(Q_4)=2,
\qquad
\chi_{\mu_{\mathrm d}}(Q_5)=4.
\]
In addition, there are exactly \(24\) labeled two-colorings of \(Q_4\) (color labels distinguished), or \(12\) unordered bipartitions. All \(24\) colorings are in one orbit under automorphisms of \(Q_4\); both classes have eight vertices and are invariant under the antipodal map \(x\mapsto x\oplus(1,1,1,1)\). For completeness, the corresponding value on \(Q_2\) is also \(2\), while \(Q_1\) is complete and has value \(1\).

## Assumptions and scope
All graphs are finite, simple, connected, and undirected. A vertex pair \(u,v\) is \(M\)-visible if some shortest \(u,v\)-path has no internal vertex in \(M\). A vertex set \(M\) is *dual mutual-visible* when this holds for every pair both in \(M\), and for every pair both in \(V(G)\setminus M\). A dual mutual-visibility coloring partitions all vertices into nonempty dual mutual-visible sets; \(\chi_{\mu_{\mathrm d}}(G)\) is its minimum number of classes. Binary vertices are represented by integers whose four low binary digits are the coordinates of \(Q_4\); \(x\oplus y\) is bitwise XOR. There is no claim about the exact values for dimensions at least six.

## Proof
**Complete four-cube classification.** A two-coloring is determined by a subset \(M\subseteq\{0,\ldots,15\}\), with the other class its complement. For each pair \(a<b\), put \(J(a,b)=\{i: a_i\ne b_i\}\). Every shortest path from \(a\) to \(b\) flips exactly the coordinates in \(J(a,b)\), once each, in one of their \(|J(a,b)|!\) possible orders. Consequently, both classes are dual precisely when, for every one of those classes \(S\), every pair lying either both in \(S\) or both outside \(S\) has at least one coordinate-flip order whose intermediate vertices avoid \(S\).

The attached `verify.py` constructs these internal-vertex masks, tests this explicit criterion on every one of the \(2^{16}=65536\) subsets, and obtains precisely \(24\) solutions. It checks that each has eight vertices and is antipodally invariant. It also enumerates the images of one solution under all coordinate permutations and coordinate flips, obtaining precisely the same \(24\)-element collection. An independently implemented restricted-graph breadth-first search rechecks that every enumerated coloring is dual. This is an exhaustive finite proof: the enumerated binary masks are all possible labeled two-colorings, and the coordinate-flip orders are all possible geodesics. One explicit solution is
\[
M=\{0,4,6,7,8,9,11,15\},\quad
V(Q_4)\setminus M=\{1,2,3,5,10,12,13,14\}.
\]
Thus \(Q_4\) admits two colors and has the stated complete two-coloring classification. Since \(Q_4\) is not complete, one color is impossible. Direct witnesses using bitmask `23` on \(Q_3\) and bitmask `3` on \(Q_2\) are independently checked in the same verifier; noncompleteness again excludes one color.

**Face-extension lemma.** Suppose \(H\) is one coordinate hyperface of \(Q_{d+1}\), isomorphic to \(Q_d\), and \(M\subseteq V(H)\) is dual mutual-visible in \(H\). Then \(M\) is dual mutual-visible in the ambient \(Q_{d+1}\). Indeed, geodesics joining two vertices of \(H\) stay in \(H\), and pairs both in \(M\) or both in \(H\setminus M\) are handled by the assumed property. Pairs in the opposite hyperface have a geodesic entirely there. For a pair with one endpoint \(a\in H\setminus M\) and the other \(b\) in the opposite face, first cross from \(a\) to its coordinate-flipped neighbor in the opposite face, and complete a geodesic there; all its internal vertices avoid \(M\). The resulting path has minimum Hamming length. These exhaust the outside pairs. Hence every color class of a dual coloring on \(Q_d\), considered separately in either hyperface, remains dual in \(Q_{d+1}\), giving
\[
\chi_{\mu_{\mathrm d}}(Q_{d+1})\leq 2\chi_{\mu_{\mathrm d}}(Q_d)
\]
whenever the right-hand side is finite.

**Five-cube exact value.** Apply this lemma to the preceding \(Q_4\) two-coloring in each of the two opposite four-faces of \(Q_5\). It yields four dual color classes, each of eight vertices, and therefore \(\chi_{\mu_{\mathrm d}}(Q_5)\leq4\). The attached verifier independently checks all four classes directly in \(Q_5\) by breadth-first search.

For the opposite inequality, Korže and Vesel's Theorem 3.14 [2] establishes \(\mu_{\mathrm d}(Q_5)=10\), where \(\mu_{\mathrm d}\) is the maximum cardinality of a dual mutual-visibility set. Since \(Q_5\) has \(32\) vertices, a coloring with at most three classes would cover at most \(3\cdot10=30\) vertices, a contradiction. Hence \(\chi_{\mu_{\mathrm d}}(Q_5)\geq4\). Combining both inequalities proves the asserted exact value. The lower bound is explicitly a consequence of the earlier published size theorem; the contribution here is the matching coloring, the exact coloring conclusion, and the complete four-cube coloring classification.

## Verification
Execute `python3 verify.py` with the Python standard library. The accompanying `verification_output.txt` is the exact captured output. The program enumerates all \(65536\) four-cube colorings using complete shortest-path coordinate permutations, independently rechecks the \(24\) accepted masks by shortest-path breadth-first search, verifies antipodal invariance and a single automorphism orbit, and independently tests explicit dual two-colorings in dimensions two to four and a four-coloring in dimension five. The published \(\mu_{\mathrm d}(Q_5)=10\) bound is quoted as an existing theorem and is not independently recomputed here.

## Relationship to prior work
Babu, Jakovac, Kuziak, Lakshmanan S., and Yero [1] introduce dual mutual-visibility *coloring*, solve the two-factor Hamming graphs, and explicitly ask for higher-dimensional Hamming graphs, particularly hypercubes (Section 7). Their solved two-factor results imply the \(Q_2\) value, but not the higher-dimensional exact values or the enumerated four-cube classification.

Korže and Vesel [2] study dual mutual-visibility *set cardinalities*, proving \(\mu_{\mathrm d}(Q_4)=8\) and \(\mu_{\mathrm d}(Q_5)=10\), and display one optimal four-cube dual set. Their \(Q_5\) result supplies exactly the lower bound used above. Cardinality maxima do not themselves give a partition, count partition colorings, or prove one orbit. The restrictions of dual sets to convex subgraphs were developed by Bujtás, Klavžar, and Tian [3]; this is compatible with, but does not imply, the face-extension construction in the opposite direction. Axenovich and Liu [4] study **ordinary** mutual-visibility coloring in hypercubes, a weaker color-class property, and its asymptotic bounds do not fix the dual coloring values here.

## Limitations
The \(Q_4\) classification uses an explicit, complete finite search whose implementation and independent geodesic check are provided; it is not a symbolic classification proof without computation. The \(Q_5\) lower bound depends on the published exact size theorem of Korže and Vesel, based in their work on integer programming and SAT; the present package does not independently replay their optimization proof. Dimensions six and higher, higher-arity Hamming graphs, and additional chromatic variants remain outside the claimed result. No claim of exhaustive global literature novelty or independent external audit is made.

## References
1. S. Babu, M. Jakovac, D. Kuziak, A. Lakshmanan S., I. G. Yero, *A variety of the mutual-visibility coloring problem for graphs*, arXiv:2609.31427v1 (25 September 2026), https://arxiv.org/html/2609.31427v1.
2. D. Korže, A. Vesel, *Variety of mutual-visibility problems in hypercubes*, arXiv:2405.05650v1 (9 May 2024), Theorem 3.14, https://arxiv.org/pdf/2405.05650.
3. C. Bujtás, S. Klavžar, J. Tian, *Visibility polynomials, dual visibility spectrum, and characterization of total mutual-visibility sets*, arXiv:2412.03066, Lemma 2.4, https://link.springer.com/article/10.1007/s00010-025-01197-y.
4. M. Axenovich, D. Liu, *A note on the mutual-visibility coloring of hypercubes*, arXiv:2411.12124v3, https://arxiv.org/pdf/2411.12124.
