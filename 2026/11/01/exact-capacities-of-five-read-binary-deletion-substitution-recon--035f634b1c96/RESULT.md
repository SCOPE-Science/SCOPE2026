# Exact capacities of five-read binary deletion–substitution reconstruction codes through length nine

## Finding

For an integer \(n\ge3\) and a binary word \(x\in\{0,1\}^n\), define the distinct-output ball \(\mathcal B(x)\) by deleting exactly one symbol and then making zero or one binary substitutions. A five-read reconstruction code is a set \(C\subseteq\{0,1\}^n\) such that any distinct \(x,y\in C\) satisfy \(|\mathcal B(x)\cap\mathcal B(y)|<5\). Write \(A_5(n)\) for the maximum size of such a code. The complete initial capacity profile is

\[
\boxed{(A_5(3),A_5(4),A_5(5),A_5(6),A_5(7),A_5(8),A_5(9))=(8,5,5,6,8,12,16).}
\]

The nonmonotonic transition from \(8\) at length \(3\) to \(5\) at length \(4\) is a genuine feature of fixed-five-read reconstruction: increasing word length also enlarges error balls. At length \(9\), the exact largest code has \(16\) words, so its optimal redundancy is \(9-\log_2(16)=5\) bits.

## Assumptions and scope

The alphabet is binary; the input length is an integer \(3\le n\le9\); the channel performs exactly one deletion and *at most* one substitution (zero substitutions are allowed). Outputs and intersections are **sets of distinct words**, not multisets of editing histories. The five reads are distinct. The claim concerns maximum codebook cardinalities, not decoding algorithms, code uniqueness, or all lengths.

For a length-\(n\) word \(x\), define \(D_i(x)\) as the word obtained by removing coordinate \(i\). If \(y\) is a word of length \(n-1\), put \(H_1(y)=\{z:d_H(z,y)\le1\}\). Then

\[
\mathcal B(x)=\bigcup_{i=1}^{n}H_1(D_i(x)).
\]

This identity defines the channel exactly and is also the specification used by the verification code.

## Proof

**Finite graph reduction.** For each permitted length, form a simple graph \(G_n\) whose vertices are all \(2^n\) binary words and whose distinct vertices \(x,y\) are adjacent precisely when \(|\mathcal B(x)\cap\mathcal B(y)|<5\). By the reconstruction-code definition, \(A_5(n)\) is the clique number \(\omega(G_n)\). The file `verify.py` constructs *every* vertex, ball, and potential edge directly from the preceding set identity. In particular it considers all \(\binom{2^n}{2}\) unordered input pairs; no sampling or probabilistic inference enters this reduction.

**Lower bounds.** The following table lists explicitly a clique of the claimed size at each length. Each integer \(v\) represents the unique length-\(n\) binary word with numerical value \(v\), padded by leading zeros. The verifier checks every pair in each listed clique against the underlying distinct-output balls.

| \(n\) | \(A_5(n)\) | Explicit codeword values | Edges of \(G_n\) |
|---:|---:|---|---:|
| 3 | 8 | 0,1,2,3,4,5,6,7 | 28 |
| 4 | 5 | 0,3,8,14,15 | 38 |
| 5 | 5 | 0,7,17,28,31 | 115 |
| 6 | 6 | 0,3,15,28,49,63 | 552 |
| 7 | 8 | 127,124,115,96,79,24,3,0 | 2917 |
| 8 | 12 | 255,248,243,224,207,129,126,50,31,76,7,0 | 15194 |
| 9 | 16 | 511,508,499,455,480,385,415,294,204,280,181,126,112,15,3,0 | 75483 |

**Exhaustive upper bounds.** The self-contained program implements a complete maximum-clique search over \(G_n\). At every recursive call it maintains a set \(P\) of possible next vertices, all adjacent to the vertices already selected. It greedily partitions \(P\) into independent sets, giving a proper coloring with color classes \(1,\ldots,c\). Any clique in a union of its first \(j\) color classes has at most \(j\) vertices. Ordering candidates by nondecreasing color, the search branches in reverse order. For a candidate \(v\), the recursive candidate set is exactly \(P\cap N(v)\), after which \(v\) is deleted from \(P\). Consequently every clique is represented in some branch. The only pruning is when the size of the current clique plus the maximum number of remaining color classes cannot exceed an already found clique; the preceding independent-set argument proves such a branch cannot improve the incumbent.

The algorithm therefore returns the exact clique number, not a heuristic or an unverified optimization output. Its independently checkable execution for \(n=3,4,5,6,7,8,9\) returns respectively \(8,5,5,6,8,12,16\), matching all the explicit witnesses. This proves every entry of the asserted profile.

## Verification

Run `python3 verify.py` using Python 3 with no third-party dependencies. It reconstructs all distinct channel outputs in two independently implemented ways: first by direct deletion-and-bit-flip generation; second by checking Hamming distance from every deletion descendant. It checks agreement for **every input word at every stated length**. It then constructs all compatibility edges, checks the explicit witnesses, performs the exhaustive coloring-bound search, and asserts the claimed maxima.

The exact per-length edge counts and explored search nodes are recorded in `verification_output.txt`; the final status is `EXACT_CERTIFICATE_OK`. The most demanding case, \(n=9\), searches a graph with \(512\) vertices, \(75{,}483\) compatible edges and \(416{,}465\) recursive calls. Independent cross-checks using a second exact maximum-clique implementation reproduced the values at lengths \(6\) through \(9\). The finite exhaustive computation, whose correctness argument is given above, is the proof of the numerical upper bounds; these numbers are not inferred from sparse tests.

## Relationship to prior work

Li, Sun and Ge's 2026 paper studies the same one-deletion/at-most-one-substitution channel and proves a family of five-read codes with redundancy \(3\log_2 n+4\) (Theorem 4.6). It does **not** give exact maximum codebook sizes for small lengths; the present result supplies the missing finite capacity profile, not a claimed improvement to its general asymptotic construction. Their 2025 paper treats other read counts, including seven, and explicitly calls for additional constant-read constructions. Song, Cai and Quek establish a general intersection bound for codewords at Hamming distance at least two; that bound is neither this small-blocklength optimum nor a stronger bound implying the displayed seven exact values. Related exact finite code-size records for ordinary single-error correction or other mixed channels concern different compatibility relations, rather than five distinct reads from the present channel.

## Limitations

The exact result stops at \(n=9\). It does not establish a closed formula or asymptotic capacity for general \(n\), classify all optimal codes, or assert that the listed witnesses are unique. The code is a transparent finite proof with complete enumeration and a sound pruning rule; it is not an infinite-family proof. Publication-priority comparisons were made against the relevant published primary sources and available indexed claims; an unindexed earlier finite table remains a residual risk. An independent mathematical audit has not been performed.

## References

1. Y. Li, Y. Sun and G. Ge, *Correcting One Deletion and One Substitution with a Constant Number of Reads*, first publicly submitted 28 April 2026, arXiv:2604.25294. https://arxiv.org/abs/2604.25294 (definition in Section II; five-read construction in Section IV.D; conclusion in Section VI).
2. Y. Li, Y. Sun and G. Ge, *Binary Reconstruction Codes for Correcting One Deletion and One Substitution*, first submitted 7 May 2025, arXiv:2505.04232. https://arxiv.org/abs/2505.04232 (problem statement, construction summary, and Section VI).
3. W. Song, K. Cai and T. Q. S. Quek, *Sequence Reconstruction for the Single-Deletion Single-Substitution Channel*, first submitted 7 January 2025, arXiv:2501.03833. https://arxiv.org/abs/2501.03833 (main read-coverage theorem and its Hamming-distance hypothesis).
