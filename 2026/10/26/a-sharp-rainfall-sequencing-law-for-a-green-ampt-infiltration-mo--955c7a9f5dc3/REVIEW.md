# Self-review

## Correctness — PASS

The claim is stated for the precise one-state instantaneous-runoff infiltration equation, with bounded nonnegative rainfall and no wetting-front relaxation between blocks. The two-rate clock transformation converts rainfall order into a comparison between translation and the flow of a nondecreasing speed ratio; the flow Jacobian is \(w(\Psi_v(z))/w(z)\ge1\). The speed ratio grows strictly only between the two capacity thresholds, which supplies both directions of the strict two-block equivalence. Adjacent swaps and an \(L^1\)-continuous solution map extend the weak bound to general rainfall schedules. The supplied analytic constant-rate solver passed 3000 seeded checks and representative equality tests. Neither those finite tests nor the literature searches replace the general proof.

## Originality — PASS, with identified residual risk

The inspected 2009 Green–Ampt multistorm paper by Gowdish and Muñoz-Carpena and the 2015 infiltration-and-redistribution paper by Lai and colleagues address forecasting and numerical modeling with richer wetting-front states. Neither inspected full text provides the present histogram-rearrangement extremum or the two-rate if-and-only-if equality boundary for the scalar runoff-only equation. Their results do not logically imply the new sharp temporal ordering without an extra comparison argument. Chu (1978) and Philip (1993) were accessible only as abstracts, with Philip's ponded-head assumption distinct; uninspected results and possible general scalar-flow rearrangement literature remain meaningful risks. Originality is a qualified self-review, not an independent novelty certification.

## Mathematical value — PASS

The conclusion provides an exact model-internal best/worst case for runoff when an intensity histogram is known but temporal sequencing is uncertain. The sharp two-bin boundary separates regimes where intensity order changes the modeled flood-runoff volume from those where it has exactly no effect. This is a nontrivial comparison across nonlinear wetting-front trajectories rather than a single constant-rainfall evaluation. Its conditional practical value is limited by the deliberate exclusion of detention, interstorm redistribution, and actual subsurface heterogeneity.

Self-review: passed. Independent audit: not yet performed.
