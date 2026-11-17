---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-09.md",
      "INDEPENDENT_AUDIT_2026-11-09.json"
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

From two fully occupied CTMCs, independently constructed 7-state transient generators using unit extinction and path rate 3r/2 vs triangle rate r. Symbolic reduction to 3- and 5-state chains yields Ltri=6/Dtri and Lpath=6(2r+s+1)(3r+s+2)/Dpath, difference =3r^2s*positive_polynomial/(2Dtri Dpath)>0. Nonsingular M-matrix ensures denominators positive. Analytic s→0 gives positive mean gap and Q^5 expansion gives 3r² t^5/80, not pointwise survival dominance. Independently checked determinant, resolvent, mean and fifth-order coefficients with SymPy.

## originality

PASS

The all-exponential-deadlines strict Laplace-order rational identity for fully occupied three sites with fixed sum of edge rates is not implied by the inspected discrete-generation metapopulation paper, broad random-network persistence paper, or same-day three-path within-topology budget optimization. Finite special-case exact result remains best-of-knowledge original.

## value

PASS

Equal-budget network architecture cannot be compared by edgewise attractiveness; the exact strict Laplace-transform order at every exponential horizon is a motivated, useful finite ecological/contact-process topology benchmark, stronger than an isolated mean computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
