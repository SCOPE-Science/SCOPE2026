---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Checked the unitary Fourier and unnormalized surface-area factor (2π)^{d/2}; the exact Weber–Schafheitlin integral M_{ν,p}=Γ(p−1)Γ(ν+1−p/2)/[2^{p−1}Γ(p/2)^2Γ(ν+p/2)] gives A_pν^{1−p}. Debye oscillatory asymptotics away from y=1, normalization/tightness, and shifted moments show Bessel-square mass approaches the y>1 law; Potter bounds handle arbitrary measurable slowly varying L. Fixed-frequency cos/sin terms vanish by nonstationary/van der Corput estimates including possible isolated stationary points; the e(r)=o(1) contribution vanishes. The coefficient for the μ=λ Wendland endpoint agrees after gamma duplication, without using finite tests as an infinite proof. Independently quadrature-checked three squared-Bessel gamma moments.

## originality

PASS

The 2021 Hubbert–Jäger preprint already prints the special Wendland formula as Theorem 5.9, and the 2023 peer-reviewed paper records even d as Conjecture 5.10; no novelty is attributed to wording of that special-case formula alone. The assessed result is the strictly wider Bessel-square transfer for arbitrary measurable slowly varying envelopes and persistent nonzero-frequency modulations. Classical Weber–Schafheitlin and Debye are credited as ingredients, not new theorems. Actual primary sections were compared; no checked theorem asserts the all-tail transfer.

## value

PASS

A mathematically natural Abelian transfer mechanism computes exact spherical Fourier decay constants even when Euclidean density has no pointwise asymptotic ratio due to fixed oscillations. The explicit Mellin constant feeds radial-kernel Sobolev equivalence and spherical covariance spectra; even d in a published Wendland conjecture is a nontrivial special application. Not merely rephrasing the 2021 special-case formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
