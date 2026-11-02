# Bit-reversal transport of reverse Burrows–Wheeler transforms of de Bruijn cycles

## Finding

Let \(n\ge2\) and let \(W\) be a binary de Bruijn cycle of order \(n\), considered up to circular rotation. Write \(B(W)\) for the *sentinel-free, cyclic-rotation* Burrows–Wheeler transform with alphabet order \(0<1\). There is a unique binary feedback table \(m=(m_0,\ldots,m_{2^{n-1}-1})\) whose state permutation traverses \(W\) and whose update on an \(n\)-bit state \(x_0\cdots x_{n-1}\) is

\[
F_m(x_0\cdots x_{n-1})=x_1\cdots x_{n-1}(x_0\oplus m_{[x_1\cdots x_{n-1}]_2}).
\]

Let \(\operatorname{rev}_{n-1}(j)\) reverse the \((n-1)\)-bit expansion of \(j\), allowing leading zeros. Then the *complete transforms*, not merely their lengths or run counts, satisfy

\[
\boxed{ B(W)=\prod_{j=0}^{2^{n-1}-1}(m_j,1-m_j),\qquad
B(W^{\rm rev})=\prod_{j=0}^{2^{n-1}-1}
(m_{\operatorname{rev}_{n-1}(j)},1-m_{\operatorname{rev}_{n-1}(j)}) . }
\]

Here each pair is concatenated as a two-character block, and \(W^{\rm rev}\) reverses the circular word. In particular, with \(T(a)=\sum_{j=0}^{2^{n-1}-2}\mathbf1\{a_j\ne a_{j+1}\}\), the *linear* numbers of constant-letter BWT runs are

\[
r(W)=2^n-T(m),\qquad
r(W^{\rm rev})=2^n-T(m\circ\operatorname{rev}_{n-1}).
\]

The transform of the reversed cycle is therefore obtained by a fixed bit-reversal permutation of the original transform's complementary two-character blocks. This does not assert that reversing the BWT character string gives the same result.

For \(n=5\), the following is the complete joint distribution of \((r(W),r(W^{\rm rev}))\) across all \(2048\) binary de Bruijn cycles up to rotation. Rows index \(r(W)\), and columns index \(r(W^{\rm rev})\):

| \(r(W)\) | 20 | 22 | 24 | 26 | 28 | 30 | Total |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 20 | 0 | 4 | 12 | 20 | 2 | 0 | 38 |
| 22 | 4 | 102 | 156 | 140 | 22 | 2 | 426 |
| 24 | 12 | 156 | 366 | 242 | 62 | 2 | 840 |
| 26 | 20 | 140 | 242 | 170 | 34 | 2 | 608 |
| 28 | 2 | 22 | 62 | 34 | 10 | 0 | 130 |
| 30 | 0 | 2 | 2 | 2 | 0 | 0 | 6 |
| **Total** | **38** | **426** | **840** | **608** | **130** | **6** | **2048** |

Equivalently, the distribution of \(r(W^{\rm rev})-r(W)\) at differences \(-8,-6,-4,-2,0,2,4,6,8\) is \(4,44,216,436,648,436,216,44,4\), respectively. Thus the sharp absolute reversal change at order five is \(8\), achieved by exactly \(8\) cycles, while \(648\) cycles have equal run counts. The maximum ratio between larger and smaller run counts is \(7/5\), achieved by exactly four cycles.

## Assumptions and scope

The word is circular, with exactly one occurrence of each possible \(n\)-bit factor. The BWT is defined by lexicographically sorting the \(2^n\) circular rotations, then reading their preceding bits; there is **no** appended terminal marker. Distinct rotations are guaranteed by the de Bruijn condition. Run counting is linear on the resulting BWT string: its first and last letters are not identified. Bit-reversal acts on **fixed-width** \(n-1\) representations, not on minimal-width numerals. The two-bit block formula holds for all integers \(n\ge2\); the finite census holds only for \(n=5\).

## Proof

### 1. A canonical permutation parametrization

Because the \(2^n\) circular \(n\)-factors occur once, the successor map on \(n\)-bit states is a permutation of all states consisting of one cycle. Its images share the \((n-1)\)-bit suffix. For each fixed suffix \(u\), the two states \(0u\) and \(1u\) must have distinct successors \(u0,u1\); otherwise the successor map would fail to be injective. Consequently there is a uniquely determined bit \(m_u\) such that the successors of \(0u\) and \(1u\) are \(um_u\) and \(u(1-m_u)\). This is precisely the stated formula for \(F_m\). Conversely, *every* such feedback table defines a bijective successor permutation, and it corresponds to a de Bruijn cycle if and only if that permutation is a single \(2^n\)-cycle. A single cycle contains the zero state exactly once, so writing its leading bits starting from that state gives a unique canonical representative. Hence enumerating all \(2^{2^{n-1}}\) feedback tables and retaining only the single-cycle ones is exhaustive and duplicate-free.

### 2. Forward BWT blocks

Sorting the rotations of \(W\) is equivalent to sorting their first \(n\) bits, because these prefixes are pairwise different and cover all binary \(n\)-tuples. Consider the rotation beginning with \(x=x_0\cdots x_{n-1}\), whose predecessor bit is \(b\). Its preceding state is \(bx_0\cdots x_{n-2}\), and the final output bit under \(F_m\) must be \(x_{n-1}\). By the feedback rule, \(x_{n-1}=b\oplus m_{[x_0\cdots x_{n-2}]_2}\), so

\[
b=x_{n-1}\oplus m_{[x_0\cdots x_{n-2}]_2}.
\]

In lexicographic order, consecutive \(n\)-bit prefixes with integer labels \(2j\) and \(2j+1\) have identical first \(n-1\) bits and last bits \(0,1\). Their preceding bits are therefore \(m_j,1-m_j\), proving the first block identity.

### 3. Reversing the circular word

A rotation of \(W^{\rm rev}\) whose first \(n\) bits are \(y=y_0\cdots y_{n-1}\) corresponds to the occurrence in \(W\) of the opposite-direction factor \(x=y_{n-1}\cdots y_0\). Its preceding bit in the reversed word is precisely the *successor* bit of \(x\) in the original word. The latter is, by definition,

\[
x_0\oplus m_{[x_1\cdots x_{n-1}]_2}
=y_{n-1}\oplus m_{\operatorname{rev}_{n-1}([y_0\cdots y_{n-2}]_2)}.
\]

For lexicographically successive labels \(y=2j\) and \(2j+1\), this gives the complementary pair indexed by \(\operatorname{rev}_{n-1}(j)\). The second transform identity follows, for **every** order and every binary de Bruijn cycle.

### 4. Exact run-count formula

Each of the \(2^{n-1}\) complementary two-character blocks contributes one internal unequal adjacency. The adjacency between consecutive blocks indexed by orientations \(a_j\) and \(a_{j+1}\) changes letter exactly when \(a_j=a_{j+1}\), since the first block ends in \(1-a_j\). Adding the initial run gives

\[
1+2^{n-1}+\sum_{j=0}^{2^{n-1}-2}\mathbf1\{a_j=a_{j+1}\}
=2^n-T(a).
\]

Use \(a_j=m_j\) and \(a_j=m_{\operatorname{rev}_{n-1}(j)}\), respectively.

### 5. Exhaustive order-five enumeration

At order five, there are \(2^{16}=65536\) Boolean feedback tables. The standalone `verify_reversal.py` enumerates **every** mask from \(0\) through \(65535\), reconstructs the orbit of \(00000\), and retains precisely the tables with 32 distinct successive states returning to \(00000\). It obtains 2048 distinct canonical cycles, as predicted by the classical enumeration \(2^{2^{n-1}-n}\). For each, it directly sorts all 32 rotations of the cycle and of its reversal, computes both run counts, and checks both complete BWT strings against the bit-reversal identities.

Independently, the checker enumerates all Euler circuits of the order-four de Bruijn graph, fixing the unique five-bit edge \(00000\) first. Every order-five de Bruijn cycle corresponds to exactly one such tour after that rooting. It constructs the cyclic words and **recomputes the two BWTs from sorted rotations**, without feedback masks or the block formula. The two enumerations agree on the complete cycle set and all 36 entries of the joint table (including zero cells). The script asserts the displayed table, the difference distribution, both marginals, 2048 total cycles, and eight maximal absolute gaps. This proves the finite assertion via a fully exhaustive, explicit algorithm whose loop bounds and uniqueness are justified above.

A concrete witness at the maximum difference is the 32-bit circular word `00000111110111001101010010001011`: its forward and reversed BWTs have 28 and 20 linear runs, respectively. Its rotations contain every five-bit factor once.

## Verification

Execute `python3 verify_reversal.py` using only the standard Python library. The script returns `VERIFY_OK` after all exact assertions. The direct-rotation and symbolic block formula are checked for every cycle at orders 2 through 5. At order five an independent Euler-tour generation produces the same 2048 canonical cycles and joint table. The finite computation is bounded and exhaustive; the unrestricted order-\(n\) identity is instead established by the preceding mathematical proof.

## Relationship to prior work

The BWT was introduced by Burrows and Wheeler in their public report dated May 10, 1994 [1]. Higgins [2] proves a general characterization of extended BWT outputs for de Bruijn sets; in the binary case this includes the existence of complementary adjacent two-character blocks, but not the correspondence between *forward and reversed* BWT block indices through fixed-width bit reversal. Lipták and Parmigiani [3] use such blocks for random de Bruijn generation, without providing this reversal law. Giuliani and collaborators [4] study BWT run sensitivity to reversing strings, exhibiting large changes for Fibonacci-plus and standard-plus words; those families do not give a joint spectrum for de Bruijn cycles. The overview by Fici and collaborators [5] discusses the de Bruijn block structure and reversal sensitivity separately; it does not combine them into this identity or the exact order-five reversal table.

The forward-only order-five BWT-run marginal distribution is already recorded in an earlier exact classification. The contribution here is **not** the one-dimensional marginal, but the all-order bit-reversal transport law, its exact sharp order-five reversal discrepancy, and the full two-dimensional joint distribution. These are not implied by knowing only either marginal, including when the two marginals happen to match.

## Limitations

The symbolic formula concerns binary de Bruijn cycles, not arbitrary words, generalized extended BWTs of necklace sets, or terminator-augmented suffix BWT. The 2048-cycle joint census is specific to order five; no sharp all-order bound on the size of reversal gaps or closed-form all-order joint distribution is claimed. The finite checker does not certify anything beyond its explicitly exhaustive state space. The priority assessment compares the accessible sources described above, not every unindexed historic manuscript. Independent mathematical assessment has not been performed.

## References

1. M. Burrows and D. J. Wheeler, *A Block-sorting Lossless Data Compression Algorithm*, SRC Research Report 124, May 10, 1994. https://www.cl.cam.ac.uk/teaching/2425/Bioinfo/papers/burrows_wheeler.pdf
2. P. M. Higgins, *Burrows–Wheeler transformations and de Bruijn words*, *Theoretical Computer Science* 457 (2012), 128–136. DOI: 10.1016/j.tcs.2012.07.019. Accessible manuscript: https://arxiv.org/pdf/1901.08392
3. Z. Lipták and L. Parmigiani, *A BWT-Based Algorithm for Random de Bruijn Sequence Construction*, LATIN 2024, 130–145. DOI: 10.1007/978-3-031-55598-5_9. Author talk slides: https://profs.scienze.univr.it/~liptak/files/Santiago2024.pdf
4. S. Giuliani, S. Inenaga, Z. Lipták, N. Prezza, M. Sciortino and A. Toffanello, *Novel Results on the Number of Runs of the Burrows–Wheeler Transform*, arXiv:2008.08506, publicly posted August 19, 2020. https://arxiv.org/pdf/2008.08506
5. G. Fici, S. Mantaci, A. Restivo, G. Romana, G. Rosone and M. Sciortino, *BWT and Combinatorics on Words*, OASIcs 131 (2025), Article 1, published August 8, 2025. https://doi.org/10.4230/OASIcs.Manzini.1
