# Fifty-seven symmetry classes of optimal six-symbol Ulam codes

## Finding
Let \(S_6\) be the set of permutations of \(\{0,1,2,3,4,5\}\). For distinct \(p,q\in S_6\), set \(d_U(p,q)=6-\operatorname{LCS}(p,q)\), where \(\operatorname{LCS}\) is the length of their longest common subsequence. A code is a subset of \(S_6\) whose distinct words have Ulam distance at least four.

The maximum cardinality is four, as previously established. The complete equality census is:

\[
\boxed{53\,640\text{ labeled four-word optimal codes, in exactly }57\text{ classes}.}
\]

The equivalence group here consists precisely of simultaneous arbitrary relabeling of the six symbols and optional reversal of the position order in every codeword. Of the 57 classes, seven have labeled orbit size \(360\), twenty-nine have orbit size \(720\), and twenty-one have orbit size \(1440\). Every optimum is equidistant: every two distinct codewords have Ulam distance exactly four.

The accompanying `CLASS_REPRESENTATIVES.tsv` gives one lexicographically canonical representative of each class and its labeled orbit size.

## Assumptions and scope
A permutation is written as a six-character string over the digits `012345`, each appearing once; the coordinate order is part of the codeword. Codes are unordered sets of distinct permutations. The 720 permutations on a fixed labeled six-symbol alphabet are distinct words. Two codes are equivalent only under the action described above; no arbitrary permutation of coordinate positions is allowed. The result concerns blocklength six, minimum Ulam distance four, and unrestricted (not necessarily subgroup) codebooks. It does not assert an all-length formula or a classification under other metrics.

## Proof
**Ordered-triple reduction.** For each \(p\in S_6\), let \(T(p)\) be the set of ordered triples obtained by choosing three positions in increasing order from \(p\). There are exactly \(\binom63=20\) such triples for each permutation, taken from \(6\cdot5\cdot4=120\) possible ordered triples. Two permutations have a common length-three subsequence if and only if \(T(p)\cap T(q)\ne\varnothing\). Consequently,

\[
 d_U(p,q)\ge4\quad\Longleftrightarrow\quad T(p)\cap T(q)=\varnothing.
\]

**Normalization and exhaustive finite certificate.** Simultaneous symbol relabeling can map any designated codeword uniquely to the identity word `012345`. After fixing that word, enumerate all \(720\) permutations and retain the \(132\) words \(p\) for which \(T(p)\cap T(012345)=\varnothing\). (Equivalently, these are the permutations with longest increasing subsequence at most two; their Catalan count is \(132\).) Among these \(132\) candidates, enumerate every strictly increasing index triple \((a,b,c)\) for which all three pairs of triple masks are disjoint. The exact count is \(298\). For each of these \(298\) four-word codes, a further exhaustive pass through all \(132\) candidates finds no word disjoint from all four triple masks. Thus no five-word code exists. One of the enumerated four-word codes is `012345`, `105432`, `325041`, `452130`, proving attainability of size four.

This is a finite, exhaustive proof: the loops cover the entire six-symbol permutation set, not a random sample. The complete algorithms are supplied in `enumerate_lcs.cpp` (direct longest-common-subsequence criterion) and `enumerate_triples.py` (120-bit directed-triple masks). `verify_labeled.py` explicitly expands every normalized four-word code under all \(720\) symbol relabelings and checks the labeled count.

**Labeled census.** A labeled four-word code has four choices of distinguished word; for each choice, exactly one of the \(720\) symbol relabelings maps it to `012345`. Double counting these incidences gives

\[
 4N=720\cdot298,\qquad N=53\,640.
\]

**Symmetry classification.** Given an unordered code, optionally reverse the six positions in every word, designate one of its four words, and apply the unique symbol relabeling carrying that word to `012345`. Sort the four resulting six-character strings, join them in order, and take the lexicographically least outcome over the eight choices. This canonical string is unchanged under the stated equivalence group. Conversely, equality of two canonical strings explicitly supplies the reversal and relabeling connecting the codes, so the canonical strings classify orbits without ambiguity.

The exhaustive enumeration yields \(57\) different canonical strings. Among the \(298\) identity-containing codes, a canonical string occurs respectively \(2\), \(4\), or \(8\) times in \(7\), \(29\), or \(21\) classes. The incidence double count above applies separately to each class: an identity-containing multiplicity \(m\) corresponds to a labeled orbit size \(720m/4=180m\). Hence the three orbit sizes are \(360\), \(720\), and \(1440\); their weighted total is \(53\,640\).

**Equidistance.** If two permutations of six symbols have longest common subsequence of length one, one must be the position-reversal of the other. Any third permutation with longest common subsequence at most two relative to each would have both longest increasing and longest decreasing subsequence of length at most two relative to the first ordering. This contradicts the Erdős–Szekeres theorem already at length five. Thus every code with at least three words and minimum Ulam distance at least four has no pair at distance five. Each optimum therefore has every pair at distance exactly four.

## Verification
From a directory containing the bundled files, run:

```
g++ -O3 -std=c++17 enumerate_lcs.cpp -o enumerate_lcs
./enumerate_lcs > census_lcs.txt
python3 enumerate_triples.py > census_triples.txt
python3 verify_labeled.py
```

The compiled program checks disjoint longest-common-subsequence relations, absence of a fifth compatible word, and the entire canonical orbit histogram. The triple-mask implementation uses a different primitive (ordered-subsequence incidence masks) and checks the same census and the absence of fifth words. The labeled-expansion implementation materializes every distinct four-word set induced by all alphabet relabelings. The reproducible values are \(720\) permutations, \(132\) identity-compatible words, \(298\) identity-containing optimum codes, \(53\,640\) labeled optimum codes, and \(57\) equivalence classes with multiplicities \(7,29,21\). A complete canonical representative list is provided as a separate TSV.

## Relationship to prior work
Göloğlu, Lember, Riet and Skachek established \(A_U(6,4)=4\) in their 2015 computational table; that value is **not** a new claim here. Their tabulated maximum does not determine the number of attaining codebooks or their symmetry types. The directed-design work of Mathon and van Trung examines related perfect packings, notably a classification of directed four-subsequence designs, but the inspected abstract does not settle the present partial directed-triple census; its full text was unavailable for complete comparison. Gentle and Wanless study perfect sequence covering arrays, where each ordered triple must be covered at equal multiplicity; in particular, their \(g(6,3)=2\) pertains to exact coverings, not the pairwise-disjoint partial packings classified here. The present count is a classification of optimal nonperfect distance-four permutation codebooks, not a new upper bound.

## Limitations
The classification is finite and relies on exhaustive computation, with complete source code provided; it does not generalize to larger lengths without additional proof. The comparison with the full 1999 Mathon–van Trung paper remains unresolved because only its bibliographic description and abstract were available. The bibliography and searched public records did not reveal a prior equivalent census, but this is not proof of priority, and an unindexed earlier enumeration remains possible. No independent audit or formal proof assistant validation has been performed.

## References
1. F. Göloğlu, J. Lember, A.-E. Riet, V. Skachek, *New Bounds for Permutation Codes in Ulam Metric*, arXiv:1504.05100v1, 20 April 2015. https://arxiv.org/html/1504.05100v1
2. R. Mathon and T. van Trung, *Directed t-packings and directed t-Steiner systems*, Designs, Codes and Cryptography **18** (1999), 187–198. https://doi.org/10.1023/A:1008353723204
3. A. E. Gentle and I. M. Wanless, *On Perfect Sequence Covering Arrays*, Annals of Combinatorics **27** (2023), 539–563 (online 2022). https://doi.org/10.1007/s00026-022-00610-6
