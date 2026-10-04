# Same-model review

## Correctness
PASS. On each uniform cell, the substitutions \(x=(j+s)/n\), \(u_n=n^{-1/3}p_j(s)\), and \(u_n'=n^{2/3}d_j\) give the exact cell energy \(n c_j\). The first-cell constant is exactly \(c_0=8/105\). For \(j\ge1\), concavity and the linear-interpolation remainder yield \(c_j=O(j^{-6})\), proving convergence of \(C\). A uniform Taylor expansion gives \(c_j=rac1{196830}j^{-6}+O(j^{-7})\), and summing the tail gives the stated \(-rac1{984150}n^{-4}\) correction. The packaged checker independently evaluates the exact polynomial cell formula at high precision.

## Originality
PASS, with a bounded residual literature risk. The broad fact that Lipschitz approximants converging to the singular minimizer can have energy tending to infinity is prior art and is not claimed. Pereira–Cruz–Torres publish rounded exact-energy values for the same nodal polygonal curve on several meshes, but the inspected full text gives neither an exact cell formula nor a rate or asymptotic constant. Ball–Knowles treat the same Manià example and standard piecewise-linear finite elements, but their inspected statements are qualitative divergence/failure and quadrature analysis. Ball's 2001 survey additionally computes the exact \(8/(105h)\) energy of a boundary-layer test function that is linear only on the first interval and equal to the singular minimizer afterward; that first-cell fact is therefore prior-covered. Feng–Schnake treat enhanced finite elements to overcome the gap and likewise do not state the full uniform nodal-interpolant asymptotic. Targeted semantic searches for the nodal-interpolant linear law, the coefficient, and the \(j^{-6}\) cell tail found no implication-equivalent result.

## Value
PASS. Uniform nodal interpolation of the known exact minimizer is the most direct geometric finite-element approximation, so its failure is a natural diagnostic rather than an arbitrary parameter slice. The exact law explains why visual convergence and energy convergence move in opposite directions and quantitatively explains the published PLFOpt table. The previously known first-cell obstruction accounts for almost all of the coefficient, while the new full-cell summation identifies the precise additional contribution and sharp tail. This gives a sharp benchmark for discretizations intended to cope with the Lavrentiev phenomenon.

## Closest literature and limitations
The closest inspected literature is Pereira–Cruz–Torres, arXiv:1003.0934v1, especially Example 4.2 and Table 3; Ball–Knowles, doi:10.1007/BF01396748; Ball's 2001 survey chapter on singular minimizers; and Feng–Schnake, arXiv:1610.03111v1. The result does not cover nonuniform meshes, discrete quadrature energies, or finite-dimensional minimizers. An unindexed thesis or note could contain the same asymptotic.

Same-model review: passed. Independent audit: not yet performed.
