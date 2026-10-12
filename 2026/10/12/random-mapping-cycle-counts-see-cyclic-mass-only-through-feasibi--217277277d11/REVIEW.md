# Review

## Correctness

PASS. Conditional on \(L_n=m\), each cyclic set and each permutation on that set receives the same number of attached rooted forests. Hence the cyclic restriction is exactly a uniform permutation. Ordered collections of \(r\) disjoint \(\ell\)-cycles in a uniform permutation have factorial mean \(\ell^{-r}\) exactly when \(m\ge r\ell\), and zero otherwise. This proves the master conditional identity and all covariance reductions.

The cyclic-point tail law follows from exact mapping counts and telescoping. The fixed-point independence is checked both through the master identity and directly at the level of a specified label. The large-\(n\) covariance uses only the classical \(\sqrt n\)-scale cyclic-point mean and a fixed-threshold expansion.

## Originality

PASS, with explicit residual risk from older mapping enumerations. The closest full inspected source is Hansen--Jaworski because it states the exact conditional uniform-permutation structure used here. Its subsequent results concern typical component sizes and Poisson--Dirichlet limits, not fixed-point independence or fixed-cycle factorial covariances against \(L_n\).

English's factorial-moment paper concerns the aggregate number of components and aggregate cyclic elements. Arratia--Tavaré provides broad asymptotic process approximations. Neither accessible statement supplies the finite threshold kernel (1)--(2).

The own prior mapping result concerns total connected components conditional on the number of cyclic vertices. It uses a Bernoulli-sum representation of permutation cycle count but does not state fixed-length cycle counts, fixed-point independence, or the higher factorial threshold hierarchy.

## Value

PASS. A fixed point is itself a cyclic vertex, so independence of each fixed-point indicator from the total number of cyclic vertices is structurally counterintuitive. The theorem explains the cancellation rather than merely observing zero covariance: all factorial mixed moments collapse to feasibility thresholds.

The higher-order formula shows exactly where dependence returns. It also covers every cycle length and every factorial order in one statement, giving a reusable local-to-global dependence law rather than an isolated numerical covariance.

Self-review: passed. Independent audit: not yet performed.


Exact replay: `VERIFY_OK mappings=50068 dist_checks=40 conditional_checks=187 covariance_checks=120 indicator_independence_checks=20 fixed_mean_checks=25 second_moment_checks=5`.
