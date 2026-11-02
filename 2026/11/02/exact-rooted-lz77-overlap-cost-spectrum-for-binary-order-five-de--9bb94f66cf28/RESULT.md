# Exact rooted LZ77 overlap-cost spectrum for binary order-five de Bruijn cycles

## Finding

Let \(\mathcal D_5\) be the \(2{,}048\) binary de Bruijn cycles of order five, modulo rotation, and take all \(32\) rooted one-traversal strings of each cycle. Let \(z(w)\) be the number of phrases in greedy LZ77 **pair-reference parsing allowing source–phrase overlap**, and \(\widehat z(w)\) the number when each reference is wholly before its phrase. The complete joint distribution of \((z,\widehat z)\), over all \(65{,}536\) rooted strings, is:

| \(z\) / \(\widehat z\) | 11 | 12 | 13 | 14 | 15 | 16 |
|---:|---:|---:|---:|---:|---:|---:|
| 10 | 12 | 66 | 276 | 642 | 178 | 8 |
| 11 | 66 | 1034 | 3828 | 6118 | 2704 | 90 |
| 12 | 0 | 1968 | 10124 | 14026 | 5448 | 122 |
| 13 | 0 | 0 | 5446 | 9362 | 2414 | 36 |
| 14 | 0 | 0 | 0 | 1366 | 200 | 0 |
| 15 | 0 | 0 | 0 | 0 | 2 | 0 |

All other pairs have frequency zero. Thus \(z\) ranges from \(10\) through \(15\), \(\widehat z\) ranges from \(11\) through \(16\), and the sharp gain \(g=\widehat z-z\) ranges from \(0\) through \(6\). Its complete rooted distribution is:

| Gain \(g\) | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---:|---:|---:|---:|---:|---:|---:|---:|
| Rooted strings | 8,848 | 20,732 | 20,334 | 11,878 | 3,468 | 268 | 8 |

The per-cycle minimum and maximum of \(g\), taken over all roots, have this complete distribution:

| \((\min g,\max g)\) | (0,2) | (0,3) | (0,4) | (0,5) | (0,6) | (1,3) | (1,4) | (1,5) |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Cycles | 12 | 544 | 1,158 | 192 | 8 | 12 | 94 | 28 |

In particular, overlap saves at least two greedy phrases at a suitable root of **every** cycle; in exactly \(134\) cycles it saves at least one at **every** root; and precisely eight rooted strings attain a gain of six.

## Assumptions and scope

A binary order-five de Bruijn cycle is a cyclic binary word of length \(32\) whose \(32\) length-five circular factors are pairwise distinct. Distinguish cycles only up to rotation, not bit-complement or reversal. A rooted traversal is the length-\(32\) *linear* word starting at a chosen cyclic position; references in its parsing cannot wrap around its end or use any symbol outside this linear interval.

All parsing positions below are zero-indexed. At a phrase head \(i\), choose the largest \(L\ge1\) such that either \(L=1\) is taken as a literal when no positive previous match exists, or there is a source \(j<i\) with \(w[j:j+L]=w[i:i+L]\). The word on the right must fit inside the traversal. The **overlap-allowed** variant has no restriction on \(j+L\) and is the pair-reference LZ parsing of Kosolobov–Shur. The **disjoint-source** variant additionally requires \(j+L\le i\) and is their novLZ parsing. Greedily advance by \(L\), counting one phrase regardless of the source chosen in a tie. Neither scheme uses a next-letter triple. Source references may overlap their own output only in the first variant. Zero-length references are replaced by single-letter literals in either scheme.

## Proof

**Step 1: Exhaustive cycle parameterization.** The \(32\) length-five windows are the \(32\) states \(s=(a,x)\) with one leading bit \(a\) and a four-bit suffix \(x\). The successor of \((a,x)\) is of form \((x,b)\). Because every length-five window occurs exactly once on a cycle, every state has precisely one predecessor and successor in the induced transition permutation. For each fixed suffix \(x\), the two states \((0,x)\) and \((1,x)\) must therefore be sent bijectively to \((x,0)\) and \((x,1)\); this is specified by a Boolean switch \(t_x\), with successor \((x,a\mathbin{\oplus}t_x)\). Conversely, any of the \(2^{16}=65{,}536\) choices for the \(16\) switches that generates one permutation cycle on all \(32\) states yields an order-five de Bruijn cycle. The state \(00000\) is unique on such a cycle, hence the cycle has a unique rooted representation starting there, and no two passing switch tables define the same necklace. Exhaustive enumeration of all switches selects exactly \(2{,}048\) one-cycle maps.

**Step 2: Exact greedy phrase lengths.** For a fixed rooted word \(w\) of length \(n=32\), define \(\lambda_i(j)\) for \(0\le j<i<n\) as the largest length of an equal prefix of suffixes starting at \(i,j\), truncated at the right boundary of \(w\). Let

\[
L_i=\max\bigl(1,\max_{0\le j<i}\lambda_i(j)\bigr),\qquad
\widehat L_i=\max\bigl(1,\max_{0\le j<i}\min\{\lambda_i(j),i-j\}\bigr).
\]

Take the maximum over an empty set to be zero. These are exactly the two greedy phrase lengths by the definitions above. Repeatedly replace \(i\) by \(i+L_i\), respectively \(i+\widehat L_i\), beginning from \(i=0\) until \(i=n\), and count the steps.

**Step 3: Finite exact census.** The included `check.py` visits all \(2^{16}\) switch choices, accepts exactly \(2{,}048\) de Bruijn cycles, then visits every one of their \(32\) roots. At every phrase head it computes the two lengths by direct comparisons with *all* earlier source starts. It increments the joint histogram and records the per-cycle minimum and maximum gain. The final exact equality tests against all \(24\) nonzero joint cells and the complete gain profiles are part of the executable certificate; the script halts on any discrepancy. Thus, by Steps 1–2, the tables are an exhaustive finite proof rather than a sample.

As an independent enumeration check, the script runs Hierholzer's Euler-tour algorithm on the sixteen-vertex binary de Bruijn graph, varying the outgoing-edge priority at every vertex through all \(2^{16}\) choices. This yields exactly the same set of \(2{,}048\) normalized necklaces. As an independent parsing check, it builds the longest-common-prefix matrix by the backward recurrence \(\mathrm{LCP}(i,j)=[w_i=w_j](1+\mathrm{LCP}(i+1,j+1))\), with terminal zeros, and recomputes phrase boundaries and both counts at all roots. All \(131{,}072\) parser instances agree with the direct comparator. The two checks do not replace the exhaustive mathematical reduction in Step 1.

For a maximal-gap witness, let `W=00000111001101100010010111110101` and start at zero-index root \(23\). The resulting traversal is `11111010100000111001101100010010`. Its overlapping phrase lengths are `1,4,1,4,4,4,3,4,3,4`, totaling \(10\) phrases; its disjoint-source phrase lengths are `1,1,2,1,1,2,2,1,2,2,3,3,3,4,3,1`, totaling \(16\) phrases. The witness confirms attainability of the sharp gain \(6\).

## Verification

Run `python check.py` with Python \(\ge3.9\); no third-party packages or input files are required. The script independently recreates both families, all parsings and all summary tables and finishes with `VERIFY_OK` only after the exact expected joint, gain, and per-cycle distributions agree. The supplementary `joint.csv` is an explicit machine-readable copy of the \(24\) nonzero cells; it is generated from the same integers displayed here. Each instance is bounded to a length-\(32\) word, and the exhaustive state space consists of \(65{,}536\) switch choices and \(65{,}536\) rooted traversals.

## Relationship to prior work

Goto–Bannai and Kärkkäinen–Kempa–Puglisi describe exact algorithms for greedy LZ77 parsing in 2012; their focus is algorithmic running time and memory, not the rooted order-five de Bruijn spectrum. Kosolobov–Shur (2017/2018) define precisely the LZ and novLZ pair-reference variants and prove general bounds such as \(z\le\widehat z\); these cover the nonnegativity of the gain but not the present joint distribution, phase range, or exact frequency counts. Andreasen (2001, thesis sections on de Bruijn sequences and Lempel–Ziv compression) uses specially concatenated de Bruijn sequences to study different compression behavior; this does not give the 32-letter all-necklace, all-root, two-variant census here. Related finite-rooted LZ78 counts use dictionary parsing, a different quantity that does not imply this joint LZ77 table.

## Limitations

This is a **finite** complete classification of binary order-five cycles only, for two explicitly defined pair-reference greedy variants. It gives phrase counts, not encoded bit lengths, and does not imply any all-order recurrence or spectral law for order six or more. Different literal conventions, dictionary LZ78, or next-letter LZ77 triple parsings are outside the claim. Literature priority is assessed against inspected accessible works, not certified exhaustive for all publications; independent mathematical review has not been performed.

## References

1. K. Goto and H. Bannai, *Simpler and Faster Lempel Ziv Factorization*, first public 2012-11-15, arXiv:1211.3642, https://arxiv.org/abs/1211.3642.
2. J. Kärkkäinen, D. Kempa, and S. J. Puglisi, *Linear Time Lempel-Ziv Factorization: Simple, Fast, Small*, first public 2012-12-12, arXiv:1212.2952, https://arxiv.org/abs/1212.2952.
3. D. Kosolobov and A. M. Shur, *Comparison of LZ77-type Parsings*, first public 2017-08-11, arXiv:1708.03558, https://arxiv.org/html/1708.03558v3.
4. P. Andreasen, *Universal Source Coding*, 2001 thesis, https://www.cs.auckland.ac.nz/~cristian/toprint/andreasen.pdf (de Bruijn and Lempel–Ziv sections).
