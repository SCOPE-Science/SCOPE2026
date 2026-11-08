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

Frame is Parseval by Fourier orthogonality. Erasure operator I-(2m)^(-1)AA*, so worst lower eigenvalue reduces to max Gram eigenvalue. Parity unitary gives pure-parity 2x2 block L_plus=(9+sqrt(9+8|T|²))/2 and mixed tridiagonal B(t). Root projection selects consecutive same-parity sites; Sylvester minors (2,4,12), (2,2,4), (3,4,14) prove strict mixed bound; m=3 noninjective two cases, m>=4 all retained frames positive. Independent full all-triple computation m=3..12 verifies equality counts and values; proof is all-m.

## originality

PASS

The sharp Nyquist three-character worst-mask spectrum is a distinct quantifier from known two-character erasure formulas and three-row full-spark results, with older bandpass literature retained as material priority risk.

## value

PASS

Sharp uniform reconstruction conditioning, phase-specific worst masks and exact finite threshold for a canonical three-character/aliasing Fourier system provide motivated exact sampling-design facts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
