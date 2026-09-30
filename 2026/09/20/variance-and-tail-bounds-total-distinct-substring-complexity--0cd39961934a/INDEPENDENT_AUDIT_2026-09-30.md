# Independent audit — 2026-09-30

**Record:** `2026/09/20/variance-and-tail-bounds-total-distinct-substring-complexity--0cd39961934a`  
**Audited repository commit:** `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
**Assigned/current source tree:** `9b074764e528b1b24ecf97a105f63dad2f3545d4`  
**Disposition:** passed

## Correctness — PASS

PASS. I independently rederived both arguments. For two length-k windows at any displacement, including overlap, equality imposes a periodicity constraint with exactly d^{-k} probability. Splitting at K=floor(log_d n), the short-length deficit is deterministically O(n), while for k=K+j the collision-pair bound gives E G_{n,k}^q <= (1/2)n^{q+1}d^{-k}; the inequality n d^{-k}<d^{-(j-1)} is exactly what reduces its q-th root to n 2^{-1/q}d^{-(j-1)/q}, and Minkowski yields the stated all-q estimate. For centered concentration, the longest-repeat union bound, restricted Hamming Lipschitz constant c_n=L_n(L_n-1)/2, McShane extension, Efron--Stein, and McDiarmid constants all check. The exceptional-set contribution is at most n in the final variance inequality. No hidden independence between overlapping windows is assumed.

## Originality — PASS

PASS, with the stated suffix-tree/additive-functional residual risk. Janson--Lonardi--Szpankowski's full 2004 paper analyzes the same total sequence-complexity statistic at the level of its mean and explicitly says asymptotic variance analysis remains open. Godbole's 2026 paper again highlights variance/concentration for the total distinct-substring count. Ahmadi--Ward concern fixed-length subword complexity, and Gaither--Ward a fixed suffix-tree profile level. I found no source giving either the filed all-moment deficit estimate or an O_d(n log^4 n) total-statistic variance/concentration theorem. Older work phrased solely as a total LCP/suffix-tree additive functional remains the principal literature risk, so the claim is not treated as an exhaustive novelty guarantee.

## Scientific value — PASS

PASS. The work directly supplies rigorous variance and concentration information for an all-length statistic whose mean is much better understood, while a separate theorem gives exponential control of the deficit from the exact deterministic maximum. The bounds are not asymptotically sharp, but they are nontrivial, explicit, and obtained by reusable collision and good-set Lipschitz arguments.

## Findings

- The overlap collision identity and every numerical exponent in the all-moment proof were independently rechecked.
- The variance transfer through the McShane extension gives Var(D_n)<=n(c_n^2+1) with the stated L_n choice.
- The 2004 same-statistic paper explicitly leaves asymptotic variance analysis open; the 2026 motivating paper again asks for variance/concentration information.

## Independent checks

- Recomputed the q-th moment reduction at k=floor(log_d n)+j, including the n d^{-k}<d^{-(j-1)} step.
- Rechecked the longest repeated substring union bound with overlapping windows.
- Re-derived the Efron--Stein and McDiarmid constants after extension and the exceptional-event error terms.
- Compared the result against first-moment, fixed-length, and suffix-tree-profile literature.

## Literature evidence

- https://arxiv.org/abs/2609.19409 — Godbole (2026), motivating expected-distinct-substrings paper highlighting the variance/concentration question.
- https://doi.org/10.1016/j.tcs.2004.06.023 — Janson, Lonardi and Szpankowski (2004), precise mean analysis for total sequence complexity; the full paper explicitly leaves asymptotic variance open.
- https://doi.org/10.3390/e22020207 — Ahmadi and Ward (2020), second-moment analysis for fixed-length subword complexity rather than the total all-length statistic.
- https://arxiv.org/abs/1605.03390 — Gaither and Ward (2016), variance of a fixed suffix-tree internal-profile level.

## Limitations

- Uniform iid letters and fixed alphabet size are essential to the present collision calculation.
- The O_d(n log^4 n) variance bound is only an upper bound; no sharp variance asymptotic, lower bound, CLT, or optimal concentration scale is established.
- An equivalent older result under total-LCP or suffix-tree additive-functional terminology cannot be categorically excluded.

No GitHub write was performed by this audit. The guarded change set only stages this audit evidence and updates the independent-audit channel in `VERIFICATION.md`; it leaves the research claim files unchanged.
