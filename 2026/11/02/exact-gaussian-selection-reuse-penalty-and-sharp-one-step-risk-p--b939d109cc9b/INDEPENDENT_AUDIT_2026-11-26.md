# Independent mathematical audit

## correctness

PASS

The orthogonal sum/difference rotation makes V± independent with means (a±b)/√2 and common variance σ². Row one is selected exactly when their signs agree, giving probability (1+Q_+Q_-)/2. The untouched coordinate contributes the same squared error under reuse and split, and the split correction contributes σ² independently. For reuse, writing E± for the centered rotated noises gives ε₁²−ε₂²=2E_+E_−, so the excess selected square is E[E_+ sgn(V_+)] E[E_− sgn(V_−)]. Each centered sign moment is 2σφ(μ/σ); multiplying gives (2σ²/π)exp(−r²/(2σ²)). For the sharp bound set w=(a+b)²/2 and g(w)=√w erf(√w/(√2σ)), so H=g(w)g(r²−w). The logarithmic derivative of g at w>0 is (1+T)/(2w), where T is the reciprocal of the displayed integral over [0,1] that strictly increases with w. Thus log g is strictly concave: the unique maximum is at w=r²/2 (ab=0) and the only zeros are the endpoints (|a|=|b|). The best-orientation deficit is the difference of a decreasing exponential and a strictly increasing unbounded function of r/σ, with opposite signs at zero and infinity. This proves the unique crossover and equality cases, including the positive penalty at r=0.

## originality

PASS

The new claim is the exact same-reading minus split correction cost in the two-row absolute-residual selection model and its competition with the sharp directional split gain. Greedy row choice and Gaussian order-statistic risk are established; the inspected results do not supply the radial exponential excess or the resulting one-update boundary for this observable.

## value

PASS

This minimal consistent system isolates a concrete selection-versus-update tradeoff: an orientation-independent penalty from reusing the observation competes with a sharp orientation-dependent benefit from choosing the row adaptively at all. The exact phase threshold demonstrates a whole low-signal neighborhood where even the best-oriented greedy reuse loses to uniform, and equal-magnitude starts lose at every signal scale. This is a motivated sharp finite boundary, not merely an isolated numerical counterexample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
