# Independent audit — Prime plus two positive cubes below \(333334^3\)

Audit date: 2026-10-01 (UTC) UTC

## Final claim assessed

The scientific claim in `RESULT.md` and `SLOGAN.txt` was assessed unchanged.

## Correctness — PASS

The identity \(12(b^3-a^3)-3=(6t-3)^2\) and the floor condition give the finite bounds \(a\le6933\), \(b\le8735\). An independent exact C++ replay checked 36,531,779 pairs, found 7,683 integral first coincidences before the floor condition, 579 floor-admissible pairs, and zero triple-cube obstructions through \(t=333333\); a direct search through \(t=10000\) matched all 110 first-pair solutions. The residual bounds then place the third shifted remainder inside the source theorem's \(10^{12}\) range and above its finite exceptional set, yielding the advertised prime-plus-two-cubes extension.

## Originality — PASS

The finite exclusion and resulting range extension are absent from the primary source and other located records.

### Equivalent formulations
The endpoint theorem and the finite obstruction were searched separately. Evidence: Only the audited record matched both statements.

### Broader coverage
No inspected prior theorem dominates the new cutoff. Evidence: The source stops at \(10^{16}\) and leaves the triple-cube obstruction open.

### Exact database or table
The new certificate is not a known-table recomputation. Evidence: The source finite exceptional set is only an input; it does not contain the exhaustive new exclusion.

### Claim versus prior implication
The final range is not mechanically implied without the finite exclusion. Evidence: The source theorems extend the range only after excluding precisely the obstruction supplied by the new computation.

### Source inspections
- **Computational Results on Sums of a Prime with Squares or Cubes** — https://arxiv.org/abs/2609.20505. Trigger: Direct source for the prior range and obstruction. Material read: Relevant full-text theorem, corollary, exceptional-set, and triple-cube-conjecture statements. Assessment: The source stops at the earlier range and leaves the finite obstruction open. Evidence: The audited exact exclusion supplies the missing finite input.

Checked sources: https://arxiv.org/abs/2609.20505; https://github.com/kapplegate2020/Sums-of-a-Prime-with-Squares-or-Cubes; published scientific archive semantic search

Residual risks: Very recent source; simultaneous computational extensions may be unindexed.

## Scientific value — PASS

This is a meaningful finite cutoff attached directly to an explicit open bottleneck: it increases the verified representation range from \(10^{16}\) to \(333334^3\), a factor of about 3.70.

## Reproducibility

An independent exact C++17 replay reproduced 36,531,779 pair checks, 579 floor-admissible first-pair coincidences, zero triple-cube obstructions through \(t=333333\), and the 110/110 direct cross-check through \(t=10000\).

## Disposition

**PASSED.** The unchanged final claim passes correctness, originality, and scientific value.
