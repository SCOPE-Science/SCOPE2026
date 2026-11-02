# Scientific review: a sharp Mittag–Leffler quartic crossover

## Correctness — PASS

The exact conditional law is a fair-sign sum with independent random length \(K_n\). For \(x=O(m^{1/4})\), exponential tilting of the signs, a uniform Berry–Esseen bound under the tilted measure and the fourth-order Cramér rate expansion give the fixed-sample ratio \(\exp(-x^4/(12m)+o(1))\). The cited Gaussian martingale tail comparison gives a bound on the *relative* tail ratio that is independent of \(m\) and \(x\). The positive Mittag–Leffler limit of \(K_n/n^p\), dominated convergence, and a sequential uniformity argument then establish all quantifiers and both sides of the claimed sharp transition. The strict positivity of that limit is explicitly taken from the source literature, not presumed from moment convergence. A standard-library checker independently reproduces 2,088 finite exact/numerical assertions. No finite test is used as an infinite proof.

## Originality — PASS, with bounded historical risk

The closest source on the **same process and statistic** is Liang (arXiv:2610.29156v1): it proves a general logarithmic sufficient range at \(q=0\), and its obstruction to a universal polynomial range uses *nonsymmetric* two-point noise. It does not state the symmetric recovery or the critical random-clock mixture. Liu, Liu and Lu (arXiv:2610.29078v1) already identify the familiar \(\exp(-x^4/(12m))\) factor for an ordinary fixed-size Rademacher sum; that factor alone is expressly not claimed as novel. The new comparison is the random Mittag–Leffler mixture \(\mathbb E\exp(-c^4/(12W_p))\), which differs from replacing the clock by its expectation. Juškevičius and Šileikis (arXiv:2610.31449v1) establish a needed global comparison inequality, not the critical mixture. Eichelsbacher and Löwe (arXiv:1705.03837), Sections 3.1–3.3, provide logarithmic moderate-deviation principles for randomly stopped sums, not the present precise, self-normalized relative-tail boundary. Searches of accessible mathematical records and the relevant primary literature found no equivalent complete claim. Earlier unindexed random-index Cramér expansions might still have implicit coverage; this remains a real historical-priority risk.

## Mathematical value — PASS

The motivating 2026 paper leaves a sharp distinction between its general logarithmic positive result and its negative polynomial counterexample. The result isolates a natural symmetric positive-step subclass, proves a *sharp* polynomial boundary \(n^{p/4}\), and identifies the full nontrivial transition profile determined by a nonconcentrating random clock. This differentiates a normal relative-tail approximation from ordinary central limit and logarithmic large-deviation assertions. The fixed-sample quartic term is classical; the step-size symmetry, small-clock control and random-mixture transition are essential to the new statement.

## Scope and limitations

The finding covers one specified symmetric two-point step-size law, fixed \(p\in(0,1)\), and finite critical multipliers. It does not apply to the full position, arbitrary symmetric laws, or a diverging critical multiplier. There is no independent mathematical or historical-priority audit; the finite verification program is supplementary.

Self-review: passed. Independent audit: not yet performed.
