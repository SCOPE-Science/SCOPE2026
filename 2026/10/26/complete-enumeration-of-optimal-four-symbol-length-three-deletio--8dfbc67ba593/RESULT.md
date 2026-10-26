# Complete enumeration of optimal four-symbol length-three deletion covers

## Finding

On the fixed four-symbol alphabet \(\Sigma=\{0,1,2,3\}\), a **one-deletion covering code** is a subset \(C\subseteq\Sigma^3\) such that every received two-symbol word is obtained by deleting one position from some word of \(C\). The minimum cardinality of such a code is \(6\), a value also attainable by already-known perfect deletion-correcting constructions.

The complete enumeration of **all** size-\(6\) covering codebooks gives exactly **644 labeled codebooks**. Of these, exactly **120** have pairwise-disjoint deletion shadows (and hence are perfect single-deletion-correcting codes); the other **524** have overlapping shadows despite using the minimum possible number of codewords. Under global permutations of the four symbols and simultaneous reversal of all words, the 644 codebooks form **21 equivalence classes**. Their orbit sizes are: one orbit of size \(8\), three of size \(12\), nine of size \(24\), and eight of size \(48\).

Let the **excess incidence** be \(e(C)=\sum_{u\in\Sigma^2}(\#\{w\in C:u\in D(w)\}-1)\), where \(D(w)\) denotes the set of distinct one-deletion descendants. The complete size-profile refinement is:

| Excess \(e(C)\) | Deletion-shadow cardinalities of the six words | Codebooks | Equivalence classes |
|---|---|---:|---:|
| \(0\) | one of size \(1\), five of size \(3\) | 48 | 3 |
| \(0\) | two of size \(2\), four of size \(3\) | 72 | 2 |
| \(1\) | one of size \(2\), five of size \(3\) | 336 | 8 |
| \(2\) | six of size \(3\) | 188 | 8 |

No other profile occurs among minimum-size covers. Here *labeled* means the symbols and the word positions are fixed; the six-word codebook is an unordered set with no repeated words. The equivalence group has size \(48\).

## Assumptions and scope

There are exactly \(64\) possible length-three codewords, and the received universe \(U=\Sigma^2\) contains \(16\) ordered pairs. For each \(w=(a,b,c)\), its distinct deletion shadow is \(D(w)=\{(a,b),(a,c),(b,c)\}\). A cover satisfies \(\bigcup_{w\in C}D(w)=U\). All incidence counts ignore multiplicities resulting from distinct deletion positions within the same word.

Equivalence permits a single alphabet relabeling applied consistently in all three positions, followed optionally by reversing every codeword. It does not permit arbitrary independent position permutations or coordinate-dependent relabelings. A code is *perfect deletion-correcting* only when the shadows partition \(U\).

## Proof

**Minimum size.** Each word has at most three distinct one-deletion descendants. Hence five words cover at most 15 received pairs, fewer than 16. The six words \(000,012,131,210,232,303\) form a cover: their shadows are respectively \(\{00\}\), \(\{01,02,12\}\), \(\{13,11,31\}\), \(\{21,20,10\}\), \(\{23,22,32\}\), and \(\{30,33,03\}\), which partition all 16 ordered pairs.

**Exhaustive cardinality certificate.** Encode word \((a,b,c)\) as integer \(16a+4b+c\), and pair \((x,y)\) as bit index \(4x+y\). Define its exact 16-bit deletion mask \(M(w)=2^{4a+b}\mathbin{\vert}2^{4a+c}\mathbin{\vert}2^{4b+c}\), where \(\vert\) denotes bitwise union. The accompanying `verify_cover.py` implements the following finite dynamic program, with the masking operation specified exactly by this definition:

\[P_{0}(0)=1;\qquad P_0(m)=0\quad(m\ne0).\]

Process the 64 words one at a time. With \(P_k(m)\) denoting the count of distinct \(k\)-element subsets of processed words whose mask union is \(m\), update

\[P_k(m\mathbin{\vert}M(w))\;\mathrel{+}=\;P_{k-1}(m),\]

with cardinalities processed in decreasing order to avoid repeated selection of a word. This is a complete induction on the processed set of words: every subset either excludes or includes the new word, and the two cases are disjoint. The final exact integer coefficients are

\[\sum_mP_6(m)=\binom{64}{6}=74{,}974{,}368,\qquad P_6(2^{16}-1)=644.\]

**Second enumeration and classification.** A separate nested-loop enumerator visits every increasing sextuple of word indices satisfying the necessary remaining-capacity condition. With \(k\) words selected, each of the \(6-k\) unselected words can cover no more than three additional pairs; thus the current mask must have size at least \(16-3(6-k)\). This justifies *all* branch pruning, at depths three, four, and five. The enumerator produces exactly 644 distinct codebooks and directly checks every pair's incidence multiplicity. The 644 split as 120 disjoint-shadow covers and 524 with at least one overlap, with the four excess-incidence and shadow-size profiles shown above.

For every enumerated codebook, the same program applies all 24 permutations of \(\Sigma\) and both choices of global reversal, taking canonical sorted sextuples. Each transformation bijects the family of covering codebooks. The images give a full orbit and are removed from the unclassified set. Therefore no equivalence class is omitted or double-counted. This yields 21 orbits with sizes \(8,12,24,48\) at multiplicities \(1,3,9,8\), respectively. Their sizes sum to 644. The complete 21 canonical representatives are included in the standalone verifier's output.

These are finite exact integer computations with complete domains and auditable source code; they are not extrapolations from partial-length experiments.

## Verification

Run `python verify_cover.py` in the same directory as this document. Python 3.10 or later and the standard library suffice. It performs two independently structured counting procedures (dynamic programming and pruned increasing-sextuple enumeration), verifies the exact orbit partition and the incidence-profile counts, and prints `VERIFY_OK`. The reference output is provided in `verify_output.txt`. The DP checks the identity for the full \(\binom{64}{6}\) search domain, while the direct enumerator's pruning is justified above.

## Relationship to prior work

Xie, Sun and Ge (arXiv:2606.15379v1, June 13, 2026) study insertion/deletion covering codes and the sphere-covering bound and large-alphabet constructions. The present exact labeled-codebook and symmetry-class census is not supplied by their results.

Chee, Ge and Ling (arXiv:1008.1343v1, August 7, 2010) already determine the **possible cardinalities** of perfect length-three one-deletion-correcting codes over all alphabets, and prove existence of perfect size-six quaternary examples. Thus the existence of an optimal six-word cover, and the minimum size, are **not** claimed to be new. What is enumerated here is the population of *every* size-six covering code, including those that are not error correcting, and the detailed equivalence/overlap classifications. A theorem about which cardinalities are achievable does not determine the number of labeled covers with any given cardinality, nor distinguish overlapping optimum covers.

## Limitations

The census concerns exactly four symbols, transmitted length three, and one deletion. No broader-alphabet enumeration or asymptotic improvement follows. Reproducing the finite enumeration is required for the numerical theorem, and the classification is under only the specified symmetry group. Equivalence under a more generous notion of coding is not treated. An equivalent directed-design census in unindexed or older literature remains a residual originality possibility; a negative search cannot establish uniqueness of presentation. No independent external audit has been conducted.

## References

1. C. Xie, Y. Sun, and G. Ge, *New bounds for covering codes under insertions or deletions*, arXiv:2606.15379v1 (first public June 13, 2026), https://arxiv.org/html/2606.15379v1. Especially Sections I and V.
2. Y. M. Chee, G. Ge, and A. C. H. Ling, *Spectrum of Sizes for Perfect Deletion-Correcting Codes*, SIAM Journal on Discrete Mathematics 24 (2010), 33–55, arXiv:1008.1343v1 (first public August 7, 2010), https://arxiv.org/pdf/1008.1343. Especially Theorem 6.4 and the small-alphabet examples.
