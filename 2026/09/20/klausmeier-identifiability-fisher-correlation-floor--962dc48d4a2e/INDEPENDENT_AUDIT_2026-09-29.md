# Independent audit — Exact identifiability dichotomy and Fisher-correlation floor in the non-spatial Klausmeier model

**Audit date:** 2026-09-29 (UTC)  
**Source path:** `2026/09/20/klausmeier-identifiability-fisher-correlation-floor--962dc48d4a2e`  
**Assigned and audited tree:** `1fe78d3b08fb5afb4732c39913e6869fef8de5c3`  
**Repository snapshot:** `SCOPE-Science/SCOPE2026` at inventory commit `e9ed144c13b7834896a844cc4f9cac3c25a168a6`

## Disposition

**PASSED.** The record survives independent review without a substantive research-file edit.

## Correctness

PASS. Integrating the exact ODE gives the displayed derivative-free recovery formulas whenever biomass is positive, while uniqueness on n=0 makes mortality structurally absent there. At positive equilibrium the inverse map (w,n)->(w(1+n^2),wn) has determinant w(1-n^2), correctly isolating the fold. For repeated isotropic Gaussian full-state equilibrium observations, I=(M/sigma^2)S^T S with S=(D Psi)^{-1}, hence the local covariance is proportional to D Psi D Psi^T; direct algebra reproduces the stated correlation and 1-rho^2 formulas. Differentiating in x=n^2 factors with the unique high-branch stationary point x=1+sqrt(2(1+m^2)); substitution gives the stated closed-form floor and, at m=0.45, rho_min=0.9972914395948188. The printed same-sign source equilibria indeed violate wn=m except at the fold; cross-pairing corrects them.

## Originality

PASS only for the source-specific formulas. Structural/practical identifiability theory, Fisher information, inverse-function arguments, and the Klausmeier equilibrium branches are established prior art and are excluded. Searches around the 2026 source, Klausmeier parameter estimation/identifiability, Fisher information, and parameter correlation did not locate the exact continuous full-state recovery dichotomy or the closed-form equilibrium correlation law and global high-biomass floor. The 2017 and 2023 Klausmeier literature supplies equilibrium and inverse-problem context but not these exact formulas. An algebraically equivalent result under systems-identification terminology remains possible.

## Scientific value

PASS. The result sharply separates structural identifiability from practical conditioning in the exact model motivating the source study: mortality is genuinely absent only on the desert invariant set, while positive full-state trajectories identify both parameters exactly, yet equilibrium-only inference can remain almost perfectly collinear. The explicit 0.99729144 floor at m=0.45 turns a qualitative numerical observation into a quantitative geometric explanation and warns against interpreting Fisher magnitude alone as directional identifiability.

## Independent checks

- Integrated both ODEs independently and verified the positive-trajectory parameter formulas and desert invariance.
- Symbolically recomputed D Psi, the Fisher covariance/correlation, derivative factorization, the unique minimizer, and the closed-form floor; the m=0.45 numeric values agree.
- Checked the source equilibrium sign pairing directly against wn=m and distinguished this prior-art correction from the originality claim.
- Checked that the current main-path tree is unchanged from the assignment snapshot.

## Literature and evidence

- https://arxiv.org/abs/2609.18231v1 — Beer, Kuehn and Piazzola (2026), motivating non-spatial Klausmeier parameter-estimation study.
- https://doi.org/10.3390/math5040069 — Köhnke and Malchow (2017), classical nontrivial Klausmeier equilibria and stability context.
- https://doi.org/10.3934/mbe.2023734 — Cruz de la Cruz et al. (2023), generalized Klausmeier model including a distinct inverse-problem setting.

## Limitations

- The trajectory identities require exact continuous full-state observations with positive biomass and are not proposed as noise-robust estimators.
- The Fisher result is local/asymptotic for repeated isotropic Gaussian equilibrium observations; transient data, partial observations, priors, or different noise models can change practical correlation.
- At the exact fold the inverse sensitivity is singular; statements about correlation there are naturally interpreted by the limiting covariance geometry rather than as an invertible Fisher calculation at the singular point.

## Repository guard

The current `main` record tree was checked against the assignment and is unchanged at `1fe78d3b08fb5afb4732c39913e6869fef8de5c3`. The publication plan changes only independent-audit materials and `VERIFICATION.md`; the Lean and expert-attestation channels are preserved exactly as `unknown` with null evidence.
