# Independent audit — 2026-09-30

**Record:** `2026/09/20/rabinovich-quintic-pump-threshold-and-critical-slowing--811a42ee7416`  
**Audited source tree:** `457bc1f740f63d52972ed5b1756da23c2d56ad9e`  
**Disposition:** passed

## Correctness — PASS

PASS. At h=sqrt(nu1 nu2), direct differentiation gives E'= -2(sqrt(nu1)x-sqrt(nu2)y)^2. This bounds x,y globally, the stable z equation bounds z, and LaSalle's largest invariant subset of the zero-dissipation plane reduces to the z-axis, after which z also tends to zero; the small-data bound supplies Lyapunov stability. The critical linear change of variables independently reproduces s'=vz, v'=-(nu1+nu2)v-sz and the displayed z equation. Solving the leading center-manifold invariance equations gives z=(pq/nu3)s^2+O(s^4), v=-(pq/(nu3 D))s^3+O(s^5), hence s'=-(p^2q^2/(nu3^2 D))s^5+O(s^7). Integration yields t^-1/4, and substitution gives t^(1/2)z -> sqrt(nu1+nu2)/2. The post-threshold quartic-root amplitude agrees with the exact equilibrium formulas.

## Originality — PASS

PASS, narrowly scoped. The 1978 primary paper already gives strict subthreshold attraction and the post-threshold equilibria, so neither the threshold location nor the bare branch is new. The accessible modern Rabinovich literature likewise treats r<1 stability and later attractors/bifurcations. I found no source stating the equality-case global theorem, the identically vanishing cubic normal-form coefficient, the fifth-order center dynamics, or the explicit t^-1/4 critical relaxation. A 1981 broad review by the original authors was not available in full text through the lawful sources inspected, so it remains a stated residual coverage risk rather than something claimed to have been read.

## Scientific value — PASS

PASS. The result changes the local interpretation of the first pump threshold from a generic cubic pitchfork to a structurally quintic one and quantifies the associated anomalously slow critical decay. Closing global asymptotic stability at equality is also a useful exact endpoint result.

## Independent checks

- Symbolically recomputed the critical coordinate transformation.
- Solved the leading center-manifold invariance equations independently.
- Recomputed the algebraic-decay constants and quartic-root branch scaling.
- Compared the endpoint claim with the 1978 primary paper and the open-access 2018 Rabinovich-system article.

## Literature evidence

- https://www.jetp.ras.ru/cgi-bin/dn/e_047_04_0715.pdf — Pikovskii, Rabinovich and Trakhtengerts (1978), primary dissipative three-wave source; gives strict subthreshold attraction and post-threshold equilibria.
- https://doi.org/10.1007/s11071-018-4054-z — Kuznetsov et al. (2018), open-access modern Rabinovich-system study; focuses on dissipativity, attractors and finite-time Lyapunov dimension rather than the critical center normal form.
- https://arxiv.org/abs/1806.01306 — Pusuluri, Pikovsky and Shilnikov, later global bifurcation/chaos organization above the first threshold.

## Limitations

- Positive damping parameters and positive pump are assumed.
- The t^-1/4 law excludes the two-dimensional strong-stable manifold, whose decay is exponential.
- The 1981 Pikovskii--Rabinovich review and older Russian-language analyses were not available in full text here and remain residual originality risks.

No GitHub write was performed by the audit chat. This file is staged by the guarded `scope-audit-change-set-v1` plan only.
