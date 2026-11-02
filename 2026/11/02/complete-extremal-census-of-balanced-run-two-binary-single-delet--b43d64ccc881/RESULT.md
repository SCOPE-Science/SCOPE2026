# Complete extremal census of balanced run-two binary single-deletion codes through length ten

## Finding
Let \(n\in\{4,6,8,10\}\). Define the admissible set
\[
\mathcal W_n=\{x\in\{0,1\}^n:|x|_1=n/2,\ \text{neither }000\text{ nor }111\text{ is a contiguous factor of }x\}.
\]
For each \(x\in\mathcal W_n\), let \(\Delta(x)\) be its **set** of length-\(n-1\) strings obtained by deleting one position. A code \(C\subseteq\mathcal W_n\) corrects one deletion if the shadows \(\Delta(x)\) of distinct codewords are disjoint.

The admissible-word counts, maximum code cardinalities, and numbers of **labeled** maximum codebooks are exactly:

| \(n\) | \(|\mathcal W_n|\) | \(\max |C|\) | Number of maximum codebooks |
|---:|---:|---:|---:|
| 4 | 6 | 2 | 4 |
| 6 | 14 | 4 | 4 |
| 8 | 34 | 8 | 1 |
| 10 | 84 | 15 | 20 |

At length eight, the unique maximum codebook is the modified Varshamov–Tenengolts syndrome class \(\sum_{i=1}^{8}i x_i\equiv3\pmod5\) inside \(\mathcal W_8\). At length ten, exactly two of the twenty maximum codebooks are full modified-VT syndrome classes (syndromes \(3\) and \(4\) modulo \(6\)); the other eighteen are not full syndrome classes. Reversal and global bit-complementation partition the twenty length-ten maxima into eight orbits, six of size two and two of size four. The accompanying `maxima.json` gives every maximum codebook in lexicographically sorted literal binary words.

## Assumptions and scope
Words are **linear**, not circular; triple avoidance is checked only at positions inside a word, not across its endpoints. Each word has exact Hamming weight \(n/2\), and distinct codebooks are distinguished as literal subsets without quotienting by coordinate transformations. Deletion positions may yield the same descendant, so \(\Delta(x)\) is a set, not a multiset. The channel deletes exactly one symbol, with unknown location; no substitutions or multiple deletions are included. The classification concerns precisely the four displayed even lengths.

## Proof
**Graph reduction.** Construct the finite graph \(G_n\) on vertices \(\mathcal W_n\), with two different vertices adjacent exactly when their one-deletion sets are disjoint. The channel's definition gives the equivalence
\[
C\text{ corrects one deletion}\quad\Longleftrightarrow\quad C\text{ is a clique of }G_n.
\]
Every maximum clique is maximal. It is therefore enough to enumerate **all maximal cliques** and identify those of largest size.

**Exhaustive vertex construction.** The checker enumerates every size-\(n/2\) subset of \(\{0,\ldots,n-1\}\), forms the corresponding binary word, and rejects a word if it contains `000` or `111`. This tests all \(\binom n{n/2}\) possible balanced words without sampling. Every deletion shadow is constructed by deleting each of the \(n\) positions, then deduplicating descendants. Every unordered vertex pair is tested for disjointness. As an independent graph-construction check, the program also groups vertices by shared deletion descendants and verifies that this complement conflict relation agrees on **every** unordered pair.

**Complete clique enumeration.** The self-contained `verify_census.py` implements the Bron–Kerbosch recursion with pivoting using exact integer bit masks. In a recursive call, \(R\) is a clique; \(P\) consists of unused common neighbors eligible to extend \(R\), and \(X\) consists of already processed common neighbors. Choosing a pivot \(u\in P\cup X\), every as-yet unreported maximal clique extending \(R\) contains a member of \(P\setminus N(u)\). Thus the recursion over these candidates is exhaustive, and transferring each processed candidate from \(P\) to \(X\) avoids duplicate maximal cliques. The terminal condition \(P=X=\varnothing\) yields exactly one maximal clique. All loops are finite, and bit masks represent the full finite vertex set rather than a truncated search.

The complete maximal-clique counts (including nonmaximum ones) are respectively \(4,16,520,675239\). Their maximum sizes and the counts attaining them are exactly the preceding table. The checker independently verifies that each recorded maximum codebook has pairwise disjoint deletion shadows. The full list of all maxima is included in `maxima.json`; it is not merely a selection of examples.

**Symmetry and syndrome checks.** Reversal and bit complement commute and both preserve weight, run bound, and deletion-shadow disjointness. Their four transformations act on the enumerated twenty maxima. Direct application to every member yields orbit sizes \((2,2,2,2,2,2,4,4)\). For each maximum \(C\), calculating \(\sum_{i=1}^n i x_i\bmod(n/2+1)\) for every \(x\in C\) shows that at length eight the one maximum is a single complete class of syndrome three; at length ten exactly two maxima have one constant syndrome, three or four. Their sizes agree with the full counts of the corresponding constrained syndrome classes, proving the precise statement about modified-VT codebooks.

## Verification
Run `python verify_census.py` in the directory holding `maxima.json`. The script uses only the Python standard library. It reconstructs all admissible vertices, checks the two independently constructed graph relations pairwise, enumerates all maximal cliques using an explicit exhaustive recursion, verifies the complete stored list of maxima, checks disjoint shadows, and recomputes the symmetry orbit and syndrome assertions. The observed terminal line is `VERIFY_OK`. An additional independent graph-and-clique enumeration using NetworkX's `find_cliques` reproduced the same maxima counts and total maximal-clique counts; NetworkX is not needed for the standalone certificate.

## Relationship to prior work
Cullina, Kulkarni and Kiyavash's 2012 constant-weight deletion-code work represents correcting codes as independent sets of deletion-conflict graphs and gives the **modified-VT coloring** using modulus \(\max(k,n-k)+1\). This proves that each syndrome class is a valid code, but it does **not** count all largest independent sets after imposing simultaneous exact balance and exclusion of both triple runs. Indeed, the present census finds eighteen optimal length-ten codebooks that are not complete modified-VT classes. Kulkarni and Kiyavash give general constrained-source bounds, with a different standard \((d,k)\) run-length-limited source model; their bound does not supply the present census. Kracht and Schober motivate insertion/deletion-robust barcodes, but examine watermark constructions rather than this exact binary constrained-code enumeration.

## Limitations
This is a complete **finite** classification for the stated four lengths, not an all-length formula or a theorem of optimality for quaternary DNA barcodes. The binary weight constraint is an idealized composition analogue; biological GC content and context effects require separate treatment. Computational completeness depends on the provided finite graph construction and exhaustive recursion, not just the observed optimum. An earlier constant-composition deletion-code thesis could not be inspected in full, and unindexed historic classifications are possible. No independent audit is claimed.

## References
1. D. Cullina, A. A. Kulkarni and N. Kiyavash, *A coloring approach to constructing deletion correcting codes from constant weight subgraphs*, ISIT 2012, DOI: 10.1109/ISIT.2012.6284242 (public IEEE entry dated 2012-08-27); expanded preprint *Two Approaches to the Construction of Deletion Correcting Codes: Weight Partitioning and Optimal Colorings*, arXiv:1211.4056v1, 2012-11-16, https://arxiv.org/pdf/1211.4056.
2. A. A. Kulkarni and N. Kiyavash, *Non-asymptotic Upper Bounds for Deletion Correcting Codes*, arXiv:1211.3128v1, 2012-11-13, https://arxiv.org/pdf/1211.3128.
3. D. Kracht and S. Schober, *Insertion and deletion correcting DNA barcodes based on watermarks*, BMC Bioinformatics 16:50 (2015), DOI: 10.1186/s12859-015-0482-7, https://link.springer.com/article/10.1186/s12859-015-0482-7.
