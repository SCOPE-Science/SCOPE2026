# Review: Grassmann distance degree \(18\) for \(S(2,3)\)

## Correctness — PASS

The model is the smooth rational-normal-quintic ruling curve of \(S(2,3)\) inside \(\operatorname{pGr}(2,7)\). A rank-two symmetric idempotent witness is constructed explicitly, rather than using an unrestricted symmetric matrix. A standard-library exact-arithmetic program verifies that its derivative numerator has degree \(18\), is squarefree, does not meet the fixed denominator, and does not meet the algebraic cut locus. The upper bound \(18\) follows for any matrix from the common denominator of degree \(10\); nonvanishing discriminants imply the witness's count persists for generic projection data. The polynomial certificate was run successfully.

## Originality — PASS (with residual literature risk)

The closest primary paper is Friedman--Hoşten--Rosana, arXiv:2610.02018, Theorem 2.2: it establishes the ED degree \(18\) of this ruling curve, for **unrestricted** symmetric-matrix data. Definition 4.2 restricts the data to rank-two projections and discards the cut locus; Section 4 does not evaluate the scroll's GD degree. Its Theorem 4.4 describes a general *expected* agreement, not the present equality proof. The earlier Friedman--Rosana--Sturmfels arXiv:2601.22843 introduces GD for lines but does not name scrolls in its searchable full text. A published mathematical record on flat limits of line-distortion scrolls involves the same surface \(S(2,3)\) but studies a different degeneration invariant. Targeted search found no implied or identical GD classification; this is not a proof of absolute publication priority.

## Value — PASS

The GD degree counts stationary fits when the observation itself is a line, a different and geometrically constrained optimization problem from the ED degree. Existing examples show GD can differ sharply from ED, so the source's ED formula does not settle GD. The scroll \(S(2,3)\) is the first nonuniform rational normal surface scroll after the balanced case, making its exact value a natural baseline for further scroll optimization. The exact equality and an explicit data witness settle that invariant without claiming a general all-scroll theorem.

## Boundaries and residual risks

The proof concerns the algebraic projection/chordal distance and complex generic points, not intrinsic geodesic distance or the maximum number of real stationary rulings. No all-scroll statement is claimed. An unindexed equivalent argument in broader Grassmannian optimization literature remains possible; full inspection of every older source is not asserted. The analysis is not independent validation.

Self-review: passed. Independent audit: not yet performed.
