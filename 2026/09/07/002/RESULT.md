# Explicit coupling-tail mixing concentration for lazy simple random walk on balanced spiders S(k,L)

## Context
Balanced spiders interpolate the star (L=1) and long-leg regimes and isolate how
central branching delays diffusion. No finite-graph mixing concentration for this
family was known; neighbors are infinite-spider excursion asymptotics, cycle-plus-
edge non-reversible speedups, and binary-tree cover GFF limits.

## Definitions
- `S(k,L)`, `k>=3`, `L>=1`: center `c` degree `k`, `k` legs each a path of `L`
  edges. `n=kL+1` vertices, `|E|=kL`. Vertex notation: `0`=center,
  `(i,j)` leg `i`, distance `j`.
- Lazy simple random walk: `P(u,u)=1/2`, `P(u,v)=(1/2)/deg(u)` for `v~u`.
  Irreducible, aperiodic, reversible with
  `pi(0)=1/(2L)`, `pi(leaf)=1/(2kL)`, `pi(internal)=1/(kL)`.
- `d(t)=max_x ||P_x(X_t in .)-pi||_TV`, `t_mix(eps)=min{t:d(t)<=eps}`.
- Coalescing coupling: pair marginally faithful, absorbed together after
  meeting; coupling time `tau_couple`. Black box (Levin-Peres-Wilmer Ch.5):
  `d(t) <= max_{x,y} P_{x,y}(tau_couple>t)`.
- Radial chain `J_t=dist(X_t,0)` in `{0..L}`: Markov with stay `1/2`
  everywhere; `0->1` w.p. `1/2`; interior `+-1` w.p. `1/4` each;
  `L->L-1` w.p. `1/2`. Leg conditional on `J`-path: `0->1` picks uniform
  independent leg; otherwise leg unchanged (forgotten at `0`).

## Result
For all integers `k>=3`, `L>=1`, the two-stage coalescing coupling below
satisfies for all starts `x,y`:

- (i) Mean: `E_{x,y}[tau_couple] <= 3L^2 <= 8kL^2 =: M`.
- (ii) Geometric tail with `T0=32kL^2=4M`:
  `P_{x,y}(tau_couple > m T0) <= 4^{-m} <= 2^{-m}` for all `m>=1`.
- (iii) Mixing: `d(mT0) <= 4^{-m}`; `t_mix(1/4) <= T0`;
  `t_mix(eps) <= T0 ceil(log2(1/eps))` for `eps in (0,1/2]`.
- (iv) Centered exponential tail:
  `P(|tau_couple-E tau_couple| > t) <= 2 exp(-t/(64 k L^2))` (i.e. `c=1/64`).

Sharper `T0'=12L^2=4*3L^2` already gives the `1/4` tail; `T0=32kL^2` is a
generous corollary. Constants are upper bounds, simulation-falsifiable.

## Proof / Evidence
Proof uses only gambler's ruin, a cycle lift, and Markov restart.

**Lemma 1 (leg hitting).** Let `H_0^J=min{t:J_t=0}`. Then
`E_a[H_0^J]=2a(2L-a) <= 2L^2` lazy steps. Full-walk leaf-to-center mean
`2L^2`, `sup_x E_x[H_c]=2L^2`.
*Proof.* Move prob `1/2` everywhere, so lazy time is `2x` jump-chain time
(hold coins independent of directions, Wald). Jump chain: interior `+-1`
`1/2`, `0` absorbing, `L->L-1` deterministically. Mean jumps `g_a=a(2L-a)`
checks `g_a=1+(g_{a-1}+g_{a+1})/2`, `g_L=1+g_{L-1}`, max `L^2` at `a=L`.

**Cycle lift.** `N=2L`, `(Z_t)` lazy walk on `C_N` (stay `1/2`, `+-1` `1/4`;
for `L=1,N=2` flip `1/2`). Fold `f(z)=min(z,N-z)` gives `J'=f(Z)` with
exactly the `J` transitions (at `0` both preimages go to `1`; at `L` both go
to `L-1`).

**Lemma 2 (coalesce distances, mean <=L^2).** Two `J`-chains from `a,b` couple
with `E[tau_J]<=L^2`. Lift to `Z^x_0=a,Z^y_0=b`; alternating selection (pick
`x/y` w.p. `1/2`, move selected `+-1` equally, other stays) gives correct
lazy-cycle marginals and hence faithful folds. Difference `D` (integer lift)
moves `+-1` w.p. `1/2` each step, no hold. `Z`-meet = `D equiv 0 mod N`;
absorbed simple walk mean `d0(N-d0)`, max `N^2/4=L^2`. `Z`-meet implies
fold-meet, so `tau_J<=tau_Z`.

**Lemma 3 (stick and hit center, mean <=2L^2).** From `J^x=J^y`, keep them
equal via common coin (both stay `1/2`, else both move with common `J`
increment: interior `+-1` together, `0->1` together, `L->L-1` together).
Each marginal correct; on `0->1` each full walk picks independent uniform
leg. Joint `J` is a single `J`-chain; hitting `0` mean `<=2L^2` by Lemma 1.
At joint `0` both at center, coalesced; keep together after. Early
off-center meeting (same leg+distance) only shortens time.

**Theorem.** (i) Strong Markov at `tau_J`: `E[tau]<=L^2+2L^2`.
(ii) Markov `P(tau>T0)<=M/4M=1/4`; restart
`P(tau>(m+1)T0)=E[1_{tau>mT0}P_{X_{mT0},Y_{mT0}}(tau>T0)]<=1/4P(tau>mT0)`,
induction gives `4^{-m}`. (iii) Coupling inequality gives `d(mT0)<=4^{-m}`;
`ceil(log_4)<=ceil(log_2)` gives looser `eps` bound. (iv) For `t=mT0+r`,
`P(tau>t)<=4^{-m}<=2exp(-t/(64kL^2))` since `T0/(64kL^2)=1/2` and
`4^{-m}<=2e^{-(m+1)/2}` (ratio `(e^{1/2}/2)(e^{1/2}/4)^m<=0.824`).
Upper deviation subset; lower is `0` if `t>=E`, else `<=1<=2exp(...)`
since `t/(64kL^2)<E/(64kL^2)<=3/(64k)<=1/64<ln2`.

*Conductance sanity.* One leg `A`: `pi(A)=(2L-1)/(2kL)<=1/2`,
`Q(A,A^c)=1/(4kL)`, `Phi=1/(2(2L-1))~1/(4L)`; Cheeger `gap>=Phi^2/2`,
relaxation `O(L^2)`, consistent with mixing upper `O(kL^2)`.

*Computational audit (support, not proof).* Fixed seed `20260907`,
grid `k in {3,4,5} x L in {5,10,20}`, 20k trials/cell hitting, 10k/cell
constructed coupling from distinct-leg leaves, 3k/cell independent-meet.
Leaf->center matches `2L^2` within ~1% (e.g. L=20: ~799 vs 800);
constructed mean ~2L^2 vs envelope `3L^2=1200` (1.5x slack, far below generic
`n^3~1e6`); zero `T0`/`2T0` exceedances vs bounds `0.5/0.25`
(medians ~600, q99 ~3200 << T0=38400 at k=3,L=20). No violation.

## Limitations
- Upper-bound concentration with generous constants only; no lower
  bounds or cutoff.
- Balanced-leg radial symmetry essential; unbalanced legs / general trees
  need different arguments. Proof covers all `k>=1` but stated `k>=3`.
- Monte Carlo evidence is seeded support; Stage-1 (differing-distance)
  starts covered by proof but grid tests equal-distance leaves.
- Lemma 3 Z-lift phrasing is heuristic; the stated J-increment rule is the
  operative coupling.

## Reproducibility
Seed `20260907`; `sim_spider.py` sha256
`0ae11070c214b88b7edb3a3e3c2723a789200abec6d5f9fc0883cfa067bf2de0`;
run grid above; pass criteria: hitting ratio within 5%, coupling mean
`<=3L^2`, empirical `P(tau>T0)<=0.5`, `P(tau>2T0)<=0.25`. Any violation
refutes the constant.

## References
- Levin-Peres-Wilmer, Markov Chains and Mixing Times (coupling inequality,
  gambler's ruin `d(N-d)`, Markov restart).
- Csaki-Csorgo-Foldes-Revesz arXiv:1501.00466 (infinite-spider heights,
  distinct asymptotic regime).
- Feng-Gerencser arXiv:2411.07125 (cycle+edges non-reversible speedup,
  distinct family/method).
- Dembo-Rosen-Zeitouni arXiv:1906.07276 (binary-tree cover GFF limit,
  distinct tree/observable/method).
