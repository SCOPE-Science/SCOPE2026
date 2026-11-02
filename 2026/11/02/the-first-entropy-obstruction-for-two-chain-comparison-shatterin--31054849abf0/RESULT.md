# The first entropy obstruction for two-chain comparison shattering

## Finding
Let \(A_1<\cdots<A_a\) and \(B_1<\cdots<B_b\) be two disjoint chains, where \(a,b\ge1\). Let \(\mathcal S_{a,b}\) consist of the \(\binom{a+b}{a}\) linear extensions of their disjoint union, represented by Boolean queries \(q_{i,j}\) asking whether \(A_i\) precedes \(B_j\). Put \(H_{a,b}=\lfloor\log_2\binom{a+b}{a}\rfloor\).

**Sharp first entropy obstruction.** Every two-chain profile with \(a+b\le6\) attains the cardinality upper bound \(\operatorname{Ldim}(\mathcal S_{a,b})=H_{a,b}\). Among profiles with \(a+b=7\), exactly the unordered profile \(\{a,b\}=\{3,4\}\) fails to attain it:
\[
\operatorname{VCdim}(\mathcal S_{3,4})=3,\qquad
\operatorname{Ldim}(\mathcal S_{3,4})=4<5=H_{3,4}.
\]
For background, the exact static formula for every profile is \(\operatorname{VCdim}(\mathcal S_{a,b})=\min\{a,b\}\). The novelty assessment concerns the unique first adaptive entropy obstruction at seven elements, not the standard static formula or any previously determined two-row ideal ranks.

## Assumptions and scope
All orders are strict on labeled elements, and queries compare one element from each chain; comparisons inside a chain are constant and omitted. A complete adaptive shattering tree of depth \(d\) has a query at each internal node and realizes all \(2^d\) binary answer paths. The Littlestone dimension is the largest such \(d\). For a finite class with \(N\) distinct concepts it is at most \(\lfloor\log_2 N\rfloor\). The claims concern precisely the two-chain linear-extension classes, not arbitrary partial orders with the same number of elements.

## Proof
**1. Grid representation and VC dimension.** Encode an interleaving by its nondecreasing gap vector \(0\le g_1\le\cdots\le g_a\le b\), where \(g_i\) counts the \(B\)-elements before \(A_i\). Its answer to \(q_{i,j}\) is \(1\) exactly when \(g_i<j\). Consequently the positive-answer sets are precisely the order ideals of the rectangular product order on \([a]\times[b]^{\mathrm{op}}\) (with coordinates oriented so that positive implication means downward closure). A support of ideal-membership queries is VC-shattered exactly when it is an antichain: comparable queries cannot realize the forbidden reverse labeling, while every subset of an antichain extends to an ideal. The grid has width \(\min\{a,b\}\), witnessed by a diagonal and bounded by its row and column chain partitions. This gives the stated static formula.

**2. First-query obstruction.** For a query \(q_{i,j}\), write \(N_{i,j}\) for the number of interleavings in which \(A_i\) precedes \(B_j\). Counting by the overall position \(p\) of \(A_i\) gives the exact finite sum
\[
N_{i,j}=\sum_{p=i}^{i+j-1}\binom{p-1}{i-1}\binom{a+b-p}{a-i}.
\]
A complete depth-five shattering tree needs at least sixteen concepts realizing each answer to its root query. At \((a,b)=(3,4)\), the smaller of \(N_{i,j}\) and \(35-N_{i,j}\), tabulated by rows \(i=1,2,3\) and columns \(j=1,2,3,4\), is respectively
\[
(15,10,4,1),\quad(5,13,13,5),\quad(1,4,10,15).
\]
Every root query therefore has a branch with at most fifteen concepts, so depth five is impossible. This is an exhaustive first-query obstruction, not an extrapolation from sampled trees.

**3. Matching lower bounds and minimality.** The attached `witnesses.json` contains full depth-two, depth-three, and depth-four adaptive trees for profiles \((2,2)\), \((2,3)\), and \((3,3)\), plus a depth-four tree for \((2,5)\), needed to check the nonexceptional seven-element profile. Each leaf specifies an actual interleaving satisfying the entire answer path. `verify.py` checks these witnesses directly and separately computes the exact Littlestone recurrence on all relevant smaller classes. Appending new \(B\)-elements at the end embeds \(\mathcal S_{a,b}\) into \(\mathcal S_{a,b'}\) for \(b'\ge b\), preserving the old query answers, and hence cannot lower Littlestone dimension. This gives the lower bound four for \((3,4)\) from \((3,3)\), and transfers the depth-three and depth-four witnesses to intermediate profiles. When one chain has length one, the concept class is a threshold class on \(b+1\) ordered insertion gaps, of dimension \(\lfloor\log_2(b+1)\rfloor\), exactly its cardinality bound. Together these cases cover every unordered positive two-chain profile with total size at most seven. Thus the first-obstruction threshold and its uniqueness within that range are sharp.

## Verification
The reproducible package includes `verify.py`, `witnesses.json`, and `verification_output.txt`. Run `python verify.py` with these files together. The checker enumerates gap vectors using combinations with repetition, rather than generating shuffled words as the witness constructor did. It checks each branching node and the path-realizing leaf at every certificate position; applies the exact recursive Littlestone definition on twelve unordered profiles through seven elements; compares directly computed split counts with the binomial sum; and verifies static dimensions on the twelve profiles. The resulting output begins `ALL_TWO_CHAIN_COMPARISON_CHECKS_PASS` and records four valid tree certificates. A finite checker is only supporting evidence: the exact upper bounds and small-profile exhaustive coverage are proved above.

## Relationship to prior work
Chase and Freitag, *Bounds in Query Learning* (first public arXiv version, 23 April 2019), develops Littlestone dimension and general query-learning bounds but does not state the three-by-four first root-split threshold in the inspected full text. Chase, Freitag, and Reyzin's later query-learning article (arXiv 2023; MFCS 2024) likewise studies general expected-query and compression results, rather than these exact interleaving dimensions. Eiben, Ganian, Kangas, and Ordyniak study counting linear extensions and parameterized complexity; their article supplies related poset context but no adaptive-shattering statement in its inspected open full text. The standard correspondence between two-chain interleavings and ideals of a rectangular grid is used, not claimed as original. Previously available research already gives an exact recurrence for all two-row grid ideals, including the two-element-chain family; that result is treated as prior coverage and no new claim about this covered subfamily is made. Searches also considered Ferrers diagrams, monotone lattice paths, merge comparisons, order ideals, aliases for online shattering, and previously available mathematical records.

## Limitations
No all-parameter formula for \(\operatorname{Ldim}(\mathcal S_{a,b})\) is claimed beyond the sharp parameter ranges identified. The results do not extend the existing complete two-row ideal recurrence to three rows or give an all-size three-row recurrence. They do not determine optimal adaptive identification complexity or worst-case merge-sorting cost, which are different optimization problems. Priority relative to older, differently named studies of adversarial comparison-tree lower bounds and order-ideal shattering may remain unresolved despite the indicated searches. The verification is not an independent external audit.

## References
1. H. Chase and J. Freitag, *Bounds in Query Learning*, arXiv:1904.10122v1, first submitted 2019-04-23. https://arxiv.org/abs/1904.10122
2. H. Chase, J. Freitag, and L. Reyzin, *Applications of Littlestone dimension to query learning and to compression*, arXiv:2310.04812, first submitted 2023-10-07; MFCS 2024. https://arxiv.org/abs/2310.04812
3. E. Eiben, R. Ganian, K. Kangas, and S. Ordyniak, *Counting Linear Extensions: Parameterizations by Treewidth*, Algorithmica 81 (2019), online 2018-09-04. https://doi.org/10.1007/s00453-018-0496-4
