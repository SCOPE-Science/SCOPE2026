# Complete equality patterns for short nonbinary two-deletion reconstruction

## Finding

Let \(q\ge3\) and let \(\Sigma_q\) be a labeled alphabet of size \(q\). For a length-\(n\) word \(x\), denote by \(\mathcal D_t(x)\) the **set of distinct** subsequences obtained by deleting exactly \(t\) coordinates. Consider unordered pairs \(\{x,y\}\) of length-\(n\) words for which \(\mathcal D_1(x)\cap\mathcal D_1(y)=\varnothing\); these are admissible pairs with one-deletion separation. Define the two-deletion ambiguity \(J(x,y)=|\mathcal D_2(x)\cap\mathcal D_2(y)|\).

**Theorem (complete equality-case census).** For every integer \(q\ge3\) and every \(n\in\{3,4,5,6\}\), the maximum \(M_n(q)\) of \(J(x,y)\) and the exact number \(E_n(q)\) of **labeled, unordered** admissible pairs attaining that maximum are:

| Length \(n\) | Maximum \(M_n(q)\) | Extremal-pair count \(E_n(q)\) | Canonical patterns by support size \(s\) |
|---|---:|---|---|
| 3 | 3 | \((q)_{\underline{3}}/2\) | \(\{3:1\}\) |
| 4 | 4 | \((q)_{\underline{2}}/2+2(q)_{\underline{3}}+(q)_{\underline{4}}/2\) | \(\{2:1,3:4,4:1\}\) |
| 5 | 6 | \((q)_{\underline{3}}/2\) | \(\{3:1\}\) |
| 6 | 6 | \((q)_{\underline{2}}+4(q)_{\underline{3}}+(q)_{\underline{4}}\) | \(\{2:2,3:8,4:2\}\) |

Here \((q)_{\underline{s}}=q(q-1)\cdots(q-s+1)\), with value zero when \(s>q\). Every canonical pattern listed below attains the stated maximum, and no other equality pattern does. The digits in the next table are **abstract equality labels**, not field elements or fixed alphabet values. Apply any injective relabeling of the distinct digits to symbols of \(\Sigma_q\); also identify two codeword orders when counting pairs.

| \(n\) | Canonical equality-pattern center pairs \((x,y)\) |
|---|---|
| 3 | `012 / 210` |
| 4 | `0110 / 1001`; `0112 / 1021`; `0120 / 1002`; `0120 / 1021`; `0120 / 2102`; `0123 / 1032` |
| 5 | `01201 / 10210` |
| 6 | `001201 / 010210`; `010101 / 100110`; `010210 / 001201`; `010210 / 101201`; `011001 / 101010`; `012010 / 102100`; `012010 / 102101`; `012011 / 102101`; `012012 / 021021`; `012012 / 102102`; `012013 / 102103`; `012312 / 021321` |

Under simultaneous alphabet relabeling, reversal of both words, and swapping the two centers, these patterns form respectively \(1,4,1,5\) symmetry classes. In the quaternary case the extremal-pair counts, for lengths three through six, are respectively \(12,66,12,132\).

## Assumptions and scope

The alphabet is arbitrary but finite with \(q\ge3\). Each two-deletion ball contains **distinct output words**, not deletion-position multiplicities. The separation hypothesis is exactly the empty intersection of the one-deletion shadows. For equal-length centers this is equivalent to Levenshtein distance at least two. All maxima and enumerations are over **unordered distinct centers**. The four blocklengths \(n=3,4,5,6\) are the complete domain of this theorem; no statement about equality-case populations for longer lengths is inferred.

The statement classifies extremizers of the established pairwise ambiguity problem; it does not claim that the isolated maximum values, including the universal bound of six, are previously unknown.

## Proof

**Step 1: Reduce every alphabet to set partitions.** Concatenate an ordered pair of length-\(n\) centers, producing \(2n\) indexed positions. Record which positions carry equal symbols. This is a partition of the indexed positions. Such a partition has a unique **restricted-growth string** \(a_1,\ldots,a_{2n}\), determined by
\[
 a_1=0,\qquad 0\le a_j\le1+\max_{1\le i<j}a_i\quad (2\le j\le2n).
\]
Its number of distinct labels is \(s=1+\max_j a_j\). Any concrete pair over \(\Sigma_q\) with the same equality pattern is obtained by injecting these \(s\) abstract labels into the alphabet, giving exactly \((q)_{\underline{s}}\) ordered labeled pairs if \(s\le q\), and none otherwise. The sizes of each deletion shadow and its pairwise intersections depend only on the equality pattern, not on the chosen injection.

**Step 2: Exhaustively determine the qualifying equality patterns.** The accompanying complete source file `rgs_classifier.cpp` recursively generates **every** restricted-growth string of length \(2n\), without skipping any partition. For each string, it forms both centers, enumerates all exactly-one-deletion subsequences and rejects the pattern unless their distinct sets are disjoint. For every survivor it enumerates and deduplicates the exactly-two-deletion subsequences, intersects these sets, and updates the maximum and its full list of witnesses. The encodings are injective: for these lengths the largest possible restricted-growth digit is at most eleven, and each retained symbol is written as a distinct base-sixteen digit, with fixed output length within each comparison.

The complete exhaustive counts for \(n=3,4,5,6\) are respectively \(203,4140,115975,4213597\) total equality patterns. Respectively \(133,3690,113073,4194600\) satisfy the one-deletion-separation condition. The computed maxima are \(3,4,6,6\). The exhaustive witness lists have respectively \(1,6,1,12\) patterns, exactly the ones given in the theorem, grouped by support sizes as stated. These are finite exhaustive computations, with their full source and execution output embedded alongside the theorem; they are not statistical samples. The proof of completeness is the bijection from arbitrary pairs to restricted-growth equality patterns together with the explicit exhaustive recursive traversal.

**Step 3: Count labeled, unordered pairs.** For each support size \(s\) there are \((q)_{\underline{s}}\) injections of the equality labels into \(\Sigma_q\). Since the centers of a qualified pair are distinct, swapping their order has no fixed point; it is a fixed-point-free involution. Therefore the sum of the labeled ordered counts is divided by precisely two. Applying the profile multiplicities \(\{3:1\}\), \(\{2:1,3:4,4:1\}\), \(\{3:1\}\), and \(\{2:2,3:8,4:2\}\) gives the four displayed formulas, for every \(q\ge3\) without further computation.

**Step 4: Symmetry classes.** Alphabet relabeling has already been removed by restricted-growth normalization. The remaining actions on an ordered representative are center swap and simultaneous reversal; they commute, and both preserve deletion shadows. Re-normalizing each image partitions the complete witness lists into orbits of sizes \(1\); \(1,2,2,1\); \(1\); and \(4,2,2,2,2\), respectively. The complete independent orbit replay is in `verify_orbits.py`.

## Verification

Run `g++ -std=c++17 -O3 -Wall -Wextra -pedantic rgs_classifier.cpp -o rgs_classifier` and `./rgs_classifier`, then compare with `rgs_output.txt`. Independently run `python3 verify_direct.py` and compare with `direct_output.txt`; it constructs actual labeled words and actual deletion-output tuples rather than canonical partitions, and checks all eligible pairs for alphabet sizes two through six in the listed finite test ranges. Run `python3 verify_orbits.py rgs_output.txt` to check the exact canonical-pattern supports and the orbit decomposition against `orbit_output.txt`.

The verifier transcript ends in `DIRECT_VERIFY_OK`; the orbit transcript ends in `ORBIT_VERIFY_OK`. The restricted-growth enumerator is the exhaustive proof certificate for **all** alphabets at the four stated lengths; direct-word runs are additional independent tests rather than a purported proof by extrapolation.

## Relationship to prior work

Sun and Ge, *Extremal Deletion-Ball Intersections under Run-Count and Lower-Order Deletion-Ball Intersection Constraints* (first posted June 24, 2026), prove a general sharp upper bound, which in the present separation and two-deletion setting yields six. Wang, Li, and Fu, *Sequence Reconstruction Problem for Ternary Deletion Channels* (first posted September 29, 2025), determine ternary worst-case intersection values, while Wang, Li, and Fu, *On Sequence Reconstruction Problem for q-ary Deletion Channels* (first posted September 15, 2026), obtain general-alphabet maxima and characterize asymptotic extremizers for sufficiently large lengths. These known bounds and large-length descriptions are **not** claimed as new here.

The claimed contribution is the **complete equality-pattern and labeled-population classification at every length from three through six**, including the short-length boundary behavior and the exact orbit counts. The consulted articles' statements and inspected case analyses did not exhibit this finite equality-pattern census or its all-alphabet polynomial counts. A stronger or equivalent enumeration in unindexed work remains possible; a negative literature search does not prove global novelty.

## Limitations

The classification is restricted to the four explicitly stated lengths and pairwise intersections of exactly-two-deletion balls under one-deletion separation. It makes no claim about longer-length populations, code rates, practical decoder complexity, or physical sequencing experiments. The finite classification relies on a reproducible, deterministic, exhaustive computation of equality patterns; no independent external audit has been performed. Published maximum bounds are credited. Possible equivalent enumeration in unindexed literature is a residual originality risk.

## References

1. Xiang Wang, Han Li, Fang-Wei Fu, *On Sequence Reconstruction Problem for q-ary Deletion Channels*, arXiv:2609.16837, first posted September 15, 2026. https://arxiv.org/abs/2609.16837
2. Yubo Sun, Gennian Ge, *Extremal Deletion-Ball Intersections under Run-Count and Lower-Order Deletion-Ball Intersection Constraints*, arXiv:2606.25822, first posted June 24, 2026. https://arxiv.org/abs/2606.25822
3. Xiang Wang, Han Li, Fang-Wei Fu, *Sequence Reconstruction Problem for Ternary Deletion Channels*, arXiv:2509.24237, first posted September 29, 2025. https://arxiv.org/abs/2509.24237
