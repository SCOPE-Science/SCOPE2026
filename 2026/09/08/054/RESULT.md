# Explicit flat-moduli stability for Loewner's torus inequality: deficit controls distance to the hexagonal torus

## Context

Loewner's torus inequality states that every unit-area flat 2-torus satisfies
`sys^2/area <= 2/sqrt(3)`, with equality only at the hexagonal torus.
The sharp constant and abstract equality characterization are prior work;
no explicit quantitative stability modulus bounding the deficit by moduli
distance to the hexagonal point was known.

## Definitions

- `T`: unit-area flat 2-torus, parametrized by `tau = x + iy` in the closed
  `SL(2,Z)` fundamental domain `D = {|x| <= 1/2, x^2+y^2 >= 1}`, `y >= y_h := sqrt(3)/2`,
  via the lattice `Lambda_tau = y^{-1/2}(Z + tau Z)` (area 1).
- Hexagonal class `[T_hex]`: corners `tau_h^pm = +-1/2 + i y_h` in `D`.
- Loewner deficit: `delta(T) = 2/sqrt(3) - sys(T)^2`.
- `d_hyp`: hyperbolic quotient distance on `M = SL(2,Z)\H`;
  `d(.,.)` denotes hyperbolic distance on `H`, `cosh d = 1 + |tau-tau_h|^2/(2 y y_h)`.

## Result

For every unit-area flat 2-torus `T`, with `d = d_hyp([T],[T_hex])`:

```
delta(T) >= (1/2) * min(d^2, 1),
```

with `delta = 0` only at the hexagonal torus. In particular the explicit
constant `c = 1/2` works globally over the full moduli space.

## Proof / evidence

1. **Systole (Lemma 1).** For `tau in D`, `sys(Lambda_tau)^2 = 1/y`, so
   `delta(y) = 2/sqrt(3) - 1/y` depends only on `y`.
   Proof: `|m+n tau|^2 = m^2+2mnx+n^2(x^2+y^2) >= m^2-|mn|+n^2 >= 1`
   for `(m,n) != (0,0)` (using `|x| <= 1/2`, `x^2+y^2 >= 1`), equality at `(1,0)`;
   scale by `y^{-1/2}`.
2. **Quotient bound (Lemma 2).** `d_c(tau) = min_+- d(tau,tau_h^pm)` satisfies
   `d_hyp([tau],[tau_hex]) <= d_c(tau)` since `H -> M` is distance-nonincreasing.
   As `r -> min(r^2,1)` is nondecreasing, it suffices to bound `d_c`.
3. **Reduction to one variable.** For fixed `y`, `delta` is fixed and `d_c`
   increases in `u = 1/2-|x|`. For `y >= 1` the maximum is at `x = 0`;
   for `y_h <= y < 1` the constraint `x^2+y^2 >= 1` forces the maximum on the
   arc `|x| = sqrt(1-y^2)`. Define `N(y)`, `t_max(y) = N(y)/(2 y y_h)`,
   `d_max(y) = acosh(1+t_max(y))`; it suffices to show
   `delta(y) >= (1/2) min(d_max(y)^2,1)`.
4. **Universal estimate.** `d^2 <= 2t` where `t = cosh d - 1`, from
   `cosh z = sum z^{2k}/(2k)! >= 1+z^2/2`. So `delta >= t_max` implies the claim.
5. **Key identity.** `sqrt(3) y delta(y) = 2y - sqrt(3)` and
   `sqrt(3) y t_max(y) = N(y)` (since `2 y_h = sqrt(3)`), so
   `delta - t_max = [(2y-sqrt(3)) - N(y)]/(sqrt(3) y)`.
6. **Compact piece `y_h <= y <= 8/5`: `delta >= t_max`.**
   - `1 <= y <= 8/5`: `g(y) = 2y-sqrt(3)-1/4-(y-y_h)^2 >= 0` because
     `g(1) = 0` exactly in `Q(sqrt(3))` and
     `g'(y) = 2(1+y_h-y) >= 2(y_h-3/5) > 0` (from `1.732^2 < 3`).
   - `y_h <= y <= 1`: with `w = sqrt(1-y^2)`, `N(y) = 2-w-sqrt(3) y` exactly;
     need `w >= (2+sqrt(3))(1-y)`; both sides `>= 0`, squaring gives
     `(1-y)(1+y) >= (7+4sqrt(3))(1-y)^2`, i.e. for `y < 1`
     `y >= (3+2sqrt(3))/(4+2sqrt(3)) = sqrt(3)/2 = y_h` exactly
     (using only `(sqrt(3))^2 = 3`).
7. **Cap inactive on `[y_h, 8/5]`.** `delta <= delta(8/5) = 2/sqrt(3)-5/8 <= 13/24`
   since `2/sqrt(3) <= 7/6 iff 144 <= 147`; and
   `cosh 1 - 1 >= 1/2+1/24+1/720 = 391/720 >= 13/24`, so `d_max <= 1`.
8. **Tail `y >= 8/5`.** `delta >= delta(8/5) >= 1/2` since
   `2/sqrt(3) >= 9/8 iff 256 >= 243`; RHS `<= 1/2`.
9. **Equality case.** `delta = 0 iff y = y_h`, forcing `x = +-1/2`, i.e. hex class.
10. **Replay.** `artifacts/verify_stability.py` (stdlib only) replays all
    integer-exact thresholds (`144<=147`, `256>=243`, `391>=390`, `1732^2<3`,
    threshold identity) and prints ALL CHECKS PASSED (15); float scan finds
    worst ratio `~0.5127` at `(x,y) = (0,1)`, consistent with `c = 1/2`
    (near-sharp for this route; optimality not claimed).

## Limitations

- Restricted to flat unit-area 2-tori; no claim for non-flat metrics or higher genus.
- Constant `c = 1/2` is near-sharp for this route (numeric worst `~0.5127`)
  but global optimality is not claimed.
- Quotient-distance step uses the folded-corner upper bound (valid direction
  for a deficit lower bound).

## Reproducibility

Run `python3 artifacts/verify_stability.py` (stdlib only); must print
`ALL CHECKS PASSED`. All analytic steps use only `(sqrt(3))^2 = 3` and
positive-term series truncation plus the integer inequalities above.

## References

- V. Bangert, M. Katz, An optimal Loewner-type systolic inequality and harmonic
  one-forms of constant norm, arXiv:math/0304494. Sharp inequality, abstract
  equality via Abel-Jacobi/submersion and Berge-Martinet lattices; no stability modulus.
- C. Horowitz, K. U. Katz, M. G. Katz, Loewner's torus inequality with
  isosystolic defect, arXiv:0803.0690. Conformal-variance defect within a class;
  no flat-moduli distance bound.
- J. Eyll, Stability of systolic inequalities for the Mobius strip and Klein
  bottle, arXiv:2502.13715. L2-conformal-factor stability for different surfaces.
- D. Bonforte et al., Stability in Gagliardo-Nirenberg-Sobolev inequalities,
  arXiv:2007.03674. Evidences recognized explicit-stability program; different inequality.
