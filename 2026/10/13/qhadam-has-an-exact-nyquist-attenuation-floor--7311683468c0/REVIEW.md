# Review

## Correctness

PASS. The alternating first moment is an exact geometric sum, and bias correction produces a parity law: every even step is already at the limiting momentum ratio while odd steps approach it from above. Constant squared gradient makes the bias-corrected second moment exactly \(G^2\), so the entire quasi-hyperbolic second-moment interpolation collapses to the same value. The sharp floor follows by differentiating the limiting first-moment factor.

Risk: the theorem is an input-response statement rather than a fixed-objective convergence result.

## Originality

PASS. The defining QHAdam paper gives the two immediate-discount mixtures, the stale-momentum interpretation, general update bounds, and parameter sweeps, but the inspected full text does not state the alternating-input parity law or exact erasure of the second-moment parameters. Focused published-record searches found no implication-equivalent result.

Residual risk: an equivalent short frequency-response derivation may exist in unindexed notes.

## Value

PASS. The result assigns a precise highest-frequency role to both QHAdam immediate discounts. It proves that the first-moment discount sets a sharp attenuation floor \(1-\nu_1\), while the second-moment discount cannot alter this structured response at all. This directly sharpens the source paper's qualitative distinction between stale first moments and second-moment update control.

Self-review: passed. Independent audit: not yet performed.
