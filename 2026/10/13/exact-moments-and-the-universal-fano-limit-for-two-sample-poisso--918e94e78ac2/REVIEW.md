# Self-review

## Correctness
PASS. The claim is derived from an exact Skellam representation, a telescoping Bessel recurrence, an exact Poisson score identity, and standard Bessel asymptotics. The quantifiers cover every \(\lambda>0\). The numerical checker is supplementary and is not used as an infinite proof.

## Originality
PASS. The closest inspected primary source gives the Skellam difference law, while the closest order-statistic source proves only qualitative underdispersion. Searches across equivalent min/max, Skellam, absolute-difference, Bessel, and Fano formulations did not locate the paired variance formulas or the \(1-1/\pi\) limit with opposite first-order corrections. The publicly inaccessible 2015 Poisson Gini-mean-difference paper is retained as a specific overlap risk for the intermediate mean formula, not treated as ruled out.

## Value
PASS. The result quantitatively resolves the simplest Poisson order-statistic underdispersion problem, gives exact moments usable at finite intensity, and identifies a universal asymptotic noise reduction together with a directional min/max split.

## Closest literature and limitations
Gan and Kolaczyk (arXiv:1708.04018) provide the Skellam law but not order-statistic moments. Badiella, del Castillo and Puig (2023) prove Poisson order statistics are underdispersed but do not quantify the deficit. The result is restricted to two iid Poisson observations and does not claim a larger-sample analogue.

Self-review: passed. Independent audit: not yet performed.
