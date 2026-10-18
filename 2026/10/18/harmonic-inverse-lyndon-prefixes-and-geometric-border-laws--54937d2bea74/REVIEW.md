# Scientific review: harmonic inverse Lyndon prefixes and geometric border laws

## Correctness — PASS

The stated formulas hold for every finite totally ordered alphabet of fixed size \(q\geq2\), all positive lengths, and all permitted longest-border lengths. Their core is a unique-root refinement of the established anti-Lyndon periodic-prefix characterization (Bonizzoni et al., arXiv:1705.10277, Proposition 7.21). Root uniqueness uses the unborderedness of anti-Lyndon words; maximal border corresponds to root length. Möbius inversion counts the roots. Prefix closure and integer tail-summing then give the exact expected total inverse Lyndon array mass. The geometric-limit mean is justified with a uniform exponential-tail bound, not simply pointwise convergence. The finite checker exhaustively compares independent descriptions in the documented ranges.

## Originality — PASS (within the inspected literature)

The principal predecessor supplies the anti-Lyndon characterization, which is explicitly credited. The 2019/2020 paper arXiv:1911.01851 studies borders between consecutive canonical inverse Lyndon factors. The March and September 2026 inverse Lyndon array papers (arXiv:2603.17537 and arXiv:2609.23401) supply constructions and structural border correction. Examination of the relevant definitions, results, experimental sections, and border discussions found no exact fixed-length border histogram, its geometric conditional limit, or the harmonic random-prefix tail and sharp \(\frac{q}{q-1}n\log n\) array-mass law. Relevant published results about distinct substrings and subsequence universality concern different observables. A remaining risk is that an independent enumeration or average-case analysis may occur in literature not located by the checked searches.

## Value — PASS

The 2026 inverse Lyndon array work identifies nontrivial borders as a central structural difficulty but gives construction-time benchmarks rather than a distribution for this feature. The explicit necklace-refined border law quantifies that difficulty for uniformly sampled inverse Lyndon words; the sharp harmonic tail predicts logarithmic individual array entries and \(n\log n\) total entry mass for random strings. This is a natural exact average-case statistic for a recently introduced string data structure, not a selected parameter slice or a restatement of the running-time bound. The word-level root classification is a known starting point, not claimed as a new stand-alone theorem.

## Limitations and overlap risks

The law conditions on an inverse Lyndon word; it does not describe the border of a maximal factor in a random string. Input for array expectation must be iid uniform. A membership characterization and primitive-necklace enumerator are already known, so the contribution is the derived quantitative distribution and array statistic. Literature coverage is not exhaustive; independent scientific validation has not occurred.

Self-review: passed. Independent audit: not yet performed.
