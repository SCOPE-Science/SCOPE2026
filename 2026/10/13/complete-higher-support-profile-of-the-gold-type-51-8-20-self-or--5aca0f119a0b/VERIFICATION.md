---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Independent polynomial multiplication and reduction modulo 0x11d verified the period 255 of alpha, evaluated all trace constraints, and found 51 points, with norm exponents 0,6,13 modulo 15. The explicit trace generator is injective and its binary Gram matrix vanishes. Independent hyperplane/coset generation of all 417,198 positive-dimensional subspaces and support calculation by word-weight sums reproduced each bin, the hierarchy (20,30,38,42,46,48,50,51), and the minimizer counts (34,34,323,17,510,85,51,1). The revised self-orthogonality proof using weight divisibility by four is valid.

## originality

PASS

The trace construction and ordinary-weight theory are prior context. The inspected related claims handle other exact codes or different ranks/constructions and do not give the full support census of the specified two-trace code.

## value

PASS

The two-coefficient Gold construction supplies a natural rank-two case distinct from the collapsed rank-one examples. The exact table gives extremal frequencies and all possible intermediate unions, e.g. 17 four-spaces at support 42 out of 200,787. It is a reproducible reference for how this small self-orthogonal code behaves beyond ordinary weights, without implying a rank-two family theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
