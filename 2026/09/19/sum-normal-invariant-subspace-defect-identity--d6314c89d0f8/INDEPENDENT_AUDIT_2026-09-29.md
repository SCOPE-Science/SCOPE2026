# Independent audit — 2026-09-30

Record: `2026/09/19/sum-normal-invariant-subspace-defect-identity--d6314c89d0f8`  
Assigned and audited source tree: `261e354791748bc2ba5b900ce9a89a9bab3f5a11`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `e56d3fdd641b73251b22e3bb73aac4b580d361da`  
Disposition: **passed**

## Correctness

**independently_supported**. The block-compression identity is exact: for T_j=[[A_j,X_j],[0,B_j]], the M-compression of [T_j*,T_j] is [A_j*,A_j]-X_jX_j*, hence D_A=P_M D_T|_M+sum_j X_jX_j*. Positivity therefore passes from a sum-hyponormal tuple to its invariant restriction. If D_T=0, D_A=sum X_jX_j* and the restriction is sum-normal exactly when every X_j=0, i.e. the subspace reduces every coordinate. In finite dimension, D_A is positive with trace zero, so it vanishes and every finite-dimensional invariant subspace is reducing. The bilateral-shift/Hardy-space example independently confirms failure of blanket sum-normal inheritance already for d=1. The record correctly confines the downstream source issue to the auxiliary invariant-restriction argument rather than the separately proved main decomposition theorem.

## Originality

**qualified_source_specific_correction**. Invariant versus reducing subspaces for normal operators and the block calculation itself are classical. The current Chavan–Reza–Sequeira preprint is a September 2026 source on sum-hyponormal tuples, and targeted current searches found no public correction matching this exact defect identity and its application to the source's invariant-restriction assertion. Originality is therefore accepted only for locating and repairing that source-specific statement and tracing its consequence; no novelty is claimed for the classical single-operator phenomenon.

## Scientific value

**meaningful_targeted_correction**. The identity gives the exact obstruction omitted by the blanket inheritance claim and prevents a false use of sum-normality along invariant flags, while preserving the valid sum-hyponormal inheritance and the source's independently proved main theorem. That makes the correction scientifically useful despite its elementary proof.

## Literature and evidence checked

- https://arxiv.org/abs/2609.19287
- https://doi.org/10.1017/prm.2021.68
- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/19/sum-normal-invariant-subspace-defect-identity--d6314c89d0f8
## Limitations

- The block identity is elementary and classical in spirit; novelty is source-specific.
- The audit does not challenge the source's separately proved main compact-tuple decomposition theorem.
- The source is very recent, so an unindexed author correction or parallel note cannot be excluded.
