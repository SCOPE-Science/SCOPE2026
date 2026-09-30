# Review status after independent-audit repair

The original same-model review passed the mathematics but accepted an originality framing that is not sustainable after repository-level comparison. The independent audit of 2026-09-29 found an earlier SCOPE record, `2026/09/17/steinberg-covering-number-for-pgln--e3667d632f22`, published at 2026-09-17T23:23:16Z, that already proves the same universal Steinberg-cube theorem and exact 2/3 covering exponent for PGL_n(q).

## Correctness

**PASS.** The proof in this record is mathematically sound. Monteiro--Stasinski provide every nonlinear center-trivial irreducible in the Steinberg square. Self-duality puts the trivial character in the square. For every nontrivial center-trivial linear character lambda, the twist lambda St is an irreducible distinct from St, so lambda is absent; hence the square defect is exactly the nontrivial linears. If chi were absent from the cube, then chi St would be supported only on those d-1 linears. Each such linear constituent has multiplicity at most one, so chi(1)St(1)<=d-1, contradicting St(1)>=q>d-1. The PGL_2(2)=S_3 exception is direct. The twisted GL_n(q) central-character-fiber corollary follows by tensoring with a linear character.

## Originality correction

**REPAIRED.** The 2026/09/17 SCOPE record has repository precedence for the universal cube and exact 2/3 exponent. The present record must therefore not describe those conclusions as a separate discovery. What remains distinct and useful is the explicit statement that every nontrivial linear is missing from the square, the short degree-obstruction proof of cube universality, and the twisted central-character-fiber corollary. The corrected RESULT.md, METADATA.json, SLOGAN.txt, and AUDIT.json make that status explicit.

The main external input remains Monteiro--Stasinski, arXiv:2609.17319. The 2013 Steinberg-square theorem for simple groups is prior background. No claim is made that the short exact-defect argument or the twist corollary has broad priority over all older literature.

## Scientific value

**PASS after reframing.** As a corroborating/refining record, the alternate proof is valuable: it gives an especially short quantitative obstruction for the cube and isolates the complete square defect. The GL_n(q) twisting statement packages the higher powers by central-character fiber. The value is expository and confirmatory relative to the earlier SCOPE theorem, not first-discovery priority for the 2/3 exponent.

## Limitations

- The exact 2/3 covering exponent and universal cube duplicate the earlier SCOPE result.
- The square-support refinement depends on the very recent Monteiro--Stasinski nonlinear-coverage theorem.
- No new tensor-product multiplicities are computed.
