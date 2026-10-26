# Scientific review

## Correctness — PASS

The conservative-stage coefficients and Patankar denominators are reconstructed from the original equations. The stage and final solves reduce to an explicit rational scalar map, and algebraic simplification gives the complete exact error multiplier. Its denominator is strictly positive for every finite positive step and every positive normalized state. An explicit negative derivative in the squared error makes the boundary multipliers exhaustive, proving the sharp global contractivity, unique minimax step, non-crossing boundary, and exceptional cubic step. A standalone exact-rational checker tests the update identity and independent inequalities; its finite tests support, but are not substituted for, the analytic proof. Risks: only strictly positive starts and the specified conservative two-state scheme are covered.

## Originality — PASS (best-knowledge comparison)

The 2017 method paper already supplies the scheme, order and positivity; the 2022 stability paper already proves local stability and uses the symmetric exchange as a numerical test; and the 2023 negative-coefficient paper documents failure of global stability for other schemes. These results are not represented as new. The new statement is the *sharp global nonlinear error map and rate*, unique globally best step, universal sign-crossing threshold and exact cubic special step for conservative-stage MPRK22(1/2) with two-way symmetric exchange. The relevant full-text sections and targeted public mathematics-record searches did not identify a statement implying these four formulas. They cannot be deduced from the previously established local Jacobian criterion or from one-way decay. Risks: publication-priority uncertainty for specialized work not identified by the searched aliases, and possible overlap with uninspected non-obvious sources. Negative search results alone are not taken as proof of novelty.

## Value — PASS

Published stability analyses distinguish local from global MPRK behavior and explicitly discuss whether nonnegative Runge--Kutta coefficients should lead to global convergence. A constructive sharp global rate theorem for the canonical positive mass-conserving test problem therefore answers a motivated nonlinear numerical-stability question. The exact no-crossing frontier distinguishes positivity from monotone relaxation, the unique worst-case-optimal step is a practical benchmark, and the cubic step clarifies the tradeoff between worst-case and asymptotic rates. The theorem is deliberately limited to the symmetric two-way exchange; it does not resolve the broader conjecture.

Self-review: passed. Independent audit: not yet performed.
