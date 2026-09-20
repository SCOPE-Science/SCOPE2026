# Review

## Correctness

**PASS.** The upper bound is given by an explicit product of stars. Each non-singleton part gets a unit-edge star coordinate that realizes distance two within that part and distance one from that part to its complement. If there are at least two singleton parts, one additional half-unit-edge star realizes distance one between their vertices. Taking the supremum gives exactly the complete-multipartite graph metric.

For the lower bound, every non-singleton part contains a pair at graph distance two, and some coordinate must realize that distance. Two such pairs from different parts cannot be realized in the same tree coordinate: the corresponding four-point sums would be \(4,\le2,\le2\), contradicting the four-point condition. If at least two singleton parts exist, a coordinate realizing their distance one also cannot realize any non-singleton same-part distance two, since the corresponding sums would be \(3,\le2,\le2\). Thus the required coordinates are all distinct, matching the construction.

The standalone verifier reconstructs the coordinate pseudometrics for all 128 connected complete-multipartite isomorphism types on 2 through 10 vertices, checks the supremum identity pairwise, checks every coordinate's four-point condition, and checks the numerical quartet certificates. These finite checks support but do not replace the general proof.

## Originality

**PASS, to the best of our knowledge, with a specific residual risk.** The current accessible full text of Ashworth--Clarke--Giansiracusa--Jones--Quijas-Aceves--Ren, arXiv:2609.19372v1, was inspected in the relevant definition and examples sections. It proves complete bipartite graphs have rank two (Proposition 3.5), includes complete graphs minus a perfect matching among rank-half families (Theorem 3.3), gives \(K_4\setminus e\) as a rank-two example (Example 3.6), and classifies rank-one graphs (Theorem 3.7). No general complete-multipartite statement appears, and the full text has no occurrence of “multipartite”. Targeted searches for phylogenetic rank together with complete multipartite/tripartite terminology found no additional source stating the formula.

Cartwright--Chan, arXiv:0912.1411 / Combinatorica 32 (2012), was inspected because its Section 5 contains complete multipartite graphs in a tree-rank characterization. That work studies a different tropical tree-rank notion; it explicitly says its definition differs from the Pachter--Sturmfels Chapter 3 notion. Its Proposition 13 therefore does not establish the supremum-product phylogenetic rank formula here.

The most plausible prior source capable of overturning originality is Pachter--Sturmfels, *Algebraic Statistics for Computational Biology* (Cambridge University Press, 2005), Section 3.5, ISBN 9780521857000. Bibliographic information and the table of contents were inspected, and the 2026 paper's descriptions of the section were inspected, but the full text of Section 3.5 itself was not inspected. Because that section introduces the underlying rank notion and mixtures of tree metrics, an unnoticed complete-multipartite special case there would directly weaken or eliminate the originality claim. No such special case was found in searchable metadata or the later literature checked here. This residual risk is retained rather than treated as evidence of absence.

## Value

**PASS.** The formula completely determines a natural, broad graph class for a parameter introduced into graph theory only recently. It unifies several examples treated separately in the 2026 source, gives an immediate complete spectrum \(1,\ldots,\lfloor n/2\rfloor\) for fixed-order complete multipartite graphs, and exposes a simple geometric mechanism: distance-two pairs from distinct non-singleton parts are pairwise incompatible in any single tree coordinate, while singleton parts collectively cost at most one further coordinate.

## Limitations

- The full text of Pachter--Sturmfels (2005), Section 3.5, was not inspected and is the principal residual originality risk.
- The theorem concerns connected complete multipartite graph metrics; it does not classify general graphs of a given phylogenetic rank.
- The finite verifier checks the explicit construction and lower-bound certificates only through order 10; the theorem itself is proved without computational assumptions.
- Independent audit has not been performed.

Same-model review: passed. Independent audit: not yet performed.
