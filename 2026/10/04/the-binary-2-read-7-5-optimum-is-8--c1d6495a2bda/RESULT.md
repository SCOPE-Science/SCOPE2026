# The binary \(2\)-read \((7,5)\) optimum is \(8\)
## Finding
For binary \(2\)-read length-seven codes in the nanopore composition model, where the \(2\)-read vector records the multiset of each adjacent zero-padded pair and code distance is Hamming distance between read vectors, the maximum cardinality at minimum read distance \(5\) is exactly \(8\). The classical binary \((7,3)\) maximum is \(16\), so at the first perfect-Hamming length the necessary classical-distance reduction for \(2\)-read distance \(5\) loses a factor of two.

An explicit optimal code is
\[
\{1111111,1110000,1100110,1011100,1000001,0110011,0011001,0001110\}.
\]

## Assumptions and scope
Let \(x=(x_1,\ldots,x_7)\in\{0,1\}^7\), extended by \(x_i=0\) outside \(1\le i\le7\). Its \(2\)-read vector has eight entries, the \(i\)-th being the multiset \(\{x_{i-1},x_i\}\). A binary \(2\)-read \((7,5)_2\)-code is a subset of \(\{0,1\}^7\) in which every two distinct words have read-vector Hamming distance at least \(5\).

The statement concerns this finite binary parameter only. It does not assert an exact formula for other lengths, alphabets, read lengths, or distances.

## Proof
For a binary adjacent pair, its multiset is uniquely determined by the sum \(s_i=x_{i-1}+x_i\in\{0,1,2\}\). Thus read-vector Hamming distance is exactly the ordinary Hamming distance between the eight-symbol sum vectors \(s(x)=(s_1,\ldots,s_8)\).

Construct a graph \(G\) on all \(2^7=128\) binary words, joining \(x\) and \(y\) exactly when \(d_H(s(x),s(y))\ge5\). Then a \(2\)-read \((7,5)_2\)-code is exactly a clique of \(G\).

The supplied verifier constructs every one of the 128 read vectors directly and checks the sum representation against an independent representation by sorted two-element multisets. It then computes \(\omega(G)\) in two independent exact searches. The first is a bit-set branch-and-bound maximum-clique search whose greedy coloring of every remaining candidate subgraph gives a rigorous upper bound on any extension. The second enumerates maximal cliques by a Bron--Kerbosch search with pivoting. Both return \(\omega(G)=8\). The displayed eight-word set is separately checked pairwise and therefore gives the matching lower bound.

For comparison, every binary classical \((7,3)\)-code has at most \(16\) words because radius-one Hamming balls have size \(8\) and are disjoint. The standard length-seven Hamming code has \(16\) words and minimum distance \(3\), so the classical optimum is exactly \(16\).

## Verification
Run `python verify.py`. It reconstructs the read-vector graph from definitions, checks all pair distances under two read-vector encodings, runs both exact clique procedures, verifies the explicit witness, and independently constructs the standard binary length-seven Hamming code. The expected terminal line is `VERIFY_OK`.

## Relationship to prior work
Banerjee--Yehezkeally--Wachter-Zeh--Yaakobi introduced the composition/read-vector nanopore model. Sun--Ge subsequently studied \(2\)-read codes under Hamming distance, including minimum distance \(5\), and related that regime to classical distance-three codes. Their paper gives asymptotic redundancy bounds for \(2\)-read distance \(5\); the inspected definitions, distance-five section, summary tables, and conclusion do not state the exact binary length-seven optimum above.

The exact value \(8\) is not implied by the classical reduction alone: at length seven that reduction permits as many as \(16\) words. The finite computation therefore quantifies a strict loss caused by the read-vector constraint at the first nontrivial perfect-Hamming length.

## Limitations
The proof is exhaustive and exact only for binary length \(7\), read length \(2\), and minimum read distance \(5\). No asymptotic improvement is claimed. An unindexed finite computation of this small parameter could exist despite the literature searches reported in the review; this remains the principal originality risk.

## References
1. A. Banerjee, Y. Yehezkeally, A. Wachter-Zeh, and E. Yaakobi, “Error-Correcting Codes for Nanopore Sequencing,” arXiv:2305.10214, first public version 2023-05-17.
2. Y. Sun and G. Ge, “Bounds and Constructions of \(\ell\)-Read Codes under the Hamming Metric,” arXiv:2403.11754, first public version 2024-03-18.
