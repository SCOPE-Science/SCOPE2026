# Scientific review

## Correctness — PASS
The discrete two-impurity matching conditions yield exact \(r,t\) for arbitrary propagating momentum, hence the absorption and the band-centre parity alternatives. With fixed budget and odd separation, differentiating the explicit rational formula gives a quartic; the Möbius change \(z=x/(b-x)\) turns this quartic into a polynomial with exactly one coefficient sign change. Its opposite end signs prove a unique global interior maximizer for **every** positive budget. Exact leading asymptotics follow from the polynomial implicit equation. The included independent matching solver passed 500 random complex-amplitude tests, 180 optimization grids, and phase and singular-limit checks; symbolic algebra independently confirmed the derivative and polynomial conjugacy.

## Originality — PASS (scope-restricted)
The reviewed sources distinguish the precise new proposition from close antecedents. Burke–Wiersig–Haque's single absorbing defect does not imply a two-site allocation theorem; Miroshnichenko–Kivshar's conservative decorated networks and Guilarte–Muñoz-Castañeda's predominantly real continuum double-deltas likewise do not provide it. Merkel et al. **already demonstrate near-perfect one-sided absorption**, so generic near-perfect absorption is explicitly excluded from the originality claim. Longhi's edge-loss setting has a different number of leads and an initial-state-controlled transient question. The precise candidate claim combines parity-specific exact flux, strict global optimality for every fixed positive budget, and the high-budget limiting upstream allocation. Search coverage cannot establish historical uniqueness; undiscovered equivalent two-defect scattering optimizations are a residual risk. The proof concerns only the exact model in RESULT.md.

## Mathematical value — PASS
Fixed material or dissipation budgets are a natural design constraint in non-Hermitian scattering. The parity dichotomy is structural, and the exact optimizer answers a nonconvex global resource-allocation question without local-minimum ambiguity. The strong-loss contrast is consequential: under identical total strength, single-defect absorption vanishes but a two-site odd-separation design approaches unit absorption. This makes the precise allocation rule, not merely the correct scattering algebra, the valuable result. Its limitations are ideal coherent single-frequency incidence and no robustness theorem.

## Closest literature and priority risk
[1] Miroshnichenko–Kivshar, arXiv:cond-mat/0505023; [2] Merkel et al., arXiv:1509.01443; [3] Guilarte–Muñoz-Castañeda, arXiv:1010.3116; [4] Burke–Wiersig–Haque, arXiv:1910.07439; [5] Longhi, DOI:10.3390/photonics13060574. An unlocated equivalent allocation theorem in specialized non-Hermitian scattering studies remains a plausible priority risk. A published technical review may uncover an equivalent earlier treatment.

Self-review: passed. Independent audit: not yet performed.
