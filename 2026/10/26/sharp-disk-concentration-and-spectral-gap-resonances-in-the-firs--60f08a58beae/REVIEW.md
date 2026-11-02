# Independent mathematical audit

## correctness

PASS

Complex Hermite basis Φ0=bar z, Φ_n=(z^n bar z−nz^{n−1})/√n! has distinct angular frequencies and Gaussian normalized norms. Disk Toeplitz eigenvalues are λ0=1−e^(−x)(1+x), λn=(1/n!)∫0^x e^(−t)t^(n−1)(n−t)^2dt (n≥1), tending0. Adjacent difference equals −e^(−x)x^n(x−n)(x−n−1)/(n+1)!, proving eventual decrease but possibly a remote bump. A Gamma-density comparison f_n(n+s)>f_n(n−s) excludes remote maxima by λn(n)<1/2 for n≥1, while elementary exponential bounds show λ0(x)>1/2 for x≥2 and λ1(x)>1/2 for x≥3. Comparing λ2−λ0=−(1/2)e^(−x)x²(x−1) and λ1−λ3=(1/6)e^(−x)x(x−2)(x²−3) proves all-radius leading/second distinct indices, with ties at x=1,2. The optimal gap is their difference and Parseval proves sharp equality exactly in their eigenspace sum. Independently checked 16 radii over 75 modes plus 25 adjacent identities/radius (464 tests). Infinite ranking relies on the Gamma bound, not the finite samples.

## originality

PASS

Maximenko–Tellería-Romero 2019 Section 6 Proposition 6.3 gives the general Laguerre radial Toeplitz eigenvalue integrals (including this disk by specialization), but does not rank them globally or compute optimal first-Hermite gap. Abreu–Speckbacher 2018 Section 5 discusses sharp disk concentration explicitly for Gaussian h0 and local Hermite large-sieve bounds; different window and no first-excited two-resonance phase diagram. Analytic specializations alone do not supply the nontrivial global spectral ordering; possible older Laguerre/Gamma study remains a risk.

## value

PASS

The first non-Gaussian Hermite window is a natural next case after Gaussian concentration. This identifies exact optimal signal modes at every disk radius, a triple top-eigenspace at x=1, and a sharp stability constant and equality directions, including the runner-up resonance at x=2. It is more useful than simply restating diagonal integrals.

The dated certificate retains the supplied scientific assessment, sources and limitations.
