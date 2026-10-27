# Sharp open-neighborhood VC dimension of threefold categorical products of cliques

## Finding

Let \(A_1,A_2,A_3\) be finite alphabets with \(|A_i|=q_i\ge3\). On \(X=A_1\times A_2\times A_3\), form the categorical (tensor, direct) product \(G=K_{q_1}\times K_{q_2}\times K_{q_3}\): distinct vertices \(x,c\) are adjacent if and only if \(x_i\ne c_i\) for all three coordinates. Set \(\mathcal N=\{N_G(c):c\in X\}\), where \(N_G(c)\) is the **open**, not closed, neighborhood of \(c\).

**Theorem.** Write the three alphabet sizes in increasing order as \(a\le b\le c\). Then
\[
\operatorname{VCdim}(X,\mathcal N)=
\begin{cases}
3,&b=3,\\
5,&a\ge4\ \text{and}\ c\ge5,\\
4,&\text{otherwise}.
\end{cases}
\]
Thus the maximum for all threefold categorical products with at least three symbols per coordinate is five. The thresholds are sharp: the smallest three-point, four-point, and five-point witnesses occur already for alphabet triples \((3,3,3)\), \((3,4,4)\), and \((4,4,5)\), respectively.

## Assumptions and scope

A set \(S\subseteq X\) of size \(m\) is *shattered* when every subset of \(S\) equals \(S\cap N_G(c)\) for some \(c\in X\). All alphabets are finite, all sizes at least three, and there are **exactly three factors**. The theorem is not about a Cartesian graph product, closed neighborhoods, or Hamming-distance-one adjacency. There is no claim about products of four or more factors or factors of size two.

## Proof

**1. Partition reduction.** Suppose an \(m\)-element sample \(S=\{x^{(1)},\ldots,x^{(m)}\}\) is shattered. Some center \(c^0\) must realize the all-positive trace \(S\), so \(x_i^{(j)}\ne c_i^0\) for every \(i,j\). For each coordinate \(i\), partition the index set \([m]\) by equality of \(x_i^{(j)}\). Call the resulting partition \(P_i\); it has at most \(q_i-1\) blocks.

For an arbitrary center \(c\), the **excluded** sample indices are exactly the union of at most one block of each \(P_i\): coordinate \(i\) excludes the block of indices whose \(i\)-th value equals \(c_i\), or excludes nothing when \(c_i=c_i^0\). Hence \(S\) is shattered only if every subset of \([m]\) can be expressed as a union of one or zero blocks from each of \(P_1,P_2,P_3\).

Conversely, any three partitions \(P_i\) of \([m]\) into at most \(q_i-1\) blocks enjoying that union property yield a shattered sample. Assign a different nonzero symbol of \(A_i\) to every block of \(P_i\), and reserve one extra symbol \(0\) not occurring among the sample's values in coordinate \(i\). Every union of chosen blocks is the excluded-index set of the center whose coordinates equal the chosen block symbols, taking \(0\) wherever no block is chosen. In particular, all index triples of the constructed sample are distinct, because the union property supplies singleton *included* traces. This establishes an exact equivalence, not merely a necessary relaxation.

For a partition \(P\) let \(B(P)\) denote its collection of block indicator masks. The test is therefore the finite identity
\[
\{u\mathbin{\vert}v\mathbin{\vert}w:
 u\in B(P_1)\cup\{0\},\ v\in B(P_2)\cup\{0\},\ w\in B(P_3)\cup\{0\}\}
=\{0,1,\ldots,2^m-1\},
\]
where \(\vert\) in this display denotes bitwise union (not an arithmetic division), and masks encode subsets of \([m]\). For reproducibility the code uses the native bitwise OR operation.

**2. Complete six-point obstruction.** There are \(203\) set partitions of a labeled six-point set, generated once each by restricted-growth strings. A common permutation of sample indices sends the *first* partition to the canonical representative with the same sorted list of block sizes, of which there are exactly \(11\). The second and third unrestricted partitions may be exchanged, so it is enough to enumerate unordered pairs from the \(203\) choices, for each of the \(11\) representatives. This quotient covers every possible triple of six-point partitions.

Two safe pruning conditions precede the exact mask-union test. First, if all singleton excluded masks are realizable, then every sample index must be a singleton block in at least one of the three partitions: a union of nonempty blocks equaling a singleton must use a singleton block. Second, if \(A=\{u\vert v:u\in B(P_1)\cup\{0\},v\in B(P_2)\cup\{0\}\}\), then fewer than \(64\) possible pairs from \(A\times(B(P_3)\cup\{0\})\) cannot yield \(64\) distinct unions. These tests cannot discard a shattered configuration. Exactly \(27{,}375\) candidates survive both tests; exhaustive bitmask unions on all survivors yield at most \(61\) distinct patterns. Consequently no six-point sample is shattered. This excludes all larger samples as well.

**3. Sharp four- and five-point obstructions.** The same complete restricted-growth enumeration, now without symmetry pruning, gives the following finite comparisons. A bound \((r_1,r_2,r_3)\) means that partition \(P_i\) has at most \(r_i\) blocks.

| Sample size | Block caps | Partition triples | Most union traces | Shattered triples |
| --- | --- | ---: | ---: | ---: |
| \(4\) | \((2,2,4)\) | \(960\) | \(15\) of \(16\) | \(0\) |
| \(5\) | \((2,5,5)\) | \(43{,}264\) | \(28\) of \(32\) | \(0\) |
| \(5\) | \((3,3,3)\) | \(68{,}921\) | \(30\) of \(32\) | \(0\) |

If \(b=3\), two coordinate partitions have at most two blocks; the remaining coordinate has at most four blocks on four sample indices. Therefore four cannot be shattered. If \(a=3\), one coordinate partition has at most two blocks and the other two have at most five blocks on five indices, excluding shattering of five. Finally, if \(a\ge4\) but \(c\le4\), all three partitions have at most three blocks, again excluding shattering of five. The universal six-point obstruction covers all remaining cases.

**4. Attaining every claimed value.** The following ordered samples consist of coordinate triples drawn from the indicated alphabets, with symbols \(1,2,\ldots\), and all coordinates allow the reserved center symbol \(0\):

* For \((q_1,q_2,q_3)=(3,3,3)\), \(S_3=\{(1,1,1),(1,2,2),(2,1,2)\}\).
* For \((q_1,q_2,q_3)=(3,4,4)\), \(S_4=\{(1,1,1),(1,1,2),(1,2,3),(2,3,3)\}\).
* For \((q_1,q_2,q_3)=(4,4,5)\), \(S_5=\{(1,1,1),(1,2,2),(1,3,3),(2,1,2),(3,1,4)\}\).

Directly varying the center over the corresponding alphabets produces respectively \(8\), \(16\), and \(32\) traces; `verify.py` checks each trace and can reconstruct a witnessing center for every one. Enlarging alphabets preserves any existing shattered sample, since its witnessing centers remain available. Permuting coordinates likewise preserves shattering. These constructions therefore match all three upper cases and prove the theorem. \(\square\)

## Verification

Run `python3 verify.py` with Python 3.9 or newer. No additional packages or inputs are needed. The script enumerates restricted-growth strings (Bell numbers \(B_4=15\), \(B_5=52\), \(B_6=203\)), checks all three forbidden partition kernels, enumerates all eleven six-point partition shapes with a complete symmetry reduction, and evaluates all three witness samples directly in the original graph relation. All loops are finite and their coverage is justified in the proof; computations are part of the proof's finite certificate, not experimental extrapolation.

## Relationship to prior work

Adler, Benediktsson, and Macpherson [1] determine sharp open-neighborhood VC bounds for Johnson graphs and Hamming **Cartesian** products, where adjacent words differ in exactly *one* coordinate. Their Hamming Theorem 4.6 bounds that graph class by three, and Theorem 4.7 gives its exceptional parameters. Here adjacency requires differing in *all three* coordinates; the graph is a categorical rather than a Cartesian product. Theorems 4.6–4.7 therefore do not imply the present classification. The contrast is substantive: the categorical product of clique factors may have VC dimension five.

The use of tensor products of complete graphs is standard in graph theory [2]. Previous studies of this graph family involving homotopy invariants of independence or neighborhood complexes concern a different invariant; topological statements alone do not supply the precise trace-shattering thresholds above. Work on disjointness and VC dimension in communication complexity [3] concerns communication cost for restricted set families, rather than the same three-coordinate neighborhood incidence relation.

## Limitations

The result assumes three factors, each of size at least three. It does not give an exact VC dimension for any other number of factors, for binary factors, or for closed neighborhoods. The proof contains a reproducible finite exhaustive step; its reliability depends on the completeness of the partition generator, the legitimate symmetry quotient, and the bitmask-union checks, all explicitly displayed. Independent external proof or code review has not been performed. An undiscovered equivalent formulation under coordinatewise non-equality concept classes or categorical graph-product terminology remains a literature-priority risk.

## References

[1] I. Adler, B. G. Benediktsson, D. Macpherson, *Vapnik–Chervonenkis Dimension and Density on Johnson and Hamming Graphs*, arXiv:2007.16042v1, publicly posted 2020-07-31; later in *Discrete Applied Mathematics* 312 (2022), 29–44. https://arxiv.org/pdf/2007.16042.

[2] P. M. Weichsel, *The Kronecker Product of Graphs*, *Proceedings of the American Mathematical Society* 13 (1962), 47–52. https://doi.org/10.2307/2033769.

[3] A. Bhattacharya, S. Chakraborty, A. Ghosh, G. Mishra, M. Paraashar, *Disjointness through the Lens of Vapnik–Chervonenkis Dimension: Sparsity and Beyond*, *Computational Complexity* 31 (2022), article 9. https://doi.org/10.1007/s00037-022-00225-6.
