# Independent audit — 2026-09-30

Record: `2026/09/19/nonuniform-dct-limit-ar1-klt--0e66e853b965`  
Assigned and audited source tree: `5286c10e8e4d19f394508e31319b63b9d8dff623`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `28af218c98ecb9144b704fd8170f8b177228180d`  
Disposition: **passed**

## Correctness

**independently_supported**. The joint high-correlation/large-block asymptotic is correct. Setting x_{m,N}=Nω_{m,N} in the exact AR(1) phase equation and assuming N(1-ρ_N)→c gives tan((mπ-x)/2)=x/c; the left side decreases from infinity to zero on ((m-1)π,mπ), so the root is unique. The centered sinusoidal eigenvector formula then converges by Riemann sums to the stated Robin-profile mode, while the exact eigenvalue formula gives λ_{m,N}/N→2c/(c²+x_m(c)²). For m=1, integrating the limiting centered cosine against the constant function reproduces the overlap A(c) and distance D(c), so DCT-DC convergence occurs iff N(1-ρ_N)→0. Independent dense diagonalization at representative critical scalings agrees with the formula, including D(1)=0.066212844... and the Dirichlet-side limit sqrt(2-4sqrt(2)/π)=0.446505730.... The exact inverse-covariance identity T_N=ρ[L_N+(1-ρ)E_N]+(1-ρ)²I also checks entrywise and explains the boundary scale.

## Originality

**qualified_joint_limit_refinement**. The AR(1) KLT eigenvectors, transcendental phase equations, continuous exponential-kernel Robin equations, and fixed-N ρ→1 DCT limit are classical. The full Torun–Akansu 2013 paper was obtained through authorized institutional access after open-access attempts failed and inspected; it explicitly gives the discrete transcendental KLT kernel, the continuous analogue, and the fixed-N DCT endpoint, but it does not state the N(1-ρ) joint boundary law or the first-row nonuniformity criterion. Reznik's 2026 factorization likewise states correction factors approaching identity at fixed block length. Targeted searches did not locate the critical joint limit, explicit D(c), or the resulting operator-norm obstruction. Novelty is therefore supported only for that nonuniform joint-limit analysis.

## Scientific value

**meaningful_nonuniformity_theorem**. The theorem supplies the missing quantifier behind the familiar 'high correlation implies DCT' heuristic: large blocks require 1-ρ=o(1/N) even for the leading mode. The explicit Robin crossover and macroscopic Dirichlet-side row distance directly constrain when a new exact DCT-core factorization can be approximated by dropping its correction stage.

## Literature and evidence checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/19/nonuniform-dct-limit-ar1-klt--0e66e853b965
- https://arxiv.org/abs/2609.20221
- https://doi.org/10.1109/TSP.2013.2265225
- https://doi.org/10.1049/ip-f-1.1981.0061
## Literature access note

The prior source `10.1109/TSP.2013.2265225` was obtained through authorized institutional access and inspected (10 pages). Contains the discrete AR(1) KLT transcendental kernel, its continuous exponential-covariance analogue, and a fixed-N rho→1 DCT remark; no N(1-rho) joint-limit theorem was found.

## Limitations

- The asymptotic is for each fixed low mode; it is not uniform over all N transform rows.
- The transform-level result is an operator-norm lower bound from one row, not a full correction-spectrum asymptotic.
- Continuous exponential-covariance Robin eigenproblems and the fixed-N DCT endpoint are prior art.
- No coding-gain or end-to-end approximation guarantee is proved.
