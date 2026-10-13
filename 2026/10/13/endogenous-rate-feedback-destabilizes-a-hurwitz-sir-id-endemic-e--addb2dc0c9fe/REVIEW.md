# Review of endogenous-rate endemic instability

## Correctness

**PASS.** The full five-equation field is exactly the simulation feedback system stated in the 2026 SIR-ID article, locally inside strict clipping bounds. Direct rational substitution verifies every equilibrium equation. The upper-left three-dimensional characteristic polynomial satisfies the cubic Hurwitz test, while the full quintic has the exact Routh first-column sign pattern \((+,+,+,-,+,+)\) and no zero pivots, proving exactly two right-half-plane eigenvalues. `verify.py` reconstructs the derivatives and polynomial arithmetic. The claim is linear instability, not a demonstrated Hopf transition or limit cycle.

## Originality

**PASS within the specifically compared evidence.** The motivating work analyzes a three-population Jacobian with coefficients fixed in its published Theorem 7 while specifying a coupled five-equation simulation model. The present five-variable rational counterexample and sign certificate are absent from the relevant original sections inspected. Closely related studies of age-structured infectivity feedback and hysteretic SIRS responses use different dynamical systems and do not imply this exact witness. Searches covering the source identifiers, aliases, five-state equilibrium stability, rate laws, and characteristic-polynomial reductions revealed no matching published finding. Unindexed or inaccessible mathematical work remains a possibility; unsuccessful searches alone cannot establish absolute novelty.

## Value

**PASS.** The difference is not a generic request to include two more variables: it reverses a qualitative endemic-stability conclusion precisely where the source's distinctive endogenous-rate mechanism feeds back into incidence and removal. A fully interior exact witness demonstrates that a stable frozen-rate SIR subsystem may conceal a two-dimensional oscillatory unstable mode, directly affecting interpretation of the model's asymptotic predictions. This is a model-specific structural boundary, not an asserted epidemiological forecast.

## Closest literature and limitations

Breidenich and colleagues (2026), https://doi.org/10.3390/axioms15080603, Remark 1, Model 1, Theorem 7, and simulations; Kuniya and Inaba (2023), https://doi.org/10.3934/mbe.2023581; Guan, Kopfová, and Rachinskii (2024), https://doi.org/10.1137/22M154274X. Neither another biological mechanism nor generic Routh–Hurwitz theory supplies this exact five-state witness automatically. No claim of global dynamics, periodic solutions, an actual Hopf point, or empirical relevance is made. The same-model calculations do not constitute an independent audit.

Self-review: passed. Independent audit: not yet performed.
