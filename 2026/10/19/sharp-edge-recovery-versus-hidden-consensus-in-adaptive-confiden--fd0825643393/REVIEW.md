# Independent mathematical audit

## correctness

PASS

The underlying graph stays K_n. While its one ineffective edge is absent, the update is the self-looped averaging matrix for K_n minus that edge. If M is the maximum other-edge disagreement, opposite endpoints differ by at most 2M via a mediator. To compare an updated endpoint with an updated mediator, subtract the average over n opinions from that over n−1 opinions. The numerator over n(n−1) sums n−1 disagreements with the omitted endpoint: n−2 are at most M and one at most 2M, so the new ordinary-edge gap is at most M/(n−1). Mediators share the same updated opinion. Since receptive bounds do not decrease, this proves invariance until recovery. Meanwhile subtracting endpoint updates divides their positive gap by n−1 each step, and the absent bound scales by δ. Strict receptiveness requires ((n−1)δ)^t>d/c₀, giving no finite recovery at or below threshold (including δ=0) and the asserted first integer T above it, even when the logarithmic ratio is an integer. Endpoint gaps up to and including T remain nonzero, so consensus is first at T+1. Loop-inclusive degrees n−1 at the endpoints and n elsewhere give invariant L for the missing-edge update. Diameter goes to zero if the graph never completes. Endpoint and mediator mean difference contracts with signed eigenvalue λ=−(n−2)/[n(n−1)]; subtracting that degree-weighted mean from the ordinary mean gives coefficient 2(n−2)/[n(n²−2)] times this difference. Since the final consensus opinion is the ordinary mean at T, this proves the closed formula. An exact boundary example with x=(0,1/4,1/3,3/5), c₀=1/2, δ=2/5 has equal gap and confidence 1/5 at t=1 (still absent), recovery at t=2, and common value 17857/60480 at t=3. The divergence of T at the threshold requires d>c₀, as stated.

## originality

PASS

The exact same-model literature establishes qualitative stabilization and observes hidden consensus, not the exact stratification and consensus-value formula. Distinct catalogue results overlap the threshold substantially, including one nearly identical K_n theorem and a broader twin-pair threshold. They are documented as actual mathematical coverage of those components, not credited as distinctions and not treated as evidence of earlier priority. The submitted result also determines the exact nonsymmetric finite-time consensus opinion, which none of the compared statements supplies. That is a supported distinction rather than a claim that hidden consensus or even the cutoff is unique across the catalogue.

## value

PASS

The one-gap clique is the simplest complete-network family that isolates a mediator mechanism rather than merely observing that a simulation converges. Exact timing separates network recovery from opinion agreement. For nonsymmetric initial means the closed finite consensus value quantifies the effect of the switching time and the sign of the pre-switch mode, unlike an assertion of consensus alone. It also identifies the limiting agreement as recovery is delayed arbitrarily near the cutoff.

The dated certificate retains the supplied scientific assessment, sources and limitations.
