# Independent audit — 2026-09-29

**Record:** `2026/09/18/gashkov-sidelnikov-deep-hole-multiplicity--160ef35008b2`  
**Title:** Uniform deep-hole leader multiplicity for ternary Gashkov--Sidel'nikov codes  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `0855a937eb022ba0ffb9ea24116dd4f05b138803`  
**Disposition:** **REPAIRED**

## Correctness

**PASS_AFTER_REPAIR** — The explicit bound is mathematically sound. I inspected all four conic branches in Shi et al.: each admissible first parameter has exactly two conic lifts, while a marked minimum leader determines the first branch coordinate and, outside the at-most-six-point exceptional set, forces the required character condition and nonzero-square discriminant. Hence 2A(S)≤|V(S)|≤2A(S)+12. The source character-sum expansion gives (q-3√q-28)/4≤A(S) and, because the deleted weighted terms are nonnegative and the three complete nonconstant sums have absolute values at most 1, 3√q and 3, also A(S)≤(q+3√q+4)/4. Together with |V(S)|=3M(S), this yields the filed discrepancy bound. Norm-orbit invariance is an immediate multiplication-by-T bijection.

## Originality

**PASS_AFTER_REPAIR** — The filed prior-work discussion was materially incomplete. The 1986 Gashkov–Sidel'nikov paper does not merely give an existence proof and weight spectrum: in its quasi-perfectness proof it explicitly counts solutions of the three-term conic system with a quadratic-character sum N centered at q+1 and error O(√q). This substantially anticipates the qualitative q/6+O(√q) leader-multiplicity scale. The repair withdraws novelty for that asymptotic and retains only the sharper explicit constant, marked-leader comparison, and norm-orbit formulation. The inspected 1992 Zetterberg decoder does not count all deep-coset leaders. The 1987 FCT paper was not accessible at theorem level and remains a priority caveat.

## Scientific value

**PASS_AFTER_REPAIR** — After reframing, the record remains useful as a quantitative sharpening: it turns the 2026 branchwise search-density estimate into a uniform nearest-neighbor multiplicity bound with an explicit leading √q constant 1/2 and a finite additive constant, and it isolates exact norm-class symmetry. The qualitative asymptotic itself is no longer presented as the contribution.

## Findings

- The inequality 2A(S)≤|V(S)|≤2A(S)+12 is valid in all four cyclic/constacyclic branches; the +12 term is exactly the at-most-six exceptional first parameters times two conic lifts.
- The complete weighted character sum also supplies the needed upper bound A(S)≤(q+3√q+4)/4 because every deleted exceptional summand is nonnegative.
- The 1986 source already contains a q+O(√q) count of the conic solution system used to prove quasi-perfectness, so the filed claim that older work supplied only existence/ordinary weight spectra is inaccurate.
- Dodunekov–Nilsson 1992 was obtained in full text through authorized Oxford access and contains an algebraic decision/location decoder, not the present all-leader multiplicity count.

## Independent checks

- Read arXiv:2609.20402 in full through the authorized text extraction, including the four branch lemmas and Remark 4.7.
- Inspected the open-access 1986 Russian full text and its displayed conic solution-count formula and 8√q discrepancy estimate.
- Inspected the complete four-page 1992 Zetterberg decoding paper through authorized Oxford access.
- Checked the q=9 archived exhaustive output and independently verified the counting identities algebraically.

## Sources

- https://arxiv.org/abs/2609.20402 — Shi et al. 2026: norm-one torus model, unique two-term decomposition, four conic decoding branches, and q/4+O(√q) admissible-parameter density.
- https://www.mathnet.ru/eng/ppi957 — Gashkov–Sidel'nikov 1986 open-access full text: quasi-perfectness proof includes a quadratic-character count N=q+1+O(√q) for the underlying three-term conic system.
- https://doi.org/10.1109/18.149509 — Dodunekov–Nilsson 1992: binary Zetterberg algebraic decoder; full text inspected, no all-leader multiplicity theorem found.
- https://dblp.org/rec/conf/fct/GashkovS87 — 1987 FCT conference paper located bibliographically; theorem text was not obtained.

## Limitations

- The 1987 FCT paper could not be inspected at theorem level; no claim is made about its exact contents.
- The audit does not claim the explicit constants are optimal.
- The repaired originality claim is for the sharpened explicit discrepancy and formulation, not for the q/6+O(√q) scale.

This audit is independent of the repository's pre-existing same-model review. GitHub was read only as evidence; no repository changes were made by this audit run.
