# Review

## Correctness

PASS. Under the Prüfer bijection, a uniform labeled tree becomes \(n-2\) iid uniform labels, the degree of a fixed vertex is one plus its occupancy, and the leaves are exactly the empty labels. The mixed generating function follows by separating the distinguished vertex's own empty-box indicator from the other \(n-1\) empty-box indicators.

Differentiating at \(z=1\), or equivalently counting ordered marked Prüfer positions, gives the factorial covariance formula exactly. Its first-order bracket is zero, and for every higher order strict positivity follows from \(((n-1)/n)^r<(n-1)/n\). The fixed-order limit is a direct expansion. Exact enumeration through \(n=8\) reproduces all identities.

## Originality

PASS, with a specific occupancy-literature residual risk. Aldous's full public text was inspected at its leaf and degree sections and at the complete-graph specialization. It treats leaf probabilities and degree distributions, including the known binomial degree law for uniform labeled trees, but does not state the degree/total-leaf mixed covariance or higher factorial hierarchy.

Steele's classical leaf-count work was checked at the accessible abstract and bibliographic record. It studies the total leaf count and its central limit behavior, not a distinguished degree jointly with that count.

The closest own occupancy result concerns the total number of occupied boxes against counts of boxes of a specified occupancy. It does not state the covariance of one specified box's factorial occupancy with the number of empty boxes, nor the Cayley-tree interpretation and exact first-order cancellation.

## Value

PASS. Degree and leaf abundance are among the most basic local and global statistics of a random labeled tree. Exact zero covariance would ordinarily suggest weak first-order interaction, but the conditional mean is explicitly nonconstant and nonmonotone: moving from leaf to degree two lowers expected leaf abundance, while further degree increases raise it.

The all-order factorial hierarchy isolates the cancellation as genuinely first-order rather than an independence phenomenon. The positive limiting constants \((r-1)/e\) provide a compact local-to-global dependence signature that is useful when comparing tree statistics through Prüfer occupancy.

Self-review: passed. Independent audit: not yet performed.


Exact replay: `VERIFY_OK words_checked=280391 leaf_mean_checks=6 first_cov_checks=6 factorial_cov_checks=21 conditional_checks=27 pgf_checks=24 sign_checks=15`.
