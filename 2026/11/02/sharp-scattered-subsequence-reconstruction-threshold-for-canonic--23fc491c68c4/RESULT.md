# Sharp scattered-subsequence reconstruction threshold for canonical binary order-five de Bruijn cycles

## Finding

Write \(\mathcal B_5\) for the binary de Bruijn necklaces of order five, and let \(w(W)\) denote the uniquely defined length-\(32\) rotation of \(W\) that begins with \(00000\). Define \(D_k(w)\) to be the **set**, without multiplicities, of all binary strings of length \(k\) occurring as scattered subsequences of \(w\). Put
\[
 c_k=\left|\{D_k(w(W)):W\in\mathcal B_5\}\right|.
\]
The complete initial separation profile relevant to reconstruction is:

| \(k\) | \(c_k\) |
|---:|---:|
| 8 | 1 |
| 9 | 1 |
| 10 | 21 |
| 11 | 629 |
| 12 | 1,520 |
| 13 | 2,016 |
| 14 | 2,048 |

At \(k=13\) there are exactly \(32\) doubleton classes and \(1{,}984\) singleton classes, with no other class sizes. Every doubleton consists of two words differing by interchanging two letters separated by exactly one other position. The length-\(14\) deck separates all \(2{,}048\) necklaces, and the **sharp reconstruction threshold is \(14\)**.

For example, the distinct canonical words `00000101011000110100111011111001` and `00000101011000110100111110111001` have identical \(13\)-decks; the length-\(14\) string `10001000011110` is a subsequence of the first but not the second. The complete list of \(32\) pairs is in `ambiguous_pairs.csv`.

## Assumptions and scope

All words are over the ordered alphabet \(\{0,1\}\). A binary de Bruijn cycle of order five is a cyclic binary word of length \(32\) containing each possible binary length-five factor exactly once, with positions interpreted cyclically when testing this property. Each such cycle contains \(00000\) once, so its specified root \(w(W)\) is unambiguous. After rooting, scattered subsequences use the **linear** order of all \(32\) positions without wrapping. Distinct subsequences are sets, not multisets; no deletion multiplicities or alternative roots are included.

## Proof

**1. Exhaustive cycle parametrization.** Identify the \(32\) binary states with integers \(x\in\{0,\ldots,31\}\) using their five-bit representations. A successor state on a de Bruijn cycle is obtained by shifting the state to the left by one bit and appending an outgoing bit. For this map to be bijective, the two states \(s\) and \(16+s\) for every four-bit suffix \(s\in\{0,\ldots,15\}\) must append complementary bits. Conversely, any choice of \(16\) bits \(m_s\) defines a permutation
\[
 T_m(x)=2(x\bmod16)+\left(m_{x\bmod16}\oplus\left\lfloor\frac{x}{16}\right\rfloor\right),
\]
where \(\oplus\) is binary exclusive-or. Its outputs are pairwise different because inputs sharing their four-bit suffix append opposite bits and different suffixes have different shifted prefixes. This permutation corresponds to a de Bruijn cycle precisely when it is one cycle of length \(32\). Every binary order-five de Bruijn necklace arises from exactly one such table. The first five output symbols of the state orbit beginning at state zero are zero, so recording its leading bit at every step produces the canonical root.

The supplied checker tests each of the \(2^{16}=65{,}536\) feedback tables, requiring return to state zero after \(32\) steps with no earlier return. Exactly \(2{,}048\) pass, yielding \(2{,}048\) distinct canonical roots. Independently, all \(2^{16}\) local two-edge orderings are passed to Hierholzer's Euler-tour construction on the \(16\)-vertex, \(32\)-edge binary order-four overlap graph. Extracting and normalizing the resulting cycles produces exactly the same set of \(2{,}048\) roots. These two constructions have different traversal logic.

**2. Exact subsequence-deck recurrence.** For every linear prefix \(u\), let \(S_j(u)\) be its set of length-\(j\) scattered subsequences. With \(S_0(u)=\{\varepsilon\}\) and \(S_j(\varepsilon)=\varnothing\) for \(j>0\), appending a symbol \(b\) gives
\[
 S_j(ub)=S_j(u)\cup\{vb:v\in S_{j-1}(u)\}.
\]
Indeed, a subsequence either omits the final symbol or uses it as its last symbol. This proves the dynamic update computed by the checker. The second implementation independently tests each length-\(j\) binary candidate by successively taking its earliest available matching position, which succeeds if and only if the candidate is a subsequence. Both implementations agree on every canonical word for each \(8\le j\le14\).

**3. Finite classification and sharpness.** Grouping the exact bitsets from step 2 gives the displayed counts \(c_8,\ldots,c_{14}\); in particular \(c_{13}=2016\) with exactly \(32\) doubletons, while \(c_{14}=2048\) with all singletons. Testing the exclusive-or of the two \(32\)-bit words in every doubleton gives exactly \(5\cdot2^t\) for some integer \(0\le t\le29\). Thus they differ at precisely two positions separated by one position. Every de Bruijn word has \(16\) ones, so the unequal letters are exchanged, not both flipped in the same direction.

For a length-\(32\) word and \(j<k\le32\), any length-\(j\) subsequence can be extended to a length-\(k\) subsequence by selecting additional positions. Consequently \(D_j(w)\) is the set of length-\(j\) subsequences of members of \(D_k(w)\). Equality of two \(k\)-decks therefore implies equality of every shorter deck. The explicit \(13\)-deck collisions rule out all \(k\le13\), and the complete \(14\)-deck separation proves the claimed sharp threshold.

## Verification

Compile with a standard C++17 compiler:

```sh
g++ -std=c++17 -O3 verify_debruijn_decks.cpp -o verify_debruijn_decks
./verify_debruijn_decks
```

The checker includes the feedback-table and Euler-tour cycle constructions, the subsequence dynamic program and earliest-match definition checker, full bitset equality grouping, and all numerical assertions. It prints `VERIFY_OK` only after all comparisons succeed. `spectrum_table.csv` records the exact class counts; `ambiguous_pairs.csv` records every doubleton in eight-digit hexadecimal encoding. A separate direct candidate-by-candidate Python control was also applied to one representative pair and gave identical \(13\)-decks and distinct \(14\)-decks.

## Relationship to prior work

Dress and Erdős (2005) develop reconstruction from distinct subsequences and credit Schützenberger and Simon's general result: all length-\(N\) words are determined by their length-\(k\) decks for \(2k>N\). At \(N=32\), this gives the general sufficient level \(k=17\), not the sharper restricted-family threshold \(14\). Karandikar, Kufleitner and Schnoebelen (2013) study the index of Simon's congruence over all words and do not classify its restriction to de Bruijn cycles. Barker and collaborators (2020) give a linear-time comparison algorithm for general full subsequence spectra, but their theorem does not yield the above de Bruijn-family class-count table. The earlier constructions and algorithms are fully credited; the claim here is the exact restricted finite separation profile and sharp threshold.

## Limitations

This is a finite exhaustive result for **binary order-five** cycles canonically rooted at the unique occurrence of \(00000\). It makes no claim about unrooted circular-deck observations, arbitrary root choices, other orders or alphabets, or multisets of embeddings. The proof is checkable by the included C++17 program but has not undergone independent mathematical audit. Searches of accessible published literature cannot exclude an obscure historical equivalent table.

## References

1. A. W. M. Dress and P. L. Erdős, *Reconstructing Words from Subwords in Linear Time*, Annals of Combinatorics 8 (2004), 457–462. DOI: https://doi.org/10.1007/s00026-004-0232-4.
2. P. Karandikar, M. Kufleitner, and Ph. Schnoebelen, *On the index of Simon's congruence for piecewise testability*, first arXiv version 2013-10-03. https://arxiv.org/abs/1310.1278.
3. L. Barker, P. Fleischmann, K. Harwardt, F. Manea, and D. Nowotka, *Scattered Factor-Universality of Words*, first arXiv version 2020-03-10. https://arxiv.org/abs/2003.04629.
