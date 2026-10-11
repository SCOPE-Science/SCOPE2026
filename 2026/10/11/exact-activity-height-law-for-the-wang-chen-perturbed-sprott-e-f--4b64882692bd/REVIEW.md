# Same-model scientific review

## Correctness
PASS. The claim follows from exact generator identities for the coordinate functions and an exact square identity for \(\dot z\). Compact support gives bounded complete trajectories on the invariant support, which makes the variation-of-constants formula prove \(y\ge0\). The equality case \(A=0\) is not inferred from a finite computation: it forces \(x=1/4\) on the support, stationarity forces \(y=1/16\), and invariance then forces \(z=-16a\). The dependency-free checker independently replays the polynomial identities and equilibrium substitution.

## Originality
PASS with residual indexing risk. The introducing Wang–Chen preprint/article, the coexistence paper, the 2020 KCC study, and Chen–Liu–Wei–Feng’s global/KCC paper were inspected for statements with the same objects and parameters. Their results concern equilibrium stability, numerical Lyapunov data, coexistence and basins, dynamics at infinity, and Jacobi/KCC stability. None of the inspected material states or implies the exact stationary activity–height law, the \(y\)-weighted probability formulation, or the unique zero-activity characterization. Targeted published-result searches using the DOI, equations, moment-law aliases, and activity/height language returned only analogous laws for different vector fields. A nonindexed prior derivation remains possible.

## Value
PASS. The Wang–Chen system is specifically used as an example where a stable point attractor coexists with non-equilibrium periodic or chaotic dynamics. The new law gives a source-specific exact statistic that distinguishes the equilibrium from every non-equilibrium compact recurrent state and continuously ties the displacement of a positive \(y\)-weighted height to a dynamical activity \(\int \dot z^{\,2}\,d\mu\). At the documented \(a=0.01\) multistability parameter it separates the point value \(-0.16\) from every periodic or strange stationary state without relying on a finite Lyapunov computation. This is a motivated structural invariant of the reported multistability, not an arbitrary parameter slice or a table recomputation.

## Closest literature and limitations
The closest same-system sources are Wang–Chen’s introduction of the flow, Sprott–Wang–Chen’s coexistence study, Gupta–Yadav–Gupta’s KCC analysis, and Chen–Liu–Wei–Feng’s global/KCC analysis. The theorem assumes compactly supported invariant measures; it neither establishes attractor existence nor validates a particular numerical attractor. It concerns a \(y\)-weighted mean of \(z\), not the ordinary mean. Search coverage is finite, so an unindexed prior statement remains a residual originality risk.

Same-model review: passed. Independent audit: not yet performed.
