# Uniform entropic K-convexity with vanishing error on compact RCD(K,infty) spaces

## Context

Let (X,d,m) be a compact RCD(K,infty) metric measure space with m a probability measure. Let mu0,mu1 in P_2(X) have finite relative entropy H(.|m), bounded densities with compact support, and finite Fisher information. Let mu^eps_t, t in [0,1], eps>0, be the entropic interpolation (Schrodinger bridge) joining mu0 to mu1 with reference reversible Brownian motion on (X,d,m) (generator L=(1/2)Delta, symmetric with respect to m). Write H_t = H(mu^eps_t|m), W = W_2(mu0,mu1), and h(t) = (1-t)H(mu0) + tH(mu1) - (K/2)t(1-t)W^2.

## Definitions

Relative entropy H(mu|m) = integral rho log rho dm if mu = rho m, else +infty. Entropic interpolation mu^eps_t is the marginal flow of the minimizer of eps H(P|R^eps) over path measures P with endpoints mu0,mu1, where R^eps is reversible Brownian motion with generator (eps/2)Delta. Potentials: phi_t = eps log P_t f, psi_t = eps log P_{1-t} g. Current velocity v_t = (1/2)grad(phi_t - psi_t), osmotic velocity w_t = (1/2)grad(phi_t + psi_t); current action A_t = integral |v_t|^2 d mu_t, osmotic action F_t = integral |w_t|^2 d mu_t = (eps^2/4) I(mu_t) with Fisher information I. Conserved energy E = A_t - F_t (constant in t). Dynamical Schrodinger value V_eps = E + 2 integral_0^1 F_t dt.

## Result (TARGET resolution, affirmative)

Theorem. Under the hypotheses above, there exists C = C(K, diam X, H(mu0), H(mu1), I(mu0), I(mu1)), independent of eps and t, such that for all t in [0,1], H(mu^eps_t|m) <= (1-t)H(mu0|m) + tH(mu1|m) - (K/2)t(1-t)W_2(mu0,mu1)^2 + C eps. Hence C eps -> 0 as eps -> 0, and narrow convergence mu^eps_t -> mu_t (a W_2-geodesic, by Schrodinger-to-OT Gamma-convergence) recovers exact K-displacement convexity of H.

The constant depends on the Schrodinger-cost gap (V_eps - W^2)/eps through a number C0, which is itself controlled by the endpoint entropies and Fisher bounds; this is within the admitted C(K, diam X, entropies, Fisher bounds) dependence. The disprove alternative (no uniform C, or a limit violating K-convexity) is rejected by this proof.

## Proof and evidence

The proof assembles cited standard Schrodinger-bridge theorems (not re-proved); the original step is the sign-correct Green-kernel estimate using only integrated Fisher control.

Step 1, second-derivative inequality. Along the interpolation the Conforti-Tamanini formula (also Gentil-Leonard-Ripani on RCD) gives H''(t) = (1/2) integral [Gamma_2(phi_t) + Gamma_2(psi_t)] d mu_t. The RCD(K,infty) weak Bochner inequality Gamma_2 >= K Gamma yields H''(t) >= K(A_t + F_t) =: K S_t with S_t = A_t + F_t >= 0. With e(t) = H_t - h(t), e(0) = e(1) = 0 (exact endpoints) and e''(t) = H''(t) + K W^2 >= K(S_t - W^2).

Step 2, conserved energy and competitor. HJB duality gives E = A_t - F_t constant in t (Leonard; Conforti). The Benamou-Brenier formulation of the dynamical Schrodinger problem gives the value identity E + 2 integral_0^1 F_t dt = V_eps. Since (mu_t,v_t) is admissible for the W_2^2 problem, W^2 <= integral_0^1 A_t dt = E + integral_0^1 F_t dt. A mollified-W_2-geodesic competitor (admissible under the bounded-density and Fisher hypotheses; classical Schrodinger-cost control V_eps - W^2 <= C0 eps with C0 depending on diameter, entropies and Fisher bounds) yields V_eps <= W^2 + C0 eps. Combining gives integral_0^1 F_t dt <= C0 eps and |E - W^2| <= C0 eps. No pointwise bound on F_t is needed.

Step 3, Green-kernel integration for both signs of K. With Green kernel G(s,t) <= 0, integral_0^1 G(s,t) ds = -t(1-t)/2, max_s |G(s,t)| <= 1/4: e(t) = integral_0^1 G(s,t) e''(s) ds. Since G <= 0, e'' >= K(S - W^2) flips to G e'' <= G K (S - W^2) pointwise. Writing S_s - W^2 = (E - W^2) + 2 F_s: e(t) <= K(E - W^2)(-t(1-t)/2) + 2K integral G(s,t) F_s ds. For K >= 0: first term <= (K/2)t(1-t)|E - W^2|, second <= 2K max|G| integral F; total <= C0 eps (K t(1-t)/2 + K/4). For K < 0 (K = -|K|): identical expression; first term <= (|K|/2)t(1-t)|E - W^2|; second term = 2|K| integral |G| F <= 2|K| (1/4) C0 eps (positive error, bounded). In both cases sup_t e(t) <= C eps with C depending on |K|,C0. For K = 0: H'' >= 0 exactly (C = 0). Sending eps -> 0 with narrow convergence recovers exact K-displacement convexity.

Computed verification (verification-critical). Exactly solvable 1D Gaussian Schrodinger bridge (closed form, no discretization error; output/artifacts/gaussian_check.py, results in output/artifacts/gaussian_bridge.json): with c solving c/(s0^2 s1^2 - c^2) = 1/eps and v_t = (1-t)^2 s0^2 + t^2 s1^2 + 2t(1-t)c + eps t(1-t), gap(t) = -{ (1/2)log v_t - [(1-t)(1/2)log s0^2 + t(1/2)log s1^2] } (OT sign). In all three cases (symmetric narrow s0 = s1 = 0.1; asymmetric 0.1,0.3; wide 0.5,0.5) max_t gap(t) = -0.0 to machine precision at every tested eps: exact K = 0 convexity with C = 0, stronger than the C eps allowance. The eps-mechanism is visible in the excess over the limit profile: max|excess| vanishes superlinearly (ratios to eps: 6.13 to 0.62 symmetric, 1.41 to 0.07 asymmetric), consistent with O(eps) with a Fisher-scaled constant (1/s^2 = 100 for the narrow case). Re-ran during audit and reproduced. Torus Sinkhorn grid scripts are exploratory only (resolution-limited) and are not used for the rate claim; they are not copied to the public package.

## Limitations

(a) The second-derivative formula, energy conservation, Schrodinger-to-OT Gamma-convergence on RCD, and the mollified-geodesic competitor estimate are cited as standard black-box theorems, not re-proved; the original contribution is their assembly with the sign-correct Green-kernel estimate using only integrated Fisher control. (b) Bounded densities, compact support, and finite Fisher information are used for the competitor; the Green-kernel step itself needs only the integrated bound. (c) The Gaussian check covers the K = 0 Euclidean case in closed form; general K != 0 RCD illustration is analytic (Steps 1 to 3), not numerical.

## Reproducibility

Run python3 output/artifacts/gaussian_check.py (numpy required); it prints per-eps max OT gap and excess ratios and writes output/artifacts/gaussian_bridge.json. The audit re-executed this script and reproduced the reported numbers (max OT gap -0.0; symmetric excess 0.3066, 0.0941, 0.0287, 0.00764, 0.001245; asymmetric 0.0703, 0.0133, 0.00344, 0.000866, 0.000139).

## References (results used, not claimed)

Erbar-Kuwada-Sturm (entropic curvature-dimension); Leonard (Schrodinger problem, energy conservation, entropic convexity); Conforti (second-order equation for Schrodinger bridges); Conforti-Tamanini; Gentil-Leonard-Ripani (HWI via entropic interpolation; RCD extension); Ripani (convexity and regularity for entropic interpolations); Lott-Sturm-Villani and Ambrosio-Gigli-Savare (K-convexity iff RCD); Benamou-Brenier (dynamic formulation); Mikami and Leonard (Schrodinger-to-OT Gamma-limit).
