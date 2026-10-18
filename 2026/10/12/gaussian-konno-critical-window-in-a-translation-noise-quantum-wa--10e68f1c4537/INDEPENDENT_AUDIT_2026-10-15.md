# Independent mathematical audit

## correctness

PASS

The channel consists of U_θ with probability q_t and spatially homogeneous global translations R,R^{-1} with p_t/2 each. Since R commutes with U_θ, every t-step Kraus word becomes a translation times U_θ^k; summing independent Bernoulli choice counts yields exactly X_t =d Q_{K_t}+S_{t−K_t}, K_t∼Bin(t,q_t). Independently built the full mixed-state channel on a 21-position periodic embedding with four steps, angle 0.7 and p=0.3; channel position probabilities match the explicit convolution to maximum error 5.55×10^−17. The coherent Konno limit for the fixed specified coin phase, binomial K_t concentration, classical CLT conditional on K_t, and |Q_k|≤k prove the q_t√t→0,→λ>0,→∞ regimes. Integrating the standard Konno density gives Var V=1−sinθ and κ4 V=−(1/2)(1−sinθ)^2(4−sinθ), strictly negative. This validates the limiting convolution and non-Gaussianity, not a local density limit or monitored first returns.

## originality

PASS

The same channel appears in Štefaňák et al but their inspected source analyzes monitored return observables, not this unmonitored position crossover; the pure Konno limit is known and expressly credited. Earlier measured-restart quantum-walk crossovers have different channels; general commuting-Kraus work may implicitly encode the random-time factorization but no inspected earlier full critical-window theorem established this triangular-array convolution.

## value

PASS

The exact channel-to-random-time convolution converts a natural translation-noise quantum stochastic walk into an analyzable mixture and identifies a sharp Gaussian/ballistic transition with an explicit non-Gaussian critical law. It is a motivated scaling-classification boundary of an actual published model, not simply changing a sample size in an established CLT.

The dated certificate retains the supplied scientific assessment, sources and limitations.
