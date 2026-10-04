# Review

## Correctness

PASS. Every state \((0,0,V)\) is fixed because the Yogi second-moment increment is multiplied by the squared gradient. For \(V>0\), the local sign branch is constant and the map is differentiable. Its Jacobian has tangent eigenvalue \(1\) and an exact \(2\times2\) transverse block with determinant \(\beta_1\) and trace \(1+\beta_1-(1-\beta_1)\chi_V\). The Jury conditions give the stated necessary-and-sufficient transverse-stability inequality and the exact accumulator threshold. At equality, the transverse polynomial factors as \((r+1)(r+\beta_1)\).

Risk: no global claim is made for trajectories initialized at the nonsmooth endpoint \(V=0\).

## Originality

PASS. The defining Yogi paper gives the additive second-moment rule, a stochastic convergence theorem, and a practical warning that second-moment initialization matters, but its inspected text does not give a deterministic fixed-manifold or local Jacobian analysis. Focused searches for Yogi fixed points, scalar quadratic stability, accumulator initialization, local spectra, and limit cycles did not identify the invariant equilibrium ray or the exact \(V_c\) threshold. A current implementation documents a configurable nonzero initial accumulator, which makes the state dependence operationally relevant rather than artificial.

Residual risk: a generic dynamical-systems analysis of adaptive optimizers may contain an equivalent neutral-manifold observation without using Yogi-specific terminology.

## Value

PASS. Yogi was designed specifically to alter how the second-moment state remembers past gradients, and its source paper reports initialization sensitivity. The result identifies a structural consequence of that design: unlike an EMA second moment that decays at a zero gradient, Yogi can retain any positive accumulator forever at the optimum. The exact threshold quantifies when that retained state stabilizes or destabilizes curvature and shows the corresponding speed penalty.

Same-model review: passed. Independent audit: not yet performed.
