# The first entropy-bound failure for adaptive orientations of triangular books

## Finding
For each integer \(r\ge 1\), let \(B_r=K_{1,1,r}\) be the *triangular book*: two spine vertices \(0,1\) joined by an edge, and \(r\) page vertices adjacent to both spine vertices and to no other page vertex. A hypothesis is an acyclic orientation of every edge; a query specifies an edge and asks its direction (encoded relative to the increasing endpoint labels). Let \(\mathcal A_r\) be this finite binary concept class.

The exact Littlestone dimensions for \(1\le r\le7\) are
\[
(\operatorname{Ldim}(\mathcal A_r))_{r=1}^7=(2,4,5,7,8,10,11).
\]
For all \(r\ge1\), the number of concepts is \(|\mathcal A_r|=2\cdot3^r\), and the VC dimension is \(r+1\), the rank of the connected graph's cycle matroid. The VC and counting facts are background, not claims of novelty.

The smallest page count for which the information-theoretic cardinality bound on Littlestone dimension is *not attained* is \(r=7\):
\[
\operatorname{Ldim}(\mathcal A_7)=11<12=\lfloor\log_2(2\cdot3^7)\rfloor.
\]
For each \(1\le r\le6\), equality holds in the cardinality bound. At \(r=7\), there are \(4374\) different acyclic orientations, enough to support \(4096\) leaves in principle, but no depth-\(12\) fully adaptive binary edge-query tree.

## Assumptions and scope
The vertex set of \(B_r\) is \(\{0,1,2,\ldots,r+1\}\), its edges are \(\{0,1\}\) and \(\{0,i\},\{1,i\}\) for \(2\le i\le r+1\). The query order is the spine edge, then the two spokes of each page, in increasing page index. Bit \(0\) means that the lower-labelled endpoint directs the edge toward the higher-labelled endpoint; bit \(1\) means the reverse. An adaptive tree of depth \(d\) is shattered if every one of its \(2^d\) answer paths agrees with some acyclic orientation. Repeating a coordinate on one path cannot split the surviving hypotheses and is therefore unnecessary.

The exact adaptive classification is asserted only for \(r\in\{1,2,3,4,5,6,7\}\). No formula or extrapolation for \(r\ge8\) is asserted.

## Proof
**Orientation decomposition.** Let \(s\) be the spine bit and \(a_i,b_i\) the two spoke bits on page \(i\). If \(s=0\), exactly the local pair \((a_i,b_i)=(1,0)\) creates a directed triangle. If \(s=1\), exactly the pair \((0,1)\) does. Any directed simple cycle is a triangle through the spine (or contains the spine edge with two page paths; such a four-cycle would require a forbidden directed triangle when the spine is oriented). Hence the acyclic orientations are exactly those satisfying these local restrictions, with three independent local choices on each page for either spine bit. There are therefore \(2\cdot3^r\) hypotheses.

For completeness, the four-cycle issue can be checked directly: a directed cycle using two distinct pages would require one directed page path from \(0\) to \(1\) and another directed page path from \(1\) to \(0\). Exactly one of those two directed page paths conflicts with the direction of the spine and would already give a directed triangle. Thus triangle avoidance suffices.

**Exact recursion.** Index the \(2\cdot3^r\) valid orientations and represent any surviving hypothesis set by a finite bitmask \(S\). For each edge-query index \(q\) let \(S_{q,0}\) and \(S_{q,1}\) denote those orientations giving the specified bit. Define \(F_r(S,0)\) to mean \(S\ne\varnothing\), and for \(d\ge1\) set
\[
F_r(S,d)\iff\bigvee_{q=0}^{2r}\bigl(F_r(S_{q,0},d-1)\land F_r(S_{q,1},d-1)\bigr).
\]
This is equivalent, by induction on \(d\), to existence of a complete shattered adaptive tree of depth \(d\): its root must use some coordinate \(q\), and each answer branch must admit the remaining depth. If \(|S|<2^d\), the predicate is false because distinct answer paths require distinct hypotheses. The program in `verify.py` uses this valid pruning rule, otherwise enumerates every possible root query, and memoizes exact finite subproblems. It never infers impossibility from a timeout or an unexamined branch.

Running the recurrence from the complete concept set gives the displayed dimensions. In particular, the depth-\(12\) test is false when \(r=7\), after \(236276\) distinct cached subproblems were computed across all tested depths. The exact complete-tree certificates in `CERTIFICATE.json` separately establish all seven lower bounds, including a depth-\(11\) tree with \(2047\) internal queries and \(2048\) distinct acyclic leaf witnesses at \(r=7\). These facts jointly prove the upper and lower bounds for every claimed finite parameter.

The VC formula follows from the known forest criterion for acyclic orientations: fixed queried edge supports are shattered exactly when they are forests. Since \(B_r\) is connected on \(r+2\) vertices, the maximum forest size is \(r+1\).

## Verification
Run `python verify.py CERTIFICATE.json` using Python 3.10 or later and the two supplied files in the same directory. The script independently constructs the concept set for each parameter, checks all its members for acyclicity by topological vertex elimination, evaluates the exact adaptive recursion, and checks each full binary certificate against all edge answers and acyclicity. It verifies \(3508\) leaf witnesses across seven complete trees, with no duplicated witness within any tree. The expected output is reproduced in `verification_output.txt`.

The search state counts for \(r=1,\ldots,7\) are \(11,72,224,1298,5396,28117,236276\), including calls used in the final unsuccessful depth test. An explicit early cardinality pruning branch is logically exact. Code and certificate are required computational evidence; the displayed cardinality bound by itself does not establish the strict inequality at \(r=7\).

## Relationship to prior work
Kozma and Moran (2013, Section 3.1, Lemma 12 and Proposition 15) already characterize the VC-shattered supports for acyclic graph orientations as forests. Blagoev (first posted August 8, 2018) develops an exact enumeration method for acyclic orientations of complete multipartite graphs, encompassing \(K_{1,1,r}\). Cardinal, Hoang, Merino, Mička and Mütze (first posted December 7, 2022) study Gray-code generation and lattice structures for acyclic orientations, particularly on chordal graphs. Those count, static-shattering and generation results do not themselves give the optimal depth of an adaptive edge-query shattering tree. The new statement is the exact finite adaptive sequence and its first information-theoretic failure at seven pages.

## Limitations
The result is a finite-range exact classification, not a uniform formula in \(r\). The upper bound at seven pages is computationally exhaustive and depends on correct execution of the supplied small verifier; it is not a separate short structural obstruction theorem. Relevant historical priority searches cannot exclude every unpublished or differently indexed earlier computation. Independent external mathematical validation has not been performed.

## References
1. L. Kozma and S. Moran, *Shattering, Graph Orientations, and Connectivity*, Electronic Journal of Combinatorics 20(3) (2013), P44, DOI 10.37236/3326; https://www.combinatorics.org/ojs/index.php/eljc/article/download/v20i3p44/pdf/ .
2. V. Blagoev, *On the Number of Acyclic Orientations of Complete k-Partite Graphs*, arXiv:1808.02787v1, August 8, 2018; https://arxiv.org/html/1808.02787v1 .
3. J. Cardinal, H. P. Hoang, A. Merino, O. Mička and T. Mütze, *Combinatorial Generation via Permutation Languages. V. Acyclic Orientations*, arXiv:2212.03915v1, December 7, 2022; https://wrap.warwick.ac.uk/id/eprint/174321/13/WRAP-combinatorial-generation-via-permutation-languages-acyclic-orientations-Mutze-2023.pdf .
