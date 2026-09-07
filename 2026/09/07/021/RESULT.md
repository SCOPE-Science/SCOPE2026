# Centre-stratified census of 2-step nilpotent Lie algebras of dimension 6 with 2-dimensional centre over F2

## Context

Two-step nilpotent Lie algebras bridge textbook Heisenberg examples with Lazard correspondence and p-group classification. Full dimension-6 lists over algebraically closed fields of characteristic not 2 are classical (Morozov; de Graaf), but those works explicitly exclude characteristic 2. Over F2 alternating (`[x,x]=0`) diverges from skew-symmetric, and no citable per-orbit structure-constant table with automorphism orders existed for the fixed-centre stratum `(d,c)=(6,2)`. This record supplies that table as a reusable benchmark.

## Definitions

Let `V=F2^6` with basis `e0..e5`. A bracket is alternating F2-bilinear `[,]:VxV->V` with Jacobi identity. It is 2-step nilpotent if `[[x,y],z]=0` identically, i.e. `[L,L] subset Z(L)` where `Z(L)={x:[x,.]=0}`; then Jacobi is automatic. Isomorphism is `GL(6,F2)` base change. Fix `Z0=span{e4,e5}`, `Q0=span{e0..e3}`. A `Z0`-adapted bracket has image in `Z0` and `Z0` central, encoded by two alternating 4x4 matrices `(A,B)`: `[ei,ej]=Aij e4+Bij e5` for `i,j<4`. Alternating 4x4 over F2 has dimension 6 (strict upper triangle for pairs `(01,02,03,12,13,23)`), so 64^2=4096 adapted brackets. Bit code: integer 0..63 with bit k = entry at k-th pair. Ranks over F2 are in `{0,2,4}`; Pfaffian `Pf=b0b5+b1b4+b2b3` distinguishes 4 (Pf=1) from 2 (nonzero, Pf=0).

## Result

Up to `GL(6,F2)`-isomorphism there are exactly `N=4` 2-step nilpotent brackets on `F2^6` with `dim Z=2`. Representatives with `Z0` central (`[e4,.]=[e5,.]=0`):

- L0 `(a,b)=(0,12)`: `[e0,e3]=e5`, `[e1,e2]=e5`. Derived dim 1. Rank type `(0,4,4)`. Orbit 84. Stab 1440. |Aut|=368640.
- L1 `(1,12)`: `[e0,e1]=e4`, `[e0,e3]=e5`, `[e1,e2]=e5`. Derived dim 2. Rank type `(2,4,4)`. Orbit 1260. Stab 96. |Aut|=24576.
- L2 `(1,32)`: `[e0,e1]=e4`, `[e2,e3]=e5`. Derived dim 2. Rank type `(2,2,4)`. Orbit 1680. Stab 72. |Aut|=18432.
- L3 `(12,22)`: `[e0,e2]=e5`, `[e0,e3]=e4+e5`, `[e1,e2]=e4`, `[e1,e3]=e5`. Derived dim 2. Rank type `(4,4,4)`. Orbit 336. Stab 360. |Aut|=92160.

Here `12=(03),(12)`; `22=(02),(03),(13)`; `1=(01)`; `32=(23)`. Rank type `rt=sort(rank A,rank B,rank(A+B))`. The four `(derived,rt)` pairs are distinct, hence the four are pairwise non-isomorphic. Every 2-step bracket with centre dimension 2 is isomorphic to exactly one `Li`. `|Aut(Li)|=256*stab`.

## Proof / Evidence

Deductive lemmas: (1) Any 2-step `L` with `dim Z=2` conjugates to `Z0`-adapted form by sending `Z(L)` to `Z0`. (2) Adapted centre is `2+dim Rad(A,B)` where `Rad={v:Av=Bv=0}`; centre exactly `Z0` iff `Rad=0`; 3360 of 4096 pairs satisfy this (derived 1:84, derived 2:3276). (3) For `Rad=0`, isomorphisms preserve `Z0`, so `G=[[P,0],[R,S]]` with `P in GL(4,F2)`, `S in GL(2,F2)`, `R:Q0->Z0` free; pair transforms as `S.phi1=phi2(P.,P.)`, `R` trivial; classes are `GL(4,F2)xGL(2,F2)`-orbits (order 20160*6=120960) and `|Aut|=256*|Stab|`. (4) `dim[L,L]` and sorted rank triple are invariants (`S` permutes `{A,B,A+B}`).

Finite certificate (stdlib, deterministic): `|GL2|=6`, `|GL4|=20160`; rank-type census `(0,4,4):84,(2,4,4):1260,(2,2,4):1680,(4,4,4):336`; orbit expansion of four lex-min reps has sizes `84,1260,1680,336`, pairwise disjoint, union all 3360 Rad0 pairs (completeness, N=4); stabilizers `1440,96,72,360` satisfy `stab*orbit=120960`; tensors alternating with image in centre by construction, all `6^3=216` Jacobi triples (1296 scalar equations) vanish, 6-dim brute-force centre dim 2, derived as claimed; invariant separation gives non-isomorphism; sample block-diagonal `6x6` reductions `diag(P,S)` verified on all 36 pairs plus `det!=0`; same routine reduces any input in at most 120960 trials. Independently re-verified with alternate `P*M*P^T` congruence, Pfaffian rank, and separate 6-dim tensor code with identical numbers.

## Limitations

Finite-field census only (`F2`, `(d,c)=(6,2)`, class 2). No transfer to characteristic !=2, algebraically closed fields, other centre strata, or higher nilpotency class. Proof is computer-assisted: Lemmas 1-4 deductive; orbit partition, stabilizers and tensor re-verification are finite enumerations (4096 fibre, 120960 group) certified by replay script, not by hand.

## Reproducibility

Run `python3 output/artifacts/verify_census.py` (stdlib only, fixed order, no randomness, <2 min). It prints group orders, fibre counts, orbit sizes, stabilizers, Aut orders, Jacobi/centre logs, invariant table and reduction certificates, asserting each expected number. Data in `output/artifacts/census.json` (reps, bits, brackets, invariants).

## References

- W. A. de Graaf, Classification of 6-dimensional nilpotent Lie algebras over fields of characteristic not 2, J. Algebra 309 (2007), 640-653. https://doi.org/10.1016/j.jalgebra.2006.08.006
- H. Abdelwahab et al., The algebraic and geometric classification of nilpotent binary Lie algebras, arXiv:1902.01706. https://arxiv.org/abs/1902.01706
- B. Ren, L. S. Zhu, Classification of 2-Step Nilpotent Lie Algebras of Dimension 8 with 2-Dimensional Center, Comm. Algebra 39 (2011). https://doi.org/10.1080/00927872.2010.483342
- Z. Yan, S. Deng, The classification of two step nilpotent complex Lie algebras of dimension 8, Czech Math J 63 (2013). https://doi.org/10.1007/s10587-013-0057-6
- B. Ren, L. S. Zhu, Classification of 2-step nilpotent Lie algebras of dimension 9 with 2-dimensional center, Czech Math J 67 (2017). https://doi.org/10.21136/cmj.2017.0253-16
- M. A. Gauger, On the classification of metabelian Lie algebras, Trans. Amer. Math. Soc. 179 (1973). https://doi.org/10.1090/S0002-9947-1973-0325719-0
