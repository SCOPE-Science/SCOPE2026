# Independent mathematical audit

## correctness

PASS

On the negative half-line direct convolution gives f(t)=e^{rt}/[(a+r)(b+r)]; on the positive half-line it gives [e^{−at}/(a+r)−e^{−bt}/(b+r)]/(b−a). The matching of f and f′ and the jump −1 in f″ imply that the third distributional derivative of the correlation product has masses −f(−T), −f(T) at −T/2,+T/2. Every term from the remaining piecewise exponentials integrates to a sum of smooth T-dependent coefficients times e^{±iωT/2}/(λ−iω). In the cell ω=((2n+1)π+φ)/T, |φ|≤π, derivatives in T or φ preserve the O(n⁻¹) bound on compact positive-delay bands: the phases depend only on φ, and ∂_Tω=−ω/T only costs one power of ω in the squared denominator. The ratio f(T)/f(−T) has slope 2r at 0. For r<a its derivative is the difference of two decaying exponentials, with the positive term decaying faster, so the ratio has one maximum and then decreases to zero, crossing 1 transversely once at positive T. For a≤r≤b the derivative is positive directly; for r>b the positive term already dominates at zero and grows faster. In a positive-frequency phase cell the normalized leading map is f(−T)e^{iφ/2}−f(T)e^{−iφ/2}; its derivative at (T*,0) is invertible as a real 2×2 matrix, with diagonal entries −f(−T*)ρ′(T*) and f(T*). On a small ball, composing the perturbed map with the inverse of that derivative gives the fixed-point iteration x↦x−J⁻¹F_n(x); uniform C¹ closeness makes it a contraction into the ball for large n. This proves one transverse zero with displacement O(n⁻¹). Away from that ball the leading term is bounded away from zero on the compact phase cell and delay band; this proves exhaustion or exclusion with the stated boundary qualification. Reality supplies the conjugate strings. For (2,3,1) the balance factors as (e^T−1)(e^T−3)=0. Formal assumptions allow r=a and r=b in the exclusion branch despite the title; no claim is made for delay tending to either endpoint of (0,∞). CHECK.py and its recorded output were inspected, not executed or used to infer exhaustion.

## originality

PASS

The supported distinct statement is the rate-dependent high-angular-frequency existence, local uniqueness and compact-band exhaustion/exclusion for this mixed-direction three-factor window. Published two-factor nonvanishing and the closest indexed high-frequency strings for a different window do not give that dichotomy. The mentioned repeated-rate subfamily is not credited as new; its cited coverage could not be independently located. This is not an absolute priority claim.

## value

PASS

The result turns a leading-order cancellation into a sharp existence and exclusion theorem for actual regular zeros of a natural exponential-convolution window. It identifies the mechanism by a simple rate inequality and localizes and enumerates the asymptotic branches on compact positive-delay bands. Distinguishing true transverse zeros from small Fourier values at approximate phases is substantive for ambiguity-zero questions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
