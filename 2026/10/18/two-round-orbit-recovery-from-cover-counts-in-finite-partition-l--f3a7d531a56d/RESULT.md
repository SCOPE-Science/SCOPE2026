# Two-round orbit recovery from cover counts in finite partition lattices

## Finding

Let \(n\geq1\), and let \(\Pi_n\) be the set of partitions of \([n]=\{1,\ldots,n\}\). Regard \(\Pi_n\) as a directed relational structure with \(R(P,Q)\) if and only if \(Q\) is obtained from \(P\) by merging exactly two of its blocks. Starting with one uniform vertex colour, perform synchronous one-dimensional colour refinement, recording the preceding colour and the multisets of colours among both incoming and outgoing \(R\)-neighbours.

**Theorem.** After at most two refinement rounds, two vertices have equal colours if and only if the multisets of cardinalities of their blocks agree. Thus the resulting colours are exactly the automorphism orbits of this directed Hasse structure. Their number is the integer partition function \(p(n)\). A class of block-size type \(\lambda=(1^{m_1}\cdots n^{m_n})\) contains exactly

\[
\frac{n!}{\prod_{r=1}^{n}(r!)^{m_r}m_r!}
\]

vertices. Moreover, two rounds are necessary for every \(n\geq14\): the first refinement still merges at least two distinct orbits. An exhaustive integer-partition calculation shows that one round already gives the orbit partition for \(2\leq n\leq13\); at \(n=1\) the initial one-colour partition is already the orbit partition.

## Assumptions and scope

The ground set has size \(n\geq1\), and **only the directed cover relation** (one immediate merge) belongs to the signature. In particular, \(R\) is not the full strict refinement order, its transitive closure, or the underlying undirected cover graph. No vertices are individualized and no rank predicates or block-size labels are initially supplied. Refinement round zero is the uniform colouring; rounds one and two both retain prior colours and count neighbours separately in the two directions. The claim is an orbit-classification statement *inside* each specified finite structure.

For a partition \(P\) with block sizes \(s_1,\ldots,s_k\), let \(k(P)=k\) and \(F(P)=\sum_{i=1}^k(2^{s_i-1}-1)\). The latter is the number of directed edges entering \(P\): each block of size \(s_i\) has exactly \(2^{s_i-1}-1\) unordered nontrivial two-way splittings. The number of directed edges leaving \(P\) is \(\binom{k}{2}\), obtained by choosing a pair of blocks to merge.

## Proof

**Step 1: what the first colour detects.** Since the initial colouring is uniform, round one records exactly the incoming and outgoing degrees, and therefore exactly the pair \((k(P),F(P))\). Here \(k\mapsto\binom{k}{2}\) is injective on positive integers. There is no identification ambiguity at \(k=1\): only the indiscrete partition has one block.

**Step 2: an injective arithmetic label for a merged pair.** Suppose \(R(P,Q)\) merges two blocks of sizes \(a,b\geq1\). The change in incoming degree is

\[
F(Q)-F(P)=2^{a+b-1}-2^{a-1}-2^{b-1}+1.
\]

Consequently

\[
2\bigl(F(Q)-F(P)\bigr)-1=(2^a-1)(2^b-1).\tag{1}
\]

The right-hand side uniquely determines the unordered pair \(\{a,b\}\). To prove this, write \(u\leq v\) and \(M(u,v)=(2^u-1)(2^v-1)\). The value \(1\) occurs only at \((1,1)\). If \(u<v\), then

\[
M(u,v)-1=2^u\bigl(2^v-1-2^{v-u}\bigr),
\]

whose parenthetical factor is odd, so \(\nu_2(M(u,v)-1)=u\). For \(u=v\geq2\),

\[
M(u,u)-1=2^{u+1}(2^{u-1}-1),
\]

hence \(\nu_2(M(u,u)-1)=u+1\). Two off-diagonal pairs giving the same product must have the same smaller entry, then the same larger entry. Two diagonal pairs are separated by strict monotonicity. A diagonal pair \((u,u)\), with \(u\geq2\), cannot equal an off-diagonal pair: equality of the two-adic valuations would force the latter's smaller entry to be \(u+1\), but then its product is at least \((2^{u+1}-1)^2>(2^u-1)^2\). The exceptional pair \((1,1)\) was already treated. This proves injectivity without appealing to an unproved uniqueness property of Mersenne factorizations.

**Step 3: reconstruct all block multiplicities from the second colour.** The first colour of \(P\) gives \(k(P)\) and \(F(P)\). The second colour includes the multiset of first-round colours of all immediate coarsenings \(Q\). Every such colour exposes \(F(Q)\), so equation (1) and Step 2 reconstruct the multiset

\[
\mathcal D(P)=\{\!\{\{s_i,s_j\}:1\leq i<j\leq k\}\!\},
\]

with the multiplicities of distinct merges retained. If \(k\geq2\), count every occurrence of an integer \(r\) in these unordered pairs, counting \(\{r,r\}\) twice. Each original block of size \(r\) participates in exactly \(k-1\) pairs, so this count is \(m_r(k-1)\), and division by \(k-1\) yields the exact number \(m_r\) of \(r\)-blocks. If \(k=1\), the partition is uniquely determined by its size \(n\). Thus any two vertices with equal round-two colours have the same block-size type.

Relabelling \([n]\) by its symmetric group preserves the directed cover relation, and the relabelling group is transitive on the set partitions having any fixed block-size type. Refinement cannot separate vertices in a common group orbit. Conversely, we have shown that two distinct block-size types are already separated in round two. Hence the colour classes coincide with the orbits even under the full automorphism group, and no later refinement can split them. The number of types is \(p(n)\), and choosing unordered blocks with the specified multiplicities gives the stated multinomial class size.

**Step 4: sharpness and the finite threshold.** The two distinct block-size types

\[
\lambda=(1,1,3,3,3,3),\qquad\mu=(2,2,2,2,2,4)
\]

both partition \(14\), have \(k=6\) blocks, and have \(F=12\). Their first-round colours agree, while their block-size types, and therefore their automorphism orbits, differ. For any \(n>14\), adding \(n-14\) singleton blocks to both types preserves equality of \(F\) and of their common block count, proving the lower bound for every \(n\geq14\). Finally, the finite bound \(n\leq13\) is checked by enumerating all integer partitions via the exact recurrence \(\mathcal P(t,b)=\bigcup_{j=1}^{\min(t,b)}\{\lambda\cup\{j\}:\lambda\in\mathcal P(t-j,j)\}\), with \(\mathcal P(0,b)=\{\varnothing\}\). Counting distinct \((k,F)\) signatures gives, for \(n=1,\ldots,13\), the respective values \(1,2,3,5,7,11,15,22,30,42,56,77,101\), exactly the corresponding numbers \(p(n)\). The explicit exhaustive implementation is included in the verification materials. This is a finite check; the all-\(n\) theorem follows from Steps 1–3, not from extrapolation.

## Verification

The executable file `verify_direct.py` constructs the entire directed Hasse relation for \(1\leq n\leq8\), runs two synchronous refinement rounds, and confirms equality with the block-type partition. This includes the \(4140\)-vertex partition lattice at \(n=8\). It also checks the displayed \(n=14\) first-round collision and the two-adic identity for \(4005\) unordered exponent pairs.

The separate file `verify_types.py` works on the weighted quotient by symmetric-group block types rather than enumerating individual set partitions. Its directed merge and splitting multiplicities produce an exact equitable quotient of the full graph. For every \(1\leq n\leq36\), it confirms that the second-round colours distinguish all \(p(n)\) types, and it exhaustively checks that round one succeeds precisely for \(n\leq13\). The highest tested case has \(17977\) integer partition types. Run either script with Python 3 and no nonstandard packages. Their recorded outputs are `direct_output.txt` and `types_output.txt`. The two verification methods serve as finite corroboration and a reproducible finite enumeration, not as a proof for unbounded \(n\).

## Relationship to prior work

Ehrenborg and Readdy (arXiv:1009.3976) study restricted-type partition lattices and Möbius functions; their discussion of the partition lattice and block-size types supplies combinatorial background, not colour-refinement bounds. Ehrenborg and Hedmark (arXiv:1606.01443, especially Section 2) explicitly describe the merging-block cover relation and the symmetric-group action, then pursue homology and representations of partition filters. Arvind, Köbler, Rattan and Verbitsky (arXiv:1502.01255) develop colour refinement, its orbit-partition criterion (refinability), and the hierarchy of graph classes; they do not assert this specific two-round theorem for partition-lattice Hasse relations. These classical objects and mechanisms are not claimed as discoveries. The claim here is the reconstruction of every block-size orbit from two directed-cover refinement rounds, including the exact failure of one round from size \(14\) onward.

The result is not an immediate restatement of a full-comparability-relation statement: a directed cover predicate and its transitive closure carry different one-step neighbourhood data, and neither two-round implication follows merely by renaming the relation.

## Limitations

The theorem uses both directions of the **directed** cover relation; no equivalent statement is claimed for its undirected version, for a restricted partition filter, or for arbitrary finite posets or digraphs. The recovered orbit partition does **not** establish identification of the entire lattice among arbitrary other structures by two-variable counting logic. The two-round bound is uniformly optimal, not the minimum for all individual sizes. The integer-partition table for small \(n\) is an exhaustive finite calculation. Earlier specialized unpublished or differently worded coverage is still possible; the literature comparison is not independent priority certification.

## References

1. R. Ehrenborg and M. A. Readdy, *The Möbius function of partitions with restricted block size*, arXiv:1009.3976, public preprint dated 2010-09-21.
2. R. Ehrenborg and D. Hedmark, *Filters in the partition lattice*, arXiv:1606.01443, public preprint dated 2016-06-05.
3. V. Arvind, J. Köbler, G. Rattan, O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255, first version publicly dated 2015-02-04.
