# Interval-support characterization for binary three-window composition multispectra and the sharp four-window obstruction

## Finding

For each integer \(m\ge1\) and binary word \(w=w_1\cdots w_{m+2}\), let \(H_3(w)=(c_0,c_1,c_2,c_3)\), where \(c_j\) is the number of indices \(i\in\{1,\ldots,m\}\) such that the consecutive length-three factor \(w_iw_{i+1}w_{i+2}\) has exactly \(j\) ones. This vector retains the multiplicities of unordered composition reads but discards their positions.

**Theorem.** A nonnegative integer vector \((c_0,c_1,c_2,c_3)\) is \(H_3(w)\) for some binary word \(w\) of length \(m+2\) **if and only if** \(\sum_{j=0}^3c_j=m\) and its positive coordinates have consecutive indices. More precisely, whenever \(c_a,c_b>0\) and \(a<b\), all \(c_j>0\) for \(a<j<b\); and every such profile admits a constructive witness.

Consequently the number of distinct three-window composition multispectra is exactly
\[
T_m=\sum_{r=1}^{\min(4,m)}(5-r)\binom{m-1}{r-1}=\frac{m^3+11m+12}{6},\qquad m\ge1.
\]
Of the \(\binom{m+3}{3}\) formal nonnegative four-coordinate profiles, precisely \(m^2-1\) are impossible. The generating function is
\[
\sum_{m\ge1}T_m z^m=\frac{z(4-9z+8z^2-2z^3)}{(1-z)^4}.
\]
For the deterministic read-composition channel that supplies only \(H_3(w)\), the largest zero-error code of length \(m+2\) has \(T_m\) words. The constructive proof gives one representative of each channel output in \(O(m)\) time per profile.

The three-window result is the last instance of the **interval-support sufficiency** property: for every fixed window width \(h\ge4\), the all-positive profile \((1,1,2,1,\ldots,1)\), with \(h+1\) coordinates and the extra count in the coordinate indexed \(2\), is not realized by any binary word of length \(2h+1\). Its coordinate sum is \(h+2\). In particular, \((1,1,2,1,1)\) is unrealizable at width four although it has consecutive positive support.

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\); factors are contiguous; all factors are taken with overlap; the channel observes the **multiset of their compositions**, not their order, their locations, or their literal bit patterns. A profile contains four nonnegative integer counts. For the main theorem the read length is exactly three and the host length is \(m+2\), with \(m\ge1\). The sharpness assertion about windows of width \(h\) is a counterexample for each \(h\ge4\), not a classification of all profiles of wider windows. Binomial coefficients with an upper argument below the lower nonnegative argument are zero.

## Proof

**Necessity.** Write \(s_i=w_i+w_{i+1}+w_{i+2}\). Each successive window discards one bit and adds one bit, so \(s_{i+1}-s_i=w_{i+3}-w_i\in\{-1,0,1\}\). A finite walk on integer levels with steps of magnitude at most one visits every level between its minimum and maximum. Therefore, if weights \(a<b\) occur in the window sequence, every intermediate weight occurs, establishing interval support. There are exactly \(m\) windows, giving the sum condition.

**Construction: preliminary gadgets.** Adding one bit to the left of a word whose first two bits are \(00\) produces the new triple \(000\) if the new bit is \(0\). Adding \(1,0,0\) successively to the left of a word initially beginning \(00\) produces, in order, the new triples \(100,010,001\): each has weight one, and after the three steps the word again begins \(00\). Thus any number of weight-one windows may be added at the left by the cyclic prepending schedule \(1,0,0,1,0,0,\ldots\). Analogously, if the word ends \(11\), appending \(0,1,1\) in that order produces the weight-two triples \(110,101,011\) and restores the suffix \(11\). Repeating that schedule adds any number of weight-two windows. Appending \(1\) to a word ending \(11\) adds one weight-three window. For a word ending \(01\), the appending schedule \(0,0,1\) produces weight-one triples \(010,100,001\), restores suffix \(01\), and can be repeated indefinitely.

**Construction: all possible supports.** Suppose the desired positive support is a singleton \(\{j\}\). Repeat a fixed binary period of length three and weight \(j\), namely one of \(000,001,011,111\), and take its first \(m+2\) symbols. Every triple then has weight \(j\). For support with at least two indices, the cases below each start with **one occurrence of every listed weight**:

* Support \(\{0,1\}\): start from \(0001\), prepend \(c_0-1\) zeros, and append \(c_1-1\) bits from the periodic schedule \(0,0,1\).
* Support \(\{1,2\}\): start from \(0011\), prepend \(c_1-1\) bits from \(1,0,0\), then append \(c_2-1\) bits from \(0,1,1\).
* Support \(\{0,1,2\}\): start from \(00011\), prepend \(c_0-1\) zeros, prepend \(c_1-1\) bits from \(1,0,0\), and append \(c_2-1\) bits from \(0,1,1\).
* Support \(\{0,1,2,3\}\): start from \(000111\), prepend \(c_0-1\) zeros, append \(c_3-1\) ones, prepend \(c_1-1\) bits from \(1,0,0\), and append \(c_2-1\) bits from \(0,1,1\).

Each schedule retains exactly the required two-bit state at its active end. Adding bits creates one new initial or terminal length-three window without modifying existing windows. The complements of the constructions for \(\{0,1\}\) and \(\{0,1,2\}\) cover \(\{2,3\}\) and \(\{1,2,3\}\), respectively. These are all contiguous supports in \(\{0,1,2,3\}\). Each construction has exactly \(m\) length-three windows, hence length \(m+2\), proving sufficiency.

**Exact enumeration.** For positive support consisting of \(r\) consecutive indices there are \(5-r\) placements in \(\{0,1,2,3\}\). Each placement has \(\binom{m-1}{r-1}\) positive compositions of the total \(m\). Summing yields the displayed formula for \(T_m\). Since the total number of nonnegative four-tuples summing to \(m\) is \(\binom{m+3}{3}\), subtraction gives \(\binom{m+3}{3}-T_m=m^2-1\). Expanding the binomial sum gives the rational generating function. A zero-error code can contain at most one word per profile, and choosing one constructed witness for each profile attains that bound.

**Failure for every width \(h\ge4\).** Suppose a binary word of length \(2h+1\) had the width-\(h\) weight-histogram with one occurrence of each weight \(0,1,\ldots,h\), except that weight \(2\) appears twice. Presence of weights zero and \(h\) forces factors \(0^h\) and \(1^h\). These are disjoint; because the word has length \(2h+1\), apart from these two blocks there is exactly one unused bit. Thus, up to complementing the bits, the word is obtained by inserting one bit before, between, or after the blocks of \(0^h1^h\). Directly comparing length-\(h\) window sums shows that the sole repeated weight is respectively in \(\{0,1,h-1,h\}\): adding a bit before the blocks repeats \(0\) or \(1\); adding a bit between repeats \(0\) or \(h\); adding a bit after repeats \(h-1\) or \(h\). For \(h\ge4\), weight \(2\) does not belong to this set. This contradiction establishes the claimed obstruction. At \(h=3\), these four candidate duplicate weights exhaust all four weights, consistent with the interval-support theorem. \(\square\)

## Verification

A standalone standard-library Python program, `verify.py`, checks the constructive witness for all \(28{,}273\) realizable interval profiles through \(m=28\); independently generates all possible profiles by a two-bit-state dynamic program for \(1\le m\le40\) (\(113{,}650\) distinct profiles across these values); and enumerates all \(131{,}064\) literal words of lengths three through sixteen. For widths three through eight it independently enumerates \(174{,}720\) literal words of lengths \(2h+1\) to check that the only feasible one-duplicate full-support positions are \(\{0,1,h-1,h\}\) (which is all positions when \(h=3\)). The checks are finite confirmations; the preceding mathematical argument establishes all-length statements.

Reproduce with Python 3: `python verify.py`.

## Relationship to prior work

Marcovich and Yaakobi study length-fixed **literal substring** multispectra and reconstruction under missing or erroneous reads, whereas the observation here identifies all length-three factors with the same number of ones and asks for the *full set of feasible count-vectors*. Gupta and Mahdavifar study reconstruction from composition multisets of substrings of **all lengths**, a strictly more informative observation; their methods and codebook results do not give this length-three output-space characterization. Sporring and Darkner consider an **ordered sequence** of sliding local histograms and reconstruct signals from that ordered stream; the present observation discards window order entirely.

The cubic polynomial \((m^3+11m+12)/6\) is **already recorded** numerically in OEIS A188554 for a different family of monotone-step words and pattern-avoiding binary arrays. The polynomial's numerical sequence is **not claimed to be new**. The substantive result here is the exact realizability bridge between binary overlapping triple-read profiles and gap-free supports, with constructive optimal codebooks and a sharp obstruction beginning at read length four. Earlier binary read-length-two composition-multispectrum counts concern a different observation length and do not imply this realizability theorem.

## Limitations

No new exact numerical sequence is claimed: its coincident values and formula have an earlier independent interpretation in OEIS A188554. The characterization and optimal codebook apply only to noiseless, unordered binary length-three composition reads, without deletions, substitution errors, or uncertain observation counts. The width-four obstruction disproves an extension of the interval criterion but does not enumerate all feasible profiles for larger read lengths. A further independently discovered proof of the same realizability bridge may exist in the literature, especially in less-indexed work on sliding-window histograms. No independent formal or expert validation is claimed.

## References

1. S. Marcovich and E. Yaakobi, *Reconstruction of Strings from their Substrings Spectrum*, arXiv:1912.11108, first submitted 2019-12-23. https://arxiv.org/abs/1912.11108
2. U. Gupta and H. Mahdavifar, *A New Algebraic Approach for String Reconstruction from Substring Compositions*, arXiv:2201.09955, first submitted 2022-01-24. https://arxiv.org/abs/2201.09955
3. J. Sporring and S. Darkner, *Reconstructing Binary Signals from Local Histograms*, Entropy 24(3), 433 (2022). https://doi.org/10.3390/e24030433
4. OEIS Foundation, A188554, *Number of 3 × n binary arrays without the pattern 0 1 in four directions* (first recorded 2011); see the 2024 comment interpreting the values as nonincreasing-step words and the existing cubic formula. https://oeis.org/A188554
