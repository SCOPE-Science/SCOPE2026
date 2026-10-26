# Scientific review: A parity-repaired Poisson crossover for competitive monomer–dimer adsorption on complete graphs

## Correctness — PASS

The exact vacancy chain has singleton probability \(q_k=2\varepsilon/(k-1+2\varepsilon)\). Every pair of adjacent vacancy-count states has a first visit using a fresh uniform, giving independent comparison indicators with probabilities \(\varepsilon/j\). A direct sum of first-visit mismatches, double visits, boundary exceptions and Le Cam errors proves the finite-size \(5\varepsilon\) bound. Deterministic parity repair yields the final law; harmonic asymptotics prove the stated window and the Poisson central limit regime. The standalone program returned 294 successful finite exact or numerical assertions, supplementary to the proof.

## Originality — PASS relative to inspected literature

Cadilhe and Privman (arxiv:cond-mat/0311190) consider mixed kinetic adsorption on a fixed-connectivity Bethe lattice; Pippenger (doi:10.1137/0402034) considers random greedy graph adsorption, including edge-only occupation; and Chen (arxiv:1506.08484) considers complete-graph equilibrium Gibbs matching fluctuations. The latter primary PDF was inspected at the model and theorem level, including whole-document searches for kinetic terminology. None of the inspected statements implies the weak-rate terminal law on the complete graph. Searches for rare-rate competition, parity-alias Poisson laws and stronger matching coverage found no evaluated duplicate. Complete texts of several specialist papers were inaccessible; any broader hidden result remains an originality risk.

## Mathematical value — PASS

The motivated observable is the number of irreversibly deposited monomers, not a contrived sub-count. The complete graph supplies a mean-field benchmark for competing single and pair adsorption; the integrated monomer hazard is logarithmic and becomes critical at \(\varepsilon\asymp(\log n)^{-1}\). The limit distinguishes a parity-*repaired* Poisson count from a parity-*conditioned* one, including different zero/one-monomer probabilities and even–odd mean gaps. An explicit uniform total-variation estimate extends the conclusion through the entire weak-rate range.

## Limitations and residual uncertainty

The theorem is restricted to complete graphs, uniform irreversible rates, and \(0<\varepsilon\le1/4\). Available primary full texts were not exhaustive, and absolute historical novelty is not certified. Finite tests do not certify infinite-size claims; the proof provides those arguments. No independent scientific audit was conducted.

Self-review: passed. Independent audit: not yet performed.
