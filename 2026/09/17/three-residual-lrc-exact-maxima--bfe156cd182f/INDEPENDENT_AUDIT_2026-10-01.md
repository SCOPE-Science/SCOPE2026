# Independent mathematical audit — SCOPE-20260917-bfe156cd182f

Audit date: 2026-10-01 (UTC) UTC.

Outcome: **PASSED**.

## Final claim assessed

Exact maxima for the three residual three-block LRC cases.

## Correctness

**PASS** — The locality-one partition lemma is valid without linearity: coordinates with the same symbol-partition form classes of size at least three, the representative map is injective, and changing one class changes every coordinate in that class. This gives the binary size bound 16 and ternary size bound 9. Independently enumerating the displayed binary 14-coordinate generator reproduced 128 distinct codewords and minimum distance 4, while the certified three-block bound is strictly below 256, so the maximum linear dimension is 7.

## Originality

**PASS** — Kang–Xiong explicitly leave exactly these three rows outside Corollary V.2; their Table V.1 gives the needed upper bounds but not the exact residual conclusions. Xia–Chen's locality-one characterization and Yang et al.'s binary construction cover ingredients, not the combined nonlinear exact maxima or the residual closure. Resultary search returned this record as the matching exact closure and no stronger earlier published result.

## Value

**PASS** — Closing all three named residual rows of a new finite-length LRC table is a natural completeness problem; two closures strengthen linear information to nonlinear maximum code size. This is a finite but motivated exact classification, not an arbitrary parameter slice.

## Source inspections

- **M.-H. Kang and M. Xiong, Linear Programming Bounds for Locally Recovery Codes II, arXiv:2609.16044v1 (2026).** Full text inspected, especially Table V.1 and Corollary V.2. The three assigned parameter rows are exactly the exceptions left outside the paper's exact linear-dimension conclusion. Consequence: The paper supplies the upper bounds but leaves the three residual exact maxima/dimensions unresolved.
- **Y. Xia and B. Chen, Complete Characterizations of Optimal Locally Repairable Codes With Locality 1 and K-1, IEEE Access 7 (2019).** Bibliographic record and the assigned paper's disclosed use were compared. Consequence: Covers linear locality-one construction context, not the nonlinear residual maxima proved here.
- **Resultary semantic search for the three exact residual LRC rows.** Search returned the assigned closure as the direct hit and no stronger earlier record implying all three conclusions. Consequence: No published Resultary coverage located; search failure is not used alone as novelty proof.

## Residual risks

- The binary nonlinear maximum for parameters \((14,4;2,2)\) remains outside the claim.
- Bibliographic records for some older construction sources were inspected less deeply than the full Kang–Xiong source; those sources are used only as acknowledged ingredients, not to establish novelty.

The accompanying JSON audit records the implication comparisons and exact coverage analysis in structured form.
