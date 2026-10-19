# Complete length-thirteen binary one-gap three-deck reconstruction classes

## Finding
For binary words of length \(13\), the one-gap deck through subsequence length \(3\) has exactly \(8188\) distinct profiles: \(8184\) singleton fibers and exactly four fibers of cardinality \(2\), with no larger fibers. The four exceptional fibers, represented by their two words in lexicographic order, are:

| First word | Second word |
| --- | --- |
| `0001010000100` | `0010000101000` |
| `0101111010110` | `0110101111010` |
| `1001010000101` | `1010000101001` |
| `1101111010111` | `1110101111011` |

In each row the right-hand word is the reversal of the left-hand word. The four fibers form two orbits under global bit complementation. Hence the largest code in which no two distinct words have the same observation contains exactly \(8188\) words, and exactly \(16\) maximum *labeled* codebooks exist. The words of lengths \(3\) through \(12\) have distinct profiles, whereas at length \(2\) the words `01` and `10` collide because no spaced length-two observation exists.

## Assumptions and scope
The alphabet is \(\{0,1\}\). For a binary word \(w=w_1\cdots w_n\), a pattern \(v=v_1\cdots v_\ell\) with \(1\leq\ell\leq3\), and an ordered index tuple \(1\leq i_1<\cdots<i_\ell\leq n\), call the tuple admissible when \(i_{j+1}-i_j\geq2\) for every \(j\). The count \(F_n(v;w)\) is the number of admissible tuples with \(w_{i_j}=v_j\) for all \(j\). The profile is the vector of these counts for all \(2+4+8=14\) patterns \(v\) of lengths \(1,2,3\), in increasing binary order within each length. Counts are exact integers; the sequence order is not discarded.

A zero-error reconstruction code is a subset of \(\{0,1\}^{13}\) on which this profile map is injective. The claim concerns this fixed finite length and this precise observation. It is not a theorem for arbitrary lengths, larger gaps or alphabets.

## Proof
For any prefix length \(i\), write \(F_i(v)\) for the multiplicity of pattern \(v\) in the first \(i\) symbols. Empty-pattern counts in any prefix equal \(1\), and all nonempty-pattern counts in the zero prefix are \(0\). For the newly appended last symbol \(b=w_i\), the admissible tuples either omit index \(i\) or include it. This gives, for every symbol \(a\),
\[
F_i(a)=F_{i-1}(a)+\mathbf 1_{a=b}.
\]
For each nonempty word \(u\) of length at most \(2\),
\[
F_i(ub)=F_{i-1}(ub)+F_{i-2}(u)
\]
when the last symbol equals \(b\), while for the other last symbol the count is unchanged. The second term requires the preceding picked index to lie at most \(i-2\). For \(i=1\), every such extension count vanishes. These recurrences compute the full fourteen-coordinate profile for each binary word using integer addition only.

The standalone program `gapped_verify_dp.cpp` enumerates every one of the \(2^{13}=8192\) words via these recurrences. It groups the *entire* fourteen-coordinate integer vector in an ordered map; therefore distinct vectors cannot be merged by hash collisions. The exact enumerated group sizes are \(8184\) classes of size \(1\) and four classes of size \(2\). The program asserts the four exact pairs displayed above and asserts that every pair consists of mutual reversals. It also enumerates every word at each length from \(1\) through \(12\), checking the stated injectivity range and the degenerate length-two exception.

A mathematically independent exhaustion is supplied by `gapped_verify_direct.py`. It enumerates all index combinations of lengths \(1,2,3\), discards tuples containing consecutive indices, explicitly constructs each binary subsequence, and accumulates fourteen pattern counts. Thus its kernel does not rely on the prefix recurrence. It independently confirms the same exact class-size histogram and the same four pairs. Both programs provide full finite certificates by exhaustive evaluation, not extrapolations from samples or probabilistic hashes.

Finally, a code injective on profiles can take at most one word from each profile fiber, and can attain this upper bound by taking exactly one from each. Since there are \(8188\) fibers, the optimum is \(8188\). Every maximum code must include all \(8184\) singleton words and choose exactly one element from each of four independent doubletons. Thus the exact number of such labeled codebooks is \(2^4=16\). No classification up to coordinate or alphabet symmetry is asserted for those codebooks.

## Verification
Using a C++17 compiler and Python 3, run the following commands after extracting the two source files alongside this document:

```sh
c++ -std=c++17 -O2 gapped_verify_dp.cpp -o verify_dp
./verify_dp
python3 gapped_verify_direct.py
```

Successful runs end respectively with `VERIFY_DP_OK` and `VERIFY_DIRECT_OK`. All equality tests use exact integer-valued signatures, not hash digests. Both programs additionally assert the four exact reversal pairs and all fiber sizes at length \(13\).

## Relationship to prior work
Golm, Nahvi, Gabrys and Milenkovic (2022), Section II and the numerical table at the end of Section III, define the same nonconsecutive-index deck and already report the threshold \(G(3)=13\) and *one example* of a confusable length-thirteen pair. That threshold and example are prior work, **not findings claimed here**. The numerical table is explicitly labeled as displaying example confusable pairs; it does not give the complete fiber histogram, the three additional pairs, a sharp reconstruction-code size, or the classification/count of maximum codebooks. The result here supplies those strictly stronger finite combinatorial data at the published threshold.

Rigo, Stipulanti and Whiteland (2023) reformulate these observations as gapped-binomial equivalence. Their paper develops complexity for factors of special infinite words and gives a binary characterization for gap-one, order-two equivalence. That work does not derive the unrestricted finite length-thirteen gap-one, order-three fiber classification obtained here. The names “one-gap, order-three binomial equivalence” and “two-spaced gapped three-deck” refer to the same observation in this result.

## Limitations
The proof is a bounded complete census for \(n\leq13\), not an infinite theorem. It makes no claim that the already-published value \(G(3)=13\) is new. The numerical computation and exact classification have been checked by two separate methods, but independent external audit has not occurred. An unindexed equivalent finite histogram or subsequent fuller publication could subsume the novelty claim. Degenerate lengths lacking nonempty length-three spaced subsequences must not be confused with the literature's meaningful reconstruction threshold.

## References
1. J. Golm, M. Nahvi, R. Gabrys and O. Milenkovic, *The Gapped k-Deck Problem*, arXiv:2201.12671 (public preprint first submitted 2022-01-29), https://arxiv.org/html/2201.12671v2 .
2. M. Rigo, M. Stipulanti and M. Whiteland, *Gapped Binomial Complexities in Sequences*, IEEE International Symposium on Information Theory (2023), DOI: 10.1109/ISIT54713.2023.10206676, public full text https://orbi.uliege.be/bitstream/2268/302524/1/isit2023.pdf .
