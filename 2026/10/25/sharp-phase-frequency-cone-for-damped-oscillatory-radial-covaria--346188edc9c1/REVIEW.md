# Independent mathematical audit

## correctness

PASS

The radial Fourier transform of e^{-zr} for Re z>0 is c_d z/(z²+ρ²)^((d+1)/2). For z=α−iω, multiplying by (1−iβ) and taking real part gives the exact spectral density. The continuous argument θ(ρ)=Arg(z²+ρ²) rises from −2φ to 0, so the spectral cosine argument decreases from dφ−arctanβ to −φ−arctanβ, a total sweep (d+1)φ. Pointwise nonnegative spectrum is equivalent to the phase interval lying in [−π/2,π/2], yielding φ≤π/(d+1), −cot(dφ)≤β≤cotφ. Strict positive definiteness on distinct sites follows from positive density on an open annulus; boundary α=ω=β=1,d=3 has explicit spectrum 64πρ²/(ρ⁴+4)², and d=4 fails frequency threshold. An independent exact symbolic d=3 identity and 600 numeric spectral sign cases confirmed formulas; continuity/all-d proof is analytical.

## originality

PASS

Classical Schoenberg/Bochner theory establishes spectral positivity criteria, and RandomFields RMdampedcos gives the β=0 slice α/ω≥cot(π/(2d)); these do not state the full real-β frequency–phase cone. Schubert et al (2020) study damped oscillatory temporal ARMA covariance, not arbitrary-dimensional radial extension. The complex Laplace/Fourier transform is standard, and a radial harmonic phase result elsewhere remains a priority risk. The assessed increment is the necessary-and-sufficient full cone including sharp endpoint and strictness.

## value

PASS

Provides an exact admissible covariance family in every Euclidean dimension with a tunable damping-phase parameter, endpoint behavior, strict kernel definiteness and a 3D-but-not-4D explicit witness; useful in spatial covariance design beyond the known damped-cosine subfamily.

The dated certificate retains the supplied scientific assessment, sources and limitations.
