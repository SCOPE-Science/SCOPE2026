# Independent audit — 2026/09/15/033

**Date:** 2026-09-29  
**Disposition:** **REPAIRED**  
**Audited tree:** `acf55c7d0d9f9da25564ebb989bce237146a0489` at repository commit `253a0fe5d0217455660a277f9adb940030e567ad`

## Correctness

**REPAIRED** — The dimension-16 obstruction itself is real: the literal residual exponent recorded from Dodson’s Section 10 estimate is already below 2 at d=16 and decreases thereafter. But the filed record mixed that literal exponent with a different generalized cutoff-deficit formula and called the resulting threshold sharp. Expanding the generalized formula actually gives the exact condition delta <= (77-5d)/39 - 1/(10d), not merely (77-5d)/39 plus an unspecified correction. The broader claim that all Young-exponent tuning is impossible was also not established. The repair states only the method-local monotone-cutoff obstruction and cleanly separates the two formulas.

## Originality

**PASS_WITH_CAUTION** — Dodson’s theorem already stops at d=15. The record adds a transparent diagnostic identifying one exponent that crosses the absorption threshold at d=16, but it is an algebraic post-analysis of an existing proof rather than a new PDE theorem. No priority claim is made.

## Value

**PASS_WITH_CAUTION** — Pinpointing the precise term that fails at d=16 is useful when attempting to extend the rigidity argument, provided it is presented as an obstruction inside this particular cutoff/Young arrangement rather than as a universal impossibility theorem.

## Literature/evidence checked

- [Dodson, A determination of the blowup solutions to the focusing NLS with mass equal to the mass of the soliton](https://arxiv.org/abs/2106.02723): The source theorem proves minimal-mass rigidity in dimensions 2 through 15; the audit treats its Section 10 architecture as the fixed framework under analysis.
- [Annals of PDE version of Dodson’s paper](https://doi.org/10.1007/s40818-022-00142-5): Journal metadata confirms the same d<=15 scope.

## Limitations of this audit

Main-branch tree and blob guards were checked before staging and matched the assignment. Literature search is claim-specific and is not a proof of absolute priority. GitHub was read only; no repository writes were made. No inaccessible source is claimed as read.
