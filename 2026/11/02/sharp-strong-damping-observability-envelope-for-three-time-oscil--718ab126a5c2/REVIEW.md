# Independent mathematical audit

## correctness

PASS

For H row j=e^{-ajh}(cos(jωh),sin(jωh)), j=0,1,2, direct Cauchy–Binet gives D=e^{-2ah}sin²(ωh)+e^{-4ah}sin²(2ωh)+e^{-6ah}sin²(ωh). Applying |sin x|<|x| for positive x yields D<ε²g(u), u=ah, ε=ω/a, g=u²(e^{-2u}+4e^{-4u}+e^{-6u}); ε→0 at fixed u proves sharp global envelope. The derivative equation 1/u=m(u) has exactly one root using the explicit (1-e^{-2u})^4 variance bound, and g has a nondegenerate maximum. Localization by Φε≤g and compact C² convergence imply unique true optimum for sufficiently small ε; implicit differentiation of Φε=g-ε²k+O(ε⁴), k=u⁴(e^{-2u}+16e^{-4u}+e^{-6u})/3, gives c3=k′/g″ and K3=k. Independent numerical reconstruction: u3=0.631289958074151, C3=0.24937906195962, c3=-0.23880902554942, K3=0.083980623867224. Checked sample normal-matrix determinant directly.

## originality

PASS

Primary full-text complex OU D-optimal design studies stationary process correlated measurements of both coordinates and unknown trends/covariances, not three independent-noise scalar readings estimating an unknown deterministic 2-vector. General observability scheduling and arithmetic-spectrum design summaries do not establish this exact sharp envelope and spacing expansion. Unindexed oscillatory experimental-design computations remain a plausible risk.

## value

PASS

Three scalar samples in a rapidly decaying oscillator must trade accumulated phase against amplitude loss. The sharp universal information limit, unique high-damping spacing, and finite-frequency correction quantify a concrete design tradeoff for a natural minimal-state estimation problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
