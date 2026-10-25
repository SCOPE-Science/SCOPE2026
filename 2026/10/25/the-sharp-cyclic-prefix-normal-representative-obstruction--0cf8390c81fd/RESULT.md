# The sharp cyclic prefix-normal representative obstruction

## Finding

A binary linear word is **prefix normal with respect to ones** if, at each length, its prefix contains at least as many ones as every contiguous factor of that length. A **prefix-normal cut** of a binary circular word is a cut yielding a prefix-normal linear word.

For each integer \(n\ge 1\), every binary circular word of length \(n\) has a prefix-normal cut **if and only if** \(n\le10\). At length \(11\), exactly **three** circular words without such a cut exist, up to rotation (reversal and complement are *not* identified). Their lexicographically smallest rotations are:

```text
00010101011
00011001011
00110110111
```

Consequently exactly \(33\) labeled binary words of length \(11\) have no prefix-normal cut. For **every** \(n\ge11\), the explicitly constructed circular word

\[
W_n=\texttt{00010101011}\,0^{n-11}
\]

has no prefix-normal cut. This is a statement about the existence of *some* prefix-normal rotation, not about whether the unique prefix-normal form of a chosen linear word is a rotation of that word.

## Assumptions and scope

The alphabet is \(\{0,1\}\), with **ones** as the distinguished letter; reversing or complementing is not allowed when taking a cut. Circular words are equivalence classes modulo cyclic rotation only. A cut at index \(i\) of \(w=w_0\cdots w_{n-1}\) gives the length-\(n\) linear word \(w_i\cdots w_{n-1}w_0\cdots w_{i-1}\). Linear factors do not wrap around that cut. At length \(n\) the all-zero and all-one words trivially admit a prefix-normal cut.

For a linear word \(v\) of length \(n\), write \(P_v(\ell)\) for the number of ones in its prefix of length \(\ell\) and \(F_v(\ell)\) for the maximum number of ones in any contiguous length-\(\ell\) factor. Prefix normality means \(P_v(\ell)=F_v(\ell)\) for all integers \(1\le\ell\le n\).

## Proof

**A finite positive-range certificate and exact length-eleven classification.** A direct exact algorithm enumerates the \(2^n\) length-\(n\) binary words for each \(1\le n\le11\), checks every cyclic cut using the defining prefix-versus-factor inequalities, and reduces the negative cases by lexicographically minimal rotation. It finds zero negative necklaces for \(1\le n\le10\) and, at \(n=11\), precisely the three listed representatives. This algorithm is fully included as `verify.py`.

A second enumeration independently constructs necklaces through **positive gap compositions**. For any circular word with \(d\ge1\) ones, a cut beginning at a one is encoded by the \(d\) positive cyclic gaps \((g_1,\ldots,g_d)\) between successive ones, summing to \(n\). Each such gap tuple yields the word \(10^{g_1-1}\cdots10^{g_d-1}\); taking the least cyclic rotation of the tuple counts each nonzero binary necklace exactly once. No cut beginning with zero can be prefix normal when the word contains a one.

A rotation beginning at a one is prefix normal precisely when, for every \(1\le k\le d-2\) and \(2\le j\le d-k\),

\[
\sum_{t=1}^{k} g_t\ \le\ \sum_{t=j}^{j+k-1}g_t.
\]

Indeed, the left sum is the distance from the first to the \((k+1)\)-st one. A smaller sum on the right gives \(k+1\) ones in a shorter internal interval than the initial \((k+1)\)-one span, contradicting prefix normality. Conversely, any factor with more ones than a prefix of equal length provides a shorter span of consecutive ones than the corresponding initial span. This proves the criterion without relying on the bitwise implementation. It is also the gap characterization used in the published theory of prefix-normal words. Enumerating all positive compositions with \(1\le d\le n\), taking their cyclic classes, and checking every rotation by these inequalities independently reproduces the first enumeration for every \(n\le11\). This second algorithm and exact expected outputs are included in `verify.py`.

The `witnesses.csv` certificate independently gives, for each of the \(33\) cuts of the three exceptional necklaces, an explicit later factor with strictly more ones than the prefix of the same length. Every listed witness is checked directly by `verify.py`.

**The unbounded negative range.** For arbitrary \(n\ge11\), the word \(W_n\) has ones exactly at zero-based positions \(3,5,7,9,10\). A cut starting at a zero fails at length one. A cut at any of positions \(3,5,7\) starts with `10` but contains a later `11`, so fails at length two. The cut at position \(9\) starts with `11000` but contains a later `10101`, which has three ones against the prefix's two, so fails at length five. The cut at position \(10\) starts with `100` but contains a later `101`, so fails at length three. Appending any number of zeros preserves all five comparisons. Thus no cyclic cut is prefix normal, for every integer \(n\ge11\).

These positive and negative arguments give the asserted sharp iff threshold and exact first-exception census.

## Verification

Run `python3 verify.py` with `witnesses.csv` in the same directory. Only the Python standard library is required. The checker exhausts all binary words and all cyclic positive-gap compositions for lengths one through eleven; confirms the identical three exception necklaces under the independent methods; verifies all 33 explicit factor witnesses; and tests the fixed symbolic obstruction comparisons for lengths eleven through 120. The unbounded conclusion above follows from the explicit mathematical proof, **not** from testing through 120. All additions, comparisons and counts are exact integers.

## Relationship to prior work

Fici and Lipták's foundational work establishes existence and uniqueness of a prefix-normal **form** for each *linear* word, with no promise that the form lies in its cyclic rotation class. They explicitly observe that the form need not be a rotation or reversal of the input; that observation is logically different from the existence of *some* prefix-normal cut of a circular input. The 2014 generation paper develops exhaustive algorithms for linear prefix-normal words. The 2014 *Normal, Abby Normal, Prefix Normal* paper supplies the equivalent consecutive-one-gap inequalities used as one independent check here. The later consolidated 2016 manuscript treats linear equivalence, Lyndon/pre-necklace containment and fixed-density enumerations. None of these inspected results provides the sharp cyclic-cut existence threshold or the three rotation classes at its first failure.

The cyclic-cut obstruction distinguishes canonicalization by a rephasing of the **same** circular word from canonicalization by replacing the word with another equivalent linear word. The direct combinatorial family makes the obstruction persist at every longer length.

## Limitations

The first-failure census is exhaustive only at length eleven; no formula for the number of exceptional necklaces at larger lengths is claimed. Finite verification supports the small threshold; the all-length construction is proved separately. The claim is **ones-prefix normality with linear factors after each cut**, not a condition comparing prefixes to all circular factors, and not a simultaneous condition for zeros. Unindexed prior work or nontextual supplementary datasets might contain equivalent enumeration; priority is not independently certified.

## References

- G. Fici and Z. Lipták, *On Prefix Normal Words*, Developments in Language Theory (2011), DOI: 10.1007/978-3-642-22321-1_20. Accessible author-version HTML at https://arxiv.org/abs/1805.12405 (uploaded in 2018, retaining the 2011 proceedings content).
- P. Burcsi, G. Fici, Z. Lipták, F. Ruskey and J. Sawada, *On Combinatorial Generation of Prefix Normal Words*, arXiv:1401.6346v1 (first public version 2014-01-24), https://arxiv.org/abs/1401.6346.
- P. Burcsi, G. Fici, Z. Lipták, F. Ruskey and J. Sawada, *Normal, Abby Normal, Prefix Normal*, arXiv:1404.2824v1 (first public version 2014-04-01), https://arxiv.org/html/1404.2824v1; see the fixed-density gap criterion.
- P. Burcsi, G. Fici, Z. Lipták, F. Ruskey and J. Sawada, *On Prefix Normal Words and Prefix Normal Forms*, arXiv:1611.09017v1 (2016-11-28), https://arxiv.org/abs/1611.09017; revised consolidation of the above theory.
