# Independent Audit — Classification of extremal interval endomorphism global dimension

Audit date: 2026-09-29 (UTC)
Record path: `2026/09/17/extremal-interval-endomorphism-global-dimension--15e3312baa42`
Audited tree: `fd0190a45e5163d138d28c6e55d3e160ea6cbb16`

## Disposition

**PASSED** — All three audit axes pass, subject to the explicit qualifications below.

## Correctness

**PASS**. Aoki’s full preprint was inspected at Proposition 6.1, Theorem 6.5 and Corollaries 6.6–6.7. For a saturated pair of weight n-1, the identity |S∩C|+|P\(S∪C)|+(|C\S|-|Max(C\S)|)+(|S\C|-|Min(S\C)|)=1 is immediate, so exactly one defect is present. Re-deriving the four cases gives respectively a double star, the n=3 connected cases (already double stars), K_{2,n-2}, and its dual. The relative downset/upset and extremal-boundary conditions force the claimed edge directions and exclude extra comparabilities. Conversely, the displayed pairs in each listed family have W(S,C)={P}, hence are saturated of weight n-1. Aoki’s exact formula gldim Lambda_P=Omega(P) and the relative Auslander relation then give both equivalences and the enumeration 3,5,n+2.

## Originality

**PASS**. Aoki’s September 2026 v1 proves the sharp bound gldim Lambda_P<=n-1, gives a one-sided star extremizer, and supplies the saturated-pair formula, but the inspected paper does not classify all equality cases. Targeted searches for equality/extremal classifications using the double-star and K_{2,n-2} descriptions found no matching prior result. The audited theorem is therefore a new-looking equality classification derived from, but not stated in, the source preprint.

## Scientific value

**PASS**. The theorem upgrades a newly proved sharp bound from one example to a complete structural classification of every equality case, transfers it to interval-resolution global dimension, and counts all extremal isomorphism types. That is a natural and useful completion of the source theorem, with a short defect-one mechanism that is likely reusable in related extremal questions.

## Literature evidence

- https://arxiv.org/abs/2609.15927 — Toshitaka Aoki, Interval endomorphism algebras of posets (2026). Full PDF inspected, including Proposition 6.1, Theorem 6.5, and Corollaries 6.6–6.7; source proves the bound/formula but not the audited equality classification.

## Independent checks

- Read Aoki’s exact definitions of W(S,C), saturated pair, and omega-bar and independently redid each of the four defect-one cases.
- Checked the converse saturated pairs and the low-order overlaps in the isomorphism count.

## Limitations

- The underlying Aoki preprint is very recent, so a concurrent or subsequent equality classification could appear after the audited record.
- No claim is made that the saturated-pair formula or sharp n-1 bound is original to this record.

GitHub was used only as read-only evidence. The repository tree matched the assigned tree exactly.
