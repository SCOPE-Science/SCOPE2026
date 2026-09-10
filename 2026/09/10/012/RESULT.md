# Finite-Type B2 Transverse-Slice Obstruction at Joint J* for B1

## Context
Cluster-vs-scattering frontier after Lee–Schiffler positivity (skew-symmetric only),
Gross–Hacking–Keel–Kontsevich theta/broken-line theory, and Bridgeland
Hall-algebra scattering–stability: where does finite cluster/F-polynomial dynamics
end and infinite (Badlands-type) scattering begin? The admitted investigation fixed
the strictly skew-symmetrizable cyclic rank-3 exchange matrix
B1 = [[0,2,-1],[-1,0,1],[1,-2,0]] with symmetrizer D = diag(1,2,1) and the
pre-fixed initial joint J* = e1-perp ∩ e2-perp, seeking a non-cluster
imaginary-root wall W* visible to total-degree order ≤ 4. The finding below is the
completed audit of that scope: a structural obstruction proving the target
impossible as stated, plus exact finite certificates closing the J* slice.

## Definitions
- B1, D as above; D*B1 = [[0,2,-1],[-2,0,2],[1,-2,0]] is skew-symmetric.
- Cartan counterpart A = 2I − |B1|; symmetrized S = D*A =
  [[2,-2,-1],[-2,4,-2],[-1,-2,2]], symmetric; q(v) = (1/2) vᵀSv.
- Joint J* = e1-perp ∩ e2-perp; walls incident to J* have normals n = (a,b,0).
- c-vectors are COLUMNS of the C-matrix under Fomin–Zelevinsky mutation:
  C'[i][k] = −C[i][k];
  C'[i][j] = C[i][j] + [C[i][k]]₊[B[k][j]]₊ − [−C[i][k]]₊[−B[k][j]]₊ (j≠k).
- Transverse exchange matrix B12 = [[0,2],[-1,0]] (|bc| = 2, finite type B2).
- F-polynomial mutation is FZ-IV with principal coefficients (see DRAFT §1).

## Result
For B1 with D = diag(1,2,1) at J* = e1-perp ∩ e2-perp:
1. (Obstruction, all orders.) q(a,b,0) = (a−b)² + b² ≥ 1 for every nonzero
   integral (a,b). Hence no imaginary-root (q ≤ 0) normal incident to J* exists
   at order ≤ 4 or any order.
2. (Transverse slice is finite type B2.) Alternating 6-step mutation on B12
   closes exactly ((B,C) back to seed), with 0 sign-incoherence; the 8 distinct
   c-vectors are ±(1,0), ±(0,1), ±(1,1), ±(2,1) (complete B2 root system),
   all with q ∈ {1,2}.
3. (Rank-3 BFS depth ≤ 6.) From B1 there are 40 distinct (B,C) seeds with
   by-depth counts {0:1, 1:3, 2:6, 3:8, 4:10, 5:9, 6:3}, 18 distinct c-vectors,
   0 sign-incoherence events. The J*-incident slice (n3 = 0) is exactly the 8
   B2 roots (−2,−1,0), (−1,−1,0), (−1,0,0), (0,−1,0), (0,1,0), (1,0,0),
   (1,1,0), (2,1,0), all with q ∈ {1,2}, with first-appearance depths ≤ 3
   (depths 4–6 add no new J*-incident c-vector).
4. (Finite F-identities.) Exact F-polynomials along the B2 cycle close
   (F back to (1,1) after 6 steps; every exchange division machine-verified
   exact). Every theta/F identity in the J* slice is a finite polynomial identity.
5. (Consequences.) The admitted target — W* incident to J*, non-cluster,
   imaginary-root, order ≤ 4, infinite theta product — is impossible as stated
   ((1) kills the imaginary-root clause at all orders; (2)–(4) show the slice is
   exhaustively finite-cluster). The preset fallback's lex-first non-cluster
   candidate set {W ∈ W_le4 : n ∉ C_le6} is EMPTY (W_le4 at J* = finite B2
   cluster walls, all in C_le6), so the fallback is unsatisfiable as written
   and is not claimed.

## Proof / Evidence
- (1) is algebra: (1/2)(2a²−4ab+4b²) = a²−2ab+2b² = (a−b)²+b² ≥ 1; replayed on
  box ±50 in `artifacts/verify_target.py`.
- (2) is exact finite computation: `artifacts/b2_exact.py` replays period-6
  (B,C) closure, sign coherence on all visited seeds, q-table, and rank-3
  q ≤ 0 box scan with no n3 = 0 entry. C-mutation sign validated: the used
  MINUS formula equals standard extended-matrix mutation and reproduces the
  analytic B2 system, while the PLUS alternative explodes (626 seeds, 332
  c-vectors, 177 incoherent at depth 6).
- (3) is exact finite computation: `artifacts/cvec_bfs.py` + logged
  `artifacts/cvec_bfs.json` replay 40 seeds / 18 c-vectors / slice data;
  slice first-appearance max depth 3 independently rechecked.
- (4) is exact finite computation: `artifacts/fpoly_b2.py` replays the 6-cycle
  with exact divisions via in-script linear solves.
- No KS order-4 broken-line product is cited; none is needed for the headline
  because (1) rules out imaginary walls at all orders and finite-type B2
  transverse theory places W_le4 at J* among the cluster walls.

## Limitations
- Decides only the J* transverse slice; non-cluster walls at joints with
  n3 ≠ 0 for this B1 are not investigated and not claimed.
- Transverse-slice ⇒ wall-finiteness invokes textbook finite-type rank-2
  consistency; not re-proved here.
- F-polynomial divisions verified by in-script truncated linear solves, not an
  independent CAS.
- Off-slice c-vectors ±(1,1,1) have q = −1 with explicit cluster mutation paths
  ([1,0] and [1,0,2]); they are cluster walls, not non-cluster evidence.

## Reproducibility
Stdlib-only Python, seconds (paths relative to this record directory):
  python3 artifacts/verify_target.py
  python3 artifacts/b2_exact.py
  python3 artifacts/cvec_bfs.py
  python3 artifacts/fpoly_b2.py
Logged tables: `artifacts/b2_slice.json`, `artifacts/cvec_bfs.json`.

## References
- Lee–Schiffler, Positivity for cluster algebras. https://arxiv.org/abs/1306.2415
- Gross–Hacking–Keel–Kontsevich, Canonical bases for cluster algebras. https://arxiv.org/abs/1411.1394
- Bridgeland, Scattering diagrams, Hall algebras and stability conditions. https://arxiv.org/abs/1603.00416
- Fomin–Zelevinsky, Cluster algebras I: Foundations. https://arxiv.org/abs/math/0104151
- Kontsevich–Soibelman, Stability structures, motivic DT invariants and cluster transformations. https://arxiv.org/abs/0811.2435
