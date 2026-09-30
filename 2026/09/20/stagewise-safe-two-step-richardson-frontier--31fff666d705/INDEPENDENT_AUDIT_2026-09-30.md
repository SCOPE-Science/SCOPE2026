# Independent Audit — Sharp stagewise-safe Richardson frontier and a no-acceleration barrier

**Audit date:** 2026-09-30 (UTC) (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `a1a616dba5a20bdf28f26e786eb5f168ec9e77ff`  
**Audited current source tree:** `a1a616dba5a20bdf28f26e786eb5f168ec9e77ff`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` record tree exactly matches the assignment snapshot. GitHub was used only as read-only evidence. The UTC-dated independent-audit files were absent when this guarded change set was prepared.

## Correctness — PASSED

PASS. Uniform Euclidean nonexpansiveness of one Richardson factor over [mu,L] is exactly 0<=tau<=2/L. The unconstrained degree-two shifted-Chebyshev polynomial has roots producing normalized steps u=2/(1+a±(1-a)/sqrt(2)), so feasibility changes exactly at a=sqrt(2)-1, i.e. kappa=1+sqrt(2). In the constrained branch the submitted endpoint lower bound is valid and the pair {u,v}={2,2/(1+2a)} equioscillates at the endpoints; its sole interior extremum has magnitude a^2/(1+2a), which stays below the endpoint value precisely on the claimed branch. I independently evaluated dense spectral grids at kappa=1.1,2,1+sqrt(2),3,10,100 and reproduced every closed-form optimum to numerical precision. The m-stage lower bound follows immediately by evaluating at lambda=mu.

## Originality — PASSED

PASS, narrowly scoped. Classical Golub–Varga Chebyshev semi-iteration and later reviews establish the unrestricted Chebyshev/Richardson acceleration theory, including factorized parameter behavior; Manteuffel treats a different stationary second-degree minimax problem. Public full text for Golub–Varga Part I is available and targeted searches for the exact per-factor nonexpansiveness constraint, the transition 1+sqrt(2), and the constrained two-step formula found no matching theorem. The new credit is only for this explicitly stagewise-safe minimax frontier and the resulting first-order-factor no-acceleration barrier.

## Scientific value — PASSED

PASS. The theorem quantifies the exact price of insisting that every first-order factor be nonexpansive: two-step Chebyshev optimality breaks at a sharp condition number and the same safety constraint forces O(kappa log(1/epsilon)) rather than O(sqrt(kappa) log(1/epsilon)) complexity for arbitrarily many factors. This cleanly distinguishes factorwise safety from stability of a three-term Chebyshev recurrence.

## Independent checks

- Re-derived the Chebyshev-root feasibility threshold and both closed-form minimax values.
- Rechecked the constrained lower-bound equality conditions and uniqueness of the unordered optimal pair.
- Dense-grid numerical verification at six representative condition numbers matched the formulas to floating-point precision.
- Re-derived the comparison identities against repeated optimal Richardson and unrestricted degree-two Chebyshev.
- Checked the m-stage lower bound at lambda=mu and the asymptotic iteration-count expansion.
- Compared with openly accessible Golub–Varga Part I, Axelsson's open historical review, and Manteuffel's stationary second-degree formulation; no covering stagewise-safe theorem was found.
- Verified the current main tree SHA exactly equals the assigned source-tree SHA; the dated audit pair is absent and VERIFICATION.md is unchanged.

## Limitations

- The result concerns exact arithmetic, SPD spectra in a continuous interval, and first-order Richardson-factor representations.
- It does not cover stable three-term Chebyshev recurrences, discrete-spectrum tailoring, or floating-point internal amplification.
- Restricted-zero minimax approximation is a broad older subject, so a differently phrased approximation-theoretic equivalent remains a residual priority risk.

## Evidence and references

- https://eudml.org/doc/131485
- https://doi.org/10.1007/BF01386014
- https://doi.org/10.1155/2010/972794
- https://doi.org/10.1137/0719058
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/20/stagewise-safe-two-step-richardson-frontier--31fff666d705

This guarded change set updates only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
