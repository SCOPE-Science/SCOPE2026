# Independent audit — 2026-09-30

**Record:** `2026/09/09/043`  
**Audited source tree:** `f9128b2bd7254236fc77b25dc95ab03abb80a034`

## Correctness — PASS

The all-n replacement arguments are valid: in each of M0, M1, M2, M3, M5 and M6, a point occupying the shaded cell yields a new occurrence with a strictly improved lexicographic/minimality measure, so a minimal counterexample cannot exist. A fresh 120-order relative-order check reproduced all six replacement patterns and the two failing M4/M7 replacements. The two C implementations use materially different occurrence and shading tests; their committed logs agree on all 80 values through n=10, and the S5 witnesses explain the first M4/M7 separation.

## Originality — PASS

The six all-n coincidences themselves are applications of the pre-existing Shading Lemma: each shaded square is incident to a pattern point, so that component is covered by prior theory and is not counted as new. The surviving original content is the exact selected length-4 census, especially the M4 and M7 rows through n=10 and their finite-window separation/witnesses. Targeted searches and the length-2 classification literature inspected did not supply those exact length-4 rows or an implication that determines them. The PASS therefore rests on the census component, not on rebranding the Shading Lemma.

The comparison explicitly checked equivalent formulations, broader coverage, exact tables/databases, and whether prior results logically imply the final claim.

## Scientific value — PASS

After discounting the known shading-lemma coincidences, the record still gives exact, independently reproducible avoidance data for the two genuinely restrictive single-cell length-4 meshes in the frozen window, with first distinguishing witnesses and a quantified n=10 separation. That is a natural finite boundary datum for mesh-pattern enumeration; the record explicitly avoids claiming asymptotics or completeness of all length-4 single-cell meshes.

## Source inspections

- **Hilmarsson et al. — Wilf-classification of mesh patterns of short length** — Abstract plus the full Shading Lemma statement/conditions from the authors' presentation; the lemma page was visually inspected. The Shading Lemma adds an incident square without changing the avoidance class; it covers the six vacuous single-cell shadings here. https://arxiv.org/abs/1409.3165
- **Claesson, Tenner, Ulfarsson — Coincidence among families of mesh patterns** — Abstract and the generalized/simultaneous shading-lemma statements available in full-text excerpts. Broadens coincidence machinery but does not supply the M4/M7 length-4 avoidance rows. https://arxiv.org/abs/1412.0703
- **Su, Kitaev, Zhang — Equidistribution of mesh patterns of short length** — Abstract and scope. A 2026 near-complete classification for mesh patterns of length 2, not the selected length-4 meshes. https://arxiv.org/abs/2605.19429

## Residual risks

- The six all-n vacuous-shading equivalences are not novel; they are applications of the established Shading Lemma. Originality rests only on the selected finite census/witness component.
- The window W is not proved complete among all dihedral-reduced single-cell length-4 meshes, and no asymptotic separation is claimed.
- A targeted literature search cannot exclude an obscure unpublished table of the same M4/M7 counts.

## Disposition

**PASS.** The final claim passes correctness, originality, and scientific value without changing `RESULT.md` or `SLOGAN.txt`.
