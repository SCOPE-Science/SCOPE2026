# Alphabet rigidity at the first one-gap three-deck collision

## Finding

Let \(\Sigma\) be an arbitrary labeled alphabet of \(q\geq 2\) symbols. Define the **one-gap three-deck** of a length-\(n\) word to record, for each word \(u\in\Sigma^\ell\), \(1\leq\ell\leq3\), the number of increasing index tuples \(1\leq i_1<\cdots<i_\ell\leq n\) satisfying \(i_{j+1}-i_j\geq2\) and spelling \(u\).

At length \(n=13\), the equivalence classes of words with identical decks consist of exactly \(4\binom q2\) classes of size two and \(q^{13}-8\binom q2\) singleton classes. There are no larger classes. Every collision uses jointly exactly two distinct alphabet symbols and, after relabeling these as `0` and `1`, belongs to one of the four unordered pairs

1. `0001010000100` / `0010000101000`;
2. `0101111010110` / `0110101111010`;
3. `1001010000101` / `1010000101001`;
4. `1101111010111` / `1110101111011`.

Each unordered alphabet-symbol pair supports exactly four collisions, independently of all other symbol pairs. Therefore the largest code of mutually distinguishable length-13 words has size

\[
q^{13}-4\binom q2,
\]

and the number of distinct maximum labeled codebooks is

\[
2^{4\binom q2}.
\]

For completeness, the deck is injective at every length \(3\leq n\leq12\) for every finite alphabet \(q\geq2\). The length-two observation is degenerate and is not part of that injectivity assertion.

## Assumptions and scope

All words are linear, of a fixed common length, over a finite alphabet with distinguishable symbols. The observation includes every gapped subsequence multiplicity for lengths one, two, and three, not merely distinct subsequences and not ordinary contiguous factors. A gap of one *unselected* position is required between consecutive selected positions; equivalently, consecutive selected indices differ by at least two. Codebooks are labeled subsets of \(\Sigma^{13}\); no quotient by symbol permutation or reversal is taken.

## Proof

**Exact finite lemma (the only computational premise).** At length thirteen, direct exhaustion of all \(2^{13}=8192\) binary words yields four collision classes of size two, exactly the four displayed pairs, and no others. Direct exhaustion of all \(3^{13}=1594323\) ternary words yields twelve collision classes of size two, namely the three relabelings of those four binary pairs by the three unordered pairs of ternary symbols; all other ternary classes are singletons. Exhaustion of binary words of each length from three through twelve finds no collisions. The executable complete census `gapped3_qary_cert.cpp` verifies every clause of this lemma, without assumptions about random sampling. Its signature generator counts all length-one positions, all length-two index pairs at separation at least two, and all length-three index triples whose two consecutive separations are at least two. It uses exact nonnegative integer multiplicities as dictionary keys; distinct signatures cannot be combined by hash collisions because keys are compared for equality. The ternary census checks the exact complete twelve-pair list, not just the number of collisions.

**Alphabet aggregation lemma.** For any mapping of alphabets \(f:\Sigma\to\Delta\), not necessarily injective, and any word \(w\), let \(f(w)\) be its letterwise image. For each pattern \(v\in\Delta^\ell\) with \(1\leq\ell\leq3\), the gapped occurrence count of \(v\) in \(f(w)\) equals the sum of gapped occurrence counts of patterns \(u\in\Sigma^\ell\) with \(f(u)=v\). This follows by partitioning all admissible index tuples by their original spelled pattern. Thus equal source decks always induce equal image decks.

**No genuinely three-letter collision.** Suppose distinct length-thirteen words \(x,y\) over \(\Sigma\) have equal decks. Choose an index where \(x\) and \(y\) differ, with symbols \(a\neq b\). If the union of letters appearing in \(x\) and \(y\) includes a third symbol \(c\), define an alphabet map to \(\{0,1,2\}\) by \(a\mapsto0\), \(b\mapsto1\), \(c\mapsto2\), sending all remaining symbols arbitrarily to these three. The mapped words differ at the selected index and their combined alphabet support contains all three ternary letters. By the aggregation lemma they have equal ternary decks, contradicting the exact ternary lemma: its only non-singleton classes are the two-symbol relabelings of the four binary pairs. Hence the combined support of any collision has exactly two symbols.

Restrict now to these two symbols. Choosing their identification with binary `0` and `1` turns the collision into one of the four binary pairs of the finite lemma. Conversely, injectively relabeling either binary pair with any two distinct alphabet symbols preserves the entire deck. Since the four binary pairs are closed under complement in pairs and their eight words are mutually distinct, each unordered two-symbol alphabet admits precisely four unordered collision pairs. Distinct alphabet-symbol supports cannot share a word, because each word in the listed pairs contains both symbols. Hence the collision graph is a matching with \(4\binom q2\) edges and all other vertices isolated.

A distinguishable codebook can contain at most one endpoint of each matching edge and can include every isolated vertex, so the maximum size is \(q^{13}-4\binom q2\). Every maximum chooses exactly one endpoint independently on every edge, giving \(2^{4\binom q2}\) maximum labeled codebooks.

For \(3\leq n\leq12\), if any distinct \(q\)-ary words had equal decks, mapping two distinct symbols appearing at a disagreement position to binary `0` and `1` (mapping other letters arbitrarily) would give distinct binary words with equal decks by the aggregation lemma. This contradicts the exact binary lower-length census. This finishes the proof.

## Verification

Compile and run the accompanying complete census using a C++17 compiler:

```
g++ -std=c++17 -O2 gapped3_qary_cert.cpp -o gapped3_qary_cert
./gapped3_qary_cert
```

Successful output ends with `PASS_BINARY_3_TO_12_INJECTIVE_BINARY_13_FOUR_TERNARY_13_TWELVE_TWO_LETTER_PAIRS`. The complete run enumerates the \(1,594,323\) ternary length-thirteen words and verifies that all of the \(1,594,311\) signatures and the twelve collision pairs are exactly as stated, in addition to the binary lengths three through thirteen.

An independent occurrence counter using explicit index combinations, as compared with a dynamic-programming occurrence counter, is provided in `independent_deck_check.py`. Run `python3 independent_deck_check.py`; the test ends with `INDEPENDENT_DIRECT_AND_DP_PASSED 516`. The second program cross-checks both descriptions of each displayed collision for every binary or ternary symbol-pair embedding and compares direct versus dynamic-programming counts for 500 additional pseudorandom instances. This second test is supplementary; the exhaustive finite premise rests on the complete census.

## Relationship to prior work

Golm, Nahvi, Gabrys, and Milenkovic introduced gapped \(k\)-deck reconstruction and reported the binary first collision at length \(13\) for \(k=3\); that binary threshold is not new here. Earlier direct binary classification gives the same four two-element classes, and is likewise not a new claim. The contribution here is the *all-alphabet rigidity assertion*, supported by complete ternary exhaustion and the alphabet-aggregation reduction, together with the resulting exact \(q\)-ary reconstruction code size and maximum-codebook count for every alphabet size.

Rigo, Stipulanti, and Whiteland develop \((g,k)\)-binomial equivalence and sequence complexity functions; their definitions coincide with the present deck model for \(g=1,k=3\), but their inspected finite-word definitions and sequence results do not supply the specific length-thirteen arbitrary-alphabet class decomposition. Nearby reconstruction-code results for deletion channels and contiguous pair-multispectra concern different observations and cannot imply this equivalence-class count without additional arguments.

## Limitations

The arbitrary-alphabet conclusion is proved from an exhaustive, finite ternary computation and a mathematical reduction; no compact purely symbolic classification of all ternary words is provided. The result concerns this particular gap constraint, three-deck, and source length thirteen; it does not characterize larger collision lengths or higher-order decks. A finite computation is a rigorous exhaustive premise only because every ternary word and every relevant factor multiplicity is covered by the accompanying executable procedure. Published or indexed work unavailable to the present literature comparison could conceivably contain equivalent results. No independent external audit has been performed.

## References

1. R. Golm, M. Nahvi, R. Gabrys, and O. Milenkovic, *The Gapped \(k\)-Deck Problem*, arXiv:2201.12671, first public version 2022-01-29; 2022 IEEE International Symposium on Information Theory, pp. 49–54. https://arxiv.org/abs/2201.12671
2. M. Rigo, M. Stipulanti, and M. A. Whiteland, *Gapped Binomial Complexities in Sequences*, IEEE International Symposium on Information Theory 2023, pp. 1294–1299. https://orbi.uliege.be/handle/2268/302524
