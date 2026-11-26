# Independent mathematical audit

## correctness

PASS

Condition on the endpoint W_H=y. Brownian bridge reversal in the damped sup norm couples to e^(−u/2)(y+B_u) with error bounded on [0,H] by O((|x_H|+|y|+|B_H|)/H); the tails beyond H vanish because of the exponential damping. Both statistics are Lipschitz in sup norm (constants 1 and 2), and the path includes 0 in its closure, so the endpoint is restricted to |y|≤r on the event. On bounded endpoint sets the scaled Gaussian density tends uniformly to 1/√(2π) for |x_H|=o(√H). Sandwiching in r works at continuity points of the integrated distribution function. For transfer, the critical ERW conditional drift is S_k/(2k); the martingale increment is a_{k+1}(ξ_{k+1}−S_k/(2k)), so Azuma with sum of squared increment bounds O(log ℓ) makes |M_ℓ|>H^(1/4) negligible. The cited conditional clock estimate with ℓ=ceil((log n)^16), r=1 and threshold H^(−4) gives O(H^(−8)) conditional error on the good starts. Independently, the same rate follows from embedding each increment by exit from a Brownian interval with endpoints −a_{k+1}(1+S_k/(2k)) and a_{k+1}(1−S_k/(2k)). Its time has conditional variance O(a_{k+1}^4) and mean a_{k+1}^2(1−(S_k/(2k))^2); Doob bounds the time martingale and the summed conditional mean deficit has expectation O((1+M_ℓ²)/ℓ). Brownian increments after T_ℓ are fresh given the start. The Brownian modulus on an O(H) horizon at mesh H^(−4) is ≤H^(−1) except with probability bounded by a polynomial in H times exp(−cH²); the grid has mesh O(ℓ^(−1)), and the coefficient error is O(ℓ^(−1/2)+L^(−2)) times a Brownian maximum bounded by H² outside a negligible event. The omitted early walk is bounded by ℓ/L and the damped extension is negligible. Thus these errors are genuinely o(H^(−1/2)) in probability of exceptional events, not merely o(1). Nearest-neighbour exit uses absolute maximum threshold 1 after dividing by L; cycle cover uses range threshold 1−1/L. H∼2 log L converts 1/√(2π) to 1/(2√π). Qin's integrable uniform bounds apply to both integer-time tails. Their integral equals the expected time divided by L². Tonelli gives E[J^(−2)] after integrating the profile; the integrals are finite by domination and positive because the limiting Brownian statistics are positive and finite almost surely. The comparison constants follow from M_y≤R_y≤2M_y. No numerical constant or all-time continuity is needed.

## originality

PASS

Credit only the exact critical rare-event profile and resulting first-order constants. Endpoint disintegration, the embedding, clock bounds and uniform integrability are prior tools. The closest inspected work explicitly leaves the critical tail limit and the normalized cover mean open. This is a bounded best-of-knowledge assessment.

## value

PASS

The exact constant resolves Qin's explicit critical cover-mean question. The profile also sharpens the exit result and identifies why expectation is governed by walks surviving to an unusual L² horizon rather than by the typical L²/log L fluctuation law; it gives usable integral characterizations beyond order bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
