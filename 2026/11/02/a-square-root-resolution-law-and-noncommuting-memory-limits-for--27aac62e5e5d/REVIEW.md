# Independent mathematical audit

## correctness

PASS

The stationary lag-k covariance is e^{-αh|k|} exp(kωhJ) plus τI at lag0; in the circular polarization basis, spectra are f±=τ+g(φ∓θ), g(φ)=(1-r²)/(1−2r cosφ+r²). Gaussian block KL between forward and order-reversed paths has a trace ratio formula with determinants equal, and absolute covariance summability plus a positive spectral floor justify the Toeplitz-to-circulant per-step limit. The frequency integral (1/4π)∫(f+−f−)²/(f+f−) equals the stated closed expression by Fourier convolution of Poisson kernels. Independently integrating this spectral ratio numerically matched the closed form at nonresonant parameters. For τ>0, Puiseux expansion of K=sqrt(c[4τ+c(1−τ)²]), ν=2τe^-2αh/(c+τ(1+e^-2αh)+K), and sin²θ gives Eτ/h=2ω²/α[1−(3/2)sqrt(2ατ)sqrt h+O(h)]; independent high-resolution checks agree. At each fixed m, Σ_m(0)=11^T⊗I+τI positive, forward/reverse covariance difference O_m(h), hence Gaussian KL quadratic O_m(h²). For τ=0, exact E0=4e^-2αh sin²ωh/(1-e^-2αh), with linear h correction. All limits keep α>0, ω≠0 and τ>0 fixed before h→0.

## originality

PASS

The Gaussian pathwise entropy and Kalman innovations machinery, OU housekeeping production, and noise-induced memory are established prior art. The precise all-history rotational OU spectral expression, leading sqrt(h) deficit coefficient and order-of-limits contrast do not appear in inspected primary statements. Broad Gaussian state-space approaches may imply the expression by specialization; this is a residual priority risk.

## value

PASS

This precisely resolves a natural statistical-thermodynamics sampling paradox: arbitrarily fine short-memory observations lose physical-time arrow-of-time signal under fixed sensor noise even as the entire noisy time history recovers the full diffusion housekeeping production. The explicit nonanalytic 3/2 coefficient quantifies a resolution cost not available from generic memory bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
