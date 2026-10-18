# Scientific review

## Correctness — PASS

A period partitions indices into equal-letter residue chains. With exactly two marked positions, such chains force precisely two cases: singleton chains creating a terminal interval of periods, or one length-two chain creating an isolated period. The proof enumerates the allowable positions for each case, rigorously identifies the one overlapping class, and counts both distinct profiles and singleton classes; an exact residue-six evaluation yields the quadratic quasipolynomial. Independent direct bitwise period checks cover every weight-two word through length 100 plus seeded large-length spot tests. The computational test has no role as a substitute for the infinite proof.

## Originality — PASS, with literature residual risk

Rivals–Rahmann's general 2003 period-set recurrence and Rivals–Sweering–Wang's 2022/2023 unrestricted period-set asymptotic are close foundations. Their inspected formulations do not specialize to a fixed two-marker support, do not imply the finite six-residue formula by themselves, and give no classification of singleton observation fibers. Rivals' 2024 incremental algorithms address unrestricted period sets. Targeted literature searches and semantically similar research-record comparisons did not expose an equivalent result. General fixed-composition period-set results may be hidden in older or poorly indexed literature, including the not-fully-accessible *Periods and binary words* (2000); this is a genuine residual risk rather than evidence of uniqueness.

## Mathematical value — PASS

The precise period profile is a natural autocorrelation observation of a sparse sequence, and its reconstruction ambiguity matters for the information carried by a period signature. The all-length classification exposes both an isolated-gap mechanism and a nontrivial arithmetic six-period correction to the number of possible signatures. The singleton classification determines exactly when that observation identifies the two-marker word, a property not available from the total count. The result concerns exactly two ones and does not promise extensions or applications beyond that scope.

Self-review: passed. Independent audit: not yet performed.
