# Finite-Volume Destabilization of the Kummer Semistable Pullback on a Goldstein–Prokushkin–Fu–Yau Threefold

## Context

The heterotic Hull–Strominger system on a non-Kahler Calabi–Yau threefold asks for a conformally balanced metric and a Hermitian–Yang–Mills (HYM) bundle connection satisfying Green–Schwarz anomaly cancellation. On Goldstein–Prokushkin (GP) torus bundles over K3 with Fu–Yau balanced metrics, a natural candidate bundle is the pullback of a semistable bundle from the base. The admitted target asks whether the pullback of a specific strictly semistable rank-2 extension on a Kummer K3 is slope-stable (hence HYM) or destabilized at fixed finite fiber volume.

## Definitions

Let `S = Km(E x E)` be the smooth projective Kummer K3 with Picard data `<h, e_1..e_16>`, `h^2 = 2`, `h.e_i = 0`, `e_i.e_j = -2 delta_ij`. Let `sigma` swap the two abelian factors, fixing `h`, fixing 4 exceptionals and swapping 6 pairs. Put `D = e_1 - e_2`, `L = O_S(D)`, `F_1 = e_3 - e_4`, `F_2 = e_5 - e_6`, `H = N h - sum e_i` ample for `N >> 0`. Let `E` be a non-split extension `0 -> L -> E -> L^{-1} -> 0`. Let `pi : X -> S` be the GP `T^2`-bundle with ASD classes `(F_1, F_2)`, `tau = ||Omega||_{omega_u} omega_u^2` the Fu–Yau balanced class at fiber volume `eps_0 = 1`, invariant under the lift `tilde sigma`. Slope: `mu_tau(F) = rk(F)^{-1} int_X c_1(F) ^ tau`.

## Result

Theorem: with the data above, `mu_tau(pi^*L) = 0 = mu_tau(pi^*E)`. Hence the reverse slope inequality `mu_tau(pi^*L) >= mu_tau(pi^*E)` holds with equality and the strict stability inequality `mu_tau(pi^*L) < mu_tau(pi^*E)` is false at finite fiber volume. `pi^*E` is strictly semistable and not polystable, so it admits no HYM metric in `[tau]` by the balanced Li–Yau converse, and the balanced D-term / stringy Futaki pairing on `s = diag(1,-1)` equals `2||gamma||^2 > 0`. In particular `pi^*E` cannot close Green–Schwarz with this Fu–Yau metric.

## Proof / Evidence

Base: `D^2 = -4`, `H.D = 0`, so `deg_H L = 0`. `L^2 = O(2D)` has `(2D)^2 = -16`, so on K3 `chi(L^2) = 2 - 8 = -6`; since `c_1(L^2)` has `H`-degree 0 and is nontrivial, `h^0 = h^2 = 0`, hence `h^1(L^2) = 6`: non-split `E` exists (a P^5). Whitney gives `c_1(E) = 0`, `c_2(E) = 4`, and `E` is strictly semistable of slope 0 with `gr(E) = L (+) L^{-1}`. GP data: `F_i` are integral primitive `(1,1)` and `H`-primitive, hence ASD; `sigma^*F_i = -F_i` gives anti-invariant harmonic representatives. Fu–Yau continuity in swap-invariant spaces yields an invariant balanced class at `eps_0 = 1` (Lemma 4). Slope: `mu_tau(pi^*E) = 0` topologically; with `I = int pi^*[D] ^ tau`, the lift satisfies `tilde sigma^* pi^*[D] = -pi^*[D]` and `tilde sigma^*tau = tau`, so `I = -I`, i.e. `I = 0` at every finite `eps > 0` with no adiabatic limit; the triple-pullback term vanishes by form degree. Non-split pullback: `R^1 pi_*O_X = O_S` and `H^0(S,L^2) = 0` make the Leray edge map injective, so `e_X = pi^*e_S != 0` (Lemma 5); thus `pi^*E` is strictly semistable, not polystable since `L not = L^{-1}`. No HYM follows from HYM => polystable. Lemma 6: the Kobayashi extension formula gives pairing `2||gamma||^2 > 0` since `gamma != 0` for every metric. Script `output/artifacts/slope_check.py` reproduces all arithmetic and eps-independence at `eps in {0.1, 0.5, 1, 10}`.

## Limitations

Claim is for the stated symmetric swap-invariant Kummer and balanced data at finite fiber volume; it does not address other Fu–Yau classes, other line bundles, or adiabatic limits. Lemmas 4-6 use standard Fu–Yau continuity, Leray, and balanced DUY/Kobayashi facts cited rather than re-proved.

## Reproducibility

Run `python3 output/artifacts/slope_check.py`; it asserts `D^2 = -4`, `H.D = 0`, `chi(L^2) = -6`, `h^1 = 6`, `c_2(E) = 4`, and `mu(pi^*L) = 0 = mu(pi^*E)` across fiber volumes.

## References

Fu–Yau superstring with flux I/II; Goldstein–Prokushkin non-Kahler Calabi–Yau/HYM; Li–Yau HYM on non-Kahler manifolds; Kobayashi Differential Geometry of Complex Vector Bundles Ch. V; Garcia-Fernandez T-dual Hull–Strominger solutions (crelle-2019-0013 / arxiv:1810.04740, nearest background, inspected and not covering); Phong–Picard–Zhang Anomaly flow and Fu–Yau equation.
