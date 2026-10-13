# Self-review

## Correctness
PASS. The proof handles every integer \(q\ge2\) and \(k\ge1\), with the binary and one-information-symbol boundaries stated separately. The one-check obstruction is a positive-affine collision of two constant-message codewords with equal orientation. The unrestricted length-three supply follows from an exact primitive-triple count, a coprimality union bound, and a Cartesian extension. The verifier independently computes gcd primitive forms and exact rational signatures for finite ranges; those computations corroborate, rather than replace, the quantified proof.

## Originality
PASS for the narrow combined exact systematicity-gap theorem. The 2015 Pearson-code paper already establishes the optimal unrestricted capacity and general canonical primitive representatives. The 2016 systematic-coding paper already gives the two-reference fixed-to-fixed construction. Neither inspected full text supplies the universal necessity of two check symbols for a full-message systematic encoder, and the capacity result alone does not imply it. Searches using fixed-to-fixed, single-parity, positive-affine and reference-symbol equivalent formulations found no encompassing statement. An unindexed exposition of this elementary obstruction is the material residual risk.

## Value
PASS. For the storage/communications setting with unknown gain and offset, the new theorem settles whether one can retain all information coordinates at the same whole-symbol overhead as an unrestricted Pearson encoder. The answer is sharply negative for all \(q\ge3\) and \(k\ge2\): the one-symbol penalty is uniform, and the exact exceptional cases are proved. This is a motivated systematic-versus-nonsystematic boundary, not a new optimum-size table or a claimed improvement of the already known two-reference construction.

Self-review: passed. Independent audit: not yet performed.
