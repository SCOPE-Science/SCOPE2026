# Scientific review

## Correctness

PASS. The logarithmically tilted rates \(r_{n,i}=1+\theta_{n,i}/\log n\) sum exactly to \(n\). Their late-first-arrival intensities sum to \(\kappa e^{-s}\), and their rare long-gap birth intensities converge to \(\kappa e^{-c}\) with unit-exponential residual lifetimes. Each coupon makes at most one relevant rare-gap mark on a bounded start horizon, allowing a direct independent triangular-array Poisson limit. The superposition clock and the near-threshold-gap estimate transfer this to fixed draw-count windows, and integer-valued path convergence gives the first-hitting law. The hitting-time renewal/resolvent calculation gives the limiting Laplace transform and mean. Jensen's inequality proves the exact weak-heterogeneity penalty \(\kappa\ge1\). The checker passes 60 exact and numerical assertions; asymptotic statements rely on the analytic argument.

## Originality

PASS, with residual priority uncertainty. Earlier uniform expiring-window process results already identify a stationary immigration–death chain and its first-hitting law; those are not claimed anew. The present theorem instead treats arbitrarily bounded, triangular nonuniform weights differing from uniformity at the critical relative scale \(1/\log n\), and proves dependence of the *entire* dynamic and first-completion laws on the exponential profile statistic \(\kappa=\lim n^{-1}\sum_i e^{-\theta_{n,i}}\). Long's motivating paper gives uniform critical one-time occupancy and stationary flux, and Attrill–Garoni analyze a different clumsy-reset model. Published record searches found related heterogeneity in reset coupon collectors, but no statement implying the nonuniform deterministic-expiration limit. General Poisson-extreme and nonuniform coupon-collector literature remains a priority risk.

## Value

PASS. The order \(1/\log n\) is the sharp natural scale at which tiny changes in type frequencies become order-one multiplicative changes in critical missing-type intensities. The theorem identifies the one-parameter universality statistic and proves a strict Jensen penalty even though the sampling probabilities themselves converge uniformly to \(1/n\) in relative error. This resolves a motivated sensitivity question for finite-lifetime coverage and supplies its process and completion-time consequences.

## Scope and risks

Only uniformly bounded, mean-zero logarithmic profiles with a convergent exponential mean; fixed finite \(c\) and deterministic expiration. No finite-\(n\) mean convergence, quantitative error, or general nonuniform result. No independent historical-priority or mathematical audit.

Self-review: passed. Independent audit: not yet performed.
