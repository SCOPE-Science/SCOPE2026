# Exact proper conflict-free colorings of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a finite simple complete multipartite graph with \(r\ge 2\), and let
\[
s=\left|\left\{i:n_i=1\right\}\right|.
\]
A proper vertex coloring of \(G\) is proper conflict-free if and only if at least two partite sets contain a singleton color class. Therefore
\[
\chi_{\mathrm{pcf}}(G)=r+\max\{0,2-s\}.
\]
This criterion also classifies every optimum coloring. Define \(w(2)=1\) and \(w(n)=n\) for \(n\ge3\). If \(q=\chi_{\mathrm{pcf}}(G)\), the number \(U(G)\) of optimal color partitions up to permutation of color names is
\[
U(G)=
\begin{cases}
1,&s\ge2,\\
\displaystyle\sum_{i:n_i\ge2}w(n_i),&s=1,\\
\displaystyle\sum_{i<j,\,n_i,n_j\ge2}w(n_i)w(n_j),&s=0.
\end{cases}
\]
Thus the number of labeled optimal colorings with palette \([q]\) is \(q!U(G)\).

## Assumptions and scope
Graphs are finite and simple. The graph has at least two nonempty partite sets, so it is connected and has no isolated vertices. A proper conflict-free coloring is a proper vertex coloring in which every vertex has a color occurring exactly once in its open neighborhood. The result concerns the ordinary proper conflict-free chromatic number, not list variants or \(h\)-conflict-free variants with \(h>1\).

## Proof
In a proper coloring of a complete multipartite graph, every color class lies wholly inside a single partite set, because vertices from distinct parts are adjacent. Fix a vertex \(v\in V_i\). Its open neighborhood is exactly \(V(G)\setminus V_i\). Hence a color occurs exactly once in \(N(v)\) if and only if its entire color class is a singleton contained in some part \(V_j\) with \(j\ne i\).

Let \(W\) be the set of part indices that contain at least one singleton color class. The coloring is proper conflict-free exactly when, for every \(i\), the set \(W\setminus\{i\}\) is nonempty. Since \(r\ge2\), this is equivalent to \(|W|\ge2\). This proves the structural criterion.

A singleton part contributes a singleton color class already when the part is monochromatic. A non-singleton part contributes no singleton color class when monochromatic, and the least expensive way to make it contribute one is to split it into exactly two color classes, one of which is a singleton. Thus the baseline proper coloring uses \(r\) colors, and exactly \(\max\{0,2-s\}\) additional colors are necessary and sufficient to create two witnessing parts. This proves the chromatic-number formula.

For the enumeration, if \(s\ge2\), optimality permits no extra split, so the partition into the original parts is the unique optimum color partition. If \(s=1\), exactly one non-singleton part must be split into two blocks with a singleton block. A part of size two has only one such set partition, while a part of size at least three has one for each choice of the singled-out vertex, giving the factor \(w(n_i)\). If \(s=0\), exactly two distinct non-singleton parts must be split in this way, giving the product \(w(n_i)w(n_j)\) and the stated sum. Every optimum partition has exactly \(q\) nonempty color classes, so assigning the \(q\) color names contributes a factor of \(q!\).

## Verification
The standalone verifier `verify_pcf_complete_multipartite.py` independently enumerates every proper color partition for every complete-multipartite isomorphism type with at least two parts through order ten. It checks proper conflict-freeness directly from neighborhood color multiplicities, compares that definition with the two-witness-part criterion, and compares both the minimum number of colors and the number of optimal unlabeled color partitions with the formulas above. Its replay output is:

`ALL CHECKS PASSED; multipartite_types=128; proper_partitions=66497; pcf_partitions=50017; optimal_unlabeled_partitions=687; max_order=10`

This finite computation is a stress test only; the universal statement is proved by the argument above.

## Relationship to prior work
Chuet, Dai, Ouyang, and Pirot study proper \(h\)-conflict-free colorings and general bounds; the inspected text of arXiv:2505.04543 does not state a complete-multipartite exact formula. Pradhan and Sharma give complexity results and linear-time optimal algorithms on several graph classes, including chain graphs, but their algorithmic coverage does not state the arbitrary complete-multipartite structural criterion or enumerator proved here. Earlier work of Caro, Petruševski, Škrekovski, and Tuza gives general upper bounds for proper conflict-free coloring; in particular, their domination-based framework yields a natural \(\chi(G)+2\) upper bound on complete multipartite graphs, whereas the present result determines exactly when zero, one, or two colors beyond \(\chi(G)=r\) are necessary.

A semantic research-index search for the invariant together with complete-multipartite, complete-bipartite, singleton-part, and equivalent witness formulations found no covering result. The closest indexed exact result concerns crown graphs, which are obtained from complete bipartite graphs by deleting a perfect matching and therefore are not a complete-multipartite special case of this theorem. Another indexed result gives an exact odd-chromatic formula on complete multipartite graphs, but odd neighborhood multiplicity is a different and weaker condition than unique neighborhood multiplicity.

## Limitations
The proof uses the exact open-neighborhood structure of complete multipartite graphs and does not extend automatically to graphs obtained by deleting cross-part edges. It does not address list proper conflict-free coloring or the \(h>1\) variant. The literature comparison is necessarily limited by indexing and terminology; older results phrased through equivalent unique-neighborhood language remain a residual search risk.

## References
1. Q. Chuet, T. Dai, Q. Ouyang, and F. Pirot, *New bounds for proper h-conflict-free colourings*, arXiv:2505.04543, first public version 2025-05-07.
2. A. Pradhan and S. Sharma, *Complexity and algorithms for proper conflict-free coloring in graphs*, arXiv:2608.10874, first public version 2026-08-11.
3. Y. Wu and X. Zhang, *On proper conflict-free colorings of IC-planar graphs*, Discrete Applied Mathematics, DOI:10.1016/j.dam.2025.05.005.
4. Y. Caro, M. Petruševski, R. Škrekovski, and Z. Tuza, *Remarks on proper conflict-free colorings of graphs*, arXiv:2203.01088.
