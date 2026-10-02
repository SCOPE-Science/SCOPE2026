# Independent scientific audit — SCOPE-20260917-5ddf2e7adc1e

Audited at: 2026-10-01T06:12:13.318800Z

Disposition: **passed**

## Correctness — PASS

The first steady equation is exactly \(\nabla\!\cdot(U\nabla[d\log U+\alpha V])=0\); testing against the bracketed potential and using \(U>0\) and Neumann conditions forces \(d\log U+\alpha V\) to be constant. With \(K=h(U)\), centering the elliptic equation and writing \(z=\log U\), \(w=V-\overline V\) gives \(z-\overline z=-(\alpha/d)w\). The covariance identity yields the sign obstruction when \(\alpha\phi\) is nondecreasing. If \(\phi\) is \(L\)-Lipschitz, Cauchy-Lipschitz plus the Neumann Poincare inequality gives \((1+R^2\lambda_1)\|w\|_2^2\le |\alpha|L\|w\|_2^2/d\), proving global uniqueness under the strict criterion. For \(h(u)=u/(1+u)\), \(\sup_u u h'(u)=1/4\), matching the source's first negative bifurcation threshold at mean one.

## Originality — PASS

The motivating primary paper develops well-posedness, linear stability, and local bifurcation for the spatial-memory system. The inspected no-growth section gives the local critical strengths and first critical mode, but not the global logarithmic-slope covariance obstruction. Targeted Resultary and literature searches did not locate an equivalent global theorem.

### Equivalent formulations

No equivalent all-amplitude positive-steady-state exclusion criterion was located.

### Broader coverage

Broader dynamical coverage does not imply the global stationary uniqueness theorem.

### Exact database or table

The result is an analytic energy/covariance theorem, not a table lookup.

### Claim versus prior implication

The sharp threshold match in the saturating example is therefore stronger than restating linear stability.

## Value — PASS

The theorem converts a local pattern-formation picture into a global exclusion of every positive finite-amplitude stationary pattern in an explicit parameter region. In the saturating law it reaches exactly the first local bifurcation threshold from the stable side, ruling out detached/subcritical positive steady branches there.

## Sources inspected

- Dynamics of a Coupled Nonlocal PDE-ODE System with Spatial Memory: Well-Posedness, Stability, and Bifurcation Analysis — https://arxiv.org/abs/2503.11550. NOT_COVERING: The inspected no-growth section is local stability/bifurcation analysis and does not state a global all-amplitude logarithmic-slope uniqueness theorem.
- Bifurcation and Pattern formation in reaction-diffusion models with nonlocal advection and time delays — https://doi.org/10.3934/dcds.2026134. NOT_COVERING_IN_MATERIAL_READ: No theorem matching the exact covariance criterion or its sharp saturating-law consequence was located.

## Residual risks

- Broad chemotaxis and aggregation-diffusion literatures contain related entropy/steady-state arguments under different variables; no exact implication was located in this run.

## Limitations

- The theorem concerns positive classical steady states only.
- It does not establish dynamical convergence or exclude nonstationary attractors.
- The quantitative criterion is strict; equality is unresolved in general.
