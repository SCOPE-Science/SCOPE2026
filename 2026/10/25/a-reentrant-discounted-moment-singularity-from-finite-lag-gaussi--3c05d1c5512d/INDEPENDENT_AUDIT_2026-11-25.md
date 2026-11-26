# Independent mathematical audit

## correctness

PASS

For q=e^(-ah), r=1-q, v=σ²(1-q²)/(2a), the conditional OU increment has mean -rx and raw second moment v+r²x². Dividing by h gives the generator with drift -rx/h and squared diffusion (v+r²x²)/h; the standard deviation is globally Lipschitz and strictly positive. The finite-horizon moments obey m₂'=λ₂m₂+c and m₄'=λ₄m₄+6c m₂, with c=v/h, λ₂=-(1-q²)/h and λ₄=(-4r+6r²)/h=aF(ah). Linear growth gives the finite moments needed for localized Itô and passage to expectation. Both start at zero. Factoring the time convolution and using Tonelli gives exactly 6c²/[β(β-λ₂)(β-λ₄)] if β>λ₄. The forcing m₂(u) is strictly positive on u>0, so integration over a fixed subinterval in u gives m₄(t)≥C exp(λ₄t) for t≥1. This proves divergence at equality as well as below it. N=(1-q)(1-3q) is positive precisely when s>log 3, and H'=4s q(3q-1)<0 there, with H(log 3)>0 and H(∞)=-1. Thus F rises to one peak and falls to zero, giving the closed, singleton and empty divergence sets for the stated discounts. The invariant density from the speed measure is proportional to (1+r²x²/v)^(-(1+1/r)); the integrable speed measure for this nonexplosive irreducible diffusion gives a unique invariant probability. The beta-integral variance is v/(2r-r²)=σ²/(2a), and the fourth moment exists exactly for r<2/3, including logarithmic divergence at the boundary. Applying the same Laplace calculation to the true OU process replaces (λ₂,λ₄,c) by (-2a,-4a,σ²), giving the finite comparator. Independent 64-digit bisection of H and F-0.4 reproduced the peak and both quoted endpoints to their displayed precision.

## originality

PASS

The legitimate distinct claim is the sharp global reentrant lag/discount classification, including the unique interior maximum and closed divergence band. Lade's coefficients match exactly, and Pearson theory provides the stationary family and transient moment hierarchy. These furnish the fixed-lag growth exponent by specialization, but the strongest inspected prior statements do not evaluate the sign and extrema of that exponent over the lag/discount plane. The standard ingredients and their direct consequences are not separately credited as new.

## value

PASS

The model is the first nontrivial unbounded-reward test of a natural raw-increment reconstruction of a familiar diffusion in this comparison. It isolates a practical mathematical failure of reasoning from exact variance preservation or small-lag consistency: at positive discount there is an exact bounded interval of lags with infinite quartic evaluation, even though the true OU cost is always finite. Large-lag finiteness despite an infinite invariant fourth moment is also not recoverable from the stationary cutoff. The sharp threshold gives a benchmark in a setting where both mechanisms are exactly visible.

The dated certificate retains the supplied scientific assessment, sources and limitations.
