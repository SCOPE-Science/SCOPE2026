# Self-review

## Correctness
**PASS.** The binary kappa formula is derived directly from Cohen's definition and independently reduced to an exact rational expression. The finite domain is explicit and exhaustive: fixed \(N\), fixed reference-positive count \(P\), every cell positive, and \(\kappa>0\). Complete exact enumeration gives no reversal through \(N=9\) and one class-label-normalized reversal at \(N=10\). The displayed infinite family has closed formulas whose inequality reduces to \(3N>0\). The packaged verifier returns `VERIFY_OK`.

Risk: the cutoff depends on the stated positivity restrictions; removing them permits smaller but more degenerate discrepancies.

## Originality
**PASS.** Cohen's original paper owns the chance-corrected agreement formula, and Cicchetti–Feinstein directly analyze high-agreement/low-kappa paradoxes caused by marginal imbalance. Those sources establish the qualitative phenomenon, not the sharp nondegenerate finite boundary under fixed prevalence. Searches by aliases, exact tables, positive-kappa language, smallest-sample language, and ranking-reversal language did not locate the ten-case classification or the persistent family.

Risk: the arithmetic is elementary enough that an unindexed teaching example or software test could contain the same pair. Search failure is not proof of bibliographic uniqueness.

## Value
**PASS.** Raw accuracy and Cohen's kappa are both routinely reported in diagnostic and observer-agreement settings, and the literature explicitly warns that their marginal sensitivity can change interpretation. The result isolates the smallest all-positive, above-chance case in which that difference changes an actual comparative ranking, rather than merely changing a numerical value. The family shows that the effect persists at every larger sample size.

Self-review: passed. Independent audit: not yet performed.
