# Two-zero contraction and the exact census of shortest run-limited universal necklaces

## Finding

Let \(r\ge2\). A circular binary word is *admissible* when its periodic extension contains no contiguous run \(0^r\). An admissible word is *universal at order \(r+1\)* if its cyclic windows contain every binary word of length \(r+1\) avoiding \(0^r\). Words differing only by cyclic rotation are one necklace; reversal and bit complementation are **not** identified.

**Theorem.** Every shortest such necklace has length
\[
L_r=2^{r+1}-2.
\]
Its cyclic \(r+1\)-factor multiset consists of every one of the \(2^{r+1}-3\) permissible factors exactly once, with one additional occurrence of \(e_r=10^{r-1}1\). Moreover, the number of distinct shortest necklaces is
\[
\boxed{N_r=2^{2^r-r-2}}\qquad(r\ge2).
\]
More precisely, deleting two zeros from the unique cyclic run \(0^{r+1}\) in each ordinary binary de Bruijn cycle of order \(r+1\) is a **two-to-one surjection** onto the optimal necklaces. The inverse choices are the two occurrences of \(e_r\) in each shortest necklace.

Thus \(N_2=1\), \(N_3=8\), \(N_4=1024\), and \(N_5=33554432\). The new contribution is the complete, all-order necklace count and the explicit covering map; the sharp minimum-length phenomenon belongs to the previously studied zero-run covering problem.

## Assumptions and scope

A cyclic window is read with indices modulo the full word length, including wraparound. The binary symbols are labeled. Every permitted factor must appear at least once, not necessarily exactly once. We take \(r\ge2\); this excludes the degenerate one-symbol admissibility case. A standard binary de Bruijn cycle of order \(k\) has length \(2^k\) and contains every length-\(k\) binary factor exactly once. Its classical number up to rotation is \(2^{2^{k-1}-k}\). The argument below works with necklaces rather than distinguished starting positions.

## Proof

**1. Permitted edges and the first obstruction.** Exactly three binary length-\(r+1\) words contain \(0^r\):
\[
0^{r+1},\qquad 0^r1,\qquad 10^r.
\]
Hence there are \(2^{r+1}-3\) permitted windows. Associate to each permitted word the directed edge from its length-\(r\) prefix to its length-\(r\) suffix, in the order-\(r\) binary de Bruijn graph. The vertex \(0^r\) is absent. Every surviving vertex has two incoming and two outgoing edges except
\[
u=10^{r-1},\qquad v=0^{r-1}1,
\]
where the first has indegree two and outdegree one, and the second has indegree one and outdegree two. These vertices are distinct for \(r\ge2\).

If a cyclic universal word had exactly \(2^{r+1}-3\) windows, it would traverse every permitted edge exactly once, contradicting the degree imbalance. Therefore at least one additional edge occurrence is required. With exactly one additional occurrence, balance forces that edge to leave \(u\) and enter \(v\). The unique permitted edge with this pair of endpoints is
\[
e_r=10^{r-1}1.
\]
This proves the lower bound and the necessary complete multiplicity profile of every possible minimizer.

**2. A contraction from ordinary de Bruijn cycles.** Take any ordinary binary de Bruijn cycle \(D\) of order \(r+1\). Its only occurrence of \(0^{r+1}\) is a run of exactly \(r+1\) zeros, bounded on both sides by ones: extending it would repeat \(0^{r+1}\). In the order-\(r\) de Bruijn graph, that run corresponds to the unique three-edge passage
\[
u\xrightarrow{10^r}0^r\xrightarrow{0^{r+1}}0^r\xrightarrow{0^r1}v.
\]
Delete the central zero vertex and replace this three-edge passage by one additional copy of the edge \(u\xrightarrow{e_r}v\), parallel to the original copy. In terms of circular words this deletes precisely two zeros from the run. Every other original edge remains, and the three deleted original edges are exactly the forbidden factors. The resulting circular word therefore avoids \(0^r\), contains all allowed \(r+1\) factors, repeats \(e_r\) twice, and has length \(2^{r+1}-2\). This attains the lower bound.

**3. Inverse choices, exactly two.** Conversely, any shortest admissible universal necklace has, by Step 1, precisely the complete multiset of permitted edges with \(e_r\) duplicated. Its two occurrences of \(e_r\) are at distinct cyclic starting positions. Replace either occurrence by the three-edge passage displayed in Step 2 (equivalently, insert two zeros into that occurrence's run of \(r-1\) zeros). The resulting Eulerian circuit uses all \(2^{r+1}\) edges of the full binary de Bruijn graph exactly once, hence is an ordinary de Bruijn cycle of order \(r+1\). These are the only inverses, because the unique forbidden zero vertex in any full de Bruijn cycle must be expanded from one of the two copies of \(e_r\).

The two reconstructed de Bruijn necklaces are distinct: each has a unique occurrence of \(0^{r+1}\), and contracting it returns the same shortest necklace with a distinguished choice of one of its two distinct \(e_r\) occurrences. An isomorphism by rotation preserving this distinction would require a nontrivial period of the shortest necklace, which is impossible because its factor multiset contains permitted factors with multiplicity one. Therefore the contraction map is exactly two-to-one.

**4. Count.** The classical de Bruijn cycle formula gives
\[
B_{r+1}=2^{2^r-(r+1)}.
\]
Division by the two inverse choices established in Step 3 yields
\[
N_r=B_{r+1}/2=2^{2^r-r-2},
\]
completing the proof for every integer \(r\ge2\). \(\square\)

## Verification

The standalone standard-library `verify.py` checks all circular binary words at \(r=2\) and \(r=3\), yielding respectively one and eight distinct optimum necklaces, and checks that every candidate has the exact claimed factor profile. It independently evaluates integer Laplacian cofactors of the augmented de Bruijn graph by fraction-free elimination for \(2\le r\le6\), obtaining the expected counts of directed rooted trees. Finally it constructs 225 randomized Euler tours for \(2\le r\le10\), checking lengths, forbidden runs and the full factor multisets. Run `python3 verify.py`. Exhaustive small cases and exact finite determinants corroborate the all-order bijective proof; they cannot substitute for it.

## Relationship to prior work

The ordinary de Bruijn necklace formula and Euler-tour description are classical. Moreno and Matamala (2007) study *lexicographically minimal* de Bruijn sequences for languages defined by forbidden substrings, with each selected factor once; their language definition imposes cyclic admissibility on a candidate factor itself. Chee and collaborators (2020) consider a different constraint, preventing nearby repetitions of windows, and develop enumeration techniques. Bernardini and collaborators (2021) address construction and sanitization of strings avoiding forbidden factors, not this exact circular covering enumeration. The previously known sharp zero-run covering length and balancing profile agree with Step 1; our contribution is the exact number of optimal necklaces and a two-to-one explicit relation to unconstrained cycles. None of the located comparison statements supplies that all-order enumeration directly.

## Limitations

The claim concerns a single forbidden monochromatic run and window length exactly one more than the forbidden run. It does not enumerate arbitrary forbidden sets, other window lengths, larger alphabets, linear covering words or dihedral equivalence classes. The usual limitation of literature searching remains: an unindexed or differently phrased equivalent statement could exist. The proof establishes the all-order result independently of the finite checks, but no independent mathematical audit is asserted.

## References

- E. Moreno and M. Matamala, *Minimum de Bruijn Sequence in a Language with Forbidden Substrings*, arXiv:0711.1695 (first public 2007-11-12), https://arxiv.org/html/0711.1695v1.
- Y. M. Chee, T. Etzion, H. M. Kiah, A. Vardy, V. K. Vu and E. Yaakobi, *Constrained de Bruijn Codes: Properties, Enumeration, Constructions, and Applications*, arXiv:2005.03102 (first public 2020-05-06), https://arxiv.org/abs/2005.03102.
- G. Bernardini, A. Marchetti-Spaccamela, S. P. Pissis, L. Stougie and M. Sweering, *Constructing Strings Avoiding Forbidden Substrings*, CPM 2021, DOI: 10.4230/LIPIcs.CPM.2021.9, https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CPM.2021.9.
- Classical de Bruijn enumeration: N. G. de Bruijn, *A combinatorial problem*, 1946; the formula is also recalled in Chee et al. (2020), above.
