# Non-semistability obstruction for the named quintic Tyurin pencil

## Context

The admitted target asked for a Schmid nilpotent-orbit / SL2-orbit plus
Clemens–Schmid analysis of a named quintic degeneration
`Xt = {l*q + t*q5 = 0}` in `P^4`, with `H = {l=0}` a hyperplane,
`Q = {q=0}` a quartic, meeting along a quartic K3 surface
`S = H cap Q`, deciding a conjectured 1/202/1 limit weight table and a
nonsplit Abel–Jacobi extension. That program presupposes a smooth total
space and a simple-normal-crossing d-semistable central fiber
`H union Q` so that the bare-triple `(H,Q,S)` Clemens–Schmid sequence applies.

This record reports the emergent obstruction found while executing the
target's own first steps: the central-fiber geometry is smooth as stated,
but the total space is singular and the central fiber is not d-semistable,
so the bare `(H,Q,S)` route is inapplicable without semistable reduction.

## Definitions

Work in `P^4` with homogeneous coordinates `[x0:x1:x2:x3:x4]` over `C`.
Define:

- `l = x0`
- `q = x0^4 + x1^4 + x2^4 + x3^4 + x4^4 + x0*x1^3 + x0*x2^3`
- `q5 = x0^5 + x1^5 + x2^5 + x3^5 + x4^5 + x0^3*x1^2`
- `F = l*q + t*q5 = x0*q + t*q5` on `P^4 x D`, `D = {0<|t|<epsilon}`
- `H = {l=0} = {x0=0}`, `Q = {q=0}`, `S = H cap Q`
- `C = S cap {q5=0}`, i.e. at `x0=0`: `{sum_{i=1..4} xi^4 = 0, sum_{i=1..4} xi^5 = 0}` in `P^3`
- `X = {F=0} subset P^4 x D`, central fiber `X0 = H union Q`

Friedman d-semistability for a two-component normal-crossing
`V1 union_S V2` requires `N_{S/V1} tensor N_{S/V2} = O_S`.

## Result

For the named triple `(l,q,q5)` above:

1. `H` and `Q` are smooth; `S` is a smooth quartic K3 surface and `H`
   meets `Q` transversely along `S`.
2. The total space `X` is singular along the curve `C = S cap {q5=0}`.
   `C` is a smooth nonempty complete-intersection (4,5) curve of degree 20
   and genus 51. Hence the family as written is not semistable.
3. `N_{S/H} tensor N_{S/Q} = O_S(5)`, which is ample hence nontrivial, so
   `H union Q` is not d-semistable. No smoothing with central fiber exactly
   `H union Q` is semistable; Kawamata–Namikawa smoothing does not apply.
4. Consequently the stated bare-triple `(H,Q,S)` Schmid/SL2 plus
   Clemens–Schmid program with explicit `T,N,W,F_lim` and Abel–Jacobi
   extension cannot be executed as written. The conjectured 1/202/1 weight
   table is neither proved nor disproved here; what is proved is that it
   cannot come from the bare `(H,Q,S)` triple without a new central fiber
   obtained by semistable reduction (blow-up along `C` and/or base change).

## Proof / evidence

**Q smooth.** Partials: `dq/dx0 = 4x0^3+x1^3+x2^3`,
`dq/dx1 = x1^2(4x1+3x0)`, `dq/dx2 = x2^2(4x2+3x0)`,
`dq/dx3 = 4x3^3`, `dq/dx4 = 4x4^3`.
If `x0=0`, vanishing forces `x1=x2=x3=x4=0`, invalid in `P^4`.
On `x0=1`: `x3=x4=0`, `x1,x2 in {0,-3/4}`; then
`dq/dx0 = 4+x1^3+x2^3 in {4,229/64,101/32}`, never zero. So `Q` smooth.
`H={x0=0}` is a `P^3`. On `S`, `sum_{i>=1} xi^4=0` has gradient
`(4x1^3,...,4x4^3)`, never zero on `S`; `S` smooth quartic, hence K3 by
adjunction. On `S`, `dq = (x1^3+x2^3)dx0 + sum 4xi^3 dxi` with some
`4xi^3` nonzero, so `ker dq` is transverse to `{dx0=0}`.

**Total space singular along C.** `dF = q dx0 + x0 dq + t dq5 + q5 dt`.
Over `t=0, x0=q=0` this is `q5 dt`. Hence points of the central fiber with
`q5=0` are singular in `X`, points with `q5!=0` smooth. So
`C = S cap {q5=0}` lies in `Sing(X)`.

**C smooth.** At `x0=0`, Jacobian rows `(4xi^3),(5xi^4)` are dependent iff
`a4xi^3+b5xi^4=0` for all `i` for some `(a,b)!=(0,0)`. If `b=0`, all `xi=0`,
impossible; else each `xi in {0,c}`, `c=-4a/5b`. Then
`sum xi^4 = k c^4` with `k` nonzero entries; vanishing forces `k=0` or
`c=0`, both invalid projectively. So `C` is a smooth complete intersection
wherever nonempty. Degree `4*5=20`; genus
`g = 1 + (20/2)(4+5-4-1) = 51` for a smooth (4,5) curve in `P^3`.

**C nonempty with explicit point.** Take `zeta=eta=exp(i pi/4)`,
`zeta^4=eta^4=-1`, `1+zeta^5 = 1-zeta != 0` with modulus-squared
`2-sqrt(2)`. Take `u^5 = -(1+zeta^5)/(1+eta^5) != 0`. Then
`(1:zeta:u:eta u)` (with `x0=0`) satisfies `sum fourth = 0` and
`sum fifth = 0` by construction, all entries nonzero. Numerically both
equations evaluate to `<4e-16` and a `2x2` Jacobian minor has modulus
`~15.307`, verified by `output/artifacts/verify_C_point.py` (re-ran PASS).

**d-semistability failure.** `S subset H` has normal bundle
`O_H(S)|_S = O_{P^3}(4)|_S`; `S subset Q` has normal
`O_Q(H)|_S = O_{P^4}(1)|_S`. Tensor product `O_S(5)` is ample, hence
nontrivial (`c1 != 0`). Friedman's condition fails.

## Limitations

- Does not prove or disprove the conjectured 1/202/1 limit weight table,
  the rank-one `N` isomorphism, or Abel–Jacobi nonsplitting.
- Does not compute any semistable reduction, monodromy matrix, or limit
  Hodge filtration.
- General-fiber smoothness for `0<|t|<epsilon` is not claimed here; only
  local evidence was sketched during investigation and uniform-epsilon
  patching remains open.
- The obstruction concerns the bare `(H,Q,S)` triple; the weight table may
  still hold after a corrected (blown-up / base-changed) central fiber.

## Reproducibility

Run `python3 output/artifacts/verify_C_point.py`: checks the explicit point
on `C`, both defining equations, nonzero coordinates, and Jacobian rank.
All other steps are closed-form Jacobian / normal-bundle computations above
and can be re-derived by hand or in any computer algebra system.

## References

- Doran–Harder–Thompson, Mirror symmetry, Tyurin degenerations and
  fibrations on Calabi–Yau manifolds, arXiv:1601.08110.
- Doran–Thompson, The mirror Clemens–Schmid sequence,
  Eur. J. Math. 10:63 (2024).
- Friedman, Global smoothings of varieties with normal crossings;
  Kawamata–Namikawa, Logarithmic deformations of normal crossing varieties
  and smoothing of degenerate Calabi–Yau varieties.
- Lee, Smoothing Tyurin degenerations and Hodge numbers of Calabi–Yau
  threefolds; Morrison, The Clemens–Schmid exact sequence and applications.
