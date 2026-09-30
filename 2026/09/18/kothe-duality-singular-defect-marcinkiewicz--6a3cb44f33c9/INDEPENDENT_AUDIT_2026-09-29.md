# Independent audit — Köthe duality erases the singular defect in Huang's logarithmically monotone examples

**Audit date:** 2026-09-29 (UTC)
**Source path:** `2026/09/18/kothe-duality-singular-defect-marcinkiewicz--6a3cb44f33c9`
**Audited tree:** `c784c44c05d9c2610699bb391bbe04cbbe96df14`

## Disposition

**PASSED.** The record survives independent review on correctness, originality, and scientific value without a substantive research-file change.

## Correctness

The associate-space identities and distance statement are correct. Since the singular seminorm vanishes on bounded finite-measure-support truncations, the N_lambda unit ball contains all such truncations of every ambient unit-ball element. Monotone convergence therefore gives the reverse inequality to the immediate unit-ball inclusion and proves equality of the associate norms isometrically. The same truncation argument works for X=ker Phi. The Fatou property of the standard Marcinkiewicz norm then identifies the biassociate with E. Finally, seminorm subadditivity gives ||g-x||_E >= |Phi(g)-Phi(x)|=1 for x in X, while x=0 attains equality; any Köthe functional vanishing on X vanishes on all bounded finite-support tests and hence has zero representing function.

### Independent checks

- Proved the renormed associate identity in both directions: N_lambda>=||.||_E gives one inequality, and bounded finite-support monotone truncations with N_lambda=||.||_E give the other by monotone convergence.
- Repeated the same truncation argument for X=ker Phi, which contains every bounded finite-support function because Phi vanishes there.
- Used the standard Fatou property of M_psi and Lorentz--Luxemburg to identify E^{times times}=E isometrically, hence both claimed biassociates.
- Checked dist_E(g,X)=1 from |Phi(g)-Phi(x)|<=Phi(g-x)<=||g-x||_E and ||g||_E=1.
- Checked that a Köthe-represented functional annihilating X must annihilate characteristic functions of finite-measure sets and therefore be represented by zero almost everywhere.

## Originality

PASS as a source-specific consequence, not as a new general duality principle. The full 11-page v1 of Huang's July 2026 preprint was independently retrieved and inspected. It proves that Phi vanishes on bounded finite-support functions, gives the exact Phi-values of f and g, and constructs N_lambda and X=ker Phi, but it does not discuss Köthe associates, biassociates, the distance of g to X, or localization of the separating functional in the singular/non-Köthe dual. The truncation lemma, Lorentz--Luxemburg theorem, Fatou-space theory, and existence of singular functionals are classical and explicitly excluded.

### Literature checked

- https://arxiv.org/abs/2609.20270 — Jinghao Huang, A logarithmically monotone symmetric norm which is not fully symmetric, arXiv:2609.20270v1. Full 11-page preprint independently inspected; it supplies Phi, N_lambda, X, and the explicit f,g values but no Köthe-duality conclusions.
- https://www.sciencedirect.com/book/9780080874788/interpolation-of-operators — Bennett--Sharpley, Interpolation of Operators; standard associate-space, Marcinkiewicz, Fatou, and Lorentz--Luxemburg theory is prior art.

## Scientific value

The result gives a clean structural diagnosis of the two new counterexamples: their pathology is completely invisible to integral/Köthe duality and disappears under biassociation, yet in the kernel example the missing explicit unit vector is maximally far from the closed ideal. This sharply separates Köthe and singular Banach-dual information in a concrete current construction.

## Limitations

- The general truncation lemma is elementary prior theory and is not itself a novelty claim.
- The result concerns Köthe/associate duals and biassociates, not a classification of the full Banach dual or its singular part.
- Because Huang's motivating examples are recent, unindexed parallel observations remain a residual originality risk.

## Publication guard

The current source tree on `main` matched the assignment tree exactly during this audit. This guarded change-set adds only the independent-audit evidence pair and updates the independent-audit channel in `VERIFICATION.md`; the Lean and expert-attestation channels are preserved unchanged.
