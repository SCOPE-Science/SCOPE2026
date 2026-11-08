# Independent mathematical audit

## correctness

PASS

PASS: With unnormalized dA and 4/π weight (1−|z|²)^3, orthogonality gives E_N=Σ_{m≥1}w_m|Σ_j exp(imθ_j)|², w_m=24/[m(m+1)(m+2)(m+3)], and a_m=m² w_m. Differentiation termwise valid since Σm²w_m<∞, Parseval yields circulant Hessian λ_k=N(A_{k,N}+A_{N−k,N}−2A_{0,N}), λ_0=0, with correct conjugate frequency pairing. a_m decreasing and discretely convex with exact first/second differences, hence all λ_k>0 and the unique minimizing one or two modes are k=floor(N/2),ceil(N/2). Hurwitz zeta sums give λmin=16π²/N−1728ζ(3)/N²+O(N^-3). Spectral Taylor gives sharp local λmin/2 on mean-zero perturbations, not a global modulus. Independently checked exact rational differences and central eigenmodes N=2..15.

## originality

PASS

PASS (best of knowledge): Corbett 2026 and Abakumov–Borichev–Fedorovskiy 2020 establish global regular-polygon minimization; the inspected Hessian discussion does not furnish this α=3 full eigenvalue formula and softening expansion. Published Resultary 2026 α=1 Fourier Hessian theorem is a distinct critical-weight regime with first harmonic least curved and order-N eigenvalue, whereas the cubic regime has Nyquist minimum and order N^−1 curvature.

## value

PASS

PASS: The sharp all-N spectrum and high-frequency least-stable mode identify a genuine local stability transition beyond global minimization; explicit asymptotic softening is a natural quantitative invariant for boundary-pole energies.

The dated certificate retains the supplied scientific assessment, sources and limitations.
