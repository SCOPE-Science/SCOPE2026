# Independent Audit — 2026-09-28

**Record:** `2026/09/10/048`  
**Title:** General linear Jordan longest part exactly 7 in socle degree 6  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `087523569194acbb15f3c855e35152df6408d02f`  
**Disposition:** **PASSED**

## Independent checks

- Expanded the apolar action independently and checked the factorial evaluation identity.
- Checked the open-set/genericity step and the nilpotency-index-to-largest-Jordan-block equivalence.
- Compared the claim with current Jordan-type survey and Lefschetz literature.

## Three-axis assessment

- **Correctness — PASS**: The proof is exact. For F homogeneous of degree 6 and L=Σa_i x_i, the apolar action gives L^6∘F=6!F(a). Since F is nonzero over an infinite characteristic-zero field, F(a)≠0 on a nonempty Zariski open set, so multiplication by a general L has L^6≠0 while L^7=0 in the socle-degree-6 algebra. Hence the nilpotency index, and therefore the largest Jordan block, is exactly 7. This directly excludes the target’s “longest part ≤6” clause.
- **Originality — LIMITED**: The argument is an elementary consequence of standard Macaulay inverse-system/apolarity identities and the definition of Jordan nilpotency. The retrieved Jordan-type literature supplies the surrounding framework but does not appear to state this exact target-refutation lemma verbatim. The audit therefore treats priority as limited rather than claiming a new general theorem.
- **Scientific Value — PASS**: As a diagnostic result it is useful: it cleanly shows that the proposed socle-6 target was internally inconsistent and isolates exactly which clause must be removed, while leaving WLP failure and strict dominance below H^∨ open. The value is corrective/methodological rather than a deep new classification theorem.

## Findings

- Current main tree equals assigned SHA.
- The multinomial/apolar identity L^6∘F=720F(a) was independently checked symbolically.
- General nonvanishing follows from F≠0 and infinitude of the field; A_7=0 gives the matching upper bound.
- The conclusion does not rule out WLP failure at H=(1,4,6,8,6,4,1) with a 7-block.

## Sources compared

- Repository record 048 RESULT.md: https://github.com/SCOPE-Science/SCOPE2026/blob/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/10/048/RESULT.md — States the apolar identity and target refutation audited here.
- Altafi–Iarrobino–Macias Marques, Jordan type of an Artinian algebra, a survey: https://arxiv.org/abs/2307.00957 — Provides the standard Jordan-type/Lefschetz framework and interpretation of Jordan strings in Artinian algebras.
- Gondim, On higher Hessians and the Lefschetz properties: https://arxiv.org/abs/1506.06387 — Provides standard apolar Artinian-Gorenstein/Lefschetz context; it does not contradict the elementary nilpotency-index argument.

## Limitations

- Originality is deliberately rated limited: a one-line consequence of standard apolarity should not be marketed as a major new theorem merely because an exact phrase was not retrieved.
- Characteristic zero/infinite field is essential to the stated proof; no claim is made in characteristics dividing 6!.

This audit is independent of the repository’s pre-existing audit material. GitHub was read only as evidence; no repository changes were made by this audit run.
