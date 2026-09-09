# Exhaustive Bott wash-out and stability threshold for an admitted Villadsen diagonal system

## Context

The Toms–Winter regularity program divides simple nuclear C*-algebras into the
Jiang–Su-stable classified range and the Villadsen-type boundary where strict
comparison can fail. On the failure side the radius of comparison is the fine
invariant: Elliott–Li–Niu classify certain Villadsen algebras by K0 together
with radius of comparison, so exact rc intervals with finite Cuntz-obstruction
certificates are recognized open data.

The admitted target asked for `1/4 <= rc(V) <= 1` for the Villadsen first-type
diagonal AH limit with `A1 = M2(C((S^2)^2))`, recursive rule `n_{i+1} = 4 n_i`,
`X_{i+1} = X_i^3 x (S^2)^2` (3 coordinate-projection eigenvalue maps plus point
evaluations), via a finite-stage Bott-projection Cuntz obstruction. Executing
that plan, stage-3 witness assembly succeeded but persistence failed at `j = 8`
by exact integer threshold, and the failure generalized to the complete design
space. This record states the resulting emergent finding.

## Definitions

- `Aj = M_{Nj}(C(Xj))`, `Xj = (S^2)^{tj}`, `t1 = 2`, `t_{j+1} = 3 t_j + 2`,
  `N1 = 2`, `N_{j+1} = 4 N_j` (3 coordinate branches + 1 point-evaluation branch).
- Closed forms: `tj = 3^j - 1`, `Dj := dim Xj = 2 tj = 2(3^j - 1)`,
  `Nj = 2 * 4^{j-1}`. Stage 3: `t3 = 26`, `D3 = 52`, `N3 = 32`.
- `Xj` is connected (product of spheres); every projection in `M_K(Aj)` has
  constant rank and every normalized trace evaluates it as `rank / (K Nj)`.
- Bott line: the Hopf/Bott projection `e = (I + N)/2`, `N = x s1 + y s2 + z s3`
  (Pauli matrices), rank 1, `c1` the generator of `H^2(S^2)`.
- Witness designs in `M_K(A3)` with normalized gap `g = 1/4` (absolute rank gap
  `c = 8K`): `a = E_m + theta^t`, `b = theta^{m+t+c}` (`E_m` = sum of `m` Bott
  pullbacks on distinct coordinates, `theta` = trivial line); complement of
  `E_m` inside `b` has rank `R = t + c`. Chern obstruction iff `m > R`
  (top-degree test `2m > 2R`). Targets equal to the full matrix identity are
  excluded (trivially comparable).
- General pairs allow both `a, b` Bott-carrying with disjoint Bott coordinates
  (worst case; shared factors cancel); obstruction needs `S := ma + mb > c`.
- Chern-shadow dynamics: Bott support triples (`m -> 3m`), complement rank
  quadruples (`R -> 4R`); wash stage = least `j >= 3` with
  `m 3^{j-3} < R 4^{j-3}`.
- Stable-range forcing stage `J(g)` = least `j >= 3` with
  `g Nj >= (Dj+1)/2`; Toms strict `+1` form `J^+(g)` uses `Dj/2 + 1`.
- Homogeneous bound values `uj := Dj/(2Nj) = (3^j-1)/2^{2j-1}`.

## Result

**Theorem.** For the above system:

- (a) *Finite-stage witnesses exist.* With `c = 8K`, designs with `m > R`
  carry a genuine stage-3 Chern obstruction. The optimal pure `K = 1` design
  is `a = E_23` (rank 23) vs. `b = theta^31` (rank 31), gap `8/32 = 1/4`,
  `m/R = 23/8` maximal over the full census. `m = 24` is excluded (`b` would be
  the `32x32` identity). Full census: 122 obstructed `(m,t)` trivial-target
  designs (`64 + 55 + 3` for `K = 1, 2, 3`; none for `K >= 4`) and 605
  obstructed general pairs (`327 + 225 + 53`; all overlap patterns).
- (b) *Uniform wash-out.* Every stage-3 gap-`1/4` witness washes by `j <= 8`:
  worst trivial-target shadow washes at `j = 7`; worst general-pair shadow
  `(S,c) = (26,8)` is obstructed at `j = 7` (`2106 > 2048`) and washed at
  `j = 8` (`6318 < 8192`). Stable-range forcing gives independently
  `J(1/4) = 8` (robust to `+-2`); Toms strict `+1` form agrees
  (`J^+(1/4) = 8`). Four quantities coincide at `j = 8`.
- (c) *All birth stages, all gaps.* `K = 1` births only `j <= 7`
  (`8192 > 6560` at `j = 8` infeasible); `K = 2` only `j <= 4`; `K >= 4`
  nowhere at any stage. Worst-shadow wash over all feasible `(K, i)` is
  `j <= 8` (at most 9 over the extended later-birth table). Closed form for
  any fixed `g > 0`: `J(g) <= ceil(ln(2/g)/ln(4/3))`, tight on
  `{1, 1/2, 1/4, 1/8, 1/16, 1/32, 1/100, 1/1000}`
  (`J = 3, 5, 8, 10, 13, 15, 19, 27`); strict Toms `+1` form is at most one
  stage later.
- (d) *Threshold.* For general seed `s` (`t_{i+1} = 3 t_i + s`),
  `D_{i+1}/N_{i+1} = (3/4)(D_i/N_i) + s/(2N_i)` exactly, so contraction
  `k/m = 3/4 < 1` for *every* seed `s` (verified `s = 1..10`): slow dimension
  growth and mean dimension zero throughout the admitted `(m = 4, k = 3)` rule.
  Positive rc needs `k/m >= 1`.
- (e) *Upper half secured.* `u3 = 13/16 <= 1`, strictly decreasing for
  `j >= 2`, `-> 0` (epsilon-stages: `1/2 -> 5`, `1/4 -> 8`, `1/8 -> 10`,
  `1/16 -> 13`, `1/32 -> 15`, `1/100 -> 19`, `1/1000 -> 27`). Rounding
  `G/n > D/2n => G >= floor(D/2)+1` is exact; stage-3 sharpness `G = 26`
  (not forcing) vs. `G = 27` (forcing).

**Corollary (under cited standard lemmas L1--L5).** No fixed-gap Bott pair
witnesses `rc(V) >= g` for any `g > 0` in the limit; trace identities
`d_tau(a) + 1/4 = d_tau(b)` hold exactly for all (limit) traces, so failure is
purely on the comparison side. `rc(V) <= 13/16 <= 1` (indeed `rc(V) = 0` along
the `liminf` route). In particular the target lower bound `rc(V) >= 1/4` is
unwitnessable in the admitted data (`k/m = 3/4 < 1` puts `V` on the stable side).

## Proof / evidence

Machine-proved here (stdlib-only exact `Fraction`/integer arithmetic; all
`VERIFY_OK`, one-command replay `python3 output/artifacts/verify_manifest.py`
-> `MANIFEST_OK: 16/16`): stage recursions and closed forms; Bott identities
`{si,sj} = 2 delta_ij I`, `N^2 = (x^2+y^2+z^2) I`, `e = (I+N)/2`
idempotent/self-adjoint/trace-1 at 7 rational sphere points; cohomology ring
`c * c^{-1} = 1` in `Z[u_1..u_m]/(u_i^2)` (brute force `m <= 8` + sparse audit
`m = 12, 23, 26`); obstruction table and rank/coordinate budgets; exhaustive
censuses (`64, 55, 3` trivial; `327, 225, 53` general; `K >= 4` impossible since
`R >= c = 8K >= 32 > 26 >= m`); wash dynamics and `J`-tables; closed-form `J(g)`
bound (float log proposes, exact arithmetic disposes); seed recurrence and
epsilon-stages; rounding and `G = 26/27` sharpness; side conditions C1--C7
(`D` even, `3+1 = 4` multiplicity split, `tj >= 1`, integrality, `u1 = u2 = 1`
boundary, `Mj = 4^{j-1}`, `D/2` integral).

Cited standard theorems (statements only, scope flagged): L1 Cuntz = MVN for
projections; L2 Husemoller-type stable-range embedding (`f - e >= D/2` forces);
L3 Chern-class obstruction (`m > R` test); L4 limit-trace restriction to
normalized block traces; L5 homogeneous bound `rc(M_N(C(X))) <= dim X/(2N)` +
`liminf` lemma + Toms pointwise rank lemma; Niu mean-dimension-zero implies
strict comparison (corroboration only). Assumed: generic-density simplicity of
`V` (standard Villadsen hypothesis; moot for the refuted lower bound).

Key auditable skeleton: rank preservation (each diagonal step multiplies
constant ranks by 4; normalized gaps preserved exactly); Chern test
(`c(E_m) = prod(1+u_i)`, inverse top term `(-1)^m u_1...u_m != 0` in degree
`2m`; embedding into trivial rank `m+R` requires equality with `c(Q)`
supported in degrees `<= 2R`: obstruction iff `m > R`); overlap cancellation
(`(1+u)^{-1}(1+u) = 1`, so `S_eff <= S` and `S <= c` kills all overlap
patterns); dynamics (Bott support triples, complement quadruples, ratio
`(3/4)^j` decides); birth windows (`c_i = K N_i/4 < t_i` required).

## Limitations

No claim is made on the full target interval `1/4 <= rc(V) <= 1` (its lower
half is refuted as witnessable here, upper half secured as above). No claim
`rc(V) = 0` beyond the `liminf` route modulo cited L5 plus
simplicity/trace-identification hypotheses (stated, not proved here). No claim
about other Villadsen parameter regimes (`k/m >= 1`); the threshold diagnostic
predicts where to look, but persistence there is not proved here. Theorems
L1--L5 and Niu's theorem are cited, not re-proved; only their numerical side
conditions are machine-checked (C1--C7).

## Reproducibility

All arithmetic is stdlib-only exact:

```
python3 output/artifacts/verify_manifest.py   # MANIFEST_OK: 16/16 VERIFY_OK
```

Per-script outputs print exact tables (stage data, `J`-grids, census counts,
wash stages, epsilon-stages). Independent audit recomputation confirmed:
trivial census `64/55/3`, general census `327/225/53`, max `m/R = 23/8`,
worst wash `j = 8`, `J(1/4) = 8`, threshold recurrence, `u3 = 13/16`.

## References (cited background, not verified here)

Elliott–Li–Niu, Remarks on Villadsen algebras (2209.10649); Elliott–Niu II
(2510.13695); Toms–Winter, The Elliott conjecture for Villadsen algebras of
the first type (math/0611059); Niu, Mean dimension and AH-algebras with
diagonal maps (1010.0623); Hirshberg–Phillips (2312.11203); standard
comparison/stable-range material (Husemoller fibre systems; Rordam/Blackadar
Cuntz = MVN for projections; Toms rank lemma and homogeneous rc bound).
