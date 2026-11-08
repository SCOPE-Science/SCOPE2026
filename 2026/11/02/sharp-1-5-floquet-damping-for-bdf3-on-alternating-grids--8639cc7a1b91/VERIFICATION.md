---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

Recomputed the BDF3 coefficients directly from four-node cubic Lagrange interpolation, the two companion matrices, and their reduced quadratic z^2-T(r)z+E(r). The three scaled Schur-Jury expressions equal strictly positive coefficient polynomials divided by Delta(r) for every r>0; endpoint limits give the unattained optimal 1/5 parasitic two-step radius. The discriminant is r^4 F(r+1/r)/Delta^2 with F(u)=u^4-22u^3-173u^2-390u-279, one root u>2 by Descartes and endpoint signs; it yields reciprocal mode-transition ratios. The eigenvalue 1 is simple, while both parasitic eigenvalues are strictly damped, implying uniform-in-step-number homogeneous zero stability for each FIXED positive alternating r. Independently recreated exact symbolic identities in independent_checks.py; finite example ratios are not the all-r proof.

## originality

PASS

Compared the exact two-periodic Floquet spectrum and all-positive-r stability, not simply variable-step BDF3 titles, against the joint-spectral-radius general-step work and modern ratio-restricted/smooth-grid stability theorems. The exact sharp 1/5 radius and reciprocal real/complex transition are not implied by inspected ratio-bound results. Guglielmi-Zennaro full text was unavailable and an equivalent periodic calculation cannot be ruled out.

## value

PASS

Arbitrarily large alternating adjacent-step jumps constitute a natural test family for the fragile zero stability of higher BDF methods. The unrestricted r>0 exact damped spectrum and mode-transition threshold isolate a precise structural phenomenon beyond smooth grids or one-off numerical examples. It gives a useful sharp benchmark, without asserting global variable-step or forced-equation stability.

The dated certificate retains the supplied scientific assessment, sources and limitations.
