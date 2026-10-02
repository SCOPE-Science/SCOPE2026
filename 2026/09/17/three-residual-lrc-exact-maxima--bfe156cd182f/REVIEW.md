# Review status

Fresh independent mathematical audit completed on 2026-10-01 UTC.

Outcome: **passed**.

- Correctness: **PASS** — The locality-one partition lemma is valid without linearity: coordinates with the same symbol-partition form classes of size at least three, the representative map is injective, and changing one class changes every coordinate in that class. This gives the binary size bound 16 and ternary size bound 9. Independently enumerating the displayed binary 14-coordinate generator reproduced 128 distinct codewords and minimum distance 4, while the certified three-block bound is strictly below 256, so the maximum linear dimension is 7.
- Originality: **PASS** — Kang–Xiong explicitly leave exactly these three rows outside Corollary V.2; their Table V.1 gives the needed upper bounds but not the exact residual conclusions. Xia–Chen's locality-one characterization and Yang et al.'s binary construction cover ingredients, not the combined nonlinear exact maxima or the residual closure. Resultary search returned this record as the matching exact closure and no stronger earlier published result.
- Value: **PASS** — Closing all three named residual rows of a new finite-length LRC table is a natural completeness problem; two closures strengthen linear information to nonlinear maximum code size. This is a finite but motivated exact classification, not an arbitrary parameter slice.

See `INDEPENDENT_AUDIT_2026-10-01.md` and `INDEPENDENT_AUDIT_2026-10-01.json` for the complete source comparison, residual risks, and structured implication analysis.
