# Fixed-contrast nested-square outer-vertex threshold by one CGO corner test: impossibility of the stated single-test separation

## Context

The admitted target considered the fixed dyadic nested-square conductivity cell and asked whether the outer vertex `v=(1/2,1/2)` can be distinguished by one CGO corner test at fixed `tau*=5` with thresholds `|I(5;v)| >= 0.25` at the true vertex and `|I(5;v')| <= 0.05` at every test vertex `v'` with `|v'-v| >= 0.5`, with remainder `|R| <= C*5^{-delta} <= 0.08` (equivalently a nonlinear monotonicity gap with margin 0.12). This audit resolves the literal target conjunction.

## Definitions

- `Omega = B_1` (unit disk), `D1 = (-1/2,1/2)^2`, `D2 = (-1/4,1/4)^2`.
- `sigma = 1 + 2*1_{D1\D2} + 4*1_{D2}` (values 1/3/5).
- `R(x1,x2) = (-x2,x1)`: 90-degree counter-clockwise rotation. `R` preserves `Omega`, `D1`, `D2`, hence `sigma o R = sigma`.
- `v = (1/2,1/2)`, `Rv = (-1/2,1/2) =: v2` (another outer corner of `D1`); `|v2-v| = 1.0 >= 0.5`.
- For corner `z` and unit direction `omega`, `u0(x;z,omega) = exp(rho.(x-z))` with `rho = tau(omega + i omega^perp)`, `tau = 5` (entire harmonic since `rho.rho = 0`), `f_{z,omega}` its trace on `dOmega`.
- DtN power-difference observable: `J(z,omega) = <(Lambda_sigma - Lambda_1) f_{z,omega}, f_{z,omega}>`.
- Canonical adapted rule: at a `D1` corner use the outward bisector; at `v`, `omega = (1,1)/sqrt2`; at `v2`, `omega2 = Romega = (-1,1)/sqrt2`. "Concentrating at z" means `omega` lies in the outward normal cone so `|grad u0|^2 = 2 tau^2 exp(2 tau omega.(x-z))` peaks at `z` and decays inside `D1`.

## Result

**Theorem (literal target conjunction is false).** With the canonical adapted rule, `J(v2,omega2) = J(v,omega)` exactly, and the common value satisfies `J >= 0.456 >= 0.25`. Hence the conjunction `|I(5;v)| >= 0.25` and `|I(5;v')| <= 0.05` for all `v'` with `|v'-v| >= 0.5` is impossible: the rotated true vertex `v2` is at distance 1.0 but carries the same large value `>= 0.456 > 0.05`. The failure margin is at least 0.40. The remainder in this exact formulation is identically zero, hence `<= 0.08`. So: largeness holds, remainder holds, distant-smallness fails.

## Proof / evidence

**Exact symmetry lemma.** `J(Rz,Romega) = J(z,omega)` for all `z,omega`. Since `sigma o R = sigma` and `Omega o R = Omega`: if `u` solves `div(sigma grad u)=0` with `u|_{dOmega} = f`, then `u o R` solves the same equation with data `f o R` (chain rule, `R` orthogonal). Hence `Lambda_sigma(f o R) = (Lambda_sigma f) o R` and likewise for `Lambda_1`; the `L^2(dOmega)` pairing is rotation-invariant, so quadratic forms agree on rotated data. Moreover with `rho' = tau(Romega + i Romega^perp) = R rho`, `u0(x;Rz,Romega) = exp(rho'.(x-Rz)) = exp(rho.(R^{-1}x-z)) = u0(R^{-1}x;z,omega)` using `(Ra).(Rb) = a.b`. Thus `f_{Rz,Romega} = f_{z,omega} o R^{-1}` and the DtN forms are equal. No numerical error. Applied to `z=v`: `J(v2,omega2) = J(v,omega)` exactly; any rotation-equivariant adapted single-test rule takes identical values at the two corners, so no thresholds `(0.25,0.05)` can separate them.

**Certified quantitative pinning.** Standard monotonicity (background 1, `sigma >= 1`) gives `J(z,omega) >= int_Omega ((sigma-1)/sigma)|grad u0|^2 >= int_{P'}(2/3)|grad u0|^2` where `P' = [1/4,1/2]^2 subset D1\D2` (up to null set) has contrast 3, i.e. `(sigma-1)/sigma = 2/3`. With `tau=5`, `omega=(1,1)/sqrt2` at `z=v`, writing `a = 5 sqrt2`: `E(P') := int_{P'} exp(2 tau omega.(x-v)) dx = ((1-exp(-a/4))/a)^2`, so `J(v,omega) >= (100/3) E(P')`. Hand-checkable enclosure: `sqrt2 in [1.4142,1.4143]`, so `a in [7.071,7.0715]`, `a/4 >= 1.76775`; `e >= 2.718` (0..6 factorial sum); for `x>0`, `e^x >= 1+x+x^2/2+x^3/6`, at `x=0.767` giving `>= 2.1363`; hence `e^{a/4} >= 5.806`, `e^{-a/4} <= 0.1723`, `q := (1-e^{-a/4})/a >= 0.11704`, `E(P') = q^2 >= 0.013698`, `J >= (100/3)*0.013698 >= 0.456`. Numerically `E(P') = 0.013754`, `J >= 0.4585` from `P'` alone, `>= 0.6692` using all of `D1`. Thus `J(v2,omega2) = J(v,omega) >= 0.456`, exceeding the claimed distant cap 0.05 by `>= 0.40` while satisfying largeness 0.25.

## Limitations

Disproves the literal universal-distant-smallness claim under the canonical adapted concentrating rule. Does not prove or rule out a corrected "four vertices versus background" statement (all `D1` corners large, genuine background probes small); no background-probe upper bound is claimed here. CGO-corrector representations inherit the conclusion only insofar as they represent the same full-DtN observable.

## Reproducibility

`output/artifacts/verify_target.py` (stdlib only) prints `VERIFY_OK`: logs `a` enclosure, Taylor floor, `(1-e^{-a/4})/a`, `E(P')`, `F_v >= 0.4568`, numeric `0.4585`, full-`D1` `0.6692`, `dist(v,Rv) = 1.0 >= 0.5`. All closed-form integrals, the symmetry change of variables, and the hand enclosure are self-contained above.

## References

- H. Liu and C.-H. Tsou, Stable determination of polygonal inclusions in Calderon's problem by a single partial boundary measurement, Inverse Problems 2020 (arXiv:1902.04462): qualitative nested-polygonal uniqueness / log-stability; records no fixed 1/3/5 single-tau threshold.
- J. Xiao, A new type of CGO solutions and its applications in corner scattering, Inverse Problems 2022: new CGOs / generic scattering; no nested-square vertex inequality.
- E. Blasten et al., On corner scattering for operators of divergence form: qualitative corner uniqueness; no fixed-cell threshold.
- E. Beretta and E. Francini, Lipschitz / global stability for polygonal conductivity inclusions: stability in Hausdorff distance; no 1/3/5 tau=5 vertex test.
