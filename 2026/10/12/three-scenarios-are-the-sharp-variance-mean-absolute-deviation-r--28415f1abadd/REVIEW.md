# Self-review

## Correctness
**PASS.** The lower bound is exact: any two equally weighted observations have centered deviations of equal magnitude and opposite sign, so population variance is exactly the square of mean absolute deviation. The three-scenario witness has common mean \(20\), with MAD values \(20/3<22/3\) but variance values \(200/3>182/3\). The general centered triple formula \(M=2s/3\), \(V=s^2/2+h^2/6\) is derived algebraically, and padding by the common mean proves persistence at every larger scenario count. The packaged verifier returns `VERIFY_OK`.

Risk: unequal scenario probabilities are not covered by the support-two identity in this form and require a separate boundary analysis.

## Originality
**PASS.** Konno and Yamazaki directly compare the \(L_1\) mean-absolute-deviation and Markowitz \(L_2\) risk models, and prove exact proportionality for multivariate normal returns. That strong prior result covers order equivalence under normality but does not state the smallest equally weighted finite support on which order reversal is possible. Targeted database and web searches did not locate the one/two-scenario identity as a sharp portfolio-ranking boundary, the equal-mean three-scenario witness, or the exact \((s,h)\) decomposition.

Risk: the boundary is elementary once both dispersion formulas are written together, so an unindexed teaching or software example may contain an equivalent construction.

## Value
**PASS.** Mean-variance and mean-absolute-deviation optimization are established competing portfolio models. The result identifies the smallest scenario model in which choosing one dispersion penalty rather than the other can change a deterministic portfolio risk ranking. The equal-mean witness isolates the modeling choice itself, and the structural formula shows precisely how variance's quadratic penalty sees within-side imbalance that MAD ignores.

Self-review: passed. Independent audit: not yet performed.
