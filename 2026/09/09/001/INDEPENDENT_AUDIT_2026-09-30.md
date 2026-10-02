# Independent audit — SCOPE-20260909-001

Audit date (UTC): 2026-09-30 (UTC)

## Final claim

For the overpartition function S(n) counting overpartitions with no part divisible by 3, S(n) is even for n at least 1 and, for odd m, S(m) is congruent modulo 4 to twice the number of odd divisors of m not divisible by 3. Equivalently, S(m) is 2 modulo 4 exactly when the 3-free part of m is a square. A commuting pair of overline-bit involutions gives a direct four-orbit proof away from the single-value overpartitions.

## Correctness

**PASS** — The formal-product proof was reconstructed independently. Dividing G(q) by G(q^2) leaves the product over odd parts not divisible by 3; modulo 4, each factor is 1 plus twice its positive geometric tail and every product of two such tails vanishes, so the coefficient is twice the relevant divisor count. A fixed-point-free overline flip proves evenness, and convolution gives the odd congruence. The V4 action on nonrectangular overpartitions has four distinct orbit points, while single-value overpartitions number exactly twice the same divisor count. These are all-n arguments; the N=120 computation is only corroboration.

## Originality

**PASS** — Sang-Shi's full text was inspected and does contain mod-4 dissection families that cover the S(4n+2) subcase, which is therefore not novel. Searches did not find the stronger all-odd divisor-count congruence, the square criterion, or the V4 orbit witness for this exact object. published-results index returned the present record as the exact match.

### Originality checks

#### Equivalent formulations

Searches: published-results semantic search for singular overpartitions mod 4 square criterion; Web search for Cbar_3,1 and overpartitions with parts not divisible by 3 modulo 4.

Evidence: The published-results index returned this record as the exact semantic match.; Searches found prior divisibility families but not the divisor-parity/square dichotomy or V4 witness..

Reasoning: The product identity, divisor-count formulation, square formulation, and orbit formulation were all compared as equivalent statements.

#### Broader coverage

Searches: Sang-Shi arXiv:1712.08930 full text; Chen-Hirschhorn-Sellers arXiv:1405.3626.

Evidence: Sang-Shi gives mod-4 dissection congruences including the even-progression subcase.; Chen-Hirschhorn-Sellers concerns mod-3 families, not the all-odd mod-4 dichotomy..

Reasoning: The located broader congruence families do not imply the exact all-odd divisor-count classification or combinatorial witness.

#### Exact database or table

Searches: Exact coefficient/congruence searches for odd m and 3-free square criterion.

Evidence: No database or table encoding the all-odd mod-4 classification was found..

Reasoning: Finite coefficient tables would not themselves prove the all-n statement.

#### Claim versus prior implication

Searches: Sang-Shi mod-4 formulas specialized to the k=3 singular-overpartition object.

Evidence: The known S(4n+2) congruence is a genuine special case and is explicitly excluded from novelty.; The prior formulas located do not yield the stated odd square iff criterion or V4 orbit decomposition..

Reasoning: The final claim contains a stronger odd classification and witness not implied by the prior-covered even progression.

## Value

**PASS** — The result gives a clean all-n classification on a natural singular-overpartition function together with a structural combinatorial explanation, not just isolated congruence checks. The square criterion and orbit decomposition are independently useful refinements even though one even-progressions corollary is prior-covered.

## Source inspections

- **Arithmetic properties / mod-4 dissections for Rogers-Ramanujan-Gordon type overpartitions** — https://arxiv.org/abs/1712.08930. Trigger: Direct prior-overlap check and object identification. Material read: Full text around the object identification and final mod-4 congruence families. Method: Primary full-text comparison. Assessment: Covers the even-progression subcase but not the full odd square criterion or V4 witness found in searches. Evidence: The paper identifies the relevant singular-overpartition object and states mod-4 progressions.
- **Package formal-series and orbit verifiers** — artifacts/series.py; artifacts/crank.py; artifacts/series_N120.json. Trigger: Correctness. Material read: Complete source and stored coefficient data. Method: Independent proof reconstruction plus exact coefficient/orbit checks. Assessment: Consistent with the all-n proof. Evidence: Coefficient identities hold through N=120 and orbit assertions through the tested odd sizes; the proof itself is symbolic.
- **Arithmetic properties of Andrews' singular overpartitions** — https://arxiv.org/abs/1405.3626. Trigger: Prior congruence comparison. Material read: Abstract/record and cited mod-3 scope. Method: Literature comparison. Assessment: Different modulus and does not imply the odd mod-4 classification. Evidence: Its principal families are modulo 3.

## Residual risks

- Best-of-knowledge originality is not an exhaustive literature proof.
- The exact equation numbering of the Sang-Shi overlap varies by version; the substantive progression overlap is what matters.

## Disposition

PASSED
