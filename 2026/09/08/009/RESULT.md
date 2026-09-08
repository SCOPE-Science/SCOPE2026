# A non-CI Pfaffian Gorenstein ideal at the char-3 exceptional Hilbert function, with resolution and Jordan-type separation from the CI exception

## Context

Let `K = F_3`, `R = K[x,y,z]`. In characteristic zero every codimension-3
complete intersection has the Weak Lefschetz Property, and recent theorems
close the codimension-3 Gorenstein Lefschetz question for small Sperner
number in characteristic zero. In characteristic 3 the published boundary is
a single complete-intersection datum: every CI with Hilbert function
`(1,3,5,5,3,1)` has WLP except, after change of variables,
`I0 = (x^2, y^3, z^3)` (Boij–Migliore–Miró-Roig–Nagel–Zanello, Lemma 3.7).
By the Buchsbaum–Eisenbud structure theorem every non-CI codimension-3
Gorenstein ideal is Pfaffian (submaximal Pfaffians of an alternating matrix).
The question decided here: does the non-CI Pfaffian locus at the same
exceptional Hilbert function share the CI resolution and Jordan behavior,
or diverge?

## Definitions

- Alternating matrix `M` (`M[i][i] = 0`, `M[j][i] = -M[i][j]`); its five
  submaximal Pfaffians `Pf_k` (Pfaffian of the 4x4 block omitting row/column
  `k`: `M_ab*M_cd - M_ac*M_bd + M_ad*M_bc`) generate the Pfaffian ideal `J`.
- Grade-3 Gorenstein non-CI: `R/J` Artinian of socle dimension 1 with a
  minimal graded resolution of ranks `1-5-5-1` (a complete intersection has
  ranks `1-3-3-1`).
- Jordan partition of a linear form `L`: block sizes of multiplication by `L`
  on the Artinian quotient (length 18 here), recovered from nullities of
  powers of the multiplication matrix.
- All computation is exact linear algebra over `F_3` (Macaulay matrices,
  Gauss–Jordan rank, quotient-basis multiplication matrices). No floating
  point, no Groebner bases.

## Result (theorem, proved + computed)

Let `M` be the alternating 5x5 matrix over `F_3[x,y,z]` with upper triangle:

| entry | polynomial |
|---|---|
| M12 | 0 |
| M13 | x + 2y + z |
| M14 | y + 2z |
| M15 | x^2 + yz + y^2 |
| M23 | 2x |
| M24 | y |
| M25 | 2x^2 + 2xz + 2y^2 + 2yz + 2z^2 |
| M34 | 2xy + 2y^2 + yz |
| M35 | x^3 + 2x^2y + x^2z + xy^2 + 2xyz + xz^2 + 2y^3 + yz^2 |
| M45 | 2x^3 + x^2y + x^2z + 2xy^2 + 2xyz + 2xz^2 + 2y^3 + 2yz^2 + 2z^3 |

Let `J` be the ideal of its five submaximal Pfaffians:

- Pf0 (omit 0), deg 4: `x^4 + 2x^3z + x^2y^2 + x^2z^2 + xy^3 + xz^3 + 2y^4 + 2y^2z^2 + 2yz^3`
- Pf1 (omit 1), deg 4: `2x^4 + 2x^3y + x^3z + x^2y^2 + x^2z^2 + 2xy^3 + 2xz^3 + y^4 + y^3z + y^2z^2 + yz^3 + 2z^4`
- Pf2 (omit 2), deg 3: `2x^2y + 2x^2z + xyz + 2xz^2 + 2y^3 + y^2z + 2z^3`
- Pf3 (omit 3), deg 3: `2x^2y + 2x^2z + 2xyz + 2xz^2 + 2y^3 + z^3`
- Pf4 (omit 4), deg 2: `xy + xz + y^2 + 2yz`

Then:

(a) `R/J` is Artinian with Hilbert function `(1,3,5,5,3,1)` (Macaulay-matrix
    ranks; quotient vanishes in degrees 6 and 7), socle concentrated in
    degree 5 with dimension 1.

(b) All five Pfaffians are minimal generators (per-degree rank gain 1 in
    degree 2, 2 in degree 3, 2 in degree 4), so `mu(J) = 5`: `J` is NOT a
    complete intersection. Since `M` is alternating with no nonzero constant
    entries and `R/J` is Artinian of length 18 (hence grade 3), the
    Buchsbaum–Eisenbud theorem gives the minimal graded resolution
    `0 -> R(-8) -> R(-6)+R(-5)^2+R(-4)^2 -> R(-4)^2+R(-3)^2+R(-2) -> R`
    (ranks `1-5-5-1`; i.e. `F1 = [2,3,3,4,4]`, `F2 = [4,4,5,5,6]`,
    `F3 = [8]`), whose graded Euler characteristic
    `1 - t^2 - 2t^3 + 2t^5 + t^6 - t^8` equals the Hilbert numerator
    `(1+3t+5t^2+5t^3+3t^4+t^5)(1-t)^3` in every degree. So `J` is Gorenstein
    non-CI of Pfaffian type.

(c) The known CI exception `I0 = (x^2, y^3, z^3)` has minimal resolution
    `0 -> R(-8) -> R(-6)+R(-5)^2 -> R(-3)^2+R(-2) -> R` (ranks `1-3-3-1`).
    The graded Betti tables of `R/J` and `R/I0` DIFFER (`1-5-5-1` vs
    `1-3-3-1`).

(d) Jordan separation on every `F_3`-rational form: for EVERY nonzero linear
    form `L` over `F_3` (all 26), the Jordan partition of multiplication by
    `L` on `R/J` differs from that on `R/I0`. Example `L = x+y+z`: `R/J`
    has `[5,5,3,3,2]` (power nullities `0,5,10,14,16,18`) vs `R/I0`
    `[3,3,3,3,3,3]` (nullities `0,6,12,18`). Full census: `R/I0` is `[3^6]`
    on 24/26 forms (`[2^9]` on 2/26); `R/J` takes 7 other partitions and
    NEVER `[3^6]` or `[2^9]`:
    `(6,4,4,2,2):10, (6,4,4,2,1,1):4, (5,5,4,2,2):4, (5,5,4,2,1,1):2,`
    `(6,4,4,1,1,1,1):2, (6,4,3,3,2):2, (5,5,3,3,2):2`.

## Proof / evidence

Exact replay: `python3 output/artifacts/verify_lane109.py` (stdlib only,
~1–2 min) checks Hilbert, Pfaffian degrees, per-degree minimal-generator
rank gains, socle dimensions, quotient-basis multiplication matrices, power
nullities, Jordan partitions, and the 26-form census. The auditor re-ran it
fresh and reproduced every number, and additionally reimplemented
Hilbert/socle/mingens/Jordan from an independent transcription of the matrix
with fresh elimination code: exact agreement. The graded shifts in (b) are
forced (not separately syzygy-computed in the script): generator degrees fix
`F1 = [2,3,3,4,4]`; codimension-3 Gorenstein duality with socle degree 5
fixes `F3 = [8]` and `F2 = 8 - F1 = [4,4,5,5,6]`; the Euler identity against
the Hilbert numerator was verified numerically. `M` has no units, so the BE
complex is minimal. The `I0` resolution is the Koszul resolution of type
`(2,3,3)`.

## Limitations

- The matrix was found by random search in one feasible degree pattern
  (`M12 = 0` zero entry is necessary; an all-positive-degree box yields no
  `(2,3,3,4,4)` model); no classification of the non-CI locus is claimed.
- "Generic Jordan type" is over the finite field `F_3` (census of all 26
  nonzero forms); separation holds on every form, stronger than generic.
- No WLP/SLP verdict for `R/J` is claimed beyond the Jordan data.
- DRAFT's phrase "`x^5,y^5,z^5` in `J`" is corrected here: `z^5` lies in
  `J_5` but `x^5, y^5` enter at degree 6; Artinian status follows from
  vanishing in degrees 6–7. The replay script's docstring overstates its
  scope (it executes Hilbert/socle/Jordan checks; resolution shifts and
  Euler are deduced as above, not syzygy-computed in-script).
- Prior-art gap rests on the five checked sources (full text for the two
  dispositive ones); an obscure non-arXiv source with the same matrix cannot
  be logically excluded.

## Reproducibility

`output/artifacts/verify_lane109.py` — stdlib-only Python 3; run
`python3 output/artifacts/verify_lane109.py`; expected tail line
`ALL 26 NONZERO LINEAR FORMS SEPARATE. VERIFIED.` Exit nonzero on any
mismatch (assertions on Hilbert, gains, socle, and pairwise Jordan
inequality).

## References

- M. Boij, J. Migliore, R. Miró-Roig, U. Nagel, F. Zanello, On the Weak
  Lefschetz Property for Artinian Gorenstein algebras of codimension three,
  arXiv:1302.5742 (J. Algebra 403 (2014), 48–68). — CI-only char-3 data:
  Lemma 3.7 (`I = (x^2,y^3,z^3)` at `(1,3,5,5,3,1)`), Theorem 3.8
  (`(1,3,6,6,3,1)` exception).
- N. Abdallah, N. Altafi, A. Iarrobino, A. Seceleanu, J. Yaméogo, Lefschetz
  properties of some codimension three Artinian Gorenstein algebras,
  arXiv:2203.01258. — SLP for Sperner ≤ 6 in characteristic zero.
- M. Boij, J. Migliore, R. Miró-Roig, U. Nagel, The weak Lefschetz property
  for artinian Gorenstein algebras of small Sperner number,
  arXiv:2406.17943. — WLP for Sperner ≤ d+1.
- B. Costa, R. Gondim, The Jordan type of graded Artinian Gorenstein
  algebras, arXiv:1811.02072. — mixed-Hessian Jordan-type machinery.
- N. Abdallah, N. Altafi, A. Iarrobino, J. Yaméogo, Jordan degree type for
  codimension three Gorenstein algebras of small Sperner number,
  arXiv:2406.06322. — complete JDT for almost-constant
  `T = (1,3,s^k,3,1)`, `s = 3,4,5`, characteristic zero.
- D. Buchsbaum, D. Eisenbud, Algebra structures for finite free resolutions,
  and some structure theorems for ideals of codimension 3, Amer. J. Math. 99
  (1977), 447–485. — structure theorem for grade-3 Gorenstein ideals.
