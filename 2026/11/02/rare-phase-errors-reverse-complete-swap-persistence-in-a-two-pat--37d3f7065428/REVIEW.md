# Scientific review: rare phase errors and two-patch dispersal

## Correctness — PASS

The hypotheses identify the environmental Markov chain and fix the order of reproduction then migration. The fixed-state threshold follows from the sign of the explicit two-by-two characteristic determinant and the fact that the non-Perron eigenvalue lies below one. The period-two threshold follows from the factored two-period determinant and the product determinant bound. The all-or-nothing migration exponent follows from ergodic frequencies for an environmental state chain or, at complete swapping, the two-state match/mismatch chain. The positive interior regime follows from strictly positive left Perron weights, exact switch identities, and the law of large numbers for switch counts. The rational witness uses componentwise matrix inequalities checked by `check.py`. The proof does not mistake finite tests for almost-sure or all-parameter proofs.

## Originality — PASS within inspected sources, with residual historical risk

Schreiber (2010), DOI 10.1098/rspb.2009.2006, supplies the general stochastic metapopulation matrix model and correlation-dependent growth context, but its examined exact formula is for complete pooled mixing and its partial-mixing expansion is perturbative. Schreiber and Li (2011), DOI 10.1080/17513758.2010.525667, derive spectral/evolutionary conclusions for periodic environments; their Theorem A1 offers broader period-two spectral monotonicity, so monotonicity of the deterministic growth threshold is not claimed as an independent advance. Williams and Hastings (2011), DOI 10.1098/rspb.2010.2074, review switching-induced persistence and stochastic game interpretations; those themes are credited as prior knowledge. The present, more specific joint result is the sharp complete-swap timing singularity together with positive interior dispersal under arbitrarily small but positive phase error, both frozen systems subcritical, and an exact positive certificate at a nontrivial Markov switch probability. These statements were not identified in the material inspected. Historical priority is provisional: other specialized or older random matrix treatments may contain a dominating theorem, and the Williams–Hastings article was available mainly through indexed full-text sections rather than a complete directly accessible copy.

## Value — PASS

The all-or-nothing movement boundary is a mathematically natural control parameter, not an arbitrarily selected finite slice. Its almost-sure growth sign flips discontinuously when strictly imperfect season alternation replaces perfect alternation, whereas strictly partial migration remains robust. The explicit two-patch rational example at an appreciable phase-error rate demonstrates that this distinction changes viability even though the two frozen environments are individually declining. This separates a fragile synchronization strategy from robust ecological rescue, a useful diagnostic for interpreting temporal correlations in metapopulation models.

## Scope and limitations

This is a linear rare-population model with two patches, fixed exchange fraction, two opposing environmental fitness profiles, and exogenous symmetric Markov switching. It is not a nonlinear bounded-population persistence theorem and does not estimate demographic extinction probabilities or determine the exact noisy-growth transition for every dispersal fraction. The all-parameter conclusions rely on the analytical proof, not numerical experiments. No external independent audit has been performed.

Self-review: passed. Independent audit: not yet performed.
