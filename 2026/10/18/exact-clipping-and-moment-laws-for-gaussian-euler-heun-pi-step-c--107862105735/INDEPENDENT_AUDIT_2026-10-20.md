# Independent mathematical audit

## correctness

PASS

With common Gaussian increment, the drift-corrected Heun second-stage difference gives x_E−x_H=−λ²h²x/2+(λ g h^(3/2)/2)Z exactly, so its scaled squared norm is noncentral χ²_d(Δ), Δ=λ²h||x||²/g². Rechecked the inverse monotone transformation for U=C ε^(−k), both clipping atoms, derivative of Q(v) for the interior density, Poisson-mixture small-ball coefficient (leading e^(−Δ/2) Q^(d/2)/(2^(d/2)Γ(1+d/2))), layer-cake integral threshold q=d/k, and Cramér rate for sample mean of squared Gaussian coordinates. A separate numerical implementation checked the exact affine discrepancy and noncentral CDF for d=1,2,4,8, but finite simulation was not used to prove tails or limit laws. Raw, non-clipped moments diverge at threshold; clipped ones never do.

## originality

PASS

Kemperman–Ambrogioni describe the shared-noise embedded stochastic Euler–Heun PI controller in a general diffusion sampler. Ilie–Jackson–Enright establish PI recursions and stability for adaptive Milstein SDE integrators, but their inspected Section 3.1 does not derive this exact conditional noncentral chi-square law, its moment threshold, or cap-atom large-deviation rates. The Gaussian and Cramér components are classical and explicitly not claimed as new. The full Kemperman–Ambrogioni paper remained inaccessible and authorized access was safety-blocked; its possible overlap is a substantial documented priority risk, not proof of noncoverage.

## value

PASS

One-step gain distributions quantify extreme trial-step proposals and precisely separate an uncapped heavy-tail pathology from actual bounded implementation. Sharp per-dimension power moments and cap probabilities are natural design diagnostics for a published adaptive PI rule and OU benchmark; these exact facts could be independently useful despite not proving adaptive solver convergence. The value does not rest solely on rebranding an elementary Gaussian norm as noncentral chi-square.

The dated certificate retains the supplied scientific assessment, sources and limitations.
