# Exact maximal Sidon census in Z_60: maximum size 7 with full dihedral classification

## Context

In a cyclic group `Z_n`, a Sidon (B2) set requires all pairwise sums (or equivalently all ordered differences) to be distinct. The elementary counting bound `k(k-1)+1 <= n` is often slack. At `n=60` it allows `k=8` (`56+1=57<=60`) while the Singer perfect difference set `(57,8,1)` from the projective plane of order 7 lives one step below. Pilot search places `n=60` inside a `58-62` defect block where the counting allowance fails. `Z_60` is highly composite with 2-torsion (`-30=30`), so wrap-around collisions differ from the interval Golomb-ruler case. Closing one defect order and classifying its extremals is a citable extremal table entry.

## Definitions

Let `n=60`, `Z_60=Z/60Z`.

- **Sidon (primary):** `A subset Z_60`, `|A|=k`, is Sidon iff the `k(k+1)/2` sums `a+b mod 60` with `a<=b` (unordered with repetition) are pairwise distinct.
- **Differences cross-check:** `A` is weakly Sidon iff the `k(k-1)` ordered differences `a-b mod 60` with `a!=b` are nonzero and pairwise distinct.
- **Lemma (equivalence):** In any abelian group the two definitions coincide, including with 2-torsion. Proof: `a-b=c-d` with distinct ordered pairs gives `a+d=c+b`, a sum collision unless the same pair; the 2-torsion subcase `a-b=b-a` gives `2a=2b`, collision of `{a,a}` vs `{b,b}`; conversely `a+b=c+d` with distinct multisets gives `a-c=d-b`, a difference collision, doubling case `2a=c+d` gives `a-c=d-a`. Hence pruning on either family is sound and complete; a partial set failing either test has no Sidon superset.
- **Equivalence group:** Translations `x->x+t` and reflections `x->-x+t` generate dihedral `D_60` of order 120. Fix translation by requiring `0 in A` (rooted sets, sorted increasingly). Translation-canonical rep = lexicographically minimal sorted `k`-tuple among translates containing `0` (hence among all 60 translates). Dihedral-canonical rep = `min(translation-canonical(A), translation-canonical(-A))`. Each orbit has a unique minimal element.

Counting bound: differences need `k(k-1)` distinct nonzero residues, so `k(k-1)+1<=60` allows `k=8`; the theorem shows the bound is slack.

## Result

**Theorem.** In `Z_60` with the above Sidon definition:

- (a) The exact maximum size is 7. Example witness `W={0,1,3,7,12,20,38}` has 28 distinct sums and 42 distinct nonzero ordered differences (see below). No Sidon 8-set exists.
- (b) There are exactly 50092 rooted 7-sets containing `0`, i.e. 7156 translation classes each of size exactly 7 (no periodic class), forming exactly 3578 dihedral classes each containing exactly 2 translation classes (zero self-mirror classes). Every canonical representative is verified Sidon with per-witness certificates.

Witness sums `a+b (a<=b) mod 60`, sorted (28 distinct):

`0,1,2,3,4,6,7,8,10,12,13,14,15,16,19,20,21,23,24,27,32,38,39,40,41,45,50,58`

Full upper-triangle table (rows/cols `0,1,3,7,12,20,38`):

- `0+*: 0,1,3,7,12,20,38`
- `1+*: 2,4,8,13,21,39`
- `3+*: 6,10,15,23,41`
- `7+*: 14,19,27,45`
- `12+*: 24,32,50`
- `20+*: 40,58`
- `38+38=16`

The 42 ordered differences are all nonzero and distinct (machine-checked).

Census checksums (SHA-256 of JSON-encoded sorted rep lists):

- dihedral `2fa9f1d47355effe4c4c6f35be850af5247454cf1e216866056602749e84a603` (3578 reps)
- translation `d87fe6bda33fc10c8e9df6f5d32d3bdebd1c4c1ea4289cda22af97fd340a6615` (7156 reps)

## Proof / Evidence

Deterministic depth-first backtracking, seed 0, no RNG, candidates in increasing order, root `{0}`:

- Maintain occupied difference set `D`. At node `S`, for each `v>max(S)` compute new diffs `(v-a),(a-v)` for `a in S`. Reject `v` if any is `0`, in `D`, or repeats another new diff (including `(v-a)==(a-v)`, i.e. distance 30). Else recurse on `S+{v}`.
- Node = accepted partial Sidon set visited (incl. root). Attempt = candidate `v` trial.
- Soundness/completeness: a set is visited iff every sorted rooted prefix is Sidon; any `k`-set translates to a unique increasing rooted chain, so it is found iff Sidon; pruning only discards sets already failing Lemma 1, whose supersets can never become Sidon.

Frozen run (`n=60`):

- visited nodes 534471, attempts 5169009, ~2.8 s stdlib Python
- depth distribution `1:1, 2:58, 3:1542, 4:22160, 5:151450, 6:309168, 7:50092`
- rooted 7-sets 50092, 8-sets 0
- Depth-2 is 58 not 59 because `v=30` from `{0}` gives diffs `30,30` and is rejected (2-torsion pruning).

Note: an early brief estimated ~441669 nodes under an unspecified node convention. Under the frozen convention above the exact reproducible count is 534471 with identical rooted-7 count 50092; both DFS implementations agree exactly, so the discrepancy is definitional, not mathematical.

Independent verifier (sums-based, independently coded): new sums for `v` are `2v` and `v+a (a in S)`; reject iff they collide among themselves or with stored sums. Cold re-run gives byte-identical visited/attempts/depth/n7/n8. All 3578 dihedral and 7156 translation reps rechecked sums-primary (28) and differences (42, nonzero), plus canonical minimality, pairing, and SHA-256 (16 checks PASS).

Reduction: 50092 rooted 7-sets reduce to 7156 translation-canonical classes (distribution `{7:7156}`) and 3578 dihedral classes (distribution `{2:3578}`).

## Limitations

- Proof of nonexistence/census is computation-dependent (534k-node tree regenerated by script, not human-readable; no proof-assistant certificate). Correctness rests on Python, Lemma 1, and audit of two short scripts.
- Literature recheck incomplete: live HTTPS verification was blocked by transport errors. Obscure optical-orthogonal-code / difference-packing tables may tabulate max 7 at `v=60`; if so the maximum-theorem component overlaps prior tabulation and novelty rests on the certified 3578-class census, explicit sum tables, and replayable log.
- Only `Z_60` is closed. Claims about `Z_58,59,61,62` and `Z_63+` are motivation only, not proved here.
- Certified only for seed 0 increasing order; different orderings would give different node counts but the same census.
- No RNG; ordering increasing is the only search order certified.

## Reproducibility

Requires only Python 3 stdlib; ~3 s + ~5 s:

```
python3 output/artifacts/sidon_search.py --out output/artifacts
python3 output/artifacts/verify.py --dir output/artifacts
```

Verifier exits 0 with `VERIFY PASS` (witness sums/diffs/values, all-rep Sidon, minimality x2, dihedral cover, 2-to-1 pairing, trans-size-7, counts, 2 checksums, cold no-8-set, n7/visited/attempts/depth matches).

## References

- Singer perfect difference sets and projective planes `(57,8,1)` and `(73,9,1)` — existence at 57/73 does not decide 60. https://en.wikipedia.org/wiki/Difference_set
- Optimal Golomb rulers / distributed.net OGR tables (interval Sidon, e.g. 10-mark length 55) — interval packing without wrap-around, explicitly different problem. https://en.wikipedia.org/wiki/Golomb_ruler
- Bose-Chowla construction and counting bound `k(k-1)+1<=n`; OEIS maximal-Sidon tables — give `k<=8` and `k>=7` at 60 but do not close 8 vs 7 nor enumerate extremals. https://oeis.org/A005282
