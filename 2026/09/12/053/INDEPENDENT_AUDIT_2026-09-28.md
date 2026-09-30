# Independent Audit — 2026-09-29

**Record:** `2026/09/12/053`  
**Title:** Dense E-I QIF fixed-budget heterogeneity-ratio gamma restoration at rho_c=2.545, 34.6 Hz, E-leads-I  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `2f8ef22c8ae8093c5a007c97a6c562597371ed1a`  
**Disposition:** **PASSED**

## Independent checks

- Reimplemented the four fixed-point equations and six-dimensional Jacobian directly from the stated model.
- Bisectioned the leading eigenvalue crossing independently and recomputed the critical frequency and transversality.
- Compared the archived cycle and spiking JSON summaries to the filed numerical claims.
- Compared scope with the MPR primary source and adjacent QIF E-I literature, keeping originality limited to the concrete witness.

## Three-axis assessment

- **Correctness — PASS**: A fresh implementation of the stated six-dimensional MPR-plus-synapse Jacobian reproduces the critical ratio rho_c=2.5453391692, eigenpair ±0.217293075 i/ms (34.5833 Hz), critical fixed point, and transversality d Re(lambda)/d rho=0.0317492/ms. The archived rho=4 mass-cycle and N=7500 spiking summaries agree with the filed means/frequencies. The record correctly labels fixed-point uniqueness and cycle stability as numerical rather than global analytic facts.
- **Originality — LIMITED_TO_SPECIFIC_WITNESS**: The MPR reduction and E-I gamma bifurcation mechanisms are established. Focused literature comparison did not identify a prior result using this exact fixed-sum Lorentzian heterogeneity budget S*=2 with rho=Delta_E/Delta_I as the control axis and this parameter set. That supports treating the threshold as a specific new numerical witness, not as a broad novelty claim or proof of priority.
- **Scientific Value — PASS**: The record gives a reproducible constrained-heterogeneity control experiment: baseline stable at rho=1, a simple transversal Hopf on the E-concentrated side, no corresponding crossing on the sampled I-concentrated side, phase information, and a finite-spiking cross-check. The result is useful as a benchmark even though it is not universal.

## Findings

- Current tree equals assigned tree SHA.
- Independent bisection reproduces rho_c=2.5453391692 and f_c=34.5833 Hz.
- Finite-difference transversality at step sizes 1e-3 and 1e-4 reproduces 0.0317492/ms.
- Archived rho=4 mass cycle reports 36.67 Hz and E-leading-I phase -1.2902 rad; the N=7500 spiking file reports a 38 Hz E-rate peak with means close to the mass cycle.

## Sources compared

- Montbrió–Pazó–Roxin, Macroscopic Description for Networks of Spiking Neurons: https://journals.aps.org/prx/abstract/10.1103/PhysRevX.5.021028 — Primary source for the exact QIF firing-rate/mean-voltage reduction with Lorentzian heterogeneity.
- Repository record 053 RESULT.md: https://github.com/SCOPE-Science/SCOPE2026/blob/main/2026/09/12/053/RESULT.md — Defines the fixed-sum heterogeneity-ratio experiment, parameter set, and numerical claims audited here.

## Limitations

- The uniqueness claim remains based on spread-start Newton continuation rather than a global theorem.
- Stable limit-cycle evidence is from time integration rather than Floquet multipliers.
- The finite spiking confirmation is one N=7500 realization for the reported points; no universal robustness claim is made.
- Absence of a covering prior in the focused search is not proof of absolute priority.

This audit is independent of the repository’s pre-existing audit material. GitHub was read only as evidence; no repository changes were made by this audit run.
