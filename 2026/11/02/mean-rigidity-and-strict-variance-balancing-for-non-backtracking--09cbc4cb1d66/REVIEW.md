# Scientific review

## Correctness (C): PASS

The claim covers all finite bouquets of at least two simple cycles of lengths at least three, with a hub start and the immediately-nonreversing transition. The proof reduces each excursion to a petal label, accounts for the final vertex being reached one edge before hub return, uses independent geometric waiting stages, and calculates the petal-occupation covariance eigenvalue via explicit first-step recurrences. The weighted variance decomposition and integer balancing argument then follow. The standard-library `verify.py` independently solves the original edge-and-visited-set chain using exact rational arithmetic; all 7,820 assertions passed. This finite test is supplementary, not an infinite proof. Potential risk: a different definition of cover time, notably counting full hub-return excursions, would shift the mean, but the definition and correction are explicit here.

## Originality (O): PASS, with residual historical-priority uncertainty

Full relevant material was inspected in Breen et al., arXiv:2203.12049 (2022), on non-backtracking Kemeny constants, and in Matsuo–Kawagishi–Ohsaki (first public November 2022) on non-backtracking mean first passage and cover times. The later Breen et al. arXiv:2510.06650 pinwheel discussion was also read for potential direct implications. None of the inspected claims evaluates both the hub-started bouquet cover-time mean for arbitrary petal lengths and its exact strict quadratic imbalance penalty in variance. Stationary mean hitting times do not determine the joint hitting-set cover statistic; model-wide order bounds do not imply its exact second moment. Searches for bouquet, pinwheel, windmill, non-backtracking coupon-collector, variance, and weighted occupation-time equivalents did not identify another covering result. Related classical Markov-reward or coupon-collector work remains a possible unlocated equivalent; absence of a match is not proof of historical priority.

## Value (V): PASS

A bouquet of cycles is a natural highly inhomogeneous family for studying non-backtracking vertex discovery: every petal is deterministically traversed once entered, but branch sizes affect the time cost of repeats. The mean's complete insensitivity to petal length allocation is a structural rigidity phenomenon, while the variance distinguishes every imbalance and yields the exact best design at fixed edge budget. This is not a generic coupon-collector restatement because the nonuniform petal traversal lengths and the negative same-petal transition correlation require a covariance calculation; a degree/eigenvalue formula for Kemeny's constant would not settle it.

## Literature and limitations

Checked: Breen et al. (2022), arXiv:2203.12049; Matsuo, Kawagishi and Ohsaki (2023), DOI 10.1587/comex.2022XBL0146; Breen et al. (2025), arXiv:2510.06650, for pinwheel comparison. The result is limited to non-backtracking hub-started vertex cover times on one-vertex cycle bouquets. Equivalent classical reward-process formulas may exist; independent assessment of historical priority is still needed.

Self-review: passed. Independent audit: not yet performed.
