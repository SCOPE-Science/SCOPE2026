---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification details

The exact shift weights are derived from \(\int_{\mathbb D}|z|^{2j}dA=1/(j+1)\). For every positive integer \(m,N\), each consecutive weight product belongs either to a one-sided telescoping chain or a unique crossing chain. The proof's strict-log-convexity inequality gives the maximizer over all crossing residues without relying on numerical interpolation. The remaining discrete quadratic has exactly one maximizer when \(N\) is even and two when \(N\) is odd.

The accompanying `VERIFY.py` uses only Python standard-library `fractions.Fraction`, reconstructs squared weights without floating point, independently multiplies forward paths and checks the exact claimed inverse-power norm and all inverse-domain equality indices for \(1\le m\le20\), \(1\le N\le13\). Additional rational checks compare every crossing path against endpoint values. These computations validate individual finite cases, not the general inequality or the infinite-dimensional spectrum by themselves.

Proof-dependent but separately stated scope limits: no norm formula for arbitrary polynomial symbols, no extension to weighted harmonic Bergman spaces, no full pseudospectral characterization. The publication-priority assessment is a same mathematical model literature comparison, not an independent external certification.
