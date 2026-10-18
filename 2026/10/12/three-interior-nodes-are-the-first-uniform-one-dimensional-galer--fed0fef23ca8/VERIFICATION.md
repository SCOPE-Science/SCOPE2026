---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Uniform P1 consistent-mass and stiffness matrices M=hT/6,S=K/h give H=h²M^-1S=6T^-1K. N=1 gives e^(-3τ)>0; N=2 generator −H Metzler irreducible, giving strictly positive matrix exponential. At N=3 independently verified H has diagonal (51/14,30/7,51/14), adjacent −18/7 and corner +9/14, with eigenvalues (30±18sqrt2)/7 and 3. Sine spectral projectors yield E13=(e^(−λ1τ)+e^(−λ3τ))/4−e^(−3τ)/2; nearest couplings (sqrt2/4)(e^(−λ1τ)−e^(−λ3τ))>0, diagonals positive. Sign of E13 equals sign of g(τ)=exp((3−λ1)τ)+exp(−(λ3−3)τ)−2: g(0)=0,g'(0)<0,g''>0, g→∞; unique positive crossing τ*=0.212811776921..., so failure precisely (0,τ*h²) and strictly positive after. Independently checked exact rational matrices/SymPy eigenvalues, scipy exponentials and high-precision root. No extrapolation to N≥4.

## originality

PASS

Standard consistent-mass Galerkin failure at small times and eventual positivity were shown by Thomée and collaborators. The inspected open primary subdiffusion paper states general phenomena and gives higher-dimensional numerical thresholds, not the exact minimal uniform one-dimensional N=3 classification or explicit τ*. Closely relevant 2015 CMAM source could not be read in full; residual risk explicitly preserved. A Resultary indexed three-spectral-level positivity barrier is broader abstractly but does not fix this FE matrix or provide the least interior-node threshold.

## value

PASS

Provides a uniquely minimal, fully explicit one-dimensional consistent-mass heat semigroup example and exact scale-free positivity return time, useful as a reproducible benchmark for schemes, mass lumping and positive semigroup tests. This is a motivated sharp finite boundary rather than an arbitrary small-matrix curiosity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
