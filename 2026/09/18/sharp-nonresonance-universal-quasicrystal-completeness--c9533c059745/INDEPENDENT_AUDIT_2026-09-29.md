# Independent Audit — 2026-09-29

**Record:** `2026/09/18/sharp-nonresonance-universal-quasicrystal-completeness--c9533c059745`  
**Title:** Sharp nonresonance criterion for universal quasicrystal completeness  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `aa1255bb1f0b287117a1b8cff3b852666db50dd0`  
**Disposition:** **PASSED**

## Independent checks

- Checked the n versus 2n fractional-part identity that forces tau in Z.
- Checked that rational independence of 1,alpha_1,...,alpha_d excludes a nonzero relation mapping to v=0.
- Checked the one-dimensional exceptional formula beta=-1/(alpha+r), r rational.

## Three-axis assessment

- **Correctness — PASS**: Both directions of the phase-lock characterization are valid. An integer relation yields v=a-t alpha with v dot beta=t and a constant phase (-1)^t. Conversely, common phase implies A_n=v dot n+tau{n dot alpha} is integral; choosing n with fractional part above 1/2 and comparing n with 2n forces tau to be an integer, after which the coordinate tests give a=v+tau alpha in Z^d and recover the relation. The two-translate annihilator on E union (E+v) has Fourier transform zero on the entire frequency set and works on arbitrarily small positive measure.
- **Originality — PASS**: The current Bertolini--Florit-Simon--Liehr--Taylor preprint publicly states the universal-completeness construction and higher-dimensional extensions, while targeted searches found no public converse identifying the full common-phase translation group or proving a zero-scale obstruction under rational resonance. Older simple-quasicrystal sampling/Riesz-basis papers are adjacent but address different stability or bounded-remainder-set properties.
- **Scientific Value — PASS**: The result upgrades a sufficient arithmetic hypothesis into an exact obstruction for the new universal-completeness family: nonresonance gives the source theorem below measure one, while resonance creates annihilators on sets of arbitrarily small measure. The group formula gives a concrete harmonic-analytic mechanism rather than only a counterexample.

## Findings

- Current source tree exactly matches the assigned SHA.
- Independently checked the integer-relation/common-phase equivalence and injectivity of (t,a) -> a-t alpha.
- Independently verified the two-copy cancellation and its duality implication for every finite p.
- Fresh searches found no public source matching the converse or exact phase-lock group.

## Sources compared

- Bertolini, Florit-Simon, Liehr, Taylor, Universal completeness of exponentials: https://arxiv.org/abs/2609.20805 — Primary 2026 universal-completeness source; the positive higher-dimensional direction is inherited from it.
- Matei and Meyer, Simple quasicrystals are sets of stable sampling: https://doi.org/10.1080/17476930903394689 — Older adjacent stable-sampling result, not the present universal L1-uniqueness converse.
- Grepstad and Lev, Riesz bases, Meyer's quasicrystals, and bounded remainder sets: https://doi.org/10.1090/tran/7157 — Related arithmetic/Riesz-basis theory; no matching exact phase-lock obstruction was located.

## Limitations

- The positive half of the dichotomy is imported from the primary source and retains its norm bound ||beta||_2<1/2.
- The result concerns uniqueness/completeness, not quantitative frame or Riesz-basis constants.
- The source preprint is very recent, so unindexed contemporaneous observations remain possible.

This audit is independent of the repository’s pre-existing audit material. GitHub was read only as evidence; no repository changes were made by this audit run.
