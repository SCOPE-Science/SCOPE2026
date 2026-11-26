# Independent mathematical audit

## correctness

PASS

For one preselected port and distinct inputs, all permutations carry the same product of spatial amplitudes. Squaring the internal tensor symmetrization, normalized by 1/√(N!), leaves the Gram permanent. It is positive by testing against a tensor power of a vector having nonzero overlap with each internal input. Squared moduli of a complex Haar row are independent unit exponentials divided by their sum, so Dirichlet integration gives the Mellin formula and its first two logarithmic derivatives. For fixed t>−1 the gamma-ratio term in the scaled cumulant is ∫₀ᵗ[log m−ψ(m+Nu)]du. Using ψ(x)=log x+O(1/x) uniformly here gives −∫₀ᵗ log(1+u/α)du, zero at α=∞. At t=−1 the limiting cumulant diverges, and its right derivative tends to −∞ even for α=1. The effective domain has a neighborhood of zero, and the limiting cumulant is lower semicontinuous and essentially smooth, so Gärtner–Ellis gives a full good LDP. Strict positivity of F″ follows from ψ₁(1+t)>1/(1+t); its derivative at zero is −γ. Stirling gives Fα(t)=t log α−(α−1/2) log t+O(1) for finite α, proving infinite rate at and above the upper endpoint. Independently, expanding the exact log-Mellin transform at t=s/√N after subtracting the exact log mean yields (s²/2)[ψ₁(1)−Nψ₁(m)]+O_s(N⁻¹ᐟ²): the third derivative is O(N) there using ψ₂(x)=O(x⁻²) at large x and m≥N. This proves the asserted CLT including α=1 and ∞. Finally Z_N→F′α(0), and the arithmetic normalization contributes Fα(1). The stated gap is Fα(1)−F′α(0)>0 by strict convexity and Fα(0)=0. The internal-state factor cancels exactly. The uploader's finite Python check was inspected, not executed; it cannot establish the asymptotic claims.

## originality

PASS

The distinct supported contribution is the explicit ratio-dependent law for a selected subset of a Haar row, in particular 1<α<∞, and the corresponding quantitative separation of the fixed-port optical probability from its own Haar average. The factorization and mean, the m=N large-deviation law in classical guise, and the dilute Cramér endpoint are not independent novelty. The strongest retrieved classical theorem concerns a geometric-to-arithmetic mean with the denominator taken over the same coordinates; it does not already include the fluctuating selected mass from the full row.

## value

PASS

Fixed-port full bunching is a naturally measured optical event. The exact exponent distinguishes what a typical Haar interferometer does from what the familiar Haar expectation suggests, uniformly from dense to dilute scaling, and identifies when a geometric-mean approximation that drops the selected mass would give the wrong tail. The explicit finite-ratio rate and strict exponent, invariant under product-state distinguishability after normalization, are useful quantitative information beyond fitting a simulation, restating the mean or quoting the same-coordinate CLT.

The dated certificate retains the supplied scientific assessment, sources and limitations.
