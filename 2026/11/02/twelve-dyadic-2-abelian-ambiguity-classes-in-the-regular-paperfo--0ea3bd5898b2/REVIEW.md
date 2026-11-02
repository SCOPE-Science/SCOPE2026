# Mathematical review: dyadic 2-Abelian fibres of paperfolding factors

## Correctness — PASS
The claim is for all integers \(k\ge4\), all twelve signatures, and **distinct** length-\(2^k\) factors. Its proof uses the published exact factor-complexity theorem for paperfolding words (Allouche 1992), whose proof and defining hypotheses were examined in the primary PDF, together with a self-contained four-skeleton construction. Every factor is a rotation of a canonical skeleton, and the source theorem forces all \(4N\) labelled rotations to be distinct. The odd-position alternation and even-position recurrence establish the circular bigram counts. Cutting a circular edge gives the explicit endpoint-resolved signatures and class sizes. A separate executable check uses overlapping bigrams and direct factor enumeration at seven dyadic levels. Unrestricted validity rests on the argument and the established dependency, not the finite checks.

## Originality — PASS (qualified)
The closest result, Allouche (1992), counts all distinct factors, but does not state their 2-Abelian multiplicities. The exact counting approach is compatible with but not identical to the canonical-position programme of Allouche and Bousquet-Mélou (1994); its complete primary text was not accessed. Madill and Rampersad (arXiv:1208.2856) study one-letter Abelian complexity of the same word and not this finer endpoint-and-bigram fibre distribution. Parreau et al. (arXiv:1405.3532) consider 2-Abelian complexities of Thue–Morse and period-doubling rather than paperfolding. Semantic research-record and published-literature searches found no statement with the same full parameter domain and cardinality law; that failure alone is not proof of global novelty. The exact 1994 full-text comparison is a residual priority risk, not a claim of thorough exclusion.

## Value — PASS
This class-size spectrum quantifies the loss of distinguishability when a paperfolding factor is represented by local bigram data. The full, endpoint-resolved, all-dyadic-level classification is substantially more informative than merely counting the \(4N\) factors or the number of 2-Abelian classes. Its Toeplitz skeleton/edge-cut interpretation naturally explains the extreme fibres and can guide comparable multiplicity calculations for other automatic sequences. The restriction to dyadic lengths and regular folding instructions is explicit; no downstream general theorem is asserted.

## Limitations
The paperfolding factor-complexity theorem is an explicit published dependency. No assertion is made for non-dyadic lengths, general folding instructions, occurrence-weighted probabilities, or higher-order Abelian classes. Earlier equivalent results under different terminology remain possible, especially in the 1994 canonical-position literature.

Self-review: passed. Independent audit: not yet performed.
