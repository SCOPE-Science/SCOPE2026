# Independent Audit — 2026-09-30

**Record:** `2026/09/19/square-class-completion-graded-involutions-m2--162d7332757e`  
**Title:** Square classes complete the order-two elementary involutions on M2(F)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `b26993404b09d5c6a5c527cbfcbbcd55df184dfe`  
**Disposition:** **PASSED**

## Three-axis assessment

- **Correctness — PASS:** PASS. The classification follows directly from the graded anti-automorphism constraints. If the two diagonal primitive idempotents are fixed, anti-multiplicativity forces e12*=a e21 and e21*=a^{-1}e12. If they are swapped, the off-diagonal matrix units are eigenvectors and involutivity plus e12e21=e11 forces the common sign ±1. A graded automorphism normalizing the neutral diagonal algebra is monomial: diagonal conjugation changes a by a square and the coordinate swap sends a to a^{-1}, so the exact invariant is the square class. The scalar-extension argument for graded *-identities is valid in characteristic zero; centrality can also be phrased as the identity [f,x]=0, so it is preserved and reflected under scalar extension. Thus the omitted sigma_a forms have the same graded *-identity and central-polynomial spaces after descent.
- **Originality — PASS:** PASS, with a material version-history qualification. The current public abstract of arXiv:2609.20488 still states an arbitrary characteristic-zero field and claims all G-graded involutions, whereas the cited Bahturin–Zaicev classification is explicitly over an algebraically closed field of characteristic different from 2. The square-class/discriminant classification itself is standard and is not novel; the defensible contribution is the explicit correction of the arbitrary-field formulation together with the PI-equivalence observation. A metadata mirror reports an update on 18 September 2026, but the accessible public text did not expose a revised theorem statement, so this audit does not claim that an inaccessible/current full version was checked line by line.
- **Scientific value — PASS:** PASS. The record identifies a genuine missing family over fields such as Q, gives the exact replacement classification for the affected branch, and sharply limits downstream damage by proving that the omitted forms are PI- and central-PI-equivalent to the transpose representative. This is a useful correction even though its structural ingredient is classical.

## Independent findings
- Direct matrix-unit computation reproduces exactly the sigma_a and rho_± families.
- Monomial graded conjugacy changes a only by a square and/or inversion, and inversion preserves the square class.
- Over Q, a=2 supplies an explicit class not represented by ±1.
- Central-polynomial invariance can be reduced to ordinary identity invariance through commutators, avoiding a hidden descent gap.

## Independent checks
- Re-derived the two idempotent-action cases and the parameter constraints from anti-multiplicativity.
- Checked the diagonal and antidiagonal normalizer actions on sigma_a and on the rho sign.
- Checked scalar-extension preservation/reflection of graded *-identities and centrality.
- Compared the recent paper's public field hypothesis with Bahturin–Zaicev's algebraically closed hypothesis.

## Literature evidence
- https://arxiv.org/abs/2609.20488 — Current public abstract: characteristic-zero F and a claim to consider all G-graded involutions on M2(F).
- https://arxiv.org/abs/math/0609417 — Bahturin–Zaicev; public abstract states the algebraically closed, characteristic-not-2 hypothesis.
- https://doi.org/10.1016/j.jalgebra.2006.10.046 — Published Bahturin–Zaicev classification.
- https://doi.org/10.1016/j.jalgebra.2023.11.002 — Related central-polynomial background for second-order matrices with graded involution.

## Limitations
- The audit covers only the order-two elementary-grading branch stated in the record, not the Klein-group branch or all arbitrary-field gradings.
- The square-class classification is classical discriminant theory; originality is only in applying it as an explicit correction/completion and in the PI-equivalence consequence.
- A public metadata mirror reports an arXiv update on 18 September 2026, but no accessible full revised theorem text was available through the audited sources; no claim is made about text that could not be inspected.

The assigned source-tree SHA still matches the current record tree inspected on `main`. GitHub was used only as read-only evidence; no repository writes were made.
