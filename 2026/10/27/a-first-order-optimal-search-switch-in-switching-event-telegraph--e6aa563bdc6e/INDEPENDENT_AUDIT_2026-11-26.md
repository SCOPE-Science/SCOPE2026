# Independent mathematical audit

## correctness

PASS

Poisson marking produces independent reset and flip clocks of rates r=λp and κ=λ(1−p). The no-reset backward system has spatial exponents ±√(s(s+2κ))/v; boundedness to the left selects the positive exponent, and only the target-facing mode is required to have boundary value 1 at L. Thus the no-reset hit transform from (0,+v) is φ(s)=exp[−(L/v)√(s(s+2κ))]; κ=0 is ballistic. A trial until hitting or the first reset lasts on average (1−φ(r))/r and succeeds with probability φ(r)>0, giving (1−φ(r))/(rφ(r)). The κ=λ no-reset transform at s↓0 gives an infinite mean; also F_q(p) diverges as p↓0 for each q>0. For a=√(p(2−p)), b=qa, h=(1−p)/(2−p), the derivative has sign h−ψ(b), ψ=(1−e^(−b))/b. Stationarity parametrizes p=(1−2ψ)/(1−ψ) strictly increasing in b>b₀ and q=Q(b). Direct differentiation gives bQ'/Q=1−AD/(BC) with A,B,C,D as in the proof. A/B strictly decreases by the weighted-average derivative of t/(e^t−1); (D/C)'=−A/C²<0. Both factors are positive and H=AD/(BC) goes from infinity to zero with H'<0, so Q has one nondegenerate minimum q_s and diverges at both ends. At fixed p the derivative sign expression strictly increases with q, so relative to the stationary curve it is negative outside the two roots and positive between them. At the fold the derivative has a quadratic zero (the critical q as a function of p has a nondegenerate minimum, and ∂_q(h−ψ)>0), giving a stationary inflection. The upper stationary point is a strict local maximum, never an endpoint tie. Along the smooth lower branch the derivative in p of the objective ratio to p=1 vanishes, and its log derivative in q has sign m(qa)−m(q)<0 with m(z)=z/(1−e^(−z)) increasing. The ratio tends from a value strictly above one at the fold to zero (lower branch O(q²), endpoint exponential), hence crosses exactly once and the switch is discontinuous. The lower b tends to b₀, so q²p→b₀²/2 and F_q(p)/q²→2(e^b₀−1)/b₀². I independently checked the displayed decimal constants by standard-library Decimal bisection in /workspace/branches/replay_telegraph.py (run with python3); q_s=2.9938108746030780388…, q_c=3.7295732243919928885…, p_c=0.1204656388350102878…, objective coefficient 3.0882773047417401791…. These non-interval numerical checks are supplemental; the proof gives exact thresholds by uniqueness, and the frozen script was inspected, not executed.

## originality

PASS

The supported advance is the complete finite-distance fold and unique discontinuous global optimum at fixed r+κ for deterministic favorable relaunch, not the Bernoulli telegraph model, standard first-renewal mean or Brownian asymptote. The strongest same-model primary source gives position laws and scaling, not this first-passage optimization. The strongest readable first-passage optimization treats a different reset mark and varies reset rate at fixed reduced target distance. No inspected result implies the frozen fixed-sum phase diagram; full-text access limits are recorded separately.

## value

PASS

The total-event constraint models a single opportunity clock and exposes an actual design tradeoff absent from varying an independent restart rate. The proof distinguishes onset of a metastable interior solution from its true global crossover, gives both sharp thresholds and the discontinuity, and links the long-distance optimal reset scale to diffusive search. These results answer more than an MFPT evaluation or a sampled optimization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
