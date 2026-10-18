# Self-review

## Correctness — PASS

The claim concerns exactly the improvement from an odd jury to one with two additional voters. Conditional gain-loss enumeration produces a binomial factor times signed powers of \(\lambda=p(1-p)\). Equal parameters are combined before the effective support count is set. An elementary exponential-polynomial Rolle argument proves the nonasymptotic upper bound for all jury sizes, and interlacing gives a genuinely sharp family of valid probability laws. The limit of its leading weight to one proves high average competence and majority favorable environments. Positive pairwise correlation is exactly \(\operatorname{Var}(P)>0\). Reproduced exact checks are supporting, not a substitute for these infinite proofs.

## Originality — PASS (best-knowledge, residual risk)

The inspected primary full texts include Dietrich–Spiekermann (MPRA 40135, §6 and Appendix A), Kaniovski's correlated voting study, and Kaniovski–Zaigraev's homogeneous correlated-jury design. They address de Finetti averaging, conditional monotonicity or parametrized correlation, but the examined theorem statements do not imply the \(d-1\) sharp finite-support reversal count with the realizing family. Searches of published research records did not identify equivalent or dominating results; these are not exhaustive novelty certificates. Berend–Sapir's 2007 paper is unusually close: its public abstract promises necessary/sufficient dependent-voter augmentation criteria, while its inaccessible complete text could include the present special result. This is an explicit outstanding bibliographic risk, not an assertion of full-text exclusion.

## Mathematical value — PASS

The theorem quantitatively determines how often expanding a correlated jury may help or hurt as the electorate grows. The dependence on effective numbers of environmental competence scales rather than the mean accuracy is structural. The attaining construction rules out a blanket monotonicity claim even for a highly competent, positively correlated electorate. The proof has no implications for strategic votes, continuously distributed latent quality, or arbitrary dependence graphs.

## Verification and limits

`verify.py` checked 175 exact rational sign evaluations for \(2\le d\le15\), reproduced the exact three-regime coefficients, and independently compared five odd-jury majority probabilities via 100-digit arithmetic. The global result follows from the written proof. No independent audit was performed.

Self-review: passed. Independent audit: not yet performed.
