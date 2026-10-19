# Review of the cubic ensemble-variance theorem

## Correctness

**PASS.** The proof starts with the single-forbidden-word transfer characteristic equation and obtains a word-uniform expansion of its Perron escape rate. Primitive length-\(q\) word counts and the Fine–Wilf theorem identify all sufficiently short least periods, with a uniform summable second-moment majorant and an explicit long-period remainder. The final mean correction is smaller than the cubic variance. The extracted checker independently tests eigenvalues and correlation roots, plus primitive-period counts, while the written proof handles all cylinder depths.

## Originality

**PASS, with a bounded priority risk.** Georgiou, Dettmann and Altmann (2012) explicitly supply the individual-hole equation and study means; Attarchi and Bunimovich (2020) study averaging inequalities; Cheriyath and Agarwal (2019/2022) study correlation-polynomial escape comparisons. Those mathematical contributions are credited. None of the inspected relevant accessible primary texts states the complete \(h^3\) variance law with primitive-word coefficient, and comparisons against mathematical-result records found no equivalent statement. The distinction is the passage to a uniform second moment over all holes, with a proof that long primitive periods do not create a competing contribution. An unindexed stronger theorem remains possible; this is not a certification of absolute historical priority.

## Mathematical value

**PASS.** For a fixed hole size, individual escape rates differ according to periodicity, but their full-population spread is a natural unresolved statistical observable. The cubic law quantifies its exact leading constant and shows rare short-period holes dominate even while a generic hole has the universal first-order rate. This is a genuinely second-moment dynamical statement, not a renamed mean or routine computational extension.

## Scope and limitations

The base is a fixed integer \(b\ge2\); holes are individually fixed length-\(n\) symbolic cylinders selected uniformly, and the initial dynamics uses Lebesgue probability. The result does not address non-Markov holes, annealed time-resampled holes, or nonuniformly sampled locations. Finite checks corroborate only finite cases. No independent scientific audit has been performed.

Self-review: passed. Independent audit: not yet performed.
