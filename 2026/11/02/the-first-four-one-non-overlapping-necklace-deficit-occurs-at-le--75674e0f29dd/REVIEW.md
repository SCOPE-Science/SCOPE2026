# Scientific review

## Correctness

PASS. Every claimed maximum for length at most eleven has an explicit code meeting the primitive-rotation-class upper bound. At length twelve, an explicit code has 39 words and an independently checkable six-class obstruction reduces the 40-class upper bound to 39. Each of 1296 possible transversals is tested by the defining two-way prefix-suffix condition, and all six five-class subfamilies are separately certified feasible. The standalone package checker returned `VERIFY_OK`; the proof reduces each finite assertion to exhaustive, simple integer/string comparisons.

## Originality

PASS, with residual historical-priority uncertainty. The 2012 Chee–Kiah–Purkayastha–Wang paper gives unrestricted constructions and bounds. Blackburn's 2013 study provides unrestricted bounds and constructions. The fully inspected 2024 characterization of maximal non-overlapping codes is not an evaluation of the weight-four problem, and the inspected 2025 polarity-balanced tables specialize to half-positive content rather than length-twelve weight four. No inspected source states the six-necklace impossibility or the exact weight-four first deficit. General algorithms for arbitrary non-overlapping codes do not imply the numerical result without specializing and solving the constrained instance. Unindexed specialized tables remain a risk.

## Value

PASS. Primitive necklaces offer a natural synchronization-code packing ceiling, but attainment is a stronger property. The first strict failure at weight four and length twelve, after sharpness at every shorter length, is a motivated boundary; the irredundant six-necklace obstruction supplies a compact structural reason rather than only a numerical optimum. The exact witness and exhaustive certificate provide a reproducible benchmark for sparse composition-constrained synchronization codes.

## Limits

The statement is finite and fixed-weight. No pattern for larger blocklengths or other weights is asserted. A self-review is not independent certification, and historical priority is qualified.

Self-review: passed. Independent audit: not yet performed.
