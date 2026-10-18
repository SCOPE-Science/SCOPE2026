# Two shortest unique factors in dyadic paperfolding prefixes

## Finding
For each integer \(n\ge 6\), let \(P_n\) be the first \(2^n\) bits of the regular paperfolding word \(p_1p_2\cdots\), indexed from one and specified by \(p_i=0\) when the odd part of \(i\) is congruent to \(1\pmod4\), and \(p_i=1\) when it is congruent to \(3\pmod4\). A factor is *unique* when it has precisely one occurrence as a contiguous substring of the finite word (overlaps count separately).

The minimum length of a unique factor in \(P_n\) is exactly
\[
L_n=2^{n-4}+1.
\]
There are exactly **two** distinct factors of this minimum length, each occurring once, and their complete set of one-based starting positions is
\[
\{11\cdot 2^{n-4},\ 12\cdot 2^{n-4}\}.
\]
Equivalently, their zero-based starts are \(11\cdot2^{n-4}-1\) and \(12\cdot2^{n-4}-1\). Both factors are also minimal unique substrings, since all shorter factors repeat.

## Assumptions and scope
The alphabet is \(\{0,1\}\), with the explicit paperfolding convention above; the reversal, complement, or shifted indexing conventions used elsewhere must be translated before comparison. All occurrences refer to the *finite* prefix, not the infinite sequence. The result holds for every integer \(n\ge6\), without restrictions on the exponent. Put \(k=n-4\), \(q=2^k\), so \(|P_n|=16q\).

## Proof
**Elementary digit rule.** For every positive integer \(i\), let \(\nu_2(i)\) be its two-adic valuation. The bit \(p_i\) is determined by the residue of \(i/2^{\nu_2(i)}\) modulo four. In particular \(p_{2i}=p_i\), and \(p_{2i+1}\) equals \(i\bmod2\). Moreover, if \(0<|h|<q\) and \(tq+h>0\), then \(\nu_2(tq+h)=\nu_2(h)<k\) and \(p_{tq+h}\) depends only on \(h\) and the parity of \(t\). Indeed, dividing \(tq+h\) by \(2^{\nu_2(h)}\), the added term is a multiple of four except when \(\nu_2(h)=k-1\), in which case it is \(2t\) modulo four. Also, \(p_{tq}=p_t\) for positive \(t\).

**Repeated factors through length \(q\).** Consider an arbitrary interval of \(P_n\) with length at most \(q\). It contains at most one multiple of \(q\). If it contains none, translate it to the other gaps between consecutive multiples of \(q\) whose gap index has the same parity. All bits are preserved, and at least eight valid occurrences result (including the original). If it contains the multiple \(tq\), for some \(1\le t\le16\), place the same interval of offsets around each \(t'q\) with \(1\le t'\le16\), \(t'\equiv t\pmod2\), and \(p_{t'}=p_t\). All these copies lie within the finite prefix, and their bits agree by the digit rule. Every parity/bit class among the sixteen indices contains at least three representatives. Thus every factor of length at most \(q\) has at least three occurrences. In particular no such factor is unique.

**A finite synchronization lemma.** Any two occurrences of the same length-nine factor in the *infinite* paperfolding word begin at congruent positions modulo eight. To prove it without sampling the infinite word, write its one-based start as \(8t+r\), where \(1\le r\le8\). Among the nine indices, only indices divisible by eight have unspecified values; all other bits are fixed by \(r\) and \(t\bmod2\). At each divisible-by-eight position, allow *both* bit values, even when they are not jointly realizable. Enumerating these finite supersets gives the following sets, with words of length nine written literally:

| Start residue \(r\) | Possible length-nine words (a safe superset) |
| --- | --- |
| 1 | `001001100`, `001001110`, `001101100`, `001101110` |
| 2 | `010011000`, `010011100`, `011011000`, `011011100` |
| 3 | `100110001`, `100111001`, `110110001`, `110111001` |
| 4 | `001100011`, `001110011`, `101100010`, `101110010` |
| 5 | `011000100`, `011000110`, `011100100`, `011100110` |
| 6 | `110001001`, `110001101`, `111001001`, `111001101` |
| 7 | `100010011`, `100011011`, `110010011`, `110011011` |
| 8 (zero modulo eight) | `000100110`, `000100111`, `000110110`, `000110111`, `100100110`, `100100111`, `100110110`, `100110111` |

These thirty-six words are pairwise different, proving the lemma. The included standalone checker regenerates all sets from the two-adic rule and verifies their disjointness; the tabulated finite proof can also be checked directly.

**Dyadic alignment.** For every integer \(k\ge3\), if two equal length-\(2^k+1\) factors of the infinite word occur at starts \(a\) and \(b\), and \(2^k\mid a\), then \(2^k\mid b\). At \(k=3\), this follows from the length-nine synchronization lemma. For the induction step, their first nine symbols imply \(b\equiv a\equiv0\pmod8\), hence both starts are even. Select symbols at the even-indexed absolute positions \(a,a+2,\ldots,a+2^k\) and at \(b,b+2,\ldots,b+2^k\). Using \(p_{2i}=p_i\), these are equal length-\(2^{k-1}+1\) factors starting at \(a/2\) and \(b/2\). The former start is divisible by \(2^{k-1}\), so induction makes \(b/2\) divisible by \(2^{k-1}\), as required.

**Enumerating the first possible unique length.** For \(q+1\) consecutive positions in \(P_n\), an interval beginning away from a multiple of \(q\) contains exactly one multiple \(tq\), \(1\le t\le15\). Moving its offsets to other multiples with the same \((t\bmod2,p_t)\) preserves its bits, and each such class contains at least three indices. Thus none of these intervals is unique.

A length-\(q+1\) interval beginning at a multiple of \(q\) is \([tq,(t+1)q]\) with \(1\le t\le15\). Its interior bits are determined exactly by \(t\bmod2\), and its endpoint bits are \((p_t,p_{t+1})\). Conversely, the interior bit at offset \(q/2\) equals \(t\bmod2\), so two of these aligned factors are equal *if and only if* their triples \((t\bmod2,p_t,p_{t+1})\) agree. From the first sixteen letters

`0010011000110110`

the eight triple classes are

| Triple \((t\bmod2,p_t,p_{t+1})\) | Indices \(t\) |
| --- | --- |
| (0,0,0) | 4, 8 |
| (0,0,1) | 2, 10 |
| (0,1,0) | **12** |
| (0,1,1) | 6, 14 |
| (1,0,0) | 1, 9 |
| (1,0,1) | 5, 13 |
| (1,1,0) | 3, 7, 15 |
| (1,1,1) | **11** |

Thus exactly two *aligned* factors are singleton classes, at starts \(11q\) and \(12q\). For \(k\ge3\), the alignment lemma rules out any occurrence of either word at an unaligned start. For the remaining base \(k=2\), direct finite enumeration of all sixty length-five factors in the length-sixty-four prefix yields exactly two singletons, with one-based starts \(44\) and \(48\); this base computation is reproducible in `checker.py`. Consequently, for every \(k\ge2\) exactly these two length-\(q+1\) factors are unique. Together with the lower bound this proves all claims.

## Verification
Run `python checker.py` using Python 3. It independently constructs all thirty-six nine-bit template words, asserts pairwise disjointness of the eight residue classes, regenerates the endpoint triples, and counts all length-\(q\) and length-\(q+1\) factors directly for every \(6\le n\le12\). `checker_output.txt` records the actual successful execution. The infinite assertion rests on the preceding arithmetic and induction, not on those finite tests. The finite base \(n=6\) is exhaustively counted.

## Relationship to prior work
Kishi, Guo, Urbina, and Bannai (2026) study minimal unique substrings in Fibonacci and Thue–Morse morphic words and prove a complete theorem for the latter. That stronger *Thue–Morse* classification does not imply a classification for regular paperfolding prefixes. Banbara et al. (2026) completely classify smallest string attractors in Fibonacci and period-doubling words; attractor positions solve a different occurrence-coverage problem and do not imply the exact shortest-unique-factor counts here. Allouche (1992) gives the infinite paperfolding word's factor complexity, which counts distinct factors without classifying their multiplicities in finite prefixes. Existing numerical attractor data on regular paperfolding prefixes similarly concern covering sets, not shortest unique factors. Exact statement/implication and alias checks and residual originality risks appear in `AUDIT.json`.

## Limitations
The convention for the regular paperfolding word is essential. The theorem does not enumerate *all* minimal unique substrings of \(P_n\), only the shortest ones, nor does it classify arbitrary non-dyadic prefixes, generalized paperfolding words, or overlapping repetitions outside the finite-prefix setting. No independent mathematical audit has been performed. Searches cannot rule out differently formulated or unindexed prior results.

## References
1. K. Kishi, P. Guo, C. Urbina, H. Bannai, *On Occurrence-Preserving Morphisms*, arXiv:2605.18034 (initial public preprint 2026-05-18), DOI:10.4230/LIPIcs.CPM.2026.24; full text https://drops.dagstuhl.de/storage/00lipics/lipics-vol369-cpm2026/html/LIPIcs.CPM.2026.24/LIPIcs.CPM.2026.24.html.
2. M. Banbara, H. Bannai, P. Guo, D. Köppl, T. Mieno, Y. Okamoto, *The Smallest String Attractors of Fibonacci and Period-Doubling Words*, arXiv:2602.16152v1 (2026-02-18), https://arxiv.org/html/2602.16152v1.
3. J.-P. Allouche, *The Number of Factors in a Paperfolding Sequence*, Bulletin of the Australian Mathematical Society 46 (1992), 23–32, DOI:10.1017/S0004972700011655.
4. OEIS A337120, *Factor complexity of the regular paperfolding sequence*, https://oeis.org/A337120.
