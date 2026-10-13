# Self-review

## Correctness
**PASS.** For a balanced protective table \((a,b)\), the formulas
\[
RR=\frac ab
\]
and
\[
OR=\frac{a(n-b)}{b(n-a)}
\]
are exact. Pairwise ranking signs reduce to two integer numerators, giving a necessary-and-sufficient strict-reversal test. The complete protective domains for \(n\le5\) are exhausted exactly: no strict reversal occurs through \(n=4\), and exactly one occurs at \(n=5\). The infinite family follows from the identity
\[
4(n-3)(n-1)-3(n-2)^2=n(n-4).
\]
The packaged verifier independently checks rational and cross-multiplied comparisons and returns `VERIFY_OK`.

Risk: the minimality theorem is specific to equal arm sizes and positive cells.

## Originality
**PASS.** The inspected epidemiologic literature explicitly establishes that odds ratios and risk ratios diverge as baseline risk rises and gives the exact baseline-risk conversion. That prior fact is not claimed as new. The accepted claim is the sharp finite cross-study ordering result: first weak-order mismatch at \(n=4\), first strict reversal at \(n=5\), uniqueness of the protective \(n=5\) pair, and an all-\(n\) continuation family. Semantic-result searches and exact-table web searches did not locate this statement.

Risk: because the result is an elementary consequence of standard formulas, an unindexed teaching example or software test could contain the witness. No checked source stated the sharp minimum or uniqueness theorem.

## Value
**PASS.** Risk ratios and odds ratios are routinely used to compare binary outcomes, and the literature warns that their relationship depends on baseline risk. The result turns that warning into the smallest exact benchmark where two otherwise comparable balanced trials receive opposite efficacy rankings. The persistent family demonstrates that the ranking conflict is structural and provides a compact regression test for clinical-statistics software and educational examples.

Self-review: passed. Independent audit: not yet performed.
