# First sharp failure of count-and-transition bounds for adaptive circular subsequences

## Finding

Let \(w\) be a nonconstant binary circular word of circumference \(n\ge2\). Write \(z(w)\) and \(o(w)\) for its numbers of zeros and ones, and \(t(w)\) for its number of cyclic transitions (including the last-to-first adjacency). A binary word \(u\) is a *one-turn circular scattered subsequence* of \(w\) if \(u\) is a subsequence of some linear rotation of \(w\). The rotation may depend on \(u\). Define \(U(w)\) to be the largest integer \(k\) such that **every** binary word of length \(k\) is such a subsequence, and put
\[
 B(w)=\min\bigl\{z(w),o(w),t(w)+1\bigr\}.
\]

**Theorem (first failure, complete boundary, and persistent family).** For every nonconstant binary circular word with \(2\le n\le14\), one has \(U(w)=B(w)\), with exactly one exception up to cyclic rotation:
\[
 w_*=\texttt{00000101111101},\qquad B(w_*)=7,\quad U(w_*)=6.
\]
Its 14 rotations are all the exceptions among labeled binary words of length at most 14. Moreover, for *every* pair of integers \(a,b\ge5\),
\[
 w_{a,b}=0^a\,1\,0\,1^b\,0\,1
 \quad\text{satisfies}\quad U(w_{a,b})=6<B(w_{a,b})=7.
\]
For arbitrary nonconstant binary circular words of any circumference, \(U(w)\le B(w)\).

The result concerns the **union of scattered-subsequence spectra over rotations** (\(\forall u\,\exists\text{ rotation}\)), not the previously studied condition that **one rotation** contains every target (\(\exists\text{ rotation}\,\forall u\)).

## Assumptions and scope

Binary words are on the fixed alphabet \(\{0,1\}\). A circular word is a word considered up to cyclic rotation, not reversal or bit complementation. A circular scattered subsequence selects distinct positions in clockwise order within **one traversal** of the circle; equivalently it is a linear subsequence of a single rotation. The selected positions must not make more than one revolution. The finite classification includes all lengths \(2\le n\le14\) and all nonconstant binary words. The family assertion is for all integers \(a,b\ge5\), without an upper length restriction. The scripts use the literal symbols `0` and `1`.

## Proof

**1. A universal upper bound.** Any circular scattered subsequence can have no more cyclic changes of symbol than its parent word: successive chosen positions partition the cycle into disjoint nonempty arcs, and each change between successive selected symbols requires at least one parent transition on its arc. Thus an alternating binary target of even length \(t(w)+2\) (which has \(t(w)+2\) cyclic transitions) is impossible. Also, the constant length-\(z(w)+1\) and length-\(o(w)+1\) targets are impossible. These three obstructions prove \(U(w)\le B(w)\).

**2. Finite complete classification.** A property of being a circular scattered subsequence is invariant under rotation of the target, since the starting chosen position may also be rotated. Thus it suffices to test one representative of each length-\(B(w)\) *target necklace*. Likewise \(U\) and \(B\) are unchanged by rotating the parent, so parent necklaces suffice. Every length-\(n\) binary word is generated, its lexicographically least rotation is used as representative, and every nonconstant representative is tested. In `verify.py`, `scan_greedy` tests each target against the \(n\) source cuts with an ordinary greedy subsequence scan. Independently, `scan_selection` enumerates every size-\(B(w)\) subset of the parent's positions, forms its selected word, and adds every rotation of that word to the covered-target set. This is exhaustive because every cyclic subsequence arises from some set of selected positions, and shifting the first selected position realizes all rotations. The two methods agree for every input.

The complete computed census is:

| Circumference \(n\) | Binary necklaces | Necklaces with \(U(w)<B(w)\) |
|---:|---:|---:|
| 2 | 3 | 0 |
| 3 | 4 | 0 |
| 4 | 6 | 0 |
| 5 | 8 | 0 |
| 6 | 14 | 0 |
| 7 | 20 | 0 |
| 8 | 36 | 0 |
| 9 | 60 | 0 |
| 10 | 108 | 0 |
| 11 | 188 | 0 |
| 12 | 352 | 0 |
| 13 | 632 | 0 |
| 14 | 1182 | 1 |

The sole failure is \(w_*\), for which the least missing target necklace of length seven is `0010011`. Because \(w_*\) has exactly six cyclic transitions, it cannot have a proper period of seven (a seven-periodic double word has an even number of transitions in each period, and hence a multiple of four transitions in total), and it is plainly nonconstant; thus its rotation orbit has size 14.

**3. Lower bound six at the exception.** The next table explicitly certifies all 14 rotation classes of binary targets of length six. For each target, the listed 1-based cyclic positions in `00000101111101` yield it, in the indicated order; after the last position, no more than one traversal has occurred. Any rotation of a listed target is similarly obtainable by starting at another selected position.

| Target | Chosen cyclic positions |
|---|---|
| `000000` | 1,2,3,4,5,7 |
| `000001` | 1,2,3,4,5,6 |
| `000011` | 1,2,3,4,6,8 |
| `000101` | 1,2,3,6,7,8 |
| `000111` | 1,2,3,6,8,9 |
| `001001` | 1,2,6,7,13,14 |
| `001011` | 1,2,6,7,8,9 |
| `001101` | 1,2,6,8,13,14 |
| `001111` | 1,2,6,8,9,10 |
| `010101` | 1,6,7,8,13,14 |
| `010111` | 1,6,7,8,9,10 |
| `011011` | 7,8,9,13,14,6 |
| `011111` | 1,6,8,9,10,11 |
| `111111` | 6,8,9,10,11,12 |

Thus \(U(w_*)\ge6\). The next step shows that it is strictly less than seven.

**4. Structural forbidden pattern in every member of the family.** In the cyclic run decomposition \(0^a,1,0,1^b,0,1\), denote the large zero run by \(A\), the large one run by \(B\), and the two singleton zero runs by \(C,E\) in cyclic order. The circular target `0010011` has two zero-blocks, each of length two; there is at least one selected one between these two zero-blocks in *both* circular directions. Consequently a single parent zero run cannot contribute selected zeros to both target zero-blocks. Since only \(A\) contains more than one zero, one target zero-block must use \(A\), while the other uses both singleton zeros \(C,E\). To have \(C,E\) adjacent among selected positions, they must be selected in the clockwise order \(C\to E\): the reverse arc \(E\to C\) passes through \(A\), where the other target zero-block has selected positions. Their clockwise arc passes through all of \(B\), which must therefore contain no selected symbols. Once \(B\) is skipped, only the two singleton ones remain selectable, while `0010011` requires three ones. This contradiction proves the target is absent for **all** \(a,b\ge1\).

For \(a,b\ge5\), both symbol counts are at least seven and there are exactly six cyclic transitions, so \(B(w_{a,b})=7\). Every \(w_{a,b}\) has \(w_*\) as a one-turn circular scattered subsequence, by deleting surplus symbols only from the two long runs. Every length-six target that appears in \(w_*\) therefore also appears in \(w_{a,b}\). Hence \(U(w_{a,b})\ge6\). Together with the absent target `0010011`, this proves \(U(w_{a,b})=6\).

## Verification

Run `python3 verify.py` in a directory containing that single standalone script. It requires Python's standard library only. Expected leading line: `ROTATIONAL_SUBSEQUENCE_BOUNDARY_PASS`. The script independently checks the entire finite census by (i) target-centric greedy subsequence membership through every cut and (ii) source-centric enumeration of all selected-position subsets and target rotations. It checks the explicit length-six witnesses and several longer members of the infinite family. The proof of the *arbitrary-parameter* family is the run argument in Section 4; finite experiments alone do not establish it.

## Relationship to prior work

Barker, Fleischmann, Harwardt, Manea and Nowotka introduce scattered-factor universality and define *circular universality* by the existence of **one** rotation that is universal for every target; this reverses the quantifiers used here. Fleischmann, Germann and Nowotka analyze the same one-cut notion through arch decompositions and powers. Kosche, Koß, Manea and Siemer develop minimal and shortest absent subsequences for a fixed linear word. Their established results are not claimed as new here. None of the inspected corresponding statements asserts the first exact failure of the rotation-union count/transition bound or the persistent two-parameter obstruction described above. The claim is limited to the specified new invariant and a precise structural family; it does not follow from a mere difference of naming conventions.

## Limitations

The global equality \(U(w)=B(w)\) is **not** claimed; the theorem explicitly disproves it. The finite minimality and uniqueness claims rest on an exhaustive reproducible computational census through circumference 14, with two implementations of the membership test. No classification of all deficient words at larger lengths, nor a general formula for \(U(w)\), is asserted. An equivalent result in unindexed literature is possible. No independent mathematical audit has been performed.

## References

1. L. Barker, P. Fleischmann, K. Harwardt, F. Manea and D. Nowotka, *Scattered Factor-Universality of Words*, first publicly posted 2020-03-10, arXiv:2003.04629, especially Definition 4 and Section 4 on the fixed-cut circular universality index. https://arxiv.org/abs/2003.04629
2. P. Fleischmann, S. B. Germann and D. Nowotka, *Scattered Factor Universality — The Power of the Remainder*, first publicly posted 2021-04-19, arXiv:2104.09063, especially Definition 2, Theorems 9–10, and the conclusion. https://arxiv.org/abs/2104.09063
3. M. Kosche, T. Koß, F. Manea and S. Siemer, *Absent Subsequences in Words*, first publicly posted 2021-08-31, arXiv:2108.13968, especially Definitions 2.2–2.4 and Theorems 3.1 and 3.4. https://arxiv.org/abs/2108.13968
