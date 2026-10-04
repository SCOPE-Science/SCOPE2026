# Same-model review

## Correctness

PASS. The disease-free subsystem gives an exact counterexample. Before the senescence switch, \(u=L=I=R=0\) and \(H\) follows a positive logistic equation. Immediately after the switch, the printed removed equation gives \(\partial_tR=-r_sH<0\) at the boundary \(R=0\). The explicit update printed in the paper has the identical sign defect. Summing the component equations independently reproduces the source’s doubled senescence term in the total-density balance.

## Originality

PASS. The predecessor spore-dispersal paper has no HLIR removed compartment, while broader plant-disease HLIR literature supplies only the general compartmental context. Exact-title, DOI, positivity, removed-density, senescence, and equivalent-formulation searches found no published correction or prior source-specific counterexample. The claim is restricted to this printed model and does not claim novelty for the general inward-pointing criterion for compartment systems.

## Value

PASS. The paper interprets \(R\) as a density and uses \(H+L+I+R\) in disease severity. Failure of nonnegative invariance therefore affects the mathematical admissibility of the modeled state, not merely a cosmetic formula. The exact boundary trajectory pinpoints a necessary correction target without overclaiming which biological repair is preferred.

## Closest literature and limitations

The primary source is DOI 10.3934/math.2023125. Its immediate predecessor, DOI 10.3390/sym14061131, develops only the healthy-host/spore subsystem and proposes an HLIR split as future work. Rimbaud et al., DOI 10.1111/eva.12681, provide earlier plant-disease HLIR context but do not contain the source-specific senescence term.

The fitted outbreak simulation code was not available in the inspected article, so the review does not claim that every published numerical trajectory crosses into negative \(R\). It proves that the printed continuum model and displayed Euler update fail positivity for admissible nonnegative data.

Same-model review: passed. Independent audit: not yet performed.
