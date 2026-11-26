# Independent mathematical audit

## correctness

PASS

The resonance straddles the single minimum, so 0 < nx_n < y_B. Comparing f_B(y/(n+1)) with f_B(y/n) at y=nx_n brackets the next short-wave wavenumber strictly between nx_n and y_B; taking the increasing limit gives y_B. For the Taylor inversion, f_B(t)-1=t tanh(t)(B-g(t)) with g(t)=(t coth(t)-1)/t². The sign of t³ sinh²(t)g'(t) is that of cosh(2t)-1-(t/2)sinh(2t)-t², whose series starts in degree six and has strictly negative coefficients thereafter. Thus f'_B(y_B)>0 and Taylor inversion first for nx_n and then division by n gives the stated n^-3 correction and O_B(n^-5). At criticality y_B→0 and y_B²=45δ(1+O(δ)) from its root equation. Dividing the difference of the two even Taylor series by (nx_n)²-x_n² leaves an O((nx_n)^4)=O(δ²) remainder with an n-independent bound, giving the uniform critical claim. For the weak-tension limit write α=nB and use the sign of the exact matching residual at test x: the limits of F/(n-1) at x=c/√α for α→0, F/n at x=c for α→α₀∈(0,∞), and BF at x=c/α for α→∞ are respectively 1-c², tanh(c)-α₀c² and c-c². Each gives two-sided bracketing, and the monotone profile tanh(x)/x² has the required two edges. Compactifying α covers every possible sequence that could violate the supremum claim. This is an analytic audit; verify.py was inspected, not run, and its reported 329 floating-point tests are not used as evidence of uniform convergence. Only linear phase-speed matching is certified by this reasoning.

## originality

PASS

The matched-root branch, existence and uniqueness, and decrease of the fundamental root were already known. The supported distinction is the joint quantitative description of the short and fundamental wavelengths, in particular the relative weak-tension limit across all n with nB variable. Bounded statement-level comparisons support that distinction, not an absolute priority claim.

## value

PASS

The short-wave limit and approach identify a physical wavelength that persists as the fundamental wavelength diverges. More importantly, uniformity across harmonic orders resolves how the dispersion matching switches between two different weak-tension scalings and makes the critical coefficient useful without fixing n first. This is a meaningful distinction for selecting resonant linear wave modes, not a claim about nonlinear existence or stability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
