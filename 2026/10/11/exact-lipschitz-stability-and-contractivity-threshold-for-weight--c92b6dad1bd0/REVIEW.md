# Scientific review

## Correctness — PASS
The generalized soft-threshold formula follows from strict convexity and the KKT conditions; fixing an active face makes the map affine with rank-one-corrected derivative. Every active subset genuinely occurs, so the finite maximum of linear operator norms is both necessary and sufficient. Differentiation on the kernel proves the complete nonexpansive classification. Hölder duality gives the exact planar factor. The standalone deterministic verifier passes 1,240 checks; numerical tests do not prove the infinite quantifiers.

## Originality — PASS, with residual risk
Duchi et al. (2008) cover Euclidean threshold projection, but not ambient \(\ell_p\)-metric Lipschitz stability for all positive weights. Kobos (2015) and Jamison--Kamińska--Lewicki (2004) cover linear norm-one projection obstructions. Denkowska (2013) and Kamińska--Lewicki (2004) present stronger general structural descriptions of contractive sets; these may subsume much of the qualitative obstruction, which is not separately presented as novel. The specific quantitative global Lipschitz modulus and sharp anisotropic planar constant were not found in inspected primary material or targeted searches. The full 2004 papers were not accessible and equivalent historical formulations remain a residual risk. Search incompleteness is not evidence of mathematical uniqueness.

## Value — PASS
Weighted cross-polytopes model coordinate-weighted sparse constraints; their nearest-point-map stability is a natural approximation invariant. The exact modulus covers every finite dimension and strictly positive weight pattern, provides a closed two-dimensional amplification factor, and precisely separates contractive from expansive parameter regimes. Its value is the complete quantitative sensitivity theorem, beyond a routine KKT calculation.

## Scope and remaining limitations
Real finite-dimensional \(\ell_p\) only, \(1<p<\infty\), with positive weights and radius. The higher-dimensional exact modulus remains an explicit finite optimization over matrix operator norms rather than a universal elementary closed form. General historical contractive-set theory remains the principal originality risk; a separate audit has not been performed.

Same-model review: passed. Independent audit: not yet performed.
