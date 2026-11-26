---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

For fixed d<1 the two endpoints are distinct and transverse. The critical chord density gives weights (ts)^((α+1)/2) and kernel singularity order α+2; replacing the denominator by its linear part incurs a relative O(t+s) error since its real part is bounded below by cos(φ)(t+s). The error is bounded by a constant times (ts)^((α+1)/2)/(t+s)^(α+1) and is Hilbert–Schmidt, as are the off-endpoint pieces. Logarithmic conjugation gives the claimed cosh kernel and the beta integral gives 2^(α+1) times the gamma quotient, with an exponential tilt of either sign according to orientation. For fixed angle the positive symbol has image (0,C] and closure [0,C]; only the closure includes zero, despite the compressed wording at frozen line 52. The half-line compression is bounded and positive, and long translated plane-wave packets give the essential spectrum. One can justify boundedness of restriction by the kernel Gram form of the adjoint on compactly supported chord test functions and then duality. Polar decomposition transfers nonzero essential spectra, and closedness includes zero. Independently, mapping the two endpoints to 0 and ∞ in a half-plane takes the chord to a single ray of angle ±arcsin d; the arclength, target density and Bergman isometry factors cancel exactly, yielding the same homogeneous trace kernel on the entire ray, hence the same symbol on the full logarithmic line. Derivation: /workspace/chord-proof-check.md. With s=α+1>0 and δ=π−2φ, uniform large-frequency Stirling reduces the maximum to y^s exp(−δy) at y=s/δ, while bounded frequencies contribute zero in the limit. Since cosφ~δ/2 the limit is 2π(s/e)^s/Γ(s+1). At α=d=0 the multiplier 2πξ/sinh(πξ) has maximum 2. The frozen numerical script evaluates example maxima from the symbol formula; it is not an independent derivation of the Fourier identity or an infinite-dimensional certificate.

## originality

PASS

The supported distinct content is the critical power-weighted analytic chord family at nonzero incidence, including the sharp grazing limit. There is strong prior model overlap: the centered real-power Hankel symbol is known and Merzon–Sadov diagonalize an explicitly tilted Laplace ray Gram operator, with a grazing norm limit, at denominator power one (the excluded Hardy endpoint in the equivalent model). Neither read theorem covers the combination of nonzero tilt, the higher denominator power and the critical ray weights for α>−1. The multiplier method, the angular tilt as a general mechanism, and the diameter case are not credited as new.

## value

PASS

The critical trace has a natural noncompactness invariant that general trace bounds do not determine. The theorem identifies it at each oblique incidence and shows quantitatively why decreasing chord length does not force it to vanish: the controlling frequency escapes to order (π−2φ)⁻¹, and the boldface limiting constant persists at the critical weight. This is a sharp geometric degeneration result, not just repetition of the centered Hankel calculation or of an unweighted ray transform. The degenerate chord itself is not part of the assertion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
