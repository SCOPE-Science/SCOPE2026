# Scientific review

## Correctness

**PASS.** The adjacent-one classification is proved from binary carry behavior, including the initial \(j=0\) case. Two initial \(110\) arches consume four ones; all subsequent completed arches consume one, with exactly the identified one-symbol exceptional residue. The general greedy-arch universality lemma has both directions proved, and the four-state count gives the Fibonacci specialization. Independent code checks prefix lengths through \(65{,}536\) but does not substitute for the proof.

## Originality

**PASS, with historical limitations.** Searches concerned Baum–Sweet, prefix universality, Simon subsequences, greedy arches, and Fibonacci dyadic counts. The closest broad result is the general arch/absent-subsequence framework of Kosche et al. The full relevant sections of that work and Waldschmidt's Baum–Sweet description were inspected; neither states the sparse-exception prefix formula in those portions. Published research records on general binary subsequence-universality distributions give a different aggregate invariant and do not imply the particular all-prefix formula without a further Baum–Sweet-specific argument. Priority assessment is not exhaustive; the original 1976 paper could not be read in full.

## Value

**PASS.** This is an exact all-prefix classification of a natural subsequence-capacity invariant for a classical automatic word. The exceptional indices identify a mathematically sharp synchronization failure at powers of four, and the dyadic specialization ties scattered-subsequence coverage to Fibonacci growth. The result is not a finite numerical cutoff, a routine normalization check, or merely a bound.

## Scientific limitations

Only zero-indexed initial prefixes and the fixed binary alphabet are covered; general factor intervals and complete absent languages are not. Source access and independent-priority checks remain incomplete. The mathematical proof is self-contained under the given definitions.

Self-review: passed. Independent audit: not yet performed.
