---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

From the two one-variable reproducing kernels, restrict the full tensor kernel along (z,e^{iθ}z), then apply the coordinate swap projection P+=(I+U)/2. This yields a diagonal positive kernel with coefficients (c_n(2r)+C_n^(r)(cos θ))/2, normalized by c_n(2r). For θ in (0,π), positivity is strict because adjacent contributing phases differ, while Darboux expansion at e^{±iθ} gives λ_n−1/2=β n^(−r) cos((n+r)θ−πr/2)+O(n^(−r−1)). Rational phases use period classes, irrational phases use Weyl equidistribution; the scaled exceedance count N(t)~β^(1/r) M t^(−1/r) implies ordered s_k~βM^r k^(−r) and Schatten iff p>1/r. Endpoint θ=0 gives identity, θ=π gives even projection, neither centered operator is compact. Independently checked 352 weighted kernel row identities and 79 Hardy identities; for r=1 and θ=π/2 the ordered constant tends to 1/4 (k=500: 0.25025025). Asymptotic requires the analytic two-singularity transfer and counting, not finite tests.

## originality

PASS

Relevant quotient-domain and symmetrized-polydisc Toeplitz papers analyze representation decomposition and operator kernels, not an ordered singular-value limit of a twisted curve trace. Gegenbauer Darboux estimates and Weyl are standard inputs, and the claim is a specific, non-implied spectral compression with an arithmetic coefficient; possible equivalent harmonic-analysis formula remains an originality risk.

## value

PASS

The symmetric analytic-kernel trace is a natural Hilbert-space restriction/compression. Quantifying its exact compact spectral defect yields sharp approximation numbers, optimal weak Schatten order and a logarithmic critical residue. The rational-vs-irrational phase mean is a nontrivial arithmetic effect invisible from the ordinary decay exponent; this is more than a normalization of a known Toeplitz estimate.

The dated certificate retains the supplied scientific assessment, sources and limitations.
