# Review of the rank-two quaternary distortion threshold

## Correctness

PASS. The projective-weight dictionary recovers the zero-column count and the five column multiplicities from the Hamming weights. The faithful actions \(\mathrm{PGL}_2(2)=S_3\), \(\mathrm{PGL}_2(3)=S_4\), and \(\mathrm{PGL}_2(4)=A_5\) prove both field and blocklength thresholds. Distinct nonnegative quaternary multiplicities require ten positions. For the constructed family, the identity and odd-permutation lower bound agree at \(\bigl((4t+10)/(4t+9)\bigr)^2\). Direct enumeration of all invertible two-by-two maps checks six parameter instances; the proof, not the enumeration, handles all parameters.

## Originality

PASS with residual risk. Bennett--Fox--Morrell (2026, arXiv:2607.26261, DOI: 10.4230/LIPIcs.APPROX/RANDOM.2026.24) introduces distortion and universal algorithms but does not identify this projective parity threshold or compute the infinite family. Bouyukliev--Bouyuklieva--Kurz (2020) treats projective codes under a larger equivalence group *including field automorphisms*. Their convention identifies the two examples and cannot imply the strict monomial distortion value. Indexed mathematical records include examples of equal Hamming enumerators with inequivalent higher-dimensional codes, but not this quaternary first-threshold and exact distortion law. An unindexed projective-line computation remains a possible overlap.

## Value

PASS. Distortion is newly motivated as a quantitative refinement of linear code equivalence. The result gives the earliest failure of Hamming-spectrum completeness within all rank-two quaternary codes, proves the small-field rigidity boundary, and computes an exact near-unit metric gap for an unbounded family. The distinction between field-linear and semilinear equivalence matters: the same example has no gap under the latter convention. The theorem is a sharp structural metric result, not a routine table entry or a numerical improvement without context.

## Limits and closest prior literature

The phenomenon is specific to dimension two and strict field-linearity. It supplies no hardness theorem, decoding guarantee, or higher-dimensional classification. Classical equivalence classifications often allow field automorphisms, so comparisons must preserve the same equivalence group. An independent audit has not been conducted.

Self-review: passed. Independent audit: not yet performed.
