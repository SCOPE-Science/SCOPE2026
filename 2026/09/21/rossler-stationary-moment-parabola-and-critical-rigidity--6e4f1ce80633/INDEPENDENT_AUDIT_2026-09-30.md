# Independent Audit — Exact stationary moment parabola and critical rigidity in the Rössler system

**Audit date:** 2026-09-30 (UTC) (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `0ac1cfd6a57407a1f98b10495cd7cfcaac44413d`  
**Audited current source tree:** `0ac1cfd6a57407a1f98b10495cd7cfcaac44413d`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` directory tree exactly matches the assigned snapshot tree. GitHub was used read-only. `INDEPENDENT_AUDIT_2026-09-30.md` and `.json` were absent when this guarded change set was prepared.

## Correctness — PASS

PASS. Invariance of x, y, z, (x^2+y^2)/2, and x^2/2 under the flow gives the stated first- and second-moment balances exactly. Eliminating the means yields Var(y)=(cm-b-am^2)/a, which factors as (m-z_-)(z_+-m), and the covariance identities follow immediately. The heightwise law is also sound: testing invariant measures against ψ(z) shows the compactly supported signed measure [b+z(E[x|z]-c)]ν has zero distributional derivative; compact support forces that measure to vanish, giving ν({0})=0 and E[x|z]=c-b/z almost everywhere. Nonnegativity of variance then gives the discriminant obstruction, critical uniqueness, endpoint rigidity, and the sharp two-equilibrium mixture envelope.

## Originality — PASS

PASS, narrowly scoped. Starkov–Starkov's localization work is prior art for exclusion of periodic dynamics in parts of parameter space and is not credited. Kontorovich et al. explicitly describe their Rössler variance relation as approximate and note that exact variance evaluation is not achieved by their cumulant closure. Targeted searches did not locate the exact invariant-measure moment parabola, the heightwise conditional-mean identity, or the discriminant-zero uniqueness/statistical-rigidity theorem. The originality claim is limited to these exact stationary-measure consequences.

## Scientific value — PASS

PASS. The theorem gives closed analytic constraints on every compact stationary state, not just a numerically sampled physical attractor, and turns the equilibrium discriminant into a complete one-dimensional moment feasibility interval. The critical case yields uniqueness of the compact invariant probability measure and time-average rigidity for every bounded forward-global trajectory, while carefully avoiding an unsupported pointwise-convergence claim.

## Independent checks

- Re-derived every displayed moment identity directly from Lie derivatives.
- Checked the conditional-expectation argument as a distributional zero-flux statement on the z marginal.
- Verified endpoint variance zero forces y, then x and z, to be constant on invariant support, hence an equilibrium delta measure.
- Checked that convex mixtures of the two equilibrium deltas realize every point of the claimed moment parabola.
- Compared with the 2009 cumulant-analysis paper, which characterizes its variance calculation as approximate rather than the exact stationary identity here.
- Compared with Rössler localization literature; no exact stationary-measure parabola or conditional law was located.
- Current main exactly matches the assigned source tree; the dated audit files are absent and VERIFICATION.md is unchanged.

## Limitations

- The invariant-measure results assume a,b,c>0 and compact support.
- The theorem does not classify noncompact invariant objects or prove pointwise convergence of every bounded trajectory at the critical discriminant.
- The no-compact-dynamics consequence in the negative-discriminant regime is close to earlier localization work and is not treated as the principal originality claim.

## Evidence and references

- https://doi.org/10.1016/0375-9601(76)90101-8
- https://doi.org/10.1016/j.chaos.2006.02.011
- https://doi.org/10.2174/1874110X00903020029
- https://doi.org/10.1098/rspa.2023.0627
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/21/rossler-stationary-moment-parabola-and-critical-rigidity--6e4f1ce80633

This guarded change set changes only the independent-audit channel of `VERIFICATION.md`; the Lean-verification and expert-attestation channels remain exactly as previously recorded.
