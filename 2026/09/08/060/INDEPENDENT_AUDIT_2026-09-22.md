# Independent three-axis audit — 2026-09-24

Reviewer type: separate AI audit. This document records reproducible scientific checks and literature comparison, not a transcript of private reasoning.

## Audited source

- Record: `SCOPE-20260908-060`
- Source path: `2026/09/08/060`
- Inventory source tree: `8abfff5e932b06b517ef99080669404b0d826334`
- Audited `RESULT.md` blob: `738cf312992cfb46ecee6fd899b5e044ba243f46`
- Claim audited: exact ordered-integer point and Vieta-component censuses in the box `max(|x|,|y|,|z|)<=10^4` for `x^2+y^2+z^2=3xyz+k`, `k=0,1,2`, with explicit component roots and extremal branches.

## Correctness — PASS

The principal finite counts were independently regenerated from the defining Vieta involutions. Starting from the stated component roots, a fresh bounded flood applied

`(x,y,z)->(3yz-x,y,z)`, `(x,y,z)->(x,3xz-y,z)`, and `(x,y,z)->(x,y,3xy-z)`

while requiring the equation and the `10^4` box bound at every step. The component sizes reproduced exactly:

- `k=0`: `[1,118,118,118,118]`, total `473`;
- `k=1`: `[2,2,2]`, total `6`;
- `k=2`: `[120,120,120]`, total `360`.

The floods are pairwise disjoint within each `k`. Canonicalizing nonnegative points by coordinate sorting gives respectively 22, 1, and 16 sorted nonnegative triples, and the largest attained absolute coordinates are 9077, 1, and 6765, matching the record. Direct equation checks pass for every regenerated point.

The completeness argument is also sound in the audited range. For a nonnegative ordered solution `0<=x<=y<=z` with `z>=2`, the other quadratic root `z'=3xy-z` satisfies `zz'=x^2+y^2-k`. For `k=0,1,2`, the record's inequalities force `0<=z'<z`, except for the listed irreducible points in `{0,1}^3`; hence repeated descent stays inside the box and reaches a root. Sign cases with odd numbers of negative coordinates reduce to the finite `{-1,0,1}^3` exceptions, while two-negative solutions mirror nonnegative solutions. This supports completeness of the bounded floods, not merely their internal consistency.

## Originality — PASS relative to the literature checked

No checked source publishes this exact three-surface, height-`10^4`, ordered-point census together with box-component decomposition and logged Vieta paths. The classical `k=0` Markoff tree and its Fibonacci branch are longstanding prior art and are not novel here. More recent work, including Urzúa–Zúñiga, **The birational geometry of Markov numbers**, arXiv `2310.17957`, studies the classical Markoff equation structurally, while Alfaya et al., **Branches of Markoff m-triples with two k-Fibonacci components**, arXiv `2603.23306` (March 2026), studies special infinite branches of the generalized equation `x^2+y^2+z^2=3xyz+m`. Neither source found supplies the audited bounded census for `m=1,2` or the combined `k=0,1,2` box data.

Searches included the exact equations for `k=1,2`, the extremal coordinates `6765` and `9077`, height-`10000` census terminology, generalized Markoff/Markoff-Hurwitz literature, and Vieta-component language. The originality verdict is therefore relative to the literature checked.

## Scientific value — FAIL

After separating classical structure from the computation, the surviving contribution is a bounded census at an arbitrary height with 839 points total. It does not resolve Markoff uniqueness, classify generalized Vieta orbits in an unbounded setting, prove a new asymptotic, or derive a reusable structural theorem beyond the elementary descent argument already implicit in standard Markoff-tree methods. The `k=1` case is essentially finite and elementary, and the `k=0` data reproduce familiar initial Markoff branches. The `k=2` point list and path certificates are valid benchmark data, but a height-`10^4` cutoff by itself is not a meaningful new scientific regime under the campaign's value standard.

## Repair attempt

A bounded repair was considered by narrowing the record to the `k=2` census and its deepest branch. This remains a finite cutoff computation with no structural classification beyond the box and therefore does not restore sufficient scientific value.

## Final disposition

**FAILED** on scientific value; correctness passes and the bounded census is original relative to the literature checked. Scientific rejection evidence is published at the source record; archival relocation to the assigned failed-attempt path remains pending and does not affect the scientific verdict.
