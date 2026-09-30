# Independent Audit — 2026-09-29

**Record:** `2026/09/12/010`  
**Title:** Refutation of the uniform 15% cyclotomic smoothing-width improvement at dimension 1024  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `8c6de884ce6f2e55956064bf439a82d266636e05`  
**Disposition:** **PASSED**

## Independent checks

- Recomputed the exact first-shell expression and its base-2 logarithm independently.
- Checked the power-of-two cyclotomic unit-ideal embedding normalization: the coefficient basis is orthogonal up to one common scale in the canonical embedding.
- Compared the claim with standard smoothing-parameter lower-bound literature.

## Three-axis assessment

- **Correctness — PASS**: The counterexample is mathematically sound. For the unit ideal in the power-of-two cyclotomic coefficient embedding the lattice is Z^1024, and in the canonical embedding it is an orthogonal common rescaling, so the relevant smoothing ratio is unchanged. With L=ln(2048(1+2^128)) and s'=0.85 sqrt(L/pi), the 2048 shortest dual vectors alone contribute 2048 exp(-(289/400)L), whose log2 is about -89.43 and hence is far above 2^-128. The filed exact interval argument is conservative and valid.
- **Originality — LIMITED**: The decisive mechanism is the standard first-shell lower bound for the smoothing parameter applied to the unit ideal/Z^n. This is a useful target-specific counterexample, but not a new general smoothing-parameter theorem; standard literature already makes shortest-vector lower bounds immediate.
- **Scientific value — PASS**: The record cleanly prevents a false uniform constant-factor improvement from being propagated into structured-lattice analyses. Its value is primarily as a sharp falsification/boundary example rather than as a broad new cryptographic result.

## Findings

- The current record tree exactly matches the assigned tree SHA.
- Independent recomputation gives log2(first-shell mass) about -89.43 at 0.85 s_B, a violation of the 2^-128 target by more than 38 bits.
- The standard shortest-vector lower bound already explains why a fixed c<1 cannot uniformly beat the stated baseline on this member as epsilon becomes tiny.
- The repository's `output/artifacts/...` wording is a stale workspace-style path; the actual packaged script is `artifacts/verify_counterexample.py`. This packaging issue does not affect the scientific claim and is not treated as a substantive research repair.

## Sources compared

- Micciancio–Regev, Worst-Case to Average-Case Reductions Based on Gaussian Measures: https://doi.org/10.1137/S0097539703447898 — Introduces/uses the lattice smoothing parameter and Gaussian-mass framework underlying the baseline.
- Random Lattice Theory, Lemma 1.3.6 (shortest-vector lower bound): https://link.springer.com/chapter/10.1007/978-981-19-7644-5_1 — States the standard lower bound eta_epsilon(L) >= sqrt(ln(1/epsilon)/pi)/lambda_1(L*), reflecting the same first-shell obstruction.
- Zheng et al., Cyclic Lattices, Ideal Lattices and Bounds for the Smoothing Parameter: https://arxiv.org/abs/2112.13185 — Provides ideal/cyclic-lattice smoothing context; it does not supply the submitted 15% claim.

## Limitations

- The audit validates the negative uniform statement, not any positive improvement for restricted ideal classes.
- The audit does not infer security consequences for a concrete cryptosystem from the one-lattice counterexample.

This audit is independent of the repository's pre-existing audit material. GitHub was read only as evidence; no repository changes were made by this audit run.
