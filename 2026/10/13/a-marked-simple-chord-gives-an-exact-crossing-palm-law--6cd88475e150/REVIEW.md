# Review

## Correctness

PASS. Conditioning a fixed adjacent pair to be matched leaves a uniform perfect matching on the remaining endpoints, and a simple chord contributes no crossings. This gives the full Palm identity for arbitrary integrable \(f\), not merely a first-moment calculation.

Deleting the chord incident to a distinguished endpoint from a uniform size-\(n\) diagram leaves a uniform size-\(n-1\) diagram and can only remove crossings. This independently proves the stochastic-order input used for all monotone transforms.

The covariance and simple-chord variance are then elementary exact consequences. The exact crossing variance used for the correlation is explicitly stated in the inspected full primary manuscript and is also reproduced by the package checker through size \(7\).

## Originality

PASS, with a bounded residual risk from older generating-function literature. The closest inspected full paper is Paguyo's treatment, because it analyzes both the crossing count and the simple-chord count in the same manuscript. Its crossing section gives marginal crossing moments and its simple-chord section gives a Poisson approximation via size-bias coupling; the inspected text does not state a mixed covariance, a marked-simple-chord deletion law, or an exact correlation.

Acan's archive-era paper defines simple chords, studies chord lengths and crossing degrees, and develops uniform growth models, but its inspected statements do not give the total simple-chord/total-crossing mixed law.

Flajolet--Noy is broader classical background for crossing moments and component asymptotics. Only abstract-level material was accessible for that source, so it is retained as a residual risk rather than being declared non-covering from snippets alone.

## Value

PASS. Crossings and simple chords are the two random chord-diagram statistics singled out in the closest modern probability treatment because they exhibit Gaussian and Poisson marginal regimes. The exact Palm identity explains their dependence at finite \(n\) and gives a closed-form correlation without a bivariate generating function.

The identity for every monotone endpoint transform is structurally stronger than one covariance number and is reusable for other crossing functionals. The exact \(n^{-1/2}\) correlation decay quantifies how a local isolated-chord statistic interacts with a global intersection statistic.

Self-review: passed. Independent audit: not yet performed.


Exact replay: `VERIFY_OK matchings_checked=146599 moment_checks=30 palm_checks=86 stochastic_checks=62 correlation_checks=6`.
