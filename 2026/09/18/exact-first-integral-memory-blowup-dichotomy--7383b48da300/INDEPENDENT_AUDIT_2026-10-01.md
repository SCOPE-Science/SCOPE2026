# Independent audit — SCOPE-20260918-7383b48da300

Audit date (UTC): 2026-10-01

## Final claim

For the F2 exponential-memory equation, the exact first integral yields finite-time positive blow-up when \(v_0<1\), immediate singularity when \(v_0=1\), and finite-time negative blow-down when \(v_0>1\), with universal leading logarithmic amplitudes \(\sqrt{2/\alpha}\) and \(1/\sqrt{2\alpha}\) on the positive branch.

## Correctness

**PASS** — The linear-chain reduction, change \(w=(1-v)^{-1}\), and integrating-factor first integral were reconstructed directly. Its sign is monotone on each side of \(v=1\): for \(v_0<1\), the bracket multiplying the Gaussian exponential stays positive as \(u\) increases; for \(v_0>1\), it stays negative as \(u\) decreases. The corresponding time integrals converge by Gaussian decay, proving the two finite-time branches. Gaussian-tail inversion reproduces the displayed leading and first subleading terms; independent high-amplitude numerical checks approach the predicted ratios on both branches. The source primary full text was inspected: Theorem 2 is stated for every positive bounded history, but its proof explicitly restricts to \(0\le v<1\), so the supercritical history is genuinely omitted.

## Originality

**PASS** — The exact first integral uses standard integrating-factor and linear-chain techniques, which are excluded from the novelty claim. The source-specific correction is not present in the motivating paper: its theorem quantifies over all positive bounded histories while the proof enters the one-sided region before introducing the reciprocal variable. Exact-phrase and follow-up searches located no correction giving the three-way initial-memory classification or the sharpened universal amplitudes. The result is therefore original only as a correction and sharpening of this F2 problem, not as a new general integration method.

### Equivalent formulations

Aliases, parameter normalizations, and source-specific formulations were compared by implication rather than by title similarity. Exact-title, exact-claim, alias, and primary-literature searches found no equivalent stronger statement beyond the qualifications below.

### Broader coverage

The closest general results and source theorems were inspected directly. General machinery that is prior art is excluded from the novelty claim; none of the inspected broader statements implies the final claim at the stated strength.

### Exact database or table

Finite computations and tables were treated as corroborative evidence only. They were not used to infer an infinite theorem or to establish novelty.

### Claim versus prior implication

The exact first integral uses standard integrating-factor and linear-chain techniques, which are excluded from the novelty claim. The source-specific correction is not present in the motivating paper: its theorem quantifies over all positive bounded histories while the proof enters the one-sided region before introducing the reciprocal variable. Exact-phrase and follow-up searches located no correction giving the three-way initial-memory classification or the sharpened universal amplitudes. The result is therefore original only as a correction and sharpening of this F2 problem, not as a new general integration method.

## Value

**PASS** — The claim repairs a theorem whose stated hypothesis includes explicit regular histories with \(v_0>1\) that evolve in the opposite direction, and it identifies which leading singular constants are universal rather than history-dependent. Correcting the quantifier and classifying the omitted half-plane is mathematically substantive even though the integration method itself is elementary.

## Sources inspected

- Memory-induced blow-up solutions and their dynamical transitions in distributed delay differential equations — https://arxiv.org/abs/2609.15470 — NOT_COVERING and directly contradicted in scope: Theorem 2 is stated for every positive bounded history, whereas the proof explicitly focuses on the region below the singular memory level.
- Memory-induced blow-up solutions and their dynamical transitions in distributed delay differential equations — https://www.alphaxiv.org/abs/2609.15470 — BACKGROUND only; no correction or two-sided classification stated.

## Residual risks and limitations

- The real-valued supercritical continuation leaves the nonnegative biological state space before negative blow-down; under a nonnegativity convention the solution should instead be regarded as terminating when it exits that state space.
- The claim is specific to the F2 nonlinearity and a single exponential memory kernel.

## Disposition

**PASSED**
