# Independent Audit — 2026-09-28

**Record:** `2026/09/10/037`  
**Title:** N4 has an F7-minus-fragile double-deletion pair (0,1)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `a2f03405bd5d7f563e77e02fd49fd163f7025cc4`  
**Disposition:** **PASSED**

## Independent checks

- Reimplemented ternary Gaussian-elimination rank from the published A4 matrix rather than invoking repository scripts.
- Enumerated the complete λ scan and independently enumerated F7-minus minor models on each deletion/contraction side.
- Compared the concrete claim against Brettell–Pendavingh and the 'excluded minors are almost fragile' theorem by hypotheses and conclusions, not by title similarity alone.

## Three-axis assessment

- **Correctness — PASS**: A fresh exact GF(3) reconstruction, independent of the filed finder/verifier code, recovered rank 8 for N4; min λ=2 for N4\0\1 over the complete subset scan; the stated F7-minus minor has rank 3, 29 bases and six 3-point lines, and the supplied permutation carries its bases exactly to the reference non-Fano model. Exhaustive deletion/contraction searches on all 14 remaining elements reproduced the six delete-only and eight contract-only rows exactly.
- **Originality — PASS**: The reviewed prior literature publishes the dyadic excluded-minor census and the 16-element N4, and separately gives an almost-fragile structural theorem with bounded/Δ–Y alternatives. Those actual statements neither name the pair (0,1), furnish the stated minor model, nor imply the complete 14-row fragility ledger; N4 lies at the size boundary where the general theorem does not force this concrete witness. Focused searches under N4/non-Fano/F7-minus/fragile terminology found no covering prior statement.
- **Scientific Value — PASS**: The record supplies a compact, exact, independently replayed fragile seed in the first beyond-census dyadic obstruction, with a concrete minor certificate and every one-element side classified. That is reusable structural data for the dyadic excluded-minor/fragility program rather than a bare numerical lookup.

## Sources compared

- Repository record 037 RESULT.md: https://github.com/SCOPE-Science/SCOPE2026/blob/main/2026/09/10/037/RESULT.md — Defines the exact N4 matrix, pair, minor certificate and 14-row fragility table audited here.
- Brettell–Pendavingh, Computing excluded minors for classes of matroids representable over partial fields: https://arxiv.org/abs/2302.13175 — Gives the dyadic excluded-minor census through 15 elements and exhibits the 16-element N4; it does not supply this concrete N4/F7-minus deletion-pair ledger.
- Brettell–Clark–Oxley–Semple–Whittle, Excluded minors are almost fragile: https://arxiv.org/abs/1603.09713 — Provides a general bounded-or-almost-fragile structural theorem with Δ–Y/dual alternatives, not the record's explicit pair/minor/table.

## Limitations

- The originality conclusion is a priority assessment against the located primary literature, not a claim that every unpublished computation or inaccessible source was searched.
- The independent computation audits the supplied labeled representation; isomorphic relabelings carry the result accordingly.

This audit is independent of the repository's pre-existing `AUDIT.json`. GitHub was read only as evidence; no repository changes were made by this audit run.
