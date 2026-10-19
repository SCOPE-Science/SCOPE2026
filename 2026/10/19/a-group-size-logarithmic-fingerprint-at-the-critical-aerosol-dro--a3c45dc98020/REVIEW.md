# Self-review

## Correctness — PASS

For every fixed integer \(s\ge3\) and strictly interior initial data, a forward-invariant unit square and a strict LaSalle argument give global convergence to extinction. An explicit reciprocal-Lyapunov lower bound permits an elementary exponentially stable forcing lemma. Applied successively to the transverse displacement and its cubic residual, that lemma establishes the *actual* trajectory expansion \(d=-2s^2x^3/9+O(x^4)\), not merely an unspecified formal center-manifold series. Integrating \(\dot x=-x^2-(s^2/9)x^3+O(x^4)\) proves existence of the finite remainder limit and all claimed ratios. Symbolic identities and finite numerical examples are independently replayable via `verify.py`; the long-time proof is analytical.

## Originality — PASS, with residual risk

The motivating primary source [1] was inspected in its full-text model, threshold, equality-adjacent theorems, proofs, and hyperedge-size analysis. It introduces this ODE and establishes results on either side of the critical reproduction number, but does not state the critical reciprocal-prevalence logarithmic law. Jhun–Jo–Kahng [2] studies a different direct-simplicial SIS system with no contaminated-environment dynamics; its critical exponents do not imply the specific \(s^2/9\) coefficient. Searches across available mathematical records for the source, equivalent critical relaxation laws, reciprocal prevalence, arctangent saturation and group-size normalizations found no same-object implication. Classical nonlinear reductions are acknowledged; a more general unlocated coupled-infection theorem may potentially subsume this specialization. An unsuccessful search is not proof of uniqueness.

## Mathematical value — PASS

A natural scale normalization \(\sigma=1/s\) keeps both infection channels and the entire disease-free linearization fixed as hyperedge size changes. The exact second-order extinction fingerprint identifies a mathematically meaningful variable not discernible from reproduction threshold or even leading critical prevalence. This provides a motivated boundary for threshold-only comparisons of aerosol and droplet hazards, rather than an arbitrary numerical invariant.

## Scientific scope and risks

All results are for a deterministic, homogeneous two-variable mean-field ODE at a fixed critical family. There is no claim for a finite stochastic process, arbitrary heterogeneous mixing, an independent review, or inferred practical identifiability in noisy observations. Earlier general critical epidemic asymptotic techniques might imply the reduced scalar behavior; the coefficient and the cross-group comparison are the contribution asserted.

Self-review: passed. Independent audit: not yet performed.

## References

[1] Nguyen–Porter (2026), arXiv:2601.03563v1, https://arxiv.org/pdf/2601.03563.

[2] Jhun–Jo–Kahng (2019), arXiv:1910.00375, https://arxiv.org/pdf/1910.00375.
