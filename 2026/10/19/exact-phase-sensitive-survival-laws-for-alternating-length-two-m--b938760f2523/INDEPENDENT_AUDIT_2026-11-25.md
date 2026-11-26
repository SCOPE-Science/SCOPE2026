# Independent mathematical audit

## correctness

PASS

On the repaired statement, n pair tests use n+1 i.i.d. base-k digits including the dangling final digit. Writing A=J-E_pq and B=J-E_rs, the even count is 1^T(AB)^m1. On (1,e_p), AB has trace k^2-2+de and determinant (kd-1)(ke-1). Counts k and k^3-2k+d follow from zero tests and inclusion-exclusion of the two events; joint occurrence is one word when q=r and none otherwise. The order-two recurrence gives all four rational numerators and denominators. The adjacent differences are k^2 z^2/(D_0 D_M), z/D_M and (k-1)^2 z^2/(D_M D_H). The reciprocals have strictly positive coefficients (positive roots for D_0,D_H; positive recursion for D_M), giving the onset and strict comparisons. The larger mid root satisfies P_H(lambda_M)=k(k-1)-lambda_M<0 and exceeds the largest D_0 root. Leading poles do not cancel (in the high case the positive leading root exceeds (k-1)/k); all are simple except the double binary D_0 root. Each next digit has at least k-1 allowable choices, giving the same rate on odd horizons by a multiplicative bound, not the same prefactor. At odd horizons, word reversal preserves the observation parity of each tested pair and swaps the overlap bits when the two forbidden pairs are themselves reversed. The mixed word counterexample and prefactor ratio were independently checked: python3 /workspace/branches/independent_checks.py 1. The original checker was inspected and not executed. Configuration frequencies follow from the two independent digit equalities, and the argument includes identical holes and k=2.

## originality

PASS

The supported distinction from the preceding moving-hole literature is the strict all-base coefficientwise survival hierarchy, including the starting-phase effect even when rates coincide, and the exact critical binary correction beyond the b>=3 theory. Do not credit the standard count-by-transfer-product or the b>=3 periodic-pattern growth framework as original. Much of the narrower result is now a direct corollary of a later-indexed exact formula; the binary alternation law is also separately present in later indexed records. These are real coverage relations, not independent novelty for the overlapping formulas or evidence that they preceded the frozen result. In the inspected earlier sources the explicit phase hierarchy and all-base correction were not established.

## value

PASS

Finite survival has a strict phase dependence invisible in the all-time escape exponent; it matters already after two tests and the complete four-class ordering starts at four tests, on even horizons. The binary critical class also exhibits a genuine polynomial correction where a simple-root law would mislead. This gives usable information about moving-hole experiments beyond the choice of transfer representation or numerical examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
