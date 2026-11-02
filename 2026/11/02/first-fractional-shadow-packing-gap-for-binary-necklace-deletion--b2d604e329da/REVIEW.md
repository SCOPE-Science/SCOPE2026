# Scientific review of the finite necklace-deletion packing theorem

## Correctness

**PASS.** The claim is fully finite and every stated quantifier is checked by the standalone exact-rational verifier. The nine-word length-nine witness has disjoint deletion shadows. The \(59/6\)-weight cover of 19 genuine conflict cliques proves no ten-word code can exist. Rational feasible solutions on opposite sides of the shadow packing LP prove its exact length-nine optimum \(41/4\), and code/dual pairs verify equality for all positive lengths below nine. The empty-necklace boundary is included. Risk: executable verification must be rerun if either standalone certificate file changes; no behavior beyond nine is asserted.

## Originality

**PASS, with historical-priority qualification.** In Sloane (2002), deletion-correcting codes are linear words with fixed indices; necklace enumerations arise from shift registers rather than unrooted deletion outputs. Abdel-Ghaffar–Ferreira–Cheng (2010) treats cyclic algebraic codes, their expurgations and **rooted** deletion decoding; its cyclic-shift obstruction is not an optimality statement for rotation-class messages. Adamson–Deligkas–Gusev–Potapov (2020) studies an overlap-distance \(k\)-centre objective rather than deletion-shadow packing. Published finite deletion-code comparisons concern other channels. No inspected source proves the identical length-nine integral/fractional pair or its first-gap property. Risk: unindexed or older necklace-specific packing literature may contain an equivalent fact; novelty has not been independently established.

## Value

**PASS.** Removing the distinguished origin is a natural synchronization model for circular strings. Unlike ordinary deletion codes, both transmitted symbols and deletion outputs are rotation classes. The first exact obstruction to the natural output-capacity LP is a motivated finite cutoff, not merely another code-size table entry: it shows that local shadow capacities admit total fractional mass \(41/4\) while all valid integral codebooks have at most nine messages. The distinct conflict-clique certificate explains how additional pairwise obstructions close the gap. No downstream infinite theorem is claimed.

## Sources and limitations

Primary inspected sources: Sloane, *On Single-Deletion-Correcting Codes* (arXiv:math/0207197, 2002); Abdel-Ghaffar–Ferreira–Cheng, *Correcting Deletions Using Linear and Cyclic Codes* (IEEE TIT, 2010); Adamson et al., *The K-Centre Problem for Necklaces* (arXiv:2005.10095, 2020). Proofs of broader priority, larger lengths and other alphabets are not offered. The available published research-record comparison did not identify a directly covering statement, but absence from an index is not novelty proof.

Self-review: passed. Independent audit: not yet performed.
