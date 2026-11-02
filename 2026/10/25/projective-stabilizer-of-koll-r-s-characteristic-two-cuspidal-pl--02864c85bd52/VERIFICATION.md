---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

The primary curve has unique cusp at [0:1:0] and unique tangent Z=0, so every geometric projective stabilizer fixes both and acts affinely by x->Ax+C, y->Dx+By+E. The primary parametrization t->(t^q,t^(q+2)+t) identifies the affine curve with A1, whose automorphism must be t->at+b. Comparing x yields A=a^q, C=b^q. In char2, (at+b)^(q+2) contains exponents q+2,q,2,0. The t² coefficient b^q a² has no left-hand mate when q>=4, forcing b=0. Remaining coefficients give B=a and a^(q+1)=1, D=C=E=0. Conversely these diagonals preserve the equation; odd q+1 has simple roots. Independent parity expansion checks q=4..256 verified every relevant exponent, finite confirmation of a universal coefficient argument.

## originality

PASS

Kollar 2026 builds the characteristic-two rational plane-curve family and proves its affine normalization and unique double cusp; he does not state this exact geometric PGL3 stabilizer in the inspected primary text. Full stabilizer of a fixed embedding is strictly more constrained than Aut(A1), and unrelated known stabilizers of other cuspidal curves cannot imply it. Novelty is best-of-knowledge and excludes group scheme or abstract curve automorphisms.

## value

PASS

The exact projective symmetry group and obstruction to translations are a natural invariant distinguishing this unusual large-degree positive-characteristic embedded curve from its highly symmetric affine normalization. An infinite-parameter complete group classification is independently useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
