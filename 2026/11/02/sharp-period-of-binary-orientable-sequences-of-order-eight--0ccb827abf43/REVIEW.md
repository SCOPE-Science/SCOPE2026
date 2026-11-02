# Scientific assessment

## Correctness

**PASS.** Every qualifying cycle yields zero-one variables on the 240 nonpalindromic eight-bit factors, satisfies reversal-pair inequalities and seven-bit flow balance, and obeys an additional proved local identity at the 16 palindromic seven-bit vertices. An explicit nonnegative integral dual certificate gives the upper bound 92; the standard-library checker verifies all 240 coefficient inequalities, its total weight 92, and the local identity. A cyclic witness has 92 distinct nonpalindromic reversal classes. The argument is finite, exact, and does not extrapolate from experiments.

## Originality

**PASS, subject to bibliographic uncertainty.** Gabrić–Sawada (CPM 2024, Table 1 and Section 4) gives precisely the prior interval 92 to 96, and its construction/extension does not prove the missing upper bound. Mitchell–Wild (2021/2022) is a recursive lower-bound construction, and the later Mitchell–Wild nonbinary work does not resolve the binary order-eight optimum. The distinction is between a previously known 92-position construction and a newly certified sharp global upper bound. The 1993 source chapter was not inspected in full, but its 96-position bound is described in the later full primary papers. Unindexed priority claims remain possible.

## Mathematical value

**PASS.** Exact optimization at the first unresolved binary order eliminates a genuine four-position extremal gap in orientation-sensitive position-location sequences. The argument also exhibits a useful local consequence of reversal exclusion—opposite-bit transitions through palindromic states—and supplies an economical, reproducible dual bound instead of a solver-only numerical assertion. No arbitrary parameter slice or routine table recomputation is needed for the motivation.

## Closest literature and limitations

The closest references are Gabrić–Sawada 2024 (Table 1: order eight, 92 constructed, 96 upper), Mitchell–Wild 2021/2022 (recursive sequences), Dai et al. 1993 (original upper bound), and Mitchell–Wild 2025/2026 (generalized nonbinary constructions and bounds). This result determines only the binary order-eight maximum, not a general order-dependent capacity or classification of all maxima. The full 1993 chapter was unavailable for direct inspection; an equivalent obscure earlier argument has not been ruled out.

Self-review: passed. Independent audit: not yet performed.
