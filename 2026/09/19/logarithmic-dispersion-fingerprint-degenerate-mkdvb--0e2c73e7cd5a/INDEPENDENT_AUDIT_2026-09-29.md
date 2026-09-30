# Independent audit — Universal logarithmic dispersion fingerprint in degenerate mKdV–Burgers shocks

**Audit date:** 2026-09-29 (UTC)  
**Source path:** `2026/09/19/logarithmic-dispersion-fingerprint-degenerate-mkdvb--0e2c73e7cd5a`  
**Audited tree:** `6b7f41eb20cf4b74357e9e48f50bf0cd8d7907b8`

## Disposition

**PASSED.** Correctness, originality on the stated narrow boundary, and scientific value all pass. The record may remain in the validated set.

## Correctness

**PASS.** The asymptotic coefficients check directly from the integrated profile equation. With v=s-U and q=U'=-v', the cubic flux defect gives 3 s v^2-v^3=mu q+kappa q q_v. Solving q=(3s/mu)v^2+bv^3+O(v^4) gives b=-1/mu-18 kappa s^2/mu^3. Thus y=1/v obeys y'=3s/mu-(1/mu+18 kappa s^2/mu^3)/y+O(y^-2), and the source's v comparable to xi^-1 estimate makes the remainder integrable after one bootstrap. This yields exactly the displayed logarithmic coefficient and, after inversion, mu^2/(27s^3)+2kappa/(3s). A fixed translation changes only the nonlogarithmic xi^-2 term, so the pairwise dispersion-comparison limit has the stated sign and coefficient.

## Originality

**PASS, with the limitations below.** The claim is properly separated from the center-manifold coefficient already present in arXiv:2609.20591: the audited contribution is the integrated exact leading coefficient, logarithmic correction, and translation-invariant dispersion-comparison limit. The 2026 source advertises two-sided degenerate-shock decay rather than this refined coefficient. Older literature, especially Jacobs–McKinney–Shearer (JDE 116, 1995), treats the same mKdV–Burgers traveling-wave equation; no accessible statement located gives the displayed logarithmic tail. A lawful full-text attempt through Oxford could not be completed because publisher verification required human action, so that paper was not claimed as read. This creates material residual priority risk, but accessible descriptions characterize it as traveling-wave existence/classification and no concrete overlapping theorem was found. On that narrow and explicitly qualified boundary, originality passes.

## Scientific value

**PASS.** The refinement identifies the first asymptotic order at which dispersion changes a degenerate shock whose leading tail is universal. The translation-invariant comparison law is stronger and more usable than two-sided decay bounds: it can inform refined profile matching, interaction estimates, and numerical far-field conditions. The result is modest in scope but scientifically substantive.

## Independent checks

- Re-derived the cubic coefficient in q(v) directly from the integrated traveling-wave equation.
- Converted to y=1/v and checked the logarithmic coefficient, inversion, and translation invariance.
- Checked the pure-viscous limit and the sign of the pairwise dispersion-comparison law.
- Attempted lawful full-text access to Jacobs–McKinney–Shearer (1995); the publisher flow required human verification, so no inaccessible text was treated as read.

## Literature and repository prior-art boundary

- https://arxiv.org/abs/2609.20591 — Eun–Han–Kim source for the monotone degenerate shock, two-sided tail control, and center-manifold expansion.
- https://arxiv.org/abs/2408.06801 — Purely viscous precursor used as a consistency boundary.
- https://doi.org/10.1006/jdeq.1995.1043 — Jacobs–McKinney–Shearer (1995), same mKdV–Burgers traveling-wave equation; full text was not accessible without human publisher verification during this run.
- https://doi.org/10.3934/dcdsb.2016078 — Later phase-plane/bounded-traveling-wave context citing the 1995 paper.

## Limitations

- Only the monotone degenerate right tail is treated; no oscillatory-regime or nonlinear-stability improvement is proved.
- Higher-order nonlogarithmic terms are not classified.
- Jacobs–McKinney–Shearer (1995), a directly relevant same-equation paper, could not be read in full because authorized publisher access required human verification; this is an explicit originality limitation.

## Repository identity

The assigned source-tree SHA `6b7f41eb20cf4b74357e9e48f50bf0cd8d7907b8` matched the current tree at the audited path after comparing the assignment inventory commit `e9ed144c13b7834896a844cc4f9cac3c25a168a6` with the source-tree checked commit `253a0fe5d0217455660a277f9adb940030e567ad`; none of the intervening changed files touched this record. GitHub was read only during the audit.
