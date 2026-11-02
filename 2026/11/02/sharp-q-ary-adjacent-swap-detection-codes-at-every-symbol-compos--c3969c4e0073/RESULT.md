# Sharp \(q\)-ary adjacent-swap detection codes at every symbol composition

## Finding

Fix an ordered alphabet \(\Sigma=\{0,\ldots,q-1\}\) of size \(q\ge3\). For any \(n\ge1\), form the simple graph \(G_{q,n}\) with one vertex for each word in \(\Sigma^n\). Two *distinct* vertices are adjacent exactly when one is obtained from the other by exchanging two consecutive **unequal** letters. A set of words detects every single adjacent-swap error precisely when it is an independent set of this graph; *detection* does not require decoding a word corrupted by a swap.

The maximum size of such a code is
\[
\alpha(G_{q,n})=\frac{q^n+q^{\lceil n/2\rceil}}2.
\]
For a fixed composition \(\boldsymbol p=(p_0,\ldots,p_{q-1})\) of \(n\), write \(G_{\boldsymbol p}\) for the induced component consisting of words in which symbol \(j\) appears \(p_j\) times. Put
\[
N_{\boldsymbol p}=\frac{n!}{\prod_{j=0}^{q-1}p_j!},\qquad m=\lfloor n/2\rfloor.
\]
Define
\[
U_{\boldsymbol p}=
\begin{cases}
\displaystyle\frac{m!}{\prod_{j=0}^{q-1}\lfloor p_j/2\rfloor!},
&\text{if }\sum_j(p_j\bmod 2)=n\bmod 2,\\
0,&\text{otherwise}.
\end{cases}
\]
Thus the positive case requires zero odd multiplicities when \(n\) is even and exactly one odd multiplicity when \(n\) is odd. The exact composition-resolved optimum is
\[
\boxed{\alpha(G_{\boldsymbol p})=\frac{N_{\boldsymbol p}+U_{\boldsymbol p}}2.}
\]
In every composition class simultaneously, the words with an even inversion number form an optimal code.

## Assumptions and scope

Letters are ordered only to define inversion parity, and the optimum is independent of that ordering. The result allows unused alphabet symbols (zero entries in \(\boldsymbol p\)). There is no assumption that all multiplicities are positive. For \(n=1\) the graph has no edges and the formula gives the expected optimum of \(q\). The theorem concerns one *detected* adjacent unequal swap, not one *corrected* swap, substitution errors, arbitrary-position transpositions, or swaps combined with deletions. Its all-alphabet statement is confined to \(q\ge3\); the binary fixed-weight case is already covered by earlier token-graph literature.

## Proof

**1. Independent parity class.** For a word \(w=w_1\cdots w_n\), define
\[
I(w)=\#\{(i,j):1\le i<j\le n,\ w_i>w_j\}.
\]
Exchanging unequal adjacent letters changes \(I(w)\) by exactly \(+1\) or \(-1\), since every comparison with an outside letter is preserved in the aggregate. Thus every edge has endpoints of opposite inversion parity. The even-parity words form an independent set within each fixed-composition graph and in the whole graph.

**2. Explicit matching and its unmatched set.** Partition positions into consecutive disjoint pairs \((1,2),(3,4),\ldots,(2m-1,2m)\), with a final singleton if \(n\) is odd. Let \(E\) consist of words whose letters agree within each such pair. Given a word outside \(E\), locate the *leftmost unequal pair* and exchange its two symbols. That same pair remains unequal, and all preceding pairs remain equal. Thus this operation is an involution without fixed points on the complement of \(E\). Every resulting two-word orbit is an edge of the adjacent-swap graph, and it remains within its fixed composition. Hence these edges constitute a matching saturating every word outside \(E\).

**3. Every unmatched word has even inversion number.** In a word from \(E\), inversions between two doubled-letter pairs occur in groups of four; inversions between a doubled pair and a final unpaired letter, when present, occur in groups of two. Within a doubled pair there are none. Consequently \(I(w)\) is even for every \(w\in E\). For each fixed-composition class, the matching partitions \(N_{\boldsymbol p}-|E\cap G_{\boldsymbol p}|\) vertices into adjacent pairs. An independent set contains at most one endpoint of each matching edge, plus potentially every unmatched vertex. Therefore
\[
\alpha(G_{\boldsymbol p})\le\frac{N_{\boldsymbol p}-|E\cap G_{\boldsymbol p}|}{2}+|E\cap G_{\boldsymbol p}|.
\]
On the other hand, every matching edge has exactly one even-inversion endpoint, and every unmatched vertex is even. Thus the even-parity independent set *attains* the displayed bound, proving equality.

**4. Count unmatched words.** If \(n=2m\), every element of \(E\) is obtained by doubling each letter of a length-\(m\) word. For composition \(\boldsymbol p\), such words exist precisely when every multiplicity is even; there are then \(m!/\prod_j(p_j/2)!\) choices. If \(n=2m+1\), the last undoubled letter contributes one to exactly one odd multiplicity; the other multiplicities must be even. There are then \(m!/\prod_j\lfloor p_j/2\rfloor!\) choices. This is exactly \(U_{\boldsymbol p}\). In the whole graph, choosing one letter for each of the \(m\) pairs and any final singleton yields \(|E|=q^{\lceil n/2\rceil}\), and substitution into the matching formula gives the claimed global optimum.

The lower and upper bounds hold for every permitted integer parameter, independent of the finite checks below.

## Verification

The standalone script `verify_adjacent.py` reconstructs the graph directly from literal adjacent unequal swaps; it checks the inversion-parity independent sets, computes a maximum bipartite matching by Hopcroft–Karp, and compares the resulting independent-set cardinality with both closed formulas, including all individual composition classes. It executed successfully for \(q=2\) and \(1\le n\le10\), \(q=3\) and \(1\le n\le7\), and \(q=4\) and \(1\le n\le5\): 22 parameter cases, 6,689 vertices, and 309 composition profiles. The binary cases test the boundary/general mechanism but are not claimed as a new binary result. These finite tests are corroboration only; Steps 1–4 provide the all-parameter proof.

## Relationship to prior work

De Alba, Carballosa, Leaños and Rivera [2, Corollary 3.11 and Theorem 3.10] obtain the independence number for binary fixed-weight words viewed as the token graph of a path. That binary instance is therefore **known** and not part of the novelty claim. It does not by itself give the full \(q\ge3\) multi-colour composition formula or the global count. Adamson, Flaherty, Potapov and Spirakis [1] study word-permutation graphs allowing swaps of any two positions, a different adjacency relation. Wang, Vu and Tan [3] develop codes *correcting* asymmetric swaps together with deletions; those correction requirements are stronger and their results do not assert the present detection optimum. Gregor, Merino and Mütze [4] study *star* transpositions rather than adjacent ones. Abdel-Ghaffar [5] studies detecting either a substitution or an adjacent transposition simultaneously, imposing an additional substitution restriction; his associated optimum is for a smaller admissible class of codes. The present formulas solve only the adjacent-swap detection problem, both in unrestricted and fixed-composition alphabets.

## Limitations

The theorem does **not** enumerate all maximum independent sets, address more than one error, nor assert that its codes can uniquely correct a swap. The binary subcase has already been established by the cited token-graph result. Although no prior all-\(q\) exact formula was located in the inspected materials, an equivalent theorem under another formulation or a more general matching theorem may exist. No independent scientific audit has been performed.

## References

[1] D. Adamson, N. Flaherty, I. Potapov and P. G. Spirakis, *Structural and Combinatorial Properties of 2-swap Word Permutation Graphs*, arXiv:2307.01648 (first public 2023-07-04), https://arxiv.org/abs/2307.01648.

[2] H. de Alba, W. Carballosa, J. Leaños and L. M. Rivera, *Independence and matching numbers of some token graphs*, arXiv:1606.06370 (2016), https://arxiv.org/abs/1606.06370.

[3] S. Wang, V. K. Vu and V. Y. F. Tan, *Codes for Correcting Asymmetric Adjacent Transpositions and Deletions*, arXiv:2301.11680 (2023), https://arxiv.org/abs/2301.11680.

[4] P. Gregor, A. Merino and T. Mütze, *Star transposition Gray codes for multiset permutations*, Journal of Graph Theory 103 (2023), DOI:10.1002/jgt.22915.

[5] K. A. S. Abdel-Ghaffar, *Detecting Substitutions and Transpositions of Characters*, The Computer Journal 41 (1998), 270–277, DOI:10.1093/comjnl/41.4.270.
