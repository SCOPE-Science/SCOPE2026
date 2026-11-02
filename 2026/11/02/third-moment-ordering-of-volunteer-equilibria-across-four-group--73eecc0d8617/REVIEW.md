# Scientific review: four-size moment order in the volunteer game

## Correctness — PASS

For the specified random focal-player size model, each interaction gives the known one-volunteer payoff gradient \(BG_p(1-x)-C\). Because all sizes are at least two, \(G_p\) is strictly increasing from 0 to 1, giving one attracting interior equilibrium for every \(0<C/B<1\). The four-size moment-matching nullspace has dimension one and is spanned by Lagrange barycentric weights. The proportionality factor is precisely the difference in third raw moments, and the third divided difference of \(q^{t-1}\) is negative for all \(0<q<1\). This proves the global sign and root comparison, not merely a sampled assertion. A five-size example with identical moments through order three provides a strict positive generating-function gap. The exact-rational standalone checker reports 2330 passed assertions, testing 210 ordered four-node supports and both rational examples. Exact arithmetic supports, but does not replace, the proof.

## Originality — PASS within inspected evidence; historical priority provisional

Diekmann (1985) introduced the fixed-size volunteer dilemma. Peña (first public online November 4, 2011) developed random-group public-good replicator dynamics and the N-person volunteer case, with Jensen comparisons for group-size variability. His relevant article and appendices were materially examined. Brännström et al. (2010) developed broad analyses of group-size fluctuations in continuous-investment evolutionary games; relevant sections were examined. Their explicit results, as inspected, do not establish the comparison of *two distinct laws of equal mean and variance* using the third moment across every benefit–cost ratio, nor its five-support obstruction. Multiple scientific searches for the aliases moment-matched generating functions, divided-difference ordering and volunteer equilibria found no implication-equivalent published finding. These checks are not proof of global priority, and the interpolation lemma itself is classical. Specialized unlocated literature remains a genuine historical-priority risk.

## Value — PASS

Mean and variance are standard coarse summaries of measured group size, and prior work shows that group-size heterogeneity affects public-good selection. The theorem supplies the first nontrivial support-size regime in which such summaries leave an ambiguity but the third moment resolves the **entire** equilibrium comparison across parameter values. The explicit five-class pair marks the sharp point where that information ceases to suffice. This is a useful structural distinction about equilibrium inference rather than an arbitrary numerical slice. Scope is restricted to the idealized well-mixed replicator model with fixed focal law, independent potential volunteers and shared costs and benefits.

## Limits and closest literature

The four-size criterion is not claimed for general unbounded supports. The result makes no claim about empirical estimation, assortment or stochastic finite-population fixation. Complete historical priority and independent validation are outstanding. Closest sources: Diekmann (1985), https://doi.org/10.1177/0022002785029004003; Peña (2011), https://doi.org/10.1111/j.1558-5646.2011.01504.x; Brännström et al. (2010), https://arxiv.org/abs/1010.5478.

Self-review: passed. Independent audit: not yet performed.
