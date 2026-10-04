# Same-model review

## Correctness
PASS. The proof reduces the linear lower-tail minimization under an integer-mean constraint to truncated geometric laws using the published half-space extreme-point theorem. For each reduced law the mean is strictly increasing and the lower-tail probability strictly decreasing in the geometric parameter. The remaining finite family for support cardinality at most seven is exhausted by exact rational sign certificates in `verify.py`; the eight-point witness is certified by the same method. Decimal approximations are not used in the proof.

## Originality
PASS. The lead paper explicitly gives an eight-point log-affine counterexample to the \(1/2\) bound and supplies the localization mechanism, but its inspected introduction and proof do not state that eight points are minimal. Targeted searches for the support-seven/eight cutoff, truncated-geometric integer-mean median bounds, and the lead example did not return an equivalent indexed finding or a published statement of this cutoff. The main residual risk is an unlocated later paper or note containing the same finite-support observation.

## Value
PASS. The lead paper singles out the failure of the natural half-mass-at-the-mean strengthening and gives an eight-point example without locating the first support size where failure is possible. Determining that the displayed support size is minimal gives a natural exact boundary, explains why smaller discrete log-concave models retain the stronger inequality, and converts an illustrative counterexample into a sharp structural cutoff.

The closest literature and scope limitation are described in RESULT.md. The result does not claim a best constant for each support size or classify all eight-point failures.

Same-model review: passed. Independent audit: not yet performed.
