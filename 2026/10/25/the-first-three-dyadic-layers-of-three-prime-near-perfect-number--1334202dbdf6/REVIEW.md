# Independent mathematical audit

## correctness

PASS

Multiplicativity gives Δ=σ(n)−2n=H(p+q+1)−pq with H=2^{a+1}−1. Δ>0 yields p²−2Hp−H<0, hence p≤H+floor(sqrt(H(H+1))), namely 6,14,30. If p<H, Δ>2^a p forces q|Δ and thus q|H(p+1), so q≤H(p+1); if p>H, positivity forces (p−H)q<H(p+1); p=H yields an impossible extra factor 2 in Δ. These inequalities bound all p,q, so finite enumeration is exhaustive. Independent implementation enumerated every prime pair under the proved bounds before applying divisibility (7,66,382 pairs for a=1,2,3) and found exactly the five displayed pairs; each σ and omitted divisor checked by direct integer arithmetic. The finite checker has proved bounds, not an arbitrary cutoff.

## originality

PASS

No located exact or dominating covering result after primary-paper and Resultary comparisons; all four named comparison checks and residual priority risks are separately documented.

## value

PASS

The proposed result is a complete naturally filtered three-prime-support slice of an established finiteness question, with a sharp first nonempty dyadic layer and proved exhaustive upper bounds. It supplies a genuine classification rather than a finite scan or new-example claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
