---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

On an eigenvector, the proposed cycle keeps v constant and the momentum/parameter flip equations give the stated radius exactly. In a transverse eigenmode the first variation of the scalar squared-gradient norm vanishes by orthogonality, leaving a 2x2 block with characteristic polynomial \(z^2-(1+\beta_1)(1-2\mu/\lambda)z+\beta_1\). Jury's inequalities reduce exactly to 0<mu<lambda.

## originality

PASS

The full NovoGrad paper and official implementation define the exact update ordering used here. The paper contains no quadratic cycle analysis. Bock-Weiss proves analogous period-two cycles for Adam, but Adam's coordinatewise moment dynamics differ materially from NovoGrad's scalar layer normalization.

## value

PASS

Exact limit cycles on convex quadratics are a meaningful optimizer diagnostic. The sharp curvature ordering—lower modes damped, higher modes unstable—adds structural information specific to NovoGrad rather than a parameter example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
