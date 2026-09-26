# Independent audit — 2026-09-22 campaign

**Record:** `2026/09/08/089`  
**Audited source tree:** `53f60816e676907b77606cc9bcb70763d6fd49b4`  
**Audit performed:** 2026-09-26 UTC  
**Disposition:** PASSED

## Correctness

PASS — Replayed Latin and overlay tests: A,B,C_pub are Latin, |AB|=|AC_pub|=100 and |BC_pub|=91. The separate exact-cover census yields 1080 transversals and 305 unlabelled A-mates with unique minimum B-deficit 9; B has 932 transversals and 5 unlabelled mates with unique minimum A-deficit 24. The published candidate C* is a symbol relabeling of C_pub, with deficit 9, not an improved triple. The census is exhaustive only for C orthogonal to A or to B; it says nothing about C nonorthogonal to both.

## Originality

PASS, qualified — Egan–Wanless supply the near-orthogonal order-10 triple and classify mates for orders at most nine, not these two fixed-pair order-10 mate strata. The candidate relabeling is not original; the 305/5 partition counts and their deficit distributions are the finite contribution. Their printed arrays were not independently transcribed from the PDF in this audit, so the result is tied to the committed arrays.

## Scientific value

PASS — The conditional minima and uniqueness delimit two concrete search strata of the 3-MOLS(10) problem and give reusable exact-cover benchmarks. They do not settle global three-square feasibility or a global deficit minimum.

## Prior work and source access

- https://arxiv.org/abs/1406.3681
- https://arxiv.org/abs/2605.02132

## Scope of the decision

The verdict concerns “Exact mate-stratum deficit boundary for the fixed Egan–Wanless order-10 pair” as written in `RESULT.md` and the committed package at the source tree above. Replayed computations and any limitations are identified in each axis; no inaccessible full text or global statement beyond the record's finite scope is treated as verified.
