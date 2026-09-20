# Same-model review

Same-model review: passed. Independent audit: not yet performed.

## Correctness

**PASS.** The two claims use different forms of evidence.

For the period-seven family, the proof is algebraic once the finite-field identity is checked. The verifier confirms that the stated degree-21 polynomial is irreducible, that the stated element has order 16513, and that the five displayed exponents annihilate both the first and third BCH syndromes. The divisibility argument M | N_s for 7 | s and 21 ∤ s is elementary modulo 21, and the BCH bound supplies the matching lower bound 5.

For s=6, the verifier confirms the field model and a weight-six codeword. The weight-five exclusion is exhaustive after a justified reduction: cyclicity normalizes one support exponent to zero, and every possible remaining four-element support has a partition into two pairs. The program enumerates every unordered pair of nonzero exponents and checks every matching complementary syndrome subject to disjointness. Thus it cannot miss a weight-five support. The BCH bound excludes smaller weights. Cyclotomic-coset sizes independently give the stated dimensions.

Potential failure modes were checked explicitly: support exponents in each exhibited word are distinct; the two defining cosets are disjoint in the s=6 and s=7 cases; the field elements used have the required exact multiplicative orders rather than merely orders dividing them; and the period-seven lifting preserves five distinct cyclic coordinates.

## Originality

**PASS, to the best of our knowledge.** The most relevant recent source is Wang--He--Yi--Zheng, arXiv:2609.00532 (1 September 2026), which studies exactly the family C_(2,N,5,1) with N=2^(2s)+2^s+1. It proves distance five for several congruence/divisibility classes by explicit low-weight relations and records counterexamples to a universal distance-five statement. The period-seven condition here is not one of the sufficient conditions reported there, and s=6 is not covered by those conditions.

Originality searches used the exact lengths 4161 and 16513, the exact parameter strings [4161,4125,6] and [16513,16471,5], the code notation C_(2,4161,5,1) / C_(2,16513,5,1), combinations with “binary BCH” and “minimum distance”, and the explicit period-seven support exponents. No prior source stating either result was located. Repository searches by the same numerical parameters and BCH terminology found no prior SCOPE record.

The numerical lengths themselves occur in unrelated finite-geometry/LDPC literature, so an occurrence of 4161 or 16513 alone is not evidence of coverage of this narrow-sense BCH result. No specific inaccessible paper was identified as especially likely to contain these exact claims. Residual risk remains from older computational BCH tables, theses, books, or non-indexed catalogues; accordingly no certainty of first discovery is claimed.

The period-seven proof method is structurally related to the small-divisor relation method used by Wang--He--Yi--Zheng. The originality claim is therefore the new order-16513 relation and the resulting sufficient class, not the generic strategy of obtaining BCH codewords from subgroup relations.

## Value

**PASS.** Exact minimum distances of BCH families are a central coding-theoretic parameter problem. The s=6 result identifies a concrete exceptional distance-six case beyond the source paper's displayed small exceptions, while the period-seven certificate expands the known exact distance-five regime by an infinite arithmetic class and gives the explicit [16513,16471,5] instance. Both statements are compact, independently reusable, and accompanied by exact verification.

## Access and residual uncertainty

The current arXiv record and searchable public literature were inspected. No particular inaccessible paper was found whose title or abstract strongly suggested coverage of the exact claims. The residual originality uncertainty is therefore generic rather than tied to a known inaccessible source: historical code tables and computational catalogues may be incompletely indexed.

No independent validation is asserted.
