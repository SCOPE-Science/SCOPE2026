# Exact maximum reverse-shuffle root multiplicities through length \(20\)

## Finding
For an integer \(n\ge1\) and a binary word \(w\in\{0,1\}^{2n}\), define its **reverse-shuffle root set**
\[
\mathcal R(w)=\{r\in\{0,1\}^{n}:w\text{ is an order-preserving interleaving of }r\text{ and }r^{\mathrm R}\},
\]
where \(r^{\mathrm R}\) denotes reversal. A root is counted **once**, regardless of the number of supporting interleavings. Write
\[
M_n=\max_{w\in\{0,1\}^{2n}}|\mathcal R(w)|.
\]
The complete sharp extremal profile for **every** \(1\le n\le10\) is:

| \(n\) | \(M_n\) | Number of maximizing binary words |
|---:|---:|---:|
| 1 | 1 | 2 |
| 2 | 2 | 4 |
| 3 | 3 | 8 |
| 4 | 5 | 8 |
| 5 | 9 | 8 |
| 6 | 16 | 8 |
| 7 | 29 | 8 |
| 8 | 52 | 8 |
| 9 | 94 | 8 |
| 10 | 170 | 8 |

In particular, \(M_{10}=170\), attained by exactly eight words of length \(20\). Their complete list is:

- `01010101101010101010`
- `01010101011010101010`
- `01010101100110101010`
- `01010101010110101010`
- `10101010101001010101`
- `10101010011001010101`
- `10101010100101010101`
- `10101010010101010101`

There are no other length-\(20\) maximizers. The corresponding word universe contains \(2^{20}=1,048,576\) candidates; the number with any reverse-shuffle root is \(\binom{20}{10}=184,756\).

## Assumptions and scope
Words are **labeled binary**, linear, and of even length; reversal acts on the letters of the root, not on the source word. Two distinct position partitions yielding the same root are not counted separately. There are no quotient operations by reversal, complementation, rotation, or word isomorphism. All claims about sharp maxima and optimizer counts are **finite**, restricted to \(1\le n\le10\); no formula for larger lengths is asserted.

## Proof
Fix \(n\in\{1,\ldots,10\}\). Every interleaving of \(r\) with \(r^{\mathrm R}\), for \(r\in\{0,1\}^{n}\), is specified by a set \(P\subseteq\{0,\ldots,2n-1\}\) of size \(n\): positions in \(P\) receive the letters of \(r\) in forward order and the complementary positions receive the letters of \(r\) in backward order. Conversely, **every** root of **every** binary length-\(2n\) word admits at least one such partition. Thus the root--partition pairs form a finite, exhaustive representation without any structural exclusions.

The standalone file `enumerate.cpp` uses two exhaustive finite loops: it ranges over all \(2^{2n}\) binary masks, retaining **exactly** those with \(n\) set bits, and then over all \(2^n\) binary roots. For each pair, it constructs the unique interleaved source word exactly as above and sets one bit indexed by that source and root. Bitwise OR merges multiple supporting partitions for the same root. Therefore, after these loops, the population count of the bitset of each word is **exactly** \(|\mathcal R(w)|\), not an approximation or count of decompositions. A final complete scan over every word computes the maximum, all maximizing words, and the full root-count histogram. This is a terminating exhaustive proof for each specified \(n\).

For the upper bound at \(n=10\), the program verifies that all \(\binom{20}{10}=184,756\) masks were visited and all \(2^{10}\binom{20}{10}=189,190,144\) root--mask pairs processed. It finds maximum \(170\), achieved precisely at the eight listed words. The same argument and run apply independently for each \(1\le n\le9\), yielding the table.

For a separate check on the coverage of source words, a binary reverse-shuffle square must be an **abelian square**: its first and second halves have equal letter counts. Conversely, for a binary abelian square, match corresponding zeros in reverse order and corresponding ones in reverse order across the two halves. The induced matching permutation splits into two decreasing subsequences and hence avoids \(123\); Lemma 6.2 of He--Huang--Nam--Thaper implies that the word is a reverse-shuffle square. Therefore the number of words with nonempty root set is \(\sum_{k=0}^n\binom{n}{k}^2=\binom{2n}{n}\). This statement is used **only as a coverage cross-check**, not claimed as a new result or as a replacement for the maximality enumeration.

## Verification
Compile the standalone verifier with `g++ -O3 -std=c++17 enumerate.cpp -o enumerate` and run `./enumerate 10` (and analogously for each smaller positive integer). `profile.txt` contains all ten exact extremal results, the full finite histograms, and the complete optimizer lists. Execute `python verify_small.py` for a logically independent direct-word, direct-partition enumeration through \(n=6\). Execute `python verify_witnesses.py` from the same directory to check \(170\) **distinct** length-\(10\) roots of the first displayed maximizer using the explicit position selections in `witnesses_n10.tsv`.

All these checks were executed against these specific files. The exhaustive program confirmed the expected mask and assignment totals and the independent attainable-word count \(\binom{2n}{n}\) for every \(n\le10\). The direct partition program agrees through \(n=6\), and all \(170\) lower-bound root certificates passed their character-by-character checks. The upper bounds for \(n=7,8,9,10\) depend on the complete C++ enumeration as specified, rather than on a second independently implemented full search at those lengths.

## Relationship to prior work
He, Huang, Nam, and Thaper introduced and characterized reverse shuffle squares, including their Lemma 6.2 and large-alphabet asymptotic enumeration. That characterization does not provide the **number of distinct generating roots of each given binary word**, nor the sharp maximum of that statistic. Grytczuk, Pawlik, and Pleszczyński studied related generalized squares and cutting distances, not the root-multiplicity maximum. Datko and Pawlik gave a finite extremal-root table for **ordinary** binary shuffle squares \(r\shuffle r\), not reverse shuffle squares \(r\shuffle r^{\mathrm R}\): their length-\(20\) ordinary maximum is \(19\), whereas the statistic treated here has maximum \(170\). The two root conventions are not interchangeable (for example, `0110` has two reverse-shuffle roots but no ordinary shuffle root).

## Limitations
No asymptotic limit, recurrence, or proof for \(n\ge11\) is claimed. The integer sequence of finite maxima should not be extrapolated as an infinite identity. Although the finite proof is exhaustive, independent external mathematical validation is still outstanding. Prior coverage checks cannot exclude all unindexed or unavailable enumerations, and an earlier computation of the same finite inverse-shuffle maximum remains a residual originality risk.

## References
1. X. He, E. Huang, I. Nam, R. Thaper, *Shuffle Squares and Reverse Shuffle Squares*, arXiv:2109.12455 (first public preprint September 25, 2021); especially the reverse-shuffle characterization, Lemma 6.2. An accessible complete preliminary manuscript is *Twins in Words and Shuffle Squares*, SURIM 2021, Section 6, `https://surim.stanford.edu/sites/g/files/sbiybj26191/files/media/file/twins_in_words_and_shuffle_squares.pdf`.
2. J. Grytczuk, B. Pawlik, M. Pleszczyński, *More Variations on Shuffle Squares*, *Symmetry* **15** (2023), 1982, doi:10.3390/sym15111982 (earlier arXiv:2308.13882).
3. D. Datko, B. Pawlik, *Roots of Binary Shuffle Squares*, *Symmetry* **17** (2025), 305, doi:10.3390/sym17020305, especially Table 6 (ordinary-shuffle roots).
