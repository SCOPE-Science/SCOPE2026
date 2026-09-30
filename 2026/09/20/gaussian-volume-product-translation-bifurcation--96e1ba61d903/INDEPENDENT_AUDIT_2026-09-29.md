# Independent Audit — Quartic endpoint stability and translation bifurcation for the Gaussian volume product

**Audit date:** 2026-09-29 (UTC) (UTC)  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Assigned source tree:** `7c9fee98b3faef7b86ec7d0fc1a7618da9c54fe6`  
**Audited current source tree:** `7c9fee98b3faef7b86ec7d0fc1a7618da9c54fe6`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Disposition:** passed

The current `main` record path is unchanged from the dispatcher's source-check commit, so the audited tree equals the assigned source tree. GitHub was used read-only. The UTC-dated independent-audit marker files were absent when this guarded change set was prepared.

## Correctness — PASS

PASS. The fourth-order translation calculation is consistent with the source's second-order expansion and with direct numerical integration. For A(epsilon,s), differentiating the shifted Gaussian integral gives the stated fourth coefficient from the spherical second and fourth moments. For the polar factor, rho(u)=(1+epsilon<u,e>)^{-1}; Taylor expansion through fourth order gives the displayed critical coefficients. At s_c=2/(n+1) the quadratic terms cancel and multiplication yields c_4=-R_n(n+1)D_n/(32n(n+2)). The bound R_n>(n-1)/2 makes D_n>0. Even analyticity then reduces the local critical equation to a scalar equation in q=epsilon^2; the implicit-function theorem gives the square-root branch and its gain. I independently integrated the translated ball/polar product numerically at n=2,3,5 and epsilon=0.03,0.02,0.01; (1-Phi)/epsilon^4 converged to the submitted beta_n values.

## Originality — PASS

PASS. The full current arXiv v1 was inspected. Proposition 5.1 translates the Euclidean ball and expands both Gaussian factors only through order epsilon^2, obtaining the coefficient proportional to n+1-2/sigma^2 and using it for the strict supercritical regime sigma^2>2/(n+1). The paper does not compute the quartic coefficient at equality or a nearby nonzero translated critical branch; its subsequent sections turn to global planar and small-variance maximization. Targeted searches found no separate higher-order translation/bifurcation result. The audited originality is therefore the endpoint fourth variation and local symmetry-breaking law, not the underlying Gaussian volume product or the source's second variation.

## Scientific value — PASS

PASS. The theorem resolves the degeneracy left exactly at the source's translation threshold: the centered ball remains strictly quartically stable within translations at equality, then loses radial stability and emits an (n-1)-sphere of translated local maxima with explicit square-root scaling and gain. This sharpens the phase-transition picture while clearly remaining a finite-dimensional translated-ball statement rather than a full convex-body stability theorem.

## Independent checks

- Read the full current arXiv:2609.18472v1; Proposition 5.1 expands translated balls through epsilon^2 and proves non-maximality only for sigma^2>2/(n+1).
- Re-derived the fourth coefficient of the translated-ball Gaussian factor from the divergence theorem and spherical moments.
- Re-expanded the polar radial integral through fourth order and checked cancellation of the critical quadratic terms.
- Rechecked the lower bound on R_n, positivity of D_n, the implicit-function branch coefficient and the gain coefficient.
- Independently evaluated the exact radial/spherical integrals for n=2,3,5; the normalized fourth-order errors converge to the stated beta_n.
- Targeted searches for quartic endpoint stability and translated-ball bifurcation found no covering prior result.
- GitHub comparison found no changes under the assigned record path; both UTC-dated audit files are absent and VERIFICATION.md retains the verified blob SHA.

## Limitations

- The result concerns only translations of the fixed unit ball and does not prove full shape stability or global optimality in dimensions n>=3.
- The bifurcating orbit is locally maximal only inside the translated-ball family.
- The motivating preprint is extremely recent, so unindexed parallel work remains a residual priority risk.

## Evidence and references

- https://arxiv.org/abs/2609.18472
- https://arxiv.org/pdf/2609.18472
- https://doi.org/10.1016/S1631-073X(02)02328-2
- https://github.com/SCOPE-Science/SCOPE2026/tree/eff2c6312cec5b0dee5115e5f42211a853092dfb/2026/09/20/gaussian-volume-product-translation-bifurcation--96e1ba61d903

This guarded change set updates only the independent-audit channel. Lean verification and expert attestation remain exactly as previously recorded.
