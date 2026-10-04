# Same-model review

## Correctness
PASS. Under the complete null, the FDP equals the indicator of at least one rejection. For iid \(E_i=cB_i\), the e-BH step-up rule reduces exactly to \(Nc\ge K/\alpha\). Monotonicity in \(c\) and the constraint \(pc\le1\) reduce the family to \(c=1/p\), after which the threshold is \(\lceil Kp/\alpha\rceil\). Partitioning \(p\) by this integer threshold gives the finite binomial-tail envelope. The low-level optimizer follows from the factorial-moment bound and a Bonferroni lower bound, with no asymptotic or computational step needed for the theorem.

## Originality
PASS. The closest primary source defines base e-BH, proves arbitrary-dependence FDR control, discusses all-or-nothing e-values, gives a perfectly dependent sharpness construction, and supplies PRDS bounds. Those results do not state the exact iid two-point complete-null FDR, optimize over the two-point calibration, or identify the one-spike extremizer. Focused literature and database searches using aliases such as “all-or-nothing”, “two-point”, “Bernoulli e-value”, “iid”, “complete null”, and “exact FDR” did not reveal an equivalent statement. Residual risk remains that the elementary specialization may appear in unindexed notes or supplementary material.

## Value
PASS. All-or-nothing e-values are a canonical extremal testing construction in the e-value literature, and base e-BH is a standard multiple-testing rule. Quantifying its exact complete-null calibration under independence gives a natural benchmark for how much the arbitrary-dependence sharpness example relies on common-event dependence. The finite envelope, unique conventional-level optimizer, and explicit limit \(1-e^{-\alpha}\) provide a reusable calibration fact rather than a parameter-only numerical recomputation.

## Closest literature and limitations
Wang--Ramdas (arXiv:2009.02824v1; DOI:10.1111/rssb.12489) is the direct source. Lee--Ren (arXiv:2404.17562v1) is a later e-BH calibration paper checked for potentially stronger coverage. The result is restricted to iid identical two-point null e-values and does not characterize arbitrary independent e-value distributions or alternatives. The stated \(\alpha_0\) is sufficient, not claimed optimal.

Same-model review: passed. Independent audit: not yet performed.
