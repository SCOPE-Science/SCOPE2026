# The commutator-square collapse of T(3,4,5) is A6 of order 360

## Context

Ordinary two-generator triangle-group finiteness is closed by the
spherical/Euclidean/hyperbolic trichotomy. The next finite-vs-infinite
boundary is which short extra relators collapse a hyperbolic baseline to
finite. This record answers one minimal such boundary question: the
commutator-square perturbation of the representative hyperbolic triple
(3,4,5). The object was fixed before computation by two minimality choices:
(3,4,5) is a representative hyperbolic triple in 3 ≤ l ≤ m ≤ n ≤ 6, and
[a,b] is the shortest nontrivial reduced word beyond the triangle relators
with smallest nontrivial exponent k=2.

## Definitions

- Baseline: `T(3,4,5) = <a,b | a^3 = b^4 = (ab)^5 = 1>`, hyperbolic since
  1/3+1/4+1/5 = 47/60 < 1 (infinite by the classical Fuchsian trichotomy,
  cited as background).
- Perturbed group: `G = G(3,4,5;2) = <a,b | a^3 = b^4 = (ab)^5 = [a,b]^2 = 1>`
  with `[a,b] = aba^{-1}b^{-1}`, i.e. last relator `(aba^{-1}b^{-1})^2 = 1`.
- Permutation composition convention: `(pq)(i) = p[q[i]]` (a after b).

## Result

**Theorem.** `G ≅ A6`; in particular `|G| = 360`.
Generator orders are exact: `|a| = 3`, `|b| = 4`, `|ab| = 5`, `|[a,b]| = 2`.
`G` is perfect (trivial abelianization), has trivial center, element-order
distribution `{1:1, 2:45, 3:80, 4:90, 5:144}`, and conjugacy-class sizes
`[1, 40, 40, 45, 72, 72, 90]`. Hence `G` is a proper finite quotient of the
infinite baseline `T(3,4,5)` (equivalently, A6 is a finite quotient of
`T(3,4,5)` factoring through the commutator-square relator).

## Proof / Evidence

**Upper bound |G| ≤ 360 (Todd–Coxeter).** A from-scratch HLT Todd–Coxeter
enumeration over the trivial subgroup (`tc.py`, no GAP/Magma/SmallGroups)
terminates DONE with 360 live cosets (402 definitions, 618 passes,
42 coincidences), recorded as explicit permutations `pa, pb` of
`{0..359}` in `cert_G345k2.json`. The stdlib-only checker
`verify_G345k2.py` confirms: (V1) `pa, pb` are permutations; (V2) all four
defining relators close at all 360 base points (1440 traces); (V3) the
action is transitive from 0, so 360 = |G:1|; (V4) permutation orders
`|a|=3, |b|=4, |ab|=5`, commutator order 2. By standard Todd–Coxeter
correctness a complete closed table over 1 proves `|G| ≤ 360`. The engine
was validated on controls (trivial group → 1, T(2,3,5) → 60,
T(2,3,3) → 12).

**Lower bound |G| ≥ 360 (explicit surjection onto A6).** In S6 let
`a0 = (3 4 5)` (one-line `[0,1,2,4,5,3]`) and
`b0 = (0 1 2 3)(4 5)` (one-line `[1,2,3,0,5,4]`), both even hence in A6.
Direct integer computation (committed in `a6_identification.json`,
rechecked by `verify_a6.py`): `a0^3 = 1`, `b0^4 = 1`,
`a0·b0 = (0 1 2 4 3)` of order 5, `[a0,b0] = (0 5)(3 4)` of order 2.
Thus `a ↦ a0, b ↦ b0` respects all four relators and extends to a
homomorphism `π : G → A6`; BFS from the identity over `{a0^±1, b0^±1}`
visits exactly 360 distinct even permutations = 6!/2, so `<a0,b0> = A6`
and `π` is surjective. Hence `|G| ≥ 360`.

**Conclusion.** `|G| ≤ 360` and `|G| ≥ 360` give `|G| = 360`; a surjection
between finite groups of equal order is an isomorphism, so `G ≅ A6`.
Corollaries (perfectness, center 1, order/class data) agree exactly
between the certificate and the A6 model; an independent BFS on
`<pa,pb> ≤ S_360` has order 360 (faithful action).

**Separation.** The certificate permutations satisfy the three baseline
relators, so G is a quotient image of T(3,4,5); finiteness (360) against
cited infiniteness of T(3,4,5) makes it proper.

## Limitations

- Baseline infiniteness of T(3,4,5) is cited classical background, not
  re-proved.
- Literature position rests on targeted exact-presentation searches plus
  admission triage, not an exhaustive-textbook sweep.
- No general collapse criterion, downstream theorem, or multi-case census
  is claimed. A bounded 76-tuple exploration is reported only as an
  ancillary observation (six closed tables, 70 inconclusive at cap); the
  theorem is independent of it.
- The index-120 consistency file is a corollary of |G|=360 and |a|=3
  (120 orbits of size 3), not an independent Reidemeister–Schreier replay.

## Reproducibility

Run from the record directory (stdlib only, seconds):

- `python3 output/artifacts/verify_G345k2.py` — V1–V6 certificate recheck.
- `python3 output/artifacts/verify_a6.py` — A1–A4 A6 identification recheck.
- Re-enumeration: import `output/artifacts/tc.py`, run
  `Enumeration([[0]*3, [2]*4, [0,2]*5, [0,2,1,3]*2]).run()` → DONE, 360.

Artifacts: `cert_G345k2.json` (closed 360-point table),
`a6_identification.json` (explicit A6 generators),
`structure_G345k2.json` (order/class/center data),
`rs_index_check_G345k2.json` (index-120 consistency),
`tc.py`, `verify_G345k2.py`, `verify_a6.py`.

## References

- Caprace–Conder–Kaluba–Witzel, Hyperbolic generalized triangle groups,
  property (T) and finite simple quotients (arXiv:2011.09276) — infinite
  groups, orthogonal.
- Larsen–Lubotzky–Marion, Deformation theory and finite simple quotients
  of triangle groups I (arXiv:1301.2949) — existence framework, orthogonal.
- Bridson–McReynolds–Reid–Spitler, On the profinite rigidity of triangle
  groups (arXiv:2004.07137) — rigidity, orthogonal.
- Allcock, Triangles of Baumslag–Solitar groups (arXiv:0808.0934) —
  different family.
- Howie–Williams, The Tits alternative for generalized triangle groups of
  type (3,4,2) (arXiv:math/0603682) — different boundary.
- Auditor live arXiv API checks (8 Sept 2026): commutator+triangle-group
  (2 unrelated hits); A6+triangle-group (0 hits); a^3=b^4 (unrelated).
