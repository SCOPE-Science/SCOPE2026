# Independent audit — 2026-09-30 UTC

Record: `2026/09/20/two-lag-variance-envelopes-positive-reversible-chains--faa525a3c3c5`  
Assigned and audited source tree: `23162899020d484e11d308488033b0a35ec6dd6f`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `aa28ffc11d621af904d9937872860f4b3bd117e9`  
Disposition: **passed**

## Correctness

**independently_supported**. The two-moment envelopes and variance consequences are correct. Positivity and reversibility give a probability spectral measure on [0,1] with first moments rho and q. The lower measure on {0,q/rho} and upper measure on {(rho-q)/(1-rho),1} reproduce exactly the two prescribed moments. Quadratic Hermite interpolation has remainder signs x(x-b)^2>=0 and (x-a)^2(x-1)<=0, so every C^3 function with nonnegative third derivative lies between the two expectations. Applying this to x^k gives the later-lag bounds, and to H_N gives the sharp finite-horizon variance interval because H_N''' is positive for N>=4 and N<=3 is already determined by two moments. For g(x)=(1+x)/(1-x), the lower extremizer yields tau>=1+2rho^2/(rho-q). If v=q-rho^2>0, the displayed two-point family with c<1 has exactly fixed first two moments and a positive mass tending to a nonzero limit at c as c approaches 1, so tau diverges. Products of the stated two-state refresh chains realize these two-atom spectral measures in finite-state positive reversible chains.

## Originality

**qualified_supported_classical_moment_specialization**. The spectral representation and moment-sequence viewpoint are established prior work; Berg-Song explicitly base reversible-chain autocovariance estimation on moment representability, and truncated Hausdorff/Markov-Krein extremal theory is classical. Targeted searches did not locate the audited closed-form fixed-(r1,r2) package: simultaneous sharp later-lag envelopes, exact finite-horizon variance interval, the geometric identification boundary q=rho^2, and the finite-state exact-moment construction proving unbounded asymptotic variance for q>rho^2. Originality is therefore restricted to this MCMC-oriented specialization and attainability package, with explicit risk of an equivalent older moment-problem formulation.

## Scientific value

**meaningful_exact_identification_region**. The result states exactly what two population autocorrelations do and do not determine under positive reversibility: every finite-horizon mean variance has a sharp computable range, while long-run variance can be arbitrarily bad unless the moments collapse to a single spectral atom. That distinction is practically relevant to short-lag MCMC diagnostics.

## Independent checks

- Verified algebraically that both extremal two-point measures have first moment rho and second moment q.
- Checked both Hermite remainder signs and the strict positivity of H_N''' for N>=4.
- Reduced the lower asymptotic-variance endpoint exactly to 1+2rho^2/(rho-q).
- Verified symbolically that the c-dependent two-point family preserves both moments exactly and that finite-state refresh kernels realize the required atoms.

## Literature and evidence checked

- https://doi.org/10.1007/BF01210789
- https://doi.org/10.1214/ss/1177011137
- https://doi.org/10.1214/07-AAP486
- https://doi.org/10.1214/23-AOS2335
- https://arxiv.org/abs/2207.12705
- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/20/two-lag-variance-envelopes-positive-reversible-chains--faa525a3c3c5

## Limitations

- The observable spectrum must lie in [0,1]; arbitrary reversible chains with negative spectrum require a different moment problem.
- The bounds concern one fixed observable and exact population lags rather than uncertain empirical autocorrelations.
- The exact upper finite-horizon endpoint with an atom at 1 is nonergodic when spectral variance is positive, although irreducible finite-state chains approach it with exact prescribed moments.
- The generic two-moment extremal principle is classical and not part of the novelty claim.
