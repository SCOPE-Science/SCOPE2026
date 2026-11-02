# Independent mathematical audit

## correctness

PASS

Eliminated x=(A+kI)^-1(v+f) and u=A(A+kI)^-1v-k(A+kI)^-1f to recover the exact transformed Hessian. Orthogonal diagonalization yields g_k(t)=sqrt(1+alpha t^2)/(t+k) with derivative sign alpha k t-1, hence largest spectral mode at an endpoint. The ratio g_k(a)/g_k(b) decreases strictly in k from >1 to <1 and crosses once at k_*; for any fixed distinct eigenvalue the endpoint-versus-interior ratio decreases before k_* and increases after, so the maximum of these ratios has a unique minimizer even for exactly two eigenvalues. Angle theta=atan(sqrt(alpha)t) and phi=atan(sqrt(alpha)k_*) converts g_k to a reciprocal sine, giving the endpoint-equality midpoint sine bound; a third eigenvalue c_* realizes equality, and the two-endpoint matrix yields kappa=1. k_*=1/sqrt(alpha) iff alpha ab=1. Reconstructed endpoint ratio and tested 900 fresh random finite spectra plus exact three-mode bound; finite tests not substitutes for derivation. Handles singular a=0 and every alpha>0.

## originality

PASS

Preuster, Schaller, Schiela and Stoll 2026 full public preprint section 3.1 explicitly gives the general transformed governing operator and a bound (Proposition 3.3, equation 16), and section 4.2 tunes that bound in an elliptic example. This claim specializes to fully observed symmetric PSD spectra and minimizes the ACTUAL finite-spectrum condition number, not an abstract upper bound. Wang–Chen–Sun 2023 and Pearson–Wathen 2012 establish matching-preconditioner shifts and factor-two-like bounds, which are credited; no inspected theorem implies the unique freely tuned scalar spectral minimizer and sharp three-mode endpoint envelope. The equivalence risk from matched Schur-complement literature persists.

## value

PASS

This is a sharp optimization of a practical, natural free scalar feedback parameter that differs from the standard matched shift unless alpha ab=1. The explicit optimal gain, uniqueness, singular-PSD boundary and tight <2 spectrum-sensitive envelope provide a concrete control/preconditioning design fact; it does not claim to optimize computational solve time or arbitrary feedback matrices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
