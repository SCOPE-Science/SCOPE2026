# Same-model review

## Correctness
**PASS.** Centering at \(Q_0=(0,1/b,0)\) gives an exact cancellation of both \(xz\) and \(x^2(y-1/b)\), leaving
\[
\dot V=(1/b-a)x^2-b(y-1/b)^2-cz^2.
\]
The embedded exact checker confirms the coefficient identity. The strict case gives a global exponential estimate. At \(a=1/b\), properness of \(V\) supplies forward completeness and LaSalle reduces the zero-derivative set to \(Q_0\). The backward-filter formula for \(y\) is exact for bounded complete trajectories and yields strictness unless the trajectory is the equilibrium.

## Originality
**PASS.** The two foundational Ma–Chen papers were read in full and provide local equilibrium/bifurcation structure rather than this global theorem. Aybar's 2020 full text contains the closest exact predecessor: on \(b=c\), \(c(a-c)=1\), the quadratic Darboux polynomial \(I^*=x^2+(y-1/c)^2+z^2\) has cofactor \(-2c\). That curve is a special case of the strict region here; it does not imply the arbitrary-
\(b,c\) half-space, the endpoint \(a=1/b\), or the bounded-complete ceiling. Semantic literature-index searches for the exact vector field, centered energy, source DOI, aliases, and ceiling returned no same-system dominating result. The selected Yao article, Szumiński's non-integrability result, Cândido–Llibre–Valls' Hopf/invariant-surface work, and Rao–Zhong's controlled delayed system do not imply the claim.

## Value
**PASS.** The half-space \(a\ge1/b\) is defined by the model's savings and investment-cost parameters rather than an arbitrary numerical slice. It separates a region with a rigorous open-loop global attractor and unique compact stationary state from parameter regimes where recurrent behavior is possible, supplies a quantitative exponential rate off the boundary, and gives a strict pointwise investment-demand ceiling on every non-equilibrium bounded complete trajectory. This is a structural extension of a known special Darboux identity, not a table recomputation.

## Closest literature and limitations
The closest exact statement found is Aybar's special quadratic Darboux case. Ma–Chen I/II provide the original local and bifurcation analysis; Rao–Zhong treat impulsively controlled delayed variants; Yao et al. treat fixed-time synchronization. The public abstract rather than publisher full text was inspected for Cândido–Llibre–Valls. The theorem here certifies a closed half-space and does not claim a complete global-stability classification outside it.

Same-model review: passed. Independent audit: not yet performed.
