# Review: a 448-period quaternary orientable sequence of order five

**Correctness — PASS.** The exact 448-symbol witness is included verbatim; direct modulo-indexed and wraparound-window enumeration both give 448 distinct five-factors and 448 distinct nonpalindromic reversal classes. This establishes an orientable cyclic sequence of least period 448. The independent finite-program replay uses only the Python standard library; the result is a constructive lower bound and makes no unverified global optimality claim.

**Originality — PASS within examined literature.** Mitchell and Wild (arXiv:2603.18646, Table 4 and §6) report a previous best lower bound 404 and upper bound 452 for this exact parameter, discussing longer constructions as an open problem. Their earlier construction and Gabrić–Sawada's general method do not imply or exhibit the 448-period witness in the material compared. Scientific-index searches for quaternary orientable sequences, order-five reversal-avoiding cycles, the numbers 448/404/452, and equivalent de Bruijn formulations found no stronger published covering statement. Earlier unindexed or later undiscovered constructions are residual risks; failed search is not uniqueness proof.

**Value — PASS.** This concrete verified witness closes 44 of the 48 positions between the latest documented construction and published upper bound (91.7% of that gap). Orientable sequences are studied as position-sensing codes; narrowing a named extremal small parameter to 448–452 is a meaningful finite contribution, not merely a program-size change or a generic restatement.

**Limits.** No upper bound sharper than 452, classification, or all-parameter theorem is asserted. Independent audit has not been performed.

Self-review: passed. Independent audit: not yet performed.
