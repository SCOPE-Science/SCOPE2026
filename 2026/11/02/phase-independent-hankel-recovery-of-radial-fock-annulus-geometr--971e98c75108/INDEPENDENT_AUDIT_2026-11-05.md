# Independent mathematical audit

## correctness

PASS

For L>0, 0<ρ<1, a mod L, the exact Fock monomial eigenvalue is gamma expectation λ_n=(1/n!)∫_0^∞g(u)e^{-u}u^n du. Fourier mask coefficients c_m=[sin(πmρ)/(πm)]exp[−im(πρ+2πa/L)] and gamma transform q_m=(1−2πim/L)^−1 imply absolutely convergent λ_n−ρ=Σ_{m≠0}c_m q_m^{n+1}, with error O(r₂^{n+1}) after m=±1. Two-conjugate geometric terms produce exact Hankel H_n=−4|b|²r^{2n+4}sin²θ[1+O((r₂/r)^n)]; since b≠0, sinθ>0, it is eventually negative. The H ratio tends r², yielding L=2π/sqrt(R^−1−1), and two successive calibrated deviations recover complex b then a modulo L. Valid for all L and interior duty ρ, not noisy spectra or ρ=0,1. Independent high-precision Fourier-gamma recreation at L=1.7,ρ=.31,a=.72 recovered L to 3.22e−11 at n≈32, H<0. The frozen checker.py was inspected; its finite assertions are not the proof.

## originality

PASS

Proposition 3.4 of Esmeral García–Maximenko 2025 (full article and exact page inspected) already states broad injectivity of bounded radial symbols from all sufficiently high gamma moments. This covers uniqueness as a corollary and must not be called new. The retained claim is stronger constructive explicit inversion of single-arc periodic mask using a universally negative 2×2 Hankel determinant with a geometric error; this algorithm and coefficient were not found in materially read primary results. Related Knutsen periodic annuli and radial Toeplitz diagonalization are prior; a disguised Prony/exponential fitting formula could precede the method and remains risk.

## value

PASS

A sign-definite phase-blind diagnostic resolves oscillatory first-mode cancellations and directly identifies period before reconstructing duty and placement. This is a natural exact, constructive inverse spectral invariant for physically motivated periodic radial masks. Finite noisy conditioning is expressly not claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
