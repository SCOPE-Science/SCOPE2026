# Independent mathematical audit

## correctness

PASS

Map each n-bit word to concatenation of the increasing lists of values tagged 1 then 0. Every nonidentity at-most-one-descent permutation has a unique word; only n+1 prefix-tag words collapse to identity, making total variation error O(n/2^n) and cardinality 2^n-n. The unique descent is FO definable using position adjacency and value decrease, yielding interpretation of tag word in value order; conversely position order is FO from the tag predicate. FO binary word languages have aperiodic deterministic automata; under uniform fair bits each recurrent class of the random-letter transition matrix must be aperiodic (else every letter transition cyclically advances its period classes and contradicts eventual stabilization of word transitions), giving rational finite Markov limits. For any a/b choose b equal-length inner binary words and cross-bifix-free patterns 0^K 1 s_i 1^K, K=d+1; the first occurrence of any pattern is equiprobable among b types via terminal replacement, misses vanish exponentially, and earliest-hit event is FO, giving a/b. Independent checks of 11950 small binary-word and pattern cases passed; proof covers arbitrary denominators and n→∞.

## originality

PASS

Markström–Räty (Oct 15, 2026) prove convergence for every small permutation class, so existence part is PRIOR COVERED. A crucial later primary work (Falgas-Ravry, Markström, Räty, Skerman, arxiv:2610.34328, Oct 25, 2026), fully inspected, proves Theorem 1.4: density in [0,1] for exponential-growth small classes. The one-descent class has |G_n|=2^n-n (exponential), but density does NOT imply exact rationality of every limit or realization of every rational; Theorem 1.2 full spectra is only for polynomial-growth classes and does not apply. Current result exact Q spectrum survives this recent stronger comparison. Earlier layered permutation cross-bifix constructions are methodological precedents. Dedicated one-descent proof in unindexed source remains risk.

## value

PASS

The set of all first-order limit probabilities is a canonical logical invariant of a natural permutation class. New broader 2026 results show convergence and density only; determining all values, excluding irrational limits and exhibiting explicit sentences with every rational limit is a complete meaningful classification, not a mere limit-existence repetition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
