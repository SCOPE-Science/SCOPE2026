# Independent mathematical audit

## correctness

PASS

The image of a nondecreasing 1-Lipschitz map is an interval and idempotence forces it to be a clamp. For commuting f, the endpoint images x=f(a), y=f(b) belong to [a,b]; left exterior steps are free (2^u choices) iff x=a, right steps free (2^v choices) iff y=b, and the k interior binary steps with y-x ones contribute binom(k,y-x). The weighted sum gives C_n=(k+2)2^(k-1)+(2^u+2^v-2)2^k+(2^u-1)(2^v-1) for k>=1; k=0 gives 2^(n-1). At fixed k, C depends strictly convexly on 2^u+2^v. Uniform compositions u+k+v=n-1 have P(min>=j)=binom(n+1-3j,2)/binom(n+1,2), while C has log_2 C=n-1-min(u,k,v)+O(log n) uniformly; this proves the full CDF and expectation, not via finite sampling. Independently reconstructed 120 direct idempotent/commutation cases (n<=8) and matched all formulas.

## originality

PASS

Published contraction-semigroup results supply classification, rank, regularity and fixed-point counts, but their inspected statements neither impose fe=ef for each clamp nor derive an idempotent centralizer profile or the uniform-idempotent logarithmic CDF. Search found no mathematical implication covering all these consequences; originality remains best-of-knowledge.

## value

PASS

An idempotent centralizer is a canonical intrinsic invariant in a natural family of transformation monoids. The exact distribution across all clamps, placement extremizers, and nondegenerate random-idempotent limiting law add structural and probabilistic information beyond overall monoid element counts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
