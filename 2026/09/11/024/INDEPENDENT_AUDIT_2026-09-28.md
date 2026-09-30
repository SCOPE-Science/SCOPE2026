# Independent Audit — 2026-09-28

**Record:** `2026/09/11/024`  
**Title:** Smooth 3D Mahler-stability gap at distance 1.1 is false  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `cf787db17d4c82fa732b1e788b8f1ce22aed3a7b`  
**Disposition:** **PASSED**

## Independent checks

- Re-derived the 3/2 lower bound from the sign-average identity and trace inequality.
- Recomputed the exact sandwich and product bounds with rational arithmetic.
- Compared the conceptual counterexample with the known equality characterization and 2026 Mahler literature.

## Three-axis assessment

- **Correctness — PASS**: The smoothed-octahedron argument is valid. For delta=10^-6 and r=1-3delta, strict convexity and smoothness follow from the positive-definite diagonal Hessian of sum sqrt(x_i^2+delta^2), while r B_1^3⊂K⊂B_1^3. The elementary operator-norm/trace argument gives d_BM(B_1^3,parallelepipeds)≥3/2 and the sandwich transfers this to d_BM(K,P)≥(3/2)r=1.4999955. Polarity gives K°⊂r^-1 B_infty^3, hence |K||K°|≤(32/3)r^-3, whose excess over 32/3 is about 9.60006×10^-5<10^-3. The same estimates yield the stated arbitrarily-small excess with distance bounded above 1.4 by choosing delta sufficiently small.
- **Originality — LIMITED**: The conceptual obstruction is already implicit in the equality theory: in dimension 3 both parallelepipeds and affine octahedra attain the symmetric Mahler minimum, so a stability gap measured only from the parallelepiped class cannot persist under smooth approximation of the octahedron. The record contributes a clean explicit C-infinity smoothing and numerical certificate for the proposed (1.1,10^-3) cell, rather than a new Mahler phenomenon.
- **Scientific Value — PASS**: The explicit counterexample efficiently invalidates a quantitatively specified but structurally impossible target and identifies the missing second equality class. That is scientifically useful for reformulating any valid stability statement (for example, distance from the full equality family), even though the underlying minimizer geometry is known.

## Findings

- Current main tree exactly equals the assigned source-tree SHA.
- Exact rational arithmetic gives d_BM lower bound 2999991/2000000 and product excess about 9.60006e-5.
- The smoothness/strict-convexity and polarity-sandwich steps are valid.
- The novelty is limited because octahedral equality is part of known three-dimensional symmetric Mahler equality theory.

## Sources compared

- Repository record 024 RESULT.md: https://github.com/SCOPE-Science/SCOPE2026/blob/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/11/024/RESULT.md — Contains the explicit smoothing and quantitative bounds audited here.
- Iriyeh–Shibata, Symmetric Mahler’s conjecture for the volume product in the three dimensional case: https://arxiv.org/abs/1706.01749 — Proves the three-dimensional symmetric Mahler inequality and determines the equality condition.
- Chen–Li–Xi–Xu, The Mahler Conjecture in Three Dimensions: https://arxiv.org/abs/2605.09334 — Current 2026 three-dimensional Mahler work gives a new proof and full equality characterizations; it subsumes the separate symmetric preprint context.

## Limitations

- The witness is not claimed to be a zonoid, so it does not decide a zonoid-only stability fallback.
- The 3/2 estimate is sufficient for the disproof; the audit does not need or claim an exact Banach–Mazur distance formula for every smoothing.

This audit is independent of the repository’s pre-existing audit material. GitHub was read only as evidence; no repository changes were made by this audit run.
