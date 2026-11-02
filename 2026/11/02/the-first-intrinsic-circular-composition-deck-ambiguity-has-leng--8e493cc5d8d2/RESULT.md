# The first intrinsic circular composition-deck ambiguity has length fifteen

## Finding

For a nonempty binary circular word \(w=(w_i)_{i\in\mathbb Z/n\mathbb Z}\), define its full cyclic composition deck by the integers
\[
H_w(k,j)=\#\left\{i\in\mathbb Z/n\mathbb Z:\sum_{r=0}^{k-1}w_{i+r}=j\right\},
\quad 1\le k\le n,\quad 0\le j\le k.
\]
The deck records **multiplicities** of the Hamming weights of all rooted cyclic contiguous windows, separately for every length. A bracelet is a binary word modulo rotation and reversal; global exchange of zero and one is *not* part of bracelet equivalence.

**Exact finite classification.** For each \(1\le n\le15\), all collisions between distinct bracelets with identical full cyclic composition decks are precisely the following six unordered pairs (each displayed string is the lexicographically least member of its bracelet):

| Length | First bracelet | Second bracelet | Relation by bit complementation |
| --- | --- | --- | --- |
| 12 | `001011001101` | `001011010011` | Yes |
| 14 | `00101011001101` | `00101011010011` | Yes |
| 15 | `000100101001101` | `000100110100101` | No |
| 15 | `000100110001101` | `000100110100011` | No |
| 15 | `001011010111011` | `001011101101011` | No |
| 15 | `001011100111011` | `001011101100111` | No |

Every collision fiber has exactly two bracelets. The first two pairs consist of a bracelet and the bracelet of its complement; the four pairs at length fifteen are two complement-conjugate pairs of *genuine* ambiguities. Thus the first failure of recovery **even when global bit exchange is permitted** occurs at length fifteen. In particular, length thirteen has no collision despite the collision at length twelve.

Let \(B_n\) be the number of binary bracelets and \(D_n\) the number of distinct full cyclic composition decks. Their exact values are:

| \(n\) | \(B_n\) | \(D_n\) | \(n\) | \(B_n\) | \(D_n\) |
| ---: | ---: | ---: | ---: | ---: | ---: |
| 1 | 2 | 2 | 9 | 46 | 46 |
| 2 | 3 | 3 | 10 | 78 | 78 |
| 3 | 4 | 4 | 11 | 126 | 126 |
| 4 | 6 | 6 | 12 | 224 | 223 |
| 5 | 8 | 8 | 13 | 380 | 380 |
| 6 | 13 | 13 | 14 | 687 | 686 |
| 7 | 18 | 18 | 15 | 1224 | 1220 |
| 8 | 30 | 30 |  |  |  |

Consequently, the exact maximum cardinality of a zero-error code using this observation on length-fifteen bracelets is \(1220\), versus \(1224\) possible bracelets.

**Infinite propagation.** If \(u\) and \(v\) are either of the two weight-six, length-fifteen pairs above, then for every integer \(m\ge1\), the circular words \(u^m\) and \(v^m\) have identical decks, yet remain inequivalent under rotations, reversal, and global bit exchange. Therefore intrinsic reconstruction failure occurs at infinitely many lengths, including every positive multiple of fifteen.

## Assumptions and scope

All words are binary, nonempty and cyclic, with rooted windows counted by their starting position. Windows may wrap once around the indicated circle, but their lengths satisfy \(1\le k\le n\). Two strings of length \(n\) represent the same bracelet if one is a rotation of the other or of its reversal. There are no sampling errors and all window-length histograms are available. A global bit exchange maps a word to its complement and changes individual observed Hamming weights; it is considered only when calling an ambiguity *intrinsic*.

The finite classification covers **all** binary words of lengths \(1\) through \(15\), including periodic and constant words. The propagation statement concerns repetitions of the displayed length-fifteen words, for arbitrary \(m\ge1\).

## Proof

**1. Short-window reduction.** Write \(M=\sum_i w_i\). The length-\(k\) cyclic window beginning at phase \(i\) and its complementary length-\(n-k\) cyclic window beginning at \(i+k\) partition the circle. Thus for \(0\le k\le n\), with the natural conventions for empty windows,
\[
H_w(n-k,M-j)=H_w(k,j).
\]
The full deck is therefore determined by \(M\) and the rows with \(1\le k\le\lfloor n/2\rfloor\). Every entry follows from integer sums of explicit bits; no approximation is involved. Rotation and reversal permute the starting phases without changing the rows.

**2. Exhaustive finite argument.** The self-contained `verify.py` is a finite exhaustive proof certificate with no external packages or data. For each \(1\le n\le15\), it enumerates all \(2^n\) binary words. It retains a word exactly when the word is the lexicographic minimum of its \(2n\) rotation/reversal transforms. It computes the short-window weight histograms, groups canonical bracelets by their signatures, and tests the exact collision lists above.

Completeness of the canonical enumeration is immediate: the rotation/reversal transformations act on all \(2^n\) words, and every orbit contains one and only one lexicographically least distinct word. The code additionally sums the sizes of these orbits, obtaining exactly \(2^n\), and independently checks the total against the binary-bracelet Burnside formula
\[
B_n=\frac1{2n}\left(\sum_{d\mid n}\varphi(d)\,2^{n/d}+R_n\right),\qquad
R_n=\begin{cases}n\,2^{(n+1)/2},&n\text{ odd},\\ \frac n2(2^{n/2+1}+2^{n/2}),&n\text{ even}.\end{cases}
\]
Two implementations calculate every candidate histogram, one by directly summing the bits of each rooted window and one by rolling cyclic window sums. Both are compared for each canonical bracelet. The code checks the complementary-window identity, compares the exact fiber populations, asserts that no fiber has size greater than two, and checks bit-complement equivalence and nonequivalence for each displayed pair. The resulting complete counts are the displayed table. This is a **finite exhaustive computation**, not an extrapolation from samples.

For direct reproducibility of the existence of the two intrinsic collision types, the following are their complete *short-row* histograms for the weight-six length-fifteen representatives. A row at length \(k\) lists \((H_w(k,0),\ldots,H_w(k,k))\). Each listed row is shared by both words in its pair; the complementary-window identity supplies every longer row.

| \(k\) | `000100101001101` / `000100110100101` | `000100110001101` / `000100110100011` |
| ---: | --- | --- |
| 1 | `9,6` | `9,6` |
| 2 | `4,10,1` | `5,8,2` |
| 3 | `1,10,4,0` | `2,8,5,0` |
| 4 | `0,7,7,1,0` | `0,7,7,1,0` |
| 5 | `0,3,9,3,0,0` | `0,3,9,3,0,0` |
| 6 | `0,1,7,7,0,0,0` | `0,1,7,7,0,0,0` |
| 7 | `0,0,5,8,2,0,0,0` | `0,0,4,10,1,0,0,0` |

Their bit complements give the other two length-fifteen pairs. Canonical rotation/reversal comparison verifies that neither word in either weight-six pair is equivalent to the other even after complementing. Since the first pair differs at the circular arrangement level, these are not merely alternate starting positions of the same circle.

**3. Propagation to infinitely many lengths.** Let \(u,v\) be either weight-six collision pair of length \(p=15\), so both have weight \(M=6\). Define \(H_w(0,0)=|w|\) and all other entries at length zero to be zero. For \(0\le k\le pm\), write \(k=qp+r\) with \(0\le r<p\). A length-\(k\) window in the \(m\)-fold power \(u^m\) consists, as far as total weight is concerned, of \(q\) complete periods and a residual length-\(r\) window. Every starting phase of \(u\) occurs exactly \(m\) times. Hence
\[
H_{u^m}(k,j)=m\,H_u(r,j-qM)=m\,H_v(r,j-qM)=H_{v^m}(k,j).
\]
If \(u^m\) were a rotation or reversal of \(v^m\), with or without symbol exchange, comparison of the first \(p\) positions after that operation would make \(u\) a rotation or reversal of \(v\), with or without exchange. This contradicts the verified base-pair inequivalence, proving the claimed infinite propagation.

**4. Structural distinction from pair correlations.** The composition deck is stronger than the usual cyclic two-point autocorrelation. Indeed let \(S_k(i)\) be the weight of the length-\(k\) window at phase \(i\), and let \(C_d=\sum_iw_iw_{i+d}\). For \(1\le k\le n\), direct counting of ordered pairs of positions inside each window gives
\[
\sum_i S_k(i)^2=kM+2\sum_{d=1}^{k-1}(k-d)C_d.
\]
Thus \(2C_d\) is the second finite difference, at \(k=d\), of the known sequence \(\sum_iS_k(i)^2\). The deck determines every pair correlation, but the reverse fails: at length fifteen there are \(1144\) different autocorrelation profiles among \(1224\) bracelets, versus \(1220\) distinct full composition decks. Both values are recomputed by the verifier.

## Verification

Run `python3 verify.py` with a standard Python 3 interpreter in the same directory as this document. The program exhausts lengths \(1\) through \(15\), directly and independently recomputes every cyclic-window histogram twice, validates every orbit and the Burnside bracelet counts, and compares all collision fibers with the six displayed pairs. It also explicitly tests the repetition identity for the two weight-six pairs at multipliers \(1\) through \(6\). Successful execution prints `VERIFY_OK`. The infinite repetition assertion is proved in Section 3 rather than inferred from these finite tests.

## Relationship to prior work

Badkobeh, Fici, Kroon and Lipták (public arXiv record June 12, 2012) develop binary jumbled-matching indices and the set of attainable Parikh vectors, where multiplicities of the window compositions and cyclic identification are not the reconstruction statistic. Acharya, Das, Milenkovic, Orlitsky and Pan (public arXiv record March 10, 2014) study complete substring-composition **multisets for linear strings**, up to reversal, and exhibit their first nontrivial collision at linear length eight. Their interleaving construction and prime-length results concern linear endpoints; they do not imply the circular collision table above. Ota and Manada study reconstruction of circular words using frequencies of **ordered substrings** and minimal absent words; discarding order within every window yields a different and weaker observation channel.

Other published results on adjacent-pair multispectra, two-binomial equivalence and substring-attractor censuses concern different observations. Coincidence of a numerical length, common use of a cyclic string, or a binary alphabet is not an implication between their statements and this complete circular composition-deck classification. A targeted literature and published-record search found no covering classification of the six pairs. This is a priority assessment, not a proof of absolute novelty.

## Limitations

Only the sharp *first intrinsic* threshold, the full classification through length fifteen, and the specified infinite family of counterexamples are proved. No full classification for length greater than fifteen is claimed. This observation model requires all noise-free, multiplicity-preserving contiguous cyclic-window composition histograms, and does not model sampling errors, missing windows, scattered subsequences, or larger alphabets. Literature not indexed or inaccessible in the searches could affect historical priority. 

## References

1. G. Badkobeh, G. Fici, S. Kroon, Z. Lipták, *Binary Jumbled String Matching for Highly Run-Length Compressible Texts*, arXiv:1206.2523, first publicly submitted 2012-06-12. https://arxiv.org/abs/1206.2523
2. J. Acharya, H. Das, O. Milenkovic, A. Orlitsky, S. Pan, *String Reconstruction from Substring Compositions*, arXiv:1403.2439, first publicly submitted 2014-03-10. https://arxiv.org/html/1403.2439v1
3. T. Ota, A. Manada, *A Reconstruction of Circular Binary String Using Substrings and Minimal Absent Words*, IEICE Transactions on Fundamentals, 107-A(3), 409–416 (2024), DOI:10.1587/transfun.2023TAP0015. https://doi.org/10.1587/transfun.2023TAP0015
4. The self-contained `verify.py` accompanying this result (finite enumeration and independent histogram implementations).
