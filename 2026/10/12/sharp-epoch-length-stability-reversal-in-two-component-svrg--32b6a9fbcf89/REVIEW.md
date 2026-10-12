# Self-review

## Correctness — PASS

The exactly specified sampling and snapshot update produce a finite signed-curvature recurrence. Independent Walsh terms give the two exact squared-moment polynomials. The two cutoffs are globally unique: \(F_2\) has a monotone branch after one; \(F_3\) has at most one crossing before one by its Bernstein sign pattern and rises strictly after one. Eliminating \(z\) at the two-step cutoff yields a cubic with unique real zero in the stated interval, and its derivative and resultant give the unique heterogeneity crossover. The strict rational witnesses independently verify the two regimes. The standard-library checker was run successfully, but finite tests are not used as the universal proof.

## Originality — PASS, with risk

The original Johnson–Zhang 2013 procedure already gives the last-iterate SVRG update, so this is not an algorithmic claim. Relevant full-text comparisons include Johnson–Zhang 2013, Xiao–Zhang 2014 (averaged/proximal), Sebbouh et al. 2019 (Free-SVRG), and Kahale 2020 (averaged quadratic Q-SVRG). Their results concern generic sufficient rates or different snapshots, not the exact short-epoch second-moment boundaries and their unique crossing. Semantic searches for equivalent formulas, cutoffs and stronger coverage did not identify an implying published theorem. Older specialized analyses of scalar random affine recurrences remain the main residual risk; search absence alone is not a novelty certificate.

## Value — PASS

The first random SVRG epoch has two updates; adding just one update is a natural minimal epoch-design comparison. Contrary to monotonic intuition, the larger epoch permits *either* larger *or* smaller mean-square-stable stepsizes depending on measurable curvature heterogeneity. The exact phase diagram, not isolated numerical endpoints, supplies a parameter criterion useful for understanding this tradeoff.

## Literature and limitations

Sources: Johnson–Zhang (2013), Xiao–Zhang (2014), Sebbouh et al. (2019), and Kahale (2020). Restriction: two nonidentical positive scalar component curvatures, uniform independent samples, last-iterate snapshots, and epoch lengths two or three. Unpublished/equivalent older scalar calculations cannot be ruled out. No independent scientific audit was performed.

Self-review: passed. Independent audit: not yet performed.
