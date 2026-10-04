# Review

## Correctness

PASS. The classical forest-extension formula counts trees containing a fixed forest by the product of component sizes times a power of \(n\). Applied first to a marked geodesic and then to the geodesic with selected extra endpoint edges, it gives every subset-inclusion probability of off-path neighbors. The resulting probability generating function factors exactly into a binomial and a Bernoulli term.

The stochastic regression follows from an explicit coupling that removes one Bernoulli trial and lowers a second Bernoulli success probability whenever the conditioned distance increases by one. The covariance inequalities and asymptotics then follow analytically.

## Originality

PASS, with a residual classical-enumeration risk. Pitman's full paper was inspected at the unrooted forest-extension lemma. It supplies the counting engine but does not state the marked degree-distance conditional law.

Aldous's random-tree paper explicitly lists degree distribution and diameter as studied observables. Berzunza Ojeda--Janson's full open article treats distance profiles and root-degree conditioning in a general simply generated-tree framework. Neither inspected source states the binomial-plus-Bernoulli conditional law, strict stochastic regression, or covariance limit.

Targeted semantic-database and web searches for conditional degree given distance, degree-distance covariance, stochastic monotonicity, and equivalent Cayley-tree formulations found no matching theorem.

## Value

PASS. Degree and distance are two of the most basic local/global observables of a random tree. The result gives a complete finite conditional distribution rather than a single moment, and upgrades the intuitive statement that farther marked vertices favor smaller endpoint degree to exact first-order stochastic regression.

The asymptotic \(\operatorname{Cov}(D,\Delta)\to-1\) together with vanishing correlation quantifies a useful scale-separation phenomenon: dependence remains order one even though distance fluctuations grow like \(\sqrt n\).

Same-model review: passed. Independent audit: not yet performed.


Exact replay: `VERIFY_OK trees_enumerated=280392 distance_mass_checks=28 conditional_probability_checks=84 mean_checks=28 stochastic_tail_checks=85241 covariance_checks=7`.
