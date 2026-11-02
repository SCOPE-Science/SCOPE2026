# Self-review

## Correctness — PASS
The theorem states explicit integer ranges, linear-factor rather than cyclic coverage, a one-based position convention, and the one-per-symbol restriction forced by singleton factors. The proof first exhibits the first \(q\) positions as an attractor. The \(m=1\) case is separate, then every potentially missed factor is classified into nonwrapping short, wrapping short, and long overlapping-occurrence types. The latter two force the same endpoint selections; the boundary factor \(U_r\) establishes the converse. Counting uses independent selections across letter classes. Complete brute-factor checks for 88 parameter instances agree with all implications. Scientific limit: the script does not prove the infinite theorem, which relies on the written case analysis.

## Originality — PASS, residual uncertainty
The closest overlapping publicly posted result proves the \(q=2,r=0\) alternating full-period case with \(m^2-1\) optimal pairs. That special case is explicitly acknowledged as prior. The present theorem additionally classifies all \(q\ge3\) alphabets and every nonempty proper terminal prefix, including the sole-obstruction phenomenon and its exact \(2^r m^{q-r-2}\) exclusion term. Prezza (2017), Kempa et al. (2018), Restivo et al. (2022) and Banbara et al. (2026) provide general attractor foundations, algorithms, asymptotic prefix complexities or classifications for different morphic families, respectively, not this explicit finite-period placement census. Neither a search failure nor a thematic difference alone proves uniqueness. Residual risk: a general result on minimum attractors of periodic words may implicitly specialize to this formula, and independent review is not complete.

## Mathematical value — PASS
Attractor size alone loses the choice complexity of an optimal factor-covering representation. The result exactly counts all minimum representations for a canonical periodic baseline and identifies which boundary placements are forbidden; the last-letter completion of a period removes the obstruction altogether. All failures among the combinatorially large family are witnessed by one short factor. The answer is an infinite-parameter classification, not an arbitrary one-off numerical slice or mere recomputation of a known binary count.

## Limits and closest literature
The statement requires a full permutation period and its own initial-segment suffix. The binary full-period specialization was known; morphic fixed-point classifications and general suffix-tree checking algorithms do not directly enumerate the present position sets. A possible implicit earlier specialization remains a scientific originality risk.

Self-review: passed. Independent audit: not yet performed.
