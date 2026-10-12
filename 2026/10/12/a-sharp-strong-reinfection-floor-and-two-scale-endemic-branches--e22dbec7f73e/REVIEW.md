# Review of the sharp strong-reinfection SEIRV asymptotic

## Correctness — PASS

The finding is about positive equilibria with fixed rates \(\Lambda,\alpha,\mu,\gamma,\delta,\theta>0\) and \(0<\sigma<1\). The five stationarity equations reproduce the scalar reduction in the primary paper's Lemma B.1 exactly. The primary-infection term strictly decreases with positive infection and increases with primary transmission. The leading coefficient of the cleared cubic is \(-H B\beta^2\sigma\), and its constant coefficient is negative throughout the strictly subcritical regime, ensuring at most two positive roots. A smooth blow-up \(I=B^{-1/2}y\), \(\beta=\beta_\infty+B^{-1/2}z\) produces a nondegenerate fold with explicitly verified derivatives. Localization inequalities confine *every* nonnegative scalar value in the near-critical strip to this fold scale and preclude a remote competing positive branch. The implicit-function theorem supplies the stated error orders; a separate regular perturbation yields the \(B^{-1}\) and order-one infected branches. The printed verifier checks nontrivial exact rational identities and a two-positive-root witness; those examples are not substitutes for the analytic proof.

## Originality — PASS (specific statement)

The motivating Khan–Wang–Liu–Xiong paper already proves existence of a subcritical saddle-node, the scalar cubic, and a finite-reinfection threshold computed numerically. It is not credited here with (nor claimed here anew) that previously proved structure. The new exact claims concern the positive limiting floor for \(\mathcal R_0^C(B)\), the coefficient of its \(B^{-1/2}\) approach, and the two different infected-equilibrium scales for fixed subcritical primary transmission. Published SEIRE and SVEIRE studies already contain reinfection and backward bifurcation but employ different flow systems, so those mechanisms alone do not imply the displayed SEIRV singular asymptotics. A related analysis of vaccination dependence of the *local* reinfection threshold concerns a distinct parameter sensitivity and does not determine the global-fold large-\(B\) limit. Search coverage and unavailable full-text comparisons remain risks, not proof of uniqueness.

## Mathematical value — PASS

The precise gap is how far reducing the primary-transmission reproduction number can lower the critical equilibrium threshold when reinfection is very strong. The leading constant \(1-\delta/K\) is a sharp floor, not just a numerical trend; the \(B^{-1/2}\) fold scaling identifies a singular contact between two mechanistically different endemic regimes, and the \(B^{-1}\) lower branch quantifies its separation from the persistent order-one upper branch. These statements refine, rather than repackage, the plotted finite-parameter threshold curve and give an explicit high-reinfection benchmark for analyses of vaccination and waning-immunity extensions.

## Closest literature and risks

The primary model and its original lower-threshold theorem: Khan–Wang–Liu–Xiong (2026), DOI `10.1080/17513758.2026.2713881`, §§2,5,7,8 and Appendix B.1 as available through indexed full-text sections. Related earlier mechanisms: Wang et al., DOI `10.1142/S1793524522501327`; Sulayman–Abdullah–Mohd, DOI `10.3390/math9040327`. The 2022 SEIRE work was inspected through its arXiv full-text HTML rendering (with some missing formula glyphs); some publisher/PDF contents were not accessible, and unindexed or newer results may cover special aspects of the calculation. This does not establish global dynamical stability or exact parameter independence of epidemic forecasts.

Self-review: passed. Independent audit: not yet performed.
