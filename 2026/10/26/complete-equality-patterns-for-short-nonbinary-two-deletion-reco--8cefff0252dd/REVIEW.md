# Self-review

## Correctness — PASS

The exact domain is every labeled alphabet of size \(q\ge3\), with word lengths \(n=3,4,5,6\), distinct unordered center pairs, and empty one-deletion-shadow intersection. The claimed object is the entire **equality-case** census, not merely the known intersection upper bound. The proof reduces arbitrary alphabets to equality partitions on \(2n\) labeled positions and proves an injective lift count \((q)_{\underline{s}}\). It enumerates all \(203\), \(4140\), \(115975\), and \(4213597\) corresponding restricted-growth patterns and checks every one-deletion and two-deletion set, with duplicate subsequences removed. Each maximum and every equality pattern is retained. Dividing ordered pairs by two is justified by the fixed-point-free center swap. Independent direct enumeration for small labeled alphabets and a separate orbit replay match. The primary proof evidence is the complete reproducible classifier source and its matched output, not the output log alone.

## Originality — PASS, with residual risk

Wang, Li, and Fu (arXiv:2509.24237) determine ternary maximum values, not the complete labeled equality counts. Sun and Ge (arXiv:2606.25822, Theorem 1.1) supply a universal upper bound of six for one-deletion-separated centers under exactly two deletions; an upper bound does not enumerate equality cases. Wang, Li, and Fu (arXiv:2609.16837, Theorem 32, Remark 5, Section VI) give general-alphabet maximal behavior and extremal structure for sufficiently large lengths, and a sharper classification for \(t\ge q+2\), which does not cover \(t=2\). None of the inspected relevant claims states the all-alphabet length-three-through-six equality templates and falling-factorial pair counts. Relevant semantic mathematical-record searches and accessible earlier claims did not identify equivalent coverage. An undiscovered combinatorial enumeration, or an implicit small case of an older equivalence theorem, remains possible; searches cannot prove absolute priority.

## Value — PASS

The exact population and structure of worst-case ambiguity pairs refine a natural reconstruction threshold question. In particular, six-way ambiguity first appears at length five with one three-symbol equality type, while length six has twelve types across two-, three-, and four-symbol supports. Their counts differ significantly by alphabet size, including the quaternary counts \(12,66,12,132\), and the complete symmetry classification reveals \(1,4,1,5\) orbit types. This is a natural complete classification at the shortest interesting lengths, not an arbitrary reslicing or a claim of new code-rate improvement.

## Closest literature and remaining limitations

Inspected: arXiv:2609.16837 (introduction, definitions, Sections III–VI, Theorem 32, Remark 5, appendix opening); arXiv:2606.25822 (abstract, Introduction and Theorem 1.1); arXiv:2509.24237 (introduction, main ternary theorem and short-length computations). The theorem does not address other lengths, higher deletions, or practical protocols. There is no independent external audit. Residual originality risk: unindexed prior equality-census work.

Self-review: passed. Independent audit: not yet performed.
