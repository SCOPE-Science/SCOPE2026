# The integral critical group of the Coxeter graph

## Finding
Let \(G\) be the Coxeter graph, the 28-vertex cubic distance-transitive graph of girth seven. Its (ordinary, unembedded) graph critical group is
\[
K(G)\cong \mathbb Z/8\mathbb Z\oplus(\mathbb Z/56\mathbb Z)^5.
\]
In particular it has minimal generator number six, exponent \(56\), and seven-primary subgroup \((\mathbb Z/7\mathbb Z)^5\). Its order, equivalently its spanning-tree number, is \(4{,}405{,}854{,}208\). The novel claim concerns the integral invariant factors, not a new graph construction, graph spectrum, or Matrix--Tree formula.

## Assumptions and scope
The underlying graph has vertices the 28 three-element subsets of \(\{0,1,\ldots,6\}\) that are not among the seven Fano lines \(\{i,i+1,i+3\}\pmod 7\), for \(i=0,\ldots,6\). Two retained triples are adjacent exactly if disjoint. This is the standard Fano--Kneser realization of the Coxeter graph. Lexicographically order the vertices and delete the last row and column of the integer Laplacian \(L=3I-A\), obtaining \(R\in\mathbb Z^{27\times27}\). The critical group is the finite abelian cokernel \(\mathbb Z^{27}/R\mathbb Z^{27}\). The claim is only for this graph, not for all cubic distance-regular graphs.

## Proof
The accompanying `certificate.json` specifies all 28 triples in order and an integral 27-by-27 matrix \(B\), and `verify_integral.py` checks, entry by entry, the exact identity
\[
RB=56I_{27}.
\]
Consequently \(R\) is invertible and \(56R^{-1}=B\) is integral. If \(d_1\mid d_2\mid\cdots\mid d_{27}\) are the positive integer Smith factors of \(R\), integer unimodular equivalence therefore implies that every \(d_i\) divides \(56\).

The same exact checker calculates the integer determinant by fraction-free elimination and obtains
\[
\det R=4{,}405{,}854{,}208=2^{18}7^5.
\]
It calculates Gaussian-elimination ranks of \(R\) over the prime fields \(\mathbb F_2\) and \(\mathbb F_7\), respectively \(21\) and \(22\). Therefore precisely six Smith factors are even, precisely five are divisible by seven, and no other prime divides any factor. Since every factor divides \(56=2^3\cdot7\), the six even factors have 2-adic exponents at most three; their exponents sum to eighteen, forcing exponent three for each. Similarly each of the five factors divisible by seven contains seven to exactly the first power. Divisibility ordering places these on five of the six factors divisible by eight, giving 21 unit factors, one factor 8, and five factors 56. This proves the displayed critical-group decomposition.

For independent arithmetic checks, `verify_sympy.py` directly recomputes the Smith form over \(\mathbb Z\) from the Fano construction. The determinant also follows independently from the previously published adjacency spectrum: the nonzero Laplacian eigenvalues are \(1\) (eightfold), \(4\) (sevenfold), and \(4\pm\sqrt2\) (sixfold each); the Matrix--Tree Theorem gives \(28^{-1}4^7 14^6=2^{18}7^5\).

## Verification
Execute `python verify_integral.py` in the artifact directory using the included JSON certificate; this uses only the Python standard library and checks all 729 entries of the inverse-multiplier identity, the determinant, both modular ranks, graph size, degree, connectivity and girth. Separately, with SymPy installed, execute `python verify_sympy.py` for an exact integer Smith-normal-form calculation. Both programs ran successfully from the final newly created artifact directory. These checks constitute an explicitly finite reproducible certificate, not a claim of independent scholarly certification.

## Relationship to prior work
The graph's structure and spectrum are classical: Dejter (arXiv:1002.1960, originally public 2010-02-09) describes the Coxeter graph in detail; MathWorld compiles its 28-vertex structure and adjacency spectrum, citing Biggs, Bondy, and van Dam--Haemers. Their spectrum implies the group order but does not, as a general matter, determine integral Smith factors. Jacobson--Niedermaier--Reiner's 2003 theorem treats complete multipartite graphs and Cartesian products of complete graphs, which do not include this cubic graph. No matching published critical-group decomposition was located in targeted searches. Prior studies of other cubic graphs' critical groups, including the McGee graph, have a different graph and integral Laplacian and do not imply this answer.

## Limitations
No all-graph-family Smith theorem or general distance-regular critical-group classification is asserted. The arithmetic identity and computations are exact but limited to the displayed 28-vertex graph. Historical unpublished computations or unindexed critical-group tables could contain the same factors; absence from searches cannot establish priority. Independent external audit has not been performed.

## References
- I. J. Dejter, *From the Coxeter graph to the Klein graph*, arXiv:1002.1960, first submitted 2010-02-09, https://arxiv.org/abs/1002.1960 .
- E. W. Weisstein, *Coxeter Graph*, MathWorld, https://mathworld.wolfram.com/CoxeterGraph.html (includes Foster census identification and spectrum).
- B. Jacobson, A. Niedermaier and V. Reiner, *Critical groups for complete multipartite graphs and Cartesian products of complete graphs*, Journal of Graph Theory 44 (2003), 231--250, https://doi.org/10.1002/jgt.10139 .
- H. S. M. Coxeter, *My Graph*, Proceedings of the London Mathematical Society 46 (1983), 117--136 (classical graph source).
