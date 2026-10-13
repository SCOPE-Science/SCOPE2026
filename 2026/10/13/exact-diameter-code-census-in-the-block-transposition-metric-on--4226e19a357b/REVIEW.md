# Review of Exact diameter-code census in the block-transposition metric on \(S_5\)

## Correctness
PASS. The metric is reconstructed from all \(20\) block transpositions on \(S_5\). Exhaustive maximal-clique enumeration and an independent four-clique enumeration agree on exactly \(540\) maximum codes of size \(4\). The symmetry, orbit, subgroup, and coset statements are checked directly by `verify.py`.

## Originality
PASS. The closest primary source records the same \(n=5\) distance distribution and the full automorphism-group order \(1440\), but its inspected full text does not contain a code/packing/independence/max-clique classification. Exact-parameter and equivalent-formulation searches did not locate a result implying the \(540\)-code census, the two orbit sizes, or the \(120\)-coset split. The remaining risk is an obscure or unindexed finite census.

## Value
PASS. Minimum distance \(3\) is the diameter of this metric on \(S_5\), making the equality case a natural extremal problem rather than an arbitrary parameter slice. The complete two-orbit classification and the separation of \(120\) cyclic-coset maxima from \(420\) non-coset maxima provide structural information not contained in the published distance table.

## Closest literature and limitations
The main comparison points are arXiv:1410.8166v1 and arXiv:1504.02157v1. The latter supplies the published distance row and full automorphism-group order used to identify the constructed \(1440\)-element isometry subgroup as the full group. The result is only for \(S_5\); no claim for larger symmetric groups is made.

Self-review: passed. Independent audit: not yet performed.
