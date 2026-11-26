# Independent mathematical audit

## correctness

PASS

In the stated normalization each translated window fits in an interval of length q, so Fourier Parseval gives exactly q times the multiplier P_n(x)=Σ_k B_n(x−k)^2. Partition of unity and finite overlap give a uniform positive lower bound. In the Fourier calculation, the partial-fraction coefficients are the Taylor coefficients of (a−u)^(−n) at u=0 and their reflections at u=a. The odd inverse powers vanish with centered cutoffs; the paired j=1 term has an integrable tail and the change of cutoff center has vanishing error. The remaining even terms are positive with the overall sign (−1)^n. The positive Gamma mixtures of geometric cosine sums decrease strictly on the half-period, giving the asserted parity switch and only extremal classes. For m=1, the sharp interior bound for h follows from sin|x|≥2|x|/π on |x|≤π/2 with x=u−π/2; off [0,π], sin²u≤min(dist(u,[0,π])²,1) gives the strict gap. The log curvatures give c_0∼√(3/(πn)) and |c_1|∼(4/π²)^n/√(πn(1−4/π²)); the odd-harmonic remainder is O(3^(−n)) relative to c_1. The endpoint gap is four times |c_1| to leading order, giving the stated coefficient. RESULT.md, VERIFICATION.md and CHECK.py were inspected. The finite rational tests reported in the package were not rerun and are not needed for the analytic all-order argument.

## originality

PASS

The supported distinct contribution is the explicit all-order parity-extremum analysis and sharp conditioning law in the painless regime, not the classical diagonalization, integer-oversampled frame existence, or the second-order endpoint example. The related half-density record has a different large-order regime. No inspected source supplies the combination of the explicit extremal classes and the sharp exponential prefactor in q≥n.

## value

PASS

The periodized square is a natural exact spectral multiplier, but its extremal locations do not follow from positivity or the painless reduction. The sign decomposition settles the whole interval for all orders, yielding computable optimal stability constants and a sharp exponential measure of near-tightness, rather than finite-grid estimates or just frame existence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
