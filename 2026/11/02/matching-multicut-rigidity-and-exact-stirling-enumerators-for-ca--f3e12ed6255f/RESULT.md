# Matching-multicut rigidity and exact Stirling enumerators for Cartesian path–cycle grids

## Finding
A **matching multicut** of a finite simple graph is an unordered partition \(\Pi=\{B_1,\ldots,B_k\}\) of its vertices into \(k\ge2\) nonempty blocks such that each vertex has at most one neighbor outside its own block. **No connectedness is assumed of the blocks.** Let \(a_G(k,t)\) count these partitions with exactly \(t\) crossing edges, and define the two-variable enumerator
\[
F_G(u,v)=\sum_{k\ge2}\sum_{t\ge1}a_G(k,t)u^kv^t.
\]

**Rigidity theorem.** For any finite family \(G_1,\ldots,G_d\) of connected simple graphs, each having at least two vertices, and \(d\ge2\), every matching multicut of their Cartesian product \(G=G_1\square\cdots\square G_d\) is uniquely the inverse image of a matching multicut of **one** factor under its coordinate projection. More precisely, if \(N_i=\prod_{j\ne i}|V(G_j)|\), then
\[
\boxed{F_G(u,v)=\sum_{i=1}^dF_{G_i}(u,v^{N_i}).}
\]
In particular the number of blocks, the cut size, and the number of partitions of each kind can be read exactly from the factors. This holds for arbitrary connected factors, not just paths or cycles.

For a path \(P_n\) on \(n\ge2\) vertices, let \(\bigl\{{t\atop k-1}\bigr\}\) denote a Stirling number of the second kind, understood as zero outside its usual range. Then
\[
\boxed{a_{P_n}(k,t)=\binom{n-t}{t}\biggl\{{t\atop k-1}\biggr\},\quad
1\le t\le\lfloor n/2\rfloor,\quad 2\le k\le t+1,}
\]
and all other coefficients are zero.

For a cycle \(C_n\) on \(n\ge3\) vertices, define
\[
q_t(k)=\frac1{k!}\sum_{j=0}^k(-1)^j\binom kj
\left((k-j-1)^t+(-1)^t(k-j-1)\right).
\]
Then
\[
\boxed{a_{C_n}(k,t)=\frac{n}{n-t}\binom{n-t}{t}\,q_t(k),\quad
2\le t\le\lfloor n/2\rfloor,\quad 2\le k\le t,}
\]
and all other coefficients are zero (in particular \(F_{C_3}=0\)). These formulas, inserted in the product identity, enumerate **every** matching multicut by number of blocks and cut edges for any finite Cartesian grid whose factors are paths or cycles.

## Assumptions and scope
All graphs are finite, undirected, loopless and simple; each factor is connected and nontrivial. Cartesian adjacency changes exactly one coordinate along an edge of that factor. The partition blocks are nonempty, unordered, and **may be disconnected**. An edge is crossing when its endpoints lie in different blocks. For two blocks this agrees with the conventional matching cut; for more blocks it is the matching-multicut condition of Gomes–Juliano–Martins–dos Santos. A labeled vertex set is counted once for each distinct unlabeled partition. A graph with no matching multicut has enumerator zero. Every variable, summation and zero-range convention above refers to these objects.

## Proof
**1. Propagation across Cartesian squares.** First let \(G=A\square B\) with connected nontrivial factors. Because the product is connected, a nonconstant valid partition has a crossing edge. Suppose an \(A\)-direction edge \((a,b)(a',b)\) is crossing. Each endpoint already has its sole permitted crossing neighbor. For any \(bb'\in E(B)\), both perpendicular edges \((a,b)(a,b')\) and \((a',b)(a',b')\) are therefore noncrossing. The parallel edge \((a,b')(a',b')\) remains crossing, since its endpoints retain the two original, distinct block labels. Walking along any path in connected \(B\), the complete \(B\)-fibers above \(a\) and \(a'\) are monochromatic in two different blocks, and every corresponding \(A\)-edge crosses.

We next show that **a monochromatic \(B\)-fiber forces every adjacent \(B\)-fiber to be monochromatic**. Suppose the fiber over \(c\) has constant block label \(L\), and \(c'\) is adjacent to \(c\) in \(A\). If the fiber over \(c'\) is not monochromatic, connectedness of \(B\) supplies some edge \(bb'\) on which the labels of \( (c',b) \) and \( (c',b') \) differ. These two vertices have already used their one allowed crossing edge along that \(B\)-edge. Thus their respective edges to \( (c,b) \) and \( (c,b') \) must be noncrossing. Both vertices consequently have label \(L\), a contradiction. Starting from the monochromatic fiber over \(a\), and using connectedness of \(A\), this propagation proves that **every** \(B\)-fiber is monochromatic. The partition is therefore pulled back from a partition of \(A\). The latter satisfies the matching-multicut condition, because crossing degree in the product at \((a,b)\) equals crossing degree in \(A\) at \(a\). If the original crossing edge instead lies in the \(B\) direction, interchange the factors. A nonconstant partition cannot be both an \(A\)-pullback and a \(B\)-pullback: fixing any \(a\) and varying \(b\) would make the second partition constant, contradicting two nonempty blocks. This proves existence and uniqueness for two factors.

Apply the two-factor argument to \(G_1\square(G_2\square\cdots\square G_d)\), noting that a Cartesian product of connected graphs is connected. Induction proves a unique active coordinate for every \(d\ge2\). A crossing edge in \(G_i\) lifts to \(N_i\) crossing edges in the full product; the number of blocks does not change. Conversely, any factor matching multicut lifts to a valid product partition. Disjointness by the unique active coordinate proves the displayed generating-function identity.

**2. Paths.** Along \(P_n\), the crossing edges of a valid partition form a matching, so their number \(t\) lies between \(1\) and \(\lfloor n/2\rfloor\). Any matching of \(t\) path edges arises by selecting \(t\) nonconsecutive positions among \(n-1\) positions, in \(\binom{n-t}{t}\) ways. Cutting at those edges leaves \(t+1\) maximal consecutive monochromatic runs. Two successive runs must have different block labels, but nonconsecutive runs are allowed to share a block. Thus for fixed crossing edges the required choices are **proper unlabeled \(k\)-color partitions of a path on \(t+1\) run-vertices**, not arbitrary partitions and not necessarily connected partitions. The ordinary chromatic polynomial of that run-path is \(q(q-1)^t\); expressing it in falling factorials yields
\[
q(q-1)^t=\sum_{k=1}^{t+1}\biggl\{{t\atop k-1}\biggr\}(q)_{\underline k}.
\]
The coefficient counts proper partitions into \(k\) nonempty unlabeled color classes; therefore the stated path formula follows. Since runs are maximal, adjacent run labels never coincide, so no counted crossing edge vanishes and no partition is counted more than once.

**3. Cycles.** The cut edges again form a matching. At least two crossing edges are necessary: deleting just one cycle edge does not disconnect the cycle, hence it cannot separate different block labels. For \(2\le t\le\lfloor n/2\rfloor\), the number of ways to choose \(t\) nonconsecutive cycle edges is \(\frac n{n-t}\binom{n-t}{t}\). One derivation marks a chosen edge and records the \(t\) positive clockwise gaps between selected edges (each at least two); there are \(\binom{n-t-1}{t-1}\) compositions for a fixed marked first edge. Counting marked selected edges in two ways gives \(\frac nt\binom{n-t-1}{t-1}=\frac n{n-t}\binom{n-t}{t}\).

The \(t\) maximal runs between these edges form a cyclic run graph. When \(t=2\), it has two vertices joined by two original boundary edges, which simply imposes different run labels; the same proper-coloring formula still applies. For \(t\ge3\), it is an ordinary \(t\)-cycle. Its chromatic polynomial in either case is
\[
\chi_t(q)=(q-1)^t+(-1)^t(q-1).
\]
The number of partitions into exactly \(k\) unlabeled nonempty proper color classes equals the number of **surjective** proper colorings with labeled colors, divided by \(k!\). Inclusion–exclusion on omitted colors gives exactly \(q_t(k)\). Multiply by the number of crossing-edge matchings to obtain the cycle formula. Every such choice of edge matching and proper run partition creates a valid matching multicut; conversely, every valid partition gives its unique edge matching and run partition. This completes the proof for all indices and boundary cases.

## Verification
A standalone Python 3 verifier (`check_matching_multicuts.py`, standard library only) constructs unlabeled partitions as restricted-growth strings and directly tests crossing degrees on graph edges, independently of the product formula. It checks every partition of paths on \(2\) to \(9\) vertices, cycles on \(3\) to \(9\) vertices, eleven small explicitly named Cartesian products including a three-cube, and the Cartesian product with \(P_2\) of all \(43\) labeled connected graphs on \(2\), \(3\), or \(4\) vertices. Seven additional grid parameter tuples are checked by comparing the factorwise formula with the path–Stirling formula. Execution result: `VERIFY_OK`. These are finite corroborations of, not substitutes for, the general proof.

## Relationship to prior work
Gomes, Juliano, Martins and dos Santos [1, 2] introduce matching multicuts and develop complexity, exact algorithms and parameterized enumeration tools. The original accessible full arXiv paper and the published conference version were examined; the Cartesian-square rigidity and the two-variable complete path–cycle product enumerators are not among the results identified. Centeno and coauthors [3] investigate partitions convex under paths of order three; the two-block restriction is related, but for three or more blocks their condition is not equivalent to the one-external-neighbor condition used here. Existing matching-cut complexity literature [4] establishes hardness and some restricted graph algorithms, but no equivalent factorwise all-partition enumerator was found in the material examined. A later conference abstract [5] treats \(P_3\)-convex partitions of graph products, not the precise matching-multicut enumerator. Novelty is a literature-search assessment, **not** a proof of publication priority.

## Limitations
The rigidity requires connected nontrivial factors and the Cartesian graph product; it does not automatically apply to strong, tensor or lexicographic products, or to products of disconnected graphs. The Stirling closed forms require path or cycle factors; arbitrary connected factors satisfy the reduction formula but require separate factor enumerators. The graph partitions permit disconnected blocks and are not convex partitions. Finite testing is not an infinite proof. An inaccessible full version of the later \(P_3\)-convex-product conference contribution, or unindexed related work, could affect priority; no independent audit has been performed.

## References
1. G. C. M. Gomes, E. Juliano, G. Martins, V. F. dos Santos, *Matching (Multi)Cut: Algorithms, Complexity, and Enumeration*, arXiv:2407.02898v1, first posted 2024-07-03. https://arxiv.org/abs/2407.02898
2. Same authors, *Matching (Multi)Cut: Algorithms, Complexity, and Enumeration*, IPEC 2024, LIPIcs 321, paper 25. https://doi.org/10.4230/LIPIcs.IPEC.2024.25
3. C. Centeno, S. Dantas, M. C. Dourado, D. Rautenbach, J. L. Szwarcfiter, *Convex Partitions of Graphs induced by Paths of Order Three*, Discrete Mathematics & Theoretical Computer Science (2010). https://doi.org/10.46298/dmtcs.502
4. P. Bonsma, *The complexity of the matching-cut problem for planar graphs and other graph classes*, Journal of Graph Theory 62 (2009), 109–126. https://doi.org/10.1002/jgt.20390
5. Borges and Nascimento, *P3-convex partitions in Cartesian product and strong product of graphs*, conference abstract (2026), full text not located during this assessment.
