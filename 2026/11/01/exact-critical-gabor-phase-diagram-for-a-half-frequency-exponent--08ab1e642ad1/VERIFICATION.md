---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-01.md",
      "INDEPENDENT_AUDIT_2026-11-01.json"
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

PASS. For r=e^(−λ)∈(0,1) Zak diagonalization on the unit critical lattice yields scalar symbol r^x[(1−rz)^−1+c e^(πix)(1+rz)^−1]. A strictly convex endpoint upper envelope gives sharp B; monotone reverse-triangle envelopes give sharp lower frame bounds outside [(1−r)/(1+r),(1+r)/(1−r)]. The modulus equation for zero reduces to a strictly monotone correlation ratio and a unique phase with Im(z)<0, giving one x∈(0,1), ω∈(0,1/2) for interior coefficients and limiting zeros at both endpoints. Sharp A vanishes exactly on the closed gap and recovers quadratically; |Zak|² has interval essential range and no level sets of positive measure by nonconstant real analyticity. Independently evaluated a 371×967 grid for seven coefficient regimes at r=0.43, including sharp extremal limits and near-zero regions; this is supplementary, the inequalities establish the quantifiers.

## originality

PASS

PASS, best knowledge. Faulhuber–Shafkulovska 2022/2023 derive sharp constants for single one-sided exponential windows, but not for their coherent half-integer frequency superposition; frame properties of summands do not imply those of the sum. Kloos–Stöckler treat totally positive/spline windows, whereas this two-tone window is complex oscillatory. Related published Gabor findings optimize spline, shifted-sampling, or Fock windows, without a documented same-window coefficient phase diagram. General Zak analysis is known and expressly credited.

## value

PASS

PASS. Stability of a coherent sum of two individually critical Riesz generators is a natural frame-theoretic question; the exact nonframe interval, moving unique Zak zero, optimal bounds and sharp quadratic onset classify a genuine full-parameter obstruction rather than a routine single-window substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
