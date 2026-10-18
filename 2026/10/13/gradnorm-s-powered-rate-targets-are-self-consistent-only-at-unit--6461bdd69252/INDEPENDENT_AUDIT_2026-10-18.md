# Independent mathematical audit

## correctness

PASS

For T positive task magnitudes and mean-one rates, sum actual G_i=T Gbar but sum targets=T Gbar M_alpha; summing signed residuals gives normalized L1 lower bound |1-M_alpha|. Explicit positive normalized G allocations x_i=s_i+1-M for M<1 and x_i=s_i/M for M>1 attain it and map to positive weights w_i=T(x_i/a_i)/sum(x_j/a_j). Strict Jensen forces heterogeneous M below/at/above one as alpha<1/=1/>1; ratio-preserving correction unique. Independent rational example T=3, rates(1/2,1,3/2),alpha=2 produced M=7/6 and attained floor 1/6 with weights (45,120,162)/109. Only instantaneous target compatibility claimed, not training failure.

## originality

PASS

Defining GradNorm paper supplies all ingredients but did not state a target total-mass residual, sharp minimization or unique ratio-preserving correction in sections read. Later direct-gradient balancing work is broader criticism, not evidence of these precise formulas. Independent Resultary searches yielded no implication-equivalent target-mass theorem; originality remains best-of-knowledge due potential informal rediscovery.

## value

PASS

This identifies an unavoidable mismatch in the defining targets of a widely used adaptive multitask loss and supplies a sharp quantifier and an algebraic mean-preserving repair. Although Jensen is elementary, the substantive object-specific incompatibility is meaningful; no downstream training improvement is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
