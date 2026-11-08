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

The hemisphere multiplier equals (1+sign x1)/2. Under O(d-1), its compressed sign operator exchanges parity sectors: a 3x3 scalar block has eigenvalues 0,±s0 and d-1 vector pairs each ±s1, while tangential traceless quadratics contribute zeros. Gamma/Beta moments give s0=dμ_d sqrt((3d+5)/2)/(d+1), s1=dμ_d sqrt(d+2)/(d+1), μ_d=Γ(d/2)/(sqrt(pi)Γ((d+1)/2)); all multiplicities sum to d(d+3)/2. Independent generalized moment-matrix diagonalization matched the closed formula for d=3..6 at max 8.7e-16; d-step algebraic inequalities and asymptotic gamma ratio establish limits analytically.

## originality

PASS

Spherical Slepian cap matrices and hemisphere reflection symmetry on S² are prior work; particularly centered half-energy modes are known, including a related Resultary half-energy multiplicity report. Neither the d=3 example nor the abstract parity law supplies the explicit noncentral eigenvalues for every d>=3 and the sharp dimension-uniform conditioning law in the primary material inspected.

## value

PASS

A complete low-degree sphere-of-arbitrary-dimension spectrum gives exact conditioning and top extremizers for hemispherical sampling; it unifies finite-dimensional representation-block structure and provides a benchmark for Slepian localization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
