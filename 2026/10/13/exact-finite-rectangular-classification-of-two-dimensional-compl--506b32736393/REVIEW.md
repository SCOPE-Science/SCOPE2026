# Review of rectangular difference-ruler census

## Correctness — PASS

For each of fifteen grids, every complete difference ruler must contain four corners. There are exactly \(2ab+a+b\) unoriented nonzero difference classes. The included source iterates all allowed point subsets from the resulting counting lower bound and discards a branch only if its uncovered classes exceed the maximum number of pairs future selected points can supply. A distinct Python implementation checks every supplied optimal witness against all signed vectors. The finite classification therefore follows from exact exhaustive exclusion and constructive coverage, with all computations reproducible from the embedded source. There is no claim that these finite checks establish arbitrary-size behavior.

## Originality — PASS (priority risk retained)

The motivating 2024 preprint defines the identical full difference-set problem in its Section 4 but supplies only general lower and asymptotic upper bounds. The 2018 planar additive-basis census optimizes a **sumset** and is not a table of planar **difference-set** minima. Comparisons were made under the equivalent names complete planar difference ruler, hole-free difference coarray, and minimum-redundancy sensor placement. No equivalent finite table was identified in the available full texts, index search, or previously recorded work. The 2016 planar difference-coarray source and a related 2018 engineering paper were not fully accessible, so published priority remains subject to checking their full contents. Absence from search results is not presented as a proof of novelty.

## Mathematical value — PASS

The exact 15-pair finite table resolves the natural smallest rectangular instances of the original two-dimensional ruler optimization invariant. In the \(6\times6\) case, the old pair-count bound gives only twelve marks; the new census proves fifteen are necessary and attainable, with explicit optimal placements. Natural exact values inform planar sparse-array and unbordered-domain questions, without asserting a more ambitious infinite-size theorem or unproved application.

## Scope and closest literature

The result concerns unlabeled integer grid difference bases, not labeled unbordered partial words; the primary invariant has one-based point-count dimensions, whereas the table uses endpoint spans. The 2018 sumset paper has superficially similar grids but does not imply the result. Unchecked engineering tables and unindexed equivalent work are residual risks, and the finite lower bound requires the supplied enumeration source.

Self-review: passed. Independent audit: not yet performed.
