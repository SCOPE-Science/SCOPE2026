# Independent audit — 2026-09-29 UTC

Record: `2026/09/20/ikeda-critical-delay-stability-and-sharp-relaxation--51fcdbf5a801`  
Assigned source tree: `16745c8c7082565a67b50dd85245e7366c64612a`  
Audited current source tree: `16745c8c7082565a67b50dd85245e7366c64612a`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `54d94a543ecfd156ae04510e8bcbba962506ec40`  
Disposition: **passed**

## Correctness

**independently_supported**. The delay-independent stability boundary and critical asymptotic check. For mu<1, |sin z|<=|z| gives the stated Halanay contraction. At mu=1, differentiating the proposed Lyapunov-Krasovskii functional gives exactly -1/2(x-sin y)^2-1/2(y^2-sin^2 y); its zero-dissipation invariant set is only the zero history, and boundedness plus bounded derivative gives the compactness needed for the retarded LaSalle argument. The characteristic equation lambda+1-exp(-lambda h)=0 has only the simple root zero in the closed right half-plane by the modulus argument. The exact observable Q=x+integral_{t-h}^t x satisfies Q'=sin x(t-h)-x(t-h). With u=Q/(1+h), the center eigenfunction has x=u to first order and oddness removes quadratic terms, yielding u'=-u^3/[6(1+h)]+O(u^5), hence sqrt(t)x(t)->+/-sqrt(3(1+h)) off the strong-stable manifold. For mu>1, the real characteristic function has a positive root.

## Originality

**qualified_source_specific_endpoint_package**. The subcritical stability and supercritical instability are standard and are not new. Nardone-Mandel-Kapral and Kubyshkin-Moriakova study Ikeda steady-state and periodic bifurcation boundaries; the 2020 special-case paper treats the zero-phase mu=1 degeneracy through a singular normal-form construction. In the checked statements, none gives the exact all-fixed-delay critical Lyapunov identity together with global endpoint attraction and the coefficient sqrt(3(1+h)). Broader scalar-delay absolute-stability and center-manifold literature remains a substantial implicit-overlap risk, so novelty is restricted to this explicit endpoint package.

## Scientific value

**meaningful_critical_endpoint_resolution**. The record resolves the nonhyperbolic boundary itself rather than only the two open parameter regimes and quantifies the transition from exponential attraction to generic t^{-1/2} critical slowing with an exact delay-dependent amplitude.

## Independent checks

- Differentiated the Lyapunov-Krasovskii functional and identified the full invariant equality set.
- Rechecked the characteristic-root modulus argument and simplicity of the zero root.
- Derived the cubic center coefficient directly from the exact Q identity and verified the h=0 scalar limit.

## Literature and evidence checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/20/ikeda-critical-delay-stability-and-sharp-relaxation--51fcdbf5a801
- https://doi.org/10.1103/PhysRevA.33.2465
- https://doi.org/10.20537/nd180302
- https://doi.org/10.20537/nd200303
- https://doi.org/10.1007/978-1-4612-4342-7

## Limitations

- Only the zero-phase Ikeda equation is covered.
- The algebraic asymptotic excludes histories on the strong-stable manifold when h>0.
- No classification of nonzero equilibria, periodic attractors or chaotic supercritical dynamics is supplied.
- General scalar delay-equation theory may contain equivalent endpoint consequences under different hypotheses or notation.
