---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

For 30 unit vertices choose 15 antipodal representatives; K_k=P_k(dot) is real PSD and condition numbers are restricted to positive-definite degrees. The exact dot-product classes 0, (sqrt5−1)/4, 1/2, (sqrt5+1)/4 and rank-five zero-dot-product projection split K12 into multiplicities 1+4+5+5; the quadratic on the rank-ten complement gives min≈0.00284858 and max≈2.57695484, ratio≈904.6444977. The inspected h3_cert.py uses exact Q(sqrt5) recurrence, checks K12 projection identities, and performs 490 degree-by-degree integer Bareiss positive-definiteness certificates for 7,9,10,11,13 and 15..499. The source proof bounds k≥500 by a Legendre Laplace integral and Gershgorin, showing kappa<199; finite checks alone are not an all-k proof. Independent construction of 30 Cartesian vertices and SciPy P12 Gram for 15 representatives gives the claimed spectrum and kappa=904.64449771351. Boundaries k=0..14 rank are distinguished; k=14 remains singular.

## originality

PASS

Best-of-knowledge PASS for sharp degree-uniform icosidodecahedral Legendre condition-number extremum, as distinct from harmonic-index designs, irrep ranks and icosahedral coordinates; qualified by inaccessible historical harmonic tables.

## value

PASS

A fixed highly symmetric spherical sampling design has a natural conditioning invariant beyond mere rank. A unique nontrivial worst degree over an infinite sequence, rigorous positive spectral gap comparisons and exact sharp extremal spectrum provide a reusable benchmark for harmonic interpolation; this is not just a renamed rank table or one tiny numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
