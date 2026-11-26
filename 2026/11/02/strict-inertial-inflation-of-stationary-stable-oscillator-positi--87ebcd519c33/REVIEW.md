# Independent mathematical audit

## correctness

PASS

The stable linear drift has force-to-position impulse G_m=(exp(-λ_s t)-exp(-λ_f t))/Δ with positive decay rates. The stationary Lévy convolution exists, any initial deterministic contribution decays, and the position characteristic exponent uses I_m=∫G_m^α. The substitution u=exp(-Δt/m) gives the beta integral mΔ^(-α-1)B(a,α+1); the recurrence and the relations among a, m and Δ give the displayed gamma formula. At the repeated root G_mc=(t/m_c)exp[-γt/(2m_c)], so direct integration gives the stated critical value, also recovered from the gamma ratio. For 1<α<2 the log derivative of the gamma factor is positive by the frozen digamma integral and strict sinh inequality; a increases from 0 to infinity, with continuous endpoint scales. Larger dilation strictly increases absolute-value tails at positive thresholds, not the signed laws in stochastic order. Common-noise coupling yields an upper bound on W1 given by the difference of mean absolute values, which is also a lower bound by the triangle inequality. The Fourier moment integral (2/π)∫(1-exp(-s^α))/s² ds gives E|Zα|=2Γ(1-1/α)/π by parts. Independently expand the beta integral by subtracting 1 inside its integrand: B(a,α+1)=1/a-ψ(α+1)-γ_E+O(a). The pole term is Δ^(-α)/(αλ_s)=I0[1+(2α-1)δ+O(δ²)] for δ=κm/γ², and the finite term contributes -I0 α[ψ(α+1)+γ_E]δ. This gives exactly Rα and the reported linear W1 coefficient, positive by the strict log derivative at a=0. Read RESULT.md, VERIFICATION.md, check.py and the recorded 197-check output; the frozen script was not run. The finite evidence does not justify the universal claims; these apply only to the position marginal and the stated noise and mass range.

## originality

PASS

The supported distinct contribution is the evaluated harmonic invariant-position scale and its quantitative Wasserstein mass response, especially the explicit strictly positive first-order coefficient. The stationary impulse integral is already known. The sign inequality for the evaluated quotient is also implicitly covered by a classical Wallis-ratio theorem and is not credited as a new inequality. Neither this special-function result nor the known oscillator integral or general bound gives the explicit coefficient without evaluating and expanding the singular small-mass scale. No inspected source gives that quantitative conclusion.

## value

PASS

The harmonic model is a natural benchmark for the invariant-measure Smoluchowski–Kramers bound. An exact, strictly positive linear coefficient distinguishes its error from the general m^(1/α) estimate and from mass-independent Gaussian behavior. The formula across all nonoscillatory masses additionally quantifies a position-marginal comparison, not just kinetic energy or qualitative damping regimes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
