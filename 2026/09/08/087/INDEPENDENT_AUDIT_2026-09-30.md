# Independent audit — SCOPE-20260908-087

Audit date (UTC): 2026-09-30 (UTC)

## Final claim

The complete labeled permanent distribution on 7 by 7 binary matrices with every row and column sum equal to 3 is 24:14,439,600; 25:6,350,400; 26:25,401,600; 27:16,934,400; 30:3,175,200; 31:1,814,400; 32:793,800; 54:29,400. Hence the minimum is 24; the displayed minimizer has permanent 24 and row/column-permutation stabilizer order 16.

## Correctness

**PASS** — The actual exhaustive C source was inspected and independently recompiled/re-run. Fixing the first row by column symmetry produced exactly 1,969,680 matrices, hence 68,938,800 labeled matrices after the factor 35, with the full claimed histogram and minimum 24. The witness permanent was separately reconstructed by direct permutation expansion and Ryser inclusion-exclusion; margins and the Schrijver ratio are exact.

## Originality

**PASS** — The minimum value itself has substantial prior-coverage risk: a secondary literature discussion reports that Ryser's symmetric-design minimizer conjecture was computationally verified by Wanless through order 12, which would cover the n=7,k=3 minimum because the Fano incidence matrix has permanent 24. However, that does not imply the complete eight-value labeled histogram or the stated witness-orbit data. published-results index and targeted literature searches found no prior source containing the full D(7,3) distribution.

### Originality checks

#### Equivalent formulations

Searches: published-results semantic semantic search: D(7,3), minimum permanent 24, full distribution; Web search: exact D(7,3) permanent minimum/distribution; Wanless thesis summary and Ryser-minimizer discussion.

Evidence: The published-results index returned this record as the only exact semantic match.; OEIS A001501 supplies the labeled count 68,938,800 but not permanent values.; A literature discussion reports prior verification of Ryser's minimizer conjecture through n=12, so the minimum 24 is not treated as novel..

Reasoning: The final audited claim is stronger than the minimum: it gives the complete labeled permanent distribution. The prior minimizer result does not determine that histogram.

#### Broader coverage

Searches: Schrijver 1998 regular bipartite perfect-matching lower bound; Wanless permanents/matchings thesis summary; Ryser permanent-minimizer literature.

Evidence: Schrijver gives a general lower bound, far below 24 at this parameter.; Prior minimizer work can cover which value is minimal but does not provide counts at every permanent value..

Reasoning: No broader theorem located implies the exact eight-bin distribution.

#### Exact database or table

Searches: OEIS A001501; published-results semantic exact-count and histogram search.

Evidence: OEIS records the number of 7 by 7 binary matrices with line sum 3, not their permanent histogram.; No independent exact histogram table was found..

Reasoning: The known count database is insufficient to recover the audited distribution.

#### Claim versus prior implication

Searches: Ryser minimizer implication at n=7,k=3; Fano-plane incidence permanent.

Evidence: A Fano-plane incidence matrix has permanent 24, so a verified Ryser minimizer statement would imply the minimum 24.; It does not imply the distribution masses or gaps..

Reasoning: Prior work partially implies one component but not the stronger complete-distribution final claim.

## Value

**PASS** — The full distribution is a natural complete classification over the standard fixed-margin class D(7,3), not an arbitrary slice. It supplies exact extremal and distributional data for a classical permanent problem even though the minimum alone may be prior-covered.

## Source inspections

- **Package RESULT and exhaustive enumerator** — RESULT.md; artifacts/enum.c; artifacts/verify.py. Trigger: Core correctness evidence. Material read: Complete RESULT.md and both source files. Method: Source inspection plus fresh compile/run and independent permanent calculation. Assessment: Supports the complete finite census and witness checks. Evidence: Fresh enumeration reproduced subtotal 1,969,680, total 68,938,800 and every histogram bin exactly.
- **OEIS A001501** — https://oeis.org/A001501. Trigger: Exact class-size cross-check. Material read: Sequence entry relevant to 7 by 7 line-sum-3 binary matrices. Method: Database comparison. Assessment: Supports the total class size only, not the permanent distribution. Evidence: The total 68,938,800 agrees.
- **Counting 1-Factors in Regular Bipartite Graphs** — https://doi.org/10.1006/jctb.1997.1798. Trigger: Broader lower-bound comparison. Material read: Statement of the general regular-bipartite lower bound as cited in the package. Method: Theorem-level comparison. Assessment: Does not imply the exact finite histogram. Evidence: At k=3,n=7 the bound is 16384/2187, not an exact minimum or distribution.
- **Permanents, matchings and Latin rectangles** — https://doi.org/10.1017/S0004972700032731. Trigger: Prior permanent-classification comparison. Material read: Published two-page thesis summary. Method: Full summary read. Assessment: Discusses permanent extremal problems but does not state the D(7,3) distribution. Evidence: No fixed D(7,3) histogram appears in the summary.

## Residual risks

- The full histogram is software-assisted; independent rerun reduces but does not eliminate implementation risk.
- The minimum component is likely not novel; originality is assessed on the stronger complete-distribution claim.
- An obscure earlier exhaustive D(7,3) histogram could exist outside the searched sources.

## Disposition

PASSED
