# Complete length-\(23\) binary substring-composition ambiguity census

## Finding

The **complete** binary substring-composition observation of a finite word records, for every nonempty contiguous factor, the number of zeros and ones in that factor, with multiplicity, without retaining the factor's position. At length \(23\) its fibers have **exactly** the following cardinalities:

| Words per observation | Number of observations | Source words |
| ---: | ---: | ---: |
| \(1\) | \(4{,}096\) | \(4{,}096\) |
| \(2\) | \(4{,}191{,}936\) | \(8{,}383{,}872\) |
| \(4\) | \(160\) | \(640\) |

No fiber has any other size. Thus the number of distinct observations is exactly \(4{,}196{,}192\), and the maximum number of words indistinguishable from a single observation is \(4\). These observations support a largest possible zero-error code of exactly \(4{,}196{,}192\) words (one representative from each fiber).

Of the \(160\) four-word fibers, precisely \(152\) are classical two-factor reversible-interleaving families. The remaining **eight** four-word fibers are noninterleaved. The standalone file `quadruple_classes.csv` lists all \(160\) fibers and labels the eight exceptions. Every singleton is a palindrome, while every doubleton is a word together with its reversal.

## Assumptions and scope

The alphabet is \(\{0,1\}\), the word is **linear and of length exactly \(23\)**, and every nonempty contiguous interval participates in the observation. In particular, for a word \(w=w_1\dots w_{23}\), define
\[
H_w(k,j)=\#\{i:1\le i\le24-k,\ \sum_{h=i}^{i+k-1}w_h=j\},\quad 1\le k\le23,\;0\le j\le k.
\]
The complete observation is the triangular integer array \(H_w\). Two words are equivalent if and only if those arrays agree entrywise. Substrings are counted **with multiplicity**; the result does not apply to the set-only version or to fixed read length.

For two strings \(u=u_1\dots u_m\) and \(v=v_1\dots v_k\), their classical interleaving is
\[
u\circ v=u\,v_1\,u\,v_2\cdots v_k\,u.
\]
Its length is \((m+1)(k+1)-1\). A **classical four-member interleaving fiber** is a four-element set consisting of \(u\circ v\), \(u\circ v^R\), \(u^R\circ v\), and \(u^R\circ v^R\), where both factors are nonpalindromic and their length is \(23\). No assertion is made for longer word lengths, other alphabets, or any observation with missing multiplicities.

## Proof

The finite theorem is proved by a complete, independently checkable exhaustion with an exact equivalence test. The accompanying C++17 source `verify.cpp` implements the following exhaustive certificate; the accompanying CSV gives its complete quadruple-class witnesses.

1. **All sources without omission.** Iterate the integers \(0\) through \(2^{23}-1\) and interpret each as a \(23\)-bit binary word. This is a bijection with the input domain.
2. **Provably complete bucketing.** Fix deterministic \(64\)-bit integers \(s_{k,j}\) using the fully specified SplitMix64 operations in `verify.cpp`. Calculate for every word
\[
K(w)=\sum_{k=1}^{23}\sum_{j=0}^k H_w(k,j)s_{k,j}\pmod{2^{64}}.
\]
If \(H_w=H_z\), then \(K(w)=K(z)\) **with certainty**. Consequently no equal-observation words can fall into different key buckets. Distinct observations may share a key, but the next step detects and rejects such collisions.
3. **Exact collision elimination.** Sort all \(2^{23}\) `(key,word)` records. For every key bucket with at least two words, recompute the complete \(H\) array for *each* member by prefix sums (a method independent of the bit-window popcount used for the key). Abort unless all arrays in the same bucket match exactly. A singleton bucket trivially has one observation. Thus the final buckets are **exactly** the equivalence classes; this argument does not use a probabilistic hash-collision assumption.
4. **Exact class histogram.** The exhaustive run returns bucket counts \(4{,}096\), \(4{,}191{,}936\), and \(160\) for sizes one, two, and four, and no buckets of any other size. The resulting source-word identity
\[
4096+2(4191936)+4(160)=8388608
\]
provides an additional completeness consistency check. Reversal invariance and the \(2^{12}=4096\) palindromes show that all singleton buckets must be palindromes and all two-member buckets must be reversal pairs.
5. **Structural classification of quadruples.** For every pair of positive factor lengths \(m,k\ge2\) satisfying \((m+1)(k+1)=24\), enumerate every nonpalindromic factor \(u\in\{0,1\}^m\) and \(v\in\{0,1\}^k\). Form the four interleavings, order their encoded \(23\)-bit words, and deduplicate resulting four-element sets. The resulting **\(152\)** distinct sets are each present among the exact \(160\) size-four fibers; conversely the explicit comparison identifies exactly eight remaining fibers. The program checks a four-element condition for every generated set, checks all \(160\) serialized CSV rows against the actual fibers, and confirms exactly eight labels `noninterleaved`. No representation by the indicated classical construction is omitted, because the factor-length equation and all permissible binary factors are exhaustively enumerated.

The arithmetic and comparisons in steps 1–5 use fixed-width integers within their capacities, and the run checks for the complete expected partition. The result is therefore a **finite exhaustive proof for precisely length \(23\)**, rather than an extrapolation from smaller instances. The full source and complete quadruple table are inseparable reproducibility artifacts for these numerical equalities.

## Verification

Compile with an ordinary C++17 compiler:

```sh
g++ -O3 -std=c++17 verify.cpp -o verify
./verify
```

Execute from the directory containing both `verify.cpp` and `quadruple_classes.csv`. A successful run prints:

```text
CHECK_OK n=23 words=8388608 singleton_classes=4096 double_classes=4191936 quadruple_classes=160 interleaved_classes=152 exceptional_classes=8 distinct_profiles=4196192 max_ambiguity=4
```

The verifier actually processes all \(8{,}388{,}608\) source words and verifies all larger-key-bucket exact profiles, independently checks all possible classical interleavings, and checks the full CSV. No result relies on trusting precomputed rows or on the presumed absence of a \(64\)-bit hash collision. Compilation, arithmetic, and execution from the extracted artifact source were completed successfully.

## Relationship to prior work

Acharya, Das, Milenkovic, Orlitsky and Pan introduced this complete composition-multiset equivalence and its polynomial representation. Their 2010 conference paper identifies length \(23\) as the first source length at which an ambiguity **outside classical interleaving** appears, and their extended 2014 preprint (subsequently published in SIAM Journal on Discrete Mathematics) gives an example and proves general bounds on the largest ambiguity class. **Those foundational noninterleaved examples and the existence of four-member classes are prior results, not claimed as new here.**

The contribution here is instead the **complete finite-length \(23\) class-size census**, its exact number of distinguishable observations and optimal zero-error codewords, and the full four-member-class division into \(152\) classical and **eight** exceptional classes. The cited original articles do not report these precise totals. Other nearby reconstruction results involving short-read multispectra or incomplete substring compositions concern different observation maps and do not imply this classification.

## Limitations

This is an exact statement at one natural **first-exceptional** blocklength, not a general formula for arbitrary length. It establishes neither a faster reconstruction algorithm nor a new universal ambiguity bound. The exhaustive certificate is executable C++17, not an independently audited formal proof. Literature searches and direct inspection of closely relevant primary papers did not identify the entire census; priority uncertainty remains for less-indexed works or independently unpublished calculations. The length-\(23\) noninterleaved phenomenon itself was previously known.

## References

1. J. Acharya, H. Das, O. Milenkovic, A. Orlitsky, and S. Pan, *On Reconstructing a String from its Substring Compositions*, IEEE International Symposium on Information Theory (2010), public author-hosted full text: https://people.ece.cornell.edu/acharya/papers/rcn_str_sbs.pdf .
2. J. Acharya, H. Das, O. Milenkovic, A. Orlitsky, and S. Pan, *String Reconstruction from Substring Compositions*, arXiv:1403.2439, first version dated March 10, 2014; subsequently *SIAM Journal on Discrete Mathematics*, DOI:10.1137/140962486. https://arxiv.org/abs/1403.2439 .
