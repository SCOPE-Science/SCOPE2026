# Independent mathematical audit

## correctness

PASS

Read actual RESULT.md from Git blob 5767935f94e01a94eccf4d3bd9d570faa2ce6df1 and packed parity checker. At fixed E=2n the parity-matched Hermite polynomial has decaying leading term x^n e^(−x²/2), while ∂E W has the exponentially growing x^(−n−1)e^(x²/2) term. Their ratio is C_n a^(2n+1)e^(−a²), C_n=2^(n+2)/(sqrtπ n!). The Robin logarithmic derivatives are −a+n/a+O(a^-3) and a−(n+1)/a+O(a^-3); ratio −1+2γ/a+O(a^-2). Thus Dirichlet and Robin roots give width 2C_n a^(2n+1)e^(−a²)(1−γ/a+O(a^-2)) for each fixed n and fixed real γ. Sturm–Liouville edge interlacing and simple nearby roots isolate the unique band; the proof does not cover n or γ increasing with a. Independent high-precision direct Kummer root solve at a=4, γ=0.7, n=0,1,2 gave width-to-asymptotic ratios 1.02187, 0.94590 and 0.81136 (finite corroboration only).

## originality

PASS

Best-of-knowledge PASS for the fixed-n/fixed-γ tunnelling prefactor and relative γ/a correction. The exact same model is treated in Gibbons–Veselov, but its full inspected §4–5 derives spectral-edge equations rather than the asserted fixed-coupling asymptotic; the authors explicitly identify this regime as needing precise asymptotics. No indexed Resultary analogue covered the operator, scaling and both coefficients together.

## value

PASS

The first fixed-coupling low-band tunnelling constant and its first γ-dependent relative coefficient resolve a specifically identified spectral asymptotic question in the exact periodic cusp-plus-delta model; each n mode has a physically meaningful exponentially narrow band. Unlike routine numerical band-gap checks, the coefficient distinguishes boundary strength from oscillator geometry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
