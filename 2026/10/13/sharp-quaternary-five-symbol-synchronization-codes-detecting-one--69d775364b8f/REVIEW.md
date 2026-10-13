# Scientific review: exact quaternary synchronization and substitution detection

## Correctness — PASS

For every admissible four-symbol length-five code, length-one overlap exclusion separates its possible first and last symbols. Reversal and relabeling reduce the problem to two exhaustive candidate sets of \(180\) and \(240\) self-unbordered words. Each has a fully bundled \(32\)-clique cover in the graph of forbidden codeword pairs. Two separately written, executed verifiers reconstruct the candidate sets and validate every graph edge used in the covers. A fully explicit \(32\)-word parity construction is checked directly, giving matching bounds. The argument is finite and exhaustive for the stated domain; it neither extrapolates from sampling nor relies on a solver outcome without a checked certificate.

## Originality — PASS, subject to documented bibliographic risk

Blackburn's non-overlapping-code bounds, Levy–Yaakobi's error-detecting mutually uncorrelated-code framework, and the Stanovnik–Moškon–Mraz length-five unrestricted maximum do not state or logically imply the sharp \(32\)-word Hamming-constrained optimum. A published exact length-five **unrestricted** classification gives \(81\) words over four symbols, not the requested minimum Hamming distance. The constrained Gilbert–Varshamov bounds described by Wang–Fang–Feng also do not visibly give this exact value; however, their full paper was unavailable for complete inspection, so an equivalent hidden result cannot be ruled out. Targeted public literature and mathematical-record searches revealed no complete equivalent classification. The binary-template idea is pre-existing; novelty is confined to sharp attainment, the complete upper certificate, and the strict \(32>27\) single-template separation.

## Value — PASS

A four-symbol alphabet naturally models DNA encodings, and reliable detection of a substitution alongside word-boundary synchronization is an established joint constraint. The exact maximum \(32\) settles a natural small-parameter optimization without adding artificial restrictions. The proof also shows that an extremal design must go beyond any one Blackburn \(I^4J\) template: the best such restricted code has \(27\) words. This is a structural design distinction, not a renamed version of the unrestricted maximum.

## Closest literature and limitations

The closest primary works are Blackburn (2013), Levy–Yaakobi (2018), Stanovnik–Moškon–Mraz (2024), and Wang–Fang–Feng (2025). The result is an exact finite bound for one triple of parameters and does not classify every optimizer, generalize to other distances or lengths, or provide an independent external audit. The complete unavailable full text of the last paper and unindexed numerical coding tables remain residual originality risks.

Self-review: passed. Independent audit: not yet performed.
