# Independent audit — 2026-09-29

Record: `2026/09/17/finite-center-generalized-derivation-norm-formula--12706865018e`  
Assigned and audited source tree: `3e3d1dffdf0a26f91b33526850e80047ea4b1d8b`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Disposition: **passed**

## Correctness

**supported**. The finite-center extension is mathematically consistent with the Huang-Pliev-Sukochev-Xu factor formula. The upper estimate follows by applying the factor uniform-submajorization bound summandwise, iterating the finite direct-sum submajorization lemma with arbitrarily small total loss, and then using Russo-Dye. For the lower estimate, the factor partial isometries can be chosen independently in each central summand; finite disjoint-union rearrangement commutes with the common dilation, giving the global lower bound and the limit N->infinity. The two-summand rank-one test is exact: for a=(p,0), b=(0,-p), the Schatten-q norm of the derivation is 2^(1/q), while forbidden global cross-center matching would give 2.

## Originality

**qualified_natural_extension**. Huang-Pliev-Sukochev-Xu (2026) provide the exact self-adjoint factor formula and a positive-operator non-factor theorem, explicitly framing the self-adjoint non-factor problem as subtler. Targeted searches did not locate this finite-atomic-center center-local formula. Older Fialkow/Fialkow-Loebl work is important prior background, so the audit accepts only the record's already qualified 'best of our knowledge' claim for the finite-center synthesis and does not assert broad priority.

## Scientific value

**meaningful_structural_extension**. The result identifies exactly how the recent factor formula survives on a non-factor algebra and gives a minimal obstruction showing why naive global sign pairing fails. The finite-center restriction is real, but the theorem and counterexample clarify the boundary of the current general theory.

## Literature and evidence checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/17/finite-center-generalized-derivation-norm-formula--12706865018e
- https://arxiv.org/abs/2609.15233
- https://doi.org/10.1016/j.aim.2026.110964
- L. A. Fialkow, A note on norm ideals and the operator X -> AX-XB, Israel J. Math. 32 (1979), 331-348.
- L. A. Fialkow and R. Loebl, Elementary mappings into ideals of operators, Illinois J. Math. 28 (1984), 555-578.

## Limitations

- The theorem is restricted to finite direct sums of infinite type-I factors and self-adjoint compact implementers.
- The audit did not claim to have read inaccessible complete text of Fialkow (1979); originality remains deliberately qualified.
- The argument does not establish an analogous formula for infinite atomic centers.
