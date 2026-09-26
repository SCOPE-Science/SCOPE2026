# Independent audit — 2026-09-22

Record: SCOPE-20260909-020. Examined 2026-09-26 against the current default branch.

## Correctness — PASS
Fetched the committed binary `artifacts/reps32.pkl` through the GitHub connection as base64 (SHA-256 `219d890bea90a749ed4109492270e8601f36a99d1c4134dd534f9a46821e9466`). The shipped verifier returned `VERIFY_OK`: 51 full multiplication tables, associativity, invariants and within-signature non-isomorphism checks. I separately implemented multiplication-table group operations, all 32³ associativity triples for every table, subgroup closure of commutators and squares, lower central series, center, conjugacy orbits, element orders, and quotient-derived size. Every field in all 51 table rows agrees. Class frequencies are 7,26,15,3 for classes 1–4; the 44 nonabelian quotient-derived frequencies are 35 of size 2 and 9 of size 4. The three maximal-class witnesses have class 4 and the order-32 class bound is 4. Completeness uses the external classification count of 51 and the separately checked distinctness; the verifier does not reconstruct all central extensions.

## Originality — PASS, narrowly
The GAP Small Groups Library already catalogs all 51 groups and exposes individual invariants; the group count, maximal class bound, and elementary lower bound on nonabelian class-2 quotient are not new theorems. The checked GAP manual and Becker–Becker paper do not provide this exact per-group joint class/derived/center/Frattini/conjugacy/γ₃/quotient-derived table with reproducible local multiplication tables. Originality is the integrated, independently replayable finite census, not either elementary extremal alone. No mapping of local g0–g50 to SmallGroup IDs is supplied.

## Scientific value — PASS, bounded
The exact 51-row joint table can serve as a checkable base case for computations concerning order-32 groups; marginal counts and two elementary extrema alone would have limited value. The uncertified automorphism ranking is explicitly excluded from the result. The missing GAP cross-identification and reliance on the known 51-class count limit reuse and completeness independence.

Sources checked: [GAP SmallGrp manual](https://gap-packages.github.io/smallgrp/doc/chap1_mj.html); [Becker and Becker, arXiv:0911.3682](https://arxiv.org/abs/0911.3682). Evidence: original `RESULT.md`, `artifacts/reps32.pkl`, `artifacts/table.json`, `artifacts/verify.py`, and independent recomputation described above.
