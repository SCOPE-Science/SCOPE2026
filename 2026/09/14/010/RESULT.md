# Disproof of the single-crossing two-box uniform free-power merger

## Statement

Let `mu = (1/2) Unif[-2,-1] + (1/2) Unif[1,2]` and for `t >= 1` let
`mu^{boxplus t}` denote the Nica-Speicher free additive convolution power,
defined by `R_{mu^{boxplus t}} = t R_mu`.
The admitted target asked whether there exists a unique finite merging time
`t_m > 1`, given as the unique root in `(1, infinity)` of the explicit Huang
subordination fixed-point boundary equation for this `mu`, such that
`supp(mu^{boxplus t})` has exactly two disjoint compact interval components
for `1 <= t < t_m` and exactly one compact interval for `t > t_m`.

## Context

Free convolution powers `mu^{boxplus t}` are governed by Bercovici-Voiculescu
subordination in Huang's fixed-point form. General theory (Huang; Belinschi-
Bercovici-Ho; Bao-Erdos-Schnelli) shows component counts are nonincreasing
and connected inputs stay connected, but gives no exact evaluation for this
disconnected uniform two-box law. The question was whether the initial gap
`(-1,1)` fills only at a later finite merger time.

## Definitions

- `G_mu(w) = integral (w-x)^{-1} dmu(x)`, `F_mu = 1/G_mu`.
- `H_t(w) = t w - (t-1) F_mu(w)`.
- For each `z` in the upper half-plane `C^+` there is a unique
  `omega_t(z)` in `C^+` with `H_t(omega_t(z)) = z`, and
  `G_{mu^{boxplus t}}(z) = G_mu(omega_t(z))`.
- `S_t = supp(mu^{boxplus t})`, compact for each `t >= 1`.

## Result

**Theorem.** For every `t > 1`, `0 in S_t`. Consequently there is no
`t_m > 1` such that `S_t` is exactly two disjoint compact intervals for
`1 <= t < t_m` and one compact interval for `t > t_m`. The claimed
single-crossing `2 -> 1` merger with Huang-equation root
`t_m in (1, infinity)` is false. Central mass is born immediately at
`t = 1^+`, a different topological pattern from the one claimed.
At `t = 1`, `S_1 = [-2,-1] U [1,2]` does have two components.

## Proof / evidence

1. Symmetry: `mu` is symmetric, so odd free cumulants vanish; scaling
   preserves this, hence each `mu^{boxplus t}` is symmetric and each `S_t`
   is a symmetric closed set.
2. Imaginary-axis reduction: for `v > 0`,
   `G_mu(i v) = -i A(v)` with `A(v) = integral v/(x^2+v^2) dmu(x) > 0`,
   so `F_mu(i v) = i/A(v)` and `H_t(i v) = i f_t(v)` with
   `f_t(v) = t v - (t-1)/A(v)`. By the symmetry
   `H_t(-bar w) = -overline{H_t(w))` and uniqueness of the subordination
   point, `omega_t(i eta) = i v(eta)` for some `v(eta) > 0`, with
   `f_t(v(eta)) = eta` and `G_{mu^{boxplus t}}(i eta) = -i A(v(eta))`.
3. Uniform enclosure: since `supp(mu) subset {1 <= |x| <= 2}`,
   `v/(4+v^2) <= A(v) <= v/2`. Hence
   `f_t(v) < 0` for `0 < v < m(t) := sqrt(2(t-1)/t)` and
   `f_t(v) > 1` for `v > M(t) := (1+sqrt(1+16(t-1)))/2`.
   So for `eta in (0,1]`, `m(t) <= v(eta) <= M(t)` and
   `-Im G_{mu^{boxplus t}}(i eta) = A(v(eta)) >= m(t)/(4+M(t)^2) =: c(t) > 0`.
4. Support conclusion: if `0 not in S_t` then with
   `r = dist(0,S_t) > 0`, `|Im G(i eta)| <= eta/r^2 -> 0`, contradicting the
   uniform positive lower bound. Hence `0 in S_t` for all `t > 1`.
5. Parity obstruction: a symmetric closed set with exactly two disjoint
   compact interval components cannot contain `0` (if `-J_i = J_i` then it
   contains `0` and two such intervals intersect; hence components must be
   swapped, `-J_1 = J_2`, disjoint from `0`). Since `0 in S_t` for all
   `t > 1`, no `S_t` with `t > 1` is exactly two intervals, refuting the
   required regime on `[1, t_m)` for any `t_m > 1`.

Numerical certification in `artifacts/verify_disproof.py` confirms
`integral x^{-2} dmu = 1/2`, the two-sided `A(v)` bounds and sign
thresholds at several `t`, and subordination spot-checks giving positive
approximate density `0.048-0.11` at `0` for `t = 1.05, 1.2, 2.0`.

## Limitations

This is a disproof of the stated single-crossing `2 -> 1` merger only. It
does not certify the full later support evolution (exploratory numerics
suggest a `2 -> 3 -> 1` pattern with outer-central merger near
`t approximately 1.27`, left uncertified), nor closed-form support edges or
densities away from zero.

## Reproducibility

Run `python3 artifacts/verify_disproof.py` (requires `mpmath`); all checks
pass. The proof uses only elementary Stieltjes bounds, standard
subordination existence/uniqueness, and Stieltjes inversion.

## References

- H.-W. Huang, Supports of Measures in a free additive convolution
  semigroup, arXiv:1205.5542.
- Z. Bao, L. Erdos, K. Schnelli, On the support of the free additive
  convolution, arXiv:1804.11199.
- S. Belinschi, H. Bercovici, C.-W. Ho, On the support of free
  convolutions, arXiv:2408.06573.
