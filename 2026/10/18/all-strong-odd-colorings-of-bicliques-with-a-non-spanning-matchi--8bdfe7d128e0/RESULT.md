# All strong odd colorings of bicliques with a non-spanning matching deleted

## Finding
Let \(a,b\ge2\) be integers, and let \(0\le t<\min(a,b)\). Form the simple bipartite graph \(G_{a,b,t}=K_{a,b}-M_t\) by deleting a matching of size \(t\). Write \(r=a-t\) and \(s=b-t\), so both are positive. A *strong odd coloring* is a proper vertex coloring in which, at every vertex, each neighbor color is represented either zero times or an odd number of times.

All color classes have exactly one of three forms: an individually colored endpoint or jointly colored pair of a deleted matching edge; an odd-cardinality block entirely among the \(r\) unmatched vertices on the first side; or an odd-cardinality block entirely among the \(s\) unmatched vertices on the other side. Conversely, every partition into these classes, with a distinct color on each class, is a strong odd coloring.

Let \(O(m,k)\) denote the number of partitions of a labeled \(m\)-element set into \(k\) nonempty blocks, each of odd size. Equivalently,
\[
O(m,k)=\frac{m!}{k!}[z^m](\sinh z)^k,
\]
where \(O(0,0)=1\) and other out-of-range values vanish. For \(q\in\mathbb Z_{\ge0}\), let \(P_{a,b,t}(q)\) count all strong odd colorings from the named palette \(\{1,\ldots,q\}\), allowing unused colors. With \((q)_{\underline d}=\prod_{i=0}^{d-1}(q-i)\), the entire coloring-count polynomial is
\[
\boxed{P_{a,b,t}(q)=\sum_{j=0}^{t}\binom tj\sum_{k=1}^{r}\sum_{\ell=1}^{s}O(r,k)O(s,\ell)\,(q)_{\underline{2t-j+k+\ell}}.}
\]
Every coefficient in the falling-factorial basis counts a distinct partition shape by number of used colors.

Define \(E(m)=1\) if \(m\) is odd and \(E(m)=2^{m-2}\) if \(m\) is positive and even. Then the minimum number of colors and the number of colorings with exactly that many **named available** colors are
\[
\boxed{\chi_{\mathrm{so}}(G_{a,b,t})=t+2+\mathbf 1_{2\mid r}+\mathbf 1_{2\mid s},\qquad N_{\min}=\chi_{\mathrm{so}}(G_{a,b,t})!\,E(r)E(s).}
\]
The stronger statement also classifies every optimal coloring: each deleted pair is monochromatic, and each unmatched side is one odd block if its size is odd or two odd blocks if its size is even. In the latter case the two blocks form one unordered odd bipartition.

As a sharp edge-sensitivity consequence, for \(a,b\ge2\) both even, deleting a single edge from \(K_{a,b}\) changes the strong odd chromatic number from \(4\) to \(3\); when both are odd, it changes from \(2\) to \(5\). This contrasts opposite responses to the same local graph operation.

## Assumptions and scope
All graphs are finite, loopless, undirected, and simple. Label the two sides \(A=\{a_1,\ldots,a_a\}\) and \(B=\{b_1,\ldots,b_b\}\). The missing edges are exactly \(a_i b_i\) for \(1\le i\le t\). Write \(A_0=\{a_{t+1},\ldots,a_a\}\) and \(B_0=\{b_{t+1},\ldots,b_b\}\). The restriction \(t<\min(a,b)\) is essential: both \(A_0\) and \(B_0\) must be nonempty, and the classification does **not** assert the same formula when a deleted matching saturates either side.

A coloring \(\varphi:V(G)\to\{1,\ldots,q\}\) is strong odd precisely when it is proper and \(\lvert N(v)\cap\varphi^{-1}(c)\rvert\in\{0,1,3,5,\ldots\}\) for every vertex \(v\) and every palette color \(c\). Colors may be unused. The polynomial above treats named colors; a coloring up to permutation of color names is instead a set partition into its nonempty color classes.

## Proof
**Color-class classification.** Fix a strong odd coloring and one nonempty color class \(C\). Properness makes \(C\) independent. If \(C\) meets both sides, a shared color on \(a_i,b_j\) requires their pair to be a nonedge, so \(i=j\le t\). Any third member would be adjacent to one member of this pair; consequently \(C=\{a_i,b_i\}\).

If \(C\subseteq A\), the unmatched vertex \(b_{t+1}\) is adjacent to every vertex of \(A\). Thus \(\lvert C\rvert\) must be odd. If \(C\) contains any matched endpoint \(a_i\), where \(i\le t\), then \(b_i\) sees exactly \(\lvert C\rvert-1\) vertices of color \(C\). This quantity is even, and must be zero, hence \(\lvert C\rvert=1\). Therefore every non-singleton class within \(A\) is an odd-sized subset of \(A_0\). The symmetric argument applies to classes within \(B\). This proves necessity.

Conversely, consider any vertex partition into the listed classes. A singleton is automatically odd independent; a deleted matched pair is independent, and any outside vertex sees zero or one member of it. Any odd-sized block within \(A_0\) is independent, and vertices in \(B\) see all its members, whereas vertices in \(A\) see none. Similarly for \(B_0\). Hence each class contributes either zero or an odd number of neighbors to any vertex. Assigning distinct colors therefore produces exactly a strong odd coloring. This proves sufficiency, including the cases \(t=0\), \(r=1\), and \(s=1\).

**Exact enumeration.** Among the \(t\) labeled deleted matching pairs, choose \(j\) to be two-vertex color classes; their other \(t-j\) pairs contribute two singleton classes each. Thus there are \(\binom tj\) choices and \(2t-j\) resulting classes. Independently partition the \(r\) unmatched \(A\)-vertices into \(k\) odd blocks and the \(s\) unmatched \(B\)-vertices into \(\ell\) odd blocks, in \(O(r,k)O(s,\ell)\) ways. The resulting \(2t-j+k+\ell\) nonempty, distinguishable vertex blocks receive pairwise distinct colors from a \(q\)-color palette in \((q)_{\underline{2t-j+k+\ell}}\) ways. Every valid coloring has one unique set of classes, so there is no overcounting. Summation proves the displayed polynomial.

For completeness, the exponential formula for set partitions gives \(\sum_{m\ge0}O(m,k)z^m/m!=(\sum_{h\ge1,\ h\,\mathrm{odd}}z^h/h!)^k/k!=(\sinh z)^k/k!\), proving the stated coefficient identity.

**Optimum and its multiplicity.** Every deleted pair needs at least one color class and attains this only when fused. A nonempty set of \(m\) vertices needs one odd-sized block when \(m\) is odd, and at least two when \(m\) is even; two odd blocks always exist for even \(m\ge2\). The minimum number of blocks is therefore \(t+2+\mathbf1_{2\mid r}+\mathbf1_{2\mid s}\), with equality forcing every missing-edge pair to be fused and a minimum odd partition on each unmatched side. An odd \(m\) admits exactly one one-block partition. For even \(m\), choosing an odd proper subset determines a bipartition into two odd blocks: there are \(2^{m-1}\) odd subsets and exchanging the two blocks identifies each unordered partition twice, leaving \(2^{m-2}\). Thus there are \(E(r)E(s)\) optimal unlabeled partitions, each receiving exactly \(\chi_{\mathrm{so}}!\) distinct assignments of its classes to an optimal named palette. This proves the optimal-coloring formula and classification.

For the edge-sensitivity statement, put \(t=0\) and then \(t=1\). If \(a,b\) are even, the two unmatched sizes change from even to odd, so the minimum goes from \(4\) to \(3\). If both are odd, the two sizes change from odd to even, and the minimum changes from \(2\) to \(5\).

## Verification
The standalone standard-library checker `verification/verify.py` independently constructs every tested graph by its adjacency masks. It generates canonical set partitions into nonempty blocks while enforcing only graph-theoretic properness and then tests the neighborhood parity condition directly for every candidate. It compares the full histogram by number of color classes with the falling-factorial coefficients and separately checks the minimum and number of optimal classes. It tested all \(30\) profiles with \(2\le a\le b\le5\), \(0\le t<a\), considering \(22,259\) proper canonical partitions in total. Additional exact arithmetic checks covered profiles as large as \((a,b,t)=(20,21,7)\). The captured output is in `verification/output.txt`; run `python3 verification/verify.py` from the package root to reproduce it. The computation is a finite stress test, not a substitute for the universal proof above.

## Relationship to prior work
Kwon and Park introduced strong odd coloring in arXiv:2401.11653 (first public 22 January 2024) and noted that complete bipartite graphs have strong odd chromatic number at most four. Their inspected treatment gives sparsity-based bounds, not a count of all strong odd colorings after deleting a non-spanning matching. Caro, Petruševski, Škrekovski, and Tuza subsequently treated trees, planar graphs, and graph products in arXiv:2410.02336, including \(K_p\square K_q\) and \(K_p\times K_q\), but their product statements do not imply the three-parameter enumerator here.

The later work “The odd independence number of graphs, I: Foundations and classical classes” (arXiv:2509.20763) proves general relations between partitions into odd independent sets and strong odd colorings, and treats several classical graph families; its general propositions do not specify the color-class structure of partial matching deletions. A publicly available exact analysis of odd crown graphs determines \(\chi_{\mathrm{so}}\) and the unique optimal partition only for \(K_{n,n}-M_n\) with odd \(n\), where the deleted matching is **spanning**. Another analysis of complete multipartite graphs gives all odd independent sets before cross edges are removed; those results cover the undeleted baseline but not the non-spanning deletion case. These are distinct implication boundaries, not merely different graph names.

Searches were performed for strong odd colorings, odd-independent-set partitions, deleted matchings in bicliques, the partial-crown and crown aliases, and the full coloring polynomial. No result among the inspected sources implied the full three-parameter polynomial or all its minimizers. This is a best-knowledge originality assessment, not a proof of priority.

## Limitations
The theorem requires both unmatched sides to be nonempty and excludes graphs with a deleted matching saturating one side, where extra color-class types may occur. Its complete color-count polynomial is not claimed for arbitrary sets of deleted cross edges. Equivalence to some unindexed published formula remains a literature risk. No outside validation of the universal proof has been performed, and finite enumeration alone cannot establish its all-parameter conclusion.

## References
1. H. Kwon and B. Park, “Strong odd coloring of sparse graphs,” arXiv:2401.11653, initial public version 2024-01-22, https://arxiv.org/abs/2401.11653.
2. Y. Caro, M. Petruševski, R. Škrekovski and Z. Tuza, “On strong odd colorings of graphs,” arXiv:2410.02336, initial public version 2024-10-03, https://arxiv.org/abs/2410.02336.
3. Y. Caro, M. Petruševski, R. Škrekovski and Z. Tuza, “The odd independence number of graphs, I: Foundations and classical classes,” arXiv:2509.20763, initial public version 2025-09-25, https://arxiv.org/abs/2509.20763.
4. “Odd independence and strong odd coloring of odd crown graphs,” publicly available mathematical result (2026), direct comparison against its full scientific statement.
5. “Odd independent sets in complete multipartite graphs,” publicly available mathematical result (2026), direct comparison against its full scientific statement.
