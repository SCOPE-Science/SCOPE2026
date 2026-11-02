# Scientific review

## Correctness

**PASS.** The activity count satisfies the exact conditional increment probability \(\alpha K_t/t\). Conditioning on its value at time \(n\) gives an exact survival product. A direct first-success decomposition gives the first two activity-class probabilities, and gamma-ratio asymptotics prove the fixed-time tail and moment threshold. The local-wait mixing argument uses an almost-sure activity limit proved in Bercu (arXiv:2203.04196, Lemma 2.1), with explicit vanishing log-product errors. The limiting Pareto constant uses the classical Mittag-Leffler asymptotic. Finite independent enumeration supports, but does not replace, these proofs.

## Originality

**PASS, subject to priority risk.** The most relevant sources include Miyazaki and Takei, arXiv:2003.04441, on the exact same binary activity process; Bercu, arXiv:2203.04196; Huillet and Möhle, arXiv:2211.17044, especially Section 8; and the delay-count papers arXiv:2005.09517 and arXiv:1906.04930. Miyazaki and Takei already prove the positive Mittag-Leffler count limit and Gaussian refinements for the equivalent binary activity chain; Huillet and Möhle's reinforced harmonic Bernoulli model **also contains** the activity-count birth process after a parameter substitution. It is not novel to construct that process or to cite its Mittag-Leffler limit. The compared primary material concerns count laws, the position, or waiting times in an independent Bernoulli scheme, not the new combined deterministic-time forward waiting theorem with its invariant far-tail coefficient and changed macroscopic exponent. Related species-sampling waiting results may provide unlocated prior coverage; Möhle’s 2021 restaurant-process article (DOI:10.1017/jpr.2021.10) was only accessible as an abstract, so its full results were not ruled out.

## Value

**PASS.** The waiting observable is natural for intermittent motion; its infinite mean at *each* finite observation time, universal far-tail coefficient, explicit next-order correction and order-of-limits change address a concrete aging question not determined by a first-moment growth rate. The result distinguishes fixed-time rare histories from typical local inactivity, rather than simply renaming a known count asymptotic.

## Limitations and evidence

The theorem assumes uniform full memory, constant stop probability and a nonzero initial step. No two-parameter uniform crossover or renewal independence is claimed. External inputs are named explicitly, including the Bercu activity-count theorem and classical Mittag-Leffler asymptotic. Exact finite checks: `python CHECK.py`, 609 passed. Historical-priority coverage may be incomplete, and no independent mathematical validation has been performed.

Self-review: passed. Independent audit: not yet performed.
