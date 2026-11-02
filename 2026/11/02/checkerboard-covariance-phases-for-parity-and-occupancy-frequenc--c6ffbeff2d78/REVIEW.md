# Scientific review

## Correctness — PASS

The probability space is completely specified and the exact identity follows by conditioning on the number of balls in one marked box. The binomial odd-parity identity gives the conditional mean. For even frequencies, the decreasing function \(Ba^N-(B-1)b^N\) supplies strict negativity; for singleton frequency, the one-peak argument gives strict positivity. For each higher odd frequency, the difference of the sign bracket changes sign at most once from positive to negative, while the bracket begins negative and tends to \(1\), proving a unique negative-to-positive transition. Its monotonicity in odd frequency gives the complementary sign ordering. The fixed-frequency expansion is uniform on compact positive-density intervals; its simple limiting zero justifies the bounded \(O_r(1)\) integer crossover error. Direct enumeration, exact-rational arithmetic and asymptotic checks agree with the proof, but do not replace it.

## Originality — PASS, subject to historical-priority risk

Targeted comparison against related published research records and primary sources found broad occupancy-moment and hypercube-mixing theory, but no matching finite parity-versus-frequency sign classification across all dimensions, sample sizes and frequency indices. Gnedin–Hansen–Pitman (arXiv:math/0701718) and Barbour–Gnedin (arXiv:0809.4387) provide occupancy moments and limiting multi-frequency covariances. Their general machinery might algebraically recover the large-box formula, so novelty is **not** claimed for generic binomial parity moments or broad joint-count methods. Nestoridi (arXiv:1507.05690) analyzes hypercube mixing rather than the historical flip-frequency covariance. Equivalent treatments could exist in classical occupancy literature not located in the inspected corpus; independent priority confirmation is outstanding.

## Mathematical value — PASS

The odd-load count is the Hamming weight of the simplest hypercube random walk, and the frequency counts describe the walk's historical flip distribution. Their dependence is not characterized by the signs of the standard occupied-box statistics. The complete checkerboard law reveals a strict odd/even structural dichotomy, a unique finite time transition at each nontrivial odd frequency, and an explicit sharp critical intensity with bounded integer error. These are natural, all-parameter structural facts, not merely isolated numerical covariances.

## Verification and limits

The attached exact arithmetic verifier reports `VERIFY_OK 144293`. The proof applies at all stated integer parameters; the large-box threshold applies at each fixed higher odd frequency. No assertion of novelty for general multinomial conditional moments, unequal box probabilities, or growing-frequency thresholds is made.

Self-review: passed. Independent audit: not yet performed.
