# Exact two-monomer Kasteleyn census on 6xN rectangles (N=6-10) by symmetry orbit

## Context

Pure dimer counts on rectangles are textbook Kasteleyn/Temperley-Fisher Pfaffians. Fixed-position monomer correlations bridge that theory to conformal-invariance asymptotics and sampling benchmarks, but no citable exact per-orbit table existed for even-width 6xN boards. Boundary-single-monomer Pfaffians (Tzeng-Wu/Wu; Giuliani-Jauslin-Lieb) cover only boundary monomers; bulk product-of-Pfaffians formalisms give numerics, not exact orbit tables.

## Definitions

Let G(N) be the 6xN grid graph (R=6 rows, N columns, N=6..10). For holes H, let Z(N,H) be the number of dimer coverings of G(N) minus H. Let Z(N,empty) be the pure-dimer count. For opposite-colour pairs {u,v} (necessary for Z>0 on the bipartite board), define C(N,u,v)=Z(N,u,v)/Z(N,empty). Symmetry is dihedral: D4 (order 8) for 6x6, Klein-4 (order 4) otherwise; orbits are canonicalised by explicit minimisation over the group. A Kasteleyn orientation is an edge orientation with every finite face odd-clockwise; then |Pf(K)|=Z where K is the signed skew-symmetric adjacency matrix.

## Result

**Theorem (doubly certified computation).** For every N in {6,7,8,9,10} and every symmetry-inequivalent opposite-colour pair {u,v} (45, 123, 156, 198, 240 orbits respectively; 762 total), the value Z(N,u,v) in `artifacts/census.csv` is exact. Every entry satisfies Pf=DP where Pf is the exact integer Pfaffian of a per-graph solved-and-verified Kasteleyn matrix (Pf^2=det over the integers, determinant recovered exactly by CRT over 7 primes) and DP is an independent profile-DP (transfer-matrix, 2^6 states) enumeration: 762/762 agreements.

Pure-dimer baselines by the same Pfaffian (agreeing with the Kasteleyn product formula) are:

- N=6: 6728; N=7: 31529; N=8: 167089; N=9: 817991; N=10: 4213133.

The unique (up to symmetry) maximiser of C(N,u,v) per N is the adjacent-corner pair:

- N=6: (0,0),(0,1): Z=3364, C=0.5 (square; (0,0),(0,1)~(0,0),(1,0));
- N=7: (0,0),(1,0): Z=16926, C=0.5368391005;
- N=8: (0,0),(1,0): Z=85659, C=0.5126549324;
- N=9: (0,0),(1,0): Z=431819, C=0.5279018962;
- N=10: (0,0),(1,0): Z=2182406, C=0.5180007372.

For each maximiser two explicit dimer coverings A!=B are stored in `artifacts/witnesses.json`, both passing edge-occupancy validation and differing by one unit-square flip (face and direction logged).

**Correction lemma.** The fixed inherited orientation (all horizontal right, vertical alternating by column), Kasteleyn for the full 6xN board, is in general NOT Kasteleyn for the punctured board. Counterexample: 6x6 minus {(1,1),(4,4)} leaves two 8-cycle hole faces with 4 clockwise edges (even). Hence per-graph GF(2) odd-clockwise solving with face-by-face re-verification is required and is done for every orbit.

## Proof / evidence

Parity zeros are theorems: single-monomer deletion on even-area 6xN leaves odd cells (Z=0); same-colour pairs leave colour imbalance (Z=0). All positive counts are certified computations, not analytic proofs: (A) planar faces enumerated by half-edge traversal, GF(2) flip system solved, every finite face verified odd-clockwise before any Pfaffian; exact determinant via CRT (product ~1e35 >> actual dets ~1e13), Pf=isqrt(det) with Pf*Pf==det asserted; (B) independent profile-DP with blocked cells; Pf==DP asserted per orbit (762/762). Independent audit reimplemented DP separately (762/762 match), brute-force backtracking on sampled N=6 orbits, Bareiss exact determinants on samples, independent orbit recount, Kasteleyn product-formula check of pure baselines, and occupancy+flip validation of all 5 witnesses. Auxiliary Temperley cross-check of the same machineries on genuine Temperleyan regions verifies trees(m x n)=dimers((2m-1)x(2n-1) minus one corner): 4=4, 15=15, 192=192 for (2,2),(2,3),(3,3); trees(6x6)=32565539635200 reported as auxiliary data, confirming no direct single-tree equality is asserted for the main two-monomer family.

## Limitations

N<=10 benchmark only; no thermodynamic-limit or Kenyon-type r^{-1/2} fits attempted. Flip-connectivity of the full monomer-dimer flip graph is not classified; only same-component distance-1 witness pairs exhibited. Symmetry reduction assumes stated dihedral actions. Same-colour zeros spot-checked, not exhaustively tabulated. Temperley equality claimed solely for the Temperleyan corner-removed family, not the two-monomer family. No floating point enters any count.

## Reproducibility

`artifacts/kasteleyn_census.py` (stdlib + numpy only): `python3 artifacts/kasteleyn_census.py --outdir artifacts/` regenerates `census.csv`, `summary.json`, `witnesses.json` in ~7 s with all assertions (face-oddness, Pf^2=det, Pf=DP, occupancy, flip exactness) active.

## References

- P. W. Kasteleyn, The statistics of dimers on a lattice, Physica 27 (1961); M. E. Fisher, Statistical mechanics of dimers, Phys. Rev. 124 (1961); H. N. V. Temperley and M. E. Fisher, Dimer problem, Phil. Mag. 6 (1961).
- F. Y. Wu, Pfaffian solution of a dimer-monomer problem: single monomer on the boundary, Phys. Rev. E 74, 020104(R) (2006) — https://arxiv.org/abs/cond-mat/0607647
- A. Giuliani, I. Jauslin, E. H. Lieb, A Pfaffian formula for monomer-dimer partition functions, J. Stat. Phys. 163 (2016) — https://arxiv.org/abs/1510.05027
- N. Allegra and J.-Y. Fortin, Grassmannian representation of the two-dimensional monomer-dimer model, Phys. Rev. E 89, 062107 (2014) — https://arxiv.org/abs/1402.5512
- S. Oh, State matrix recursion method and monomer-dimer problem (2019) — https://arxiv.org/abs/1901.07847
- R. Kenyon, Conformal invariance of domino tiling, Ann. Probab. 28 (2000); R. Kenyon, J. Propp, D. Wilson, Trees and matchings, Electron. J. Combin. 7 (2000) (Temperley bijection context).
