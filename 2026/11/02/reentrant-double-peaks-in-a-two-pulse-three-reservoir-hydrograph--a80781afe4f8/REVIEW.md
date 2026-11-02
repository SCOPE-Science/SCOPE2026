# Scientific review: two-pulse three-reservoir hydrograph

## Correctness — PASS

The domain is all positive separations and pulse-volume ratios, and local maxima are distinguished from stationary shoulders. The complete derivative quadratic is reconstructed in the proof; its discriminant, vertex sign, and positive-root geometry give the exact two-peak boundary. Cases at and below a two-time-unit separation and equality at the double root are treated separately. Logarithmic differentiation of the explicit boundary proves strict increase, decrease, and all reentrant intervals. `verify_hydrograph.py`, extracted from the new scientific package, passed 12,732 assertions. Numerical tests support but do not replace these analytic arguments. Residual risk: the physical routing assumptions may not fit measured catchments; this is outside the mathematical theorem.

## Originality — PASS, provisional

The primary hydrological comparison is Muneepeerakul et al. (2010), which derives probability distribution and autocorrelation characteristics of streamflow represented by gamma pulses, not the exact two-pulse temporal-peak phase diagram. Yang et al. (2015) analyze double-peak responses using superposed advection–diffusion kernels with different flow pathways, not delayed identical Erlang-3 input responses. The highly relevant Došlá (2009) paper supplies general implicit mixture-modality criteria and explicit gamma mixtures with common origin and differing shape/rate. In particular, its general theorem is a broader conceptual predecessor and does not, in its explicit gamma propositions, give this positive-shift, fixed-ratio reentrant delay law. The exact specialized threshold and its nonmonotone lag geometry require the separate derivative reduction given here. Targeted external and mathematical-record searches found no explicit earlier occurrence of the final theorem. General implicit coverage and unexamined publications remain genuine historical-priority risks; this is not an independence or uniqueness certificate.

## Value — PASS

A bimodal hydrograph is often interpreted as evidence of multiple runoff pathways. The theorem supplies a sharp diagnostic counterexample: *identical* routing kernels can yield two peaks solely from temporal rainfall separation, and varying that separation may remove then restore the second peak without changing storm-volume ratio. The full parameter phase diagram is exact, not a single numerical case or routine parameter fit. It gives a usable criterion for idealized hydrograph model selection and a structural warning against inferring distinct pathways from peak counts alone. Limitations: instantaneous pulses, linear superposition, one response shape, no finite storm duration or physical reachability claim.

## Closest literature and residual limitations

1. Muneepeerakul et al., *Water Resources Research* (2010), DOI 10.1029/2010WR009286: full HTML article inspected, especially model definition, overlapping pulses, derived statistics, applications and conclusion.
2. Yang, Endreny and Nowak, *Journal of Hydrologic Engineering* (2015), DOI 10.1061/(ASCE)HE.1943-5584.0001225: complete five-page lawful PDF text and equations inspected; distinct advection–diffusion kernel model and one-storm/two-pathway interpretation.
3. Došlá, *Kybernetika* (2009), https://dml.cz/handle/10338.dmlcz/140075: open-access fifteen-page PDF inspected in the relevant sections, especially Theorems 1–3 and Propositions 6–8. General mixture principles are relevant and may yield alternative derivations.

Self-review: passed. Independent audit: not yet performed.
