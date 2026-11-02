# Self-review

## Correctness — PASS
The binary-cylinder transfer matrices are exact, and row-vector updates prove both universal finite-horizon bounds and their equality cases. Tail-sum evaluation yields the expected first-hit interval. Periodic products give the entropy and escape formulas, while Perron measures and dyadic cylinders give Hausdorff dimension. Opposite-hole products are unipotent; repeated-hole blocks and operator-norm estimates separate the three cyclic regimes. `CHECK.py` corroborates the combinatorial and matrix identities with 1023 exact brute-force cases and 2046 finite spectral cases, but the infinite assertions are proved analytically.

## Originality — PASS within inspected evidence
The closest papers are Cheriyath–Agarwal (arXiv:1905.11767, fixed binary cylinder holes), Livorati et al. (arXiv:1312.7030, different time-varying geometric holes), Atnip et al. (arXiv:2103.04712, general random open pressure) and Agarwal et al. (arXiv:2401.05118, fixed Markov-measure holes). These were compared to the actual extremal *all-schedule* statement, not to the title. Published semantic-index comparisons also found nearby static survivor/zeta results, not the proposed sharp two-matrix moving-hole classification. Existing nonnegative-matrix theory might recover parts implicitly; comprehensive priority confirmation remains outstanding.

## Mathematical value — PASS
Switching between equal-length holes makes the escape problem intrinsic rather than an artifact of hole size. The exact ordering at every finite horizon and the countable-versus-positive-dimension periodic phase boundary provide meaningful dynamical information beyond standard fixed-hole escape rates.

## Limitations
Only the two complementary binary two-digit holes are studied, starting from Lebesgue measure. No general aperiodic dimension classification or higher-symbol optimization is claimed. Finite computation does not certify the infinite assertions. Independent scientific validation remains open.

Self-review: passed. Independent audit: not yet performed.
