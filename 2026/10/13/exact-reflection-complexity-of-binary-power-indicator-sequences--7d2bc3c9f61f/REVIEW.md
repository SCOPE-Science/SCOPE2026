# Scientific review

## Correctness — PASS
The proof is self-contained: gap uniqueness partitions all factors with at least two ones, long zero gaps supply the zero/one-one cases, strictly increasing successive gaps exclude reverse mates for factors with at least three ones, and symmetric interval counting handles all reversible two-one factors. Summing these exact counts gives the displayed formula, including the only exceptional short boundary palindrome. The uniform scaled profile proves both accumulation bounds. The standalone verifier uses direct factor enumeration, independent of the counting derivation, over bases 2–7 and lengths 1–140. Its finite checks corroborate, rather than replace, the infinite proof.

## Originality — PASS, qualified by priority uncertainty
Allouche et al. (arXiv:2406.09302, §§1,3,8) prove general computable regularity and calculate famous automatic examples, but do not give the exact geometric-power indicator formula or its two accumulation slopes. Krawchuk–Rampersad (2018) count cyclic-conjugacy classes in other sequences, not these reversal classes. Dvořáková–Pelantová (2026) develop general characterization results, not this computation. Targeted searches for geometric-power indicators, reversal complexity, closed formulas, and equivalent descriptions did not identify stronger coverage. An unindexed or implicit equivalent computation remains a priority risk; search absence does not establish uniqueness.

## Mathematical value — PASS
The result evaluates a natural uncomputed automatic word in the invariant explicitly introduced in the 2024 study. It completely determines reflection complexity on every base and length, and exposes a sharp dichotomy: convergence at base 2, persistent oscillation with exact extrema for every higher base. The result is not merely a finite table, renaming, or an immediate specialization of the known regularity theorem.

## Scope and limitations
No extension to other sparse supports is proved. The calculation is not a historical priority certificate. The code checks finite examples only; complete proof is mathematical.

Self-review: passed. Independent audit: not yet performed.
