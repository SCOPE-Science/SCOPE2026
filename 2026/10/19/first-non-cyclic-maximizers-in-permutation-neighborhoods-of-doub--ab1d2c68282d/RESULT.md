# First non-cyclic maximizers in permutation-neighborhoods of double-occurrence shuffle words

## Finding

For an integer \(k\ge 1\), let \(\mathcal C_k\) be the set of words of length \(2k\) in which each of \(k\) symbols occurs exactly twice, with symbol names ignored. Every such word has a unique canonical representation obtained by labeling the symbols \(1,2,\ldots,k\) in order of their first appearance. Thus \(|\mathcal C_k|=(2k-1)!!\).

For \(\gamma\in S_k\), let \(d_k(\gamma)\) count canonical words that split into two disjoint, order-preserving subsequences \(U,V\) of length \(k\) with \(U_i=V_{\gamma(i)}\) for all \(1\le i\le k\). Reversing the roles of the subsequences gives the same predicate with \(\gamma^{-1}\), so \(d_k(\gamma)=d_k(\gamma^{-1})\).

**Exact extremal theorem.** For \(k=5\) the maximum of \(d_k\) over \(S_k\) is \(134\), attained exactly at the two inverse permutations with one-line forms \(34521\) and \(54123\). For \(k=6\) the maximum is \(532\), attained exactly at the inverse pair \(345621\) and \(651234\). In contrast, the best cyclic-shift permutations have degrees \(123\) and \(508\), respectively. Consequently, \(k=5\) is the first value among \(2\le k\le6\) for which no cyclic shift maximizes the degree.

The complete finite comparison is:

| \(k\) | \(|\mathcal C_k|\) | \(\max_{\gamma}d_k(\gamma)\) | All maximizing one-line permutations | Best cyclic-shift degree |
|---:|---:|---:|---|---:|
| 2 | 3 | 2 | 12, 21 | 2 |
| 3 | 15 | 9 | 231, 312 | 9 |
| 4 | 105 | 33 | 2341, 4123 | 33 |
| 5 | 945 | 134 | 34521, 54123 | 123 |
| 6 | 10395 | 532 | 345621, 651234 | 508 |

A one-line permutation such as `34521` represents the map \(1\mapsto3\), \(2\mapsto4\), \(3\mapsto5\), \(4\mapsto2\), \(5\mapsto1\). The entries describe **canonical word neighbors**, not the number of interleavings or the number of representations of any individual word.

## Assumptions and scope

Only a finite domain is asserted: \(2\le k\le6\). The objects are unlabeled double-occurrence words with their unique first-appearance canonical labels. Two subsequences must cover every position exactly once, and their order inside each subsequence must respect the original word. A permutation is counted once per word if at least one such partition exists. The cyclic-shift comparison uses \(i\mapsto i+s\pmod{k}\) for \(0\le s<k\), interpreted with labels \(1,\ldots,k\). No claim is made about arbitrary even words with repeated symbols, minimum permutation covers, or any \(k\ge7\).

## Proof

**Lemma 1 (matching encoding).** Every element of \(\mathcal C_k\) corresponds bijectively to a perfect matching of the ordered positions \(\{0,1,\ldots,2k-1\}\): match the two positions carrying each symbol. Given a matching, label its pairs in ascending order of their smaller endpoint. Each pair then receives exactly one canonical symbol. Distinct matchings give distinct canonical words. Recursively pairing the least unmatched position with each other unmatched position enumerates all matchings once. It follows that their number is \((2k-1)!!\).

**Lemma 2 (interleaving encoding).** Fix \(\gamma\in S_k\). In any qualifying split \(U,V\), each symbol occurs equally often in \(U\) and \(V\). Since the entire word has exactly two copies of each symbol, each subsequence contains every symbol exactly once. Relabel the symbols in the order in which they occur in \(U\). Then \(U=(1,2,\ldots,k)\), and the equality \(U_i=V_{\gamma(i)}\) forces \(V_j=\gamma^{-1}(j)\). Conversely, interleaving the two permutations \((1,\ldots,k)\) and \((\gamma^{-1}(1),\ldots,\gamma^{-1}(k))\), keeping each in its given order, produces a qualifying split. Relabeling the resulting word canonically leaves its position matching unchanged. Therefore

\[
d_k(\gamma)=\left|\left\{\operatorname{Pair}(\operatorname{merge}_I(1\cdots k,\gamma^{-1}(1)\cdots\gamma^{-1}(k))): I\in\binom{[2k]}{k}\right\}\right|.
\]

Here \(I\) specifies exactly the positions occupied by the first permutation, and \(\operatorname{Pair}\) returns the sorted list of the \(k\) pairs of positions occupied by identical symbols. The set notation removes multiplicity from different interleavings that produce the same canonical word. This is exactly the algorithm in `enumerate_interleavings.py`.

**Lemma 3 (independent matching-side enumeration).** Conversely, fix a matching of the \(2k\) positions. An admissible split must select exactly one endpoint from every matched pair for the first subsequence. The \(2^k\) endpoint selections therefore exhaust all admissible splits. Reading the two subsequences \(U,V\), the unique permutation satisfying \(U_i=V_{\gamma(i)}\) is \(\gamma(i)=\operatorname{position}_V(U_i)\). Taking the set of these permutations over all endpoint selections gives exactly the neighbors of that matching. Incrementing each of their degree counts once, as implemented in `enumerate_pairings.py`, produces the same \(d_k\) by a logically different enumeration.

**Finite certificate.** The enumerations in Lemmas 2 and 3 use only bounded integer loops and finite sets. For every integer \(k\) from \(2\) to \(6\), `verify.py` computes the full map of all \(k!\) degree values by both methods, checks equality pointwise, compares all maximizers and all cyclic shifts, and verifies the classical identity-permutation degree \(\frac{1}{k+1}\binom{2k}{k}\). For the two main sizes, the entire maps appear as `degree_table_k5.json` and `degree_table_k6.json`; the verifier also checks these exact tables. It reports the maxima and precisely the maximizing permutations listed above. Because the lemmas prove that both finite enumerations are exhaustive, these integer comparisons establish the claimed finite theorem, including sharpness and uniqueness. They make no inference from a truncated search to infinitely many parameters.

For additional compact checksums, the sums of the degree entries are \(10878\) at \(k=5\) and \(255409\) at \(k=6\). The SHA-256 digests of the sorted, compact JSON degree maps generated by the verifier are respectively `1dd5f5b293589b9d4415602ea4f0b92406b4759b0e6da630bca7f760113cf98b` and `2d5d5d556335985345bed6f02da914f853aa5e152ed88d27e29899c260440045`. They are checksums of the computational output, not substitutes for the complete enumeration proof.

## Verification

Using Python 3 without external packages, run `python verify.py` from the directory containing the three scripts and two data tables. It calls the two different enumerators and compares all degree values for \(2\le k\le6\). A successful invocation ends with `ALL_FINITE_THEOREMS_VERIFIED`. The replay covers \(720\) permutations and \(10395\) canonical words at \(k=6\), and all smaller sizes. No random sampling is used in the certificate.

## Relationship to prior work

Grytczuk, Pawlik, and Pleszczyński introduce the permutation-shuffle incidence graph in *Variations on shuffle squares* (arXiv:2308.13882), Section 2.4. They determine the minimum number of permutation vertices needed to cover all canonical words for small sizes; this covering number is different from a single permutation vertex's neighborhood size. The paper's discussion after Proposition 3 explicitly asks for the maximum permutation-vertex degree. It proves that the identity vertex has Catalan-number degree and supplies the full neighborhoods for the three-symbol case, neither of which determines the two new maxima.

The later *More Variations on Shuffle Squares* by the same authors studies avoidability under general shuffle constraints; its main degree bound concerns word vertices in a different graph, not this finite permutation-incidence extremum. He, Huang, Nam, and Thaper study aggregate counts of shuffle and reverse-shuffle squares over a given alphabet; those aggregate counts do not give degree maxima across each prescribed permutation for double-occurrence canonical words. The finite theorem here addresses the previously posed permutation-neighborhood extremum at sizes five and six and exhibits the first failure of cyclic shifts to maximize it.

## Limitations

The result is finite, with no asymptotic formula or classification for \(k\ge7\). The computation is exhaustive only for the explicitly covered sizes and depends on the elementary bijections and executable programs provided. A claim of novelty is subject to independent bibliographic review: equivalent formulations could exist in later or less readily indexed research, especially work on double-occurrence pairings and generalized shuffle squares. The cited 2023 follow-up's relevant introductory and main-theorem sections were accessible, but its full text was not rechecked line by line.

## References

1. J. Grytczuk, B. Pawlik, and M. Pleszczyński, *Variations on shuffle squares*, arXiv:2308.13882, original public version August 26, 2023; Section 2.4, Proposition 3 and subsequent maximum-degree question. https://arxiv.org/abs/2308.13882
2. J. Grytczuk, B. Pawlik, and M. Pleszczyński, *More Variations on Shuffle Squares*, *Symmetry* **15** (2023), 1982. https://doi.org/10.3390/sym15111982
3. X. He, E. Huang, I. Nam, and R. Thaper, *Shuffle Squares and Reverse Shuffle Squares*, arXiv:2109.12455, first publicly available September 2021. https://arxiv.org/abs/2109.12455
