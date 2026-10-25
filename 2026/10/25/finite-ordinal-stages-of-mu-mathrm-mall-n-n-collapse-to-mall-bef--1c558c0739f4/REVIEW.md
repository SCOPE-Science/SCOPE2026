# Review

## Correctness

PASS. The finite-stage translation is defined by induction on finite annotations and formula structure. The least-fixed-point rule is matched by finite additive disjunction, and the greatest-fixed-point rule by finite additive conjunction. The translated sequent is an ordinary MALL sequent, whose cut-free proof search terminates. The \(\alpha=\omega\) complexity statement is exactly the \(\alpha=\omega\) specialization of Theorem 2.8 in the cited primary source.

## Originality

PASS on the searched literature and database evidence. The primary 2026 source establishes the transfinite classification for \(\alpha\ge\omega\) but does not state the finite-stage collapse as a theorem. The 2023 comparison paper focuses on non-wellfounded and \(\omega\)-branching systems. Three targeted literature-database queries returned no equivalent claim; the closest records concern different objects. The result is a finite-boundary corollary, so the residual risk that it is regarded as folklore is explicit.

## Value

PASS. The statement completes the boundary at the first infinite branching ordinal: all finite stages admit effective elimination to MALL, while the first infinite stage has a hyperarithmetically complete theoremhood problem. This distinguishes a genuine change in proof-search structure from a mere change of notation.

## Closest literature and limitations

The closest primary source is Das–Pshenitsyn (2026), arXiv:2602.10280; the related earlier source is Das–De–Saurin (2023), DOI 10.4230/LIPIcs.FSTTCS.2023.40. No optimal complexity bound is claimed for the finite-stage algorithm. Independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
