# Entropy-saturating online comparisons of involutions through ten letters

## Finding

Let \(\mathcal V_n\) consist of the binary functions \(h_\pi\) on the unordered pairs \(Q_n=\{\{i,j\}:1\le i<j\le n\}\), where \(\pi\) ranges over the involutions of \([n]\) and \(h_\pi(\{i,j\})=1\) precisely if \(\pi(i)<\pi(j)\). For all integers \(n\ge1\),
\[
\operatorname{VCdim}(\mathcal V_n)=n-1.
\]
For every \(1\le n\le10\), its Littlestone dimension reaches the exact hypothesis-cardinality bound:
\[
\operatorname{Ldim}(\mathcal V_n)=\lfloor\log_2 I_n\rfloor,
\qquad I_0=I_1=1,\quad I_n=I_{n-1}+(n-1)I_{n-2}.
\]
In order \(n=1,\ldots,10\), the values are \(0,1,2,3,4,6,7,9,11,13\), while the involution counts are \(1,2,4,10,26,76,232,764,2620,9496\). In particular the first strict static/adaptive separation is at six letters and the gap at ten letters is four.

For each positive integer \(s\), the same concept class on \(10s\) letters satisfies
\[
\operatorname{Ldim}(\mathcal V_{10s})\ge13s,
\qquad \operatorname{Ldim}(\mathcal V_{10s})-\operatorname{VCdim}(\mathcal V_{10s})\ge3s+1.
\]
This yields an unbounded adaptive-over-static separation inside the family of inverse-symmetric permutations. It does not assert an exact Littlestone dimension beyond ten letters.

## Assumptions and scope

An involution is a permutation \(\pi\) satisfying \(\pi(\pi(i))=i\) for all \(i\); fixed points are permitted. Positions and values both use the natural order on \([n]\). At a query \(\{i,j\}\) with \(i<j\), the answer is one when the value in position \(i\) is smaller than the value in position \(j\). VC dimension means fixed-set shattering; Littlestone dimension means a full adaptive binary mistake tree with a consistent hypothesis at every leaf. Neither parameter is a worst-case number of comparisons needed to identify a target.

## Proof

**VC upper bound.** Regard any shattered family of queries as edges of a simple graph on \([n]\). A cycle cannot be present. Indeed, independently orient its queried comparisons to demand \(\pi(v_1)<\pi(v_2)<\cdots<\pi(v_k)<\pi(v_1)\), an impossible cyclic strict inequality. Hence every shattered support is a forest, containing at most \(n-1\) edges. This argument applies even to unrestricted permutations.

**VC lower bound.** Query the \(n-1\) adjacent pairs \(\{i,i+1\}\). For any prescribed pattern of descents, partition \([n]\) into maximal consecutive blocks on which every adjacent comparison must be descending; put cuts wherever an ascent is required. Reverse each block internally, assigning its values from the same consecutive interval. The resulting permutation is the direct sum of reversals of contiguous blocks, hence an involution. Comparisons inside each block are descending, and comparisons across cuts are ascending. Thus all \(2^{n-1}\) patterns are realized. The case \(n=1\) has zero query coordinates. Combining the two bounds proves the VC formula.

**Finite Littlestone upper bounds.** Every involution either fixes the final letter or transposes it with one of the preceding \(n-1\) letters. These disjoint possibilities give \(I_n=I_{n-1}+(n-1)I_{n-2}\) with \(I_0=I_1=1\). Distinct involutions induce distinct full comparison vectors (a strict total order determines its permutation). A complete depth-\(d\) tree needs at least \(2^d\) different hypotheses, since a single hypothesis cannot realize two different root-to-leaf bit strings. Therefore \(\operatorname{Ldim}(\mathcal V_n)\le\lfloor\log_2 I_n\rfloor\).

**Finite Littlestone lower bounds.** `adaptive_certificates.json` explicitly gives a full depth-\(\lfloor\log_2 I_n\rfloor\) tree for every integer \(2\le n\le10\), including a distinct involution witness at every terminal node. It stores node queries in binary-heap order and witness indices in left-to-right leaf order. Queries are indexed by lexicographically sorted pairs with zero-based coordinates; bit zero follows the left child and bit one the right child. Involutions are indexed as lexicographically sorted zero-based tuples. The proof obligation is finite and local: at each leaf, every comparison on the path equals the branch bit. `verify_certificates.py` independently constructs the involution catalogue using the final-letter fixed-or-transposed recursion and checks all paths, all leaf witnesses, the exact concept counts, and the cardinality inequalities. Thus the lower and upper bounds agree for all listed orders, including \(n=10\), where the certificate has \(8191\) internal queries and \(8192\) distinct leaf involutions. At \(n=1\), the only hypothesis gives depth zero.

**Unbounded gap.** For each \(s\ge1\), divide the \(10s\) positions into consecutive blocks of ten. Take involutions that independently permute each block as a ten-letter involution while fixing the set of values used by that block. These are legitimate global involutions. On queries internal to a block, their comparisons agree exactly with the ten-letter class. Concatenate \(s\) copies of its depth-thirteen adaptive tree, successively querying each block, to obtain a complete tree of depth \(13s\). The all-order VC formula gives \(10s-1\), proving the asserted difference \(3s+1\).

## Verification

The supplied `build_certificates.py` computes lower-bound trees by exact two-branch recursion over subsets of the explicit involution catalogue. The separate `verify_certificates.py` does not use that search recurrence; it reconstructs involutions by insertion of the largest label as either a fixed point or one end of a transposition. The verifier independently replays every tree edge against every leaf's labeled permutation and checks distinctness of all leaf witnesses. It additionally enumerates every adjacent-descent pattern through ten letters and verifies the constructive reversal-of-blocks argument. Run `python3 verify_certificates.py` in the same directory as `adaptive_certificates.json` using a standard Python installation. The observed final line was `ALL_INDEPENDENT_CHECKS_PASS`.

The exact finite result is proved by a replayable certificate plus a general cardinality upper bound, not by statistical sampling. The infinite amplification uses only the proved ten-letter certificate and direct sums; no extrapolation of the finite dimension table is used.

## Relationship to prior work

Littlestone dimension is the adaptive shattering invariant standard in online learning; Guingona, Kolesnikov, Nierwinski and Soucy (2021) establish corresponding structural formulas for a different zero-set concept family. Gene Kim (2017) studies descent distributions of fixed-point-free involutions (perfect matchings); that enumeration/statistical problem neither treats all involutions with fixed points nor determines adaptive comparison trees. Comparison shattering of all permutations, even permutations, and restricted avoidance classes concerns other hypothesis sets and does not imply a lower-bound tree for the proper subclass of involutions. The fixed-set bound \(n-1\), and the counts \(I_n\), are included as structural background; the substantive result here is entropy saturation through ten letters and its blockwise unbounded-gap consequence. Searches did not establish global priority; a different formulation of the same adaptive comparison problem might exist.

## Limitations

The exact Littlestone values are proved only for \(1\le n\le10\); the lower bound on the subsequence \(n=10s\) does not classify other dimensions or prove entropy saturation at larger orders. No independent expert audit has been performed. The novelty assessment is limited to examined accessible sources and research-record searches; historical-priority uncertainty remains, especially under inverse-symmetric ranking or matching comparison terminology.

## References

1. Gene B. Kim, *Distribution of descents in matchings*, arXiv:1710.03896v1 (11 October 2017), https://arxiv.org/html/1710.03896v1.
2. Vincent Guingona, Alexei Kolesnikov, Julie Nierwinski and Richard Soucy, *Littlestone and VC-dimension of families of zero sets*, arXiv:2109.04805v1 (10 September 2021), https://arxiv.org/abs/2109.04805.
