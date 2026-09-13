# Multi-wall genus-0 double Hurwitz jump at d=9: verified SSV identity

## Context

Double Hurwitz numbers count connected branched covers of the projective line
with two special ramification profiles and otherwise simple branching. By the
work of Goulden–Jackson–Vakil they are piecewise polynomial in the profile
entries; Shadrin–Shapiro–Vainshtein (SSV) determined the genus-0 chamber
structure with walls given by equalities of subset sums
`x_I = y_J`, and Cavalieri–Johnson–Markwig gave tropical monodromy-graph
proofs and wall-crossing formulas. The universal-Picard geometry predicts that
crossing walls changes the number by an explicit signed sum of degenerate
contributions. This record tests that prediction on a concrete multi-wall
example at degree 9: two off-wall chambers sharing one profile, joined by a
segment meeting two walls, with both chamber values and the total jump proved
exactly.

## Definitions

Fix degree `d = 9`, genus `g = 0`, and ordered branch locus `B` of 5 distinct
fixed points in `P^1(C)`: two special points with profiles `mu`, `nu = (5,4)`
and `r = 3` simple points. Riemann–Hurwitz requires
`deficit(mu) + deficit(nu) + r = 2d - 2`, i.e. `6 + 7 + 3 = 16` for both pairs:

- `mu_A = (6,2,1)`, `nu = (5,4)`, `r = 3` (chamber A);
- `mu_B = (3,3,3)`, `nu = (5,4)`, `r = 3` (chamber B).

The connected double Hurwitz number `H` is the sum of `1/|Aut(f)|` over covers
fixing `B` pointwise. Equivalently, via the Frobenius–Burnside class algebra,
`H = N_trans / 9!` where `N_trans` counts transitive tuples
`(a, b, t_1, t_2, t_3)` in `S_9` with `a` of type `mu`, `b` of type `nu`, each
`t_i` a transposition, product `t_3 t_2 t_1 b a = 1`, modulo simultaneous
conjugation. Both pairs are off-wall: proper subset sums of `mu_A` are
`{1,2,3,6,7,8}`, of `mu_B` are `{3,6}`, of `nu` are `{4,5}`, pairwise disjoint.
Let `F(mu, k) = H^{disconn}_{g=0}(mu, k; r = 2)` denote the genus-0
disconnected double Hurwitz number with 2 simple points.

The segment `mu(s) = (6-3s, 2+s, 1+2s)` from A to B meets exactly the walls
`s = 1/3` (resonances `m_1 = 5`, `m_23 = 4`) and `s = 2/3` (resonances
`m_1 = 4`, `m_23 = 5`), with deltas `{4, 5}`.

## Result

**Theorem.** With the normalization above,

```
H_A = 324,  H_B = 40,  H_B - H_A = -284
  = 9  * (F(B,(9,))     - F(A,(9,)))
  + 8  * (F(B,(4,4,1))  - F(A,(4,4,1)))
  + 6  * (F(B,(4,3,2))  - F(A,(4,3,2)))
  + 3  * (F(B,(5,3,1))  - F(A,(5,3,1)))
  + 4  * (F(B,(5,2,2))  - F(A,(5,2,2)))
  = (-135) + (-48) + (-40) + (-37) + (-24).
```

The five `k` are exactly the one-step cut/join children of `nu = (5,4)`: the
join `(9,)` (weight `5*4 = 20`) and the four cuts `(4,4,1)`, `(4,3,2)`,
`(5,3,1)`, `(5,2,2)` with weights `5, 5, 4, 2`. The prefactors
`9, 8, 6, 3, 4` equal `M[k,nu]*|C_nu|/|C_k|`. The individual factors are:

| k | F(B,k) | F(A,k) | difference | coeff | term |
|---|---|---|---|---|---|
| (9,) | 3 | 18 | -15 | 9 | -135 |
| (4,4,1) | 0 | 6 | -6 | 8 | -48 |
| (4,3,2) | 4/3 | 8 | -20/3 | 6 | -40 |
| (5,3,1) | 5/3 | 14 | -37/3 | 3 | -37 |
| (5,2,2) | 0 | 6 | -6 | 4 | -24 |

## Proof / evidence

Transitivity is forced combinatorially: a disconnected tuple would induce a
common proper subset sum of `(mu, nu)` from its block sizes; the only common
subset sums are `{0, 9}`, so every tuple is transitive and connected equals
disconnected counts with `H = N/9!` exactly
(`N_A = 117573120`, `N_B = 14515200`, both divisible by `9!`).

Character sums: Murnaghan–Nakayama recursion from scratch in exact `Fraction`
arithmetic, self-checked by `sum dim^2 = 9!` and by transposition characters
equaling content sums, gives `H_A = 324`, `H_B = 40`. An independent
Frobenius power-sum/Vandermonde character implementation with zero shared code
agrees on the full needed table and reproduces both values.

Character-free cross-check: the `30x30` left-transposition-action matrix `M`
built from direct permutation products on canonical representatives satisfies
`N = |C_nu| (M^3)[mu,nu]` and yields identical `N_A`, `N_B`, calibrated against
raw tuple enumeration at `d <= 4`.

Wall-crossing identity: peel the last transposition,
`(M^3)[mu,nu] = sum_k M[k,nu] (M^2)[mu,k]`. Rebuilding `M` shows the only
nonzero `k` are the five children above with hand-verified weights
`{20, 5, 5, 4, 2}`. Differencing `mu_B - mu_A` and multiplying by
`|C_nu| = 18144` gives
`N_B - N_A = sum_k M[k,nu] (|C_nu|/|C_k|) (N_2(B,k) - N_2(A,k))` with integer
automorphic coefficients `9, 8, 6, 3, 4` (the `8` uses
`|C_(4,4,1)| = 9!/(4*4*2!)`); dividing by `9!` yields the boxed identity. All
ten smaller `r = 2` factors are evaluated by characters and independently
confirmed by matrix powers with exact agreement. The join term spans both
walls; each cut term carries its wall delta (`5, 5, 4, 4/2`).

## Limitations

No raw `S_9` tuple enumeration was performed (infeasible at `9!` scale);
cross-checks are two independent character implementations plus
character-free class-algebra matrix powers calibrated at `d <= 4`. The
tropical CJM monodromy-graph count was attempted but its vertex-multiplicity
rule could not be pinned down reliably in-session, so it is not used for any
claimed number; the SSV identity is proved in exact class-algebra form, which
implies the same jump the tropical geometry predicts. The five terms are
grouped by `nu`-side degeneration type; the finer split into single-resonance
contributions is described but the proved equation is the five-term form.

## Reproducibility

Run `python3 output/artifacts/char_sum.py` for the MN character sums and
self-checks; `python3 output/artifacts/t11_gjv.py` for the matrix pipeline;
the `hurwitz_double` function in `char_sum.py` with `r = 2` reproduces each
`F(mu,k)`; `t29_final.py` assembles the five-term identity and
`t32_smallcross.py` cross-checks all ten factors against matrix powers.

## References

- I. P. Goulden, D. M. Jackson, R. Vakil, Towards the geometry of double
  Hurwitz numbers, Adv. Math. 198 (2005).
- S. Shadrin, M. Shapiro, A. Vainshtein, Chamber behavior of double Hurwitz
  numbers in genus 0, Adv. Math. 217 (2008).
- R. Cavalieri, P. Johnson, H. Markwig, Tropical Hurwitz numbers, J. Alg.
  Combin. 32 (2010); Wall crossings for double Hurwitz numbers, Adv. Math.
  (2011).
- M. Kazarian, S. Lando, D. Zvonkine, Double Hurwitz numbers and
  multisingularity loci in genus 0.
