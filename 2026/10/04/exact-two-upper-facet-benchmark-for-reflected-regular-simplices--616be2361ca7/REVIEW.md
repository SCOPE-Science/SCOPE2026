# Independent mathematical audit

## correctness

PASS

Starting from Horváth's exact two-facet prism expression and visibility interval, convexity in the second coordinate reduces the maximum to the two endpoints. The upper endpoint is at most \(1-1/n^2\). The lower endpoint becomes the Rayleigh quotient of the displayed \(2\times2\) symmetric matrix, whose largest eigenvalue is exactly the stated radical after direct characteristic-polynomial calculation. The positive eigenvector satisfies the strict second-facet visibility inequality, and the explicit normal construction makes all other facets non-upper, so the relaxation is realizable. Independent eigenvalue calculations for \(3\le n<30\) reproduce the closed expression, while the bundled checker verifies the same geometry through \(n=400\). The finite checks corroborate rather than replace the analytic proof.

## originality

PASS

Originality passes for the all-dimensional two-upper-facet chamber optimum. Horváth's primary paper supplies the prism formula and visibility constraints and explicitly optimizes the two-upper-facet case in dimension five while leaving the higher-dimensional global problem open. The audited result exposes the dimension-\(n\) Rayleigh-quotient matrix, proves feasibility of its maximizing eigenvector for every \(n\ge3\), and obtains the closed all-dimensional benchmark. A related SCOPE six-simplex result covers only one specialization, not the theorem's full parameter range.

## value

PASS

The chamber is singled out by the primary source's facet decomposition and contains the published five-dimensional global optimizer. Its exact all-dimensional optimum gives a concrete lower benchmark for the still harder global problem, shows the first dimension where this chamber beats the old \(2n\) configuration, and gives a clean asymptotic ratio. This is a motivated structural subproblem, not an arbitrary restriction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
