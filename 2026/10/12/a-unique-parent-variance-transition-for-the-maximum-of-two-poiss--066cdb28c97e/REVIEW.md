# Scientific review: a unique parent-variance transition for two Poisson counts

## Correctness — PASS

The identity \(M=(S+|D|)/2\), the symmetric Skellam mass function, and the modified-Bessel recurrence give \(\mathbb EM=\lambda+h\) and \(\operatorname{Var}(M)=\lambda+\lambda k-h^2\), with \(k=e^{-2\lambda}I_0(2\lambda)\) and \(h=\lambda e^{-2\lambda}(I_0(2\lambda)+I_1(2\lambda))\). The crucial global step is a direct strictly positive logarithmic derivative of \(R=h^2/(\lambda k)\) and its two endpoint limits, which prove existence and uniqueness of the crossing for all real \(\lambda>0\). The maximum's own-mean underdispersion follows from a separate strictly positive exact difference. The verification script checks but does not replace these analytic deductions.

## Originality — PASS, with residual risk

The full text of Badiella–del Castillo–Puig (DOI:10.1016/j.spl.2023.109900), including its last-page corollary and references, establishes the different relation \(\operatorname{Var}(M)<\mathbb EM\); it does not classify the sign of \(\operatorname{Var}(M)-\lambda\). Classical Skellam and Bessel identities, and previously available exact moments of two Poisson extremes, are acknowledged inputs, not the novelty claim. Those identities determine a function but do not by themselves state or prove that it has one and only one positive zero. The positive derivative identity supplies the extra comparison. Searches for variance crossover, Skellam aliases, and modified-Bessel formulations found no explicitly covering unique-crossing theorem; unindexed equivalent results remain a real risk.

## Value — PASS

This answers a natural statistical design question left distinct by underdispersion theory: whether selecting the larger of two replicated Poisson counts increases or decreases the variance relative to one unselected count with the same intensity. It proves a global two-regime phase diagram with an exact, unique transition, not merely a local expansion or an isolated computed example. The direction reversal matters because the own-mean Fano criterion would otherwise misleadingly suggest variance reduction at every intensity. The result is restricted to two matched counts, so no higher-sample conclusion is implied.

## Limits and closest published sources

The nearest directly relevant published theorem is Badiella–del Castillo–Puig's Poisson order-statistic underdispersion corollary (2023). Standard Skellam literature and NIST's Bessel references furnish the identities underlying the proof. Neither a machine-assisted text search nor this review rules out older equivalent expressions for the sharp crossing. The verification uses finite precision and supports only computation claims.

Self-review: passed. Independent audit: not yet performed.
