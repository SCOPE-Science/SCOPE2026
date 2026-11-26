# Independent mathematical audit

## correctness

PASS

The primitive domain is exhausted by choosing six different interior entries and testing gcd with L. Each legal four-term sum is a sum of two disjoint two-subsets, and each such pair-of-pairs sum uses exactly four distinct entries. The independent bit-mask and disjoint-pair replay in /workspace/branches/9018dc32-5335-4289-8faa-84f4e113564f/independent_check.py gives minimum values (17,18,19,20,21,22,23,24,25,25) and minimizer counts (1,2,3,4,5,6,7,8,12,3) for L=7 through 16. At L=16 there are 5005 endpoint-normalized candidates, of which seven are all-even and 4998 primitive; the first two histogram entries are 25:3 and 26:10. The exact three sets in complete_run.txt there agree with the frozen list, and opposite paired entries sum to 16 in each set. For L≤15, the stated interval-union example supplies the matching elementary upper bound; the exhaustive search covers every possible lower diameter since no eight distinct integers fit in diameter <7. In the literature paragraph, 10+min(L,16) is a weaker consequence at k≥9 and the formal k=8 specialization, not Wang's exact right-hand side for k>8. This distinction does not change the theorem or the threshold interpretation.

## originality

PASS

Credit Wang for the failure witness A1 at L=16. The distinct claim is the minimum profile proving that no smaller feasible diameter fails, the matching lower bound of 25 at the known example's diameter, and the complete equality class including the two other sets. The checked sources do not supply or imply these parts at k=8.

## value

PASS

The finite cutoff is not chosen arbitrarily: it tests where a published cardinality threshold first becomes necessary in the first excluded size. The motivating example shows failure at one diameter but does not show that it is first, that its value is minimal, or how representative it is. The exact answer enumerates three distinct endpoint-reflection classes rather than reporting another isolated counterexample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
