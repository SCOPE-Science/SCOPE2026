# Scientific review

## Correctness — PASS

The proof uses the exact one-step absorbing Markov chain under the stated Fermi update, and the scale function produces the exact expected visit counts \(G_{11}\) and \(G_{12}\), hence the total cost. The derivative is explicit. When \(B'(r)\le0\), cost monotonicity is immediate; when \(B'(r)>0\), the polynomial forces \(r<1/(2T)\), while the logarithmic bound \(r\log(R/r)<1\) and the strict logarithmic derivative bound prove \(E_2'(\theta)>0\). All boundary cases \(N=4\), \(\theta=0\), and arbitrary \(\beta>0\), \(\delta<0\) are included. The independent direct Markov inversion in `check.py` agrees with 182 exact-rational instances and 10,000 numerical derivative checks pass. These computations only corroborate, not replace, the full proof.

## Originality — PASS (subject to external prior-art risk)

The 2024 source paper gives two-reward-state formulas but formally establishes monotonicity only for threshold one and explicitly leaves higher-threshold monotonicity as a conjectural issue. The present result proves the first excluded threshold for all \(N\ge4\) and a specified initial-state convention. Han–Tran-Thanh (2018) treats composition-dependent rewards but supplies simulations for the relevant policy; Duong–Han (2021) and Duong–Durbac–Han (2023) analyze full investment or mixed incentives, which do not imply the assertion. Searches of the mathematical findings index and past accessible scientific claims yielded no equivalent. A theorem hidden in unindexed subsequent literature cannot be categorically excluded.

## Mathematical value — PASS

The source identifies threshold-dependent monotonicity as a nontrivial unsolved optimization problem; this theorem resolves an infinite family at the first genuinely intermediate threshold, and produces an explicit globally optimal reward for a target cooperation fraction. It distinguishes two-cooperator conditional reward from full investment, where cost can fail to be monotone, and gives a useful rigorous boundary case for understanding the threshold conjecture.

## Limits

Only rare-mutation, all-defector-origin excursions (starting at one mutant), \(N\ge4\), constant payoff difference and threshold two are covered; general threshold monotonicity and the equally weighted two-origin convention remain open. Prior-art verification is self-review rather than independent.

Self-review: passed. Independent audit: not yet performed.
