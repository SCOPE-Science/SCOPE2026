# Refutation and exact dichotomy for central-unipotent 7-lifts in SL(2,q)

## Context

Degree 7 is the smallest regular degree missed by the Lubotzky–Phillips–Sarnak
(`p+1`) and Morgenstern (`q+1`) arithmetic Cayley–Ramanujan families, since
`7-1 = 6` is not a prime power. Marcus–Spielman–Srivastava (interlacing
families I/IV) and Hall–Puder–Sawin prove only existential, non-Cayley
Ramanujan lifts/coverings of every degree. The admitted target claimed a
universal representation-theoretic barrier: every set in a natural
central-unipotent 7-set class `C_q` in `SL(2,q)` is connected but strictly
non-Ramanujan, via a Frobenius–Schur sign plus interlacing bound. The finding
below tests that universal quantifier inside the admitted class and refutes
both conjuncts with exact certificates.

## Definitions

- `q >= 7` prime, `G_q = SL(2,q)`, `|G_q| = q(q^2-1)`, `z = -I` (central
  involution, trace `-2`).
- `U_q = {g : tr(g) = 2, g != 1}` (unipotents).
- `C_q = {{z} ∪ A ∪ A^{-1} : A = {u1,u2,u3} ⊂ U_q distinct, |S| = 7}`.
- `Cay(G_q,S)`: Cayley graph; `X(S)`: its bipartite double cover
  (672 vertices at `q = 7` when connected).
- Ramanujan threshold for degree 7: `2√6 = 4.898979…`.
  `λ2(X) = max(λ2(G), −λ_min(G))` where `G = Cay(G_q,S)`.
- `u(a) = [[1,a],[0,1]]`, so `u(a)^{-1} = u(−a)`, `u(a)u(b) = u(a+b)`.

## Result

The universal barrier is **false**, in the following sharp two-sided form:

**(a) Analytic disconnectivity, all `q ≥ 7`.**
`S_B = {−I, u(±1), u(±2), u(±3)} ∈ C_q`, but
`⟨S_B⟩` has order exactly `2q`. Hence `Cay(G_q,S_B)` has `(q²−1)/2`
components and `X(S_B)` is disconnected (components on `4q` vertices;
14/336 and 28/672 at `q = 7`).

**(b) Exact Ramanujan member of `C_7`.**
With entries mod 7, row-major,
`S_R = {z, r1, r2, r3, r1^{-1}, r2^{-1}, r3^{-1}}`,
`r1 = (4,2,6,5)`, `r2 = (2,4,5,0)`, `r3 = (1,4,0,1)`,
inverses `(5,5,1,4)`, `(0,3,2,2)`, `(1,3,0,1)`,
lies in `C_7`, generates `SL(2,7)`, and satisfies
`λ2(X(S_R)) ≤ 4.89 < 2√6` by exact integer arithmetic. Thus `X(S_R)`
is a connected 7-regular bipartite Ramanujan graph on 672 vertices.

**(c) Diagnosis.**
Members of `C_q` are symmetric but in general not normal
(`h s h^{-1} ∉ S_R` exhibited), so per-irrep character averages are
normalized block traces, not block spectra; no conjugacy-class sign can
upper-bound `λ2` on this class in the audit-plan form.

Consequence: `C_q` is mixed — it contains both disconnected and Ramanujan
members. Design guidance is the reverse of the proposed exclusion lemma:
HDX / quantum-LDPC searches must not exclude the class wholesale, and any
future barrier needs a generating hypothesis plus non-class-function methods.

## Proof / evidence

**Proof of (a).**
`z ≠ 1` is central of trace `−2 ≠ 2`, so `z ∉ U_q`.
For prime `q ≥ 7`, `{±1,±2,±3}` are six distinct nonzero residues
(differences `1,…,6 ≠ 0 mod q`), so with `A = {u(1),u(2),u(3)}`,
`|S_B| = 7` and `S_B ∈ C_q`. All of `S_B` is upper-triangular, hence
`⟨S_B⟩ ⊆ B ≠ G_q` where the Borel `B = {c = 0}` has order `q(q−1)`.
Exactly: `⟨u(1)⟩ = {u(a)}` has order `q`; `z ∉ ⟨u(1)⟩`;
`z` central gives `H = ⟨u(1)⟩ × ⟨z⟩` of order `2q`;
`S_B ⊆ H` and `u(1), z ∈ S_B` generate `H`, so `⟨S_B⟩ = H`.
Cayley component size `2q`; `(q²−1)/2` components
(24, 60, 84, 144 for `q = 7,11,13,17`, BFS-confirmed).
Each base component is non-bipartite (e.g. triangle `1–u(1)–u(3)–1`
since `u(1)·u(2) = u(3)`), so each lifts to a connected `4q`-vertex
double-cover component (28 of 672 at `q = 7`).

**Proof of (b), membership and generation (exact BFS).**
Each `r_i` has `det ≡ 1`, `tr ≡ 2 mod 7`, `r_i ≠ 1` (unipotent);
listed inverses check entrywise and lie in the set, distinct from `z`
(trace `5 ≠ 2`); `|S_R| = 7`, symmetric, of the form
`{z} ∪ A ∪ A^{-1}`: `S_R ∈ C_7`.
BFS from the identity visits all 336 Cayley vertices and all 672
double-cover vertices; the Cayley graph is non-bipartite (BFS 2-coloring
conflict), consistent with connected `X`.
Replay: `python3 output/artifacts/verify.py` prints `VERIFY_OK`.

**Proof of (b), exact Ramanujan certificate (`μ0 = 4.89 < 2√6`).**
`4.89² = 23.9121 < 24`, i.e. `4898² = 23990404 < 24000000` in integers.
Let `A` be the `336×336` adjacency matrix of `Cay(SL(2,7),S_R)`.

- *Lower leg* (`−λ_min ≤ μ0`): `M_lo = 100A + 489I` is positive-definite
  by exact fraction-free (Bareiss) symmetric elimination: all 336 pivots
  `> 0` (first/minimum pivot 489). Hence all eigenvalues of `A ≥ −4.89`.
- *Upper leg* (`λ2(G) ≤ μ0`): committed integer vector `w ∈ ℤ^336`,
  `Σw = 0`, `w ≠ 0` (scale-`10^4` rounding of a `λ2` eigenvector
  projected `⊥ 1`; `rayleigh_vec.json`) gives
  `wᵀAw = p = 55177273021248`, `wᵀw = qq = 11289966448320`,
  `p² < 24·qq²` exactly (Python ints), so by Courant–Fischer
  `λ2(G) ≤ p/qq = 4.8872840565… < 2√6`; also `100p ≤ 489·qq` exactly,
  i.e. `p/qq ≤ 4.89`. Replay:
  `python3 output/artifacts/exact_rayleigh.py` prints `EXACT_OK`.
  Consistently, `M_up = 16430400I − 3360000A + 21436J` is Bareiss-PD
  (`16430400 = 3360000×4.89` exactly; committed log reports PD,
  minimum pivot 16451836): for unit `v ⊥ 1` with `λ2(A) > μ0`,
  `vᵀM_up v < 0`, contradiction.

Therefore `λ2(X) = max(λ2(G), −λ_min(G)) ≤ 4.89 < 2√6`.

**Numerical envelope (evidence only):** two eigensolvers agree
`λ2(G) = 4.88728501` (mult 7), `λ_min = −4.64575131`;
`tr A² = 2352 = 336·7`, `tr A³ = 0`, `tr A⁴ = 34608` exactly,
matching the spectrum; eigenpair residual `∼2×10⁻¹⁵`.

**Non-normality witness:** `h = (0,1,6,0)`, `s = (4,2,6,5) ∈ S_R` gives
`h s h^{-1} = (5,1,5,4) ∉ S_R` (recomputed). For non-normal `S`, the
regular-representation block `(1/7)Σ ρ_χ(s)` has eigenvalues `≠` the
scalar character average `(1/7χ(1))Σ χ(s)` in general.

## Limitations

- Exact certificates cover the single witness `S_R` (upper bound
  `λ2(X) ≤ 4.89`), not a classification of `C_7`; the `∼1/6`-Ramanujan
  frequency is a random-sweep estimate (114–362 connected samples), not
  a census.
- `q = 11` probe (best `λ2(X) = 5.1792`, all non-Ramanujan) is evidence
  only; no claim about `q > 7` spectra is made.
- Conjugacy census recomputed from scratch over `F_7`; agrees with the
  textbook `SL(2,7)` table but no external table values are relied upon.
- The `M_up` Bareiss PD relies on the committed log; the upper leg is
  independently proved by the exact Rayleigh vector.
- Falsification-by-counterexample within the admitted class; the Borel
  containment argument is elementary. No novelty is claimed for
  interlacing or character-sum machinery, cited as background.

## Reproducibility

- `python3 output/artifacts/verify.py` → `VERIFY_OK`
  (membership, BFS connectedness, spectra, traces, residual).
- From `output/artifacts/`:
  `python3 exact_rayleigh.py` → `EXACT_OK`
  (exact integer Rayleigh certificate from committed `rayleigh_vec.json`).
- `output/artifacts/bareiss_up.log` records the committed `M_up` Bareiss
  PD run; `output/artifacts/bareiss_cert.py` is the committed Bareiss
  driver (its `lo` construction `M_lo = 100A+489I` was additionally
  re-run from scratch to PD with minimum pivot 489).
- All group arithmetic rebuilt from scratch over `F_7` (stdlib + numpy
  for the evidence envelope only; certificates are integer arithmetic).

## References

- Marcus–Spielman–Srivastava, Interlacing Families I: Bipartite Ramanujan
  Graphs of All Degrees, https://arxiv.org/abs/1304.4132
- Marcus–Srivastava–Spielman, Interlacing Families IV: Bipartite Ramanujan
  Graphs of All Sizes, https://arxiv.org/abs/1505.08010
- Hall–Puder–Sawin, Ramanujan Coverings of Graphs,
  https://arxiv.org/abs/1506.02335
- Lubotzky, Expander Graphs in Pure and Applied Mathematics,
  https://arxiv.org/abs/1105.2389
