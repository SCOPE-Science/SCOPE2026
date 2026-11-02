# Scientific review

## Correctness — PASS
The unique three-periodic state follows from \(q^3\)-contraction. The proof reduces total runoff to a periodic mass balance, establishes an anchored-state maximum formula, then proves both candidate reversed-order storage sums are at least the ascending sum. Its equality analysis yields the strict interval \((b+qa)/(1-q^2)<C<(c+qb+q^2a)/(1-q^3)\) exactly, including endpoints. All hypotheses and cases of equal depths are included. A standalone standard-library rational checker gives an additional 16,500 exact instances; the proof, not those finite instances, establishes the universal conclusion.

## Originality — PASS within examined material
The closest full text, Bartlett et al. (2015, DOI 10.1098/rspa.2015.0389), derives soil-moisture/runoff probability laws for rainfall jumps and threshold overflow, not a three-cycle permutation comparison. Its relevant main sections and appendices were inspected. Gani and Pyke (1962, DOI 10.1111/j.2517-6161.1962.tb00440.x) treat stochastic ordered dam inputs and first-emptiness probabilities under steady release; only their abstract was available. The checked literature has not been shown to imply the exact iff capacity window, but general queueing rearrangement theorems and inaccessible historical material remain priority risks.

## Value — PASS
With the rainfall total and store parameters fixed, the theorem resolves which orientation of three different equally spaced rainfall events maximizes periodic overflow, and pinpoints the complete capacity band where temporal order matters. Three positions are the smallest cyclic schedule permitting two nonequivalent orders. This supplies a structural hydrological sequencing boundary, not a calibration or prediction claim.

## Limitations and risks
The result is for scalar capped exponential-loss storage and a settled deterministic periodic calendar. It does not extend without proof to unequal gaps, stochastic inputs, nonlinear depletion or distributed hydrology. Historical priority is not independently established; an older closely titled dam paper was abstract-only during comparison. The separate checker is a finite consistency test rather than a formal certification.

Self-review: passed. Independent audit: not yet performed.
