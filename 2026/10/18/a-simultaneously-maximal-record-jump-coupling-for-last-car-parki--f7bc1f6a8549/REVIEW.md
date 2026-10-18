# Review of the record-jump coupling

## Correctness

**PASS.** Exact p(n,m) is attributed to Pinsky, Corollary 5. The strict mass-loss ratio is maximized at m=1, where an explicit logarithmic derivative is negative. The transition kernel preserves every finite-size marginal by induction. Monotonicity plus the known Borel marginal limit yields almost-sure convergence to a finite integer. The restriction that newly attained states must be the current maximum proves simultaneous maximality. Stirling and Euler--Maclaurin yield both coefficients of the total-variation tail. The expected jump count is the divergent sum of exact new-state masses. Direct enumeration and rational finite checks are reproducible in `verify.py`; they do not prove the infinite statement.

## Originality

**PASS on inspected evidence, with residual risk.** Pinsky (arXiv:2404.11529), Corollaries 5--6, already proves the exact last-car marginal formula and Borel weak convergence, a stronger fixed-size distributional input than the present work needs. Diaconis--Hicks (arXiv:1611.09821), Theorem 1 and Corollary 3, provides a reindexed equivalent marginal statistic. No assertion of fresh marginal enumeration or of a new Borel limit is made. Neither inspected primary treatment states the cross-size strict mass-loss theorem, the unique stay-or-new-maximum Markov kernel, the simultaneous maximum-agreement coupling, or the almost-surely-finite/infinite-mean jump distinction. These properties are deductions from earlier exact formulas, not independent enumerative inputs; older implicit or explicit derivations remain possible. Published mathematical literature and related statistical claims were compared; the closest parking records concerned polytopes or different parking statistics, not this stochastic coupling.

## Value

**PASS.** A finite Borel approximation is limited by its unavailable tail mass. This result proves that the last-car distribution meets the optimal information-theoretic truncation error at **every** finite size, identifies a single stochastic process achieving all optimal comparisons simultaneously, and gives the sharp second-order convergence rate. The exact record-jump mechanism also exhibits a meaningful tension between a.s. finite changes and logarithmically divergent expected change count, which is relevant to consistent simulation across sizes. The theorem is not claimed as a broader result about all parking-function coordinates.

## Limits and nearby literature

The full fixed-size law in Pinsky (2024) and the corresponding Diaconis--Hicks (2016) law are essential prior coverage. An implicit coupling identity may exist in earlier work; no exhaustive historical-priority claim is made. Bellin (2021) addresses asymptotics of preferred-coordinate positions, not the last parked car's cross-size record-jump kernel. The finite checker supports arithmetic only; no externally performed audit is reported.

Self-review: passed. Independent audit: not yet performed.
