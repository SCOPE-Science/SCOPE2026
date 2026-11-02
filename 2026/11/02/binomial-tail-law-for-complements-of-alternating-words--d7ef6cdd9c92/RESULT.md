# Binomial-tail law for complements of alternating words

## Finding

Fix two distinct letters \(a\) and \(b\). Let \(C(w,u)\) mean the set of **distinct** words left by deleting an order-preserving embedding of \(u\) in \(w\). For all integers \(m,k\geq0\), put \(w=(ab)^{m+k}\) and \(u=(ab)^k\). Every member of \(C(w,u)\) splits uniquely into \(m\) consecutive two-letter blocks, each \(ab\) or \(ba\). Define the *reversed-block run count* as the number of maximal nonempty runs of consecutive \(ba\) blocks.

**Exact classification.** A word consisting of \(m\) blocks from \(\{ab,ba\}\) belongs to \(C(w,u)\) if and only if its reversed-block run count is at most \(k\). Thus
\[
|C((ab)^{m+k},(ab)^k)|=\sum_{r=0}^{k}\binom{m+1}{2r}
=\sum_{j=0}^{\min\{2k,m\}}\binom{m}{j}.
\]
Binomial coefficients outside their natural range are zero. The number of residuals requiring *exactly* \(r\) deleted \(ab\) pairs is \(\binom{m+1}{2r}\). In particular, all \(2^m\) two-letter block words are attainable exactly when \(m\le2k\). At \(m=2k+1\) the unique missing one is the block-type alternating word starting and ending in \(ba\).

## Assumptions and scope

The source is the finite alternating word \((ab)^{m+k}\) over an alphabet containing at least the two distinct symbols \(a,b\). An embedding of \(u\) is a strictly increasing sequence of positions reading \(u\), and different embeddings may give the same residual, counted only once. The empty-word cases \(m=0\) and \(k=0\) are included. No cyclic interpretation is used. The formula is a two-parameter theorem for all nonnegative integers \(m,k\), not a finite-size extrapolation.

## Proof

**1. Every residual splits into balanced pairs.** In any prefix of \((ab)^n\), the number of \(a\)'s minus the number of \(b\)'s belongs to \(\{0,1\}\). The same is true of every prefix of the selected subsequence \(u=(ab)^k\). Take any even-length prefix \(v'\) of the residual \(v\). It comes from a source prefix with some prefix of \(u\) removed, so its \(a\)-minus-\(b\) discrepancy is one of \(-1,0,1\). Since the length of \(v'\) is even, that discrepancy must be even, hence zero. Therefore each consecutive two-letter block in \(v\) has one \(a\) and one \(b\), and is either \(ab\) or \(ba\).

**2. Necessity of the run bound.** Immediately before the first symbol of any residual two-letter block, the residual prefix has equal numbers of \(a\) and \(b\). If the block starts with \(a\), the corresponding source prefix has discrepancy zero (every \(a\) in \((ab)^n\) occurs at an odd position), so the already deleted prefix of \(u\) also has discrepancy zero. Thus an even number of letters of \(u\) have been used. If the block starts with \(b\), the source prefix has discrepancy one, so the deleted prefix has discrepancy one and an odd number of letters of \(u\) have been used. As we move through the block types, each new run of \(ba\) blocks requires the used-letter count of \(u\) to change from even to odd (from zero to odd for the initial run). Such a change uses a new \(a\) of the ordered subsequence \((ab)^k\). Distinct runs use distinct \(a\)'s; there are \(k\) of them. Hence there are at most \(k\) reversed-block runs.

**3. Sufficiency and the exact required deletions.** Conversely, partition any block-type word into single \(ab\) blocks and maximal \(ba\)-runs. Retain each \(ab\) block verbatim from a source segment \(ab\). For a maximal \(ba\)-run of length \(q\ge1\), use a source segment \((ab)^{q+1}\) and delete its first \(a\) and last \(b\); the residual is exactly \((ba)^q\), while the deleted letters form one ordered \(ab\) pair. Concatenating all segments gives source \((ab)^{m+r}\), residual \(v\), and deleted subsequence \((ab)^r\), where \(r\) is the number of reversed-block runs. If \(k\ge r\), append \((ab)^{k-r}\) to the source and delete all appended letters. The source becomes \((ab)^{m+k}\), the deleted subsequence becomes \((ab)^k\), and \(v\) is unchanged. Together with necessity, this also proves that \(r\) is the exact minimum number of deleted \(ab\) pairs.

**4. Exact count and threshold.** There are \(m+1\) boundaries before, between, and after the \(m\) blocks. A block-type word with exactly \(r\) nonempty runs of \(ba\) is determined uniquely by the \(2r\) ordered boundaries marking their starts and ends, so there are \(\binom{m+1}{2r}\) such words. Summation yields the first displayed formula; Pascal's identity yields \(\sum_{r=0}^{k}\binom{m+1}{2r}=\sum_{j=0}^{\min\{2k,m\}}\binom mj\). The largest number of reversed-block runs among \(m\) blocks is \(\lceil m/2\rceil\), giving full attainment iff \(m\le2k\). For \(m=2k+1\) the only block-type word with \(k+1\) reversed-block runs is \(ba,ab,\ldots,ab,ba\), proving sharpness.

## Verification

The standalone file `alternating_complement_verify.py` directly enumerates all distinct deletion residuals by a memoized two-choice recursion, independently builds the predicted block-type language, and compares both exact sets and two independent binomial formulas for all \(0\le k\le n\le11\): 78 parameter pairs. Run with `python3 alternating_complement_verify.py`; expected output is `ALTERNATING_COMPLEMENTS_VERIFY_OK 78 parameter pairs, n<=11`. This finite check is a regression test; the four-step proof above establishes the statements for every \(m,k\).

## Relationship to prior work

Adamson, Fleischmann and Huch introduce complement scattered-factor sets and give algorithms and structural results. Their complete open-access March 2026 preprint was inspected, especially Sections 3 and 4 and the conclusion. They explicitly leave closed formulas for special cases as an open direction. Their Theorem 4.5 concerns the singleton situation \(C(w,u)=\{u\}\) and perfect shuffles, not the present two-parameter residual-language and binomial-tail distribution. The present result makes a natural test family completely explicit rather than re-running their general dynamic programming. Standard binomial boundary counting supplies the final enumeration once the new run-language equivalence is proved.

## Limitations

The theorem is restricted to the two-symbol alternating source and alternating deleted subsequence. It does not give a closed formula for arbitrary word pairs or classify general complement-scattered-factor sets. A general algorithm in the primary paper can compute each finite instance; the contribution here is the all-parameter structural language classification, closed form, and sharp complete-coverage threshold. Independent external priority review has not been performed, and an equivalent unindexed classical shuffle count remains a residual risk.

## References

1. D. Adamson, P. Fleischmann and A. Huch, *\(\text{(Sets of) Complement Scattered Factors}\)*, arXiv:2603.20790, first posted 21 March 2026. https://arxiv.org/html/2603.20790v1
2. Standard binomial identity \(\binom{m+1}{2r}=\binom{m}{2r}+\binom{m}{2r-1}\), used in the final count.
