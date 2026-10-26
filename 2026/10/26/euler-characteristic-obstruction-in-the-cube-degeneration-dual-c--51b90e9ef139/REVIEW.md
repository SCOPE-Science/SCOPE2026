# Review

## Correctness

PASS. The reported vector gives \(21-120+420-480+192=33\). A finite \(\Delta\)-complex homeomorphic to \(\mathbb{CP}^{2}\) has Euler characteristic \(3\); the two data cannot describe the same complex. The calculation is reproduced in `verify_euler.py`.

## Originality

PASS for the scoped consistency finding. published-finding corpus semantic searches using the exact arXiv identifier, face vector, Euler-characteristic formulation, and the \(\mathbb{CP}^{2}\) comparison returned no finding covering this precise incompatibility. The primary paper's Remark 3.1.2 and Theorem 3.3.1 were read and compared directly; the cited minimal-dlt theorem was also inspected. This is not a claim to have found the corrected face vector.

## Value

PASS. Euler characteristic is a necessary global invariant of a finite \(\Delta\)-complex. The discrepancy is numerically large and directly relevant to whether a newly computed dual complex has the stated topology. Resolving it is necessary before using the reported face vector as a model of \(\mathbb{CP}^{2}\).

## Closest literature and limitations

The closest source is Shafi–Tschanz, arXiv:2512.21190v1, whose Remark 3.1.2 gives the topological comparison and whose Theorem 3.3.1 gives the cube-degeneration counts. Kollár–Laza–Saccà–Voisin, arXiv:1704.02731, Theorem 0.11(ii), gives the rational-homology constraint under minimal-dlt hypotheses. The stack/minimal-dlt distinction remains a residual applicability risk; no corrected count or source of error is inferred.

Self-review: passed. Independent audit: not yet performed.
