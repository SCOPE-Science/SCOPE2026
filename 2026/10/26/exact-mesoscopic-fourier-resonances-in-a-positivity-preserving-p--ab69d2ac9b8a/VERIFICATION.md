---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Reconstructed four diagonal displacement shifts from Eq.22 with h=1/k² and N=k² per axis: sqrt(h)=k/N, so bilinear interpolation is nodal and P_k=1/4 sum of shifts (±k,±k). Characters on Z_N² have eigenvalue cos(2πa/k)cos(2πb/k); residue lifting counts +1 with multiplicity k² for odd k, 2k² for even k. The minimum symbol is -cos(π/k) for odd k and -1 for even k; A=I-P/(1+r/k²) is SPD M-matrix, with exact kappa2=1+(1+b_k)k²/r. For k≥3 the resolved mesh-dependent cos(2πkx) has continuum solution Q/(r+2π²k²) and exact discrete solution (1+r/k²)Q/r, so grid max error→1/r. Independently enumerated multiplicities/extrema for k=2..11; all-k proof is Fourier arithmetic, not those samples.

## originality

PASS

Best-of-knowledge comparison by mathematical implication, using actual Resultary search, relevant primary source material, the assigned final claim, and explicit residual priorities. The contribution is limited to the exact special calculation/structural theorem; general underlying methods are credited.

## value

PASS

Exact nonconstant undamped modes of growing multiplicity and exact nonconvergent response to a physically resolved mesh-dependent source expose an instructive arithmetic resonance in a genuinely positivity-preserving elliptic solver. Distinguishes positivity and fixed-datum consistency from uniform spectral damping; the precise k² grid and parity are naturally compelled by displacement/mesh commensurability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
