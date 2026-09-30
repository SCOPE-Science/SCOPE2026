# Independent Audit — Eliminating the dimension-24 Type-II exception in the Knutson classification

**Audit date:** 2026-09-30 (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `8852fe1a7ea9012bce0b1e0308287102407bfbff`  
**Audited current source tree:** `8852fe1a7ea9012bce0b1e0308287102407bfbff`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` directory tree exactly matches the assigned source-tree SHA. GitHub was used only as read-only evidence. The dated independent-audit marker files were absent when this guarded change set was prepared.

## Correctness — PASS

PASS. Martín Duro’s Type-II case for module structure (1^2,2,3^2) has both one-dimensional modules fixing each three-dimensional simple. Thus the stabilizer of such a simple has order 2. Natale–Plavnik explicitly record the Nichols–Zoeller consequence that, for an irreducible character chi of a semisimple Hopf algebra, |G[chi]| divides (deg chi)^2. Applying it to a three-dimensional simple gives 2|9, impossible. If the published action is read on the right, dualizing converts it to a left stabilizer of the dual three-dimensional simple. Hence Type II cannot occur, and Martín Duro’s remaining case analysis yields the unconditional dimension-at-most-31 conclusion.

## Originality — PASS

PASS, narrowly scoped. The current 2024 journal text still states Corollary 2.32 with exactly the dimension-24 Type-II exception and explicitly describes the trivial action of both one-dimensional modules in that case. Targeted searches for a correction, erratum, dimension-24 Type-II elimination, and the stabilizer obstruction found no prior public correction. The stabilizer divisibility theorem is classical and receives no novelty credit; originality is only the short application that removes the published sole exception.

## Scientific value — PASS

PASS. Although the proof is brief, it changes a published low-dimensional classification from “all cases except one possible Type-II action” to an unconditional theorem through dimension 31. Eliminating the unique exception is scientifically useful, and the record correctly frames the contribution as a correction/application rather than a new Hopf-algebra stabilizer theorem.

## Independent checks

- Read the current journal text of Martín Duro’s paper at Corollary 2.32 and the full dimension-24 (1^2,2,3^2) Type-I/Type-II split; the Type-II premise used by the record is explicit there.
- Verified in Natale–Plavnik that Nichols–Zoeller gives |G[chi]| dividing (deg chi)^2 for irreducible semisimple-Hopf characters.
- Rechecked the left/right tensor convention: U tensor g congruent U implies g^{-1} tensor U* congruent U* after duality, so the contradiction is convention-independent.
- Targeted searches found no later correction or equivalent published elimination of this Type-II exception.
- The current main directory tree SHA exactly equals the assigned source-tree SHA; the 2026-09-30 audit markers are absent and VERIFICATION.md retains blob SHA 31a3bb079c3be0cdcbee536377edadb1613bf629.

## Limitations

- The conclusion inherits the hypotheses and all non-exceptional case analysis of Martín Duro’s classification.
- The general stabilizer-divisibility theorem is old; the originality claim is only the application to the published exceptional action.
- Because the correction is short, an unindexed note or private author correction remains the main residual priority risk.

## Evidence and references

- https://doi.org/10.1016/j.jalgebra.2024.06.021
- https://arxiv.org/abs/2211.08123
- https://arxiv.org/abs/1103.2340
- https://doi.org/10.2307/2374514
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/20/knutson-dimension-24-type-ii-exception-impossible--fc9ef1319daf

This guarded change set updates only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
