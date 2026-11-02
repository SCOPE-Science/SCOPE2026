# Scientific review: positional record–excedance dependence

## Correctness (PASS)
The proof partitions the covariance by relative position and uses the independence of a uniformly sampled prefix set from its internal rank order. For earlier excedances the prefix maximum is certainly greater than the position threshold; for same-position excedances the sole failure is selection of the initial \(i\) values, with probability \(\binom ni^{-1}\). Independence for later excedances follows by conditioning on the later value, and exact row sums prove the five-element sign boundary. The finite computations (500825 exact assertions in `verify.py`) independently reconstruct the table through eight entries and probe the sign inequalities to size 1000; the all-size proof does not depend on enumeration.

## Originality (PASS, with historical qualification)
Ehrenborg–Steingrímsson's excedance-set work, Gnedin's record-rank study, and Brändén–Claesson's mesh-pattern representations supply the natural starting points. Their inspected contents do not give the exact mixed \(\operatorname{Cov}(R_i,E_j)\) kernel or the strict global sample-size threshold \(n=5\). They are not excluded from having more general identities from which portions might be recovered; this historical-priority risk remains for independent assessment. The standard record/Eulerian marginals are not new contributions.

## Mathematical value (PASS)
The theorem resolves the complete position-dependent interaction of two canonical random-permutation statistics. Its unexpected sign pattern explains how negative contributions from all earlier excedances coexist with a positive record–excedance covariance for the whole permutation from size five onward, and quantifies the finite nonzero covariance alongside vanishing asymptotic correlation. This is more informative than a marginal generating function or an isolated moment computation.

## Scope and literature risk
All conclusions require a uniform permutation and one-based strict records/excedances. A general joint statistic enumerator could implicitly contain the finite covariance but must be checked for actual implication; the accessible primary sources examined do not state the positional matrix. No independent originality or correctness validation is claimed.

Self-review: passed. Independent audit: not yet performed.
