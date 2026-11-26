# Independent mathematical audit

## correctness

PASS

In branch mass coordinates for A_1 through A_(n−1), column 1 of the open transfer matrix consists of a_j, and column j>1 shifts mass to j−1. This verifies the finite Perron polynomial directly: λm_j=a_j m_1+m_(j+1), with m_n=0, implies Σa_j λ^(−j)=1. The root above 1 in z=1/λ is unique; summation by parts gives S_n=Σk^(−θ)−n^(1−θ), with the sum up to n. With δ=θ−1 the integral I=log(n) Ψ(δ log n) diverges for δ→0, and e^(−c)/I≤|δ|+1/log n for either sign (by e^v−1≥v). Thus S_n/I→1 and nγ≤e^(−c)/S_n→0. The power-series remainder relative to γ S_n is bounded by nγ exp(nγ)/2, proving the leading result without bounded c. For bounded c, subtract the integral from the sum cell by cell: the discrepancy series is locally differentiable at δ=0 with summable derivative, so S_n=log(n) Ψ(c)+γ_E−e^(−c)+O_C(1/log n). The exact second moment is O_C(n) by a_k≤θk^(−θ−1), giving relative exponential remainder O_C((log n)^(−2)). This establishes the stated coefficient, error and continuous c=0 limit. The proof concerns the finite branch spectral rate, not arbitrary survivor distributions.

## originality

PASS

The supported distinct result is the joint, all-sequences leading equivalent and the uniform bounded-window first correction for the true finite-matrix spectral root. Knight–Munday already give the root equation, the fixed-parameter asymptotics and the harmonic denominator at θ=1; those are not credited. The strongest apparent coverage, Bonanno–Tikekar's claimed exact induced-to-original rate formula instantiated on the identical branch model, is not an identity for that root. It gives the same near-critical coefficients as an approximation, but transferring those to the actual root requires accuracy estimates not provided by that exact identity. Thus no verified prior implication supplies the moving-parameter result.

## value

PASS

The finite/infinite invariant-measure boundary makes this joint limit natural. It quantifies the failure of interpolating the two fixed-parameter limits, gives relative control even when the scaled rate vanishes or diverges, and distinguishes the finite-hole correction from a mere replacement of the harmonic series by an integral. The proof provides accuracy control for the actual clock-time spectral observable, not just the induced rate divided by mean return time.

The dated certificate retains the supplied scientific assessment, sources and limitations.
