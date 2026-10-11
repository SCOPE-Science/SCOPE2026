# Review of the sharp rank-eight banded-gerbe theorem

## Correctness — PASS

For the mapping torus with monodromy \(f^*(u)=v\) and \(f^*(v)=-u\), the integral degree-two difference matrix has Smith entries \((1,2)\); the degree-four action is \(-1\). The Wang sequence consequently gives \(H^2=H^4=0\) and \(H^3=H^5=\mathbb Z/2\). The invariant modulo-two class restricts to \(\bar u+\bar v\), and its Pontryagin square restricts to \(2uv\) modulo four. Because restriction injects on degree-four mod-four cohomology and \(H^4(N;\mathbb Z)=0\), the integral Bockstein of this square is nonzero. Its quotient indeterminacy vanishes. Antieau--Williams Theorem A therefore gives exact twisted index four, and Becerra--Lupercio Theorem 7.5 gives actual minimum regular rank eight. Integral Poincaré duality ensures rank at most eight for any closed nonorientable five-manifold. The known three-dimensional gerbe times a sphere and a trivial gerbe realize minima four and two.

**Critical inputs:** Wang sequence for mapping tori, Pontryagin-square integral-lift identity, twisted period--index formula in dimensions at most six, and twisted-bundle Stiefel realization. The supplied checker independently recomputes the finite arithmetic but does not establish these general mathematical theorems.

## Originality — PASS, with stated residual risk

The closest primary text (Becerra--Lupercio, arXiv:2610.02555v1, Proposition 7.6) proves an **upper** bound eight but specifically says it does not know whether an order-two gerbe over a closed nonorientable five-manifold attains this bound. The manuscript provides an explicit smooth manifold and nonvanishing obstruction, filling precisely that gap. Antieau--Williams supplies the *general* cohomology-operation formula, not the computed mapping-torus example. Crowley--Grant supplies a different six-dimensional construction of index eight; it does not dominate the index-four, dimension-five claim. Meaning-level and monodromy-alias searches did not reveal another published example. A previous upper bound, even if stated for a larger class of orbifolds, does not imply attainment. Unindexed equivalent examples remain a residual possibility; a failed search by itself is not novelty proof.

## Value — PASS

This gives a sharp geometric realization at a natural dimension and isotropy threshold explicitly left open by the primary paper, and completely identifies the minimum-rank spectrum \(\{2,4,8\}\) in the constant banded-gerbe setting. The mapping-torus construction exhibits a genuine secondary period--index obstruction beyond the primary period-two condition. This is not a restatement of the published upper bound or a routine computation of an arbitrary slice.

## Scope and limits

The free locus is empty. This proof does not resolve the separate mixed-stabilizer problem (Becerra--Lupercio Question 10.2). Exact proofs depend on the published general index and realization theorems; no independent validation is represented.

Same-model review: passed. Independent audit: not yet performed.
