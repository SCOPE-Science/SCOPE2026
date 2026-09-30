# Independent audit — 2026-09-29

Record: `2026/09/17/log-slope-no-pattern-spatial-memory--5ddf2e7adc1e`  
Assigned and audited source tree: `3e42b489644626a99299e269b6c4235d58bd4c58`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Disposition: **passed**

## Correctness

**supported**. The steady-state energy argument is correct. Setting Psi=d log U+alpha V converts the first equation to div(U grad Psi)=0; the Neumann conditions and U>0 force Psi to be constant. After z=log U and w=V-mean(V), one gets z-mean(z)=-(alpha/d)w and -R^2 Delta w+w=phi(z)-mean(phi(z)). Testing by w yields the stated exact covariance identity. The double-integral covariance formula has the required sign when alpha*phi is nondecreasing, forcing w=0. If phi is L-Lipschitz, its covariance is bounded by L||z-mean(z)||_2^2; substituting the exact z-w relation and the Neumann Poincare inequality gives the threshold |alpha|L<d(1+R^2 lambda_1). For h(u)=u/(1+u), sup u h'(u)=1/4. The motivating paper's no-growth linear bifurcation formula has first mode n=1; at u*=1 with w_k=-1 and w_u=1/4 it indeed gives alpha_1=-4d(1+R^2), exactly matching the global exclusion boundary from the stable side.

## Originality

**qualified_specific_global_obstruction**. Salmaniw-Liu-Shi-Wang establish well-posedness, linear stability and local steady bifurcation for the spatial-memory model, including the n=1 no-growth critical mode, but do not state this global logarithmic-slope steady-state obstruction in the material located. Searches of the motivating work, the 2026 nonlocal-advection review and broader query terms did not locate the exact covariance criterion. Because related entropy/energy methods are common in chemotaxis and aggregation-diffusion, originality is accepted only for this model-specific theorem and sharp saturating-law consequence.

## Scientific value

**meaningful_global_complement_to_bifurcation**. The result upgrades local linear/bifurcation information to a finite-amplitude nonexistence theorem for all positive stationary patterns in an explicit parameter region. The saturating example is especially useful because the global boundary reaches the first local bifurcation threshold, excluding detached positive steady branches on the stable side.

## Literature and evidence checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/17/log-slope-no-pattern-spatial-memory--5ddf2e7adc1e
- https://arxiv.org/abs/2503.11550
- https://doi.org/10.1007/s00332-025-10233-9
- https://doi.org/10.3934/dcds.2026134
- https://arxiv.org/abs/2201.09150

## Limitations

- The theorem concerns positive classical steady states only and does not imply time-dependent convergence or absence of oscillatory/chaotic attractors.
- The multidimensional formulation is for the displayed local elliptic-smoothing system; exact equivalence with the original convolution model is supplied by the source in the one-dimensional even-periodic setting.
- The quantitative inequality is strict and can be vacuous if sup_u u|h'(u)| is infinite.
- The originality search cannot rule out an equivalent energy estimate hidden in the broad chemotaxis or aggregation-diffusion literature.
