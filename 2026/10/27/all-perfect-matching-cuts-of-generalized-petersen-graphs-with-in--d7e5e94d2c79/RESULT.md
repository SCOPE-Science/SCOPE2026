# All perfect matching cuts of generalized Petersen graphs with inner step two

## Finding

For every integer \(n\ge5\), let \(G=\operatorname{GP}(n,2)\). A *labelled perfect two-coloring* is a map \(c:V(G)\to\{0,1\}\) in which each vertex has exactly one neighbor of the opposite color (so its equitable-partition quotient matrix is \(\left(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\right)\)). The exact number is
\[
N_n=2+10\,\mathbf 1_{\{5\mid n\}}.
\]
Consequently the number of unordered bipartitions with a perfect-matching crossing edge set, and equivalently the number of distinct perfect matching cuts, is
\[
C_n=1+5\,\mathbf 1_{\{5\mid n\}}.
\]
The two always-present colorings assign opposite constant colors to the two Petersen layers. For \(5\mid n\), the other ten colorings are the five cyclic shifts, and their five complements, of the period-five template whose outer-layer colors are \((1,0,0,1,1)\) and inner-layer colors are \((1,0,0,1,0)\). This list is exhaustive for every \(n\ge5\).

## Assumptions and scope

Indices are taken in \(\mathbb Z/n\mathbb Z\). The graph has distinct outer vertices \(u_i\), inner vertices \(v_i\), and edges \(u_i u_{i+1}\), \(u_i v_i\), \(v_i v_{i+2}\). For \(n\ge5\), each vertex has three distinct neighbors. The two colors are distinguished when computing \(N_n\), but not when computing \(C_n\). A *perfect matching cut* means an edge cut that is itself a perfect matching; this is stronger than the existence of a perfect matching containing some cut. The graph is connected, so each cut determines its unordered vertex bipartition uniquely.

## Proof

Write \(a_i=c(u_i)\) and \(b_i=c(v_i)\), interpreted as elements of \(\{0,1\}\). Let \(\oplus\) denote binary addition modulo two, and introduce binary edge indicators
\[
p_i=a_i\oplus a_{i+1},\qquad q_i=b_i\oplus b_{i+2},\qquad s_i=a_i\oplus b_i.
\]
The requirement of exactly one opposite-color neighbor at each outer and inner vertex is precisely
\[
p_{i-1}+p_i+s_i=1,\qquad q_{i-2}+q_i+s_i=1,\tag{1}
\]
where these sums are ordinary integers. The first equality implies \(p_{i-1}p_i=0\) and \(s_i=1-p_{i-1}-p_i\). Since \(b_i=a_i\oplus s_i\), the first equality also gives, by taking parities,
\[
q_i=p_{i-1}\oplus p_{i+2}.
\]
Substituting this identity into the second equality in (1) yields
\[
(p_{i-3}\oplus p_i)+(p_{i-1}\oplus p_{i+2})=p_{i-1}+p_i.\tag{2}
\]
Because adjacent \(p\)-indicators cannot both equal one, the pair \((p_{i-1},p_i)\) is one of \((0,0),(1,0),(0,1)\). In the first case (2) forces \(p_{i-3}=p_{i+2}=0\). In each of the other two cases, (2) is equivalent to \(p_{i-3}=p_{i+2}\). Hence, for every index,
\[
p_{i+2}=p_{i-3},\tag{3}
\]
so \(p\) is five-periodic, even when \(n\) is not a multiple of five. If \(5\nmid n\), the cyclic and five-periodic constraints force \(p\) to be constant; the prohibition on adjacent ones makes it identically zero.

When \(5\mid n\), a five-periodic binary word with no adjacent ones has either zero, one, or two ones per period. Exactly one is impossible: if \(p_j=1\) is its sole one, then \(p_{j+2}=p_{j+3}=0\), and applying the \((0,0)\) case of (2) at \(i=j+3\) would force \(p_{j+5}=p_j=0\). Thus the possibilities are the all-zero word and exactly five words with two nonadjacent ones in a five-cycle. Each of these five latter patterns satisfies the additional zero-pair rule used above (check its five cyclic indices), so (2) holds in both directions.

For each admissible \(p\), choose \(a_0\in\{0,1\}\) and reconstruct all outer colors from \(a_{i+1}=a_i\oplus p_i\). This closes consistently around the cyclic index set because each five-block has either zero or two ones. Define \(s_i=1-p_{i-1}-p_i\) and \(b_i=a_i\oplus s_i\). Then the derived identity for \(q_i\), together with (2), verifies both original equations in (1); hence each reconstructed coloring is valid. For the all-zero pattern, its two colors are the two layer-constant solutions. When \(5\mid n\), each of the five two-one patterns gives two complementary solutions. Therefore \(N_n=2\) or \(12\), as stated.

Finally the set of cross-color edges is a perfect matching by construction. Every such matching cut corresponds to two and only two labelled colorings, since \(G\) is connected and interchanging color names changes no edges. Dividing \(N_n\) by two yields \(C_n\). \(\square\)

## Verification

Two independently constructed standard-library programs are included. Execute `python3 verify_transfer.py` and `python3 verify_direct.py` from the directory containing the files. The first explicitly builds a 256-state, four-column transfer graph and enumerates its cyclic strongly connected components, then checks the predicted labelled-coloring counts at several orders up to 101. It finds two one-state cycles and two directed five-cycles and reconstructs the formula. The second enumerates every outer-layer binary word for \(5\le n\le19\), determines its forced inner-layer colors from the outer constraint, and checks the inner constraint; it compares the entire set of solutions, not just the counts, with the five-shift template prediction. Their actual recorded outputs are `transfer_output.txt` and `direct_output.txt`. The proof above, rather than finite testing, establishes the statement for all orders.

## Relationship to prior work

Alaeiyan and Karami (2016, Theorem 3.2) prove the existence of the layer-constant coloring with quotient matrix \(\left(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\right)\), while their paper enumerates possible quotient *matrices*, not all coloring maps. The present theorem determines every coloring map and matching cut for this matrix, including the five additional nontrivial cuts when \(5\mid n\). Later literature distinguishes exact perfect-matching cuts from the weaker condition that a graph cut be contained in a perfect matching; neither statement alone implies the enumeration. Previously established classifications of dominating induced matchings in this graph family concern edge sets whose endpoints form induced matchings, not perfect matching cuts (a different invariant and edge-cardinality constraint).

## Limitations

The result applies only to \(\operatorname{GP}(n,2)\), \(n\ge5\), and to cuts that themselves form perfect matchings. It is not a classification of all equitable partitions, of arbitrary generalized Petersen parameters, or of perfect matchings merely containing a cut. Full survey of unindexed theses and books is not guaranteed; mathematical priority should be evaluated independently. The finite program outputs provide reproducible corroboration, not a substitute for the symbolic argument.

## References

1. M. Alaeiyan and H. Karami, "Perfect 2-colorings of the generalized Petersen graph," *Proceedings - Mathematical Sciences* **126** (2016), 289–294. DOI: 10.1007/s12044-016-0285-4. Online publication: 2016-05-16.
2. "Perfect matching cuts partitioning a graph into complementary subgraphs," arXiv:2210.06714 (2022).
3. "The complexity of the Perfect Matching-Cut problem," arXiv:2011.03318 (2020).
