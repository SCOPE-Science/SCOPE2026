# Finite-monodromy seeds can never yield the Boalch–Klein 7-branch Painlevé VI solution

## Context

The Boalch–Klein solution `y_K(t)` is the 7-branch algebraic solution of Painlevé VI of order-168 complex-reflection (Klein, `PSL_2(7)`) origin constructed in Boalch, math/0308221. It has exponent `theta_K = (2,2,2,4)/7` and Painlevé parameters `(alpha,beta,gamma,delta) = (9,-4,4,45)/98`, with rational parametrisation

```
y = -(5s^2-8s+5)(7s^2-7s+4) / (s(s-2)(s+1)(2s-1)(4s^2-7s+7)),
t = (7s^2-7s+4)^2 / (s^3(4s^2-7s+7)^2).
```

The admitted target asked for the minimal RS-pullback degree for `y_K`: either an explicit degree-`<=10` realization (alternative A) or a proof that every RS realization has degree `>=11` (alternative B). The degree-`<=10` Hurwitz enumeration leaves degrees 7–10 open (32, 95, 411, 1401 order-7-compatible integer profiles), and infinite-monodromy seeds form an infinite family, so the full dichotomy remains blocked. The headline below is the emergent lemma that closed completely during that investigation.

## Definitions

An RS-pullback realization of a Painlevé VI solution means: a Gauss hypergeometric (seed) equation `H` with three singular points, a rational cover `phi: P^1 -> P^1` of degree `d` (R-part), and Schlesinger transformations (S-part) such that the pullback `phi^*H` transformed by the S-part is a four-point Fuchsian equation whose isomonodromic flow projects to the given solution. Pullback replaces each local monodromy `g` by a conjugate of a power `g^k` (ramification index `k`); the S-part preserves the monodromy representation up to conjugacy. Hence the projective monodromy group of the target is isomorphic to a subgroup of the projective monodromy group of the seed.

A finite-monodromy seed is a hypergeometric equation with finite projective monodromy. Up to equivalence these are Schwarz's list: cyclic, dihedral, tetrahedral (`A_4`), octahedral (`S_4`), icosahedral (`A_5`). The binary (`SL_2`) covers have orders `2n` (cyclic), `4n` (binary dihedral), `24` (binary tetrahedral), `48` (binary octahedral), `120` (binary icosahedral).

## Result

**Theorem.** No RS-pullback realization of the Boalch–Klein solution `y_K` can arise from a finite-monodromy (Schwarz-list) hypergeometric seed, in any degree `d >= 1`. That is, there is no rational cover `phi` of any degree and no Schlesinger transformation taking a Gauss hypergeometric equation with finite projective monodromy to a Fuchsian equation whose isomonodromic deformation is `y_K`.

## Proof / evidence

Boalch (math/0308221) gives one branch's explicit `SL_2(C)` triple with `phi = e^{2 pi i/7}`:

```
M_1 = diag(phi, phi^{-1}),
M_2 = [[w, x], [-x, conj(w)]],  M_3 = [[w, mu x], [-x/mu, conj(w)]],
```

with `w = (1+phi^2)/(phi-phi^3)`, `x = sqrt(1-|w|^2) ~ 0.603 > 0` real, `|mu| = 1`. Consequences used: (i) `M_1` has exact order 7; (ii) `tr M_2 = 2cos(2pi/7)`, so `M_2` is elliptic of exact order 7 with eigenvalues `e^{+-2pi i/7}`; (iii) `x != 0` with `M_1` diagonal of distinct eigenvalues gives `[M_1,M_2] != 0`, and projectively `M_1 M_2 = lambda M_2 M_1` would require `lambda = phi^2 != +-1`, so the projective images also do not commute.

Suppose an RS realization from a finite seed existed. By the inclusion above, `y_K`'s projective monodromy (containing noncommuting elements of order 7) would embed in the finite seed group. Seed-by-seed: (1) `A_4`, `S_4`, `A_5` have element orders in `{1,2,3}`, `{1,2,3,4}`, `{1,2,3,5}` — no element of order 7; pullback sends local monodromy to powers (orders divide), so an order-7 target element forces an order multiple of 7 in the seed; the binary covers of orders 24, 48, 120 are likewise not divisible by 7 (Lagrange). (2) Cyclic seeds are abelian but `M_1, M_2` do not commute. (3) In a dihedral group every element of odd order lies in the cyclic rotation subgroup, so any two order-7 elements commute; the same holds for binary dihedral groups, where every element outside the cyclic subgroup has even order (since `(a^k x)^2 = a^n` has order at most 2). This contradicts the noncommuting order-7 pair `(M_1, M_2)`. Hence no finite seed works, in any degree.

Machine checks (exact sympy): the parametrisation satisfies Painlevé VI with `(9,-4,4,45)/98` as an exact rational identity (residual numerator identically 0) and lies on Boalch's solution-curve polynomial `F(t,y)` (identically 0); the `W_a(F_4)` alcove-reduction word from `(2,2,2,4)/7` to `(5,2,1,0)/7` has length 11 with two saturated walls; the genus-0 passport scoping gives 0 order-7-compatible profiles for degrees `<=6` and 32/95/411/1401 for degrees 7/8/9/10.

Novelty: Boalch's Inequivalence Theorem proves `y_K` is not Okamoto-equivalent to any finite-subgroup solution (a statement about the `W_a(F_4)` orbit relation); the present theorem concerns the RS-pullback relation (rational pullback plus Schlesinger), which is strictly coarser — one cover can yield Okamoto-inequivalent solutions — so neither implies the other. Kitaev's only Klein RS row (Cross, degree 12) uses the infinite hyperbolic seed `(1/7,1/2,1/3)`.

## Limitations

This theorem covers finite seeds only. It does not decide whether an infinite-monodromy hypergeometric seed could yield `y_K` in degree `<= 10` (target alternative A), nor does it prove a universal degree bound `>= 11` (target alternative B). The integer-profile filter alone cannot close that gap (degrees 7–10 admit many positive-dimensional Hurwitz profiles), and the alcove ledger gives no descent to a tabulated RS row (denominator 7 blocks half-integer resonance).

## Reproducibility

- `output/artifacts/klein_pvi_check.py` — exact PVI + curve check (PASS).
- `output/artifacts/alcove_reduction.py` — `W_a(F_4)` word + walls (PASS).
- `output/artifacts/passport_enumeration.py` — ramification-profile counts (PASS).
- `output/artifacts/finite_seed_obstruction.md` — lemma record with full proof.

## References

- P. Boalch, The Klein solution to Painlevé VI, math/0308221 (explicit triple, infinitude lemma, `(y(s),t(s))`, `F(t,y)`, Sec. 6 Inequivalence Theorem).
- P. Boalch, The fifty-two icosahedral solutions to Painlevé VI, math/0406281 (classification, standard alcove (7)).
- A. Kitaev, Special functions of isomonodromy type, nlin.SI/0309078 (Cross `RS^2_4` row, degree 12).
- R. Vidunas, A. Kitaev, Computation of RS-pullback transformations, arXiv:0705.2963 (RS theory, Theorems 3.1/4.1).
- R. Vidunas, arXiv:1212.3803 (Belyi tables).
