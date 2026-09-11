# Complete transversal spectrum and orthogonal-mate census over DCLS(11)

## Context

Diagonally cyclic Latin squares (DCLS), equivalently orthomorphisms and
complete mappings of cyclic groups, form a recognized program from Hall-Paige
through Wanless DCLS theory to Cavenagh–Hamalainen–Nelson cyclic-transversal
completion. A full order-11 Latin census (~10^25 isotopy classes) is
infeasible, so the symmetry-defined family DCLS(11) is the natural census
unit. The Wanless transversal database previously published only two order-11
exemplar squares (most/fewest transversals); no per-class distribution or
mate classification existed.

## Definitions

Work in Z_11. A **normalized orthomorphism** is a map θ : Z_11 → Z_11 with
θ(0) = 0 such that both θ|_{Z_11∖{0}} and ψ(d) = θ(d) − d (with ψ(0) = 0)
restrict to permutations of {1,…,10}. Each θ defines a Latin square

  L_θ(i,j) = θ(j−i) + i (mod 11),

which is diagonally cyclic; every normalized DCLS(11) arises this way.
Two seeds are **multiplier-isomorphic** if θ^a(d) = a·θ(a^{−1}d) for some
a ∈ F_11^*. A **transversal** is a set of 11 cells with distinct rows,
columns, and symbols. An **orthogonal mate** of L is a Latin square M with
all 121 pairs (L_{ij}, M_{ij}) distinct, equivalently a partition of the 121
cells into 11 disjoint transversals.

## Result

- **Seed census.** There are exactly **3441** normalized orthomorphisms
  (fresh backtracking enumeration; 11·3441 = 37851 agrees with OEIS A003111 /
  A006717). Under multiplier isomorphism they form exactly **C = 363**
  classes with orbit-size distribution 10^336 · 5^12 · 2^6 · 1^9
  (3360 + 60 + 12 + 9 = 3441). The canonical representative is the orbit
  minimum.
- **Transversal spectrum** (identical from two independent exact-cover
  counters over all 363 seeds):

    {3333: 33, 3443: 33, 3476: 66, 3553: 66, 3597: 9,
     3795: 36, 3949: 66, 4389: 36, 4411: 9, 37851: 9},

  summing to 363. Full per-seed table in `spectrum.json` /
  `count_log_A.json` / `count_log_B.json`.
- **Maximum.** M_DCLS = **37851**, attained at exactly 9 seeds, e.g.
  S_max = [0,2,4,6,8,10,1,3,5,7,9] (θ(d) = 2d). The nine maximizers are the
  orbit-minimal linear maps θ(d) = cd, c ∈ {2,…,10} (c = 1 gives ψ ≡ 0,
  correctly absent). The count 37851 reproduces the Wanless-database
  group-square total.
- **Mates.** Exactly **K = 363 (all seeds)** admit an orthogonal mate, via
  the universal mate M(i,j) = j−i (mod 11) with decomposition
  T_m = {(i, i+m) : 0 ≤ i < 11}, m = 0,…,10. Per-seed materialized
  11-way decompositions are in `mate_decompositions.json`.

## Proof / evidence

- **Enumeration.** Fixed-row backtrack over values 1..10 with θ-injectivity
  and ψ-injectivity pruning: 3441 solutions. Replay uses reverse value order;
  both give 3441.
- **Canonical reduction.** Orbit under the 10 multipliers; representative =
  lexicographic minimum; pairwise non-isomorphism and completeness (3441
  orbits covered) rechecked in `replay.py`.
- **Counting, method A.** Row-fixed backtrack with column/symbol bitmasks.
- **Counting, method B (independent).** Generic exact cover over 33 columns
  (rows + columns + symbols), 121 cell-options, MRV column branching —
  different code path and traversal. Logs agree on all 363 seeds. A third
  method (reverse-row bitmask backtrack) spot-recounts seeds including the
  group square.
- **Mate theorem.** M(i,j) = j−i is Latin (for fixed i, j ↦ j−i bijective;
  for fixed j, i ↦ j−i bijective). Orthogonality: given
  (u,v) = (L_θ(i,j), M(i,j)), M = v gives d := j−i = v, then
  u = θ(v) + i gives i = u − θ(v), j = i + v — a unique preimage, so all 121
  pairs occur. Each T_m has distinct rows 0..10, distinct columns i+m, and
  distinct symbols θ(m) + i — a transversal. All 363 verified by pair
  enumeration in both `run_all.py` and `replay.py`.
- **Replay.** `python3 replay.py` prints `REPLAY_OK` (seed validity,
  canonical form, distinctness, completeness over fresh 3441-enumeration,
  A/B agreement, Latin checks, third-method spots, spectrum aggregates,
  mate pair/decomposition checks). The auditor re-ran replay (REPLAY_OK)
  and independently recounted one seed per spectrum value with separate
  code — all match.

## Limitations

Scope is cyclic multiplier isomorphism exactly as archived; broader isotopy
could identify further seeds but is outside the claimed scope. Counts are
exact (exhaustive search, no sampling or heuristics). Artifact hashes:

- `seeds.json` 6e3a77f6958aad627284c2c721d0d26aeec1c3ebdc901a0c39112db8b582b432
- `count_log_A.json` b8f5d247d10d4db88a4e6d64c2250b89970255d9e9688bd0aa9d247dcc1d2cc8
- `count_log_B.json` 3ca79eaee7b78fd0e4377b4d4cd8340e97062fed265e21bc70dbc5647a5e9782
- `spectrum.json` d3982a9b4457d524792cfa86670a91a356df109fafbc49498568815890833f1d
- `mate_certificate.json` 629fb4eae19b9414bd293d28d9a660a50ea638a214dd3d816d3944433537fdb7
- `mate_decompositions.json` 14613dab9d7b1c2bdc2cfd04fa32e94b272d186c4aa82dfdc4ba4089f9a35ff0
- `run_all.py` 11548f3db2bef81b0c86e4f221ba29161a8e09552567e4bc6e8562df0e90571d
- `replay.py` bc2bea061b7c05a4384e7a7b9284e47401b9b723c033f9d7b0cd4bb5939a00e7

Reproduce: `python3 run_all.py` (stdlib only), then `python3 replay.py`.

## References

- Ian Wanless, Diagonally cyclic latin squares, Eur. J. Combin. (2004).
  https://doi.org/10.1016/j.ejc.2003.09.014
- Ian Wanless, Data on transversals in Latin squares (official database).
  https://users.monash.edu.au/~iwanless/data/transversals/
- Egan–Wanless, Enumeration of MOLS of small order (arXiv:1406.3681).
- Maenhaut–Wanless, Atomic Latin squares of order eleven.
  https://doi.org/10.1002/jcd.10064
- Cavenagh–Hamalainen–Nelson, On completing three cyclic transversals to a
  Latin square. https://arxiv.org/pdf/0712.0233
- Hulpke–Kaski–Ostergard, The number of Latin squares of order 11.
- OEIS A003111 (normalized complete mappings) / A006717 (orthomorphisms /
  transversals of cyclic squares / semi-queens).
