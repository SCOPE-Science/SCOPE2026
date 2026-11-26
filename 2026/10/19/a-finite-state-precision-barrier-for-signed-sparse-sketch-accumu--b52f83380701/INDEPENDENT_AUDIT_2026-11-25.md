# Independent mathematical audit

## correctness

PASS

Put h=1/sqrt(ζ) in {1,1/2}. Every jh for |j|≤2048 is representable. At the boundary the outward exact sum is the midpoint between ±2048h and ±2050h, and the former encodes the even low significand bit; inward updates are exact. Thus the scaled walk clips at ±2048 for any ordering. A separate exhaustive binary16 check of all 16388 state-direction cases matched this rule. Summing squares gives the pointwise ceiling, and assigning at least 2048 positive updates to each bucket in each layer attains it for N≥2048b. The strict N inequality ensures lower-embedding failure without any probability estimate. For the exact sketch, diagonal terms sum to N and unordered signed collisions have coefficient 2/ζ; distinct terms are orthogonal because some independent fair sign appears only once. There are ζ binom(N,2) terms each of second moment 1/b, giving 2N(N−1)/m and the stated Chebyshev bound. For the limiting law, conditional on the hashes and with sign-blind processing order, the bucket sign strings use disjoint independent signs. The clipped chain is symmetric, irreducible and aperiodic thanks to endpoint self-loops; one inward update exits an endpoint, so saturation is not absorption under fair signs. Each count is Bin(N,1/b); the minimum tends to infinity in probability for fixed m, and a sum of the individual conditional total-variation errors bounds the product error. This proves joint convergence despite dependent counts within layers. Finite support permits expectation convergence, and the exact uniform second moment of the scaled integer state is 1398784. Replay: compare RN binary16 serialization of (j±1)h against h·clip(j±1) for every allowed j and both h, then apply the bounded-state chain and collision expansion; the frozen script and stored output were inspected, not executed.

## originality

PASS

The distinct claim is the sharp absolute binary16 energy ceiling and consequent certain rank-one distortion in the same signed-sketch setting as the finite experiments, quantified further by its joint product-uniform limit. Standard midpoint stagnation, reflected-chain equilibrium, and exact arithmetic sketch moments are not claimed independently new. The b=2 exact Gram law is already covered more strongly by an earlier record.

## value

PASS

This supplies a concrete failure witness on the all-ones equal-leverage direction, for a specified sketch actually used in the motivating GPU study. In a regime with real-arithmetic norm preservation at high probability, it shows certain lower-norm failure without skewed leverage or overflow. The sharp ceiling separates a discrete accumulator constraint from the ordinary collision variance, and the joint stationary law predicts the scale of the asymptotic rounded energy rather than just warning that errors may grow.

The dated certificate retains the supplied scientific assessment, sources and limitations.
