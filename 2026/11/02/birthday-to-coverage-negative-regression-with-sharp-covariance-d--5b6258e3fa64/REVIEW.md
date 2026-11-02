# Self-review: birthday-to-coverage negative regression

## Correctness — PASS

The claim uses one iid uniform sampling stream and handles the exceptional all-distinct outcome \(B_m=m+1\) separately. The conditional geometric-sum representation follows directly from the successive discovery stages. Deleting one independent geometric stage couples successive conditional coverage-time distributions, proving strict first-order stochastic ordering for every integer \(m\ge2\). An independent-copy covariance identity then proves negative quadrant dependence and strict negative covariance. The exact finite-sample expression follows from the birthday mass function and the conditional geometric means. The Rayleigh moment limit, an explicit harmonic decrement expansion and exponential control of the exceptional tail yield the asymptotic covariance, while standard geometric-stage variances yield the displayed correlation constant. A standalone exact-rational/Markov-chain program passed 3,493 assertions. The finite tests do not replace the analytic proof.

## Originality — PASS (historical priority not independently certified)

Relevant search formulations were checked in a mathematical-finding index and in public research literature: first birthday collision jointly with coupon-collector completion; first repeat versus last new type; conditional stochastic ordering; negative dependence and covariance; and Rayleigh/Gumbel coupling. The accessible scientific records did not exhibit the complete conditional stochastic-order theorem and sharp mixed covariance constant. An accessible full primary PDF by Myers and Wilf (arXiv:math/0304229v1) was examined for its introduction, section structure and relevant terminal section; its results treat independent competing collectors, multiple copies and final singleton counts, rather than the same-stream first-repeat/completion pair. Flajolet and Sedgewick (2009, Chapter II) treats the two classical marginal stopping-time problems side-by-side; its accessible chapter excerpts and author-maintained book page were inspected. Marginal formulas alone do not establish their joint stochastic order or the covariance asymptotics. The complete large textbook was not read; an obscure historical theorem remains a priority risk, not a proved impossibility.

## Mathematical value — PASS

First collision and full coverage are two canonical, operationally meaningful stopping times for one uniform occupancy sequence. Proving a complete, strict conditional stochastic ordering is stronger than computing one covariance: it yields negative quadrant dependence and covariance inequalities for arbitrary increasing score functions. The sharp \(\sqrt m\) covariance and \(m^{-1}\) correlation rates quantify how a finite-sample inverse relationship persists but becomes weak in standardized terms. This gives a motivated exact dependence theorem rather than a renamed marginal identity.

## Literature and limits

Closest primary sources: Myers and Wilf, *Some New Aspects of the Coupon-Collector's Problem* (2003), arXiv:math/0304229v1, https://arxiv.org/abs/math/0304229 ; Flajolet and Sedgewick, *Analytic Combinatorics* (2009), Chapter II, https://algo.inria.fr/flajolet/Publications/AnaCombi/anacombi.html . Only uniform iid sampling is covered, and the full 2009 textbook was not exhaustively inspected. Equivalence to an older unlocated joint stopping-time result remains possible. No external or independent validation is represented.

Self-review: passed. Independent audit: not yet performed.
