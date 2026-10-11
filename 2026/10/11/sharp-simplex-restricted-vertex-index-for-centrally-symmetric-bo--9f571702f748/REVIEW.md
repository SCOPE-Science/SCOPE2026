# Review

## Correctness
**PASS.** The proof uses the positive barycentric coordinates \(\lambda_i\) of the origin in a circumscribing simplex. The opposite ray to vertex \(p_i\) hits the opposite facet at \(-\lambda_i p_i/(1-\lambda_i)\), giving the exact simplex gauge \(\|-p_i\|_P=(1-\lambda_i)/\lambda_i\). Since \(K=-K\subset P\), this is a lower bound for \(\|p_i\|_K\). Summation and the reciprocal Cauchy inequality give \(d(d+1)\). For \(K=\Delta-\Delta\), the centered-simplex identities \(-a_i/d\in\Delta\) and the linear barycentric functional \(L_i\) prove both containment in \((d+1)\Delta\) and the exact vertex norms \(d\). The bundled exact-arithmetic checker independently replays both mechanisms.

## Originality
**PASS, with an older-Minkowski-asymmetry residual risk.** Bezdek--Litvak state the same numerical lower bound only for a simplex circumscribing a Euclidean ball, and separately conjecture the unrestricted three-dimensional value \(12\) on the tetrahedral difference-body family. Their full text does not state the arbitrary symmetric-unit-ball simplex theorem. Gluskin--Litvak prove the unrestricted \(2d\) lower bound and a general average-asymmetry estimate for \(d+k\)-vertex polytopes, but the stated \(d+1\)-vertex bound is weaker than the present exact value. Exact and alias searches under vertex index, circumscribing simplex, Minkowski gauge, average asymmetry, and simplex difference body found no implication-equivalent theorem. The remaining risk is that the barycentric lemma may have appeared under older asymmetry terminology.

## Value
**PASS.** The result resolves the smallest possible outer-vertex regime of a named vertex-index problem, not an arbitrary restriction. It proves that the conjectured cost \(12\) for the three-dimensional \(T-T\) family is already forced and attained among tetrahedral outer approximants; any counterexample to the unrestricted equality must therefore use at least five outer vertices. In every dimension it also gives the sharp simplex-restricted vertex-index constant and a canonical equality family.

Same-model review: passed. Independent audit: not yet performed.
