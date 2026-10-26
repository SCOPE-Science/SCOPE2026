# Mathematical review

## Correctness — PASS

The source coefficient formula [1, Eq. (25)] was independently reduced to a two-term scalar recurrence. Three exact algebraic identities compare the starter value with the real characteristic roots and identify the discriminant phase transition. Positivity below the frontier is proved by sign-induction or a two-real-roots formula, including the double-root and annihilation boundaries. Above the frontier either the roots are conjugate nonreal with a necessarily sign-changing trigonometric sequence, or the recurrence has negative sum of roots and eventually negative even iterates (or an immediately negative second iterate). The two branches meet continuously and uniquely maximize at \(\kappa=1/2\). Finite tests only support the identities and are not relied on to establish the universal quantifiers.

## Originality — PASS, subject to residual literature uncertainty

The 2026 source [1, Section 4.1] proves A-stability, stiff damping and error-constant optimality, not the necessary-and-sufficient all-iterate scalar nonnegativity frontier under this specified backward-Euler starter. Hundsdorfer–Ruuth–Spiteri [2] establishes more general monotonicity and boundedness criteria for different method classes and starter hypotheses; such general theorems do not immediately provide the explicit optimized-family phase diagram without new family-specific analysis. Hundsdorfer [3] treats partially implicit BDF2 blends for convective flows, with a different splitting/coefficients. Lóczi [4] concerns existing BDF/Adams boundedness coefficients, and the lawful open-access full text was inspected; its general SCB criteria and named older coefficient families do not directly give the new scalar phase diagram. An implicit derivation from those criteria remains a priority risk. The \(\kappa=0\) canonical BDF2 boundary is known and is explicitly excluded from the novel contribution in isolation. A previously published BDF2 calculation studies the *delay* of first sign loss for BDF2 but not the positive-\(\kappa\) frontier. No directly equivalent prior statement was found in the actual targeted comparisons; lack of a match is not a proof of unique priority.

## Mathematical value — PASS

The 2026 family is selected by conflicting approximation-error and stiff-damping objectives. This exact, global-in-iteration threshold adds a logically distinct and practically motivated criterion: positivity of a basic dissipative mode. The optimum is interior, unlike maximizing the stiffness damping or minimizing the error constant, and increases the classical BDF2 scalar positivity budget by a factor of three. The separate discriminant and coefficient-sign mechanisms explain the switch in formula at the same optimal parameter. It gives a testable criterion for positivity-sensitive scalar applications without claiming matrix, nonlinear, or full-PDE positivity.

## Closest prior coverage and limitations

[1] Jensen–Lóczi–Ketcheson (2026), arXiv:2610.22685, Eq. (25), Sections 4.1 and 5; [2] Hundsdorfer–Ruuth–Spiteri (2003), DOI:10.1137/S0036142902406326, with lawful CWI report; [3] Hundsdorfer's partial implicit blends; [4] Lóczi (2016), arXiv:1609.07858. The main residual risk is an implicit derivation in specialized linear-monotonicity theory; there is no claim of independent validation.

Self-review: passed. Independent audit: not yet performed.
