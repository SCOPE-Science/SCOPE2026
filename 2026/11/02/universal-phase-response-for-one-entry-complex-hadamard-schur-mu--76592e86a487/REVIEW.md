# Review of the complex Hadamard phase-response theorem

## Correctness — PASS

The analytic proof reduces the complex spectral Schur-multiplier norm to a two-simplex nuclear-norm maximum, proves the needed matrix-fidelity joint concavity from an explicit minimization identity, and verifies global optimality of a symmetric stationary point without assuming symmetry of the underlying Hadamard equivalence class. The exceptional singular two-by-two sign-flip case is separated. The invariant two-dimensional compression gives a trace-norm radical and a strictly monotone scalar first-order equation, from which the closed formula follows. The phase monotonicity and exact quadratic deficit follow by differentiating the maximized scalar function. The numerical checker independently varies all row and column weights for 39 finite test cases; it does not substitute for the proof.

## Originality — PASS, with historical-priority risk

The previously established real one-sign-flip formula, including its Walsh and order-four specializations, is **prior** and is recovered only as the endpoint \(\zeta=-1\). Holbrook–Johnston–Schoch (arXiv:2206.02863v1) prove the global Hadamard maximum and study real sign patterns. Cowen et al. and Davidson–Donsig provide general trace duality/factorization and group-symmetry techniques; Christensen treats related general Schur norm theory. Inspected primary material and targeted semantic searches did not identify the exact full unit-phase formula, its strict phase ordering, or the local quadratic loss. These assertions are the claimed extension. A prior equivalent treatment framed as matrix fidelity or weighted singular-value optimization remains possible; absence from searches does not certify novelty.

## Value — PASS

Complex Hadamard symbols saturate the maximal spectral Schur norm, and changing one entry by a phase is the minimal multiplicative perturbation retaining all entry moduli. A closed class-independent phase-response law and a sharp second-order stability coefficient therefore quantify a natural robustness problem over every Fourier dimension, not an arbitrary numerical slice. The new parameter continuum is not determined by any fixed sign-flip example. The result is limited to one unimodular entry change and the spectral operator norm.

## Proof and computational boundaries

All stated identities are finite-dimensional exact algebra; the central concavity lemma is proved by a positive-matrix variational formula, not inferred from optimization logs. The checker uses unrestricted probability weights and numerical optimizers, so it cannot establish infinite-dimensional or all-order results by itself. The sign-flip endpoint is acknowledged as earlier work. Independent historical and mathematical validation have not been conducted.

Self-review: passed. Independent audit: not yet performed.
