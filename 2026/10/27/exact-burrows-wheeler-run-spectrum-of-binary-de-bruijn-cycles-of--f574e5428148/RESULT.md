# Exact Burrows–Wheeler run spectrum of binary de Bruijn cycles of order five

## Finding

Let \(\mathcal D_5\) be the set of binary de Bruijn cycles of order five, considered up to cyclic rotation (but **not** reversal or complementation). Let \(\mathrm{BWT}(C)\) be the last column of the lexicographically sorted table of the 32 cyclic rotations, with alphabet order \(0<1\), without a sentinel. Let \(r(C)\) count the maximal consecutive equal-letter runs in that linear column. Then

\[
\sum_{C\in\mathcal D_5}t^{r(C)}
=38t^{20}+426t^{22}+840t^{24}+608t^{26}+130t^{28}+6t^{30}.
\]

In particular, the possible run counts are exactly \(20,22,24,26,28,30\); precisely 38 of the 2,048 cycles attain the minimum 20. The elementary bound \(r(C)\ge 2^{k-1}+2\) for every binary de Bruijn cycle of order \(k\ge2\) is attained for \(k=2,3,4\), but is strictly unattainable for \(k=5\). Thus order five is the first strict instance of this run-bound gap.

## Assumptions and scope

A binary de Bruijn cycle of order \(k\) is a binary circular word of length \(2^k\) in which every length-\(k\) binary word occurs exactly once as a cyclic factor. A cycle means a rotation class, not an individually marked rotation. The Burrows–Wheeler transform uses all \(2^k\) rotations in ascending lexicographic order. Every de Bruijn cycle is primitive, so no rotations tie. The statistic is the *linear* run count of the final column, starting with a new run at its first character. For the cycles considered, its first and final bits differ, so it also equals the circular run count. All enumerations are exact integers; no statistical estimation is used.

## Proof

**Block characterization and permutation.** For order five, there are 16 possible binary length-four words \(u\). The two rotations whose length-five prefixes are \(u0\) and \(u1\) occupy consecutive rows (indexed \(2i,2i+1\) in lexicographic order, with \(i\in\{0,\ldots,15\}\) the numerical value of \(u\)). Their preceding symbols must be different: if they both had predecessor \(b\), the same length-five factor \(bu\) would occur twice. The final column therefore consists of 16 blocks

\[
(\epsilon_0,1-\epsilon_0)(\epsilon_1,1-\epsilon_1)\cdots(\epsilon_{15},1-\epsilon_{15}),\qquad \epsilon_i\in\{0,1\}.
\]

Conversely, to each of the \(2^{16}\) binary orientation vectors associate the 32-element last-column word above and its usual last-to-first permutation \(\lambda\), with zero-based ranks. The zero and one counts before block \(i\) are both \(i\). Hence

\[
\lambda(2i)=i+16\epsilon_i,\qquad
\lambda(2i+1)=i+16(1-\epsilon_i).
\]

This map is a permutation of \(\{0,\ldots,31\}\). Each step replaces the represented length-five prefix by its uniquely chosen preceding-symbol extension, shifting one place backward. Consequently, \(\lambda\) has one 32-cycle **if and only if** it generates one binary de Bruijn cycle of order five. If it has multiple cycles, it generates multiple shorter closed directed walks and does not define a member of \(\mathcal D_5\). Conversely, any member of \(\mathcal D_5\) uniquely determines its orientation vector, and its inverse permutation is a 32-cycle. The 32 rows of the rotation table are distinguished by their length-five prefixes, so reconstruction loses no multiplicities or distinct rotation classes.

**Run identity and lower bound.** Each of the 16 blocks contributes one run boundary internally. Across the boundary between blocks \(i\) and \(i+1\), another run boundary occurs exactly when \(1-\epsilon_i\ne\epsilon_{i+1}\), that is, when \(\epsilon_i=\epsilon_{i+1}\). Thus

\[
r(C)=17+\sum_{i=0}^{14}[\epsilon_i=\epsilon_{i+1}].
\]

More generally, write \(m=2^{k-1}\) and apply the same reasoning to the \(m\) two-character blocks of any order-\(k\) cycle, for \(k\ge2\). The unique occurrence of \(0^k\) forces its predecessor to be 1, while the unique occurrence of \(1^k\) forces its predecessor to be 0; otherwise an all-zero or all-one factor would repeat at consecutive offsets. Accordingly \(\epsilon_0=\epsilon_{m-1}=1\). Since \(m-1\) is odd, not all adjacent bits of the orientation vector can differ, and so at least one boundary between blocks is a run boundary. This proves \(r(C)\ge m+2=2^{k-1}+2\). The equality of the endpoint bits also implies that all such run counts are even.

**Complete finite certificate at order five.** The accompanying `verify.py` tests all 65,536 orientation vectors. For each vector, it builds \(\lambda\) with the displayed formula, tests whether the orbit of rank zero visits precisely 32 distinct ranks and closes, reconstructs the unique canonical cycle if it does, independently computes its sorted-rotation transform, and tallies the run count. It yields this exact table:

| Run count | Number of rotation classes |
| ---: | ---: |
| 20 | 38 |
| 22 | 426 |
| 24 | 840 |
| 26 | 608 |
| 28 | 130 |
| 30 | 6 |
| Total | 2,048 |

The same self-contained verifier uses a structurally independent enumeration: enumerate Eulerian circuits in the binary de Bruijn digraph whose vertices are length-four words and whose edges are length-five words, fixing the unique all-zero edge as the first edge. Each completed circuit determines one canonical rotation class, and its lexicographically sorted cyclic rotations give its BWT directly. The two methods produce **identical dictionaries of all 2,048 canonical words and run counts**, not merely matching histograms. The root edge has a unique occurrence in every de Bruijn cycle, so this graph method has neither missing classes nor rotational duplicates. In smaller orders the same graph method gives spectra \(t^4\), \(2t^6\), and \(4t^{10}+4t^{12}+8t^{14}\) for orders two, three, and four, respectively, establishing the first-failure statement. These are exhaustive finite enumerations, with complete source code as part of the proof certificate.

## Verification

Run `python3 verify.py` with a standard Python 3 interpreter. No external packages, downloads, or other data files are needed. The program checks all orientation vectors, reconstructs the corresponding words, checks all 32 length-five cyclic factors, recomputes the BWT by lexicographically sorting all rotations, and independently enumerates rooted Euler circuits. It asserts equality of complete maps, a total of 2,048 cycles, the six specified frequencies, and the smaller-order certificates. Successful execution ends with `PASS: independent exhaustive BWT/LF and Euler-cycle enumerations agree`. The finite enumeration is an exhaustive proof here because the block characterization reduces the entire domain to exactly \(2^{16}\) explicitly checked cases; this is not an extrapolation from samples.

## Relationship to prior work

Higgins (2012) established the fundamental representation of the BWT of a binary de Bruijn word as concatenated two-symbol permutations and characterized inversion through permutation cycles. That structural result is used here, with an explicit proof for the binary finite case; it does **not**, in the inspected manuscript/presentation, provide the order-five run-count distribution or identify the first strict gap from the elementary run bound. Kucherov–Tóthmérész–Vialette (2012) relate suffix arrays to BWT permutations, but do not classify this cyclic de Bruijn run statistic. Fici–Gabory (2025) treat generalized de Bruijn words and BWT characterizations, which provide broader structural context but not the specific six-coefficient run spectrum. The result is an exact run-compressibility refinement of those structural characterizations, not a new characterization of de Bruijn words.

## Limitations

The exact run-frequency polynomial is established only for **binary order five**, and the first-gap comparison only concerns the specified elementary lower bound at orders two through five. No formula for arbitrary order or other alphabets is asserted. The enumeration is exact and self-contained but has not undergone independent mathematical audit. Priority could be affected by unindexed numerical tables or algorithmic enumerations in the older BWT literature; structural characterizations alone are not priority evidence for the displayed polynomial. The supporting archival source-date record is a verified first arXiv version of the 2012 BWT-permutation literature, not a claim of when the entire subject began.

## References

1. P. M. Higgins, “Burrows–Wheeler transformations and de Bruijn words,” *Theoretical Computer Science* **457** (2012), 128–136, DOI: `10.1016/j.tcs.2012.07.019`. Related author presentation (November 2012): https://www.macs.hw.ac.uk/~markl/Higgins.pdf.
2. G. Kucherov, L. Tóthmérész, S. Vialette, “On the combinatorics of suffix arrays,” arXiv:1206.3877v1 (first publicly submitted 2012-06-18): https://arxiv.org/abs/1206.3877.
3. G. Fici, E. Gabory, “Generalized De Bruijn Words, Invertible Necklaces, and the Burrows–Wheeler Transform,” *MFCS 2025*, Article 48, DOI: `10.4230/LIPIcs.MFCS.2025.48`; arXiv:2502.12844: https://arxiv.org/abs/2502.12844.
