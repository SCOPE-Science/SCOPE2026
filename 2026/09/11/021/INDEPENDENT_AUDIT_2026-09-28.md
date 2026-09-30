# Independent Audit — 2026-09-28

**Record:** `2026/09/11/021`  
**Title:** Joint inversion / minus-one census of diagonally symmetric ASMs of order 7  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `4e504014333ac273e744f507f411c25c8b947db8`  
**Disposition:** **PASSED**

## Independent checks

- Generated order-7 monotone triangles/ASMs and tested diagonal symmetry and statistics directly.
- Implemented equation (168) from BFK rather than invoking the repository xprs7_full.py.
- Compared the resulting trivariate polynomial and its I,M projection with the filed table.

## Three-axis assessment

- **Correctness — PASS**: Two independent exact routes reproduce the record. First, a monotone-triangle generation of all 218,348 ASMs of order 7 yields exactly 2,630 symmetric matrices and the stated 116 nonzero (I,M) cells, including the published marginals and absence of I=20. Second, evaluating Behrend–Fischer–Koutschan Theorem 20 directly at n=7, t=1 and s+=s-=s gives a 6×6 Pfaffian with 132 nonzero (P,R,S) monomials, total coefficient 2630, nonnegative coefficients and S-support {1,3,5,7}; projecting by I=2P+(7-S)/2 and M=R+(S-7)/2 reproduces the same 116-cell table exactly.
- **Originality — LIMITED**: BFK already provide the generalized five-statistic generating function and the Pfaffian formula that determines this specialization. The order-7 evaluated J_7 table was not located in the paper or focused searches, so the concrete census appears useful and not verbatim prior data, but conceptually it is a finite evaluation of a known exact formula rather than a new enumeration theorem.
- **Scientific Value — PASS**: The independently cross-checked 116-cell table is a compact benchmark for DSASM statistics and for implementations of the generalized Pfaffian. The value is chiefly as certified data and a consistency bridge between exhaustive enumeration and the BFK generating function, not as a new structural theorem.

## Findings

- Current main tree exactly equals the assigned source-tree SHA.
- Independent enumeration reproduced 218348 ASMs, 2630 DSASMs, all 116 J7 cells and both marginals.
- Direct coefficient extraction from BFK Theorem 20 reproduced 132 (P,R,S) terms and projected cell-for-cell to the stated J7.
- The result should be described as an evaluated specialization/census; BFK already supplies the general Pfaffian formula.

## Sources compared

- Repository record 021 RESULT.md: https://github.com/SCOPE-Science/SCOPE2026/blob/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/11/021/RESULT.md — Contains the 116-cell J7 table and claimed two-route verification.
- Behrend–Fischer–Koutschan, Diagonally symmetric alternating sign matrices: https://arxiv.org/abs/2309.08446 — Defines the generalized P,R,S+,S-,T generating function and gives the t=1 Pfaffian in Theorem 20; the current v2 is dated 2026-08-31.

## Limitations

- The originality is limited because the general generating-function formula already determines the finite table.
- The audit validates the n=7 specialization and exact enumeration; it does not re-prove the six-vertex/Yang–Baxter derivation of BFK Theorem 20.

This audit is independent of the repository’s pre-existing audit material. GitHub was read only as evidence; no repository changes were made by this audit run.
