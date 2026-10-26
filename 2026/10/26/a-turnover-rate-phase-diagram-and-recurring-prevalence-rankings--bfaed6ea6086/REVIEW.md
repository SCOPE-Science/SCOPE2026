# Scientific review

## Correctness — PASS

The single-community source system is exactly \(\dot y=-y+\tau y(1-y)z\), \(\dot z=-\zeta zy+\xi(1-z)\), and the choice \(\xi=\kappa\), \(\zeta=\omega\kappa\) preserves the positive equilibrium. The two Jacobian diagonal entries are \(-A\) and \(-\kappa B\); their off-diagonal product is \(-\kappa C\), and \(AB+C=\tau-1\). Consequently the discriminant has precisely the stated two roots, with nontrivial Jordan blocks at equality. The frequency-to-damping optimum reduces to a rational derivative, while the slow spectral rate has strictly positive derivative before \(\kappa_+\) and strictly negative derivative after it; the derivative inequality follows from the strictly positive identity \(X^2-B^2D=4(\tau-1)C\).

The nonlinear comparison is not a numerical extrapolation. At the central turnover speed the linearized pair is \(-A\pm i\sqrt{\kappa_0C}\); at every strictly faster speed all real parts are strictly below \(-A\). A quadratic-remainder variation-of-constants argument gives a nonzero leading cosine term of size \(\varepsilon e^{-At}\) for the central policy, while the faster policy is \(o(e^{-At})\). Opposite positive and negative subsequential limits force infinitely many genuine nonlinear sign changes. The argument explicitly allows defective repeated eigenvalues for the faster policy.

All physical boundary and quantifier conditions are stated. The standalone checker ran 245 exact-rational parameter cases and independently checked the example spectra and several finite-time sign reversals. Finite integrations are identified as corroboration only. The source model's global attractivity and absence of limit cycles are not reasserted as new results.

## Originality — PASS, residual risk recorded

The directly governing earlier paper, Achterberg–Sensi (arXiv:2209.01224, 2022), explicitly supplies this model, its equilibrium, Jacobian, stability and an example of spiraling. Those are considered prior knowledge. Inspection of its original full text, Example 2, later slow-fast section and conclusions did not identify a sharp fixed-ratio node–focus–node window, unique globally rate-optimal turnover, maximum frequency-to-damping ratio, or a theorem of infinitely many opposite-sign prevalence comparisons for shared initial conditions. The later multigroup paper (Achterberg–Sensi–Sottile, arXiv:2407.17639, 2024) studies a higher-dimensional system with possible genuine periodicity and different adaptation mechanisms, not the exact comparison theorem.

The earlier stochastic-network moment-closure study (Achterberg–Van Mieghem, *Physical Review E* 106 (2022), 014308) is close enough to name as a residual risk, but only its abstract and metadata were available; **no negative whole-document coverage conclusion** is drawn from it. Search comparisons included published research records for adaptive-SIS relaxation, focus/node transitions, fixed-ratio contact turnover and recurrent prevalence ranking. No directly covering statement was identified, which is evidence for best-knowledge originality but not proof of global uniqueness.

## Mathematical value — PASS

Changing both link breakage and creation rates together preserves endemic prevalence but not the temporal course of infection. The finding gives **two different exact optimal turnover speeds** (fastest local asymptotic damping versus strongest relative transient oscillations), with a complete spectral phase diagram. The nonlinear sign-reversal theorem exposes an operationally relevant limitation of ordering two policies by prevalence at a single moment: the ranking can change arbitrarily late despite identical starting condition and equilibrium. This is a sharp, infinite-parameter comparative-dynamics statement, not merely a restatement of the printed Jacobian or a finite numerical slice.

## Closest literature and limitations

Primary sources: [Achterberg–Sensi, arXiv:2209.01224](https://arxiv.org/abs/2209.01224); [Achterberg–Sensi–Sottile, arXiv:2407.17639](https://arxiv.org/abs/2407.17639); [Achterberg–Van Mieghem, DOI:10.1103/PhysRevE.106.014308](https://doi.org/10.1103/PhysRevE.106.014308). The last source was not accessible in full. The proved repeated reversals have amplitudes tending to zero; they are not epidemic limit cycles. The speed optimum is an asymptotic linearized exponent, not a universal finite-time control optimum. General stochastic and heterogeneous populations are not addressed.

Self-review: passed. Independent audit: not yet performed.
