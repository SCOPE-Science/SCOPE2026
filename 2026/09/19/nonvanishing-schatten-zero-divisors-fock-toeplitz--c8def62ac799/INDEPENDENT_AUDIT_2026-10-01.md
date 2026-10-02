# Independent scientific audit — SCOPE-20260919-c8def62ac799

Audited at: 2026-10-01T14:19:47.879090Z

Disposition: **passed**

## Correctness — PASS

The Gaussian transfer formula identifies each block with a scalar multiple of a linear-composition adjoint. Its singular values show all-Schatten membership exactly when all coordinate contractions are strict. Quaternionic coefficient cancellation persists under the deformation. At zero active damping the symbols remain bounded and nondecaying while active composition remains contractive; zero passive damping in higher dimension tensors a nonzero active factor with the identity and is noncompact. The exponential-polynomial argument excludes finite rank.

## Originality — PASS

An earlier SCOPE result already proves that Qin's original decaying pair lies in every Schatten ideal, but it does not cover the bounded nondecaying active endpoint or the exact passive noncompact/all-Schatten transition. No inspected source dominates those two boundary statements.

### Equivalent formulations

The assigned endpoint is not an equivalent restatement of the prior decaying case.

### Broader coverage

No material read covers the nondecaying endpoint together with the passive damping boundary.

### Exact database or table

This is not a table lookup.

### Claim versus prior implication

The boundary statements require a new deformation analysis.

## Value — PASS

The bounded nondecaying all-Schatten endpoint and sharp passive damping transition expose a substantive separation between symbol decay and operator smoothing, a natural structural boundary in the zero-product construction.

## Sources inspected

- Zero-product problem for Toeplitz operators on the Fock space — https://arxiv.org/abs/2609.20555. COVERING_INGREDIENT: Provides bounded Schwartz zero-product symbols, hence a decaying interior point.
- Two-factor Fock Toeplitz zero divisors in every Schatten ideal — https://github.com/Resultary/2026/tree/main/2026/9/18/SCOPE-fock-toeplitz-zero-divisors-all-schatten--1095c1bf378e. COVERING_INGREDIENT: Proves all-Schatten membership for Qin's original decaying pair, not the nondecaying endpoint.
- Algebraic properties and the finite rank problem for Toeplitz operators on the Segal-Bargmann space — https://doi.org/10.1016/j.jfa.2011.07.006. INACCESSIBLE_PLAUSIBLE_SOURCE: Historical overlap with the endpoint could not be fully excluded.

## Residual risks

- Bauer-Le (2011) full text remains unverified.
- General weighted-composition recognition is prior and is not claimed as new.

## Limitations

- Dimension at least two only.
- The one-dimensional two-bounded-symbol problem remains open.
- Bauer-Le full-text overlap remains an explicit risk.
