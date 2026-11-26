# Independent mathematical audit

## correctness

PASS

For a Bloch mode with s=|v+w exp(ik)|>0 the loss identity makes every eigenvalue of the evolution generator strictly stable: equality of the real part to zero would force the lower component to vanish, which the coupling forbids for a nonzero eigenvector. As a separate check, write the integrated-survival Gramian as Q solving A*Q+QA=-I with A=-iH after removing the hopping phase. Its off-diagonal entry has imaginary part -1/(2s) and real part Delta/(gamma s). The lower diagonal entry is 2/gamma and its upper entry exceeds that by (Delta^2+gamma^2/4)/(gamma s^2). Parseval and Tonelli therefore give the exact integral with the stated normalization, including possible infinite mean. Complete absorption follows by dominated convergence because the one nondecaying momentum at criticality has measure zero. At v=w=h a finite polynomial must vanish at -1 to make the quadratic singularity integrable; division by (1+z) then reduces the integral to the squared quotient-coefficient norm divided by h^2. Multiplication by (1+z) on length L-1 vectors has Gram matrix with diagonal 2 and adjacent entries 1, whose simple largest eigenvalue is 4 cos^2(pi/(2L)) with the stated sine vector; Rayleigh–Ritz gives the value and uniqueness up to translation and phase, including L=2, while L=1 cannot cancel. Off the critical diagonal the normalized reciprocal denominator is a Poisson kernel centered at pi, of unnormalized mass 1/|v^2-w^2|. In the cancelling case the factored ratio is bounded by 4/(v+w)^2 using the exact denominator (v-w)^2+vw|1+exp(ik)|^2, yielding the finite pathwise limit. The form (2+Delta^2 I)/gamma+gamma I/4 gives the displayed optimized loss rate. The divergence asymptotic is read off the diagonal; exactly on it a noncancelling state's mean is already infinite.

## originality

PASS

The original walk and its dark momentum and localized dwell-time divergence are known. The inspected sources support those mechanisms but do not supply the normalized finite-packet critical mean-lifetime criterion together with the exact finite-block minimum and its uniquely selected preparation. The closest exact survival-operator and sine-envelope comparisons are for finite paths or endpoint-sink half-lines, with different operators or objectives. The pass concerns the combined exact coherent-preparation result in the infinite bulk-loss model and is subject to the stated search limits.

## value

PASS

The result separates eventual absorption from finite mean survival at a critical coupling in a standard dissipative model. It gives a concrete way to remove the lifetime divergence using only two adjacent sites, and a sharp support-budget law and unique state for every larger contiguous block. This resolves the preparation problem more precisely than identifying a dark mode or estimating the lifetime of a localized input.

The dated certificate retains the supplied scientific assessment, sources and limitations.
