# Scientific review: closed–singleton dependence in site-percolated recursive trees

## Correctness (C): PASS

The complete transition table follows from independent Bernoulli retention and one uniform attachment per arrival. The finite covariance recurrence is derived directly from total covariance, without an independence assumption between the counts, and the Gamma product telescopes exactly from the one-vertex initial condition. The unique parameter threshold and the logarithmic critical correction follow from classical Gamma and harmonic asymptotics. The martingale-array proof identifies the conditional increment covariance, shows quadratic fluctuations using bounded deterministic propagators, and evaluates the limiting Gaussian covariance explicitly. Independent small-size enumeration, rational matrix checks and large-size numerical recurrences passed 180 assertions. The infinite theorems rely on the written argument, not numerical data.

## Originality (O): PASS, qualified

The original 2024 Gu–Yuan site-percolation paper proves a law of large numbers and largest-cluster results, and explicitly supplies the Markov transitions for cluster counts; the transitions themselves and singleton first-order limit are prior art. Earlier Kalay–Ben-Naim work gives cluster-frequency predictions, and Janson's general small-urn theory covers Gaussian convergence in principle. The precise all-\(n\) cross covariance between the *deleted-vertex* count and *open singleton-component* count, its unique sharp asymptotic sign change, and the anomalously small positive covariance at the critical parameter were not identified as statements or implications of the inspected sources. A general covariance-matrix theorem need not include the specialized closed form and sign analysis, but could yield them after calculation; this is a genuine related-work limitation. Further unindexed specializations may exist.

## Value (V): PASS

The two natural observables describe complementary effects of deletion: how many sites disappear and how many surviving components remain isolated. An exact covariance with an unexpected sign reversal determines when increasing deletions corresponds, in the annealed law, to a deficit or excess of isolated survivor components. The cancellation at a concrete interior retention parameter shows a fine distinction between zero limiting Gaussian correlation and finite-size dependence. This is a structural dependence result across the full retention range, not an arbitrary numerical instance.

## Boundaries

The signs away from the critical retention probability are eventual, not asserted at every size. Critical covariance tends to zero but does not establish finite-size independence. The model requires uniform recursive attachment and independent sites; full historical priority and independent validation remain open.

Self-review: passed. Independent audit: not yet performed.
