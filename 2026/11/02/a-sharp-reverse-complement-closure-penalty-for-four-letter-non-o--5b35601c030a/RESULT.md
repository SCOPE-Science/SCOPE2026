# A sharp reverse-complement closure penalty for four-letter non-overlapping DNA codes

## Finding
Let \(\Sigma=\{A,C,G,T\}\), with Watson–Crick complementation \(\overline A=T\) and \(\overline C=G\). A code \(C\subseteq\Sigma^4\) is **non-overlapping** if for every ordered pair \(u,v\in C\), including \(u=v\), no nonempty proper prefix of \(u\) equals a suffix of \(v\). Write \(\rho(w)=\overline{w_4}\,\overline{w_3}\,\overline{w_2}\,\overline{w_1}\) for the reverse complement.

**Theorem.** Among all non-overlapping \(C\subseteq\Sigma^4\) obeying \(\rho(C)=C\), the maximum size is exactly \(17\). Exactly \(32\) distinct labeled codes attain this maximum. Each optimal code contains exactly \(5\) self-reverse-complementary words and \(6\) two-element reverse-complement orbits. Under alphabet permutations commuting with Watson–Crick complementation, the \(32\) optimal codes form exactly \(4\) orbits, each of size \(8\).

Thus the reverse-complement constraint reduces the best attainable cardinality from the known unrestricted value \(27\) to \(17\) at this fixed alphabet and word length.

A witness uses the encoding \(A=0,C=1,G=2,T=3\). Its \(17\) words are

```
0001 0031 0033 0201 0211 0213 2001 2031 2033
2201 2211 2213 2301 2311 2313 2331 2333
```

## Assumptions and scope
The alphabet is fixed and labeled. Codes consist of distinct words of exactly four letters, and **both** the code and every reverse complement belong to the code. Overlap lengths are exactly \(1,2,3\), including a word's self-overlaps. This is an exact combinatorial model; no biochemical binding, error-correction, GC balance, or experimental performance assumptions are made. The \(32\) optima are distinct on the fixed nucleotide alphabet, not quotiented by rotations or reversals of word positions. The symmetry group used in the four-class statement consists solely of the eight alphabet permutations \(\pi\) satisfying \(\pi(\bar a)=\overline{\pi(a)}\).

## Proof
**1. Valid orbit reduction.** Every admissible individual word is unbordered. Enumerating all \(4^4=256\) words by their four symbols and directly comparing their three proper prefixes and suffixes gives exactly \(180\) unbordered words. Reverse complementation preserves this property. Partition these \(180\) words into orbits of the involution \(\rho\). Discard an orbit if its members overlap one another (including self), and retain each other orbit as a single indivisible choice. The explicit finite enumeration in `verify.py`, reproduced without lookup tables, gives \(56\) eligible orbits: \(12\) singleton and \(44\) two-element orbits.

**2. Compatibility graph.** Form a simple graph \(G\) on those \(56\) orbit-vertices. Two distinct vertices are adjacent precisely when *every* pair of words selected from their two constituent orbits is non-overlapping. Exactly \(540\) of the \(\binom{56}{2}=1540\) possible edges are present. Assign vertex weight \(w_i=1\) or \(2\), its orbit's cardinality. A non-overlapping reverse-complement-closed code is uniquely the union of the word orbits in a clique of \(G\), and its size is exactly the clique's weight. This is a bijection, so optimization of this graph is neither a relaxation nor a restriction of the original problem.

**3. Exhaustive exact recurrence.** Number the vertices deterministically by their lexicographically sorted word orbits. Let \(N(i)\) be the neighbor bitset of vertex \(i\). For a bitset of available vertices \(P\), let \(F(P)=(M(P),K(P))\), where \(M(P)\) is the largest weight of any clique contained in \(P\), and \(K(P)\) counts cliques attaining that weight; the empty clique has weight zero. Set \(F(\varnothing)=(0,1)\). For nonempty \(P\), take the lowest-index vertex \(i\in P\). Compute the exclude branch \(F(P\setminus\{i\})\) and the include branch obtained by adding \(w_i\) to the weight component of \(F(P\cap N(i))\). Return the branch with larger weight, or their common weight and the sum of both counts on a tie. All cliques fall uniquely in one of these two disjoint branches. Induction on \(|P|\) proves the recurrence exactly.

The self-contained `verify.py` constructs every vertex and edge from the raw nucleotide words and evaluates this recurrence with memoization. Exactly \(398\) distinct bitsets occur and the top result is

\[
F(V(G))=(17,32).
\]

This is a finite **exhaustive proof**, not an extrapolation from tested word lengths: the full word domain has only \(256\) elements and every possible admissible code is represented by one of the cliques evaluated by the recurrence.

**4. Extremizer structure and symmetry.** Replaying tied choices in the same recurrence lists all \(32\) maximum cliques. Directly reconstructing and comparing every pair of constituent words confirms all \(32\) codebooks and that each contains \(5\) one-word and \(6\) two-word reverse-complement orbits. The \(8\) alphabet permutations commuting with complementation act on the optimal codebooks; enumerating their images gives four disjoint classes, all of size eight. The witness displayed above is one of these codebooks, and is checked directly.

## Verification
Run `python3 verify.py` under Python 3 using the standard library only. Expected terminal line: `VERIFY_OK`. The verifier recomputes the source universe, prefix/suffix tests, reverse complements, \(56\)-vertex graph, weighted-clique recurrence, exact optimal-count enumeration, direct constraints on all optima, and symmetry classes. As a separate consistency check, a weighted color-branching maximum-clique algorithm (with a proven admissible upper bound) independently returns maximum \(17\) and \(32\) maximizers in \(293\) calls. Its graph is created anew from the same explicit mathematical definitions. The proof of exhaustive coverage is given above; the program carries out its finite arithmetic.

## Relationship to prior work
Non-overlapping codes are also known as cross-bifix-free or mutually uncorrelated codes. Chee, Kiah, Purkayastha, and Wang established general constructions and comparisons for these codes in their public 2012 preprint. Blackburn analyzed their size and general non-overlap bounds. Stanovnik, Moškon, and Mraz proved that the **unrestricted** optimum for four-symbol, four-letter non-overlapping codes is \(27\). None of these inspected results imposes closure under the reverse-complement involution or directly determines the constrained maximum \(17\), the \(32\) labeled optimizers, or their four symmetry classes. Kari and Mahalingam treat Watson–Crick involution codes and \(\theta\)-comma-free conditions in an algebraic framework, but do not provide the exact closed cross-bifix-free codebook count at this four-letter parameter. The earlier unrestricted result is explicitly not claimed as new.

## Limitations
The theorem applies only to words of length four over the four standard DNA bases with an exact reverse-complement-closure condition. It does not prescribe GC balance, Hamming distance, avoidance of secondary structure or biochemical viability. The computed finite certificate must be replayed to check the numerical constants; no general formula for larger lengths is proved. Published and unindexed work may contain equivalent classifications not located in the searched sources, so independent historical-priority assessment remains outstanding.

## References
1. Y. M. Chee, H. M. Kiah, P. Purkayastha, and C. Wang, *Cross-Bifix-Free Codes Within a Constant Factor of Optimality*, arXiv:1209.0236, first submitted 2012-09-03. https://arxiv.org/html/1209.0236v2
2. S. R. Blackburn, *Non-overlapping codes*, arXiv:1303.1026, first submitted 2013-03-05. https://arxiv.org/abs/1303.1026
3. L. Stanovnik, M. Moškon, and M. Mraz, *In search of maximum non-overlapping codes*, *Designs, Codes and Cryptography* 92 (2024), 1299–1326, Theorem 19. https://doi.org/10.1007/s10623-023-01344-z
4. L. Kari and K. Mahalingam, *DNA Codes and their Properties*, accessible full text: https://doczz.net/doc/7869278/dna-codes-and-their-properties
