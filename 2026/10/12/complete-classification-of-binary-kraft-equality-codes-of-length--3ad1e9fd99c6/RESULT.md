# Complete classification of binary Kraft-equality codes of lengths three and four

## Finding

For any binary word-set code \(C\subseteq\{0,1\}^3\cup\{0,1\}^4\) containing at least one word of each length and satisfying the Kraft equality \(\sum_{w\in C}2^{-|w|}=1\), let \(a=|C\cap\{0,1\}^3|\). The exact number of uniquely decodable labeled *word sets*, with order of codewords disregarded, is

\[
U(a)=2\binom{8}{a}+4\mathbf{1}_{\{a=5\}},\qquad 1\le a\le7.
\]

The seven counts are \(16,56,112,140,116,56,16\), totaling **512**. Precisely 254 are prefix-free, 254 suffix-free, and **four are neither**. Those four, all with five words of length three and six of length four, form one orbit under global complementation and reversal. They are listed in `EXCEPTIONS.tsv`; the file `CENSUS.csv` gives all candidate and uniquely decodable counts.

## Assumptions and scope

A code is an **unordered set of distinct nonempty binary words**. It is uniquely decodable if two finite sequences of words from it cannot have the same concatenation unless the sequences are identical. A prefix code (respectively suffix code) has no word properly prefixing (respectively suffixing) another. The allowed lengths are *exactly three and four* and both must occur. Writing \(b=|C\cap\{0,1\}^4|\), equality in the Kraft--McMillan bound means \(2a+b=16\), hence \(b=16-2a\), with \(1\le a\le7\). Codewords are distinct, not counted with arbitrary orderings. This is a finite classification, not an asymptotic theorem.

## Proof

**Exhaustive reduction.** First select the \(a\) short words from all eight three-bit strings, and then select the \(16-2a\) long words from all 16 four-bit strings. Every admissible candidate appears exactly once. The number of candidates is

\[
\sum_{a=1}^7\binom{8}{a}\binom{16}{16-2a}=1,901,636.
\]

Apply the Sardinas--Patterson criterion: with \(D_0=C\), form the set \(D_1\) of nonempty remainders from proper prefix comparisons of codewords; inductively form \(D_{i+1}\) by removing a codeword prefix from a remainder in \(D_i\), or a remainder prefix from a codeword. The code is uniquely decodable precisely when no \(D_i\), for \(i\ge1\), meets \(C\) (equivalently, no comparison produces the empty remainder). Only suffixes of codewords appear, so the process is finite-state and repetition of a previously seen set makes the answer permanent. `verify_independent.py` implements this literal set recurrence over all 1,901,636 choices; `verify_bitmask.cpp` independently builds the graph of possible proper-suffix transitions and tests reachability of a codeword remainder. Both give the seven claimed totals and the same four exceptional codes.

**Ordinary prefix and suffix classes.** Given a chosen short set \(S\) of size \(a\), the *unique* prefix code at Kraft equality has long layer consisting of all four-bit words whose length-three prefix is not in \(S\). Thus there are \(\binom{8}{a}\) prefix codes. Reversal gives the same number of suffix codes. Their intersection is empty for \(1\le a\le7\): if a code is both, then membership of each three-bit prefix in \(S\) must equal membership of the corresponding three-bit suffix for every four-bit word. Along the strongly connected binary de Bruijn graph on three-bit words, that forces \(S\) to be empty or all eight words, contrary to scope. The computed number of additional uniquely decodable codes is exactly four, all at \(a=5\).

**Direct exceptional-code certificate.** One exceptional code has the length-three words `000 001 010 011 110` and length-four words `0001 0011 0101 0111 1101 1111`. Its Sardinas--Patterson remainder sets alternate \(D_1=\{\texttt{1}\}\) and \(D_2=\{\texttt{10},\texttt{101},\texttt{111}\}\), neither intersecting the code, so it is uniquely decodable despite being neither prefix nor suffix. Global bit complementation and reversal of all codewords preserve unique decodability and generate the other three exceptions; the direct exhaustive calculation proves no others exist.

Because every enumerated code has Kraft sum one, a uniquely decodable code cannot be enlarged by any new word: that would violate the Kraft--McMillan inequality. Schützenberger's established theorem for finite maximal codes implies that finite left-to-right deciphering delay would force the code to be prefix-free. Hence all 258 nonprefix members here have infinite deciphering delay; the finite-delay implication is **prior theory**, not a novelty claim.

## Verification

Compile and run the standalone exact enumerator with `g++ -std=c++17 -O3 verify_bitmask.cpp -o check && ./check`, and run the independent textual Sardinas--Patterson implementation with `python3 verify_independent.py`. The expected counts by \(a=1,\ldots,7\) are `16,56,112,140,116,56,16`; the expected four exceptional word sets are in `EXCEPTIONS.tsv`. Both programs examine the full \(1,901,636\)-candidate space and were executed successfully. The enumeration also checks that there are no additional finite-delay nonprefix cases by residual-graph cycle detection, agreeing with the cited general theorem.

## Relationship to prior work

The Sardinas--Patterson test and Kraft--McMillan inequality are classical. Woryna's 2016 work studies counts of uniquely decodable codes with prescribed word-length sequences, including a specific three-word length profile and a family with one exceptional length divisible by the others. Neither covers the present mixed multiplicities at lengths three and four. Woryna's 2018 study proves bounds on the ratio of prefix to uniquely decodable codes and gives exact results for two-codeword sequences, not this full saturated census. Schützenberger's finite-delay theorem accounts for the delay statement, which is explicitly not presented as new. Related fix-free and non-overlapping codes impose stronger restrictions and their enumerations do not imply this uniquely decodable classification.

## Limitations

This exact result applies to one binary finite-length profile, not to all length distributions. The programs provide a finite exhaustive proof, not a symbolic all-length classification. No claim is made about error correction, synchronization after corruption, or expected decoding complexity. Earlier unindexed exact enumerations might exist; independent literature verification has not been performed.

## References

- A. Woryna, *On the set of uniquely decodable codes with a given sequence of code word lengths*, arXiv:1608.08381 (first public version 2016-08-30), sections 1--4. https://arxiv.org/abs/1608.08381
- A. Woryna, *On the ratio of prefix codes to all uniquely decodable codes with a given length distribution*, arXiv:1804.02531 (2018), sections 1 and 4. https://arxiv.org/abs/1804.02531
- A. Sardinas and G. W. Patterson, *A necessary and sufficient condition for the unique decomposition of coded messages*, I.R.E. Convention Record, Information Theory, 1953, pp. 104--108; algorithm as presented in Woryna (2016).
- J. Berstel, D. Perrin, and C. Reutenauer, *Codes and Automata*, chapter 5, Theorem 5.2.4 (Schützenberger's finite-maximal-code theorem), Cambridge University Press, 2009. DOI: 10.1017/CBO9781139195768.006
