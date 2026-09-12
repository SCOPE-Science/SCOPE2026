# Disproof of the uniform stationary ASEP torus current variance bound

## Context

The asymmetric simple exclusion process (ASEP) with right jump rate `p > q`,
`p+q = 1`, is a paradigmatic interacting particle system in the Kardar-Parisi-Zhang
(KPZ) universality class. On the infinite line started from Bernoulli(rho),
current fluctuations are of order `t^{1/3}` (variance `t^{2/3}`) when measured
along the moving characteristic with velocity `V(rho) = (p-q)(1-2rho)`, and at
density `rho = 1/2`. Across a fixed bond with `V(rho) != 0`, fluctuations are
instead diffusive: variance is linear in `t`. The target asked whether a uniform
`t^{2/3}` variance bound could nevertheless hold for stationary ASEP on the
torus `Z_L` uniformly over densities in `[delta,1-delta]`, system sizes
`L >= L0`, and times `1 <= t <= c L^{3/2}`.

## Definitions

- Torus `Z_L = Z/LZ` with `N` particles, `rho = N/L in [delta,1-delta]` for fixed
  `delta in (0,1/2)`. Stationary measure `pi_{L,N}` is uniform over `N`-particle
  configurations. Each particle attempts right jumps at rate `p`, left at rate `q`;
  jumps onto occupied sites are suppressed.
- `J^L_x(t)` = net integrated current across bond `(x,x+1)` in `[0,t]`
  (right crossings minus left crossings). `H_L(t) = J_L(t) - E[J_L(t)]`.
  By rotation symmetry the law is independent of `x`.
- Infinite line `Z` with i.i.d. Bernoulli(rho) stationary initial data;
  `J^Z_z(t)` = net crossings of bond `(z,z+1)`.
- `Q(t)` = second-class particle position started from a single discrepancy at
  the origin under basic coupling to a stationary background.

## Result

Fix `p > q`, `p+q = 1`, and `delta in (0,1/2)`. There are **no** constants
`C, c, L0` depending only on `p,q,delta` such that stationary torus ASEP with
`N/L in [delta,1-delta]` satisfies `sup_x Var[H_L(t)] <= C t^{2/3}` for all
`L >= L0`, all `1 <= t <= c L^{3/2}`, and all bonds `x`.

Indeed, for every `C, c, L0` there is an explicit admissible sequence
`L_m = m`, `N_m = ceil(delta m)`, `t_m = floor(log(m+1))` at bond `(0,1)` with
`L_m -> infinity`, `N_m/L_m in [delta,1-delta]`, `1 <= t_m <= c L_m^{3/2}`,
`t_m -> infinity`, and

```
Var_{L_m,N_m}[J(t_m)] / t_m^{2/3} >= (d*/4) t_m^{1/3} -> +infinity,
```

where `d* = delta(1-delta)(p-q)(1-2delta) > 0`, in particular exceeding any
fixed `C` eventually.

## Proof / Evidence

Lemma 1 (infinite-line input, cited standard identities). For ASEP on `Z` from
Bernoulli(rho), `Var_rho(J^Z_z(t)) = rho(1-rho) E_rho|Q(t)-z|` (Ferrari-Fontes,
Ann. Probab. 22(2):820-832, 1994), and `Q(t)/t -> V(rho) = (p-q)(1-2rho)` a.s.
for `p > q` (Ferrari-Kipnis-Saada, Mountford, Balazs-Seppalainen). By Fatou,
`liminf Var/t >= rho(1-rho)|V(rho)| > 0` when `V(rho) != 0`. Fix
`rho* = delta < 1/2`; then `V* = (p-q)(1-2delta) > 0` and with
`d* = delta(1-delta)V*` there is `T*(p,q,delta)` with
`Var_{rho*}(J^Z_0(t)) >= (d*/2) t` for all `t >= T*`.

Torus-to-line transfer (Lemmas 2-4, proved self-contained). Couple torus
`(L_m,N_m)` with line at fixed density `rho* = delta` via the Harris graphical
construction: identical Poisson clocks on overlapping window
`I_m = [-R_m,R_m]` with `R_m = floor((log(L_m+1))^2)+1`, independent clocks
outside; optimal coupling of initial configurations inside `I_m`.
Initial-marginal coupling of hypergeometric (without replacement) vs binomial
(with replacement) on `k_m = 2R_m+1` sites has failure `<= 4k_m^2/L_m` by
sequential common-uniform coupling. Finite-speed failure (a causal chain from
`I_m^c` reaching `(0,1)` by `t_m`) is `<= 2(et_m/R_m)^{R_m}` by a Gamma/Poisson
Chernoff bound unioned over two sides. Hence
`eps_m = P(G_m^c) <= 4k_m^2/L_m + 2(et_m/R_m)^{R_m} -> 0`, and on `G_m`,
`J^{L_m}(t_m) = J^Z(t_m)` pathwise. With shared bond clocks, `|J| <= N ~ Poisson(t_m)`
gives `|D_m| <= 2N` for `D_m = J^L - J^Z`, `E[D_m^4] <= 240 t_m^4`, so
`E[D_m^2] <= 16 t_m^2 eps_m^{1/2} -> 0` and
`|Var_{L_m,N_m} - Var_{rho*}| -> 0`.

Violation. For large `m`, `t_m >= T*`, so torus variance `>= (d*/4) t_m`.
Dividing by `t_m^{2/3}` gives `>= (d*/4) t_m^{1/3} -> infinity`. The sequence
satisfies `N_m/L_m in [delta,1-delta]`, `1 <= t_m <= c L_m^{3/2}` for every fixed
`c > 0`, and `L_m -> infinity`; rotation invariance gives
`sup_x Var = Var` at `(0,1)`. Hence every candidate triple `(C,c,L0)` is violated.

## Limitations

Lemmas 2-4 are proved self-contained; Lemma 1 cites the published Ferrari-Fontes
identity and second-class law of large numbers. The disproof establishes falsity
of the uniform bound but does not determine the sharp torus variance growth rate
or the crossover scale near the recurrence time.

## Reproducibility

Take any `p > q`, `delta in (0,1/2)`. Set `L_m = m`, `N_m = ceil(delta m)`,
`t_m = floor(log(m+1))`, `R_m = floor((log(m+1))^2)+1`. Verify
`2R_m+2 < L_m`, `t_m >= 1`, `R_m/t_m -> infinity`, `k_m^2/L_m -> 0`,
`t_m/(cL_m^{3/2}) -> 0`. Recompute the coupling bounds above; the Poisson
fourth moment `E[N^4] = t^4+6t^3+7t^2+t` and Chernoff
`P(Poisson(t) >= R) <= (et/R)^R` suffice. Check density
`N_m/L_m in [delta,delta+1/L_m] subset [delta,1-delta]` for large `m`.

## References

- Ferrari, Fontes, Current fluctuations for the asymmetric simple exclusion
  process, Ann. Probab. 22(2):820-832, 1994.
- Balazs, Seppalainen, Order of current variance and diffusivity in the ASEP,
  Ann. Probab.; Seppalainen review arXiv:1004.2095.
- Aggarwal, Current fluctuations of the stationary ASEP and six-vertex model,
  Duke Math. J. 167(2), 2018 (characteristic `T^{1/3}`).
- Tracy, Widom, Total Current Fluctuations in ASEP.
- Gupta, Majumdar, Godreche, Barma, Tagged particle correlations in ASEP:
  Finite-size effects, Phys. Rev. E 76:021112, 2007.
