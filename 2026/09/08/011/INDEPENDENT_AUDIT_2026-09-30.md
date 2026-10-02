---
audit_date: 2026-09-30
status: passed
---

# Scientific audit

## Final claim

For intersecting 3-uniform hypergraphs on n=9,10,11,12,13, the maximum diversity is n-3, and every non-star has minimum degree at most 3; both bounds are attained by the two-out-of-three triangle family.

## Correctness — PASS

A fresh constraint search fixed one edge without loss of generality and independently explored all triples intersecting it. For diversity threshold n-2 it returned UNSAT for n=9..13 with 9,975; 19,550; 35,204; 59,331; and 95,093 search nodes. For non-star minimum degree at least 4 it returned UNSAT with 15,919; 68,485; 274,505; 1,010,124; and 3,410,894 nodes. The explicit two-out-of-three family was checked to have size 3n-8, maximum degree 2n-5, diversity n-3, and minimum degree 3.

**Evidence.** artifacts/div_solver.py blob 41fa11795508d3599ef30d7f1bc5a2c2147f8159; artifacts/verify.py blob 0e88c754dc2c384a646eff2b25986b2e0cab3900

**Residual risk.** The proof is finite exhaustive computation for the five stated n, not an infinite-n theorem.

## Originality — PASS

Kupavskii records Frankl's diversity conjecture for n>3k and proves it only for n at least a sufficiently large constant times k; later large-n work likewise does not settle this exact k=3 small window, and n=9 lies on n=3k rather than n>3k. Searches also found modern work linking diversity and minimum degree asymptotically, but no exact n=9..13 table or the stated minimum-degree star threshold.

- Equivalent formulations: Checked diversity as family size minus maximum degree, and minimum-degree/star formulations.
- Broader coverage: Large-n diversity theorems and asymptotic beta-parameter results are broader in n but do not imply these five exact small cases.
- Exact database or table: No published small-n table covering both invariants was found.
- Claim versus prior implication: The large-n theorems have hypotheses not verified for n=9..13 and therefore do not imply this table.
- Sources inspected: https://arxiv.org/abs/1709.02829; https://arxiv.org/abs/2304.11089; https://arxiv.org/abs/2501.02596
- Residual risk: A specialized exhaustive catalogue of small intersecting triple systems could contain equivalent data under a different invariant name.

## Value — PASS

The window begins at the natural Frankl threshold n=3k for k=3 and records the first exact cases immediately above it, while simultaneously locating the non-star minimum-degree threshold. This is a motivated finite cutoff/base-case result.

**Context.** Frankl diversity conjecture context; recent diversity/minimum-degree unification work

**Residual risk.** The value is as an exact base-case table; no uniqueness classification of extremizers is claimed.

## Disposition

PASSED. Acceptance requires PASS on correctness, originality, and value.
