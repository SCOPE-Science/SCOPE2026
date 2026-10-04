# Exact binary length-\(6\) palindromic duplication and deletion optima: \(40\) versus \(42\)
## Finding
For binary words of length \(6\), with palindromic blocks of length \(2\), the largest code correcting one palindromic duplication has cardinality \(40\), whereas the largest code correcting one palindromic deletion has cardinality \(42\). Thus the two correction problems have different finite optima at the same natural parameter where their nonequivalence was originally illustrated.

## Assumptions and scope
Let \(x=u v w\) with \(|v|=2\). A length-\(2\) palindromic duplication replaces \(u v w\) by \(u v v^{\mathrm R}w\). A length-\(2\) palindromic deletion is the inverse operation on a factor \(v v^{\mathrm R}\), replacing \(u v v^{\mathrm R}w\) by \(u v w\). The alphabet is \(\{0,1\}\), every codeword has length \(6\), and exactly one such duplication or deletion is allowed, with the no-error case included in the usual radius-one sphere. Because a duplication output has length \(8\) and a deletion output has length \(4\), intersections between spheres of distinct length-\(6\) codewords are determined entirely by equality of their one-error descendants.

For each length-\(6\) word \(x\), let \(D_{\mathrm{dup}}(x)\) be its set of distinct one-step palindromic-duplication descendants and let \(D_{\mathrm{del}}(x)\) be its set of distinct one-step palindromic-deletion descendants. Define conflict graphs \(G_{\mathrm{dup}}\) and \(G_{\mathrm{del}}\) on the \(64\) binary length-\(6\) words by joining distinct \(x,y\) exactly when the corresponding descendant sets intersect. A correcting code is exactly an independent set in the relevant graph.

## Proof
The file `certificates.json` contains explicit lower and upper certificates.

For duplication, the listed set `duplication_lower_witness` has \(40\) words. Direct reconstruction of all one-step descendants shows that no two listed words have a common duplication descendant, so \(\alpha(G_{\mathrm{dup}})\ge 40\). For the upper bound, `duplication_upper_pairs` gives \(24\) pairwise vertex-disjoint edges of \(G_{\mathrm{dup}}\). Any independent set contains at most one endpoint from each of these \(24\) pairs and at most all \(16\) remaining vertices. Hence
\[
\alpha(G_{\mathrm{dup}})\le 24+16=40.
\]
Therefore \(\alpha(G_{\mathrm{dup}})=40\).

For deletion, the listed set `deletion_lower_witness` has \(42\) words and is directly checked to be independent, so \(\alpha(G_{\mathrm{del}})\ge 42\). For the upper bound, the certificate partitions \(36\) vertices into eight disjoint conflict triangles and six disjoint conflict edges; the other \(28\) vertices are singletons. Any independent set contains at most one vertex from each triangle, at most one from each edge, and at most every singleton. Thus
\[
\alpha(G_{\mathrm{del}})\le 8+6+28=42.
\]
Therefore \(\alpha(G_{\mathrm{del}})=42\).

The two exact optima are consequently different: \(40<42\).

## Verification
Running `python verify.py` reconstructs every one-step descendant from the channel definition. It constructs each conflict graph twice: first by pairwise intersection of descendant sets and second by grouping source words by a common output and recovering all induced conflict pairs. The two constructions are asserted equal.

The same verifier checks that \(G_{\mathrm{dup}}\) has \(56\) edges and \(G_{\mathrm{del}}\) has \(34\) edges; verifies both lower-witness codes; checks every certified upper-bound pair and triangle; verifies disjointness of all upper-bound blocks; and recomputes the unmatched singleton counts. The replay terminates with `VERIFY_OK`.

## Relationship to prior work
Lenz, Wachter-Zeh, and Yaakobi introduced the fixed-length palindromic duplication/deletion framework used here and showed that, unlike tandem duplication and deletion, palindromic duplication correction and palindromic deletion correction are not equivalent. Their two explicit counterexamples use binary length-\(6\) words with duplication length \(2\), making this finite parameter a natural place to ask for the exact optima. Their paper derives sphere-size formulas and generalized sphere-packing bounds, but the inspected text does not state the two exact cardinalities proved here.

Yohananov and Schwartz later studied palindromic duplication codes for an arbitrary number of errors. Their full text states that for finite error count the optimal code size remains an open direction in general. Sun and Ge subsequently gave asymptotic constructions and bounds for palindromic/reverse-complement duplication correction; the inspected full text contains no binary length-\(6\), length-\(2\) exact optimum of \(40\), and it does not address the paired deletion optimum \(42\).

## Limitations
The result is exact only for the binary alphabet, source length \(6\), palindromic block length \(2\), and one error. It does not classify all optimal codes, give a formula for other block lengths, or compare asymptotic rates. The originality search found no inspected publication or research record stating these two exact values, but an unindexed finite computation or unpublished table remains a residual risk.

## References
1. A. Lenz, A. Wachter-Zeh, and E. Yaakobi, “Bounds on Codes Correcting Tandem and Palindromic Duplications,” arXiv:1707.00052v1, first public version 2017-06-30.
2. L. Yohananov and M. Schwartz, “On the Coding Capacity of Reverse-Complement and Palindromic Duplication-Correcting Codes,” arXiv:2312.00394v1, 2023.
3. Y. Sun and G. Ge, “On the Palindromic/Reverse-Complement Duplication Correcting Codes,” arXiv:2602.01151, 2026.
