# Exact run-two, balanced binary non-overlapping code sizes through length fourteen

## Finding
Let \(M(n)\) denote the largest possible size of a binary non-overlapping code of even length \(n\) in which every codeword has equally many zeroes and ones and contains no cyclic run of three equal symbols. Then
\[
\bigl(M(4),M(6),M(8),M(10),M(12),M(14)\bigr)=(1,2,3,5,11,24).
\]
The run-two specialization \(D_{n,2}\) of the restricted Dyck code in Construction 7 of Stanovnik, Moškon and Mraz has respective sizes \((1,2,3,5,11,20)\). Thus the first difference at these successive even lengths is \(M(14)=24>20=|D_{14,2}|\), a sharp increase of four words over that construction. An explicit twenty-four-word optimum is embedded in `certificates.json`.

| Length \(n\) | Eligible unbordered words | Exact optimum \(M(n)\) | Restricted Dyck construction |
|---:|---:|---:|---:|
| 4 | 2 | 1 | 1 |
| 6 | 6 | 2 | 2 |
| 8 | 10 | 3 | 3 |
| 10 | 24 | 5 | 5 |
| 12 | 52 | 11 | 11 |
| 14 | 128 | 24 | 20 |

## Assumptions and scope
A binary length-\(n\) word \(w=w_0\cdots w_{n-1}\) is *polarity-balanced* if it has \(n/2\) ones. Its cyclic run length is at most two when no triple \(w_i,w_{i+1},w_{i+2}\) (indices modulo \(n\)) consists of equal bits. A code \(C\subseteq\{0,1\}^n\) is *non-overlapping*, also called *cross-bifix-free*, if for every ordered pair \(u,v\in C\), allowing \(u=v\), and every \(1\le j<n\), the length-\(j\) prefix of \(u\) differs from the length-\(j\) suffix of \(v\). These are linear-prefix and linear-suffix overlaps, not cyclic overlaps of different codewords.

The exact optimum is claimed only at the six explicitly listed even lengths. The run-length condition itself includes wraparound at the end of each codeword. Distinguishing these conventions is essential to the statement.

## Proof
**Reduction to an explicit finite set.** A word in any non-overlapping code must be unbordered, since the definition also applies with \(u=v\). For each specified \(n\), let \(E_n\) be the lexicographically ordered list of all length-\(n\) binary words that are polarity-balanced, have cyclic run length at most two, and have no nonempty proper border. The complete generator in `verify.py` iterates all \(2^n\) words, applies these three tests directly, and yields the counts in column two of the table.

**Upper certificates.** Fix a length \(n\) and let \(K\) be its claimed optimum. The embedded `color_labels` array has one integer in \(\{0,\ldots,K-1\}\) for each word of \(E_n\), in exactly the lexicographic order specified above. For every pair of *distinct* words sharing a color, `verify.py` independently confirms that at least one nonempty proper prefix–suffix overlap occurs in one of the two directions. Consequently a non-overlapping code uses at most one word of each color, so its size is at most \(K\). This is a direct, finite pigeonhole proof, not an inference from a heuristic graph-coloring result.

**Lower certificates.** For each length, `witness_words` contains exactly \(K\) distinct eligible words. The same verifier directly compares all proper prefix–suffix lengths for every ordered pair and confirms that no overlap occurs; its separate self-border test has already excluded overlaps of a word with itself. Thus there is a valid code of size \(K\), and the two inequalities give \(M(n)=K\) for every length in the table.

**Comparison with Construction 7.** The restricted Dyck-count function in `verify.py` enumerates all balanced Dyck words in the formula of Construction 7 and Proposition 13, including the additional starting/ending restrictions and the odd-index double-count subtraction. Its independently computed values are the last column of the table. In particular \(20<24\) at length fourteen, whereas the sizes coincide for all earlier listed even lengths. No general extrapolation beyond length fourteen is used.

## Verification
Run `python3 verify.py` alongside `certificates.json` using Python 3 and its standard library; no solver, network, or third-party dependencies are needed. The verifier regenerates all eligible words from their definitions (rather than trusting a stored list), checks each same-color pair is incompatible, checks each distinct witness pair is compatible, and recomputes restricted Dyck construction sizes. Its completed output was:

```text
length=4 candidates=2 upper=1 witness=1 restricted_Dyck=1
length=6 candidates=6 upper=2 witness=2 restricted_Dyck=2
length=8 candidates=10 upper=3 witness=3 restricted_Dyck=3
length=10 candidates=24 upper=5 witness=5 restricted_Dyck=5
length=12 candidates=52 upper=11 witness=11 restricted_Dyck=11
length=14 candidates=128 upper=24 witness=24 restricted_Dyck=20
VERIFY_OK
```

These comparisons certify the finite theorem directly. Constructing the certificates required a search, but verifying their correctness does not trust how they were discovered.

## Relationship to prior work
The standard non-overlapping or cross-bifix-free definition and its relevance to synchronization are developed by Chee et al. [1] and Blackburn [2]. The all-code, unconstrained optimization framework in Stanovnik et al. [3] does not impose the present simultaneous polarity balance and cyclic run-two constraints. Most closely, Stanovnik et al. [4] analyze polarity balance and run restrictions, present a general characterization of maximal codes, and give Construction 7 and Proposition 13 as an explicit family of feasible combined-constraint codes. Their table records the twenty-word length-fourteen member; that construction provides a lower bound, not an exact maximum. The new statement here is the independently certified sharp combined-constraint maximum of twenty-four and its preceding finite threshold profile, not the Dyck construction or the general characterization.

## Limitations
This finite result does not provide a formula or asymptotic estimate for larger lengths, classify every optimal code, or guarantee any positive Hamming distance within the twenty-four-word code. Independent mathematical validation and a comprehensive historical-priority determination have not been performed. The comparison is with the stated Construction 7, not with every possible published constrained construction. Some publications and unindexed tables may contain equivalent finite data.

## References
[1] Y. M. Chee, H. M. Kiah, P. Purkayastha, and C. Wang, *Cross-Bifix-Free Codes Within a Constant Factor of Optimality*, arXiv:1209.0236 (first public version 3 September 2012), https://arxiv.org/abs/1209.0236.

[2] S. R. Blackburn, *Non-overlapping codes*, arXiv:1303.1026 (2013), https://arxiv.org/abs/1303.1026.

[3] L. Stanovnik, M. Moškon, and M. Mraz, *In search of maximum non-overlapping codes*, Designs, Codes and Cryptography (2024), https://doi.org/10.1007/s10623-023-01344-z.

[4] L. Stanovnik, M. Moškon, and M. Mraz, *On maximal almost balanced non-overlapping codes and non-overlapping codes with restricted run-lengths*, Computational and Applied Mathematics 44, article 109 (2025), first arXiv version 24 October 2024, https://arxiv.org/abs/2410.18458 and https://doi.org/10.1007/s40314-024-03055-0.
