# Independent mathematical audit

## correctness

PASS

The absence count of a species of size a is binomial(N−a,k) among the binomial(N,k) equally likely samples. Thus scaling expected richness by the positive binomial(N,k) preserves all comparison signs, including zeros. The largest-part recursion in the frozen proof is exhaustive by induction. Independently, python3 /workspace/branches/independent_checks.py 5 generates every composition of N by cutting internal gaps, sorts and deduplicates to obtain the partitions, then counts samples containing a species by the first selected individual from it when its a individuals are placed first: sum over j=0,…,a−1 of binomial(N−j−1,k−1). It checks every unordered pair for each N from 1 to 16 and discards ties before counting sign switches, equivalent to testing for an alternating nonzero subsequence of length three. The partition counts are 1,2,3,5,7,11,15,22,30,42,56,77,101,135,176,231. Counts of qualifying pairs are zero through 15 and exactly two among 26,565 at 16. The recomputation returns the two displayed numerator vectors entry for entry. The first has positive signs at k=2,3 and 11–16, negative signs at 4–10; the second is positive at 2–4 and 11–16, negative at 5–10. Both tie at k=1. The finite cutoff concerns equal total integer census and uniform sampling without replacement at integer k, with no restriction that species counts be equal within a pair.

## originality

PASS

Best-of-knowledge pass only for the sharp finite equal-census cutoff and the complete classification of its first-attaining pairs. Neither the hypergeometric expectation nor the possibility of multiple richness crossings is claimed new. Statement-level comparison of the strongest accessible catalogue matches gives distinct results; access to the closest older primary texts was incomplete, so this is not an unconditional priority finding.

## value

PASS

Richness ranking at a standardized sampling effort is a natural comparison. The calculation identifies precisely the first equal census for which agreement at small sample sizes and at the full census can conceal an opposing intermediate ranking, and the two complete extremal pairs make the mechanism concrete (four doubletons against four singletons, with different large-species counts). That is a meaningful sharp boundary for a known warning, not a claim about frequency or statistical significance in field data.

The dated certificate retains the supplied scientific assessment, sources and limitations.
