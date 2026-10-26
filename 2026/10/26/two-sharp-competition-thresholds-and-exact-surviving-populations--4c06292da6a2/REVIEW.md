# Scientific review

## Correctness

PASS. The first update kills each initial biomass-one site and changes each initial biomass-two site to one when competition exceeds one. The second update depends only on the number (zero, one, or two) of initially biomass-two neighbors. The run decomposition then isolates singleton fixed sites and two-site paired oscillators. All equality conditions, cyclic wraparound, complete extinction configurations, and finite-size expectations are handled algebraically. Exact-rational replay of 14,224 finite cases supports the symbolic argument without being substituted for it.

## Originality

PASS under the evidence available, with residual historical-priority uncertainty. The closest source, Sergo et al., arXiv:2606.09494v1, defines the sign-update model and proves that eventual periods cannot exceed two; that upper bound alone neither identifies the finite-cycle basins nor gives the two sharp expected survival densities or the exponentially high probability of two-cycles. Related numerical and discretized Lotka–Volterra works use different update maps. No implication-equivalent published mathematical record was found by the named searches, but equivalent one-dimensional cellular-automaton results remain a risk; material from the main source's full appendix was not completely retrievable during comparison.

## Mathematical value

PASS. The finite degree-two ring is a natural benchmark for network-driven ecological clustering, not an arbitrary parameter slice. The theorem fully classifies the dynamics and provides a sharp, discontinuous change in occupied-site density and oscillator persistence at a physically interpretable interaction threshold. The exact finite-size extinction probability and asymptotically certain oscillation phenomenon give testable calibrations of the much more general network model; no broad empirical claim is asserted.

## Limitations and closest literature

The result covers only uniform degree-two cycles, carrying capacity two, positive binary initial biomasses, and coupling larger than one. The first public source is Sergo, Koller, Erba, and Zdeborová (2026); earlier works by Roeger (2008) and Feldager, Mitarai, and Ohta (2017) discuss distinct discrete competition and ring-mixing models. Only a self-review has been performed.

Self-review: passed. Independent audit: not yet performed.
