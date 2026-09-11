# Certified rank-1 correction at the mod-5 Moore-space Adams cell (3,50)

## Context
The admitted program studies 5-primary Moore-space phenomena (Toda/Cohen–Moore–Neisendorfer
unstable-to-stable transfer, Moore exponents, v1-periodicity) via the classical mod-5 Adams
spectral sequence. The target bracket witness and the preset fallback shared one E2 premise:
Ext^{3,50} on P^3(5) is 2-dimensional with basis {a,b} and d_2(a)=0, d_2(b)=c≠0.
The computation below decides that premise.

## Definitions
- p=5. Dual Steenrod algebra A_* over F_5 with |ξ_1|=8, |ξ_2|=48, |τ_0|=1, |τ_1|=9, |τ_2|=49.
- P^3(5): mod-5 Moore spectrum/space, desuspended V(0)=cof(5:S^2→S^2); H_*(P^3(5);F_5) has
  bottom cell e2 (degree 2, primitive) and top cell e3 (degree 3) with reduced coaction
  ν̄(e3)=[τ_0]⊗e2.
- Normalized cobar complex C^s(t)=Ā_*^{⊗s}⊗H_*(P) in internal degree t; Ext^{s,t}=H^s(C^*(t)).
  (s,t)=(3,50) is stem t−s=47, filtration 3 — the detector cell fixed by the bracket degrees.
- Convention: simplicial-sign cobar differential (validated by d^2=0; see Evidence).

## Result
For H_*(P^3(5);F_5) over the mod-5 dual Steenrod algebra, in the normalized cobar complex:
1. **Ext^{3,50} is 1-dimensional (not 2).** C^3(50) has dim 10, rank(d:C^3→C^4)=6 (ker dim 4),
   rank(d:C^2→C^3)=3, so dim H=4−3=1. Survivor: k0=[1,2,2,1,0,0,0,0,0,0] in the logged
   C^3(50) basis; the other kernel vectors k1,k2,k3 are boundaries (augmented-rank test gives
   image-membership [False,True,True,True]).
2. **Ext^{5,51}=0.** C^5(51) dim 400, rank_out=327, rank_in=73, so H=0; every Adams d_2 out
   of (3,50) is automatically 0.
3. **Ext^{3,51} is 1-dimensional;** all other computed cells in s≤5, stems 44–48 vanish
   (notably C(4,51): 134→400, ranks 73/61, H=0; C(2,50): H=0).
4. **Consequence.** The admitted rank-2 cocycle basis {a,b} with d_2(a)=0, d_2(b)=c≠0
   (shared premise of the target bracket witness and the preset fallback as stated) is
   **impossible at E2 level**: only one class exists where two were required, and the d_2
   target group vanishes.

## Proof / evidence (replayable computation)
- Scripts: `output/artifacts/ext_cobar.py`, `output/artifacts/save_cell.py`.
- Certificate: `output/artifacts/cell_3_50.json` (domain bases, kernel bases, augmented-rank
  image-membership).
- Replay: `python3 output/artifacts/ext_cobar.py moore` (window s≤5, stems 44–48),
  `python3 output/artifacts/ext_cobar.py anchors` (sphere/Moore anchors),
  `python3 output/artifacts/save_cell.py` (cell certificate).
- Validation (independently re-ranked at audit): d^2=0 (D_{next}·D_{prev} nnz=0) at
  (2,50),(3,50),(3,51),(2,51),(4,51); Milnor coproduct formulas as coded; no dropped
  cobar targets in-window (count 0); anchors sphere Ext^{1,8}=F_5 (α_1 cell) and Moore
  Ext^{0,2}=F_5 correct.
- Independent cross-check: cofiber LES S^2→S^2→P with ×5=0 splitting; separately computed
  sphere cells Ext^{3,47}(S)=0, Ext^{3,48}(S)=1 (same code) give dim Ext^{3,50}(P)=0+1=1,
  agreeing with the direct Moore cobar.
- (3,50) bases: C^3(50) gamma-degree triples on e2 —
  [8,8,32],[8,16,24],[8,24,16],[8,32,8],[16,8,24],[16,16,16],[16,24,8],[24,8,16],[24,16,8],
  [32,8,8] (pure ξ_1-powers); C^2(50): [8,40],[16,32],[24,24],[32,16],[40,8].
  Survivor k0=[1,2,2,1,0,0,0,0,0,0] satisfies D@k0=0 and is non-boundary.

## Limitations
- E2-level result (plus automatic d_2-vanishing from Ext^{5,51}=0). No Moss-convergence,
  Toda-juggling, or indeterminacy claim for the single surviving class; no bracket
  nontriviality/vanishing claim.
- Convention-dependent (simplicial-sign cobar, stated comodule coaction as above).
- No in-lane May-SS or external Ext-program cross-check.
- Degree bookkeeping: bottom Moore cell in degree 2, so (s,t)=(3,50) is stem 47.

## Reproducibility
Run the three replay commands above with Python 3 + numpy (stdlib otherwise). The audit
independently reproduced all headline ranks, d^2=0, k0 cocycle/non-boundary status, and
the LES cross-check from the same scripts.

## References
- H. R. Miller, On relations between Adams spectral sequences, with an application to the
  stable homotopy of a Moore space (1981). https://doi.org/10.1016/0022-4049(81)90064-5
- Isaksen–Wang–Xu, Stable homotopy groups of spheres: From dimension 0 to 90
  (arXiv:2001.04511). https://arxiv.org/abs/2001.04511
- Belmont–Kong, A Toda Bracket Convergence Theorem for Multiplicative Spectral Sequences
  (2025). https://doi.org/10.1007/s42543-025-00099-x
- Panchev thesis, On the v1-periodicity of the Moore space (MIT).
  https://math.mit.edu/~hrm/thesis/panchev-thesis.pdf
- Andrews thesis, The v1-periodic part of the Adams spectral sequence at an odd prime.
- Bruner program/database page (mod-2 Steenrod cohomology database + ext calculator).
  http://www.rrb.wayne.edu/papers/
